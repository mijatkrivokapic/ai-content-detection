---
tip: pojam
aliases: [unseen generator, nepoznati generator, generator van trening skupa]
izvor: U. Ojha, Y. Li, Y. J. Lee, „Towards Universal Fake Image Detectors that Generalize Across Generative Models", CVPR 2023. Termin „neviđeni generator" nije ustaljen.
---
# Neviđeni generator (unseen generator)

## Definicija
Neviđeni generator je, u odnosu na dati [[Naučeni detektor|naučeni detektor]], [[Generativni model|generativni model]] čiji primerci nisu bili u trening skupu tog detektora. Detektor je naučio [[Trag generatora|tragove]] generatora koje je video, pa tragovi neviđenog generatora, koji potiču iz druge [[Raspodela modela|raspodele modela]], za njega mogu biti nepoznati.

## Jednostavan primer
Pravilo „kocka je nameštena ako u 10 bacanja padnu bar 4 šestice“ izvedeno je posmatranjem plave kocke, koja je nameštena na šesticu. Zelena kocka je nameštena na jedinicu, pa joj šestica pada sa verovatnoćom 1/10, ređe nego kod poštene kocke. Pravilo je proglašava nameštenom u oko 1% provera: za ovo pravilo zelena kocka je neviđeni generator.

## Primer
Detektor fotografija agencije Vidik treniran je na licima koja pravi model lica (StyleGAN, [[Generativna suparnička mreža|generativna suparnička mreža]]) i na autentičnim portretima. Fotografija poplave u centru Kraljeva napravljena je modelom slika iz teksta, koji radi u latentnom prostoru i ostavlja drugačije tragove. Za taj detektor model slika iz teksta je neviđeni generator, pa detektor fotografiju poplave označi kao ljudsku.

## Kontraprimer
**Agencija Vidik.** Nova profilna fotografija koju model lica napravi iz drugog vektora šuma nije primerak neviđenog generatora, iako tu fotografiju detektor nikad nije video. Detektor je video primerke istog generatora, pa za taj generator važe naučeni tragovi.

## Napomene
- Pojam je relativan: isti generator je neviđen za jedan detektor, a viđen za drugi.
- Detektor treniran samo na slikama generativnih suparničkih mreža po pravilu zakazuje na slikama [[Difuzioni model|difuzionih modela]]. Ojha i dr. to objašnjavaju time što detektor uči tragove „generisane“ klase, a sve što te tragove nema svrstava u ljudsku klasu.
- Stopa otkrivanja izmerena na viđenim generatorima ne važi za neviđene, pa se kod procene detektora navodi odvojeno.
