from rest_framework import serializers
from product.models import Order, OrderBarang
from api.produk.serializers import ProdukSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'no_hape', 'alamat', 'ongkir', 'catatan')

    def create(self, validated_data):
        # Digunakan untuk biar ketika order, otomatis mengisi user berdasarkan
        # siapa yang sedang aktif
        user = self.context['request'].user
        validated_data['user'] = user
        return super(OrderSerializer, self).create(validated_data)


class OrderBarangGETSerializer(serializers.ModelSerializer):
    # ProdukSerializer() ini digunakan untuk menampilkan detail data produk
    produk = ProdukSerializer()

    class Meta:
        model = OrderBarang
        fields = ('id', 'produk', 'harga', 'qty')


class OrderBarangPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderBarang
        fields = ('id', 'produk', 'harga', 'qty')

    def create(self, validated_data):
        # Digunakan untuk biar ketika order barang, otomatis menggunakan
        # order id yang sedang dipakai
        order_id = self.context['order_id']
        order = Order.objects.get(id=order_id)
        produk = validated_data['produk']
        validated_data['order'] = order
        validated_data['harga'] = produk.harga
        return super(OrderBarangPOSTSerializer, self).create(validated_data)
