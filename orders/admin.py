from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("unit_price",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_code", "user", "status", "payment_status", "total", "created_at")
    list_filter = ("status", "payment_status")
    search_fields = ("order_code", "user__username")
    inlines = [OrderItemInline]
