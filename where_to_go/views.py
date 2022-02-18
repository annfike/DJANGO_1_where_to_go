from django.shortcuts import render
from places.models import Excursion
from django.urls import reverse


def index(request):
    excursions = Excursion.objects.all()
    serialized_excursions  = {
      "type": "FeatureCollection",
      "features": []
    }

    for excursion in excursions:
      feature = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [excursion.lat, excursion.lon]
          },
          "properties": {
            "title": excursion.title,
            "placeId": excursion.id,
            "detailsUrl": reverse('places:place_details', args=[excursion.id,]),
          }
        }
      serialized_excursions["features"].append(feature)

    context = {
        'excursions': serialized_excursions
    }

    return render(request, 'index.html', context)