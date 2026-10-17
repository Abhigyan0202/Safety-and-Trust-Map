from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('fetch_region',views.fetch_region,name='fetch_region'),
    path('', views.map_view, name="map"),
]