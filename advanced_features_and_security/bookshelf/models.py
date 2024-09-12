from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.CharField(max_length= 200)
    publication_year = models.IntegerField()