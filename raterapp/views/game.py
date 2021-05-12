from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapp.models import User, Game, Category, CategoryGame

class GameViewSet(ViewSet):
    def create(self, request):
        game = Game()

        game.title = request.data["title"]
        game.description = request.data["description"]
        game.designer = request.data["designer"]
        game.release_year = request.data["releaseYear"]
        game.num_of_players = request.data["numOfPlayers"]
        game.time_to_play = request.data["timeToPlay"]
        game.min_age = request.data["minAge"]

        categories = Category.in_bulk(request.data["categories"])
        CategoryGame.set(categories)

        try:
            game.save()
            serializer = GameSerializer(game, context={"request": request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

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
