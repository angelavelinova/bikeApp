from django.db import models

# Create your models here.
class Bike(models.Model):
    model = models.CharField(max_length=256)
    seats = models.IntegerField()