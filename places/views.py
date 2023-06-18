from django.shortcuts import render
from django.views import View

from places.forms import PlaceForm
from places.models import Place
from yandex_maps.simple_parser import YmapsParser


def str2list(s: str):
    return list(s.strip().split(', '))


class HomeView(View):
    def get(self, request):
        return render(request, 'places/home.html')


class PlaceAddView(View):
    def get(self, request):
        context = {'form': PlaceForm()}
        return render(request, 'places/add_place.html', context)

    def post(self, request):
        form = PlaceForm(request.POST)

        if form.is_valid():
            ymaps_data = YmapsParser().parse(form.cleaned_data['ymaps_soup'])
            form_data = form.cleaned_data
            place = Place.objects.create(
                        name=ymaps_data['name'] if form_data['take_ymaps_name'] else form_data['name'],
                        description='',
                        about='',
                        url=ymaps_data['url'],
                        type=form_data['type'],
                        timetable=ymaps_data['timetable'],
                        ymaps=ymaps_data['ymaps'],
                        latitude=ymaps_data['latitude'],
                        longitude=ymaps_data['longitude'],
                        attributes={"minimum_entry": form_data['minimum_entry'],
                                    "socket_availability": form_data['socket_availability'],
                                    "entertainments": str2list(form_data['entertainments']),
                                    "furniture": str2list(form_data['furniture']),
                                    "own_food_ability": form_data['own_food_ability'],
                                    "food_availability": form_data['food_availability'],
                                    "water_availability": form_data['water_availability'],
                                    "toilets_availability": form_data['toilets_availability'],
                                    "device_rental": str2list(form_data['device_rental']),
                                    "consumables_rental": str2list(form_data['consumables_rental']),
                                    "lecture_hall_rental": form_data['lecture_hall_rental'],
                                    "capacity": form_data['capacity'],
                                    "quiet_place_availability": form_data['quiet_place_availability'],
                                    "call_place_availability": form_data['call_place_availability']})

            return render(request, 'places/added.html', {'place_name': place.name})
        return render(request, 'places/add_place.html', {'form': form})

