from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
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


@receiver(post_save, sender=get_user_model())
def manage_user_profile(sender, instance, created, **kwargs):
    try:
        my_profile = instance.profile
        my_profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance, lon=10, lat=10)


# profile config stores last recorded location and user that has nullable values
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


# Itinerary plan belongs to the user
# Uses an incrementing int primary key
# Uses the "Default title" for null values
# has the user as foreign key indicating ownership and maintaining consistency
# sharedStatus is default set to False
class ItineraryPlan(models.Model):
    ItineraryPlan_id = models.AutoField(primary_key=True)
    ItineraryPlan_title = models.CharField(max_length=100, default="Default title")
    ItineraryPlan_description = models.TextField(help_text="Enter the description of this holiday", blank=True)
    user = models.ForeignKey(defaultUserModel, default=None, on_delete=models.CASCADE)
    sharedStatus = models.BooleanField(default=False)


# uses an incrementing primary key
# has the Itinerary Plan as a foreign key indicating that the events list belong to the plan
# has a default value for event title "Default title" for null values
# Date time is set default as now incase no value was found.
# event stores the longitude and latitude of the event used for the leaflet markers
class ItineraryEvent(models.Model):
    ItineraryEvent_id = models.AutoField(primary_key=True)
    ItineraryPlan_id = models.ForeignKey(ItineraryPlan, on_delete=models.CASCADE)
    ItineraryEvent_title = models.CharField(max_length=100, default="Default title")
    itineraryEvent_description = models.TextField(help_text="Enter the description of this event")
    itineraryEvent_datetime = models.DateTimeField(default=now)
    lon = models.FloatField()
    lat = models.FloatField()
    location = gis_models.PointField(null=True)
