from rest_framework import serializers
from product.models import Order, OrderBarang, Produk
from api.produk.serializers import ProdukSerializer


class OrderSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'no_hape', 'alamat', 'ongkir', 'catatan', 'status')

    def update(self, instance, validated_data):
        if instance.status == 'cart' and validated_data['status'] == 'checkout':
            # Digunakan untuk mengurangi qty produk, ketika status dari cart
            # menjadi checkout
            orderbarang = instance.orderbarangnya.all()
            for ob in orderbarang:
                produk = ob.produk
                sisaqty = produk.qty - ob.qty
                produk.qty = sisaqty
                produk.save()
        return super(OrderSerializer1, self).update(instance, validated_data)


class OrderSerializer2(serializers.ModelSerializer):
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
        return super(OrderSerializer2, self).create(validated_data)


class OrderBarangGETSerializer(serializers.ModelSerializer):
    # ProdukSerializer() ini digunakan untuk menampilkan detail data produk
    produk = ProdukSerializer()

    class Meta:
        model = OrderBarang
        fields = ('id', 'produk', 'harga', 'qty', 'subtotal')


class OrderBarangPOSTSerializer(serializers.ModelSerializer):
    qty = serializers.IntegerField(max_value=99, min_value=1)

    class Meta:
        model = OrderBarang
        fields = ('id', 'produk', 'qty')

    def validate_qty(self, value):
        """
        Check stok dari produk
        """
        id_produk = self.initial_data['produk']
        produk = Produk.objects.get(pk=id_produk)
        if value > produk.qty:
            raise serializers.ValidationError(
                "Stok cuma ada {}".format(produk.qty)
            )
        return value

    def create(self, validated_data):
        # Digunakan untuk biar ketika order barang, otomatis menggunakan
        # order id yang sedang dipakai
        order_id = self.context['order_id']
        order = Order.objects.get(id=order_id)
        if order.status != 'cart':
            # ini digunakan untuk memvalidasi apakah status order cart atau
            # bukan. kalau bukan cart, maka sudah tidak bisa nambah barang
            raise serializers.ValidationError(
                "Anda sudah tidak bisa untuk menambah barang"
            )

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
