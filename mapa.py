from random import shuffle

from helpers import jaso_datuak, jaso_kolore_ilunak, erakutsi_mapa, mugakidea_jaso, konkistatu
from constants import Modua
import matplotlib.pyplot as plt
datuak = jaso_datuak(Modua.HERRIKA)
koloreak = jaso_kolore_ilunak()
shuffle(koloreak)
lurralde_koloreak = dict()
# TODO Hau garbixau ein
for i, row in datuak.iterrows():
	lurralde_koloreak[row['izena']] = koloreak[i % len(koloreak)]

datuak['jabea'] = datuak['izena']
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
		if erasotua.iloc[0].jabea == lurraldea.izena:
			norena = ''
		else:
			norena = f' {erasotua.iloc[0].jabea}(r)ena zen'

		print(f'{erasotzailea.iloc[0].jabea}(e)k{norena} {lurraldea.izena} konkistatu du.')
		inperioak = datuak.dissolve(by='jabea', as_index=False)
		# TODO Hemen erakutsi beharko lirateke erasotzailea eta erasotua eta soilik bi lurralde horiek ploteatu
		erakutsi_mapa(inperioak, lurralde_koloreak, ax)


print(f'{inperioak.iloc[0].jabea}k Euskal Herria konkistatu du, gora {inperioak.iloc[0].jabea}!')
