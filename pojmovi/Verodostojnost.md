---
tip: pojam
aliases: [likelihood, likelihood function, funkcija verodostojnosti]
izvor: C. M. Bishop, Pattern Recognition and Machine Learning, Springer, 2006, odeljak 1.2.3
---
# Verodostojnost (likelihood)

## Definicija
Verodostojnost primerka je verovatnoća da se [[Uzorkovanje|uzorkovanjem]] iz [[Raspodela modela|raspodele modela]] dobije upravo taj primerak. Kada je sadržaj predstavljen neprekidnim vrednostima, kao pikseli slike, umesto verovatnoće koristi se gustina verovatnoće, sa istim tumačenjem: veća vrednost znači da bi model taj primerak verovatnije proizveo. Ako se primerak drži fiksnim, a menjaju se parametri modela, verodostojnost pokazuje koliko dobro koje vrednosti parametara objašnjavaju taj primerak; tako posmatrana naziva se funkcija verodostojnosti (likelihood function).

## Jednostavan primer
Pri bacanju je pala šestica. Pod modelom „poštena kocka“ verodostojnost tog ishoda je 1/6, a pod modelom „nameštena kocka“, koja šesticu daje u polovini bacanja, 1/2. Ako je parametar modela verovatnoća šestice, funkcija verodostojnosti za opaženu šesticu ima veću vrednost za parametar 1/2 nego za 1/6: nameštena kocka bolje objašnjava opažanje.

## Primer
Jezički model kojim je generisan opis događaja naloga „očevidac“ dodeljuje rečenici „Nesreća se dogodila u noći.“ verodostojnost jednaku proizvodu verovatnoća svake reči uz prethodne: 0,02 · 0,6 · 0,5 · 0,25 · 0,3 ≈ 0,00045. Rečenica iste dužine iz izveštaja dopisnika agencije Vidik, „Sudar se desio kod rampe.“, sastoji se od ređih reči i spojeva, pa joj isti model dodeljuje verodostojnost nekoliko redova veličine manju. Ista rečenica pod modelom sa drugim parametrima, na primer pre treniranja, imala bi drugačiju verodostojnost.

## Napomene
- Verodostojnost je verovatnoća primerka uz dati model, a ne verovatnoća da je primerak proizveo taj model. Tekst može imati visoku verodostojnost pod jezičkim modelom, a da ga je napisao čovek.
- Verodostojnost dužeg primerka je izuzetno mali broj, pa se u praksi koristi njen logaritam, log-verodostojnost (log-likelihood). Logaritam proizvoda verovatnoća je zbir logaritama, što olakšava računanje.
