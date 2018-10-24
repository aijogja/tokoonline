from rest_framework import serializers
from product.models import Order, OrderBarang


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'no_hape', 'alamat', 'ongkir', 'catatan')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(OrderSerializer, self).create(validated_data)


class OrderBarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBarang
        fields = ('id', 'produk', 'harga', 'qty')

    def create(self, validated_data):
        order_id = self.context['order_id']
        order = Order.objects.get(id=order_id)
        validated_data['order'] = order
        return super(OrderBarangSerializer, self).create(validated_data)
