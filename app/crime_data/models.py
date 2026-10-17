from django.db import models
from django.contrib.auth.models import User

# New mapping of models

# Region_Reviews will include a User mapping
class Region_Reviews(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="region_reviews"
    )
    name = models.CharField(max_length=50)
    review = models.CharField(max_length=2048)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

# Region data along with FIR's will contain mapping of reviews as well
class Region_data(models.Model):
    region_review = models.ForeignKey(
        Region_Reviews,
        on_delete=models.CASCADE,
        related_name="region_data",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=50)
    firs = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.month} {self.year}"