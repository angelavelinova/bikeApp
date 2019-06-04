from django.db import models

# Create your models here.
class Bike(models.Model):
    reserved = models.IntegerField()#0-ne e rezervirano(t.e. e svobodno), 
    #1 - rezervirano e, no ne ni interesuva ot kogo, 2- zaeto e
    current_owner = models.CharField(max_length=256)# moje null, ako reserved = 0 
  
