from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import json

from points.models import Place
from points.forms import PlaceForm
from pygeocoder import Geocoder


def show_places(request):
    places = Place.objects.all()

    # Render the template depending on the context.
    return render(request, 'points/index.html', {'places': places})


def my_places(request):
    # Entry.objects.all().filter(pub_date__year=2006)
    user = request.user
    places = Place.objects.all().filter(author=user)

    # Render the template depending on the context.
    return render(request, 'points/my_places.html', {'places': places})


def add_place(request):
    form = PlaceForm(request.POST or None)
    if form.is_valid():
        place = form.save(commit=False)
        place.author = request.user

        results = Geocoder.geocode(place.address)
        lat, lng = results[0].coordinates

        place.latitude = lat
        place.longitude = lng

        place.save()
        return redirect('../../points/')
    return render_to_response('points/add_place.html', {'form': form}, context_instance=RequestContext(request))


def map_view(request):
    if request.is_ajax():
        upper_left_lat = request.GET['upper_left_lat']
        upper_left_lng = request.GET['upper_left_lng']
        lower_left_lat = request.GET['lower_left_lat']
        lower_left_lng = request.GET['lower_left_lng']

        places = Place.objects.all().filter(latitude__gte=lower_left_lat, longitude__gte=lower_left_lng, latitude__lte=upper_left_lat, longitude__lte=upper_left_lng)

        spots = {}
        for place in places:
            temp = {}
            temp['address'] = place.address
            temp['name'] = place.name
            spots[place.name] = temp

        json_data = json.dumps(spots)

        return HttpResponse(json_data)

    # Render the template depending on the context.
    return render(request, 'points/map_view.html')