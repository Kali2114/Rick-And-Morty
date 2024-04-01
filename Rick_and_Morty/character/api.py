from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .serializers import CharacterSerializer, LocationSerializer, EpisodeSerializer


class CharacterApiView(APIView):
    def get(self, request, *args, **kwargs):
        api_url = 'https://rickandmortyapi.com/api/character'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            results = data['results']
            return Response(results)
        else:
            return Response({"error": "Nie udało się pobrać danych z API Rick and Morty"},
                            status=response.status_code)