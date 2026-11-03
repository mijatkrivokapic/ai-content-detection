---
tip: pojam
aliases: [autoregressive factorization]
izvor: Y. Bengio, R. Ducharme, P. Vincent, C. Jauvin, „A Neural Probabilistic Language Model", Journal of Machine Learning Research 3, 2003
---
# Autoregresivna faktorizacija (autoregressive factorization)

## Definicija
Autoregresivna faktorizacija je razlaganje verovatnoće niza na proizvod uslovnih verovatnoća njegovih elemenata, pri čemu se verovatnoća svakog elementa računa uz uslov svih elemenata pre njega.

p(x1, …, xn) = ∏ p(xi | x1, …, xi−1)

## Jednostavan primer
Verovatnoća da iz špila od 52 karte zaredom izvučeš dva asa nije 4/52 puta 4/52, nego 4/52 puta 3/51. Druga verovatnoća se računa uz uslov da je prvi izvučeni as već izašao. Autoregresivna faktorizacija radi isto, samo sa rečima umesto karata.

## Primer
Tekst-G rečenici „Danas je lep dan." dodeljuje verovatnoću kao proizvod četiri koraka: P(Danas) = 10%, P(je | Danas) = 50%, P(lep | Danas je) = 40% i P(dan | Danas je lep) = 60%. Proizvod je 1,2%. Isto razlaganje omogućava i pisanje: model izabere „Danas", pa „je" uz uslov „Danas", i tako dalje, token po token. Brojevi su ilustrativni.

## Kontraprimer
Ista četiri tokena u obrnutom redosledu, „Dan lep je danas.", imaju korake od 2%, 1%, 5% i 1%, pa proizvod iznosi svega 0,00001%. Kada bi se tokeni birali nezavisno, bez uslova, redosled ne bi bio važan i obe rečenice bile bi jednako verovatne.

## Napomene
- Razlaganje je tačno za svaku raspodelu nad nizovima, jer sledi iz pravila proizvoda verovatnoće. Modeli se razlikuju samo po tome kako aproksimiraju uslovne verovatnoće.
- Isti postupak služi i za ocenjivanje gotovog teksta (množenje verovatnoća) i za pisanje novog.
- Ono što stoji iza „uz uslov" je [[Kontekst]]. [[Perpleksnost]] se računa iz istih koraka.
- [[Veliki jezički model]] je primena ove faktorizacije.
