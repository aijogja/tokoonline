from django.urls import include, path
from api.order.views import (
    OrderList, OrderDetail, OrderBarangList, OrderBarangDetail
)

urlpatterns = [
    path('', OrderList.as_view(), name='order-list'),
    path('<pk>', OrderDetail.as_view(), name='order-detail'),
    path('<pk>/barang/', OrderBarangList.as_view(), name='order-barang-list'),
    path('<pk>/barang/<barangid>/',
        OrderBarangDetail.as_view(), name='order-barang-detail'),
]
