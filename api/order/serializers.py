from rest_framework import serializers
from product.models import Order, OrderBarang
from api.produk.serializers import ProdukSerializer


class OrderGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'no_hape', 'alamat', 'ongkir', 'catatan')


class OrderPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', )

    def create(self, validated_data):
        # Digunakan untuk biar ketika order, otomatis mengisi user berdasarkan
        # siapa yang sedang aktif
        user = self.context['request'].user
        validated_data['user'] = user

        # Code ini digunakan untuk mengecek. Kalau sudah ada orderan dengan
        # status cart, maka tidak perlu create order, tp ambil data order tsb
        # Logikanya : cart itu cuma ada 1.
        order = user.orderanku.filter(status='cart').first()
        if order:
            return order
        return super(OrderPOSTSerializer, self).create(validated_data)


class OrderBarangGETSerializer(serializers.ModelSerializer):
    # ProdukSerializer() ini digunakan untuk menampilkan detail data produk
    produk = ProdukSerializer()

    class Meta:
        model = OrderBarang
        fields = ('id', 'produk', 'harga', 'qty', 'subtotal')


class OrderBarangPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderBarang
        fields = ('id', 'produk', 'qty')

    def create(self, validated_data):
        # Digunakan untuk biar ketika order barang, otomatis menggunakan
        # order id yang sedang dipakai
        order_id = self.context['order_id']
        order = Order.objects.get(id=order_id)
        orderbarangnya = order.orderbarangnya.all()

        produk = validated_data['produk']
        validated_data['order'] = order
        # untuk ngeset harga berdasarkan harga barang
        validated_data['harga'] = produk.harga

        # untuk mengecek apakah produk sudah pernah diorder apa belum
        # kalau sudah pernah, maka qty ditambahkan ke yang sebelumnya
        for ob in orderbarangnya:
            if produk.id == ob.produk.id:
                ob.qty += validated_data['qty']
                ob.save()
                return ob

        return super(OrderBarangPOSTSerializer, self).create(validated_data)
