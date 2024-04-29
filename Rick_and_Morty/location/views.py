from django.views import View
from django.shortcuts import render
import requests

class LocationView(View):
    template_name = 'location_view.html'

    def get(self, request, *args, **kwargs):
        api_url = 'https://rickandmortyapi.com/api/location'
        try:
            response = requests.get(api_url)
            characters = response.json()['results'] if response.status_code == 200 else []
        except requests.RequestException:
            context = {'error_message': 'Failed to load data from the Rick and Morty API'}
            return render(request, self.template_name, context)

        return render(request, self.template_name, {'characters': characters})
