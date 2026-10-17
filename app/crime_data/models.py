from django.db import models
from django.contrib.auth.models import User

class PoliceStation(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Region_Reviews(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="region_reviews",
        null=True,
        blank=True,
    )
    police_station = models.ForeignKey(
        PoliceStation,
        on_delete=models.PROTECT,
        related_name="reviews",
        null=True,
        blank=True,
    )
    review = models.TextField(max_length=2048)
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True,
    blank=True,)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.police_station.name} - {self.user.username}"

class Region_data(models.Model):
    name = models.CharField(max_length=50)
    firs = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month} {self.year}"