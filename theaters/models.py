from django.db import models

class Theater(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.location}"

class Screen(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name="screens")
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.theater.name} / {self.name}"
