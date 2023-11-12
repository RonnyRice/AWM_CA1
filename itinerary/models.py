from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

defaultUserModel = get_user_model()


# Create your models here.
# Optional custom user model Can be set up later
class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=15)

    def __str__(self):
        return str(self.username)


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.PROTECT,
        primary_key=True,
    )
    lon = models.FloatField()
    lat = models.FloatField()
    location = gis_models.PointField(null=True)
    location_lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lon), str(self.lat)


class ItineraryPlan(models.Model):
    ItineraryPlan_id = models.AutoField(primary_key=True)
    ItineraryPlan_title = models.CharField(max_length=100, default=" default title")
    ItineraryPlan_description = models.TextField(help_text="Enter the description of this holiday", blank=True)
    user = models.ForeignKey(defaultUserModel, default=None, on_delete=models.CASCADE)


class ItineraryEvent(models.Model):
    ItineraryEvent_id = models.AutoField(primary_key=True)
    ItineraryPlan_id = models.ForeignKey(ItineraryPlan, on_delete=models.CASCADE)
    ItineraryEvent_title = models.CharField(max_length=100, default="default title")
    itineraryEvent_description = models.TextField(help_text="Enter the description of this event")
    itineraryEvent_datetime = models.DateTimeField(default=now)
    lon = models.FloatField()
    lat = models.FloatField()
    location = gis_models.PointField(null=True)