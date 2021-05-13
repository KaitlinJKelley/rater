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