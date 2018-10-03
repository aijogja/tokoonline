from django.urls import include, path
from api.produk.views import ProdukList, ProdukDetail

urlpatterns = [
    path('', ProdukList.as_view(), name='produk-list'),
    path('<pk>', ProdukDetail.as_view(), name='produk-detail'),
]
