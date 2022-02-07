from django.shortcuts import render
from places.models import Excursion
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def place_details(request, id):
    place = get_object_or_404(Excursion, pk=id)
    return HttpResponse(place.title)

