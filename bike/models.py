from django.db import models

# Create your models here.
class Bike(models.Model):
    bike_id = models.IntegerField(null=False, unique=True)
    reserved = models.IntegerField(max_length=1, default=0, null=False)
    current_owner = models.CharField(max_length=256, default="None", null=True)
    reservator = models.CharField(max_length=256, default="None", null=True)
    # moje null, ako reserved = 0 
    #0-ne e rezervirano(t.e. e svobodno), 
    #1 - rezervirano e, no ne ni interesuva ot kogo, 2- zaeto e

  
