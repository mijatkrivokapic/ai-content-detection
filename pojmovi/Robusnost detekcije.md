---
tip: pojam
aliases: [detection robustness, robustness, otpornost detekcije]
izvor: J. Kirchenbauer i dr., „On the Reliability of Watermarks for Large Language Models", ICLR 2024; M. Saberi i dr., „Robustness of AI-Image Detectors: Fundamental Limits and Practical Attacks", ICLR 2024
---
# Robusnost detekcije (detection robustness)

## Definicija
Robusnost detekcije je svojstvo [[Detektor|detektora]] da zadrži [[Stopa otkrivanja pri fiksnoj stopi lažno pozitivnih nalaza|stopu otkrivanja pri fiksnoj stopi lažno pozitivnih nalaza]] kada su generisani primerci izmenjeni, slučajno ili [[Napad uklanjanjem|napadom uklanjanjem]] dozvoljenim [[Model pretnje|modelom pretnje]]. Meri se padom te stope otkrivanja posle izmene: što je pad manji, detekcija je robusnija.

## Jednostavan primer
Pravilo „bar 5 šestica u 10 bacanja“ ima stopu lažno pozitivnih nalaza od 1,5% i otkriva plavu kocku u 62% provera. Kada varalica u zapisniku prepravi svaku drugu šesticu, pravilo je otkriva u samo 8% provera. Pad sa 62% na 8% pokazuje da pravilo nije robusno na prepravljanje zapisnika.

## Primer
Detektor fotografija agencije Vidik, pri stopi lažno pozitivnih nalaza od 1%, otkriva 90% fotografija napravljenih modelom slika iz teksta. Kada iste fotografije prođu kroz kompresiju društvene mreže, otkriva 85%, a posle ciljanog napada uklanjanjem, u kome napadač dodaje šum podešen da zbuni detektor, samo 20%. Detektor je robustan na slučajnu kompresiju, ali ne i na ciljani napad. Brojevi su ilustrativni.

## Kontraprimer
**Agencija Vidik.** Detektor koji svaku fotografiju sa tragovima kompresije društvene mreže označi kao generisanu zadržava stopu otkrivanja posle kompresije, ali nije robustan: kompresovane ljudske fotografije sa društvenih mreža takođe označava kao generisane, pa mu stopa lažno pozitivnih nalaza raste. Robusnost zahteva da stopa otkrivanja ostane očuvana pri istoj stopi lažno pozitivnih nalaza.

## Napomene
- Robusnost se uvek navodi u odnosu na vrstu izmena: detektor može biti robustan na kompresiju, a nerobustan na parafraziranje.
- Robusnost na slučajne izmene ne povlači robusnost na napad, jer napadač bira izmenu koja najviše šteti detektoru.
- Kod [[Vodeni žig|vodenog žiga]] u tekstu robusnost raste sa dužinom teksta: duži tekst ima više tokena, pa žig preživljava i kada je deo tokena izmenjen.
