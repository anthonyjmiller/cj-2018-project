import geopandas as gpd
import pandas as pd
from pathlib import Path
from shapely.geometry import Point
from data import CRIMES_PATH, CRIMES_GEOPATH, SHAPES_PATH

# https://gist.github.com/nygeog/2731427a74ed66ca0e420eaa7bcd0d2b

def add_tract_id_to_crimes(crimes_path=CRIMES_PATH,
                           shapes_path=SHAPES_PATH,
                           dest_path=CRIMES_GEOPATH):

    crimes = pd.read_csv(CRIMES_PATH)
    shapes = gpd.read_file(str(SHAPES_PATH))

    crimepoints = [Point(c) for c in zip(crimes.Longitude, crimes.Latitude)]
    # make a geoframe out of crimes data
    geodf = gpd.GeoDataFrame(crimes, geometry=crimepoints, crs=shapes.crs)
    # then join it to the tract shapes
    jdf = gpd.sjoin(geodf, shapes, op='within', how='left')

    # the jdf dataframe now has the fips code needed to come up with 'tract_id'
    # and we just append it to the crimes dataframe
    crimes['tract_id'] = '1400000' + 'US' + jdf.statefp10 + jdf.countyfp10 +  jdf.geoid10

    # remove the 'geometry' column before writing to file
    data = crimes.drop(['geometry'], axis=1)
    data.to_csv(CRIMES_GEOPATH, index=False)


if __name__ == '__main__':
    print('Using', SHAPES_PATH)
    print('to add `tract_id` to:', CRIMES_PATH)
    add_tract_id_to_crimes()
    print('Wrote to:', CRIMES_GEOPATH)
