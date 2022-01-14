from django.db import models


class Excursion(models.Model):
    title = models.CharField('Название экскурсии', max_length=50)
    description_short = models.CharField('Краткое описание', max_length=256, blank=True, default='')
    description_long = models.CharField('Подробное описание', max_length=256, blank=True, default='')
    lat = models.FloatField(default=55, verbose_name='долгота')
    lon = models.FloatField(default=55, verbose_name='широта')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'
