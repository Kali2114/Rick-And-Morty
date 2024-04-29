from django.urls import path

from .views import LocationView

urlpatterns = [
    path('location_view', LocationView.as_view(), name='location_view')
]
