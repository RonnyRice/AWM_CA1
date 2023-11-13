from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("addItinerary/", views.addItinerary, name="addItinerary"),
    path("selectItineraryEvent/", views.selectItineraryEvent, name="selectItineraryEvent"),
    path("addItineraryEvent/", views.addItineraryEvent, name="addItineraryEvent"),
    path("updateUserLocation/", views.updateUserLocation, name="updateUserLocation"),
    path("deleteItineraryEvent/", views.deleteItineraryEvent, name="deleteItineraryEvent"),
    path("deleteItineraryPlan/", views.deleteItineraryPlan, name="deleteItineraryPlan"),
]

ALLOWED_HOSTS = ['*']

