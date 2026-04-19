from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from road_api.views import RoadViewSet, index # Импортируем нашу функцию index

router = DefaultRouter()
router.register(r'roads', RoadViewSet)

urlpatterns = [
    path('', index), # Главная страница теперь здесь!
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]