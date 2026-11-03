---
tip: pojam
aliases: [large language model, LLM, jezički model]
izvor: A. Vaswani i dr., „Attention Is All You Need", NeurIPS 2017; T. Brown i dr., „Language Models are Few-Shot Learners", NeurIPS 2020
---
# Veliki jezički model (large language model, LLM)

## Definicija
Veliki jezički model je [[Eksplicitni generativni model|eksplicitni generativni model]] nad nizovima [[Token|tokena]], najčešće autoregresivni transformer, koji uslovne verovatnoće iz [[Autoregresivna faktorizacija|autoregresivne faktorizacije]] računa neuronskom mrežom sa velikim brojem parametara, treniranom na velikom skupu tekstova.

## Jednostavan primer
Predlog sledeće reči na telefonu radi na istom principu: na osnovu onoga što je već napisano nudi reč koja najverovatnije sledi. Veliki jezički model je tako nešto, samo mnogo moćnije, pa tako može da napiše ceo esej.

## Primer
Tekst-G iz uputstva „napiši esej o klimatskim promenama" piše esej token po token. Za svaki sledeći token iz [[Kontekst|konteksta]] računa [[Logit|logite]] za svih oko 100 000 tokena rečnika, pretvara ih u raspodelu pomoću [[Softmax|softmax-a]] i iz nje bira token, sve dok ne izabere token za kraj teksta. Pošto je eksplicitan model, za bilo koji tekst, bio on ljudski ili generisan, može da izračuna [[Verodostojnost|verodostojnost]].

## Kontraprimer
Lica-G pravi fotografije lica nepostojećih osoba, ali je [[Implicitni generativni model|implicitni generativni model]]: ne daje verodostojnost i ne radi sa tokenima, pa nije veliki jezički model.

## Napomene
- Autoregresivni transformer nije vezan za tekst: isti postupak se primenjuje na svaki sadržaj predstavljen nizom tokena, na primer na proteinske sekvence. U prezentaciji se pojam ograničava na generisanje teksta.
- Radi jednostavnosti, u prezentaciji je jedan token jedna reč, iako je token najčešće deo reči.
- Veliki jezički model je polazna tačka celog izlaganja: sledeći pojmovi opisuju kako on računa, šta vidi, kako ocenjuje i bira tokene, i kako se njegov izlaz proverava.
