from django import forms
from .models import Region_Reviews

class RegionReviewForm(forms.ModelForm):

    rating = forms.ChoiceField(
        choices=[
            (1, "1 - Very Unsafe"),
            (2, "2 - Unsafe"),
            (3, "3 - Average"),
            (4, "4 - Safe"),
            (5, "5 - Very Safe"),
        ],
        widget=forms.Select(attrs={
            "class": "w-full h-14 appearance-none rounded-xl border border-slate-300 bg-white px-4 text-slate-700 shadow-sm outline-none transition focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
        })
    )

    class Meta:
        model = Region_Reviews
        fields = ["police_station", "rating", "review"]

        widgets = {
            "police_station": forms.Select(attrs={
                "class": "w-full h-14 rounded-xl border border-slate-300 bg-white px-4 text-slate-700 shadow-sm outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
            }),
            "review": forms.Textarea(attrs={
                "rows": 6,
                "placeholder": "Describe your experience...",
                "class": "w-full rounded-xl border border-slate-300 bg-white px-4 py-4 text-slate-700 shadow-sm outline-none resize-y focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["police_station"].required = True