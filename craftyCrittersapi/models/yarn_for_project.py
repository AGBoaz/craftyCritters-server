from django.db import models


class YarnForProject(models.Model):

    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    yarn = models.ForeignKey("Yarn", on_delete=models.CASCADE)
    