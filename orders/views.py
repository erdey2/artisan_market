# views.py (refactored view)
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from rest_framework import generics
from orders.models import Order
from .serializers import OrderSerializer


class OrderView(models.Model):
    status = models.CharField(max_length=100)

    def update_status(self, new_status):
        self.status = new_status
        self.save()

        # Notify via WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "order_notifications",
            {
                "type": "send_notification",
                "message": f"Order {self.id} status changed to {new_status}."
            }
        )

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        order.update_status(request.data['status'])
        return super().update(request, *args, **kwargs)
