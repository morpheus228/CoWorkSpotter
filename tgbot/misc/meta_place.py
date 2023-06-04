from geopy.distance import geodesic as GD

from tgbot.misc.location import Location
from tgbot.models import Place


class MetaPlace:
    def __init__(self, place_id: int):
        self.place_id = place_id
        self.distance = None

    def calc_distance(self, other_location: Location):
        self_location = Location(Place.objects.get(pk=self.place_id).only('latitude', 'longitude'))
        self.distance = GD(self_location.as_tuple(), other_location.as_tuple()).km
        return self

