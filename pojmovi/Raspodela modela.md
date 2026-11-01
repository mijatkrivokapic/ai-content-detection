---
tip: pojam
aliases: [model distribution]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, odeljak 5.5
---
# Raspodela modela (model distribution)

## Definicija
Raspodela modela je raspodela verovatnoće nad primercima sadržaja koju [[Generativni model|generativni model]] zadaje za date vrednosti svojih parametara.

## Jednostavan primer
Model kocke ima jedan parametar θ, verovatnoću šestice, a ostalih pet brojeva podjednako deli preostalu verovatnoću. Za θ = 1/6 raspodela modela je raspodela poštene kocke, a za θ = 1/2 raspodela kocke koja šesticu daje u polovini bacanja.

## Primer
Pre treniranja, model lica sa nasumičnim parametrima zadaje raspodelu modela iz koje se uzorkovanjem dobija šum. Tokom treniranja na skupu FFHQ parametri se menjaju, a sa njima i raspodela modela, koja se približava [[Raspodela podataka|raspodeli podataka]] portreta sa Flickra. Profilna fotografija naloga „očevidac“ na prijemnom portalu agencije Vidik uzorkovana je iz raspodele modela posle treniranja, ne iz raspodele portreta. Zato može imati tragove koje pravi portreti gotovo nikad nemaju, na primer različite minđuše na levom i desnom uhu ili izobličenu pozadinu iza glave.

## Kontraprimer
**Kocka.** Raspodela kocke koju držimo u ruci nije raspodela modela, čak i kada model ima θ = 1/6 i poklapa se sa njom: nju određuju oblik i masa kocke, a ne parametri modela.

**Agencija Vidik.** Raspodela portreta sa Flickra iz koje potiče skup FFHQ nije raspodela modela lica, već raspodela podataka.