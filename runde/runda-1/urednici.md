---
tip: urednicki-pregled
runda: 1
urednice: Ivana Lazović, Sara Ponjević
---
# Urednički pregled, runda 1

Runda 1 postavlja osnovu baze u tri dela koji se nadovezuju: generativni model i raspodele (prezentacija 1), reprezentacija sadržaja i latentni prostor (prezentacija 2), generisanje teksta i detekcija (prezentacija 3).

## Veze između prezentacija

| Pojam iz prezentacije 1 | Pojmovi koji se na njega oslanjaju |
|---|---|
| [[Uzorkovanje]] | [[Gausov šum]], [[Apriorna raspodela]] (2); [[Temperatura]], [[Strategija uzorkovanja]], [[Strategija izbora tokena]] (3) |
| [[Uslovno generisanje]] | [[Kontekst]] (3) |
| [[Verodostojnost]] | [[Perpleksnost]] (3) |
| [[Implicitni generativni model]] | [[Dekoder]], [[Latentni prostor]] (2) |
| [[Eksplicitni generativni model]] | [[Veliki jezički model]] (3) |

[[Token]] i [[Tokenizacija]] iz prezentacije 2 su osnova za pojmove prezentacije 3 koji rade nad tokenima: [[Logit]], [[Softmax]], [[Entropija sadržaja]], [[Perpleksnost]].

## Usvojeno

1. [[Strategija uzorkovanja]] i [[Strategija izbora tokena]] su dva pojma: širi (uključuje temperaturu) i uži (pravilo konačnog izbora tokena). Uža beleška linkuje širu.
2. [[Poligon]] je drugi sekundarni kontekst. Glavni primer pojma je iz konteksta [[Novinska agencija Vidik]], jednostavan iz konteksta [[Kocka]].
3. Svaki pojam ima svoju belešku u `pojmovi/`.
4. Pretpostavljeni pojmovi dopunjeni su u `_meta/odluke.md`.
5. Repozitorijum je organizovan po rundama (`runde/`).

## Izmene posle runde

- Beleške prezentacije 3 razdvojene su u pojedinačne fajlove; tekst nije menjan, osim aliasa i napomene u belešci [[Strategija izbora tokena]] u skladu sa tačkom 1.
- Dodate beleške za pojmove prezentacije 2 i beleška [[Strategija uzorkovanja]].
- Konteksti [[Novinska agencija Vidik]] i [[Kocka]] dopunjeni su elementima koje beleške koriste; dodat je kontekst [[Poligon]].
- Dodat `.gitignore`; uklonjeni automatski Python fajlovi.
- Materijali prezentacija premešteni su u `runde/runda-1/prezentacija-K/`.

## Otvorena pitanja

Vode se u `_meta/odluke.md`.
