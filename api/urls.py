from rest_framework.routers import DefaultRouter
from .views import FoodItemViewSet, MovieViewSet, OrderViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("food", FoodItemViewSet)
router.register("orders", OrderViewSet, basename="orders")

urlpatterns = router.urls
