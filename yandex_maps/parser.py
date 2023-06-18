import logging
from typing import List

import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class YmapsParser:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')

        self.driver = uc.Chrome(options=options)
        self.soup = None

    def get_name(self):
        self.upload_soup()

        try:
            return self.soup.find("h1", {"itemprop": "name"}).getText()
        except Exception:
            return None

    def get_url(self):
        self.upload_soup()

        try:
            return self.soup.find("a", {"itemprop": "url"}).getText()
        except Exception:
            return None

    def get_timetable(self) -> dict:
        self.upload_soup()

        try:
            week_days = self.soup.find_all("meta", {"itemprop": "openingHours"})
            return {str(i[0]): self.encode_office_hours(i[1].get("content")) for i in zip(range(1, 8), week_days)}

        except Exception:
            return {}

    def get_location(self) -> List[float]:
        while True:
            while True:
                logging.error("Попытка нажать на кнопку")
                try:
                    self.driver.find_element(By.XPATH, '//button[@aria-label="Поделиться"]').click()
                    break
                except Exception as error:
                    print(error)

            for i in range(3):
                logging.error("Попытка получить данные")

                try:
                    self.upload_soup()
                    location = self.soup.find("div", {'class': 'card-feature-view _view_normal _size_large _interactive card-share-view__coordinates'}).getText()
                    return [float(x) for x in location.split(', ')]

                except Exception as error:
                    print(error)

    @staticmethod
    def encode_office_hours(office_hours: str) -> List[List[int]]:
        hours = list(office_hours.split(" "))[1]
        opening_hour, closing_hour = hours.split('-')
        return [list(map(int, opening_hour.split(':'))), list(map(int, closing_hour.split(':')))]

    def upload_soup(self):
        self.soup = BeautifulSoup(self.driver.page_source, "lxml")

    def parse(self, url: str) -> dict:
        self.driver.get(url)

        location = self.get_location()
        name = self.get_name()
        url = self.get_url()
        timetable = self.get_timetable()

        return {
            'name': name,
            'url': url,
            'timetable': timetable,
            'latitude': location[0],
            'longitude': location[1],
        }