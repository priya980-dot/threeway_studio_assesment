from django import forms
from .models import UploadedAudio

class AudioUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedAudio
        fields = ['user', 'name', 'audio']
