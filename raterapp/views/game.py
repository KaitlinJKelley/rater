from raterapp.models.review import Review
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapp.models import User, Game, Category, CategoryGame
from django.contrib.auth.models import User as AuthUser

class GameViewSet(ViewSet):
    def create(self, request):
        game = Game()

        game.title = request.data["title"]
        game.description = request.data["description"]
        game.designer = request.data["designer"]
        game.release_year = request.data["releaseYear"]
        game.num_of_players = request.data["numberOfPlayers"]
        game.time_to_play = request.data["timeToPlay"]
        game.min_age = request.data["minAge"]

        categories = Category.objects.in_bulk(request.data["categories"])

        try:
            game.save()
            game.categories.set(categories)
            
            serializer = GameSerializer(game, context={"request": request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):

        try:
            game = Game.objects.get(pk=pk)

            game_serializer = GameSerializer(game, context={'request': request})

            return Response(game_serializer.data)
        except Exception:
            return HttpResponseServerError(Exception)

    def list(self, request):

            games = Game.objects.all() 
            serializer = GameSerializer(games, many=True, context={'request': request})  

            return Response(serializer.data)         

class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        fields = ["first_name", "last_name"]

class ReviewerSerializer(serializers.ModelSerializer):
    user = AuthUserSerializer(many=False)

    class Meta:
        model = User
        fields = ("user",)

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = ReviewerSerializer(many=False)

    class Meta:
        model = Review
        fields = ('reviewer', 'text', 'rating', 'date_created')

class GameSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Game
        fields = ('id','title', 'description', 'designer', 'release_year', 'num_of_players', 'time_to_play', 'min_age', 'categories','average_rating', 'reviews')
        depth = 1

