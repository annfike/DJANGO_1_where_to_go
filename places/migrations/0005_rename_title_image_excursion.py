# Generated by Django 4.0.1 on 2022-01-15 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_image_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='title',
            new_name='excursion',
        ),
    ]
