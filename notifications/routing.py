from django.urls import path
from notifications.consumers import OrderNotificationConsumer

websocket_urlpatterns = [
    path('ws/notifications/', OrderNotificationConsumer.as_asgi()),
]
