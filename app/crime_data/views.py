from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Region_data, Region_Reviews
from django.db.models import Avg
from .subs import get_substations
import math
def home(request):
    return HttpResponse("Welcome to Safety and Trust Map!")

def fetch_region(request):
    region = str(request.GET.get('name','POWAI')).upper()
    fir_data = Region_data.objects.filter(name=region)
    
    # print(region)
    # print("----------------------------")
    # print(fir_data)
    return render(request,"crime_data/fetch_region.html", {
        "data": fir_data,
        "region": region
    })

def getColours(request):
    substations = get_substations()
    ratings = {}
    region = str(request.GET.get('name','POWAI')).upper()
    colours = ["#FF0000","#FF3300","#FF6600","#FF9900", "#FFCC00", "#FFFF00", "#CCFF00", "#99FF00", "#65FF00","#32FF00", "#00FF00"]
    for region in substations:
        r = Region_Reviews.objects.filter(name=region).aggregate(Avg("rating"))
        r = r["rating__avg"] or 0
        r_colour = colours[math.ceil(r)]
        ratings[region] = r_colour
    return JsonResponse(ratings)

def map_view(request):
    regions = list(
        Region_data.objects
        .filter(
            latitude__isnull=False,
            longitude__isnull=False,
        )
        .values(
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