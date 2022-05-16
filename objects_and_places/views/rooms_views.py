from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from ..models import Room, Place


def index(request):

    rooms_list = Room.objects.all()

    context = {
        'rooms_list': rooms_list
    }

    return render(request, 'rooms/index.html', context=context)

def detail(request, place_id):

    places_list = get_object_or_404(Place, pk=place_id)

    context = {
        'places_list': places_list
    }

    return render(request, 'rooms/detail.html', context=context)