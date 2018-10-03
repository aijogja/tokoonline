from rest_framework import generics, permissions
from product.models import Produk
from api.produk.serializers import ProdukSerializer


class ProdukList(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
