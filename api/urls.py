from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views

schema_view = get_swagger_view(title='TokoOnline API')


urlpatterns = [
    path('docs', schema_view),
    path('kategori/', include('api.kategori.urls')),
    path('produk/', include('api.produk.urls')),
    path('order/', include('api.order.urls')),
    path('auth-token/', views.obtain_auth_token)
]

