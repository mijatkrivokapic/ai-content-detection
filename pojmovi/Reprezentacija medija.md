---
tip: pojam
aliases: [media representation, reprezentacija sadržaja]
izvor: Nema ustaljene definicije; didaktički termin (videti Pojmovnik, pojam 10).
---
# Reprezentacija medija (media representation)

## Definicija
Reprezentacija medija je oblik u kom se sadržaj jednog medija predaje modelu kao ulaz ili dobija od njega kao izlaz: struktura podataka i vrsta njenih osnovnih elemenata, na primer niz [[Token|tokena]] za tekst, mreža piksela za sliku ili niz vrednosti signala za zvuk.

## Jednostavan primer
Isti ishod bacanja kocke može se zapisati kao broj 6, kao reč „šestica“ ili kao fotografija kocke sa šest tačkica na gornjoj strani. Ishod je isti, a reprezentacije su tri, i model koji prima jednu ne može direktno da radi sa drugom.

## Primer
Nalog „očevidac“ šalje redakciji agencije Vidik opis događaja i fotografiju poplave. Jezički model opis prima i daje kao niz tokena, dok je fotografija za model mreža piksela, za svaki piksel tri broja (crvena, zelena i plava komponenta). Detektor koji agencija koristi za tekst zato ne može bez izmene da se primeni na fotografiju.

## Kontraprimer
**Agencija Vidik.** Vektori koje model računa unutar sebe, na primer tačka [[Latentni prostor|latentnog prostora]] iz koje je nastala profilna fotografija naloga „očevidac“, nisu reprezentacija medija, iako se u literaturi i oni zovu reprezentacijama. Reprezentacija medija je spoljašnji oblik sadržaja, onaj u kome ga model prima ili predaje.

## Napomene
- Isti sadržaj može imati više reprezentacija: zvuk se može predstaviti kao niz vrednosti signala ili kao spektrogram. Izbor reprezentacije određuje gde detektor traži tragove generatora.
- Pregled reprezentacija za ostale medije (video, 3D modeli, grafovi, proteini) predviđen je za rundu 2.
