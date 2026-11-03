---
tip: pojam
aliases: [encoder]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, poglavlje 14
---
# Enkoder (encoder)

## Definicija
Enkoder je deo modela koji sadržaj u [[Reprezentacija medija|reprezentaciji medija]] preslikava u tačku [[Latentni prostor|latentnog prostora]].

## Jednostavan primer
Zapisnik od 600 bacanja nepoznate kocke sažme se u jedan broj: udeo šestica. Postupak koji 600 ishoda pretvara u taj broj radi kao enkoder, jer od dugog zapisa ostavlja samo ono što opisuje kocku.

## Primer
Model koji je napravio fotografiju poplave u centru Kraljeva ima enkoder koji fotografiju od nekoliko stotina hiljada brojeva (tri boje za svaki piksel) preslikava u znatno manji niz brojeva u latentnom prostoru. Isti enkoder može da sažme i fotografiju iz arhive agencije Vidik.

## Kontraprimer
**Agencija Vidik.** Smanjenje fotografije na manju rezoluciju nije enkoder u ovom smislu: rezultat je ponovo mreža piksela, a ne tačka latentnog prostora.

## Napomene
- Kod jezičkih modela termini „enkoder“ i „dekoder“ označavaju delove transformer arhitekture i nemaju isto značenje kao ovde.
- Suprotan posao radi [[Dekoder|dekoder]].
- Enkoder sažima postepeno, kroz niz slojeva, kao levak: svaki sloj ima manje brojeva i viši nivo apstrakcije. Odbacuju se detalji koji ne menjaju smisao (tačna boja svakog piksela, pozadinski šum), a ostaju ključne osobine (šta je na slici, oblik, stil, položaj).
