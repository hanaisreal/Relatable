from django.db import models
from user.models import User
from post.models import Post

# Create your models here.
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="bookmarks", null=False)
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name="bookmarks", null=False)

    # class Meta:
    #     constraints = {
    #         models.UniqueConstraint(
    #             fields=["post", "user"],
    #             name = "already bookmarked",
    #         )
    #     }

