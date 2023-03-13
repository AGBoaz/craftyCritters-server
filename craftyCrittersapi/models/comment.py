from django.db import models


class Comment(models.Model):

    body = models.CharField(max_length=100)
    critter = models.ForeignKey("Critter", on_delete=models.CASCADE)
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="comments")
    