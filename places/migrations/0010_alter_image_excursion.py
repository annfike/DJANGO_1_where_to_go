# Generated by Django 4.0.1 on 2022-02-10 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_excursion_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='excursion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='places.excursion', verbose_name='название'),
        ),
    ]
