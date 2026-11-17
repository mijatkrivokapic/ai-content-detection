---
tip: pojam
aliases: [TPR@FPR, TPR at fixed FPR, true positive rate at fixed false positive rate, stopa otkrivanja pri fiksnom FPR]
izvor: K. Krishna i dr., „Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense", NeurIPS 2023, odeljak 4.1
---
# Stopa otkrivanja pri fiksnoj stopi lažno pozitivnih nalaza (TPR@FPR)

## Definicija
Stopa otkrivanja pri fiksnoj stopi lažno pozitivnih nalaza je [[Stopa otkrivanja|stopa otkrivanja]] koju [[Detektor|detektor]] postiže kada je [[Prag odluke|prag odluke]] izabran tako da [[Stopa lažno pozitivnih nalaza|stopa lažno pozitivnih nalaza]] ne bude veća od unapred zadate vrednosti, na primer 1%.

## Jednostavan primer
Pravilo „kocka je nameštena ako u 10 bacanja padne bar k šestica“ ima prag k:

| Prag k | Stopa lažno pozitivnih nalaza (crvena kocka) | Stopa otkrivanja (plava kocka) |
|---|---|---|
| 3 | 23% | 95% |
| 4 | 7% | 83% |
| 5 | 1,5% | 62% |

Ako je dozvoljeno najviše 5% lažno pozitivnih nalaza, pragovi 3 i 4 ne dolaze u obzir, a najniži dozvoljeni je 5. Stopa otkrivanja pri fiksnoj stopi lažno pozitivnih nalaza od 5% je zato 62%, a ne 95% koliko pravilo postiže sa pragom 3.

## Primer
Agencija Vidik bira između dva detektora za fotografije. Detektor A na svom podrazumevanom pragu otkriva 92% generisanih fotografija, ali lažno optuži 10% ljudskih. Detektor B otkriva 85%, uz 2% lažno optuženih. Agencija ne sme da optuži više od 1% autentičnih snimaka građana, pa oba praga podesi tako da stopa lažno pozitivnih nalaza na arhivi primljenih fotografija bude 1%. Tada detektor A otkriva 40%, a detektor B 80% generisanih fotografija. Na podrazumevanim pragovima A je izgledao bolje, a pri zahtevu agencije bolji je B. Brojevi su ilustrativni.

## Kontraprimer
**Agencija Vidik.** Ako proizvođač detektora prijavi 95% otkrivanja pri 1% lažno pozitivnih nalaza merenih na dnevnim fotografijama iz foto-banke, to nije stopa otkrivanja pri fiksnoj stopi lažno pozitivnih nalaza za agenciju. Na noćnim i mutnim snimcima iz arhive isti prag može dati znatno više lažno pozitivnih nalaza, pa prag treba ponovo odrediti na ljudskom sadržaju koji agencija stvarno prima.

## Napomene
- Kod [[Detekcija bez žiga|detekcije bez žiga]] prag se određuje empirijski, iz ocena koje detektor daje ljudskim primercima. Kod [[Detekcija sa žigom|detekcije sa žigom]] prag na [[P-vrednost|p-vrednosti]] direktno zadaje stopu lažno pozitivnih nalaza, bez merenja na ljudskom sadržaju.
- U radovima o detekciji generisanog teksta uobičajeno je navoditi stopu otkrivanja pri niskoj stopi lažno pozitivnih nalaza, najčešće 1%, umesto mera koje uprosečavaju sve pragove.
