from django.conf.urls import url
from api.kategori.views import KategoriList

urlpatterns = [
    url(r'^', KategoriList.as_view(), name='kategori-list')
]
