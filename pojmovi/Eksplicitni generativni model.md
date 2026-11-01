---
tip: pojam
aliases: [explicit generative model]
izvor: I. Goodfellow, NIPS 2016 Tutorial: Generative Adversarial Networks, arXiv:1701.00160, 2016, odeljak 2
---
# Eksplicitni generativni model (explicit generative model)

## Definicija
Eksplicitni generativni model je [[Generativni model|generativni model]] kod koga se [[Verodostojnost|verodostojnost]] primerka, ili njena donja granica, može u praksi izračunati.

## Jednostavan primer
Model kocke zapisan kao tabela šest verovatnoća je eksplicitan: verodostojnost svakog ishoda čita se direktno iz tabele.

## Primer
Jezički model naloga „očevidac“ je eksplicitni generativni model: verodostojnost opisa događaja izračunava se kao proizvod verovatnoća reči, kao u beleški [[Verodostojnost]]. Agencija Vidik, ako ima pristup tom ili sličnom modelu, može za svaki pristigli opis da izračuna koliko je on verovatan pod modelom.

## Kontraprimer
**Kocka.** Aparat koji baca kocku nepravilnog oblika nije eksplicitan: daje ishode, ali njihova verodostojnost ne može da se izračuna.

**Agencija Vidik.** Model lica kojim je generisana profilna fotografija naloga „očevidac“ (StyleGAN) nije eksplicitan: daje fotografiju, ali ne i njenu verodostojnost, pa agencija tu fotografiju ne može da proveri na isti način kao opis događaja.

## Napomene
- Neki modeli, na primer varijacioni autoenkoderi i difuzioni modeli, daju samo donju granicu verodostojnosti, koja može biti znatno manja od stvarne vrednosti. Za procenu primerka ona je manje pouzdana od tačne verodostojnosti.
