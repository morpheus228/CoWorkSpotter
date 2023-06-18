from typing import List
from bs4 import BeautifulSoup


class YmapsParser:
    def __init__(self):
        self.soup = None

    def get_name(self):
        try:
            return self.soup.find("h1", {"itemprop": "name"}).getText()
        except Exception:
            return None

    def get_url(self):
        try:
            return self.soup.find("a", {"itemprop": "url"}).getText()
        except Exception:
            return None

    def get_timetable(self) -> dict:
        try:
            week_days = self.soup.find_all("meta", {"itemprop": "openingHours"})
            return {str(i[0]): self.encode_office_hours(i[1].get("content")) for i in zip(range(1, 8), week_days)}

        except Exception:
            return {}

    def get_location(self):
        try:
            location = self.soup.find("div", {
                'class': 'card-feature-view _view_normal _size_large _interactive card-share-view__coordinates'}).getText()
            return [float(x) for x in location.split(', ')]

        except Exception:
            return None, None

    def get_ymaps(self):
        try:
            return self.soup.find("div", {'class': 'card-share-view__text'}).getText()
        except Exception:
            return

    @staticmethod
    def encode_office_hours(office_hours: str) -> List[List[int]]:
        hours = list(office_hours.split(" "))[1]
        opening_hour, closing_hour = hours.split('-')
        return [list(map(int, opening_hour.split(':'))), list(map(int, closing_hour.split(':')))]

    def parse(self, soup_text: str) -> dict:
        self.soup = BeautifulSoup(soup_text, 'lxml')

        latitude, longitude = self.get_location()
        ymaps = self.get_ymaps()
        name = self.get_name()
        url = self.get_url()
        timetable = self.get_timetable()

        return {
            'name': name,
            'ymaps': ymaps,
            'url': url,
            'timetable': timetable,
            'latitude': latitude,
            'longitude': longitude
        }