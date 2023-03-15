import uuid
import base64
from django.core.files.base import ContentFile
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from craftyCrittersapi.models import Photo

class PhotoView(ViewSet):
    """ View for Photos """

    def create(self, request):
        """ creates a new photo and assigns it a random name """

        format, imgstr = request.data["photo"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["project"]}-{uuid.uuid4()}.{ext}')

        photo = Photo.objects.create(
            title = request.data["title"],
            image = data
        )
        photo.save()
        serializer = PhotoSerializer(photo, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PhotoSerializer(serializers.ModelSerializer):
    """ JSON serializer for projects """
    class Meta:
        model = Photo
        fields = ('id', 'title', 'image')
