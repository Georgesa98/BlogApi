from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    is_verified = models.BooleanField(default=False)
