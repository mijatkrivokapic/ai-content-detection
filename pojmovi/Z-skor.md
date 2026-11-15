---
tip: pojam
aliases: [z-score, z-statistika, standardizovana vrednost]
izvor: J. Kirchenbauer i dr., „A Watermark for Large Language Models", ICML 2023, odeljci 2 i 3.1 (z-statistika za broj zelenih tokena, jednačine 2 i 3)
---
# Z-skor (z-score)

## Definicija
Z-skor je broj standardnih devijacija za koji posmatrana vrednost slučajne promenljive odstupa od svog očekivanja pod [[Nulta hipoteza|nultom hipotezom]]: z = (posmatrano − očekivano) / standardna devijacija, gde se očekivanje i standardna devijacija računaju pod nultom hipotezom.

## Jednostavan primer
U zapisniku sa 180 trojki, pod nultom hipotezom da je kocka poštena, posle trojke petica sledi u proseku 180 · 1/6 = 30 puta, sa standardnom devijacijom √(180 · 1/6 · 5/6) = 5. Zapisnik iz programa sa žigom (3, 5) ima 60 takvih slučajeva, pa je z = (60 − 30) / 5 = 6. Zapisnik stvarne kocke ima 32, pa je z = (32 − 30) / 5 = 0,4.

## Primer
Opis događaja od 300 tokena pod nultom hipotezom da ne nosi žig ima u proseku 300 · 1/4 = 75 zelenih tokena, sa standardnom devijacijom √(300 · 1/4 · 3/4) = 7,5. Opis naloga „očevidac“ ima 123 zelena tokena, pa je z = (123 − 75) / 7,5 = 6,4. Izveštaj dopisnika iste dužine ima 81 zeleni token, pa je z = (81 − 75) / 7,5 = 0,8.

## Kontraprimer
**Kocka.** Sam broj 60 nije z-skor: isti broj petica posle trojke znači mnogo u zapisniku sa 180 trojki, a malo u zapisniku sa 1800.

**Agencija Vidik.** Udeo zelenih tokena, 123 od 300, nije z-skor: ne uzima u obzir koliko taj udeo slučajno varira pri datoj dužini teksta.

## Napomene
- Zato se odstupanja primeraka različite dužine mogu porediti.
- Uz normalnu aproksimaciju z-skor se pouzdano tumači tek kod dovoljno dugih primeraka. Kod kratkih tekstova, sa malo [[Token|tokena]], odstupanje može biti veliko i slučajno.
