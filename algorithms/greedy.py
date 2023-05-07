"""
We have a bunch of radistations
Each one covers a number of location
Get the set of a minimum number of stations, covering a maximum number of location
"""

RADIO_FREEDOM = {"a", "b"}
UGLY_WAVE = {"x", "y", "z"}
PURITY_STATION = {"c", "d", "e"}
FLYING_PASTA_MOSTER = {"y", "z"}
ROOGE_ONE_STATION = {"b", "z"}
METROID_STATION = {"d", "z"}
AMSTERDAM_STATION = {"a", "c", "e"}
REBEL_ONE = {"m"}
DOOMSY = {"b"}

ALL_STATIONS = {
    "RADIO_FREEDOM": RADIO_FREEDOM,
    "UGLY_WAVE": UGLY_WAVE,
    "PURITY_STATION": PURITY_STATION,
    "FLYING_PASTA_MOSTER": FLYING_PASTA_MOSTER,
    "ROOGE_ONE_STATION": ROOGE_ONE_STATION,
    "METROID_STATION": METROID_STATION,
    "AMSTERDAM_STATION": AMSTERDAM_STATION,
    "REBEL_ONE": REBEL_ONE,
    "DOOMSY": DOOMSY,
}


def get_optimum_cover(stations, covered=None):

    if not covered:
        covered = set()

    if not stations:
        return covered

    biggest_station, coverage = sorted(
        stations.items(), key=lambda k_v: len(k_v[1]), reverse=True
    )[0]

    print(biggest_station)

    covered.update(coverage)
    del stations[biggest_station]

    new_stations = {}

    for station in stations:
        new_coverage = stations[station].difference(coverage)
        if new_coverage:
            new_stations[station] = new_coverage

    return get_optimum_cover(new_stations, covered=covered)


print(get_optimum_cover(ALL_STATIONS))
