from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("addItinerary/", views.addItinerary, name="addItinerary"),
    path("selectItineraryEvent/", views.selectItineraryEvent, name="selectItineraryEvent"),
    path("addItineraryEvent/", views.addItineraryEvent, name="addItineraryEvent"),
    path("updateUserLocation/", views.updateUserLocation, name="updateUserLocation"),
    path("updateItineraryShared/", views.updateItineraryShared, name="updateItineraryShared"),
    path("deleteItineraryEvent/", views.deleteItineraryEvent, name="deleteItineraryEvent"),
    path("deleteItineraryPlan/", views.deleteItineraryPlan, name="deleteItineraryPlan"),
    path("getItneraryOption/", views.getItneraryOption, name="getItneraryOption"),

]

ALLOWED_HOSTS = ['*']

