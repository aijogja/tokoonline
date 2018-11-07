from django.contrib import admin
from product.models import Kategori, Produk, Order, OrderBarang

# Register your models here.

class ProdukInline(admin.TabularInline):
    model = Produk

class KategoriAdmin(admin.ModelAdmin):
    inlines = [
        ProdukInline,
    ]

class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'merk', 'kategori', 'qty', 'harga')
    list_filter = ('kategori',)


class OrderBarangInline(admin.TabularInline):
    model = OrderBarang

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'date', 'totalbelanja')
    list_filter = ('user', 'status')
    inlines = [
        OrderBarangInline,
    ]

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Produk, ProdukAdmin)
admin.site.register(Order, OrderAdmin)