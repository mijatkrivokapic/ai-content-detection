---
tip: pojam
aliases: [false positive rate, FPR, stopa lažnih alarma, false alarm rate]
izvor: T. Fawcett, „An introduction to ROC analysis", Pattern Recognition Letters 27(8), 2006, str. 861–874
---
# Stopa lažno pozitivnih nalaza (false positive rate, FPR)

## Definicija
Stopa lažno pozitivnih nalaza je udeo [[Lažno pozitivan nalaz|lažno pozitivnih nalaza]] među svim primercima koji nisu [[Generisani sadržaj|generisani]], za dati [[Detektor|detektor]] i dati [[Prag odluke|prag odluke]]. Odgovara verovatnoći da detektor ljudski primerak označi kao generisan.

FPR = FP / (FP + TN), gde je FP broj lažno pozitivnih nalaza, a TN broj ljudskih primeraka tačno označenih kao ljudski.

## Jednostavan primer
Ako se pravilo „kocka je nameštena ako u 10 bacanja padnu bar 4 šestice“ primeni mnogo puta na crvenu, poštenu kocku, ona će biti proglašena nameštenom u oko 7% provera. Stopa lažno pozitivnih nalaza tog pravila je oko 7%.

## Primer
Redakcija agencije Vidik propusti kroz detektor 1000 fotografija iz arhive primljenih fotografija za koje je proverila da su snimljene telefonom. Detektor njih 30 označi kao generisane, pa je stopa lažno pozitivnih nalaza 30 / 1000 = 3%. To znači da bi otprilike svaki trideset treći autentičan snimak građanina izazvao sumnju. Brojevi su ilustrativni.

## Kontraprimer
**Agencija Vidik.** Ako detektor od 50 fotografija koje je označio kao generisane pogreši za njih 30, udeo 30 / 50 = 60% nije stopa lažno pozitivnih nalaza. Taj udeo se računa među označenim primercima, a ne među svim ljudskim primercima, i zavisi od toga koliko generisanih fotografija agencija uopšte prima.

## Napomene
- Kod [[Detekcija bez žiga|detekcije bez žiga]] stopa lažno pozitivnih nalaza nije unapred poznata, nego se meri na ljudskom sadržaju. Zavisi od toga na kom ljudskom sadržaju je merena: na noćnim i mutnim snimcima može biti veća nego na dnevnim fotografijama.
- Kod [[Detekcija sa žigom|detekcije sa žigom]] prag na [[P-vrednost|p-vrednosti]] direktno zadaje stopu lažno pozitivnih nalaza: to je verovatnoća da se [[Nulta hipoteza|nulta hipoteza]] odbaci iako je tačna.
