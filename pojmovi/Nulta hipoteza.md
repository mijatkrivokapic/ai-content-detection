---
tip: pojam
aliases: [null hypothesis, H0]
izvor: NIST/SEMATECH e-Handbook of Statistical Methods, odeljak 1.3.5 (Hypothesis Tests), https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm; J. Kirchenbauer i dr., „A Watermark for Large Language Models", ICML 2023, odeljak 2
---
# Nulta hipoteza (null hypothesis)

## Definicija
Nulta hipoteza je pretpostavka o raspodeli slučajne promenljive. Zadržava se, osim ako je posmatrana vrednost pod njom suviše malo verovatna.

## Jednostavan primer
Nulta hipoteza za zapisnik bacanja glasi: kocka je poštena i bacanja su nezavisna, pa posle trojke petica sledi sa verovatnoćom 1/6. Zadržava se dok broj petica posle trojke ne postane suviše veliki da bi bio slučajan.

## Primer
Kada agencija Vidik proverava žig u opisu događaja naloga „očevidac“, nulta hipoteza glasi: opis ne nosi [[Vodeni žig|žig]] sa [[Ključ žiga|ključem]] proizvođača jezičkog modela, pa je svaki token zelen sa verovatnoćom 1/4, nezavisno od ostalih.

## Kontraprimer
**Kocka.** „Zapisnik su napravila stvarna bacanja“ nije nulta hipoteza provere žiga (3, 5): pravu nultu hipotezu zadovoljava i zapisnik iz programa koji ne ugrađuje taj žig.

**Agencija Vidik.** „Opis je napisao čovek“ nije nulta hipoteza provere žiga: pravu nultu hipotezu, da opis ne nosi žig, zadovoljava i opis koji je napisao drugi jezički model.

## Napomene
- Nulta hipoteza se ne dokazuje. Kada se zadrži, to znači samo da podaci nisu dovoljni da je odbace.
- Koliko je „suviše malo verovatna“ određuje [[P-vrednost|p-vrednost]] u poređenju sa izabranim pragom.
