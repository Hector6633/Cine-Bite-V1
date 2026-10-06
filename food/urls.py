from django.urls import path
from . import views
urlpatterns = [
    path("", views.food_list, name="food_list"),
    path("add/<int:pk>/", views.add_to_cart, name="add_to_cart"),
]
