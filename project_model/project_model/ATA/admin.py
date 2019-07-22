from django.contrib import admin
from ATA.models import Direksi, Mentee, Mentor, Mata_Pelajaran, Challenge, Live_Code

# Register your models here.

class DireksiDesc(admin.ModelAdmin):
    list_display = ['id', 'nama_lengkap', 'no_telepon']
    list_display_links = ['id', 'nama_lengkap']
    search_fields = ['nama_lengkap']

class MenteeDesc(admin.ModelAdmin):
    list_display = ['id', 'nama_lengkap', 'no_telepon']
    list_display_links = ['id', 'nama_lengkap']
    search_fields = ['nama_lengkap']

class MentorDesc(admin.ModelAdmin):
    list_display = ['id', 'nama_lengkap', 'no_telepon']
    list_display_links = ['id', 'nama_lengkap']
    search_fields = ['nama_lengkap']

class Mata_PelajaranDesc(admin.ModelAdmin):
    list_display = ['id', 'nama_pelajaran']
    list_display_links = ['id', 'nama_pelajaran']
    search_fields = ['nama_pelajaran']

class ChallengeDesc(admin.ModelAdmin):
    list_display = ['id', 'nama_challenge', 'mata_pelajaran']
    list_display_links = ['id', 'nama_challenge']
    search_fields = ['nama_challenge']

class live_CodeDesc(admin.ModelAdmin):
    list_display = ['id', 'nama_live_code', 'mata_pelajaran']
    list_display_links = ['id', 'nama_live_code']
    search_fields = ['nama_live_code']

admin.site.register(Direksi, DireksiDesc)
admin.site.register(Mentee, MenteeDesc)
admin.site.register(Mentor, MentorDesc)
admin.site.register(Mata_Pelajaran, Mata_PelajaranDesc)
admin.site.register(Challenge, ChallengeDesc)
admin.site.register(Live_Code, live_CodeDesc)