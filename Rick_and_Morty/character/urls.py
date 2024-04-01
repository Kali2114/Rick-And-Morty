from django.urls import path

from .api import CharacterApiView
from .views import CharacterView

urlpatterns = [
    path('api/characters/', CharacterApiView.as_view(), name='characters_api'),
    path('character_view/', CharacterView.as_view(), name='character_view'),
]
