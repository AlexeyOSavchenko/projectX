from django.db import models


class Stations(models.Model):
    objects = models.Manager()
    ids = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    coordinateX = models.FloatField()
    coordinateY = models.FloatField()
    validFrom = models.DateField()


class Observations(models.Model):
    objects = models.Manager()
    ids = models.CharField(max_length=20)
    value = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    fk = models.ForeignKey('Stations', on_delete=models.PROTECT, related_name='observations')
