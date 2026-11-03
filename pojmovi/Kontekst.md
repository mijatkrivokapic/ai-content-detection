---
tip: pojam
aliases: [context]
izvor: T. Brown i dr., „Language Models are Few-Shot Learners", NeurIPS 2020
---
# Kontekst (context)

## Definicija
Kontekst je deo niza koji prethodi elementu koji model trenutno generiše, zajedno sa zadatim uslovom, na osnovu kog model računa raspodelu verovatnoće tog elementa.

## Jednostavan primer
Kada prijatelj započne „Pada…", skoro sigurno znaš da sledi „kiša". Znaš to zato što čuješ šta je pre toga rečeno, a ne zato što gledaš unapred. Kontekst je upravo ono što je do sada rečeno.

## Primer
Kada Tekst-G piše peti token eseja, kontekst čine uputstvo „napiši esej o klimatskim promenama" i četiri već napisana tokena („Klima se menja brzo"). Za šesti token kontekst se produžava za upravo izabrani peti token.

## Kontraprimer
Tokeni koji tek dolaze nisu deo konteksta: model ih još nije napisao i ne mogu da utiču na izbor trenutnog tokena. Model nikada ne „gleda unapred".

## Napomene
- Uslov je ono što je zadato spolja ([[Uslovno generisanje|uslovno generisanje]]), a kontekst obuhvata i tokene koje je model sam generisao.
- Najveća dužina konteksta koju model može da obradi naziva se kontekstni prozor (context window).
- Kontekst je „uslov" iz [[Autoregresivna faktorizacija|autoregresivne faktorizacije]]; iz njega model računa [[Logit|logite]].
