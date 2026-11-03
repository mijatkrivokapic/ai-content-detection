---
tip: pojam
aliases: [logit, logits]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, odeljak 6.2.2
---
# Logit (logit)

## Definicija
Logit je realan broj koji model dodeljuje jednoj od mogućih vrednosti izlaza pre normalizacije. [[Softmax]] pretvara logite svih mogućih vrednosti u raspodelu verovatnoće, tako da veći logit daje veću verovatnoću.

## Jednostavan primer
Žiri na takmičenju daje poene svakom takmičaru. Poeni su sirove ocene i još nisu procenti: tek kada se pretvore u udeo glasova dobijamo verovatnoće. Logit je takav sirov poen.

## Primer
Posle konteksta „Danas je" Tekst-G tokenu „lep" dodeljuje logit 5,1, a tokenu „petak" logit 4,4 (i tako za svih oko 100 000 tokena rečnika). Softmax nad celim rečnikom to pretvara u verovatnoće 40% i 20%. Razlika logita od 0,7 znači otprilike dvostruko veću verovatnoću, jer je e na 0,7 približno 2.

## Kontraprimer
Logit nije verovatnoća. Može biti negativan (−1,2) ili veći od 1 (5,1), a zbir logita ne daje 100%.

## Napomene
- U statistici „logit" označava logaritam šanse, log(p / (1 − p)). U dubokom učenju termin se koristi šire, za svaki izlaz pre softmax-a.
- Na logitima se primenjuju [[Temperatura|temperatura]] (deli ih) i [[Vodeni žig|vodeni žig]] (dodaje malu vrednost logitima tokena sa zelene liste).
- Logite model računa iz [[Kontekst|konteksta]].
