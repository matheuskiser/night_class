from django.shortcuts import render
from points.models import Place


def show_places(request):

    places = Place.objects.all()

    # Render the template depending on the context.
    return render(request, 'points/index.html', {'places': places})
