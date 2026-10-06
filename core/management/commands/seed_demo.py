from datetime import date, time, timedelta
from django.core.management.base import BaseCommand
from theaters.models import Theater, Screen
from movies.models import Movie, Show
from food.models import FoodCategory, FoodItem

class Command(BaseCommand):
    help = "Create Cine Bite demo data"

    def handle(self, *args, **kwargs):
        t1, _ = Theater.objects.get_or_create(
            name="Cine Bite PVR", location="Thiruvananthapuram",
            defaults={"address": "Central Mall, Thiruvananthapuram", "phone": "9876543210"}
        )
        s1, _ = Screen.objects.get_or_create(theater=t1, name="Screen 1", defaults={"capacity": 120})
        s2, _ = Screen.objects.get_or_create(theater=t1, name="Screen 2", defaults={"capacity": 180})

        m1, _ = Movie.objects.get_or_create(
            title="The Last Horizon",
            defaults={"description": "A science-fiction adventure.", "language": "English",
                      "genre": "Sci-Fi", "duration_minutes": 145, "release_date": date.today()}
        )
        m2, _ = Movie.objects.get_or_create(
            title="Kerala Stories",
            defaults={"description": "A family drama set in Kerala.", "language": "Malayalam",
                      "genre": "Drama", "duration_minutes": 130, "release_date": date.today()}
        )

        for movie, screen, start in [(m1, s1, time(19, 30)), (m2, s2, time(18, 0))]:
            Show.objects.get_or_create(movie=movie, screen=screen, show_date=date.today(),
                                        start_time=start, defaults={"end_time": time((start.hour+2)%24, 0),
                                                                     "ticket_price": 220})

        categories = {}
        for name in ["Popcorn", "Beverages", "Snacks", "Combos"]:
            categories[name], _ = FoodCategory.objects.get_or_create(name=name)

        products = [
            ("Classic Popcorn", "Popcorn", 180, 30),
            ("Cheese Popcorn", "Popcorn", 220, 25),
            ("Coke", "Beverages", 120, 50),
            ("Nachos", "Snacks", 200, 25),
            ("Movie Combo", "Combos", 399, 30),
        ]
        for name, cat, price, stock in products:
            FoodItem.objects.get_or_create(name=name, category=categories[cat],
                                            defaults={"price": price, "stock": stock,
                                                      "description": f"Fresh {name} for your movie."})
        self.stdout.write(self.style.SUCCESS("Cine Bite demo data created."))
