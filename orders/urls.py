from django.urls import path
from . import views
urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("<str:order_code>/", views.order_detail, name="order_detail"),
]
