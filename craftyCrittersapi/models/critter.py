from django.db import models
from django.contrib.auth.models import User


class Critter(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    photo = models.ForeignKey("Photo", on_delete=models.CASCADE)
