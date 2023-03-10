from django.db import models


class Comment(models.Model):

    size = models.IntegerField(null=True)
    color = models.CharField(max_length=100)
    