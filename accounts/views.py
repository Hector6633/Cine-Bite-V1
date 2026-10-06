from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import SignUpForm
from orders.models import Order

def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect("home")
    return render(request, "accounts/signup.html", {"form": form})

@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user).prefetch_related("items").order_by("-created_at")
    return render(request, "accounts/dashboard.html", {"orders": orders})
