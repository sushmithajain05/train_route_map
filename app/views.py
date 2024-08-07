from rest_framework import generics
from .models import TrainStation
from .serializers import TrainStationSerializer
from django.shortcuts import render


class TrainStationCreateView(generics.CreateAPIView):
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer

class TrainStationListView(generics.ListAPIView):
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer

def train_route_view(request):
    return render(request, 'train_route.html')