from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nama_lengkap)

    class Meta:
        verbose_name = 'Direksi'
        verbose_name_plural = 'Direksi'

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=255)
    nomor_absen = models.CharField(max_length=255)
    nilai_rata_rata = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nama_lengkap)
    
    class Meta:
        verbose_name = 'Mentee'
        verbose_name_plural = 'Mentee'

class Mata_Pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=255)
    jadwal_dimulai = models.DateTimeField()
    jadwal_berakhir = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.nama_pelajaran)

    class Meta:
        verbose_name = 'Mata Pelajaran'
        verbose_name_plural = 'Mata Pelajaran'

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=255)
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nama_lengkap)

    class Meta:
        verbose_name = 'Mentor'
        verbose_name_plural = 'Mentor'

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=255)
    banyak_soal = models.CharField(max_length=255)
    bobot_nilai = models.CharField(max_length=255)
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete = models.CASCADE)

    def __str__(self):
        return "{}".format(self.nama_challenge)

    class Meta:
        verbose_name = 'Challenge'
        verbose_name_plural = 'Challenge'

class Live_Code(models.Model):
    nama_live_code = models.CharField(max_length=255)
    banyak_soal = models.CharField(max_length=255)
    bobot_nilai = models.CharField(max_length=255)
    tanggal_pelaksanaan = models.DateTimeField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete = models.CASCADE)

    def __str__(self):
        return "{}".format(self.nama_live_code)

    class Meta:
        verbose_name = 'Live Code'
        verbose_name_plural = 'Live Code'