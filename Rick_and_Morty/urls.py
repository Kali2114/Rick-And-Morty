from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .character.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home_view'),
    path('character/', include('Rick_and_Morty.character.urls')),
    path('location/', include('Rick_and_Morty.location.urls')),
    path('episode/', include('Rick_and_Morty.episode.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
