from typing import List

from geopy.distance import geodesic as GD

from tgbot.misc.location import Location
from places.models import Place
from tgbot.spotters.applicators.applicator import Applicator


class MetaPlacesAggregator:
    def __init__(self, places: List[Place]):
        self.meta_places = [MetaPlace(place) for place in places]

        # External arguments
        self.user_location: Location = None

        self.meta_info_history = {
            'distance': False
        }

    @staticmethod
    def get_meta_info_list(spotter_methods: List[Applicator]) -> List[str]:
        return list({
            meta_info for spotter_method in spotter_methods
            for meta_info in spotter_method.meta_info_list
        })

    def set_external_args(self, user_location=None):
        self.user_location = user_location

    def apply(self, applicator: Applicator):
        for meta_info in applicator.meta_info_list:

            if not self.meta_info_history[meta_info]:

                for meta_place in self.meta_places:
                    meta_place.meta_info_to_method[meta_info](self)

                self.meta_info_history[meta_info] = True

        self.meta_places = applicator.apply(self.meta_places)


class MetaPlace:
    def __init__(self, place: Place):
        self.place: Place = place

        # Meta info:
        self.distance: float = None

        self.meta_info_to_method = {
            'distance': self.set_distance
        }

    def set_distance(self, mpa: MetaPlacesAggregator):
        place_location = Location(self.place)
        user_location = mpa.user_location
        self.distance = GD(place_location.as_tuple(), user_location.as_tuple()).km
