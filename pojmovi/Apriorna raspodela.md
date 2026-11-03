---
tip: pojam
aliases: [prior distribution, prior, apriorna raspodela P(z)]
izvor: D. P. Kingma, M. Welling, „Auto-Encoding Variational Bayes“, ICLR 2014
---
# Apriorna raspodela (prior distribution)

## Definicija
Apriorna raspodela je raspodela verovatnoće koju model pretpostavlja za [[Latentna promenljiva|latentne promenljive]] pre posmatranja bilo kakvog sadržaja. Generisanje počinje [[Uzorkovanje|uzorkovanjem]] tačke [[Latentni prostor|latentnog prostora]] iz nje.

## Jednostavan primer
Pre prvog bacanja ne znamo da li je iz džepa izvučena crvena ili plava kocka, pa pretpostavljamo da je svaka izvučena sa verovatnoćom 1/2. To je apriorna raspodela boje kocke.

## Primer
Model lica pre pravljenja profilne fotografije naloga „očevidac“ uzorkuje 512 brojeva iz standardne normalne raspodele, koja je njegova apriorna raspodela. Većina tako dobijenih tačaka leži blizu centra latentnog prostora, pa skoro svaka daje uverljivo lice.

## Kontraprimer
**Kocka.** Učestalosti ishoda izračunate posle 600 bacanja nisu apriorna raspodela, jer su dobijene posmatranjem.

## Napomene
- U bajesovskoj statistici apriorna raspodela ima šire značenje i može se odnositi na bilo koju nepoznatu veličinu, na primer na parametre modela.
- Uređena apriorna raspodela sprečava „rupe“ u latentnom prostoru: oblasti iz kojih bi [[Dekoder|dekoder]] davao besmislen sadržaj.
