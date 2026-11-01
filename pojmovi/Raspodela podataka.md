---
tip: pojam
aliases: [data distribution, data-generating distribution]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, odeljak 5.2
---
# Raspodela podataka (data distribution)

## Definicija
Raspodela podataka je raspodela verovatnoće nad primercima sadržaja određene vrste koja opisuje proces kojim takvi primerci nastaju. Trening skup se posmatra kao konačan skup primeraka [[Uzorkovanje|uzorkovanih]] iz nje.

## Jednostavan primer
Kocka koju držimo u ruci daje brojeve sa raspodelom koja zavisi od njenog oblika i rasporeda mase. Tu raspodelu ne znamo; 600 zapisanih bacanja je konačan uzorak iz nje.

## Primer
Fotografije koje građani šalju preko prijemnog portala agencije Vidik nastaju određenim procesom: snimaju se telefonima, često noću i u žurbi, najčešće na mestima saobraćajnih nesreća i nevremena. Raspodela podataka za ovu vrstu sadržaja daje znatno veću verovatnoću mutnoj noćnoj fotografiji sudara nego studijskom portretu. Agencija tu raspodelu ne zna; ima samo arhivu od oko 40 000 primljenih fotografija, koja je konačan uzorak iz nje. Fotografija koja stigne sutra nije u arhivi, ali potiče iz iste raspodele. [[Generativni model]] lica sa skupa FFHQ treniran je na portretima sa Flickra, dakle na uzorku iz druge raspodele podataka, pa su njegovi izlazi portretni, a ne snimci sa terena.

## Kontraprimer

**Agencija Vidik.** Arhiva od oko 40 000 fotografija nije raspodela podataka, već samo konačan uzorak iz nje.

## Napomene
- Raspodela podataka je u praksi gotovo uvek nepoznata i dostupna je samo kroz konačan skup primeraka. Zato je generativni model uči posredno, iz tog skupa.
- Od [[Raspodela modela|raspodele modela]] se razlikuje po tome što je određena nepoznatim procesom nastanka primeraka, a ne parametrima modela.
