from django.db import models

from Post.models import Post
from Post.Comment.models import Comment
from Users.models import Users


# Create your models here.
class LikeType(models.Model):
    type = models.CharField(max_length=24)


class Like(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(LikeType, on_delete=models.CASCADE)
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
