from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class CategoryGame(models.Model):
    game = ForeignKey('Game', on_delete=CASCADE)
    category = ForeignKey('Category', on_delete=CASCADE)