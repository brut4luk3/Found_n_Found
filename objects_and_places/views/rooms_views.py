from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from ..models import Room


def index(request):

    rooms_list = Room.objects.all()

    context = {
        'rooms_list': rooms_list
    }

    return render(request, 'rooms/index.html', context=context)