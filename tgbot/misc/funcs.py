from abc import abstractmethod, ABC
from typing import Tuple

from geopy.distance import geodesic as GD

from tgbot.models import Place
from dataclasses import dataclass


class Coords:
    def __init__(self, latitude=None, longitude=None):
        self.latitude = latitude
        self.longitude = longitude

    def as_tuple(self) -> tuple:
        return (self.latitude, self.longitude)

    def from_dict(self, dict_: dict):
        self.latitude = dict_['latitude']
        self.longitude = dict_['longitude']
        return self


def calc_distance(first_coords: Coords, second_coords: Coords):
    return GD(first_coords.as_tuple(), second_coords.as_tuple()).km


class Spotter(ABC):
    @abstractmethod
    def get_places(self, user_coords: Coords):
        pass


class NearSpotter(Spotter):
    def get_places(self, user_coords: Coords):
        places = list(Place.objects.values('id', 'latitude', 'longitude'))
        sorted_places = sorted(places, key=lambda place: calc_distance(user_coords, Coords().from_dict(place)))
        return sorted_places


def places_all_info(places):
    for place in places:
        yield Place.objects.get(pk=place['id'])
