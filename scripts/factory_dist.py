import argparse
import urllib.request
import json

from math import sin, cos, sqrt, atan2, radians

radius = 3958.8  # radius of the erf in miles

# Tesla factory coordinates in Fremont, CA
tesla_lat = radians(37.493530)
tesla_lon = radians(-121.942162)

url = "https://nominatim.openstreetmap.org/search?format=json&state=%s&city=%s"
state_url = "https://nominatim.openstreetmap.org/search?format=json&state=%s"


def get_factory_dist(state, city):
    lat, lon = -1, -1
    if type(state) != str or not state:
        return -1

    if type(city) != str or not city:
        lat, lon = get_state_center(state)
    else:
        lat, lon = get_city_center(state, city)

        if lat == -1 or lon == -1:
            lat, lon = get_state_center(state)

    if lat == -1 or lon == -1:
        return -2

    dlat = tesla_lat - lat
    dlon = tesla_lon - lon

    a = sin(dlat / 2) ** 2 + cos(tesla_lat) * cos(lat) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return int(radius * c)


def get_city_center(state, city):
    q = url % (urllib.parse.quote(state), urllib.parse.quote(city))

    data = urllib.request.urlopen(q).read()
    j = json.loads(data.decode('utf-8'))

    for entry in j:
        if entry['class'] == 'place' and entry['type'] == 'city':
            return radians(float(entry['lat'])), radians(float(entry['lon']))

    return -1, -1

def get_state_center(state):
    q = state_url % (urllib.parse.quote(state))

    data = urllib.request.urlopen(q).read()
    j = json.loads(data.decode('utf-8'))

    for entry in j:
        if entry["class"] == "boundary" and "United States of America" in entry["display_name"]:
            return radians(float(entry['lat'])), radians(float(entry['lon']))

    return -1, -1



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--state', type=str, required=True)
    parser.add_argument('-c', '--city', type=str, required=True)

    args = parser.parse_args()

    print(get_factory_dist(args.state, args.city))


if __name__ == "__main__":
    main()
