---
tip: pojam
aliases: [generative model]
izvor: C. M. Bishop, Pattern Recognition and Machine Learning, Springer, 2006, odeljak 1.5.4
---
# Generativni model (generative model)

## Definicija
Generativni model je model mašinskog učenja koji iz primeraka trening skupa uči raspodelu verovatnoće nad primercima sadržaja, sa ciljem da ona aproksimira [[Raspodela podataka|raspodelu podataka]], tako da se [[Uzorkovanje|uzorkovanjem]] iz naučene raspodele dobijaju novi primerci.

## Jednostavan primer
Nepoznata kocka bačena je 600 puta i iz zapisanih ishoda procenjena je verovatnoća svakog broja. Procenjene verovatnoće čine generativni model: iz njih se može „bacati“ virtuelna kocka i dobijati novi ishodi.

## Primer
Generativni model slika treniran je na oko 70 000 fotografija ljudskih lica. Svako uzorkovanje daje fotografiju lica osobe koja ne postoji. Nalog „očevidac“, koji preko prijemnog portala agencije Vidik šalje redakciji snimak navodnog incidenta, koristi takvo lice kao profilnu fotografiju.

## Kontraprimer
**Kocka.** Model koji za kocku samo ocenjuje da li je nameštena nije generativan, jer se iz njega ne dobijaju ishodi.

**Agencija Vidik.** Filter neželjene pošte u redakciji nije generativni model: on ocenjuje da li je pristigla poruka neželjena, ali ne uči raspodelu poruka i iz njega se ne može uzorkovati nova poruka.

## Napomene
Naučena raspodela ne mora da se poklapa sa raspodelom podataka. Jezički modeli dorađeni na osnovu ljudskih ocena namerno su pomereni ka poželjnim izlazima, a i dalje su generativni modeli.
