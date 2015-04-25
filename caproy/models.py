from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Castle(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=16384)

