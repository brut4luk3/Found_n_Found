from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from ..models import Place

def detail(request, place_id):

    place = get_object_or_404(Place, pk=place_id)

    context = {
        'place': place
    }

    return render(request, 'places/detail.html', context=context)