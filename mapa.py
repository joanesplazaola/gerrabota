from helpers import jaso_datuak, erakutsi_mapa, mugakidea_jaso, konkistatu
from constants import Modua
import matplotlib.pyplot as plt

datuak = jaso_datuak(Modua.ESKUALDEKA)
lurralde_koloreak = dict(zip(datuak.izena, datuak.kolorea))
inperioak = datuak
plt.ion()
fig, ax = plt.subplots()
erakutsi_mapa(inperioak, lurralde_koloreak, ax)
while inperioak.shape[0] > 1:
	erasotzailea = inperioak.sample()
	lurraldea = mugakidea_jaso(datuak, erasotzailea)
	if len(lurraldea) == 0:
		continue
	erasotua = inperioak[inperioak['jabea'] == lurraldea.jabea]
	if konkistatu(erasotzailea, erasotua):
		datuak.loc[datuak['izena'] == lurraldea.izena, 'jabea'] = erasotzailea.iloc[0].jabea
		norena = ''
		if erasotua.iloc[0].jabea != lurraldea.izena:
			norena = f' {erasotua.iloc[0].jabea}(r)ena zen'

		print(f'{erasotzailea.iloc[0].jabea}(e)k{norena} {lurraldea.izena} konkistatu du.')
		# TODO Hemen erakutsi beharko lirateke erasotzailea eta erasotua eta soilik bi lurralde horiek ploteatu
		erakutsi_mapa(inperioak, lurralde_koloreak, ax, erasotzailea=erasotzailea.iloc[0].jabea, erasotua=erasotua.iloc[0].jabea)
		inperioak = datuak.dissolve(by='jabea', as_index=False)


print(f'{inperioak.iloc[0].jabea}k Euskal Herria konkistatu du, gora {inperioak.iloc[0].jabea}!')
