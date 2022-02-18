import logging
from django.core.management import BaseCommand
from places.models import Excursion
import json
import requests
from io import BytesIO
import os


    
class Command(BaseCommand):
      def add_arguments(self, parser):
        parser.add_argument('-f', '--dir', type=str, help='Название папки с файлами JSON')

      def handle(self, *args, **kwargs):
            dir = kwargs['dir']
            if dir:
                  dir = dir
            else:
                  dir = 'upload'
            try:
                  load_json(dir)
            except Exception as error:
                  logging.error(error)



def load_json(dir):
      for file_json in os.listdir(f'./{dir}'):

            with open(f'{dir}/{file_json}', 'r', encoding='utf-8') as f: 
                  file = json.load(f) 

            title = file.get('title')
            description_short = file.get('description_short')
            description_long = file.get('description_long')
            lng = file.get('coordinates')['lng']
            lat = file.get('coordinates')['lat']

            
            excursion, created = Excursion.objects.update_or_create(
                  title = title,
                  description_short = description_short,
                  description_long = description_long,
                  lon = lat,
                  lat = lng
                  )
            excursion.save()

            imgs = file.get('imgs')
            for number, img in enumerate(imgs, 1):
                  r = requests.get(img)
                  i = BytesIO(r.content)
                  image, created = excursion.photos.get_or_create(
                  excursion=excursion.id, number=number
                  )
                  img_name = os.path.basename(img)
                  image.photo.save(img_name, i, save=True)
            

      

 






      # for group in file:
      #       if group == 'PM':
      #             pm_group = file[group]
      #             for pm in pm_group:
      #                   name = pm.get('name')
      #                   tg_username = pm.get('tg_username')
      #                   discord_username = pm.get('discord_username')
      #                   time_slots = pm.get('time_slots')

      #                   pm, _ = ProductManager.objects.get_or_create(
      #                         name = name,
      #                         tg_username = tg_username,
      #                         discord_username = discord_username,
      #                         )
      #                   pm.save()

      #                   for time_slot in time_slots:
      #                         time_slot = datetime.datetime.strptime(time_slot, "%H:%M")
      #                         timeslot, _ = Time.objects.get_or_create(
      #                               time_interval = time_slot, pm = pm)                       
      #                         timeslot.save()

      #       if group == 'Student':
      #             student_group = file[group]
      #             for student in student_group:
      #                   name = student.get('name')
      #                   tg_username = student.get('tg_username')
      #                   discord_username = student.get('discord_username')
      #                   student_level = student.get('level')

      #                   level, _ = StudentLevel.objects.get_or_create(
      #                         name = student_level)
      #                   level.save()
                        
      #                   student, _ = Student.objects.get_or_create(
      #                         name = name,
      #                         tg_username = tg_username,
      #                         discord_username = discord_username,
      #                         )
      #                   student.level = level
      #                   student.save()
                              
                        
                        

                        
                    

                        

      