from django.db import models

# Create your models here.
class Mentor(models.Model):
    nama = models.CharField(max_length=255)
    pengalaman = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)

class Mentee(models.Model):
    nama = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)

class blog(models.Model):
    foto = models.CharField(max_length=255)
    tanggal = models.DateField()
    banyakkomen = models.CharField(max_length=255)
    judul = models.CharField(max_length=255)
    isi = models.TextField()