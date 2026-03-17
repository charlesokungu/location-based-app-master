from django.db import models
from django.contrib.gis.db import models as gis_models

class waterfall(gis_models.Model):
    name = models.CharField(max_length=255)
    town =models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    location = gis_models.PointField()

class caves(gis_models.Model):
     name = models.CharField(max_length=255)
     town =models.CharField(max_length=255)
     address = models.CharField(max_length=255)
     location = gis_models.PointField()

class hill(gis_models.Model):
    name = models.CharField(max_length=255)
    town =models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    location = gis_models.PointField()

class spring(gis_models.Model):
    name = models.CharField(max_length=255)
    town =models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    location = gis_models.PointField()
    

    def __str__(self):
        return self.name

