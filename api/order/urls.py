from django.urls import include, path
from api.order.views import OrderList, OrderDetail

urlpatterns = [
    path('', OrderList.as_view(), name='order-list'),
    path('<pk>', OrderDetail.as_view(), name='order-detail'),
]
