# Generated by Django 4.0.1 on 2022-01-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_image_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='картинка'),
        ),
    ]