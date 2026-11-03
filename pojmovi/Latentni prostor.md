---
tip: pojam
aliases: [latent space]
izvor: D. P. Kingma, M. Welling, „Auto-Encoding Variational Bayes“, ICLR 2014
---
# Latentni prostor (latent space)

## Definicija
Latentni prostor je skup svih mogućih vrednosti [[Latentna promenljiva|latentnih promenljivih]] modela, predstavljen kao vektorski prostor u kome svaka tačka odgovara jednom sadržaju koji model može da proizvede.

## Jednostavan primer
U modelu kocke sa parametrom θ, svaka vrednost θ od 0 do 1 daje jednu kocku. Ako se θ posmatra kao latentna promenljiva, latentni prostor je duž od 0 do 1: tačka 1/6 je poštena kocka, tačka 1/2 nameštena, a bliske tačke daju kocke sličnog ponašanja.

## Primer
Latentni prostor modela lica kojim je generisana profilna fotografija naloga „očevidac“ ima 512 dimenzija. Profilna fotografija je jedna tačka u njemu. Tačka malo pomerena od nje daje lice koje liči na profilno, sa drugačijim osmehom ili pozom.

## Kontraprimer
**Agencija Vidik.** Skup svih slika iste veličine kao profilna fotografija nije latentni prostor modela lica: njegove tačke su mreže piksela, a ne vrednosti latentnih promenljivih, i najveći deo njih ne liči na lice.

## Napomene
- Kod dobro treniranih modela bliske tačke latentnog prostora obično daju sličan sadržaj, ali to nije zagarantovano.
- Latentni prostor ne mora imati manje dimenzija od sadržaja, ali obično ima (videti [[Hipoteza mnogostrukosti]]).
- Kod modela sa [[Enkoder|enkoderom]] svaki ulazni primerak posle enkodera postaje jedna tačka latentnog prostora, a slični primerci zauzimaju bliske oblasti: fotografije mačaka su blizu fotografija pasa, a daleko od fotografija automobila.
