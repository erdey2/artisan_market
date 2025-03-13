from products.models import Product
from orders.models import Order
from django.db.models import Count, Sum
from django.contrib.auth import get_user_model

User = get_user_model()
class DashboardMetrics:
    @staticmethod
    def get_total_users():
        return User.objects.count()

    @staticmethod
    def get_active_listings():
        return Product.objects.filter(is_active=True).count()

    @staticmethod
    def get_total_revenue():
        return Order.objects.filter(status='DELIVERED').aggregate(total_revenue=Sum('total_price'))[
            'total_revenue'] or 0
