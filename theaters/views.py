from django.shortcuts import render
from .models import Theater
def list_theaters(request):
    return render(request, "theaters/list.html", {"theaters": Theater.objects.filter(is_active=True)})
