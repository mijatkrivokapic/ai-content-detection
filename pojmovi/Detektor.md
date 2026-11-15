---
tip: pojam
aliases: [detector, detektor generisanog sadržaja, AI detector]
izvor: NIST AI 100-4, Reducing Risks Posed by Synthetic Content, 2024, odeljak 3.2 (synthetic content detection)
---
# Detektor (detector)

## Definicija
Detektor je algoritam koji primerku sadržaja dodeljuje ocenu (score) i na osnovu nje odlučuje da li je primerak [[Generisani sadržaj|generisan]].

## Jednostavan primer
Detektor prima zapisnik od 60 bacanja i treba da odluči da li su to stvarna bacanja poštene kocke ili zapisnik dobijen uzorkovanjem iz modela kocke sa θ = 1/2. Ocena je broj šestica u zapisniku. Kada ih je više od 20, detektor proglašava zapisnik generisanim.

## Primer
Svaka fotografija koja stigne preko prijemnog portala agencije Vidik prolazi kroz detektor fotografija. On joj dodeljuje ocenu od 0 do 1, a fotografije sa ocenom iznad 0,5 proglašava generisanim. Fotografija poplave naloga „očevidac“ dobija ocenu 0,93 i ne ide u objavu bez dodatne provere.

## Kontraprimer
**Kocka.** Program koji iz zapisnika samo računa broj šestica nije detektor: daje ocenu, ali ništa ne odlučuje.

**Agencija Vidik.** Filter neželjene pošte daje ocenu i donosi odluku, ali o tome da li je poruka neželjena, a ne da li je generisana, pa nije detektor u smislu ove baze.

## Napomene
- Ocena može biti verovatnoća, [[Perpleksnost|perpleksnost]] ili statistika testa. Kod P-Detektora niska ocena znači generisan sadržaj, a kod D-Klasifikatora visoka.
- Provera [[Vodeni žig|vodenog žiga]] je takođe detektor: ocena je [[Z-skor|z-skor]] broja tokena sa zelene liste, a odluka da li je on prevelik za slučajnost.
- Čovek koji procenjuje poreklo sadržaja nije detektor u smislu ove baze, iako radi detekciju.
- Detektor može biti proširen tako da određuje i koji je deo primerka generisan, ili kojim je generativnim modelom primerak dobijen.
