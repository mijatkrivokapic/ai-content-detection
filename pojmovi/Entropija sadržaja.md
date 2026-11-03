---
tip: pojam
aliases: [content entropy, entropija]
izvor: J. Kirchenbauer i dr., „A Watermark for Large Language Models", ICML 2023. Termin „entropija sadržaja" nije ustaljen.
---
# Entropija sadržaja (content entropy)

## Definicija
Entropija sadržaja je prosečna Šenonova entropija raspodela iz kojih su uzorkovanjem izabrani elementi tog sadržaja. Meri koliko je slobode izbora model imao pri njegovom generisanju.

H(p) = −Σ p(v) · log p(v)

## Jednostavan primer
Popunjavanje formulara sa unapred ispisanim poljima ima malo slobode (niska entropija), a pisanje slobodnog sastava na zadatu temu mnogo (visoka entropija). Entropija meri koliko je izbora autor zaista imao.

## Primer
Na zahtev da napiše funkciju koja sabira dva broja, Tekst-G posle `return a +` bira „b" sa verovatnoćom 99%, pa je entropija te raspodele skoro nula. U eseju o klimatskim promenama skoro svaki sledeći token ima desetine verovatnih kandidata, pa je entropija eseja visoka.

## Kontraprimer
Entropija ne meri dužinu ni težinu teksta. Dugačak, složen tekst koji model piše gotovo bez izbora ima nisku entropiju.

## Napomene
- Definicija je precizna i izračunljiva za nizove tokena. Za slike i druge medije pojam se koristi u prenesenom smislu.
- Entropija sadržaja meri neizvesnost raspodela iz kojih se biralo, a [[Perpleksnost]] meri koliko je model iznenađen izborima koji su stvarno napravljeni.
- Kada je entropija niska, malo je prostora i za [[Vodeni žig|vodeni žig]] i za tragove generatora: posle `return a +` žig ne može da pomeri izbor tokena „b".
- Raspodele iz kojih se računa entropija dobijaju se iz [[Logit|logita]] pomoću [[Softmax|softmax-a]].
