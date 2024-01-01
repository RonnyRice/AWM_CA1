from datetime import datetime

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

    # If user hasn't set an option to view Itinerary plan (0) or find Itinerary plan (1) set the default as 0.
    if 'user_itinerary_option_session' not in request.session:
        user_itinerary_option = "0"
    else:
        user_itinerary_option = request.session["user_itinerary_option_session"]

    # If option is to find itinerary plan find all plans that are publicly available and doesn't belong to current user
    if user_itinerary_option == "1":
        user_ItineraryPlan = ItineraryPlan.objects.filter(sharedStatus=True).exclude(user=request.user.id)

    # if option is to view itinerary plan find all plans belonging to user
    if user_itinerary_option == "0":
        user_ItineraryPlan = ItineraryPlan.objects.filter(user=request.user.id)

    # If user selected an itinerary plan
    if 'user_ItineraryPlanSelected_ID' in request.session and user_ItineraryPlan:
        # Get the selected itinerary plan and events that take place
        try:
            user_ItineraryPlanSelected = user_ItineraryPlan.get(
                ItineraryPlan_id=int(request.session["user_ItineraryPlanSelected_ID"]))

            user_ItineraryEventsSelected = ItineraryEvent.objects.filter(
                ItineraryPlan_id=int(request.session["user_ItineraryPlanSelected_ID"])).order_by(
                'itineraryEvent_datetime')
        except Exception as e:
            user_ItineraryPlanSelected = None
            user_ItineraryEventsSelected = None
            # Return to the homepage with desired options and data
    return render(request, 'home.html', {"user_ItineraryPlan": user_ItineraryPlan,
                                         "user_ItineraryPlanSelected": user_ItineraryPlanSelected,
                                         "user_ItineraryEventsSelected": user_ItineraryEventsSelected,
                                         "user_itinerary_option": user_itinerary_option})


@login_required
def addItinerary(request):
    # ensures that the request is POST and creates a new itinerary event setting teh shared option default to faulse
    if request.POST:
        try:
            ItineraryPlan_models = ItineraryPlan(None,
                                                 request.POST["itineraryPlan_name"],
                                                 request.POST["itineraryPlan_desc"],
                                                 request.user.id,
                                                 False)
            ItineraryPlan_models.save()

            return redirect('home')
        except Exception as e:
            return render(request, 'Error.html', {'error_message': str(e)}, status=404)

    return render(request, "home.html")


@login_required
def updateItineraryShared(request):
    # Ensures the request is POST and is used to update the sharedStatus if the user wants to publicly share the plan
    if request.POST:
        try:
            ItineraryPlan_selected = ItineraryPlan.objects.get(ItineraryPlan_id=int(request.POST["ItineraryPlan_id"]),
                                                               user=request.user.id)
            ItineraryPlan_selected.sharedStatus = request.POST["ItineraryPlan_SharedOption"] == 'True'
            ItineraryPlan_selected.save()

            return redirect('home')
        except Exception as e:
            return render(request, 'Error.html', {'error_message': str(e)}, status=404)
    return render(request, "home.html")


@login_required
def addItineraryEvent(request):
    # Ensures the request is POST and adds details for the itinerary event, if there is no currentDate set the default as now
    if request.POST:
        try:
            lon = float(request.POST["itineraryEvent_Longitude"])
            lat = float(request.POST["itineraryEvent_Latitude"])
            currentDateTime = request.POST["itineraryEvent_DateTime"]
            if not currentDateTime:
                currentDateTime = datetime.now()
            ItineraryPlanEvent_models = ItineraryEvent(None,
                                                       request.session["user_ItineraryPlanSelected_ID"],
                                                       request.POST["itineraryEvent_name"],
                                                       request.POST["itineraryEvent_desc"],
                                                       currentDateTime,
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
    # Ensures the Request is POST  Used to set the selected Itinerary event session,  ensures when the page refreshes
    # the event is saved for the convenience of the user to prevent them from always clicking the desired event
    request.session["user_ItineraryPlanSelected_ID"] = request.POST["itinerary_link_value"]
    return redirect('home')


@login_required
def updateUserLocation(request):
    # Ensures the request is POST updates the location of the user last recorded
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
def deleteItineraryEvent(request):
    # Deletes itinerary event
    if request.POST:
        try:
            ItineraryEvent.objects.filter(ItineraryEvent_id=int(request.POST['ItineraryEvent_id'])).delete()
            return redirect('home')
        except Exception as e:
            return render(request, 'Error.html', {'error_message': str(e)}, status=404)

    return render(request, "home.html")


@login_required
def deleteItineraryPlan(request):
    # Deletes the itinerary plan as well as the events as it cascades
    if request.POST:
        try:
            ItineraryPlan.objects.filter(ItineraryPlan_id=int(request.POST['ItineraryPlan_id'])).delete()
            return redirect('home')

        except Exception as e:
            return render(request, 'Error.html', {'error_message': str(e)}, status=404)

    return render(request, "home.html")


@login_required
def getItneraryOption(request):
    # Creates an itinerary plan option for the convenience of the user, when the page refreshes the option is saved
    # ensuring that they don't have to keep selecting the desired option
    request.session["user_itinerary_option_session"] = request.POST["user_itinerary_option"]
    return redirect('home')


def offline(request):
    # default offline page
    return render(request, "offline.html")
