---
tip: pojam
aliases: [frequency domain, spektralni domen, spektar]
izvor: A. V. Oppenheim, R. W. Schafer, Discrete-Time Signal Processing, 3. izdanje, Pearson, 2010
---
# Frekvencijski domen (frequency domain)

## Definicija
Frekvencijski domen je prikaz signala (niza vrednosti koje se menjaju u vremenu ili u prostoru, kao što su zvuk ili slika) u obliku zbira komponenti različitih frekvencija, u kome se za svaku frekvenciju zadaje koliko je zastupljena u signalu (amplituda) i kako je pomerena (faza). Dobija se Furijeovom transformacijom iz vremenskog domena, a kod slike iz prostornog.

## Jednostavan primer
Kocka se baca u pravilnom ritmu i zapisnik je „6,1,6,1,6,1,…“. U vremenskom domenu to je niz brojeva. U frekvencijskom domenu ima samo dve komponente: prosek 3,5 i jednu izraženu frekvenciju, jedno ponavljanje na dva bacanja, jer se vrednost tačno menja kao 3,5 + 2,5 · (−1)ⁿ. Zapisnik bacanja poštene kocke nema nijednu izraženu frekvenciju: njegov spektar je približno ravan.

## Primer
Snimak od jedne sekunde govora koji sintetiše Glas-G je 16 000 brojeva u vremenskom domenu. Frekvencijski prikaz istog snimka ima komponente od 0 do 8 000 Hz, jer pri 16 000 odbiraka u sekundi veće frekvencije ne mogu da se predstave.

## Kontraprimer
**Kocka.** Koliko je puta pala koja strana kocke (učestalost, histogram ishoda) nije frekvencijski domen, iako se u statistici zove „frekvencija“. Frekvencija ovde znači koliko se puta u jedinici vremena ili prostora nešto ponavlja.

## Napomene
- Kod slike frekvencije su prostorne: glatke površine daju niske frekvencije, a oštre ivice i sitne teksture visoke.
- Frekvencijski domen ne menja sadržaj, nego samo način na koji se prikazuje. Neka svojstva koja se u vremenskom ili prostornom domenu teško vide, na primer pravilno ponavljanje, u njemu postaju vidljiva. Zato se u njemu često traže [[Trag generatora|tragovi generatora]].
- [[Spektrogram]] je frekvencijski prikaz koji se menja u vremenu.
