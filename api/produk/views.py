from rest_framework import generics, permissions
from product.models import Produk
from api.produk.serializers import ProdukSerializer
from api.permissions import IsAdminOrReadOnly


class ProdukList(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ProdukDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
