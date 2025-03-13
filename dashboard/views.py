from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DashboardMetrics
from .serializers import DashboardMetricsSerializer
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema

class DashboardMetricsView(APIView):
    permission_classes = [IsAdminUser] # only admin can access this view

    extend_schema(
        summary="Retrieve Dashboard Metrics",
        description="Returns key metrics for the admin dashboard, including total users, active listings, and total revenue.",
        responses={200: DashboardMetricsSerializer},  # Define the expected response format
    )
    def get(self, request):
        metrics = {
            'total_users': DashboardMetrics.get_total_users(),
            'active_listings': DashboardMetrics.get_active_listings(),
            'total_revenue': DashboardMetrics.get_total_revenue(),
        }
        serializer = DashboardMetricsSerializer(metrics)
        return Response(serializer.data, status=status.HTTP_200_OK)
