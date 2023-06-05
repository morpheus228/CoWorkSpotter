from typing import List

from tgbot.models import Place
from tgbot.spotters.meta_place import MetaPlacesAggregator, MetaPlace


class Spotter:
    def __init__(self, batch_size: int):
        self.mpl: MetaPlacesAggregator = None

        self.batch_size: int = batch_size
        self.current_id: int = -self.batch_size

    @staticmethod
    def get_places() -> List[Place]:
        pass

    def generate(self, *args, **kwargs) -> List[MetaPlace]:
        self.mpl = MetaPlacesAggregator(self.get_places())

    def __next__(self) -> MetaPlace:
        self.current_id += self.batch_size

        if self.current_id < len(self.mpl.meta_places):
            return self.mpl.meta_places[self.current_id: self.current_id + self.batch_size]
        else:
            raise StopIteration
