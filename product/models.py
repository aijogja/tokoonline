from django.db import models

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
