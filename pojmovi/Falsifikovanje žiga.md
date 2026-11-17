---
tip: pojam
aliases: [watermark forgery, spoofing attack, spoofing, lažiranje žiga]
izvor: N. Jovanović, R. Staab, M. Vechev, „Watermark Stealing in Large Language Models", ICML 2024
---
# Falsifikovanje žiga (watermark forgery)

## Definicija
Falsifikovanje žiga je napad u kome napadač pravi primerak koji nije generisao model sa datim [[Ključ žiga|ključem žiga]], a koji [[Detekcija sa žigom|detekcija sa žigom]] ipak proglasi primerkom sa tim žigom.

## Jednostavan primer
Novčanica ima skriven znak koji se otkriva posebnim svetlom. Falsifikator koji nauči da taj znak oponaša i odštampa ga na papiru koji centralna banka nije izdala falsifikovao je žig: provera svetlom proglasi novčanicu pravom, iako nije.

## Primer
Napadač želi da diskredituje jednog dopisnika agencije Vidik. Postavlja jezičkom modelu sa žigom stotine promptova i iz odgovora procenjuje koji su tokeni češći nego što bi bili bez žiga, čime približno rekonstruiše zelene liste. Zatim sam napiše izveštaj sa terena, sa prepoznatljivim rečnikom dopisnika, birajući reči tako da sadrži previše zelenih tokena, i pošalje ga redakciji u ime dopisnika. Provera žiga tekst proglasi generisanim, iako ga model nije napisao, i dopisnik ispada da je izveštaj prepustio jezičkom modelu.

## Kontraprimer
**Agencija Vidik.** Ljudski izveštaj koji slučajno sadrži više zelenih tokena nego što je očekivano, pa ga provera žiga označi kao generisan, nije falsifikovanje žiga, nego [[Lažno pozitivan nalaz|lažno pozitivan nalaz]]: niko nije nameravao da ugradi žig.

**Agencija Vidik.** Napadač koji izveštaj prosto zatraži od jezičkog modela sa žigom nije falsifikovao žig: tekst jeste generisan tim modelom, a žig je pravi.

## Napomene
- Falsifikovanje napada garanciju [[Stopa lažno pozitivnih nalaza|stope lažno pozitivnih nalaza]] koju daje [[P-vrednost|p-vrednost]]: ta garancija važi za sadržaj koji je nastao bez znanja o ključu, a ne za sadržaj koji je napadač namerno oblikovao.
- Napadač ne mora da zna ključ. Jovanović i dr. pokazuju da se pravila žiga mogu dovoljno dobro proceniti iz odgovora modela, uz trošak manji od 50 dolara, i da falsifikovanje tada uspeva u preko 80% pokušaja.
- Falsifikovanje i [[Napad uklanjanjem|napad uklanjanjem]] su suprotni po cilju: uklanjanje pravi lažno negativan nalaz, a falsifikovanje lažno pozitivan.
