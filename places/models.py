from django.db import models
from tinymce.models import HTMLField


class Excursion(models.Model):
    title = models.CharField('Название экскурсии', max_length=50)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Подробное описание', blank=True)
    lat = models.FloatField(verbose_name='долгота')
    lon = models.FloatField(verbose_name='широта')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'
        ordering = ['title']


class Image(models.Model):
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, verbose_name='название', related_name='photos',)
    photo = models.ImageField(upload_to='images', verbose_name='картинка')
    number = models.PositiveIntegerField('Номер', default=0, blank=True)

    def __str__(self):
        return f'{self.number} {self.excursion.title}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['number']

