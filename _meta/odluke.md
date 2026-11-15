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
- sadržaj (tekst, slika, audio, video)
- standardna devijacija

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
- [[Generisani sadržaj]] je definisan uže: ceo primerak dobijen uzorkovanjem iz generativnog modela. Primerak koji je samo delom dobijen iz generativnog modela ne obuhvata se ovim pojmom; videti otvoreno pitanje. Koristi se termin „generisani“, a ne „sintetički“, radi doslednosti sa terminima generativni model i uslovno generisanje; „sintetički sadržaj“ je alias.

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
- 2026-11-13: Dodat pojam Generisani sadržaj, u užem značenju (ceo primerak), i pretpostavljeni pojam sadržaj. Razlog za užu definiciju: šira, koja obuhvata i delimično generisan sadržaj (kao kod NIST AI 100-4), zahteva prag „značajne“ izmene koji je subjektivan, a detekcija delimično generisanog sadržaja ima i zadatak lokalizacije generisanog dela.
- 2026-11-13: Dodat pojam Detektor, uže od NIST AI 100-4: detektor je algoritam (čovek nije detektor, iako radi detekciju), a definicija je binarna (generisan ili ne); određivanje generisanog dela i generativnog modela su proširenja. Detektor ne linkuje Prag odluke, da lanac definicija ne bi bio cirkularan. Kontekst Novinska agencija Vidik dopunjen je detektorima generisanog sadržaja za tekst i fotografije.
- 2026-11-13: Dodat pojam Naučeni detektor, u užem značenju kao kod NIST AI 100-4 (nadgledano učenje na primercima označenim kao generisani ili negenerisani); jednoklasni detektori nisu obuhvaćeni. Koristi se termin „naučeni“, a „trenirani detektor“ je alias. Kontekst: detektor za tekst meri perpleksnost, a detektor fotografija je naučeni.
- 2026-11-13: Dodat pojam Prag odluke, sa jednim pragom, u skladu sa binarnom definicijom detektora; dva praga i ručna provera su proširenje. Kao izvor je naveden T. Fawcett (2006), odeljak 4, gde se prag uvodi kao vrednost kojom klasifikator sa skorom postaje binarni klasifikator; formulacija je proverena u tekstu rada.
- 2026-11-15: Dodat pojam Ključ žiga kao tajna vrednost, u skladu sa beleškom Vodeni žig; javni žig je u napomeni. Kontekst: jezički model naloga „očevidac“ ugrađuje žig, a ključ drži proizvođač.
- 2026-11-15: Dodati pojmovi Mesto ugradnje žiga, Nulta hipoteza, Z-skor, P-vrednost i Detekcija sa žigom, i pretpostavljeni pojam standardna devijacija. Nulta hipoteza se ne definiše preko p-vrednosti, da lanac ne bi bio cirkularan. U primerima zelena lista je četvrtina rečnika, kao u beleški Vodeni žig, a prag je z > 4. Kontekst: model slika iz teksta ugrađuje žig u početni šum.
- 2026-11-15: Izvori za Nultu hipotezu, Z-skor i P-vrednost provereni su u tekstu izvora. Za Nultu hipotezu Casella i Berger zamenjeni su priručnikom NIST/SEMATECH i radom Kirchenbauer i dr., jer formulaciju iz udžbenika nije bilo moguće proveriti.

## Otvorena pitanja
- Pohlepni izbor: beleška [[Uzorkovanje]] ga tumači kao granični slučaj uzorkovanja, a beleška [[Strategija izbora tokena]] kaže da nije uzorkovanje. Treba usvojiti jedno tumačenje.
- Da li jednostavan primer mora biti iz konteksta Kocka i kada kocka slabo pokazuje pojam?
- Formulacija izvora za [[Uslovno generisanje]] (Goodfellow i dr., Deep Learning, pogl. 20) nije proverena.
- Delimično generisan sadržaj (primerak koji je samo delom dobijen iz generativnog modela, npr. stvarna fotografija u koju je model ubacio predmet) nije definisan. Uža definicija [[Generisani sadržaj|generisanog sadržaja]] ga isključuje, pa takav primerak u bazi nema svoj pojam. Kandidat za prezentaciju o lokalizaciji generisanog dela ili o napadima na detektore.
- „Lažno pozitivan nalaz“ se koristi nelinkovan u beleškama [[Detekcija bez žiga]], [[Vodeni žig]], [[Prag odluke]] i [[Detekcija sa žigom]]; po planu se definiše u prezentaciji 6.
