from django.contrib import admin
from .models import Avto

@admin.register(Avto)
class AvtoAdmin(admin.ModelAdmin):
    list_display = ['author', 'active', 'brand', 'model', 'price','created','updated']
    list_filter = ['author', 'active', 'brand', 'model', 'price','created','updated']
    search_fields = ['author__username', 'brand', 'model']
    raw_id_fields = ["author"]
    list_editable = ['active']

    fieldsets = [
        
        ('Информация об автомобиле', {'fields': ('author','brand', 'model', 'price')}),
        ('Дополнительная информация', {'fields': ('steering', 'mileage', 'transmission', 'drive', 'fuel','year', 'description', 'image')}),
    ]

    
    