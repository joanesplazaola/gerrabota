from random import shuffle

import geopandas as gpd
from constants import aukerak

from helpers import jaso_kolore_ilunak


def ezarri_kolorea(datuak):
	for i, row in datuak.iterrows():
		datuak.at[i, 'kolorea'] = koloreak[i % len(koloreak)]
	return datuak


def gorde_json(gdf, fitxategi_izena):
	gdf.to_file(f"data/{fitxategi_izena}.geojson", driver='GeoJSON')


def irakurri_shapelet(ezarpenak):
	gdf = gpd.read_file(f'data/{ezarpenak["fitxategia"]}.shp')
	gdf.rename(columns=ezarpenak["izenak"], inplace=True)
	return gdf


koloreak = jaso_kolore_ilunak()
shuffle(koloreak)

for key, val in aukerak.items():
	datuak = irakurri_shapelet(val)
	datuak = ezarri_kolorea(datuak)
	datuak['jabea'] = datuak['izena']

	gorde_json(datuak, val['fitxategia'])
