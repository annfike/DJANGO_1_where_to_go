# Generated by Django 4.0.1 on 2022-02-08 18:05

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_excursion_options_alter_image_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Подробное описание'),
        ),
    ]