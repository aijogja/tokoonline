from rest_framework import serializers
from product.models import Produk


class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ('id', 'nama', 'merk', 'gambar', 'harga', 'qty', 'kategori')
