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
        #requests information for the image key in photos. splits the info at ";base64,"
        format, imgstr = request.data["image"].split(';base64,')
        #?? starts at the end of format and splits the info at each "/"
        ext = format.split('/')[-1]
        #not entirely sure. sets the uploaded file as a string in photo object???
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["photo"]}-{uuid.uuid4()}.{ext}')

        #create a photo object where the image has the value of data (defined on line 20)
        photo = Photo.objects.create(
            title = request.data["title"],
            image = data
        )
        photo.save()
        serializer = PhotoSerializer(photo, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PhotoSerializer(serializers.ModelSerializer):
    """ JSON serializer for projects """
    class Meta:
        model = Photo
        fields = ('id', 'title', 'image')
