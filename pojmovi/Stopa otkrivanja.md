---
tip: pojam
aliases: [true positive rate, TPR, detection rate, stopa tačno pozitivnih nalaza, osetljivost, recall]
izvor: T. Fawcett, „An introduction to ROC analysis", Pattern Recognition Letters 27(8), 2006, str. 861–874
---
# Stopa otkrivanja (true positive rate, TPR)

## Definicija
Stopa otkrivanja je udeo [[Generisani sadržaj|generisanih]] primeraka koje [[Detektor|detektor]] označi kao generisane, za dati [[Prag odluke|prag odluke]]. Jednaka je jedan minus udeo [[Lažno negativan nalaz|lažno negativnih nalaza]] među generisanim primercima.

TPR = TP / (TP + FN), gde je TP broj generisanih primeraka tačno označenih kao generisani, a FN broj lažno negativnih nalaza.

## Jednostavan primer
Ako se pravilo „kocka je nameštena ako u 10 bacanja padnu bar 4 šestice“ primeni mnogo puta na plavu, nameštenu kocku, ona će biti proglašena nameštenom u oko 83% provera. Stopa otkrivanja tog pravila za plavu kocku je oko 83%.

## Primer
Redakcija agencije Vidik napravi 500 fotografija modelom slika iz teksta, istim kojim je napravljena fotografija poplave naloga „očevidac“, i propusti ih kroz detektor. Detektor njih 450 označi kao generisane, pa je stopa otkrivanja za taj model 90%. Brojevi su ilustrativni.

## Kontraprimer
**Agencija Vidik.** Tačnost (accuracy), udeo svih tačnih odluka, nije stopa otkrivanja. Ako je samo 1% primljenih fotografija generisano, detektor koji svaku fotografiju proglasi ljudskom ima tačnost 99%, a stopu otkrivanja 0%.

## Napomene
- Stopa otkrivanja zavisi od generatora i od izmena sadržaja: isti detektor ima različite stope otkrivanja za različite modele.
- Stopa otkrivanja sama po sebi ništa ne govori o kvalitetu detektora: detektor koji sve proglasi generisanim ima stopu otkrivanja 100%, ali i [[Stopa lažno pozitivnih nalaza|stopu lažno pozitivnih nalaza]] 100%. Zato se navodi uz stopu lažno pozitivnih nalaza, kao [[Stopa otkrivanja pri fiksnoj stopi lažno pozitivnih nalaza|stopa otkrivanja pri fiksnoj stopi lažno pozitivnih nalaza]].
