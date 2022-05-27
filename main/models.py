from distutils.command.upload import upload
from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.
class assets(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    prop = models.CharField(max_length=100)
    ctgry = models.CharField(max_length=100)

    def __str__(self):
        return self.name
