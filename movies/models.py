from django.db import models
from theaters.models import Screen

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to="movies/", blank=True, null=True)
    language = models.CharField(max_length=50, default="Malayalam")
    genre = models.CharField(max_length=100, blank=True)
    duration_minutes = models.PositiveIntegerField(default=120)
    release_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="shows")
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name="shows")
    show_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2, default=150)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["show_date", "start_time"]

    def __str__(self):
        return f"{self.movie.title} - {self.show_date} {self.start_time}"
