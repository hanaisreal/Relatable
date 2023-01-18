from django.db import models
from user.models import User
from post.models import Post

# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="likes", null=False)
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name="likes", null=False)