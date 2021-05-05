from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    designer = models.CharField(max_length=100)
    release_year = models.IntegerField
    num_of_players = models.CharField(max_length=20)
    time_to_play = models. IntegerField
    ages = models.CharField(max_length=20)