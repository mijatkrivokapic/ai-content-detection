---
tip: pojam
aliases: [latent variable, latentni vektor, z]
izvor: C. M. Bishop, Pattern Recognition and Machine Learning, Springer, 2006, poglavlje 9
---
# Latentna promenljiva (latent variable)

## Definicija
Latentna promenljiva je slučajna promenljiva modela čija se vrednost ne posmatra u podacima, a od koje zavise vrednosti koje se posmatraju.

## Jednostavan primer
U džepu su crvena poštena i plava nameštena kocka. Neko izvuče jednu i baca je, a mi vidimo samo ishode, ne i boju kocke. Boja je latentna promenljiva: ne vidimo je, a od nje zavisi koliko često pada šestica.

## Primer
Profilna fotografija naloga „očevidac“ nastala je iz vektora od 512 brojeva koji je model lica provukao kroz neuronsku mrežu. Tih 512 brojeva su latentne promenljive: na fotografiji se ne vide, ali od njih zavise poza, osmeh i osvetljenje lica. Nijedan pojedinačni broj ne odgovara samo pozi ili samo osmehu.

## Kontraprimer
**Agencija Vidik.** Vrednosti piksela profilne fotografije nisu latentne promenljive, jer se direktno posmatraju.

## Napomene
- Kod varijacionog autoenkodera latentna promenljiva se računa kao z = μ + σ · ε, gde enkoder daje sredinu μ i rasipanje σ, a ε je [[Gausov šum]]. To je poseban slučaj, vezan za tu arhitekturu, koja je predviđena za rundu 2.
- Skup svih mogućih vrednosti latentnih promenljivih je [[Latentni prostor|latentni prostor]].
