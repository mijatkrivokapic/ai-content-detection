---
tip: pojam
aliases: [watermark key, ključ vodenog žiga, tajni ključ]
izvor: NIST AI 100-4, Reducing Risks Posed by Synthetic Content, 2024, odeljci 3.1.1.1 i 3.1.1.4; J. Kirchenbauer i dr., „A Watermark for Large Language Models", ICML 2023
---
# Ključ žiga (watermark key)

## Definicija
Ključ žiga je tajna vrednost bez koje se [[Vodeni žig|vodeni žig]] ne može ni ugraditi ni proveriti: žig ugrađen jednim ključem može da proveri samo onaj ko zna taj ključ.

## Jednostavan primer
Program koji „baca“ virtuelnu kocku ugrađuje žig: posle svake trojke češće bira peticu nego što bi to poštena kocka radila. Par (3, 5) je ključ. Ko ga zna, prebroji koliko puta posle trojke sledi petica i vidi da je to previše za slučajnost. Ko ga ne zna, ne zna šta da broji.

## Primer
Jezički model kojim se služi nalog „očevidac“ ugrađuje vodeni žig pri [[Mesto ugradnje žiga|uzorkovanju]], a ključ drži proizvođač modela. Agencija Vidik ne može sama da proveri žig u opisu događaja, nego opis šalje usluzi provere koju nudi proizvođač i od nje dobija odgovor. Za svaki model sa drugim ključem agencija bi morala da koristi drugu uslugu.

## Kontraprimer
**Kocka.** Seme (seed) programa koji baca virtuelnu kocku određuje koji se zapisnik dobija, ali nije ključ žiga: ne menja raspodelu iz koje se bira, pa zapisnik ne nosi obrazac po kome bi se razlikovao od stvarnih bacanja.

**Agencija Vidik.** Isto važi za seme kojim je uzorkovan vektor od 512 brojeva za profilnu fotografiju naloga „očevidac“.

## Napomene
- Onaj ko drži ključ jedini može da proveri žig, pa postaje usko grlo: svaki primalac sadržaja mora da mu veruje i da koristi njegovu uslugu.
- Javni žig, čiji se ključ objavljuje, nije obuhvaćen ovom definicijom: tada svako može da proveri žig, ali i da ga lažno ugradi u ljudski sadržaj.
- Postoje i predlozi kod kojih se žig ugrađuje tajnim ključem, a proverava javnom vrednošću ili posebnom mrežom, pa ga svako može proveriti, a niko lažirati. Ni oni nisu obuhvaćeni ovom definicijom.
