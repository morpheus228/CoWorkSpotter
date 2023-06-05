from tgbot.spotters.applicators.applicator import Applicator


class Filter(Applicator):
    pass


class DistanceFilter(Filter):
    def __init__(self, max_distance):
        super().__init__(meta_info_list=['distance'])
        self.max_distance = max_distance

    def apply(self, meta_places):
        return [meta_place for meta_place in meta_places if meta_place.distance <= self.max_distance]
