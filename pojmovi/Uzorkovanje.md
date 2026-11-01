---
tip: pojam
aliases: [sampling]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, poglavlje 17
---
# Uzorkovanje (sampling)

## Definicija
Uzorkovanje je postupak kojim se dobija konkretna vrednost slučajne promenljive, tako da je dobijena vrednost tačno ili približno raspodeljena prema raspodeli verovatnoće te promenljive.

## Jednostavan primer
Bacanje kocke je uzorkovanje iz njene raspodele: kod poštene kocke svaki broj pada u približno šestini bacanja. Isto se postiže programom koji generatorom slučajnih brojeva bira broj od 1 do 6, svaki sa verovatnoćom 1/6.

## Primer
Nalog „očevidac“ uz snimak šalje redakciji agencije Vidik i opis događaja generisan jezičkim modelom. Posle reči „Nesreća se dogodila u“ model dodeljuje verovatnoće sledećoj reči: „centru“ 0,40, „noći“ 0,25, „Kraljevu“ 0,10, ostalim rečima ukupno 0,25. Uzorkovanje bira „noći“ u četvrtini slučajeva, pa isti prompt, ponovljen, daje različite opise. Na isti način je i arhiva od 40 000 fotografija agencije uzorak iz [[Raspodela podataka|raspodele podataka]]; tamo uzorkuje sam proces nastanka fotografija, a ne model.

## Kontraprimer
**Kocka.** Prijavljivanje uvek šestice kao ishoda nameštene kocke, jer je najverovatnija, nije uzorkovanje iz njene raspodele: ostali brojevi se tada ne bi pojavili nikad, iako svaki ima verovatnoću 1/10.

**Agencija Vidik.** Izbor uvek najverovatnije reči, „centru“, posle reči „Nesreća se dogodila u“ nije uzorkovanje iz [[Raspodela modela|raspodele modela]]: reč „noći“ se tada ne bi pojavila nikad, iako joj model dodeljuje verovatnoću 0,25. Takav izbor je uzorkovanje iz izmenjene raspodele, koja svu verovatnoću daje jednoj reči.

## Napomene
- Približno uzorkovanje koriste, na primer, difuzioni modeli, čiji iterativni postupak [[Raspodela modela|raspodelu modela]] samo aproksimira.
- [[Strategija uzorkovanja]] menja raspodelu iz koje se uzorkuje, a ne sam postupak uzorkovanja. Pohlepni izbor najverovatnije vrednosti je granični slučaj: uzorkovanje iz raspodele koja svu verovatnoću dodeljuje jednoj vrednosti.
