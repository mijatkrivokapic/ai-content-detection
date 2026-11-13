---
tip: pojam
aliases: [GAN, generative adversarial network, suparnička mreža]
izvor: I. Goodfellow i dr., „Generative Adversarial Nets“, NIPS 2014
---
# Generativna suparnička mreža (generative adversarial network, GAN)

## Definicija
Generativna suparnička mreža je [[Implicitni generativni model|implicitni generativni model]] koji se trenira u suparništvu dve neuronske mreže: generatora, koji tačku [[Latentni prostor|latentnog prostora]], uzorkovanu iz [[Apriorna raspodela|apriorne raspodele]], preslikava u primerak, i diskriminatora, klasifikatora koji za primerak procenjuje da li potiče iz trening skupa ili ga je napravio generator. Generator se podešava tako da diskriminator ne može da ih razlikuje, a diskriminator tako da ih što bolje razlikuje. Posle treniranja za generisanje se koristi samo generator.

## Jednostavan primer
U zapisniku nepoznate kocke šestica pada u polovini bacanja, a svaki drugi broj u desetini. Aparat za bacanje kocke, kome se može podešavati oblik, treba da daje ishode kao ta kocka. Posmatrač za svaki ishod procenjuje da li potiče iz zapisnika ili iz aparata. Dok aparat baca kao poštena kocka, najbolji posmatrač za šesticu procenjuje 0,75 da je iz zapisnika (0,5 / (0,5 + 1/6)), a za svaki drugi broj samo 0,375. Aparat zato pomera svoje ishode ka šestici. Kada aparat bude davao šesticu u polovini bacanja, a svaki drugi broj u desetini, posmatrač za svaki ishod procenjuje 0,5: ne može da ih razlikuje. Aparat je generator, a posmatrač diskriminator.

## Primer
Lica-G je trenirana kao GAN na fotografijama lica iz Foto-arhive. Generator iz vektora od 512 brojeva, uzorkovanih iz standardne normalne raspodele, pravi fotografiju lica od 1024×1024 piksela. Diskriminator dobija fotografije lica iz Foto-arhive i fotografije generatora i za svaku procenjuje da li je prava. Što bolje otkriva generisane fotografije, to se generator jače menja, sve dok se njegove fotografije ne prestanu prepoznavati. Posle treniranja diskriminator se odbacuje, pa je fotografija koju Lica-G pravi izlaz samog generatora za jednu tačku od 512 brojeva.

## Kontraprimer
**Kocka.** Posmatrač koji samo ocenjuje poreklo ishoda, bez aparata koji se podešava prema njegovim ocenama, nije GAN: to je samo klasifikator.

**Opšti slučaj.** Klasifikator koji za sliku kaže da li je ljudska ili generisana liči na diskriminator, ali nije GAN: nema generatora koji se prema njemu podešava i ne pravi slike.

## Napomene
- „Generator“ je ovde deo modela. U pojmu [[Trag generatora]] ista reč znači generativni model u celini.
- Generator radi kao [[Dekoder|dekoder]] bez enkodera: tačku latentnog prostora preslikava u sadržaj, ali nema načina da se sadržaj vrati u latentni prostor.
- Model je implicitan: [[Raspodela modela|raspodela modela]] zadata je samo postupkom uzorkovanja, pa [[Verodostojnost|verodostojnost]] fotografije nije dostupna.
- Diskriminator iz treniranja nije detektor: odbacuje se posle treniranja, a za detekciju je potreban poseban klasifikator, kao što je D-Klasifikator.
- Diskriminator ocenjuje pojedinačne primerke, ne raznovrsnost skupa, pa generator može da nauči samo deo raspodele podataka, na primer samo neke vrste lica.
