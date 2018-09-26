from django.urls import include, path
from api.kategori.views import KategoriList, KategoriDetail

urlpatterns = [
    path('', KategoriList.as_view(), name='kategori-list'),
    path('<pk>', KategoriDetail.as_view(), name='kategori-detail'),
]
