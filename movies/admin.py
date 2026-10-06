from django.contrib import admin
from .models import Movie, Show

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "language", "genre", "duration_minutes", "is_active")
    search_fields = ("title", "genre", "language")

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ("movie", "screen", "show_date", "start_time", "ticket_price", "is_active")
    list_filter = ("show_date", "screen")
