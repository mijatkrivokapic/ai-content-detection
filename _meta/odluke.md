---
tip: odluke
---
# Odluke

## Pretpostavljeni pojmovi
Pojmovi koje publika zna bez definisanja. Ne otvaraju se ponovo osim na zahtev studenta.

- model mašinskog učenja
- treniranje
- trening skup
- raspodela verovatnoće
- slučajna promenljiva
- parametri modela
- očekivanje (matematičko očekivanje)
- uslovna raspodela

## Konvencije
- Termin **primerak** (sample, instance) označava jednu jedinicu sadržaja (tekst, slika, audio ili video zapis). Termin „primer“ se ne koristi u tom značenju, jer je rezervisan za odeljak Primer u beleškama.

- Strategija uzorkovanja (temperatura, top-k) ne ulazi u [[Raspodela modela|raspodelu modela]] i obrađuje se kao poseban pojam [[Strategija uzorkovanja]].
- [[Uzorkovanje]] je definisano u užem, statističkom smislu, tako da obuhvata i uzorkovanje iz raspodele podataka, ne samo iz modela.
- „Jezički model“ se koristi u primerima nelinkovan, kao budući pojam.
- Za engleski „prompt“ koristi se neprevedeni termin **prompt**, sa promenom po padežima kao imenica muškog roda (prompt, prompta, promptom). Alternative „upit“, „uputstvo“ i „instrukcija“ se ne koriste.
- Veza [[Metoda maksimalne verodostojnosti|metode maksimalne verodostojnosti]] sa KL divergencijom obrađuje se u beleški [[KL divergencija]], ne u beleški metode.

- Podela na [[Eksplicitni generativni model|eksplicitne]] i implicitne generativne modele pravi se po izračunljivosti verodostojnosti, a ne po tome da li model formalno definiše gustinu (kao kod Goodfellowa). Posledica: modeli čija se verodostojnost ne može u praksi izračunati, npr. Bolcmanove mašine, svrstavaju se u implicitne.

- Redosled čitanja i izlaganja pojmova prati zavisnosti definicija i tok priče: (1) odakle dolaze primerci: [[Uzorkovanje]], [[Raspodela podataka]]; (2) model i generisanje: [[Generativni model]], [[Raspodela modela]], [[Uslovno generisanje]]; (3) učenje: [[Verodostojnost]], [[Metoda maksimalne verodostojnosti]], [[KL divergencija]]; (4) vrste modela: [[Eksplicitni generativni model]], [[Implicitni generativni model]]. Primer iz agencije kod uzorkovanja koristi jezički model pre definicije generativnog modela; to se prihvata kao najava.

## Promene konvencija
- 2026-10-31: Strategija uzorkovanja se više ne obrađuje u okviru pojma Uzorkovanje, već kao poseban pojam. Razlog: šira definicija uzorkovanja bila bi cirkularna (preko Generativnog modela) i ne bi pokrila uzorkovanje trening skupa iz raspodele podataka.
- 2026-11-01: Svaki pojam ima dva primera, ovim redom: odeljak „Jednostavan primer“ iz sekundarnog konteksta [[Kocka]], za intuiciju, pa odeljak „Primer“ iz primarnog konteksta [[Novinska agencija Vidik]], za primenu na problem. Ranije je primer iz primarnog konteksta bio jedini obavezan, a kocka se javljala samo kao sekundarni primer. Razlog: jednostavan primer olakšava razumevanje pojma pre primene.
- 2026-11-01: Uveden je opcioni odeljak „Kontraprimer“, posle odeljka „Primer“, za pojmove kod kojih kontraprimer pomaže razumevanju. Postojeće rečenice koje su u primerima služile kao kontraprimeri premeštene su u taj odeljak. KL divergencija nema kontraprimer, jer asimetrija u primeru već pokazuje šta pojam nije. Odeljak se deli na pasuse označene sa **Kocka.** i **Agencija Vidik.**, prema primeru na koji se kontraprimer odnosi.
- 2026-11-01: Tema, problem i primarni kontekst iz konfiguracije potvrđeni su; više nisu otvoreno pitanje.
- 2026-11-01: Za engleski „training set“ dosledno se koristi termin **trening skup** (trening skupa, trening skupu), umesto ranijeg „skup za treniranje“. Pridev „trenirajući“ (trenirajući primerci) ostaje u upotrebi.

## Otvorena pitanja
