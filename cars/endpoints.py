from django.urls import path
from cars.viewset import *

urlpatterns = [
    path('api/all_cars', CarSetViewset.as_view(), name="all-cars"),
    path('api/max/<origin>', CarSetMaxViewset.as_view(), name="max-cars"),
    path('api/avg/', CarSetAverageViewSet.as_view(), name="avg-cars"),


]
