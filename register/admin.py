from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['phone', 'first_name', 'last_name', 'age', 'gender']
    search_fields = ['phone', 'first_name', 'last_name']
