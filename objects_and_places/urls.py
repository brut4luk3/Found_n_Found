from django.urls import path

from .views import objects_views

urlpatterns = [
    path('', objects_views.index, name='index_objects'),
]