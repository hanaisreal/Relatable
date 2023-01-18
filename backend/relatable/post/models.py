from django.db import models
from user.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    public = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, through="postTag", related_name="posts")

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postTag" )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="postTag")