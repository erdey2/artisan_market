from rest_framework import generics
from .serializers import ProductSerializer
from products.models import Product
from .permissions import IsArtistOrReadOnly # import the new custom permissions class

class ProductListView(generics.ListCreateAPIView):
    """ Artist can create products; everyone can browse."""
    serializer_class = ProductSerializer
    permission_classes = [IsArtistOrReadOnly] # apply permissions

    def get_queryset(self):
        """ Customers can browse all products; Artist see only their own."""
        qs = Product.objects.all()

        # apply filtering
        name = self.request.GET.get('name')
        price = self.request.GET.get('price')
        if name:
            qs = qs.filter(name__icontains=name)
        if price:
            qs = qs.filter(price__lte=price)
        return qs

    def perform_create(self, serializer):
        """Assign the currently logged-in artisan as the product's artist."""
        serializer.save(artist=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a product (only by owner)."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsArtistOrReadOnly]


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


