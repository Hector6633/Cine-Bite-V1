from django.shortcuts import get_object_or_404, render
from .models import Movie, Show

def movie_list(request):
    movies = Movie.objects.filter(is_active=True)
    return render(request, "movies/list.html", {"movies": movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk, is_active=True)
    shows = Show.objects.filter(movie=movie, is_active=True).select_related("screen__theater")
    return render(request, "movies/detail.html", {"movie": movie, "shows": shows})
