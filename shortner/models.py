from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class url(models.Model):
    link = models.CharField(max_length = 10000)
    uuid = models.CharField(max_length = 10)