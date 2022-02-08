from django.shortcuts import render
from places.models import Excursion, Image
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def place_details(request, id):
    place = get_object_or_404(Excursion, pk=id)
    images = [image.photo.url for image in Image.objects.filter(excursion=place)]
    response_data = {
        "title": place.title,
        "imgs": images,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lat": place.lat, "lng": place.lon},
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})

