from django.db import models
from django.contrib.auth.models import User


class Critter(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    photo = models.ImageField(null=True, upload_to=None, height_field=None, width_field=None, max_length=100)
