from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class Review(models.Model):
    reviewer = ForeignKey("User", on_delete=CASCADE)
    game = ForeignKey("Game", on_delete=CASCADE, related_name="reviews")
    text = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)