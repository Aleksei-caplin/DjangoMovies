# Generated by Django 3.2.6 on 2021-08-15 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210809_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезда рейтинга'},
        ),
        migrations.AlterField(
            model_name='movie',
            name='world_premier',
            field=models.DateField(default=datetime.date(2021, 8, 15), verbose_name='Премьера в мире'),
        ),
    ]
