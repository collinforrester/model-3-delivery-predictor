import argparse
import urllib.request
import json

from math import sin, cos, sqrt, atan2, radians

radius = 3958.8  # radius of the erf in miles

# Tesla factory coordinates in Fremont, CA
tesla_lat = radians(37.493530)
tesla_lon = radians(-121.942162)

url = "https://nominatim.openstreetmap.org/search?format=json&state=%s&city=%s"


def get_factory_dist(state, city):
    q = url % (state, city)

    data = urllib.request.urlopen(q).read()
    j = json.loads(data.decode('utf-8'))

    for entry in j:
        if entry['class'] == 'place' and entry['type'] == 'city':
            lat = radians(float(entry['lat']))
            lon = radians(float(entry['lon']))

            dlat = tesla_lat - lat
            dlon = tesla_lon - lon

            a = sin(dlat / 2) ** 2 + cos(tesla_lat) * cos(lat) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            return int(radius * c)

    raise Exception("didn't find your city")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--state', type=str, required=True)
    parser.add_argument('-c', '--city', type=str, required=True)

    args = parser.parse_args()

    print(get_factory_dist(args.state, args.city))


if __name__ == "__main__":
    main()
