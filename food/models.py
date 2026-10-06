from django.db import models

class FoodCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="food/categories/", blank=True, null=True)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="food/items/", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)
    is_vegetarian = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)

    @property
    def sale_price(self):
        return max(self.price - self.discount, 0)

    def __str__(self):
        return self.name
