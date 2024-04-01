from django.views import View
from django.shortcuts import render
import requests

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class CharacterView(View):
    template_name = 'character_view.html'

    def get(self, request, *args, **kwargs):
        api_url = 'https://rickandmortyapi.com/api/character'
        try:
            response = requests.get(api_url)
            characters = response.json()['results'] if response.status_code == 200 else []
        except requests.RequestException:
            context = {'error_message': 'Failed to load data from the Rick and Morty API'}
            return render(request, self.template_name, context)

        return render(request, self.template_name, {'characters': characters})
