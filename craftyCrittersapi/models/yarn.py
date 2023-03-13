from django.db import models


class Yarn(models.Model):

    size = models.IntegerField(null=True)
    color = models.CharField(max_length=100)
    