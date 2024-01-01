from rest_framework import serializers
from itinerary.models import Profile, ItineraryPlan, ItineraryEvent


class ItineraryPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryPlan
        fields = ["ItineraryPlan_id", "ItineraryPlan_title", "ItineraryPlan_description", "user"]


class ItineraryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryEvent
        fields = ["ItineraryEvent_id", "ItineraryPlan_id" "ItineraryEvent_title", "itineraryEvent_description",
                  "itineraryEvent_datetime", "lon", "lat" "location"]

