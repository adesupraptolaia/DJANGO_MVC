from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telpon = models.CharField(max_length=255)
    bidang = models.CharField(max_length=255)
    jadwal_praktek = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.nama)

    class Meta:
        verbose_name = 'Dokter'
        verbose_name_plural = 'Dokter'

class Pasien(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telpon = models.CharField(max_length=255)
    alamat = models.TextField()
    keluhan = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nama)

    class Meta:
        verbose_name = 'Pasien'
        verbose_name_plural = 'Pasien'

class Resep(models.Model):
    nama = models.CharField(max_length=255)
    total_harga = models.CharField(max_length=255)
    kumpulan_obat = models.TextField()

    def __str__(self):
        return "{}".format(self.nama)

    class Meta:
        verbose_name = 'Resep'
        verbose_name_plural = 'Resep'

class Obat(models.Model):
    nama = models.CharField(max_length=255)
    kandungan = models.TextField()
    khasiat = models.TextField()

    def __str__(self):
        return "{}".format(self.nama)

    class Meta:
        verbose_name = 'Obat'
        verbose_name_plural = 'Obat'