from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    dimension = models.CharField(max_length=255)
    residents = models.ManyToManyField('character.Character', related_name='residing_locations')
    url = models.URLField(max_length=200)
    created = models.CharField(max_length=255)
