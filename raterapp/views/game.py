from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapp.models import User, Game, Category

class GameViewSet(ViewSet):
    def retrieve(self, request, pk):

        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={"request": request})

            return Response(serializer.data)
        except Exception:
            return HttpResponseServerError(Exception)

    def list(self, request):

            games = Game.objects.all() 
            serializer = GameSerializer(games, many=True, context={'request': request})  

            return Response(serializer.data)         

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__')
