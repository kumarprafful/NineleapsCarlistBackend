from rest_framework import serializers, generics
from cars.models import CarSet

class CarSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSet
        fields = '__all__'

class CarSetAvgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSet
        fields = []
