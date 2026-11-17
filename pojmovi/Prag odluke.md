---
tip: pojam
aliases: [decision threshold, threshold, prag]
izvor: T. Fawcett, „An introduction to ROC analysis“, Pattern Recognition Letters 27 (2006), str. 861–874, odeljak 4
---
# Prag odluke (decision threshold)

## Definicija
Prag odluke je granična vrednost ocene [[Detektor|detektora]]: sa jedne strane praga detektor primerak proglašava generisanim, a sa druge negenerisanim.

## Jednostavan primer
Detektor zapisnika od 60 bacanja proglašava zapisnik generisanim kada ima više od 20 šestica. Stvaran zapisnik poštene kocke ima u proseku 10 šestica i pogrešno se označi u oko 0,05 % slučajeva, a zapisnik iz modela kocke sa θ = 1/2 promakne u oko 0,7 % slučajeva. Sa pragom od 12 šestica ne bi promakao skoro nijedan generisan zapisnik, ali bi otprilike svaki peti stvaran zapisnik bio pogrešno označen.

## Primer
Detektor fotografija agencije Vidik u početku ima prag 0,5. Mnoge stvarne noćne i mutne fotografije građana dobijaju ocenu iznad 0,5, pa redakcija podiže prag na 0,9. Fotografija poplave naloga „očevidac“, sa ocenom 0,93, i dalje se označava kao generisana, ali generisana fotografija sa ocenom 0,7 sada prolazi.

## Kontraprimer
**Kocka.** Očekivani broj šestica kod poštene kocke, 10, nije prag odluke: to je svojstvo raspodele, a ne granica koju bira onaj ko projektuje detektor.

**Agencija Vidik.** Ocena 0,93 fotografije poplave nije prag, nego ocena jednog primerka.

## Napomene
- Isti detektor sa različitim pragom pravi drugačije greške: viši prag znači manje lažnih optužbi negenerisanog sadržaja, a više propuštenog generisanog.
- Prag se obično bira tako da stopa lažno pozitivnih nalaza na negenerisanom sadržaju bude prihvatljiva. Kod provere [[Vodeni žig|vodenog žiga]] ta stopa se može izračunati unapred.
- Kod detektora čija niska ocena znači generisan sadržaj, kao kod detektora zasnovanog na [[Perpleksnost|perpleksnosti]], generisanim se proglašava ono što je ispod praga.
- Proširenje: dva praga i treći ishod između njih, ručna provera.
