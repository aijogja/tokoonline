from rest_framework import generics
from product.models import Kategori
from api.kategori.serializers import KategoriSerializer


class KategoriList(generics.ListAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
