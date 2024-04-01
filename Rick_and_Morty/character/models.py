from django.db import models

class Character(models.Model):
    id = models.SmallIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255)
    origin = models.ForeignKey('location.Location', on_delete=models.CASCADE,
                                 related_name='origin_characters')
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE,
                                 related_name='location_characters')
    image = models.URLField(max_length=200)
    episode = models.ManyToManyField('episode.Episode', related_name='episode_number')
    url = models.URLField(max_length=200)
    created = models.CharField(max_length=255)

    def __str__(self):
        return self.name
