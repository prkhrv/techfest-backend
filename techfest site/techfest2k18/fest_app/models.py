from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
