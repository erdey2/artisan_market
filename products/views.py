from rest_framework import generics
from .serializers import ProductSerializer
from products.models import Product

class ProductsViewList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer()
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


