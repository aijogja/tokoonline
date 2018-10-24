from rest_framework import generics, permissions
from product.models import Order, OrderBarang
from api.order.serializers import OrderSerializer, OrderBarangSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        orders = Order.objects.filter(user=user)
        return orders


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)


class OrderBarangList(generics.ListCreateAPIView):
    queryset = OrderBarang.objects.all()
    serializer_class = OrderBarangSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        orders = OrderBarang.objects.filter(order=pk)
        return orders

    def get_serializer_context(self):
        pk = self.kwargs.get('pk')
        context = super(OrderBarangList, self).get_serializer_context()
        context['order_id'] = pk
        return context

