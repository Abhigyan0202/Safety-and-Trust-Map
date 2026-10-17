from django.shortcuts import render
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

def map_view(request):
    return render(request, "crime_data/map.html")