from typing import List

from tgbot.misc.location import Location
from tgbot.models import Place

from tgbot.spotters.spotters.spotter import Spotter
from tgbot.spotters.applicators.filter import DistanceFilter
from tgbot.spotters.applicators.sorting import DistanceSorting


class NearSpotter(Spotter):
    def __init__(self, batch_size: int):
        super().__init__(batch_size=batch_size)

    @staticmethod
    def get_places() -> List[Place]:
        return list(Place.objects.only('latitude', 'longitude'))

    def generate(self, user_location: Location):
        super().generate()
        self.mpl.set_external_args(user_location=user_location)
        self.mpl.apply(DistanceSorting())
        self.mpl.apply(DistanceFilter(max_distance=5))
