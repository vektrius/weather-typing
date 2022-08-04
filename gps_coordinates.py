from types import NoneType
from typing import NamedTuple

from geopy.geocoders import Nominatim



from exceptions import CantGetCoordinates


class Coordinates(NamedTuple):
    latitude : float
    longitude : float

def get_coordinates(city : str) -> Coordinates:
    """ Returns the coordinates of the given city """
    geolocator = Nominatim(user_agent="gps_coordinates")
    location = geolocator.geocode(city)
    if location is NoneType:
        raise CantGetCoordinates

    return Coordinates(latitude=location.latitude, longitude=location.longitude)
