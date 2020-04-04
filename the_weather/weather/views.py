from django.http import request
from django.shortcuts import render

import requests

from .models import City
from .forms import CityForm


# Create your views here.
# hard coded single city code
# def index(request):
#     print("INDEX:")
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8954063b9de4b22f3df186847e3111a8'
#     city = 'Kathmandu'
#     print("url.format(city)")
#     print(url.format(city))
#     print("requests.get(url.format(city)).json()")
#
#     city_weather = requests.get(url.format(city)).json()
#     # print(city_weather)
#     weather = {
#         'city': city,
#         'temperature': city_weather['main']['temp'],
#         'description': city_weather['weather'][0]['description'],
#         'icon': city_weather['weather'][0]['icon']
#     }
#     print(weather)
#
#     context = {'weather': weather}#nesting weather dictionary into context with key weather
#     #so template can access by weather key then go deeper to city key
#
#     return render(request, 'weather/index.html',context)


def index(request):
    print("INDEX:")
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8954063b9de4b22f3df186847e3111a8'
    cities = City.objects.all()
    ###
    form = CityForm()
    # must try catch for empty names now.
    if request.method == "POST":
        if request.POST.get('name') is not None:
            print(request.POST.get("name"))
            form = CityForm(request.POST)
            form.save()

        if request.POST.get('cross') is not None:
            row = City.objects.filter(name=request.POST.get('cross'))
            row.delete()

    weather = []
    # now we need a list where each city ko weather will be appended like before but dictionaries appended on a list

    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        try:
            single_weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
        except:
            print("error")
            City.objects.filter(name=request.POST.get('name')).delete()
            continue

        weather.append(single_weather)  # appending dictionary}

    context = {'weather': weather, 'form': form}
    return render(request, 'weather/index.html', context)
