from django.http.response import HttpResponse
from raterapp.models import Category, GamePicture
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.files.base import ContentFile
import base64
import uuid

class GamePictureViewSet(ViewSet):
    def create(self, request):
        # Create a new instance of the game picture model you defined
        game_picture = GamePicture()

        format, imgstr = request.data["game_image"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["game_id"]}-{uuid.uuid4()}.{ext}')

        game_picture.action_pic = data

        try:
            game_picture.save()
            serializer = GamePictureSerializer(game_picture, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception:
            return HttpResponse(Exception)

class GamePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePicture
        fields = '__all__'
