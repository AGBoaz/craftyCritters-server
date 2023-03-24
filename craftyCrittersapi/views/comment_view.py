"""View module for handling requests about game reviews"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from craftyCrittersapi.models import Comment, Project, Critter

class CommentView(ViewSet):

    def list(self, request):
        """ Handle request to get all comments """

        projects = Project.objects.all()
        serializer = CommentSerializer(projects, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Handle POST requests to create a comment"""

        try:
            project = Project.objects.get(pk=request.data['project'])
        except Project.DoesNotExist:
            return Response({'message': 'You sent an invalid game ID'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            critter = Critter.objects.get(user=request.auth.user)
        except Critter.DoesNotExist:
            return Response({'message': 'You sent an invalid token'}, status=status.HTTP_404_NOT_FOUND)
        
        body_text = request.data.get('review', None)
        if body_text is None:
            return Response({'message': 'Cannot submit an empty comment.'}, status=status.HTTP_400_BAD_REQUEST)
        
        comment = Comment()
        comment.body = body_text
        comment.critter = critter
        comment.project = project
        comment.save()

        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CritterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Critter
        fields = ( 'username', )

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    critter = CritterSerializer()

    class Meta:
        model = Comment
        fields = ( 'id', 'critter', 'body',)
