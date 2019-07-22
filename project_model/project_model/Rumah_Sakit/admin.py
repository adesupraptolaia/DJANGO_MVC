from django.contrib import admin
from Rumah_Sakit.models import Dokter, Pasien, Resep, Obat

# Register your models here

class DokterDesc(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telpon']
    list_display_links = ['id', 'nama']
    search_fields = ['nama']

class PasienDesc(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telpon']
    list_display_links = ['id', 'nama']
    search_fields = ['nama']

class ResepDesc(admin.ModelAdmin):
    list_display = ['id', 'nama', 'total_harga']
    list_display_links = ['id', 'nama']
    search_fields = ['nama']

class ObatDesc(admin.ModelAdmin):
    list_display = ['id', 'nama']
    list_display_links = ['id', 'nama']
    search_fields = ['nama']

admin.site.register(Dokter, DokterDesc)
admin.site.register(Pasien, PasienDesc)
admin.site.register(Resep, ResepDesc)
admin.site.register(Obat, ObatDesc)