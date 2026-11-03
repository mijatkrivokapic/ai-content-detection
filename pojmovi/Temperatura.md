---
tip: pojam
aliases: [temperature]
izvor: A. Holtzman i dr., „The Curious Case of Neural Text Degeneration", ICLR 2020
---
# Temperatura (temperature)

## Definicija
Temperatura je pozitivan parametar kojim se pre primene [[Softmax|softmax-a]] dele svi [[Logit|logiti]]. Vrednost manja od 1 koncentriše raspodelu na najverovatnije vrednosti, a vrednost veća od 1 je izravnava.

p(i) = exp(z(i) / T) / Σ exp(z(j) / T)

## Jednostavan primer
Zamisli da u restoranu uvek naručuješ najpopularnije jelo (niska temperatura) ili da nasumično biraš sa celog jelovnika (visoka temperatura). Niska temperatura daje sigurne, predvidljive izbore, a visoka raznovrsnije, ali i neobičnije.

## Primer
Neka „lep" ima logit veći za 0,7 od „petak". Pri temperaturi 1 „lep" je oko 2 puta verovatniji od „petka". Pri temperaturi 0,5 razlika logita postaje 1,4, pa je „lep" oko 4 puta verovatniji (jedna reč dominira i tekst je siguran, ali ponavljajući). Pri temperaturi 2 razlika postaje 0,35, pa je „lep" verovatniji samo oko 1,4 puta (raspodela je skoro ravna i tekst je raznovrstan, ali nepredvidiv).

## Kontraprimer
Pri temperaturi koja teži nuli, model uvek bira token sa najvećom verovatnoćom. Tada nema slučajnosti, isto uputstvo uvek daje isti tekst, a uzorkovanje prelazi u pohlepni izbor.

## Napomene
- Uzorkovanje sa temperaturom i dalje je [[Uzorkovanje|uzorkovanje]], samo iz izmenjene raspodele.
- Temperatura ne bira token, nego samo oblikuje raspodelu. Token iz nje bira [[Strategija izbora tokena|strategija izbora tokena]].
