---
tip: pojam
aliases: [spectrogram, vremensko-frekvencijski prikaz, STFT spektrogram]
izvor: A. V. Oppenheim, R. W. Schafer, Discrete-Time Signal Processing, 3. izdanje, Pearson, 2010 (kratkotrajna Furijeova transformacija)
---
# Spektrogram (spectrogram)

## Definicija
Spektrogram je [[Reprezentacija medija|reprezentacija]] signala, najčešće zvuka, u obliku dvodimenzionalne tabele u kojoj je jedna osa vreme, druga frekvencija, a vrednost u svakom polju pokazuje koliko je ta frekvencija zastupljena u kratkom delu signala oko tog trenutka. Dobija se tako što se signal podeli na kratke uzastopne prozore, a za svaki prozor izračuna [[Frekvencijski domen|frekvencijski prikaz]].

## Jednostavan primer
Snimak bacanja kocke: kocka tri puta udari o sto. Na spektrogramu se vide tri uska vertikalna traga, svaki raširen preko mnogo frekvencija, jer je udar kratak i obuhvata sve frekvencije odjednom. Između udara je tišina, pa su polja tamna.

## Primer
Jedna sekunda govora koji sintetiše Glas-G ima 16 000 odbiraka. Ako se uzimaju prozori od 25 ms sa korakom od 10 ms, spektrogram ima oko 100 vremenskih koraka sa po 201 frekvencijskom vrednošću, dakle oko 100 × 201 brojeva. Tako se zvuk predstavlja kao slika, na koju se mogu primeniti isti postupci kao na slike.

## Kontraprimer
**Kocka.** Frekvencijski prikaz celog snimka bacanja kocke, izračunat odjednom, nije spektrogram: nema vremensku osu, pa se ne vidi kada je koji udar nastao.

**Opšti slučaj.** Niz od 16 000 brojeva u sekundi koji daje generativni model govora je talasni oblik signala, a ne spektrogram: nema frekvencijsku osu.

## Napomene
- Dužina prozora je kompromis: duži prozor daje precizniju frekvenciju, a kraći precizniji trenutak.
- Spektrogram obično čuva samo jačinu frekvencija, a ne i fazu, pa se iz njega zvuk ne može tačno vratiti bez procene faze.
- Isti zvuk može imati više reprezentacija (niz vrednosti signala ili spektrogram), a izbor određuje gde se traže [[Trag generatora|tragovi generatora]], kako kaže beleška [[Reprezentacija medija]].
