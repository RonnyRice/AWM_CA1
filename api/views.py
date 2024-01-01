from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from itinerary.models import ItineraryPlan, ItineraryEvent
from .serializer import ItineraryPlanSerializer, ItineraryEventSerializer


class listItinerary(generics.ListAPIView):
    queryset = ItineraryPlan.objects.all()
    serializer_class = ItineraryPlanSerializer


class listItineraryEvent(generics.ListAPIView):
    queryset = ItineraryEvent.objects.all()
    serializer_class = ItineraryEventSerializer
