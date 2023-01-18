from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    #기본적인 AbstractUser를 상속받기 때문에 id, username, password는 이미 있다. 
    username = models.CharField(max_length=255, unique=True)
    #email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    first_name = None
    last_name = None

    USERNAME_FIELD = 'username'   #login using username
    REQUIRED_FIELDS = []