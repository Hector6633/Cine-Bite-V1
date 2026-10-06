from django.urls import path
from . import views
urlpatterns = [path("", views.list_theaters, name="theater_list")]
