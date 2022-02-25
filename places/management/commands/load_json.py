import logging
from django.core.management import BaseCommand
from places.models import Excursion
import json
import requests
from io import BytesIO
import os


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--dir', default='upload', type=str, help='Название папки с файлами JSON')

    def handle(self, *args, **kwargs):
        dir = kwargs['dir']
        try:
            load_json(dir)
        except Exception as error:
            logging.error(error)


def load_json(dir):
    for file in os.listdir(f'./{dir}'):
        file = f'{dir}/{file}'
        load_json_file(file)


def load_json_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        places = json.load(f)

        title = places.get('title', 'There is no title')
        description_short = places.get('description_short', 'There is no description_short')
        description_long = places.get('description_long', 'There is no description_long')
        coordinates = places.get('coordinates')
        if coordinates:
            lng = coordinates['lng']
            lat = coordinates['lat']
        else:
            lng = 37.374
            lat = 55.455

        excursion, created = Excursion.objects.update_or_create(
            title=title,
            defaults={
                  'description_short': description_short,
                  'description_long': description_long,
                  'lon': lat,
                  'lat': lng
            },
            )

        imgs = places.get('imgs')
        for number, img in enumerate(imgs, 1):
            response = requests.get(img)
            response.raise_for_status()
            i = BytesIO(response.content)
            image, created = excursion.photos.get_or_create(
                  excursion=excursion.id, number=number
            )
            img_name = os.path.basename(img)
            image.photo.save(img_name, i, save=True)
