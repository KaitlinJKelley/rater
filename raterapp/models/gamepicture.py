from raterapp.models.game import Game
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class GamePicture(models.Model):
    user = ForeignKey("User", on_delete=CASCADE)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING, related_name='pictures')
    action_pic = models.ImageField(
        upload_to='actionimages', height_field=None,
        width_field=None, max_length=None, null=True)