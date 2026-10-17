from django.shortcuts import render
from django.http import HttpResponse
from .models import Region_data, Region_Reviews

def home(request):
    return HttpResponse("Welcome to Safety and Trust Map!")

def fetch_region(request):
    region = str(request.GET.get('name','POWAI')).upper()
    fir_data = Region_data.objects.filter(name=region)
    print(region)
    print("----------------------------")
    print(fir_data)
    return render(request,"crime_data/fetch_region.html", {
        "data": fir_data,
        "region": region
    })

from django.shortcuts import render
from .models import Region_data

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