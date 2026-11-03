---
tip: pojam
aliases: [embedding, embedding vektor]
izvor: T. Mikolov i dr., „Efficient Estimation of Word Representations in Vector Space“, arXiv:1301.3781, 2013
---
# Ugrađivanje (embedding)

## Definicija
Ugrađivanje je vektor realnih brojeva koji model dodeljuje [[Token|tokenu]] ili drugom diskretnom elementu i uči ga tokom treniranja, tako da elementi sa sličnom ulogom u podacima dobijaju bliske vektore.

## Jednostavan primer
Model koji uči na bacanjima nameštene kocke svakom ishodu dodeljuje vektor. Brojevi od 1 do 5 se u podacima ponašaju isto, svaki pada u desetini bacanja, pa dobijaju bliske vektore. Šestica pada mnogo češće i dobija vektor udaljen od njih.

## Primer
Jezički model naloga „očevidac“ pre obrade opisa događaja svaki token zamenjuje njegovim ugrađivanjem. Tokeni „noći“ i „večeri“ javljaju se u sličnim rečenicama o nesrećama, pa imaju bliske vektore, dok je vektor tokena „poplava“ od njih udaljeniji.

## Kontraprimer
**Kocka.** Redni broj ishoda u rečniku nije ugrađivanje: on se ne uči iz podataka i bliski brojevi ne znače sličnu ulogu.

## Napomene
- U literaturi se ugrađivanjem naziva i vektor koji predstavlja celu rečenicu ili sliku. Ovde termin ima uže značenje iz definicije.
- Poznata ilustracija je da je razlika vektora „muškarac“ i „žena“ približno jednaka razlici vektora „kralj“ i „kraljica“; ona važi približno i ne za sve parove reči.
