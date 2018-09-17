from django.conf.urls import url
from api.produk.views import ProdukList

urlpatterns = [
    url(r'^', ProdukList.as_view(), name='produk-list')
]
