---
tip: pojam
aliases: [softmax]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, odeljak 6.2.2
---
# Softmax (softmax)

## Definicija
Softmax je funkcija koja skup realnih brojeva ([[Logit|logita]]) pretvara u raspodelu verovatnoće: svaki broj se stepenuje (exp), a zatim podeli zbirom svih stepenovanih brojeva, pa su rezultati pozitivni i u zbiru daju 1.

p(i) = exp(z(i)) / Σ exp(z(j)), gde je z(i) logit tokena i

## Jednostavan primer
Podela nagrade srazmerno poenima: takmičar sa više poena dobija veći udeo, a svi udeli zajedno daju celu nagradu (100%). Razlika je u tome što softmax poene prvo stepenuje, pa i ocene koje su negativne daju pozitivan udeo.

## Primer
Tri tokena imaju logite 2, 1 i 0. Stepenovanjem se dobijaju brojevi 7,4, 2,7 i 1 (zbir 11,1). Deljenjem svakog zbirom dobijaju se verovatnoće 67%, 24% i 9%, koje daju 100%. Tekst-G isto radi nad celim rečnikom od oko 100 000 tokena.

## Kontraprimer
Ocene se ne mogu prosto podeliti njihovim zbirom: negativne ocene bi dale negativne „procente". Zato se prvo stepenuju, tako da svi brojevi postanu pozitivni.

## Napomene
- Veći logit uvek daje veću verovatnoću, ali softmax ističe razlike: mala razlika u logitima daje primetnu razliku u verovatnoći.
- [[Temperatura]] se primenjuje tako što se logiti podele temperaturom pre softmax-a.
- Pojam nije u osnovnoj listi, ali je potreban da bi se razumeli [[Logit]] i [[Temperatura]].
