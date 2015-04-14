from django import forms
from points.models import Place


class PlaceForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the name of the place.")
    address = forms.CharField(max_length=200, help_text="Please enter the address of the place.")
    rating = forms.IntegerField(min_value=1, max_value=5, help_text="Please enter the rating for this place.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Place
        exclude = ['author']