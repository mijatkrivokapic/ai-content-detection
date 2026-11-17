---
tip: pojam
aliases: [trained detector, supervised detector, learned detector, trenirani detektor]
izvor: NIST AI 100-4, Reducing Risks Posed by Synthetic Content, 2024, odeljak 3.2 (supervised learning)
---
# Naučeni detektor (trained detector)

## Definicija
Naučeni detektor je [[Detektor|detektor]] čiju ocenu daje klasifikator treniran na primercima sadržaja označenim kao [[Generisani sadržaj|generisani]] ili negenerisani.

## Jednostavan primer
Klasifikator iz broja pojavljivanja svakog broja u zapisniku računa ocenu. Treniran je na 1000 zapisnika od 60 bacanja, označenih kao stvarna bacanja poštene kocke ili kao zapisnici dobijeni iz modela kocke sa θ = 1/2. Sam je „otkrio“ da je broj šestica najvažniji.

## Primer
Detektor fotografija agencije Vidik je naučeni detektor. Treniran je na arhivi od 40 000 primljenih fotografija, označenih kao negenerisane, i na 40 000 fotografija koje su modelom lica i modelom slika iz teksta generisane za tu svrhu.

## Kontraprimer
**Kocka.** Detektor iz beleške [[Detektor]], kome je prag od 20 šestica izabran napamet, nije naučen.

**Agencija Vidik.** Detektor za tekst agencije meri [[Perpleksnost|perpleksnost]] opisa iz ugla jezičkog modela. Jezički model je treniran, ali ne na primercima označenim kao generisani ili negenerisani, pa detektor nije naučen.

## Napomene
- Detektor kome je samo prag izabran na označenim primercima nije naučen, jer mu ocena nije izlaz treniranog klasifikatora.
- Detektor treniran samo na negenerisanim primercima, koji traži odstupanja od njih, nije obuhvaćen ovom definicijom.
- Naučeni detektor obično greši češće nad sadržajem generativnih modela koji nisu bili u trening skupu. Detektor agencije može slabije prepoznati fotografiju iz modela kojim nije generisan nijedan trenirajući primerak.
- Oznake mogu biti pogrešne: arhiva primljenih fotografija može sadržati i generisane fotografije koje niko nije prepoznao.
