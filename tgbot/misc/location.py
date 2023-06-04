class Location:
    def __init__(self, object_):
        self.latitude = object_.latitude
        self.longitude = object_.longitude

    def as_tuple(self) -> tuple:
        return self.latitude, self.longitude
