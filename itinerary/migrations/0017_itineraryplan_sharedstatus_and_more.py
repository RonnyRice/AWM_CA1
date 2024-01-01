# Generated by Django 4.2.7 on 2024-01-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0016_remove_itineraryplan_sharedstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='itineraryplan',
            name='sharedStatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='itineraryplan',
            name='ItineraryPlan_title',
            field=models.CharField(default='Default title', max_length=100),
        ),
    ]
