# Generated by Django 4.2.5 on 2023-11-12 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0008_alter_itineraryevent_itineraryevent_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraryevent',
            name='itineraryEvent_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 12, 9, 20, 16, 651368, tzinfo=datetime.timezone.utc)),
        ),
    ]
