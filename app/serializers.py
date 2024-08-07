from rest_framework import serializers
from .models import TrainStation

class TrainStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainStation
        fields = '__all__'