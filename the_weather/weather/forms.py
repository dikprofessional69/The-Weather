from django.forms import ModelForm, TextInput
from .models import City


# yah Trough database ma add garne ho
class CityForm(ModelForm):
    class Meta:  # adding features
        model = City  # yesle poit garxa City table ma
        fields = ['name']

