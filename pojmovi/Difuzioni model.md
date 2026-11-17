---
tip: pojam
aliases: [diffusion model, denoising diffusion model, DDPM]
izvor: J. Ho, A. Jain, P. Abbeel, „Denoising Diffusion Probabilistic Models“, NeurIPS 2020; J. Sohl-Dickstein i dr., „Deep Unsupervised Learning using Nonequilibrium Thermodynamics“, ICML 2015
---
# Difuzioni model (diffusion model)

## Definicija
Difuzioni model je [[Eksplicitni generativni model|eksplicitni generativni model]] koji sadržaj pravi tako što polazi od [[Gausov šum|Gausovog šuma]] iste veličine kao sadržaj i u nizu koraka iz njega postepeno uklanja šum, dok ne ostane primerak. Svaki korak izvodi neuronska mreža koja je tokom treniranja, na primercima trening skupa zašumljenim Gausovim šumom različite jačine, učila da proceni dodati šum.

## Jednostavan primer
Kocka se baca u pravilnom ritmu i zapisnik je „6,1,6,1“. Pri treniranju se ovaj niz u više koraka sve jače zašumljuje, dok od ritma ne ostane samo šum, a mreža uči da svaki korak obrne. Pri generisanju se polazi od četiri nasumična broja, na primer 3,9; 2,8; 4,6; 2,1, i u svakom koraku se brojevi pomeraju ka ritmu: 5,0; 2,0; 5,4; 1,8, pa 6,0; 1,0; 6,1; 1,1. Brojevi su ilustrativni.

## Primer
Slika-G iz prompta pravi sliku. Polazi od Gausovog šuma u latentnom prostoru oblika 64×64×4, to jest 16 384 broja, i u, na primer, 30 koraka uklanja šum. U svakom koraku mreža vidi i prompt, koji je uslov ([[Uslovno generisanje]]). Na kraju [[Dekoder|dekoder]] tačku latentnog prostora vraća u sliku od 512×512 piksela. Drugi šum na početku daje drugačiju sliku istog prompta.

## Kontraprimer
**Opšti slučaj.** Uklanjanje zrnastog šuma sa noćne fotografije snimljene fotoaparatom nije difuzioni model: cilj je da se očisti jedna postojeća fotografija, a ne da se iz Gausovog šuma napravi nova, a šum senzora u opštem slučaju nije Gausov (videti [[Gausov šum]]).

## Napomene
- Primerak nastaje kroz mnogo prolaza kroz mrežu (desetine ili više), dok [[Generativna suparnička mreža|GAN]], [[Varijacioni autoenkoder|varijacioni autoenkoder]] i [[Model toka|model toka]] primerak prave jednim prolazom.
- Verodostojnost primerka se ne računa tačno, nego samo njena donja granica, koja može biti znatno manja od stvarne; po definiciji iz [[Eksplicitni generativni model]] to je dovoljno da model bude eksplicitan. [[Uzorkovanje|Uzorkovanje]] iz njega je približno.
- Modeli slika iz teksta obično šum uklanjaju u latentnom prostoru autoenkodera, a ne u pikselima; tada se kaže da je difuzija latentna.
