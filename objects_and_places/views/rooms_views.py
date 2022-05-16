from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from ..models import Room, Place, Object

def index(request):

    rooms_list = Room.objects.all()

    context = {
        'rooms_list': rooms_list
    }

    return render(request, 'rooms/index.html', context=context)

def detail(request, room_id):

    room = get_object_or_404(Place, pk=room_id)

    context = {
        'room': room
    }

    return render(request, 'rooms/detail.html', context=context)