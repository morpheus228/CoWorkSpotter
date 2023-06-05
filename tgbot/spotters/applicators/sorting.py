from tgbot.spotters.applicators.applicator import Applicator


class Sorting(Applicator):
    pass


class DistanceSorting(Sorting):
    def __init__(self):
        super().__init__(meta_info_list=['distance'])

    def apply(self, meta_places):
        return sorted(meta_places, key=lambda meta_place: meta_place.distance)
