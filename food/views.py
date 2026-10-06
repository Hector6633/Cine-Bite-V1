from django.contrib import messages
from django.shortcuts import redirect, render
from .models import FoodItem

def food_list(request):
    foods = FoodItem.objects.filter(is_available=True).select_related("category")
    category = request.GET.get("category")
    if category:
        foods = foods.filter(category_id=category)
    return render(request, "food/list.html", {"foods": foods})

def add_to_cart(request, pk):
    item = FoodItem.objects.get(pk=pk, is_available=True)
    cart = request.session.get("cart", {})
    key = str(pk)
    cart[key] = cart.get(key, 0) + 1
    if cart[key] > item.stock:
        cart[key] = item.stock
        messages.warning(request, f"Only {item.stock} of {item.name} are available.")
    request.session["cart"] = cart
    request.session.modified = True
    messages.success(request, f"{item.name} added to your cart.")
    return redirect(request.META.get("HTTP_REFERER", "food_list"))
