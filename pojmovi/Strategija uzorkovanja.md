---
tip: pojam
aliases: [sampling strategy]
izvor: A. Holtzman i dr., „The Curious Case of Neural Text Degeneration“, ICLR 2020
---
# Strategija uzorkovanja (sampling strategy)

## Definicija
Strategija uzorkovanja je pravilo kojim se [[Raspodela modela|raspodela modela]] menja neposredno pre [[Uzorkovanje|uzorkovanja]], da bi se uticalo na to koji se primerci dobijaju, bez promene parametara modela. Obuhvata [[Temperatura|temperaturu]], [[Strategija izbora tokena|strategiju izbora tokena]] i tehnike koje pojačavaju uticaj uslova u [[Uslovno generisanje|uslovnom generisanju]].

## Jednostavan primer
Pre bacanja virtuelne kocke odlučimo da nikad ne prijavljujemo jedinicu, a da njenu verovatnoću ravnomerno podelimo ostalim brojevima. Model kocke se nije promenio, ali se uzorkuje iz izmenjene raspodele.

## Primer
Posle reči „Nesreća se dogodila u“ jezički model naloga „očevidac“ daje verovatnoće „centru“ 0,40, „noći“ 0,25, „Kraljevu“ 0,10 i ostalim rečima ukupno 0,25. Ako se pre uzorkovanja primeni niska temperatura, a zatim izbor samo među tri najverovatnije reči, „centru“ će se birati češće nego u četiri od deset slučajeva, a retke reči nikad. Opis događaja tada postaje predvidljiviji, što menja i ono što detektor vidi.

## Kontraprimer
**Agencija Vidik.** Dodatno treniranje jezičkog modela na izveštajima dopisnika nije strategija uzorkovanja: menja parametre, pa trajno menja raspodelu modela, a ne samo raspodelu iz koje se bira pri jednom generisanju.

## Napomene
- Strategija uzorkovanja je širi pojam od [[Strategija izbora tokena|strategije izbora tokena]], koja obuhvata samo pravilo konačnog izbora tokena (pohlepni izbor, top-k, top-p). Razgraničenje je upisano u `_meta/odluke.md`.
- Uzorkovanje iz izmenjene raspodele i dalje je uzorkovanje. Da li je pohlepni izbor granični slučaj uzorkovanja, otvoreno je pitanje u `_meta/odluke.md`.
