# Cine Bite

Cine Bite is a Django-based cinema food booking and pre-ordering platform.

## Included MVP
- Customer registration/login/logout
- Theater, screen, movie and show management
- Food categories and food items
- Session-based shopping cart
- Checkout and order creation
- Order tracking/status
- Customer dashboard and order history
- Staff/admin-ready Django admin
- REST API starter endpoints
- Bootstrap responsive UI

## Setup

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

## Demo data

After migration:

```bash
python manage.py seed_demo
```

This creates sample theaters, screens, movies, shows, food categories and food items.

## Notes
Payment gateway integration is intentionally left as a production integration point. The order model contains payment/status fields so Razorpay/Stripe can be added cleanly later.
