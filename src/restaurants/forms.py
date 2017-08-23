from django import forms
from .models import RestaurantLocation



class RestaurantCreateForm(forms.Form):
    name        = forms.CharField(label='Name', max_length=120)
    location    = forms.CharField(label='Location', required=False)
    category    = forms.CharField(label='Category', required=False)


class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
        ]