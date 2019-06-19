from enum import Enum


class Modua(Enum):
	ESKUALDEKA = 1
	HERRIALDEKA = 2
	HERRIKA = 3


aukerak = {
	Modua.ESKUALDEKA: {
		'izenak': {'es_iz_e_2': 'izena', 'es_kod_2': 'kodea'},
		'fitxategia': 'Eskualdeak.shp',
	},
	Modua.HERRIKA: {
		'izenak': {'iz_euskal': 'izena', 'ud_kodea': 'kodea'},
		'fitxategia': 'udalerriak.shp'
	},
	Modua.HERRIALDEKA: {
		'izenak': {'he_iz_e': 'izena', 'he_kod': 'kodea'},
		'fitxategia': 'Herrialdeak.shp',
	},
}
