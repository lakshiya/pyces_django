from django import forms
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['zipfile', 'repo_link','cloud_url']
        labels = {
            'zipfile' : 'Attach Zip file',
            'repo_link': 'Enter the Repo link ',
            'cloud_url': 'Enter the location of the file in Cloud'
        }
        required = {
            'zipfile' : False,
            'repo_link': False,
            'cloud_url': False
        }

