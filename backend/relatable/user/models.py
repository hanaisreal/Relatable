from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length= 50, unique=True)
    intro = models.CharField(max_length= 500)
    profile_img = models.CharField(max_length= 1000)
    logged_in = models.BooleanField(default=False)