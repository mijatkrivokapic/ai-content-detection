---
tip: pojam
aliases: [decoder]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, poglavlje 14
---
# Dekoder (decoder)

## Definicija
Dekoder je deo modela koji tačku [[Latentni prostor|latentnog prostora]] preslikava u sadržaj u [[Reprezentacija medija|reprezentaciji medija]].

## Jednostavan primer
Iz jednog broja, udela šestica, „bacanjem“ virtuelne kocke ponovo se pravi zapisnik od 600 ishoda. Postupak radi kao dekoder: iz kratkog opisa gradi pun zapis.

## Primer
Model lica kojim je generisana profilna fotografija naloga „očevidac“ ceo radi kao dekoder: vektor od 512 brojeva preslikava u fotografiju lica. Na isti način model koji je napravio fotografiju poplave na kraju generisanja dekoderom vraća tačku latentnog prostora u mrežu piksela.

## Kontraprimer
**Agencija Vidik.** Program koji otvara JPEG fotografiju iz arhive i prikazuje je na ekranu nije dekoder u ovom smislu, iako se u računarstvu i on tako zove: njegov ulaz nije tačka latentnog prostora.

## Napomene
- Kod jezičkih modela termin „dekoder“ označava deo transformer arhitekture i nema isto značenje kao ovde. Zato se engleski „decoding strategy“ ne prevodi kao „strategija dekodiranja“ (videti [[Strategija izbora tokena]]).
- Kombinacija [[Enkoder|enkodera]] i dekodera omogućava [[Rekonstrukcija|rekonstrukciju]].
- Dekoder gradi izlaz postepeno, kroz niz slojeva: od grube strukture do oblika i teksture. Pošto je pri sažimanju deo detalja odbačen, dekoder ih dopunjava na osnovu onoga što je naučio tokom treniranja, pa ne vraća kopiju originala, nego verodostojnu sliku iste suštine.
