from django.db import models


class Photo(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='projectimages', height_field=None,
        width_field=None, max_length=None, null=True
    )
    