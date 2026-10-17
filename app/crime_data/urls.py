from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fetch_region/',views.fetch_region,name='fetch_region'),
    path("reviews/add/", views.add_review, name="add_review"),
    path("reviews/search/", views.search_place_reviews, name="search_place_reviews"),
    path(
        "users/<str:username>/reviews/",
         views.user_reviews,
         name="user_reviews",
    ),
]