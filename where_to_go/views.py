from django.shortcuts import render
from places.models import Excursion
from django.urls import reverse


def index(request):
    places = Excursion.objects.all()
    excursions  = {
      "type": "FeatureCollection",
      "features": []
    }

    for place in places:
      feature = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lat, place.lon]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse('places:place_details', args=[place.id,]),
          }
        }
      excursions["features"].append(feature)

    context = {
        'excursions': excursions
    }

    return render(request, 'index.html', context)