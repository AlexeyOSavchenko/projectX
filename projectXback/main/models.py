from django.db import models

class Stations(models.Model):
    ids = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    coordinateX = models.FloatField()
    coordinateY = models.FloatField()
    validFrom = models.DateField()

class Observations(models.Model):
    ids = models.CharField(max_length=20)
    value = models.IntegerField()
    time = models.DateTimeField()
    fk = models.ForeignKey(Stations, on_delete = models.PROTECT)
