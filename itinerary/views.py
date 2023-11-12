from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point

from django.shortcuts import render, redirect

from .models import ItineraryPlan
from .models import ItineraryEvent
from .models import Profile


# Create your views here.

def index(request):
    user_ItineraryPlanSelected = []
    user_ItineraryEventsSelected = []
    user_ItineraryPlan = []

    user_ItineraryPlan = ItineraryPlan.objects.filter(user=request.user.id)
    if 'user_ItineraryPlanSelected_ID' in request.session:
        user_ItineraryPlanSelected = user_ItineraryPlan.get(
            ItineraryPlan_id=int(request.session["user_ItineraryPlanSelected_ID"]))

        user_ItineraryEventsSelected = ItineraryEvent.objects.filter(
            ItineraryPlan_id=int(request.session["user_ItineraryPlanSelected_ID"]))

    return render(request, 'home.html', {"user_ItineraryPlan": user_ItineraryPlan,
                                         "user_ItineraryPlanSelected": user_ItineraryPlanSelected,
                                         "user_ItineraryEventsSelected": user_ItineraryEventsSelected})


@login_required
def addItinerary(request):
    if request.POST:
        try:
            ItineraryPlan_models = ItineraryPlan(None,
                                                 request.POST["itineraryPlan_name"],
                                                 request.POST["itineraryPlan_desc"],
                                                 request.user.id)
            ItineraryPlan_models.save()
            return redirect('home')
        except Exception as e:
            return render(request, 'Error.html', {'error_message': str(e)}, status=404)

    return render(request, "home.html")


@login_required
def addItineraryEvent(request):
    if request.POST:
        try:
            lon = float(request.POST["itineraryEvent_Longitude"])
            lat = float(request.POST["itineraryEvent_Latitude"])
            ItineraryPlanEvent_models = ItineraryEvent(None,
                                                       request.session["user_ItineraryPlanSelected_ID"],
                                                       request.POST["itineraryEvent_name"],
                                                       request.POST["itineraryEvent_desc"],
                                                       request.POST["itineraryEvent_DateTime"],
                                                       lon,
                                                       lat,
                                                       Point(lon, lat, srid=4326))
            ItineraryPlanEvent_models.save()
            return redirect('home')

        except Exception as e:
            return render(request, 'Error.html', {'error_message': str(e)}, status=404)

    return render(request, "home.html")


@login_required
def selectItineraryEvent(request):
    request.session["user_ItineraryPlanSelected_ID"] = request.POST["itinerary_link_value"]
    return redirect('home')


@login_required
def updateUserLocation(request):
    if request.POST:
        try:
            user_lon = float(request.POST["user_lon"])
            user_lat = float(request.POST["user_lat"])
            Profile_models = Profile.objects.get(user=request.user)

            Profile_models.lon = user_lon
            Profile_models.lat = user_lat
            Profile_models.location = Point(user_lon, user_lat, srid=4326)
            Profile_models.save()
            return redirect('home')

        except Exception as e:
            return render(request, 'Error.html', {'error_message': str(e)}, status=404)

    return render(request, "home.html")


@login_required
def newItineraryView(request):
    return render(request, "newitinerary.html")
