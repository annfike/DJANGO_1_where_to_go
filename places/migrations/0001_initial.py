# Generated by Django 4.0.1 on 2022-01-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название экскурсии')),
                ('description_short', models.CharField(blank=True, default='', max_length=256, verbose_name='Краткое описание')),
                ('description_long', models.CharField(blank=True, default='', max_length=256, verbose_name='Подробное описание')),
                ('lat', models.FloatField(default=55, verbose_name='долгота')),
                ('lon', models.FloatField(default=55, verbose_name='широта')),
            ],
            options={
                'verbose_name': 'Экскурсия',
                'verbose_name_plural': 'Экскурсии',
            },
        ),
    ]
