---
tip: pojam
aliases: [false negative, FN, propušten generisani sadržaj]
izvor: T. Fawcett, „An introduction to ROC analysis", Pattern Recognition Letters 27(8), 2006, str. 861–874
---
# Lažno negativan nalaz (false negative)

## Definicija
Lažno negativan nalaz je odluka [[Detektor|detektora]] da primerak nije [[Generisani sadržaj|generisan]], doneta za primerak koji jeste generisan. Nastaje kada ocena generisanog primerka ostane ispod [[Prag odluke|praga odluke]].

## Jednostavan primer
Pravilo provere kaže da je kocka nameštena ako u 10 bacanja padnu bar 4 šestice. Plava kocka je nameštena, ali u 10 bacanja padnu samo 3 šestice, pa je pravilo proglasi poštenom. To je lažno negativan nalaz.

## Primer
Opis događaja koji je nalog „očevidac“ poslao uz snimak incidenta napisao je jezički model. Detektor koji agencija koristi dodeli mu ocenu ispod praga, pa tekst prođe kao ljudski i redakcija ga objavi kao svedočenje očevica.

## Kontraprimer
**Kocka.** Crvena, poštena kocka koju pravilo proglasi poštenom nije lažno negativan nalaz, nego tačan nalaz.

**Agencija Vidik.** Izveštaj dopisnika sa terena koji detektor označi kao ljudski nije lažno negativan nalaz: izveštaj jeste ljudski.

## Napomene
- Lažno negativan nalaz je simetričan [[Lažno pozitivan nalaz|lažno pozitivnom nalazu]]: oba su pogrešne odluke istog detektora, a prag određuje odnos između njih.
- Odsustvo [[Vodeni žig|vodenog žiga]] ne znači da primerak nije generisan, pa provera žiga daje lažno negativne nalaze za sadržaj generatora koji žig ne ugrađuju.
