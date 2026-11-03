---
tip: pojam
aliases: [watermark, vodeni žig u tekstu]
izvor: J. Kirchenbauer i dr., „A Watermark for Large Language Models", ICML 2023; NIST AI 100-4, 2024
---
# Vodeni žig (watermark)

## Definicija
Vodeni žig je skriveni signal ugrađen u sam sadržaj, pri generisanju ili posle njega, koji nosi informaciju o poreklu sadržaja i čije se prisustvo proverava tajnim ključem.

## Jednostavan primer
Novčanica ima skriven znak koji se ne vidi golim okom, ali se otkriva uz posebno svetlo. Vodeni žig u tekstu je takav skriven obrazac, a ključ je „svetlo" kojim se proverava.

## Primer
Tekst-G ugrađuje žig pri [[Uzorkovanje|uzorkovanju]]. Pre izbora svakog tokena tajni ključ i prethodni token pseudoslučajno određuju zelenu listu, četvrtinu rečnika, a [[Logit|logitima]] tokena sa zelene liste dodaje se ista mala vrednost. U običnom tekstu otprilike svaki četvrti token je zelen, a esej sa žigom sadrži znatno više zelenih tokena nego što bi slučajno imao. Taj obrazac vidi samo onaj ko ima ključ: prebroji zelene tokene i statistički proveri da ih je previše za slučajnost.

## Kontraprimer
Kada model nema izbora (posle `return a +` skoro sigurno sledi „b"), nema šta da se pomeri, pa žig ne može da se ugradi. Takođe, odsustvo žiga ne dokazuje da je tekst napisao čovek.

## Napomene
- Žig nije vidljiv vodeni znak (na primer logo preko slike) i nije metapodatak: ugrađen je u sam sadržaj.
- Žig u uzorkovanju zavisi od [[Entropija sadržaja|entropije sadržaja]], jer pomera izbore koje model ima.
- Odsustvo žiga ne dokazuje da je sadržaj ljudski, jer žig ne nose ni sadržaj drugih generatora ni sadržaj iz kog je žig uklonjen.
- Za razliku od [[Detekcija bez žiga|detekcije bez žiga]], provera žiga zahteva saradnju generatora i tajni ključ, ali ima unapred kontrolisanu stopu lažno pozitivnih nalaza.
