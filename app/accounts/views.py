from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register(request):
    # if request.user.is_authenticated:
    #     return redirect("profile")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Your account was created successfully!"
            )
            return redirect("profile")
    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


def login_page(request):
    # Django's built-in LoginView handles authentication.
    return redirect("login")


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    reviews = request.user.region_reviews.select_related(
        "police_station"
    ).all()

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form,
            "profile": profile,
            "reviews": reviews,
            "total_reviews": reviews.count(),
        }
    )

@login_required
def logout_page(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect("login")

    return render(request, "accounts/logout.html")
