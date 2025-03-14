from django.urls import path
from .views import NotificationListView, NotificationDetailView


urlpatterns = [
    path("", NotificationListView.as_view(), name='dashboard_metric'),
    path('notification/<int:pk>/', NotificationDetailView.as_view(), name='notification_detail'),
]