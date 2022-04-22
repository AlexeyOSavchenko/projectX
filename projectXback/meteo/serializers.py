from rest_framework import serializers
from .models import Stations, Observations


class ObservationSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Observations
        fields = ('ids', 'value', 'date', 'time')


class StationSerialazer(serializers.ModelSerializer):
    observations = ObservationSerialazer(many=True)
    class Meta:
        model = Stations
        fields = ('ids', 'name', 'country', 'coordinateX', 'coordinateY', 'validFrom', 'observations')