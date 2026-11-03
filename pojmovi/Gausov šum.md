---
tip: pojam
aliases: [Gaussian noise, ε, epsilon]
izvor: J. Ho, A. Jain, P. Abbeel, „Denoising Diffusion Probabilistic Models“, NeurIPS 2020
---
# Gausov šum (Gaussian noise)

## Definicija
Gausov šum je skup vrednosti nezavisno [[Uzorkovanje|uzorkovanih]] iz normalne raspodele sa srednjom vrednošću nula, koji se dodaje sadržaju ili služi kao početna tačka generisanja.

## Jednostavan primer
Baci se 100 kocki i od zbira se oduzme 350, koliko zbir iznosi u proseku. Ako se to ponovi mnogo puta, dobijene vrednosti se ponašaju približno kao Gausov šum: najčešće su blizu nule, a velika odstupanja na obe strane su retka.

## Primer
Vektor od 512 brojeva iz kog je model lica napravio profilnu fotografiju naloga „očevidac“ je Gausov šum uzorkovan iz [[Apriorna raspodela|apriorne raspodele]]. Drugi uzorak šuma dao bi lice druge osobe koja takođe ne postoji.

## Kontraprimer
**Agencija Vidik.** Zrnast šum na mutnim noćnim fotografijama iz arhive agencije nije Gausov šum u smislu definicije: nastaje u senzoru telefona i u opštem slučaju nije nezavisno uzorkovan iz normalne raspodele.

## Napomene
- U obradi zvuka „šum“ obično znači neželjene pozadinske zvuke, koji po pravilu nisu Gausovi.
- Difuzioni modeli, predviđeni za rundu 2, generisanje počinju od Gausovog šuma i postepeno ga uklanjaju.
- U varijacionom autoenkoderu Gausov šum ε dodaje se sažetom zapisu (videti [[Latentna promenljiva]]): unosi malu varijaciju, pa okolina svake tačke latentnog prostora postaje upotrebljiva, a model pri generisanju dobija sveže varijacije istog sadržaja.
