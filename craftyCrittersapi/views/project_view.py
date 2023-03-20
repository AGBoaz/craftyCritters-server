"""View module for handling requests about projects """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from craftyCrittersapi.models import Project, Photo, Critter, Yarn

class ProjectView(ViewSet):
    """Project view"""
    def retrieve(self, request, pk):
        """ Handles single request for a project"""

        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def list(self, request):
        """ Handles a request for all projects"""
        type = self.request.query_params.get("project_type", None)

        if type :
            project = Project.objects.filter(project_type=type)
        else:
            project = Project.objects.all()

        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Handle POST request for projects """
        photo = Photo.objects.get(pk=request.data["photo"])
        critter = Critter.objects.get(user=request.auth.user)

        project = Project.objects.create(
            project_type = request.data["project_type"],
            name = request.data["name"],
            tool_size = request.data["tool_size"],
            directions_link = request.data["directions_link"],
            pattern_type = request.data["pattern_type"],
            photo=photo,
            critter=critter
        )
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, pk):
        """ Handle PUT request for a project """

        project = Project.objects.get(pk=pk)
        project.project_type = request.data["project_type"]
        project.name = request.data["name"]
        project.tool_size = request.data["tool_size"]
        project.directions_link = request.data["directions_link"]
        project.pattern_type = request.data["pattern_type"]

        photo = Photo.objects.get(pk=request.data["photo"])
        project.photo = photo
        critter = Critter.objects.get(user=request.auth.user)
        project.critter = critter

        project.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ Handle DELETE requests for project """
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def addYarn(self, request, pk):
        """ Handle POST request to add yarn to a project """

        project = Project.objects.get(pk=pk)
        yarn = Yarn.objects.get(pk=request.data["yarn"])
        project.yarn.add(yarn)

        return Response (status=status.HTTP_201_CREATED)

class ProjectSerializer(serializers.ModelSerializer):
    """ JSON serializer for projects """
    class Meta:
        model = Project
        fields = (
            'id', 'project_type', 'name', 'tool_size',
            'photo', 'directions_link', 'pattern_type',
            'critter', 'yarn', 'added'
        )
