from pathlib import Path
import json
import csv

TRACTS_PATH = Path('static', 'data', 'tracts.json')
CRIMES_PATH = Path('static', 'data', 'crimes.csv')

def get_tracts():
    return json.loads(TRACTS_PATH.read_text())

def get_crimes():
    txtlines = CRIMES_PATH.read_text().splitlines()
    return list(csv.DictReader(txtlines))

