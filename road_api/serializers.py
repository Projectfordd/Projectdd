from rest_framework import serializers
from .models import Road  # <--- Было RoadSegment

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road  # <--- И здесь тоже Road
        fields = '__all__'