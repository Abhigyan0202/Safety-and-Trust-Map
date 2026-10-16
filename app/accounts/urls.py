from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Keep your existing urlpatterns here.

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="accounts/login.html"),name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("profile/",views.profile,name="profile"),
]
