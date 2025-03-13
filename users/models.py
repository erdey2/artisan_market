from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ARTIST = 'artist'
    CUSTOMER = 'customer'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (ARTIST, 'Artist'),
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTOMER)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username
