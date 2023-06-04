from abc import abstractmethod, ABC
from datetime import datetime
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


def num_to_time(n: int) -> str:
    return (str(n), '0' + str(n))[n < 10]


def string_time(time_: list) -> str:
    if time_[0] == -1:
        return 'Выходной'
    return num_to_time(time_[0]) + ':' + num_to_time(time_[1])


def get_hour_from_time(time_: str) -> int:
    return int(time_[:2])


class Timetable:
    def __init__(self, timetable: dict):
        self.timetable = timetable

    def get_working_hours(self) -> str:
        week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        timetable_str = ''
        for day in self.timetable.keys():
            timetable_str += f'{week[int(day) - 1]}\t{self.get_hours_by_day(day)}'
            # opening = string_time(timetable[day][0])
            # closing = string_time(timetable[day][1])
            # if opening == 'Выходной':
            #     timetable_str += f'{week[int(day) - 1]}\t{opening}\n'
            #     continue
            # elif opening == closing:
            #     timetable_str += 'Круглосуточно'
            # timetable_str += f'{week[int(day) - 1]}\t{opening}-{closing}\n'
        return timetable_str

    def get_hours_by_day(self, day: str) -> tuple:
        opening = string_time(self.timetable[day][0])
        closing = string_time(self.timetable[day][1])
        return opening, closing

    def get_today_hours(self) -> str:
        today = str(datetime.today().weekday() + 1)
        opening, closing = self.get_hours_by_day(today)
        if opening == 'Выходной':
            return 'Выходной'
        if opening == closing:
            return 'Круглосуточно'
        return f'{opening}-{closing}'

    def is_open_now(self) -> str:
        today = str(datetime.today().weekday() + 1)
        opening, closing = self.get_hours_by_day(today)
        if opening == 'Выходной':
            return 'Сейчас закрыто'
        elif opening == closing:
            return 'Открыто круглосуточно'
        elif get_hour_from_time(opening) < get_hour_from_time(str(datetime.now().time())) < get_hour_from_time(closing):
            return f'Открыто до {closing}'
        return 'Сейчас закрыто'


