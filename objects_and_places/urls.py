from django.urls import path

from .views import rooms_views

app_name = 'objects_and_places'

urlpatterns = [
    path('', rooms_views.index, name='index_rooms'),
]