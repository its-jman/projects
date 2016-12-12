import json
import urllib
import math

from secret import GMAPS_KEY

GMAPS_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='


# URL -> JSON Parser comes from:
# http://stackoverflow.com/questions/13921910/python-urllib2-receive-json-response-from-url
# Posted by: Martijn Pieters
def get_json(loc_string):  # Returns the JSON from google geocoding API
    # print GMAPS_URL + loc_string.replace(' ', '+') + GMAPS_KEY
    return json.loads(urllib.urlopen(GMAPS_URL + loc_string.replace(' ', '+') + GMAPS_KEY).read())  # Changed json.load to json.loads and added .read()


def get_coordinates(json_data):  # Parses JSON and returns coords for the middle of the box given
    try:
        current_json = json_data['results'][0]['geometry']['bounds']
    except KeyError:
        current_json = json_data['results'][0]['geometry']['viewport']
    sw = current_json['southwest']
    ne = current_json['northeast']
    midpoint = get_midpoint([sw['lat'], sw['lng']], [ne['lat'], ne['lng']])
    return math.radians(midpoint[0]), math.radians(midpoint[1])


def get_midpoint(coords_one, coords_two):  # Returns midpoint of two coordinates
    return (coords_one[0] + coords_two[0]) / 2, (coords_one[1] + coords_two[1]) / 2


def app_engine_return(from_location, to_location):
    loc_one_coords = get_coordinates(get_json(str(from_location)))  # Parsing JSON into each location's coordinates
    loc_two_coords = get_coordinates(get_json(str(to_location)))
    # System below is the distance formula provided by:
    # http://andrew.hedges.name/experiments/haversine/
    dlon = loc_two_coords[1] - loc_one_coords[1]
    dlat = loc_two_coords[0] - loc_one_coords[0]
    a = (math.sin(dlat / 2) ** 2) + (math.cos(loc_one_coords[0])
                                     * math.cos(loc_two_coords[0]) * (math.sin(dlon / 2) ** 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return str(format(3961 * c, '.2f'))