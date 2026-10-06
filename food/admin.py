from django.contrib import admin
from .models import FoodCategory, FoodItem

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "discount", "stock", "is_available")
    list_filter = ("category", "is_available", "is_vegetarian")
    search_fields = ("name",)
