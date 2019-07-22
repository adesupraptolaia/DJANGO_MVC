from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    berat = models.CharField(max_length=255)
    umur = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nama)

    class Meta:
        verbose_name = 'Hewan'
        verbose_name_plural = 'Hewan'
        

class Kandang(models.Model):
    nama = models.CharField(max_length=255)
    isi_kandang = models.TextField()
    luas_kandang = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nama)
    
    class Meta:
        verbose_name = 'Kandang'
        verbose_name_plural = 'Kandang'

class Penjaga(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    jadwal_jaga = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.nama)

    class Meta:
        verbose_name = 'Penjaga'
        verbose_name_plural = 'Penjaga'

class Pengunjung(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    hari_berkunjung = models.DateField()

    def __str__(self):
        return "{}".format(self.nama)

    class Meta:
        verbose_name = 'Pengunjung'
        verbose_name_plural = 'Pengunjung'