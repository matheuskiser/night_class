from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.db.models import Q
import json

from points.models import Place
from points.forms import PlaceForm
from pygeocoder import Geocoder


def show_places(request):

    places = Place.objects.all()

    # Render the template depending on the context.
    return render(request, 'points/index.html', {'places': places})


def my_places(request):
    # # Entry.objects.all().filter(pub_date__year=2006)
    # user = request.user
    # places = Place.objects.all().filter(author=user)
    #
    # # Render the template depending on the context.
    # return render(request, 'points/my_places.html', {'places': places})
    if request.is_ajax():
        upper_left_lat = request.GET['upper_left_lat']
        upper_left_lng = request.GET['upper_left_lng']
        lower_left_lat = request.GET['lower_left_lat']
        lower_left_lng = request.GET['lower_left_lng']

        user = request.user

        places = Place.objects.all().filter(latitude__gte=lower_left_lat, longitude__gte=lower_left_lng,
                                            latitude__lte=upper_left_lat, longitude__lte=upper_left_lng,
                                            author=user)

        spots = []
        for place in places:
            temp = {}
            temp['id'] = place.id
            temp['address'] = place.address
            temp['name'] = place.name
            temp['rating'] = place.rating
            temp['user_name'] = place.author.username
            spots.append(temp)

        return HttpResponse(json.dumps(spots))

    # Render the template depending on the context.
    return render(request, 'points/my_places.html')



def search_results(request):
    query = request.GET['search-query']

    places = Place.objects.filter(Q(name__icontains=query) | Q(address__icontains=query))

    return render(request, 'points/search_results.html', {'places': places, 'query': query})


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

        spots = []
        for place in places:
            temp = {}
            temp['id'] = place.id
            temp['address'] = place.address
            temp['name'] = place.name
            temp['rating'] = place.rating
            temp['user_name'] = place.author.username
            spots.append(temp)

        return HttpResponse(json.dumps(spots))

    # Render the template depending on the context.
    return render(request, 'points/map_view.html')


def get_places(request):
    if request.is_ajax():
        places = Place.objects.all()

        spots = []
        for place in places:
            temp = {}
            temp['id'] = place.id
            temp['address'] = place.address
            temp['name'] = place.name
            temp['rating'] = place.rating
            temp['user_name'] = place.author.username
            spots.append(temp)

        return HttpResponse(json.dumps(spots))

    return HttpResponse("0")