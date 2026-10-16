from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_picture", "bio"]

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email address",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")