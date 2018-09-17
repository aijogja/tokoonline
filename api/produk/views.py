from rest_framework import generics
from product.models import Produk
from api.produk.serializers import ProdukSerializer


class ProdukList(generics.ListAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
