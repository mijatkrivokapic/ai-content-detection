---
tip: pojam
aliases: [token, rečnik modela, vocabulary]
izvor: R. Sennrich, B. Haddow, A. Birch, „Neural Machine Translation of Rare Words with Subword Units“, ACL 2016
---
# Token (token)

## Definicija
Token je element konačnog skupa simbola, rečnika modela, od kojih model sastavlja niz kojim predstavlja sadržaj. Svaki token u rečniku ima svoj redni broj.

## Jednostavan primer
Zapis bacanja kocke može se graditi od rečnika sa sedam tokena: brojevi od 1 do 6 i zarez. Niz „6,1,6“ tada se sastoji od pet tokena. Redni broj tokena u rečniku je samo oznaka mesta; token „6“ nije „veći“ od tokena „1“ zato što mu je redni broj veći.

## Primer
Rečnik jezičkog modela kojim je generisan opis događaja naloga „očevidac“ ima oko 100 000 tokena. U njemu su cele česte reči, kao „je“ i „u“, delovi reči, kao „nost“, pojedinačna slova i znakovi interpunkcije. Svaka reč iz opisa, pa i neobična reč iz izveštaja dopisnika agencije Vidik, može se sastaviti od tokena iz tog rečnika.

## Kontraprimer
**Agencija Vidik.** Jedan piksel fotografije poplave nije token: njegova vrednost nije izabrana iz konačnog rečnika simbola, nego je broj koji može imati bilo koju od mnogo vrednosti.

## Napomene
- Kod teksta token najčešće nije cela reč, nego deo reči. U primerima se radi jednostavnosti često uzima da je jedan token jedna reč.
- Token nije vezan samo za tekst: i zvuk i slika se mogu pretvoriti u nizove tokena iz konačnog rečnika.
- Postupak kojim se sadržaj razlaže na tokene je [[Tokenizacija|tokenizacija]], a vektor koji model dodeljuje tokenu je njegovo [[Ugrađivanje|ugrađivanje]].
- Sam redni broj tokena nema matematičko značenje; ono nastaje tek kada se token zameni svojim ugrađivanjem.
