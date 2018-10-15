from django.db import models
from django.conf import settings

# Create your models here.

class Produk(models.Model):
    nama = models.CharField(max_length=125)
    merk = models.CharField(max_length=30, blank=True, null=True)
    gambar = models.ImageField(max_length=125, blank=True, null=True)
    harga = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    qty = models.IntegerField(default=0)
    kategori = models.ForeignKey('Kategori', on_delete=models.CASCADE)

    def __str__(self):
        return self.nama


class Kategori(models.Model):
    nama = models.CharField(max_length=30)

    def __str__(self):
        return self.nama


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True)
    no_hape = models.CharField(max_length=15, null=True)
    alamat = models.TextField()
    ongkir = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    catatan = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=(
            ('checkout', 'Checkout'),
            ('paid', 'Terbayar'),
            ('delivered', 'Terkirim'),
        ),
        default='checkout',
        max_length=10,
    )
    totalbelanja = models.DecimalField(
        max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return str(self.pk)


class OrderBarang(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    produk = models.ForeignKey('Produk', on_delete=models.CASCADE)
    harga = models.DecimalField(
        max_digits=15, decimal_places=2, default=0)
    qty = models.IntegerField(default=1)
    totalhargabarang = models.DecimalField(
        max_digits=15, decimal_places=2, default=0)

