from django import forms
from .models import Region_Reviews


class RegionReviewForm(forms.ModelForm):
    class Meta:
        model = Region_Reviews
        fields = ["police_station", "review", "rating"]

    def clean_rating(self):
        rating = self.cleaned_data["rating"]

        if not 1 <= rating <= 5:
            raise forms.ValidationError(
                "Rating must be between 1 and 5."
            )

        return rating

    def clean_place_name(self):
        return self.cleaned_data["place_name"].strip()