from django.db import models
from django.contrib.auth.models import AbstractUser

from Post.Tag.models import Tag


# Create your models here.
class Users(AbstractUser):
    role = models.CharField(max_length=24)
    first_name = models.CharField(max_length=32)
    recommendation = models.ManyToManyField(Tag, blank=True)
    last_name = models.CharField(max_length=32)
    gender = models.CharField(max_length=10)
    pfp = models.ImageField(null=True)
