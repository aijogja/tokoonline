from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from product.models import Order, OrderBarang
from api.order.serializers import (
    OrderSerializer,
    OrderBarangGETSerializer,
    OrderBarangPOSTSerializer,
)


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('status',)

    def get_queryset(self):
        # Untuk menampilkan data Order berdasarkan user yang login
        user = self.request.user
        orders = Order.objects.filter(user=user)
        return orders


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)


class OrderBarangList(generics.ListCreateAPIView):
    queryset = OrderBarang.objects.all()
    serializer_class = OrderBarangGETSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        # Untuk memisahkan serializer yang digunakan pada GET dan POST
        if self.request.method in permissions.SAFE_METHODS:
            return OrderBarangGETSerializer
        return OrderBarangPOSTSerializer

    def get_queryset(self):
        # Untuk menampilkan data OrderBarang berdasarkan id Order
        pk = self.kwargs.get('pk')
        orders = OrderBarang.objects.filter(order=pk)
        return orders

    def get_serializer_context(self):
        # Untuk mengirimkan context ke serializer
        pk = self.kwargs.get('pk')
        context = super(OrderBarangList, self).get_serializer_context()
        context['order_id'] = pk
        return context

