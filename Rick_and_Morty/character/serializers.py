from rest_framework import serializers
import requests

from ..episode.serializers import EpisodeSerializer
from ..location.serializers import LocationSerializer
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    origin = LocationSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    episode = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = '__all__'