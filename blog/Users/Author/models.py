from django.db import models

from Users.models import Users


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
