---
tip: pojam
aliases: [implicit generative model]
izvor: I. Goodfellow, NIPS 2016 Tutorial: Generative Adversarial Networks, arXiv:1701.00160, 2016, odeljak 2
---
# Implicitni generativni model (implicit generative model)

## Definicija
Implicitni generativni model je [[Generativni model|generativni model]] kod koga se ni [[Verodostojnost|verodostojnost]] primerka ni njena donja granica ne mogu u praksi izračunati.

## Jednostavan primer
Aparat koji baca kocku nepravilnog oblika ponaša se kao implicitni model: daje ishode, ali njihove verovatnoće nisu nigde zapisane i mogu se samo proceniti iz velikog broja bacanja.

## Primer
Model lica kojim je generisana profilna fotografija naloga „očevidac“ (StyleGAN) je implicitni generativni model. Fotografija nastaje tako što se slučajni vektor brojeva provuče kroz neuronsku mrežu. Svako uzorkovanje daje novo lice, ali model nema formulu iz koje bi se izračunalo koliko je neka fotografija verovatna. Zato agencija Vidik ne može da proveri profilnu fotografiju poređenjem verodostojnosti, kao kod opisa događaja, nego mora da traži druge tragove generisanja, na primer različite minđuše iz beleške [[Raspodela modela]].

## Napomene
- [[Raspodela modela]] implicitnog modela obično je zadata samo postupkom [[Uzorkovanje|uzorkovanja]], na primer transformacijom slučajnog šuma kroz neuronsku mrežu.
- Implicitni i [[Eksplicitni generativni model|eksplicitni generativni model]] čine podelu bez preklapanja: model je eksplicitan ako se verodostojnost ili njena donja granica mogu u praksi izračunati, a implicitan ako ne mogu.
