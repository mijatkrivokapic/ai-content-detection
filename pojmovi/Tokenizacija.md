---
tip: pojam
aliases: [tokenization, tokenizer]
izvor: R. Sennrich, B. Haddow, A. Birch, „Neural Machine Translation of Rare Words with Subword Units“, ACL 2016; A. Petrov i dr., „Language Model Tokenizers Introduce Unfairness Between Languages“, NeurIPS 2023
---
# Tokenizacija (tokenization)

## Definicija
Tokenizacija je postupak kojim se sadržaj razlaže u niz [[Token|tokena]] iz rečnika modela, posle čega se svaki token zamenjuje svojim rednim brojem u rečniku.

## Jednostavan primer
Zapisnik „šestica, jedinica, šestica“ tokenizuje se rečnikom kocke u niz tokena „6“, „,“, „1“, „,“, „6“, a zatim u niz njihovih rednih brojeva u rečniku.

## Primer
Pre nego što jezički model izračuna verodostojnost opisa događaja naloga „očevidac“, tokenizer razlaže rečenicu „Nesreća se dogodila u noći.“ na tokene, na primer „Nes“, „reća“, „ se“, „ dogodila“, „ u“, „ noći“ i „.“. Česte reči postaju jedan token, a ređe reči se dele na delove.

## Kontraprimer
**Agencija Vidik.** Deljenje izveštaja dopisnika na rečenice ili pasuse nije tokenizacija u ovom smislu: rečenice nisu elementi konačnog rečnika modela.

## Napomene
- Rečnici tokenizera građeni su pretežno na engleskim tekstovima, pa isti sadržaj na srpskom daje primetno više tokena nego na engleskom.
- Broj tokena u sadržaju određuje koliko podataka detektor ima na raspolaganju, pa je kratak tekst teže pouzdano proveriti.
- Deljenje na delove reči čuva korene i nastavke, pa model može da predstavi i reč koju nikad nije video kao celinu, bez posebnog tokena za „nepoznatu reč“.
