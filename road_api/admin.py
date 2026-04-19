from django.contrib import admin
from .models import Road

@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    # Какие колонки показывать в списке
    list_display = ('name', 'temp', 'status', 'created_at')
    
    # По каким полям можно искать
    search_fields = ('name',)
    
    # Фильтры справа
    list_filter = ('status', 'created_at')