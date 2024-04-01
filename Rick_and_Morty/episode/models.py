from django.db import models
import datetime
from django.utils import timezone

class Episode(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    air_date = models.CharField(max_length=255)
    episode = models.CharField(max_length=255)
    characters = models.ManyToManyField('character.Character', related_name='episodes')
    url = models.URLField()
    created = models.CharField(max_length=255)
