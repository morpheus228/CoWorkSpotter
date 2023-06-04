from typing import List

from tgbot.misc.location import Location
from tgbot.misc.meta_place import MetaPlace
from tgbot.models import Place


class Spotter:
    def __init__(self, batch_size: int):
        self.batch_size = batch_size
        self.current_id = -self.batch_size
        self.sorted_meta_places = None

    @staticmethod
    def get_place_ids() -> List[int]:
        return Place.objects.values_list('id', flat=True)

    def __next__(self) -> MetaPlace:
        self.current_id += self.batch_size

        if self.current_id < len(self.sorted_meta_places):
            return self.sorted_meta_places[self.current_id: self.current_id + self.batch_size]
        else:
            raise StopIteration

    def get_meta_places(self, location) -> List[MetaPlace]:
        pass

    def generate(self, *args, **kwargs) -> List[MetaPlace]:
        pass


class NearSpotter(Spotter):
    def __init__(self, batch_size: int):
        super().__init__(batch_size)

    def get_meta_places(self, location: Location) -> List[MetaPlace]:
        places_ids = self.get_place_ids()
        meta_places = [MetaPlace(places_id).calc_distance(location) for places_id in places_ids]
        return meta_places

    def generate(self, location: Location):
        meta_places = self.get_meta_places(location)
        self.sorted_meta_places = sorted(meta_places, key=lambda meta_place: meta_place.distance)
