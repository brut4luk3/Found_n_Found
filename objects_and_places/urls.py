from django.urls import path

from .views import rooms_views, places_views

app_name = 'objects_and_places'

urlpatterns = [
    path('rooms/', rooms_views.index, name='index_rooms'),
    path('rooms/<int:room_id>/', rooms_views.detail, name='detail_rooms'),

    path('places/<int:place_id>/', places_views.detail, name='detail_places')
]