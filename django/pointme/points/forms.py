from django import forms
from points.models import Place


class PlaceForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    address = forms.CharField(max_length=200)
    rating = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Place
        exclude = ['author', 'latitude', 'longitude']