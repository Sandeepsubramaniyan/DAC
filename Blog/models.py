from django.conf import settings
from django.contrib.gis.db  import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    
    
def locate(self):
    return self.name




    