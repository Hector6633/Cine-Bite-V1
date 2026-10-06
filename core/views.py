from django.shortcuts import render
from movies.models import Movie, Show
from food.models import FoodItem

def home(request):
    movies = Movie.objects.filter(is_active=True)[:6]
    food_items = FoodItem.objects.filter(is_available=True)[:8]
    shows = Show.objects.filter(is_active=True).select_related("movie", "screen__theater").order_by("show_date", "start_time")[:6]
    return render(request, "core/home.html", {"movies": movies, "food_items": food_items, "shows": shows})
