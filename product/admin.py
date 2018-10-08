from django.contrib import admin
from product.models import Kategori, Produk, Order

# Register your models here.

admin.site.register(Kategori)
admin.site.register(Produk)
admin.site.register(Order)