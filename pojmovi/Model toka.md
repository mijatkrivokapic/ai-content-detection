---
tip: pojam
aliases: [flow model, normalizing flow, normalizujući tok, tok]
izvor: G. Papamakarios, E. Nalisnick, D. J. Rezende, S. Mohamed, B. Lakshminarayanan, „Normalizing Flows for Probabilistic Modeling and Inference“, JMLR 22, 2021
---
# Model toka (flow model)

## Definicija
Model toka je [[Eksplicitni generativni model|eksplicitni generativni model]] koji primerak dobija iz [[Gausov šum|Gausovog šuma]] iste dimenzije invertibilnim (obostrano jednoznačnim) preslikavanjem, sastavljenim od niza jednostavnih invertibilnih koraka. Pošto se svaki primerak može preslikati nazad u šum, [[Verodostojnost|verodostojnost]] primerka izračunava se tačno, iz verovatnoće odgovarajućeg šuma i promene zapremine koju preslikavanje unosi.

## Jednostavan primer
Zbir 100 kocki, kao u belešci [[Gausov šum]], ponaša se približno kao 350 + 17,1 · ε, gde je ε Gausov šum sa srednjom vrednošću 0 i rasipanjem 1. Preslikavanje ε → 350 + 17,1 · ε je invertibilno: za zbir 367 jednoznačno sledi ε = (367 − 350) / 17,1 ≈ 1,0. Gustina zbira 367 je gustina standardne normalne raspodele u ε ≈ 1,0, što je 0,24, podeljena sa 17,1 zbog razvlačenja: oko 0,014. To je najprostiji tok, sa jednim korakom; pravi modeli povezuju mnogo složenijih koraka.

## Primer
Pretpostavimo da fotografije lica pravi hipotetički model toka Lica-T, a ne GAN kao Lica-G. Za fotografiju od 256×256 piksela (196 608 brojeva) šum ima isto toliko brojeva, za razliku od vektora od 512 brojeva kod Lica-G. Ko ima pristup modelu može fotografiju preslikati nazad u šum, očitati koliko je taj šum verovatan pod standardnom normalnom raspodelom i dodati korekciju za promenu zapremine. Rezultat je tačna verodostojnost fotografije, što kod Lica-G nije moguće.

## Kontraprimer
**Kocka.** Pretvaranje vrednosti normalnog šuma u ishod kocke (šum ispod −0,97 daje jedinicu, od −0,97 do −0,43 dvojku, i tako dalje) nije invertibilno: mnogo vrednosti šuma daje isti ishod, pa se iz ishoda šum ne može jednoznačno vratiti.

**Opšti slučaj.** GAN koji iz vektora od 512 brojeva pravi fotografiju od 1024×1024 piksela nije model toka: broj ulaznih i izlaznih vrednosti se ne poklapa, pa se proizvoljna fotografija ne može vratiti u 512 brojeva.

## Napomene
- Šum ima isti broj dimenzija kao sadržaj, pa nema „uskog grla“ kao kod [[Enkoder|enkodera]]: latentni prostor ne sažima sadržaj (videti [[Hipoteza mnogostrukosti]]).
- Tačna verodostojnost zahteva determinantu Jakobijana preslikavanja, mere promene zapremine. Zato se koraci toka grade tako da se ona lako računa.
- Prevod „model toka“ nije ustaljen; engleski „normalizing flow“ doslovno je „normalizujući tok“.
