from django.shortcuts import render
from places.models import Excursion, Image
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def place_details(request, place_id):
    excursion = get_object_or_404(Excursion, pk=place_id)
    images = [image.photo.url for image in excursion.photos.all()]
    response_data = {
        "title": excursion.title,
        "imgs": images,
        "description_short": excursion.description_short,
        "description_long": excursion.description_long,
        "coordinates": {"lat": excursion.lat, "lng": excursion.lon},
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})

