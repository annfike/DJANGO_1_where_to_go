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


class Image(models.Model):
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, verbose_name='название')
    photo = models.ImageField(blank=True, upload_to='media', verbose_name='картинка')
    number = models.PositiveIntegerField('Номер', default=0, blank=False, null=False)

    def __str__(self):
        return f'{self.number} {self.excursion.title}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

