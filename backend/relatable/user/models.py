from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    #기본적인 AbstractUser를 상속받기 때문에 id, username, password는 이미 있다. 
    nickname = models.CharField(max_length= 50, unique=True)
    intro = models.CharField(max_length= 500)
    profile_img = models.CharField(max_length= 1000, null=True)
    logged_in = models.BooleanField(default=False)