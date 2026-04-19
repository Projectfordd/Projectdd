import requests # Не забудь в начале файла!
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action # Добавляем это для создания кастомного пути
from .models import Road
from .serializers import RoadSerializer
from django.shortcuts import render

@method_decorator(csrf_exempt, name='dispatch')
class RoadViewSet(viewsets.ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

    @action(detail=False, methods=['get'], url_path='weather-proxy')
    def weather_proxy(self, request):
        lat = request.query_params.get('lat')
        lng = request.query_params.get('lng')

        if not lat or not lng:
            return JsonResponse({'error': 'Coordinates missing'}, status=400)

        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
        
        try:
            response = requests.get(url)
            return JsonResponse(response.json())
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
def index(request):
    return render(request, 'index.html')