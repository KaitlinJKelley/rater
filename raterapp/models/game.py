from raterapp.models.review import Review
from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    designer = models.CharField(max_length=100)
    release_year = models.IntegerField(default=0)
    num_of_players = models.CharField(max_length=20)
    time_to_play = models. IntegerField(default=0)
    min_age = models.IntegerField(default=21)
    categories = models.ManyToManyField("Category", through="CategoryGame")

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = Review.objects.filter(game=self)

        # Sum all of the ratings for the game
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating

        self.__average_rating = total_rating/len(ratings)