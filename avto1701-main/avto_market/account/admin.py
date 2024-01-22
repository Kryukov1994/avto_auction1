from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth','full_name', 'user_type', 'status', 'phone_number', 'email']
    list_filter = ['user_type', 'status']
    search_fields = ['user__username', 'user','full_name']  
    raw_id_fields = ['user']
