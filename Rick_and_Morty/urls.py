from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('character/', include('Rick_and_Morty.character.urls')),
    path('location/', include('Rick_and_Morty.location.urls')),
    path('episode/', include('Rick_and_Morty.episode.urls')),
]
