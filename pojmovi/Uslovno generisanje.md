---
tip: pojam
aliases: [conditional generation]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, poglavlje 20
---
# Uslovno generisanje (conditional generation)

## Definicija
Uslovno generisanje je [[Uzorkovanje|uzorkovanje]] iz [[Raspodela modela|raspodele modela]] uslovljene zadatim uslovom, pri čemu je uslov ulazni podatak koji se modelu zadaje pre uzorkovanja.

## Jednostavan primer
U džepu su crvena poštena kocka i plava nameštena kocka. Uslov „baci plavu“ određuje iz koje se raspodele dobija ishod: uz taj uslov šestica pada u polovini bacanja, a uz uslov „baci crvenu“ u šestini.

## Primer
Nalog „očevidac“ uz opis događaja šalje redakciji agencije Vidik i fotografiju navodne poplave. Fotografiju je generisao model koji pravi slike iz teksta, kome je zadat prompt „poplava u centru Kraljeva noću, snimak telefonom“. Prompt je uslov: svako uzorkovanje daje drugačiju fotografiju, ali sve prikazuju noćnu poplavu u gradu, snimljenu kao telefonom.

## Kontraprimer
**Kocka.** Bacanje jedne kocke, bez izbora između crvene i plave, nije uslovno generisanje.

**Agencija Vidik.** Profilna fotografija naloga „očevidac“ nastala je bez uslova, iz modela lica koji daje proizvoljno lice.

## Sekundarni primeri
Sinteza govora. Uslov može biti i primerak sadržaja: model kome se zada desetak sekundi snimka nečijeg glasa i tekst generiše govor tog teksta glasom sa snimka.

## Napomene
- [[Generativni model]] koji omogućava uslovno generisanje zadaje po jednu raspodelu modela za svaku vrednost uslova; trenira se na parovima primeraka i odgovarajućih uslova.
- Tehnike koje pojačavaju uticaj uslova na ishod menjaju raspodelu iz koje se uzorkuje i spadaju u [[Strategija uzorkovanja|strategiju uzorkovanja]].
