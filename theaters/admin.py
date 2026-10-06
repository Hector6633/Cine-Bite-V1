from django.contrib import admin
from .models import Theater, Screen

@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "phone", "is_active")
    search_fields = ("name", "location")

@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ("name", "theater", "capacity")
    list_filter = ("theater",)
