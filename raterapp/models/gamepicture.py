from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class GamePicture(models.Model):
    user = ForeignKey("User", on_delete=CASCADE)
    game = ForeignKey("Game", on_delete=CASCADE)
    image = models.ImageField(upload_to='images/', verbose_name="")