---
tip: pojam
aliases: [reconstruction, greška rekonstrukcije, reconstruction error]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, poglavlje 14
---
# Rekonstrukcija (reconstruction)

## Definicija
Rekonstrukcija primerka je sadržaj koji se dobija kada se primerak [[Enkoder|enkoderom]] preslika u [[Latentni prostor|latentni prostor]], a zatim [[Dekoder|dekoderom]] vrati u [[Reprezentacija medija|reprezentaciju medija]]. Razlika između primerka i njegove rekonstrukcije, greška rekonstrukcije, pokazuje koliko informacija o primerku latentni prostor čuva.

## Jednostavan primer
Zapisnik od 600 bacanja sažme se u udeo šestica, pa se iz tog broja virtuelnom kockom napravi novi zapisnik od 600 bacanja. Broj šestica u novom zapisniku biće sličan originalnom, ali redosled ishoda je izgubljen: sažetak ga nije sačuvao.

## Primer
Fotografija iz arhive agencije Vidik propuštena kroz enkoder i dekoder modela koji je napravio fotografiju poplave na prvi pogled izgleda isto kao original. Sitni detalji, na primer tekst na saobraćajnom znaku u pozadini, postaju razliveni, jer ih latentni prostor nije sačuvao.

## Kontraprimer
**Agencija Vidik.** Kopija fotografije sačuvana u drugom formatu nije rekonstrukcija, jer nije prošla kroz latentni prostor.

## Napomene
- Treniranje kroz rekonstrukciju ne zahteva da iko označi šta je bitno u primerku: model to otkriva tako što pokušava da primerak vrati iz sažetka.
- Sažeti zapis je „usko grlo“: u njega ne može da stane sve, pa je model primoran da sačuva opšta pravila i oblike, a da zanemari slučajne detalje. Poređenje originala i rekonstrukcije je signal iz koga model uči šta je bitno.
