# Generated by Django 4.0.1 on 2022-02-18 16:19

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_alter_excursion_description_short'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Номер'),
        ),
    ]