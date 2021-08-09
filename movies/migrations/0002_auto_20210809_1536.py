# Generated by Django 3.2.6 on 2021-08-09 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='world_premier',
            field=models.DateField(default=datetime.date(2021, 8, 9), verbose_name='Премьера в мире'),
        ),
    ]