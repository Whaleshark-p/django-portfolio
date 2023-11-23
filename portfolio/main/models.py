import os
from django.db import models
from django.conf import settings

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    thumbnail = models.FilePathField(path='static/main')
    text = models.CharField(max_length = 4000)
    hyperlink = models.URLField(max_length = 200, blank=True)

    def __str__(self):
        return self.title
    
    