---
tip: pojam
aliases: [threat model, model napadača]
izvor: A. Vassilev i dr., Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations, NIST AI 100-2e2025, 2025, odeljci 2.1.2–2.1.4
---
# Model pretnje (threat model)

## Definicija
Model pretnje je eksplicitan opis napadača u odnosu na koga se procenjuje sistem detekcije: šta mu je cilj, šta zna o [[Detektor|detektoru]] i šta može da uradi sa sadržajem i sa detektorom.

## Jednostavan primer
Varalica želi da plavu, nameštenu kocku provuče kroz proveru „bar 4 šestice u 10 bacanja“. Prvi model pretnje: varalica ne zna pravilo i ne može da utiče na zapisnik. Drugi model pretnje: varalica zna pravilo i sme da prepravi poneki broj u zapisniku pre nego što ga preda. Ista provera može biti pouzdana u prvom modelu, a beskorisna u drugom.

## Primer
Agencija Vidik za nalog „očevidac“ pretpostavlja sledeći model pretnje. Cilj: redakcija da objavi generisanu fotografiju poplave kao autentičnu. Znanje: napadač zna da agencija proverava materijal, ali ne zna koji detektor koristi i ne zna [[Ključ žiga|ključ žiga]]. Mogućnosti: može da kompresuje, iseca i preslikava fotografiju, i da materijal šalje više puta sa različitih naloga, pa iz toga šta je objavljeno a šta odbijeno posredno saznaje odluke detektora. Za drugog napadača, koji želi da diskredituje dopisnika, cilj je suprotan: da redakcija autentičan izveštaj tog dopisnika proglasi generisanim.

## Kontraprimer
**Agencija Vidik.** Spisak modela kojima se služi nalog „očevidac“ nije model pretnje. On opisuje kako je sadržaj nastao, a ne šta napadač želi, zna i može protiv detektora.

## Napomene
- Tvrdnja o pouzdanosti detekcije važi samo u odnosu na model pretnje. Detektor koji je pouzdan protiv napadača bez znanja može zakazati protiv napadača koji poznaje detektor.
- Po znanju napadača razlikuju se napad bele kutije (napadač poznaje detektor u potpunosti), crne kutije (vidi samo odluke detektora) i sive kutije (delimično znanje).
- Model pretnje za [[Detekcija sa žigom|detekciju sa žigom]] obavezno kaže da li napadač zna ključ žiga i [[Mesto ugradnje žiga|mesto ugradnje žiga]].
