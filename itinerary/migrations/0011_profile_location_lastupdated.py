# Generated by Django 4.2.5 on 2023-11-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0010_alter_itineraryevent_itineraryevent_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location_lastUpdated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]