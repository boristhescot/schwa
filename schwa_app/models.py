from django.db import models

# Create your models here.
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User


class AudioFile(models.Model):
    audio_file = models.FileField()
    file_name = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('file_name', 'user',)

    def __str__(self):
        return self.file_name