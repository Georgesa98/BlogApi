from django.db import models

from Post.models import Post
from Users.models import Users


# Create your models here.
class Comment(models.Model):
    fk_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    fk_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    fk_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
