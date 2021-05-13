from raterapp.models.game import Game
from raterapp.models import Review, User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponseServerError
from django.contrib.auth.models import User as AuthUser

class GameReviewVewSet(ViewSet):
    def create(self, request):
        reviewer = User.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["gameId"])

        review = Review()
        review.game = game
        review.reviewer = reviewer
        review.text = request.data["text"]
        review.rating = request.data["rating"]

        try:
            review.save()
            serializer = ReviewSerializer(review, context={"request": request})

            return Response(serializer.data)
            
        except Exception:
            return HttpResponseServerError(Exception)
        
class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        fields = ["first_name", "last_name"]

class ReviewerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["user"]

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('__all__')