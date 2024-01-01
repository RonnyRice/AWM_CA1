from django.contrib import admin
from django.contrib.auth.models import User

from itinerary.models import Profile, ItineraryPlan, ItineraryEvent

# Register your models here.

admin.site.register(Profile)
admin.site.register(ItineraryPlan)
admin.site.register(ItineraryEvent)


