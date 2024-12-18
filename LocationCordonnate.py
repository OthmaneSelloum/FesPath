import geopy
from geopy.geocoders import Nominatim
import LocationExtraction as LE

geolocator = Nominatim(user_agent="my_geocoder")

coordinates = LE.matrice_adj()

def loca(coordinate=coordinates,locations_dict={}):
    for coord in coordinate:
        location = geolocator.reverse(coord, language="fr")
        locations_dict[location.address] = coord
    return locations_dict
