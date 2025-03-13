from django.urls import path
from .views import ProductsViewList


urlpatterns = [
    path("", ProductsViewList.as_view(), name='product_list'),
    path("add/", ProductsViewList.as_view(), name="register_products"),
]