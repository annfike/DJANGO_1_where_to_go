from django.shortcuts import render
from places.models import Excursion

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
            "detailsUrl": "./static/places/moscow_legends.json"
          }
        }
      excursions["features"].append(feature)

    context = {
        'excursions': excursions
    }

    return render(request, 'index.html', context)