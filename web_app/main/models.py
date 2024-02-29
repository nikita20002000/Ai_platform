from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title