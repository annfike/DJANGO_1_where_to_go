from places.models import Excursion
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def place_details(request, place_id):
    excursion = get_object_or_404(Excursion, pk=place_id)
    photos_urls = [image.photo.url for image in excursion.images.all()]
    response_context = {
        "title": excursion.title,
        "imgs": photos_urls,
        "description_short": excursion.description_short,
        "description_long": excursion.description_long,
        "coordinates": {"lat": excursion.lat, "lng": excursion.lon},
    }
    return JsonResponse(response_context, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
