from django.utils import timezone
from django.db import models

from Users.Author.models import Author
from Post.Tag.models import Tag


# Create your models here.
class Post(models.Model):
    created_at = models.DateField(default=timezone.now)
    fk_author_id = models.ForeignKey(Author, on_delete=models.PROTECT)
    title = models.CharField(max_length=128)
    image = models.ImageField()
    content = models.CharField(max_length=8192)
    tags = models.ManyToManyField(Tag)
