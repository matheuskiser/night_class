from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

from points.models import Place
from points.forms import PlaceForm


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
        place.save()
        return redirect('../../points/')
    return render_to_response('points/add_place.html', {'form': form}, context_instance=RequestContext(request))


def map_view(request):

    # Render the template depending on the context.
    return render(request, 'points/map_view.html')