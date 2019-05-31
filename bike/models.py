from django.db import models

# Create your models here.
class Bike(models.Model):
	model = models.TextField()
	seats = models.IntegerField()