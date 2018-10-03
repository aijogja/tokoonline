from rest_framework import generics, permissions
from product.models import Kategori
from api.kategori.serializers import KategoriSerializer
from api.permissions import IsAdminOrReadOnly


class KategoriList(generics.ListCreateAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
    permission_classes = (IsAdminOrReadOnly,)
