from django.db import models

# Create your models here.

# Local file upload 
class UploadedFile(models.Model):
    zipfile = models.FileField(upload_to='uploads/', blank=True)
    repo_link = models.URLField(blank=True, null=True)
    cloud_url = models.URLField(blank=True, null=True)
