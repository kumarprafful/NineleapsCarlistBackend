from django.db.models import Count, Avg
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from cars.serializers import *
from cars.models import CarSet

class CarSetViewset(APIView):
    def get(self, request, format=None):
        queryset = CarSet.objects.all()
        serializer = CarSetSerializer(queryset, many=True)
        return Response(serializer.data)

class CarSetMaxViewset(APIView):
    def get(self, request, format=None, **kwargs):
        queryset = CarSet.objects.filter(origin=self.kwargs['origin']).order_by('-displacement')[:5]
        serializer = CarSetSerializer(queryset, many=True)
        return Response(serializer.data)

class CarSetAverageViewSet(APIView):
    def get(self, request, format=None, **kwargs):
        q1 = CarSet.objects.filter(origin="US").values('displacement').aggregate(us_avg=Avg('displacement'))
        q2 = CarSet.objects.filter(origin="Japan").values('displacement').aggregate(jp_avg=Avg('displacement'))
        q3 = CarSet.objects.filter(origin="Europe").values('displacement').aggregate(eu_avg=Avg('displacement'))
        q1.update(q2)
        q1.update(q3)
        # serializer = CarSetAvgSerializer(queryset, many=True)
        return Response(q1)
