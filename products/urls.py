from django.urls import path
from .views import ProductListView, ProductDetailView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", ProductListView.as_view(), name='product_list'),
    path("add/", ProductListView.as_view(), name="register_products"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]