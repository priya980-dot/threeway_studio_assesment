from django.db import models

class UploadedAudio(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=255)# audio title
    audio = models.FileField(upload_to='uploads/')
    date = models.DateTimeField(auto_now_add=True)# upload date
    extension = models.CharField(max_length=10)# file extension
    size = models.CharField(max_length=20)# file size
