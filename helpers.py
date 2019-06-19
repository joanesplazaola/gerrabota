from random import random
from geopandas.plotting import plot_series
import matplotlib.pyplot as plt
import geopandas as gpd
from constants import aukerak


def jaso_datuak(modua):
	gdf = gpd.read_file(f'data/{aukerak[modua]["fitxategia"]}')
	gdf.rename(columns=aukerak[modua]["izenak"], inplace=True)
	return gdf


def jaso_kolore_ilunak():
	from matplotlib import colors as mcolors
	all_colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS, )
	filtered_colors = dict()
	for color, val in all_colors.items():
		hue, s, v = mcolors.rgb_to_hsv(mcolors.to_rgb(val))
		if s > 0.2 and v < 0.9: filtered_colors[color] = val
	return list(filtered_colors.keys())


def jaso_azalera(eremua):
	return eremua.to_crs({'proj': 'cea'}).map(lambda p: p.area / 10 ** 6).iloc[0]


def jaso_puntuazioa(eremua):
	return jaso_azalera(eremua['geometry'])


def konkistatu(erasotzailea, erasotua):
	erasotzailea_puntu = jaso_puntuazioa(erasotzailea)
	erasotua_puntu = jaso_puntuazioa(erasotua)
	return erasotzailea_puntu * random() > erasotua_puntu * random()


def erakutsi_mapa(inperioak, lurralde_koloreak, ax):
	for i, row in inperioak.iterrows():
		plot_series(inperioak.loc[[i], 'geometry'], ax=ax, color=lurralde_koloreak[row['jabea']])
	plt.pause(0.0001)
	plt.draw()


def mugakidea_jaso(gdf, erasotzailea):
	mugakideak = gdf[gdf.geometry.touches(erasotzailea.iloc[0]['geometry'])]
	ez_bereak = mugakideak[mugakideak['jabea'] != erasotzailea.iloc[0].jabea]
	if ez_bereak.empty:  # TODO Hau Biarnoko herri/eskualde bategaittik dago, ez dauka mugakideik...
		return []
	return ez_bereak.sample().iloc[0]
