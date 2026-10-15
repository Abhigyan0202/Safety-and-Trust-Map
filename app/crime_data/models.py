from django.db import models

# Create your models here.
class Region_Reviews(models.Model):
    name = models.CharField(max_length=50)
    review = models.CharField(max_length=2048)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.name

class Region_data(models.Model):
    name = models.CharField(max_length=50)
    firs = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.month} {self.year}"

