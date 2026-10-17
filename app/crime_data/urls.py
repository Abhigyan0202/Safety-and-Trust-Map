from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fetch_region',views.fetch_region,name='fetch_region'),
    path("map", views.map_view, name="map"),
]