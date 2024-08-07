from django.urls import path
from .views import TrainStationCreateView, TrainStationListView, train_route_view

urlpatterns = [
    path('api/train-stations/', TrainStationListView.as_view(), name='train_station_list'),
    path('api/train-stations/add/', TrainStationCreateView.as_view(), name='train_station_create'),
    path('train_route/', train_route_view, name='train_route'),
]
