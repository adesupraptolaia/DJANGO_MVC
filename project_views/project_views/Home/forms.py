from django import forms
from .models import *

class InputBlog(forms.ModelForm):
    class Meta:
        model = blog
        fields = ('foto', 'tanggal',  'banyakkomen', 'judul', 'isi')
    
class InputMentee(forms.ModelForm):
    class Meta:
        model = Mentee
        fields = ('nama', 'note', 'foto')

class InputMentor(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('nama', 'pengalaman', 'note', 'foto')
    