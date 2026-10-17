from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegionReviewForm
from .models import Region_Reviews
from django.http import HttpResponse
from .models import Region_data, Region_Reviews


def home(request):
    return HttpResponse("Welcome to Safety and Trust Map!")

def fetch_region(request):
    #ideally, this function should return both fir data, and reviews
    region = str(request.GET.get('name','POWAI')).upper()
    fir_data = Region_data.objects.filter(name=region)
    print(region)
    print("----------------------------")
    print(fir_data)
    return render(request,"crime_data/fetch_region.html", {
        "data": fir_data,
        "region": region
    })

@login_required
def add_review(request):
    if request.method == "POST":
        form = RegionReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()

            messages.success(request, "Review added successfully!")
            return redirect("profile")

    else:
        form = RegionReviewForm()

    return render(
        request,
        "crime_data/add_review.html",
        {"form": form},
    )


def search_place_reviews(request):
    query = request.GET.get("q", "").strip()

    reviews = Region_Reviews.objects.none()

    if query:
        reviews = (
            Region_Reviews.objects
            .filter(place_name__icontains=query)
            .select_related("user")
        )

    return render(
        request,
        "crime_data/place_reviews.html",
        {"reviews": reviews, "query": query},
    )


def user_reviews(request, username):
    from django.contrib.auth.models import User

    profile_user = get_object_or_404(
        User,
        username=username,
    )

    reviews = profile_user.region_reviews.all()
    total_reviews = reviews.count()

    return render(
        request,
        "crime_data/user_reviews.html",
        {
            "profile_user": profile_user,
            "reviews": reviews,
            "total_reviews": total_reviews,
        },
    )
