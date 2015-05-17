from django import forms
from django.forms import Textarea
from points.models import Place


class PlaceForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    address = forms.CharField(max_length=200)
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 5}))
    like = forms.BooleanField(initial=True, required=False)
    # rating = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Place
        fields = ['name', 'address', 'comment', 'like']