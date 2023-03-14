"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from craftyCrittersapi.models import Critter

class CritterView(ViewSet):
    """Critter view"""
    def retrieve(self, request, pk):
        """ Handles single request for a critter"""

        critter = Critter.objects.get(pk=pk)
        serializer = CritterSerializer(critter)
        return Response(serializer.data)

    def list(self, request):
        """ Handles a request for all critters"""

        critter = Critter.objects.all()
        serializer = CritterSerializer(critter, many=True)
        return Response(serializer.data)

class CritterSerializer(serializers.ModelSerializer):
    """ JSON serializer for critters """
    class Meta:
        model = Critter
        fields = ('id', 'bio', 'photo')
