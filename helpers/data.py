from pathlib import Path
import json
import csv

TRACTS_PATH = Path('static', 'data', 'tracts.json')
CRIMES_PATH = Path('static', 'data', 'crimes.csv')
SHAPES_PATH = Path('static', 'data', 'boundaries.geojson')
CRIMES_GEOPATH = Path('static', 'data', 'tractcrimes.csv')


def get_tracts():
    return json.loads(TRACTS_PATH.read_text())

def get_crimes():
    txtlines = CRIMES_GEOPATH.read_text().splitlines()
    return list(csv.DictReader(txtlines))

