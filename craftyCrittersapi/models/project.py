from django.db import models


class Project(models.Model):

    project_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    tool_size = models.IntegerField(null=True)
    critter = models.ForeignKey("Critter", on_delete=models.CASCADE)
    photo = models.ImageField(null=True, upload_to=None, height_field=None, width_field=None, max_length=100)
    directions_link = models.TextField(null=True)
    pattern_type = models.CharField(max_length=50)
    