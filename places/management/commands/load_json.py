from pathlib import Path
from django.core.management import BaseCommand
from places.models import Excursion
import json
import requests
from io import BytesIO
import os


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--dir', default='./upload', type=str, help='Путь к папке с файлами JSON')

    def handle(self, *args, **kwargs):
        dir_path = kwargs['dir']
        for file in os.listdir(dir_path):
            file = f'{dir_path}/{file}'
            load_json_file(file)
        

def load_json_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        excursions_raw = json.load(f)

        title = excursions_raw.get('title')
        description_short = excursions_raw.get('description_short', 'description is coming soon')
        description_long = excursions_raw.get('description_long', 'description is coming soon')
        coordinates = excursions_raw.get('coordinates')
        if coordinates:
            lng = coordinates['lng']
            lat = coordinates['lat']
        else:
            lng = 37.374
            lat = 55.455

        if title:
            excursion, created = Excursion.objects.update_or_create(
                  title=title,
                  defaults={
                        'description_short': description_short,
                        'description_long': description_long,
                        'lon': lat,
                        'lat': lng
                  },
                  )

        imgs_urls = excursions_raw.get('imgs')
        for number, img_url in enumerate(imgs_urls, 1):
            response = requests.get(img_url)
            response.raise_for_status()
            img = BytesIO(response.content)
            image, created = excursion.images.get_or_create(
                  excursion=excursion.id, number=number
            )
            img_name = os.path.basename(img_url)
            image.photo.save(img_name, img, save=True)
