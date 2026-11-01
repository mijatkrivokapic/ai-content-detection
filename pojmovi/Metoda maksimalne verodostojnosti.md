---
tip: pojam
aliases: [maximum likelihood estimation, MLE]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, odeljak 5.5
---
# Metoda maksimalne verodostojnosti (maximum likelihood estimation)

## Definicija
Metoda maksimalne verodostojnosti je metoda procene parametara modela u kojoj se biraju one vrednosti parametara za koje skup opaženih primeraka ima najveću ukupnu [[Verodostojnost|verodostojnost]]. Ukupna verodostojnost nezavisnih primeraka je proizvod njihovih pojedinačnih verodostojnosti, pa se u praksi ekvivalentno maksimizuje zbir log-verodostojnosti.

## Jednostavan primer
Posle 10 bacanja sa 5 šestica, ukupna verodostojnost opaženih ishoda najveća je za vrednost parametra „verovatnoća šestice“ jednaku 1/2, a ne 1/6.

## Primer
Jezički model naloga „očevidac“ treniran je na novinskim tekstovima sa interneta. U njima se posle reči „Nesreća se dogodila u“ nastavak javlja 1 000 puta, od toga 250 puta „noći“. Metoda maksimalne verodostojnosti bira parametre tako da trenirajući tekstovi dobiju što veću ukupnu verodostojnost. U idealnom slučaju to znači da model reči „noći“ posle ovih reči dodeljuje verovatnoću 250/1000 = 0,25.

