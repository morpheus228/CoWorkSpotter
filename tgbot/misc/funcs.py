from typing import List, Tuple

from geopy.distance import geodesic as GD

from tgbot.models import Pub


def calc_distance(first_coords, second_coords):
    return GD(first_coords, second_coords).km


def get_nearest_pubs(location, n=3) -> List[Tuple[Pub, float]]:
    pubs = Pub.objects.values('id', 'latitude', 'longitude')
    pub_distance_dict = {pub['id']: calc_distance(location, (pub['latitude'], pub['longitude'])) for pub in pubs}
    nearest_pub_pairs = sorted(pub_distance_dict.items(), key=lambda j: j[1], reverse=True)[:n]
    nearest_pub_pairs = [(Pub.objects.get(id=i[0]), i[1]) for i in nearest_pub_pairs]
    return nearest_pub_pairs

