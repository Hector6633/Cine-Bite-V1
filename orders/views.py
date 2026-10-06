import uuid
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from food.models import FoodItem
from .models import Order, OrderItem

def cart(request):
    raw = request.session.get("cart", {})
    items, subtotal = [], Decimal("0")
    for pk, qty in raw.items():
        try:
            item = FoodItem.objects.get(pk=pk, is_available=True)
        except FoodItem.DoesNotExist:
            continue
        line = item.sale_price * qty
        subtotal += line
        items.append({"item": item, "quantity": qty, "line_total": line})
    tax = subtotal * Decimal("0.05")
    total = subtotal + tax
    return render(request, "orders/cart.html", {"items": items, "subtotal": subtotal, "tax": tax, "total": total})

@login_required
@transaction.atomic
def checkout(request):
    raw = request.session.get("cart", {})
    if not raw:
        messages.info(request, "Your cart is empty.")
        return redirect("food_list")
    items = []
    subtotal = Decimal("0")
    for pk, qty in raw.items():
        item = get_object_or_404(FoodItem.objects.select_for_update(), pk=pk, is_available=True)
        if qty > item.stock:
            messages.error(request, f"Not enough stock for {item.name}.")
            return redirect("cart")
        items.append((item, qty))
        subtotal += item.sale_price * qty

    if request.method == "POST":
        tax = subtotal * Decimal("0.05")
        order = Order.objects.create(
            user=request.user,
            order_code="CB" + uuid.uuid4().hex[:8].upper(),
            subtotal=subtotal,
            tax=tax,
            total=subtotal + tax,
            payment_status="PENDING",
            status="PENDING",
        )
        for item, qty in items:
            OrderItem.objects.create(order=order, food_item=item, quantity=qty, unit_price=item.sale_price)
            item.stock -= qty
            item.save(update_fields=["stock"])
        request.session["cart"] = {}
        request.session.modified = True
        messages.success(request, f"Order {order.order_code} placed successfully.")
        return redirect("order_detail", order_code=order.order_code)

    tax = subtotal * Decimal("0.05")
    return render(request, "orders/checkout.html", {"items": items, "subtotal": subtotal, "tax": tax, "total": subtotal + tax})

@login_required
def order_detail(request, order_code):
    order = get_object_or_404(Order.objects.prefetch_related("items__food_item"), order_code=order_code, user=request.user)
    return render(request, "orders/detail.html", {"order": order})
