from django.db import models


class Project(models.Model):

    project_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    tool_size = models.IntegerField(null=True)
    critter = models.ForeignKey("Critter", on_delete=models.CASCADE)
    directions_link = models.TextField(null=True)
    pattern_type = models.CharField(max_length=50)

    yarn = models.ManyToManyField("Yarn", through="YarnForProject")

    @property
    def added(self):
        return self.__added

    @added.setter
    def added(self, value):
        self.__added = value
