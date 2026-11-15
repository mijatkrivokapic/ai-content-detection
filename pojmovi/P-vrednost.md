---
tip: pojam
aliases: [p-value]
izvor: R. L. Wasserstein, N. A. Lazar, „The ASA's Statement on p-Values: Context, Process, and Purpose", The American Statistician 70(2), 2016, str. 129–133
---
# P-vrednost (p-value)

## Definicija
P-vrednost je verovatnoća da se, ako je [[Nulta hipoteza|nulta hipoteza]] tačna, dobije bar ovoliko odstupanje od očekivanja kao posmatrano.

## Jednostavan primer
Zapisnik iz programa sa žigom (3, 5), sa [[Z-skor|z-skorom]] 6, ima p-vrednost oko 4 · 10⁻⁸: bar toliki višak petica posle trojke poštena kocka bi dala otprilike jednom u 26 miliona zapisnika. Zapisnik stvarne kocke, sa z-skorom 0,4, ima p-vrednost oko 0,37.

## Primer
Opis događaja naloga „očevidac“, sa z-skorom 6,4, ima p-vrednost oko 9 · 10⁻¹⁰. Izveštaj dopisnika, sa z-skorom 0,8, ima p-vrednost oko 0,23: tekst bez žiga ima bar toliki višak zelenih tokena u skoro četvrtini slučajeva.

## Kontraprimer
**Kocka.** P-vrednost 0,37 ne znači da je kocka poštena sa verovatnoćom 0,37.

**Agencija Vidik.** P-vrednost 9 · 10⁻¹⁰ nije verovatnoća da je opis napisao čovek. To je verovatnoća ovolikog viška zelenih tokena u tekstu koji ne nosi žig.

## Napomene
- Kod provere žiga p-vrednost je jednostrana: bitan je samo višak zelenih tokena, a ne manjak.
- Vrednosti u primerima su tačne, izračunate iz binomne raspodele broja zelenih tokena, odnosno petica posle trojke. P-vrednost izračunata iz z-skora uz normalnu raspodelu samo je približna, a daleko u repu greši mnogo: za opis naloga „očevidac“ dala bi 8 · 10⁻¹¹ umesto 9 · 10⁻¹⁰.
- Mala p-vrednost ne isključuje grešku: ako se proverava mnogo ljudskih tekstova, neki od njih će slučajno imati malu p-vrednost.
