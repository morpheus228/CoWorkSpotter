from datetime import datetime

from tgbot.misc import replicas
from places.models import Place
from tgbot.spotters.meta_place import MetaPlace


def get_place_text(place: Place, meta_place: MetaPlace) -> str:
    w_h = Timetable(place.timetable).is_open_now()
    sml1 = sml1_dict[place.type]
    sml2 = sml2_dict[place.type]

    return replicas.place.substitute(
        sml1=sml1,
        sml2=sml2,
        name=place.name,
        desc=place.about,
        url=place.url,
        w_h=w_h,
        distance=round(meta_place.distance, 2),
        ymaps=place.ymaps)


sml1_dict = {'CW': '📖',
             'F': '💻'}

sml2_dict = {'CW': '📖',
             'F': '🍵'}


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

