from django.contrib import admin

from itinerary.models import Profile, ItineraryPlan, ItineraryEvent, User

# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(ItineraryPlan)
admin.site.register(ItineraryEvent)


