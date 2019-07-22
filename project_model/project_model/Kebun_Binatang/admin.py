from django.contrib import admin
from Kebun_Binatang.models import Hewan, Kandang, Penjaga, Pengunjung 
# Register your models here.

class HewanDesc(admin.ModelAdmin):
    list_display = ['id', 'nama', 'species']
    list_display_links = ['id', 'nama']
    search_fields = ['nama']

class KandangDesc(admin.ModelAdmin):
    list_display = ['id', 'nama', 'isi_kandang']
    list_display_links = ['id', 'nama']
    search_fields = ['nama']

class PenjagaDesc(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon']
    list_display_links = ['id', 'nama']
    search_fields = ['nama']

class PengunjungDesc(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon']
    list_display_links = ['id', 'nama']
    search_fields = ['nama']

admin.site.register(Hewan, HewanDesc)
admin.site.register(Kandang, KandangDesc)
admin.site.register(Penjaga, PenjagaDesc)
admin.site.register(Pengunjung, PengunjungDesc)