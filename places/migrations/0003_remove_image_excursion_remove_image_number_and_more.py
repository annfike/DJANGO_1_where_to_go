# Generated by Django 4.0.1 on 2022-01-14 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='excursion',
        ),
        migrations.RemoveField(
            model_name='image',
            name='number',
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.excursion', verbose_name='название'),
        ),
    ]