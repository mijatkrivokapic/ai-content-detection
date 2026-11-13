---
tip: pojam
aliases: [false positive, FP, lažna optužba, lažni alarm]
izvor: T. Fawcett, „An introduction to ROC analysis", Pattern Recognition Letters 27(8), 2006, str. 861–874
---
# Lažno pozitivan nalaz (false positive)

## Definicija
Lažno pozitivan nalaz je odluka [[Detektor|detektora]] da je primerak [[Generisani sadržaj|generisan]], doneta za primerak koji nije generisan. Nastaje kada ocena ljudskog primerka pređe [[Prag odluke|prag odluke]].

## Jednostavan primer
Pravilo provere kaže da je kocka nameštena ako u 10 bacanja padnu bar 4 šestice. Crvena kocka je poštena, ali u 10 bacanja slučajno padne 5 šestica, pa je pravilo proglasi nameštenom. To je lažno pozitivan nalaz.

## Primer
Dopisnik agencije Vidik pošalje noćnu, mutnu fotografiju saobraćajne nesreće snimljenu telefonom. Detektor koji agencija koristi dodeli joj ocenu iznad praga i označi je kao generisanu. Redakcija odbije autentičan materijal i posumnja u dopisnika koji ga je poslao: lažno pozitivan nalaz je lažna optužba.

## Kontraprimer
**Kocka.** Plava, nameštena kocka koju pravilo proglasi nameštenom nije lažno pozitivan nalaz, nego tačan nalaz.

**Agencija Vidik.** Fotografija poplave u centru Kraljeva koju je poslao nalog „očevidac“, a detektor je označi kao generisanu, nije lažno pozitivan nalaz: fotografija jeste generisana.

## Napomene
- „Pozitivan“ znači „označen kao generisan“, a ne „dobar“. Pozitivna klasa je generisani sadržaj.
- Pomeranje praga naviše smanjuje broj lažno pozitivnih nalaza, ali povećava broj [[Lažno negativan nalaz|lažno negativnih nalaza]].
- U agenciji je lažno pozitivan nalaz po pravilu skuplja greška od lažno negativnog, jer pogađa konkretnu osobu i odnos agencije sa izvorima.
