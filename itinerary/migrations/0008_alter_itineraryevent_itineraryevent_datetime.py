# Generated by Django 4.2.5 on 2023-11-12 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0007_itineraryevent_itineraryevent_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraryevent',
            name='itineraryEvent_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 12, 9, 19, 16, 512779, tzinfo=datetime.timezone.utc)),
        ),
    ]
