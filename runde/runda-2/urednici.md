---
tip: urednicki-pregled
runda: 2
urednici: (dopuniti)
---
# Urednički pregled, runda 2

Runda 2 se oslanja na rundu 1 i prelazi sa generisanja na detekciju u tri dela koja se nadovezuju: arhitekture generativnih modela i tragovi koje ostavljaju (prezentacija 1), detektor, žig i statistička provera (prezentacija 2), greške, robusnost i napadi na detekciju (prezentacija 3).

Pregled obuhvata PR-ove prezentacija 1, 2 i 3. Beleške su spojene na granu `urednici-runda-2`.

## Veze između prezentacija

| Pojam | Pojmovi koji se na njega oslanjaju |
|---|---|
| [[Trag generatora]] (1) | [[Detekcija bez žiga]] (1. runda), [[Neviđeni generator]], [[Napad uklanjanjem]] (3) |
| [[Difuzioni model]], [[Generativna suparnička mreža]] (1) | [[Neviđeni generator]] (3): detektor treniran na GAN-ovima zakazuje na difuzionim modelima |
| [[Detektor]] (2) | [[Prag odluke]], [[Naučeni detektor]] (2); [[Lažno pozitivan nalaz]], [[Lažno negativan nalaz]], [[Stopa otkrivanja]], [[Robusnost detekcije]], [[Neviđeni generator]] (3) |
| [[Prag odluke]] (2) | [[Lažno pozitivan nalaz]], [[Lažno negativan nalaz]], [[Stopa lažno pozitivnih nalaza]], [[Stopa otkrivanja pri fiksnoj stopi lažno pozitivnih nalaza]] (3) |
| [[Vodeni žig]] (1. runda), [[Ključ žiga]] (2) | [[Falsifikovanje žiga]], [[Napad uklanjanjem]], [[Model pretnje]] (3) |
| [[Detekcija sa žigom]], [[P-vrednost]] (2) | [[Stopa lažno pozitivnih nalaza]], [[Falsifikovanje žiga]] (3): p-vrednost zadaje stopu lažno pozitivnih nalaza, a falsifikovanje je napad na tu garanciju |

Iz runde 1 koristi se: [[Latentni prostor]], [[Dekoder]], [[Enkoder]] i [[Gausov šum]] u [[Difuzioni model|difuzionom modelu]] i [[Varijacioni autoenkoder|varijacionom autoenkoderu]]; [[Reprezentacija medija]] u [[Spektrogram|spektrogramu]] i [[Frekvencijski domen|frekvencijskom domenu]]; [[Eksplicitni generativni model]] u definiciji difuzionih modela, modela toka i varijacionih autoenkodera.

## Usvojeno

1. Svaka beleška je u skladu sa šablonom (definicija, jednostavan primer, primer, napomene) i ima izvor.
2. [[Generisani sadržaj]] je definisan uže, kao ceo primerak dobijen uzorkovanjem; [[Detektor]] je algoritam sa binarnom odlukom.
3. Pozitivna klasa je generisani sadržaj: „pozitivan nalaz“ znači „označen kao generisan“.
4. Naziv fajla [[Neviđeni generator]] ispravljen je da prati naslov beleške.
5. Pojam [[Lažno pozitivan nalaz]], koji je prezentacija 2 koristila nelinkovan, sada je definisan; beleške [[Detekcija bez žiga]], [[Vodeni žig]], [[Prag odluke]] i [[Detekcija sa žigom]] ga linkuju, odnosno linkuju [[Stopa lažno pozitivnih nalaza]].
6. Kontekst [[Kocka]] dopunjen je elementima Program sa žigom, Zelena kocka, Pravilo provere i Varalica; kontekst [[Novinska agencija Vidik]] dopunjen je detektorima generisanog sadržaja i žigom u modelima naloga „očevidac“. Konflikt u kontekstu Kocka (dva PR-a su dodala elemente na isto mesto) rešen je zadržavanjem oba.
7. Unosi u `_meta/odluke.md` ujednačeni su po formatu i redosledu, a za prezentaciju 3 dodati su unosi koji su nedostajali.

## Izmene posle runde

- Spojeni su PR-ovi prezentacija 1, 2 i 3 (grana `urednici-runda-2`).
- [[Neviđeni generator]] preimenovan (bilo „Nevidjeni generator“).
- Dodati linkovi na [[Lažno pozitivan nalaz]] i [[Stopa lažno pozitivnih nalaza]] u 4 beleške prezentacije 2.
- Dodat `README.md` runde 2 i ovaj pregled.

## Primedbe za autore (ne menjano)

- Prezentacija 1 ne koristi primarni kontekst Vidik; u odluci piše da je „Primer“ bez konteksta, sa neimenovanim modelima, ali beleške koriste Slika-G, Lica-G i Glas-G iz [[Poligon|Poligona]].
- [[Falsifikovanje žiga]]: jednostavan primer je sa novčanicom, a konvencija traži primer iz konteksta Kocka.
- [[Trag generatora]]: izvori nisu proveravani.

## Otvorena pitanja

Vode se u `_meta/odluke.md`.
