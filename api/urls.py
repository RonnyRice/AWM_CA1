
from django.urls import path
from .views import listItinerary, listItineraryEvent

urlpatterns = [
    path("itinerary", listItinerary.as_view()),
    path("itineraryEvent", listItineraryEvent.as_view())
]

