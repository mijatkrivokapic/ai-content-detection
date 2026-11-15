---
tip: pojam
aliases: [watermark detection, provera žiga, provenance data detection]
izvor: NIST AI 100-4, Reducing Risks Posed by Synthetic Content, 2024, odeljak 3.2 (provenance data detection); J. Kirchenbauer i dr., „A Watermark for Large Language Models", ICML 2023
---
# Detekcija sa žigom (watermark detection)

## Definicija
Detekcija sa žigom je provera [[Vodeni žig|vodenog žiga]] [[Ključ žiga|ključem]]: meri se koliko primerak odstupa od [[Nulta hipoteza|nulte hipoteze]] da ne nosi žig sa tim ključem, a primerak se proglašava generisanim modelom sa tim ključem kada odstupanje pređe [[Prag odluke|prag odluke]].

## Jednostavan primer
Onaj ko zna ključ (3, 5) prebroji petice posle trojke, izračuna [[Z-skor|z-skor]] i zapisnik proglašava zapisnikom iz programa sa žigom kada je z-skor veći od 4. Zapisnik sa z-skorom 6 se tako označava, a zapisnik stvarne kocke, sa 0,4, ne.

## Primer
Agencija Vidik šalje opis događaja naloga „očevidac“ usluzi provere proizvođača jezičkog modela. Usluga ključem određuje zelene tokene, računa z-skor 6,4 i, sa pragom z > 4, proglašava opis generisanim tim modelom. Izveštaj dopisnika, sa z-skorom 0,8, ne prelazi prag. Ljudski tekst od 300 tokena prelazi taj prag u oko 4 od 100 000 slučajeva.

## Kontraprimer
**Kocka.** Detektor koji samo broji šestice u zapisniku nije detekcija sa žigom, jer ne koristi ključ.

**Agencija Vidik.** Detektor za tekst agencije, koji meri [[Perpleksnost|perpleksnost]], nije detekcija sa žigom, jer ne koristi ključ.

## Napomene
- Detekcija sa žigom je [[Detektor|detektor]] čija je ocena odstupanje od nulte hipoteze, na primer z-skor ili [[P-vrednost|p-vrednost]].
- Za razliku od [[Detekcija bez žiga|detekcije bez žiga]], stopa lažno pozitivnih nalaza poznata je unapred, jer sledi iz nulte hipoteze i praga. Izvor za prag z > 4 navodi oko 3 od 100 000, iz normalne aproksimacije; tačna stopa zavisi od dužine teksta i za 300 tokena iznosi oko 4 od 100 000.
- Ako primerak ne pređe prag, to ne znači da je ljudski: sadržaj drugih generatora i sadržaj iz kog je žig uklonjen takođe ne prelaze prag.
