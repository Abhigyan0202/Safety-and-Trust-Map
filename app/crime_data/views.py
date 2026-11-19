from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Avg
from django.contrib.auth.models import User

from .forms import RegionReviewForm
from .models import Region_data, Region_Reviews
from .subs import get_substations

import math


def home(request):
    return HttpResponse("Welcome to Safety and Trust Map!")


def fetch_region(request):
    region = request.GET.get("name", "POWAI").strip().upper()

    fir_data = Region_data.objects.filter(
        name__iexact=region
    )

    reviews = Region_Reviews.objects.filter(
        police_station__name__iexact=region
    ).select_related("user", "police_station")

    total_firs = fir_data.aggregate(
        total=Sum("firs")
    )["total"] or 0

    return render(
        request,
        "crime_data/fetch_region.html",
        {
            "data": fir_data,
            "reviews": reviews,
            "region": region,
            "total_firs": total_firs,
        }
    )


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
            .filter(police_station__name__icontains=query)
            .select_related("user", "police_station")
        )

    return render(
        request,
        "crime_data/place_reviews.html",
        {
            "reviews": reviews,
            "query": query,
        },
    )


def user_reviews(request, username):
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


# MAP FUNCTIONALITY FROM BRANCH2

def getColours(request):
    substations = get_substations()
    ratings = {}

    colours = [
        "#FF0000",  # 0 - Red
        "#FF3300",  # 1
        "#FF6600",  # 2
        "#FF9900",  # 3
        "#FFCC00",  # 4
        "#FFFF00",  # 5
        "#CCFF00",  # 6
        "#99FF00",  # 7
        "#65FF00",  # 8
        "#32FF00",  # 9
        "#00FF00",  # 10 - Green
    ]

    for region in substations:
        avg_rating = Region_Reviews.objects.filter(
            police_station__name__iexact=region
        ).aggregate(
            average=Avg("rating")
        )["average"]

        if avg_rating is None:
            ratings[region] = "#cccccc"  # No reviews = gray
            continue

        # Convert rating from 1–5 into color index 0–10
        index = round((avg_rating - 1) * 2)

        index = max(0, min(index, 10))

        ratings[region] = colours[index]

    return JsonResponse(ratings)


def map_view(request):
    regions = list(
        Region_data.objects.filter(
            latitude__isnull=False,
            longitude__isnull=False,
        ).values(
            "name",
            "latitude",
            "longitude",
            "firs",
            "month",
            "year",
        )
    )

    return render(
        request,
        "crime_data/map.html",
        {"regions": regions},
    )
