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
- neuronska mreža
- transformer
- normalna (Gausova) raspodela
- Šenonova entropija
- klasifikator
- funkcija gubitka
- Furijeova transformacija
- piksel, kanal boje

## Konvencije
- Termin **primerak** (sample, instance) označava jednu jedinicu sadržaja (tekst, slika, audio ili video zapis). Termin „primer“ se ne koristi u tom značenju, jer je rezervisan za odeljak Primer u beleškama.

- Strategija uzorkovanja (temperatura, top-k) ne ulazi u [[Raspodela modela|raspodelu modela]] i obrađuje se kao poseban pojam [[Strategija uzorkovanja]].
- [[Uzorkovanje]] je definisano u užem, statističkom smislu, tako da obuhvata i uzorkovanje iz raspodele podataka, ne samo iz modela.
- „Jezički model“ se koristi u primerima nelinkovan, kao budući pojam.
- Za engleski „prompt“ koristi se neprevedeni termin **prompt**, sa promenom po padežima kao imenica muškog roda (prompt, prompta, promptom). Alternative „upit“, „uputstvo“ i „instrukcija“ se ne koriste.
- Veza [[Metoda maksimalne verodostojnosti|metode maksimalne verodostojnosti]] sa KL divergencijom obrađuje se u beleški [[KL divergencija]], ne u beleški metode.

- Podela na [[Eksplicitni generativni model|eksplicitne]] i implicitne generativne modele pravi se po izračunljivosti verodostojnosti, a ne po tome da li model formalno definiše gustinu (kao kod Goodfellowa). Posledica: modeli čija se verodostojnost ne može u praksi izračunati, npr. Bolcmanove mašine, svrstavaju se u implicitne.

- Redosled čitanja i izlaganja pojmova prati zavisnosti definicija i tok priče: (1) odakle dolaze primerci: [[Uzorkovanje]], [[Raspodela podataka]]; (2) model i generisanje: [[Generativni model]], [[Raspodela modela]], [[Uslovno generisanje]]; (3) učenje: [[Verodostojnost]], [[Metoda maksimalne verodostojnosti]], [[KL divergencija]]; (4) vrste modela: [[Eksplicitni generativni model]], [[Implicitni generativni model]]. Primer iz agencije kod uzorkovanja koristi jezički model pre definicije generativnog modela; to se prihvata kao najava.

- [[Strategija uzorkovanja]] i [[Strategija izbora tokena]] su dva pojma. Strategija uzorkovanja je širi pojam: svako pravilo kojim se raspodela modela menja neposredno pre uzorkovanja, uključujući [[Temperatura|temperaturu]]. Strategija izbora tokena je uži pojam: samo pravilo konačnog izbora tokena (pohlepni izbor, top-k, top-p). Uža beleška se linkuje na širu.
- [[Poligon]] je drugi sekundarni kontekst, za primere sa imenovanim modelima i detektorima (Tekst-G, Lica-G, P-Detektor i dr.). Glavni primer svakog pojma ostaje u kontekstu [[Novinska agencija Vidik]], a jednostavan u kontekstu [[Kocka]].
- Svaki pojam ima svoju belešku u `pojmovi/`, a naziv fajla je srpski termin u nominativu jednine. Više pojmova u jednom fajlu se ne drži.
- Materijali prezentacija čuvaju se u `runde/runda-N/prezentacija-K/`, urednički pregled u `runde/runda-N/urednici.md`, a pregled runde u `runde/runda-N/README.md`. Raspored je opisan u `README.md`.

## Promene konvencija
- 2026-10-31: Strategija uzorkovanja se više ne obrađuje u okviru pojma Uzorkovanje, već kao poseban pojam. Razlog: šira definicija uzorkovanja bila bi cirkularna (preko Generativnog modela) i ne bi pokrila uzorkovanje trening skupa iz raspodele podataka.
- 2026-11-01: Svaki pojam ima dva primera, ovim redom: odeljak „Jednostavan primer“ iz sekundarnog konteksta [[Kocka]], za intuiciju, pa odeljak „Primer“ iz primarnog konteksta [[Novinska agencija Vidik]], za primenu na problem. Ranije je primer iz primarnog konteksta bio jedini obavezan, a kocka se javljala samo kao sekundarni primer. Razlog: jednostavan primer olakšava razumevanje pojma pre primene.
- 2026-11-01: Uveden je opcioni odeljak „Kontraprimer“, posle odeljka „Primer“, za pojmove kod kojih kontraprimer pomaže razumevanju. Postojeće rečenice koje su u primerima služile kao kontraprimeri premeštene su u taj odeljak. KL divergencija nema kontraprimer, jer asimetrija u primeru već pokazuje šta pojam nije. Odeljak se deli na pasuse označene sa **Kocka.** i **Agencija Vidik.**, prema primeru na koji se kontraprimer odnosi.
- 2026-11-01: Tema, problem i primarni kontekst iz konfiguracije potvrđeni su; više nisu otvoreno pitanje.
- 2026-11-01: Za engleski „training set“ dosledno se koristi termin **trening skup** (trening skupa, trening skupu), umesto ranijeg „skup za treniranje“. Pridev „trenirajući“ (trenirajući primerci) ostaje u upotrebi.
- 2026-11-03: Strategija uzorkovanja i strategija izbora tokena vode se kao dva pojma, širi i uži. U belešci Strategija izbora tokena uklonjen je alias „strategija uzorkovanja“, da se pretraga ne bi mešala, i dodata je napomena sa linkom na širi pojam; ostali tekst beleške nije menjan.
- 2026-11-03: Uveden sekundarni kontekst Poligon, preuzet iz Pojmovnika, jer ga koriste beleške iz runde 1 (prezentacija 3).
- 2026-11-03: Beleške iz prezentacije 3 razdvojene su u pojedinačne fajlove, bez izmene teksta. Dodate su beleške za pojmove iz prezentacije 2 i beleška Strategija uzorkovanja.
- 2026-11-03: Kontekst Novinska agencija Vidik dopunjen je modelima kojima se služi nalog „očevidac“ (jezički model, model lica, model slika iz teksta), jer ih beleške iz runde 1 već koriste. Kontekst Kocka dopunjen je zapisnikom bacanja.
- 2026-11-03: Repozitorijum je organizovan po rundama (folder `runde/`). Prezentacije runde 1 premeštene su iz korena u `runde/runda-1/`, bez izmene sadržaja.
- 2026-11-03: Dodati pretpostavljeni pojmovi: neuronska mreža, transformer, normalna (Gausova) raspodela, Šenonova entropija, klasifikator, funkcija gubitka, Furijeova transformacija, piksel, kanal boje. Softmax ostaje definisan, jer za njega postoji beleška.

## Otvorena pitanja
- Pohlepni izbor: beleška [[Uzorkovanje]] ga tumači kao granični slučaj uzorkovanja, a beleška [[Strategija izbora tokena]] kaže da nije uzorkovanje. Treba usvojiti jedno tumačenje.
- Da li jednostavan primer mora biti iz konteksta Kocka i kada kocka slabo pokazuje pojam?
- Formulacija izvora za [[Uslovno generisanje]] (Goodfellow i dr., Deep Learning, pogl. 20) nije proverena.
