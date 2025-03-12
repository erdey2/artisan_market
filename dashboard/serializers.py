from rest_framework import serializers
from dashboard.models import DashboardMetrics

class DashboardMetricsSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    active_listings = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=10, decimal_places=2)