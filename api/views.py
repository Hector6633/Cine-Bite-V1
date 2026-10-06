from rest_framework import viewsets
from food.models import FoodItem
from movies.models import Movie
from orders.models import Order
from .serializers import FoodItemSerializer, MovieSerializer, OrderSerializer

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer

class FoodItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FoodItem.objects.filter(is_available=True)
    serializer_class = FoodItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        if self.request.user.is_authenticated:
            return Order.objects.filter(user=self.request.user)
        return Order.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
