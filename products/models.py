from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Product(models.Model):
    name = models.CharField(max_length=255, db_index = True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index = True)
    stock = models.PositiveIntegerField()
    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
