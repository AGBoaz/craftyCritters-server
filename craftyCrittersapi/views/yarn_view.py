"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from craftyCrittersapi.models import Yarn

class YarnView(ViewSet):
    """ craftyCritters Yarn view """
    def retrieve(self, request, pk):
        """ Handle GET requests for single yarn """

        yarn = Yarn.objects.get(pk=pk)
        serializer = YarnSerializer(yarn)
        return Response(serializer.data)

    def list(self, request):
        """ Handle GET requests for all yarn """

        yarn = Yarn.objects.all()
        serializer = YarnSerializer(yarn, many=True)
        return Response(serializer.data)

    def create(self,request):
        yarn = Yarn.objects.create(
            size = request.data["size"],
            color = request.data["color"]
        )
        serializer = YarnSerializer(yarn)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class YarnSerializer(serializers.ModelSerializer):
    """ JSON serializer for yarn """
    class Meta:
        model = Yarn
        fields = ('id', 'size', 'color')
