from rest_framework import serializers
from product.models import Kategori


class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ('nama', )
