# Generated by Django 4.0.1 on 2022-02-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_alter_excursion_description_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='images', verbose_name='картинка'),
        ),
    ]
