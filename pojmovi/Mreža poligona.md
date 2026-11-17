---
tip: pojam
aliases: [polygon mesh, mesh, mreža, trouglasta mreža]
izvor: M. Botsch, L. Kobbelt, M. Pauly, P. Alliez, B. Lévy, Polygon Mesh Processing, A K Peters/CRC Press, 2010 (oznaka odeljka nije proverena)
---
# Mreža poligona (polygon mesh)

## Definicija
Mreža poligona je [[Reprezentacija medija|reprezentacija]] trodimenzionalnog predmeta preko njegove površine: skup temena (tačaka u prostoru zadatih koordinatama) i poligona, najčešće trouglova, od kojih svaki spaja nekoliko temena, tako da zajedno prekrivaju površinu predmeta. Za razliku od [[Oblak tačaka|oblaka tačaka]], mreža zadaje i to koja temena su povezana.

## Jednostavan primer
Kocka za igru kao mreža ima 8 temena (uglovi), 12 ivica i 6 poligona (kvadrati, po jedan za svaku stranu). Svaki kvadrat se može podeliti na dva trougla, pa ista kocka ima 12 trouglova. Ako se zadaju samo 8 temena bez poligona, ne zna se da li je to kocka ili neki drugi oblik sa istim uglovima.

## Primer
Oblik-G iz opisa „stolica“ pravi mrežu sa, na primer, 5 000 temena i 10 000 trouglova. Mreža se zapisuje kao dve tabele: tabela temena (5 000 redova sa po tri broja x, y, z) i tabela trouglova (10 000 redova sa po tri rednih broja temena koja trougao spaja). Ista stolica može imati više mreža, na primer jednu sa 10 000 i jednu sa 40 000 trouglova, sa grubljom ili finijom površinom.

## Kontraprimer
**Kocka.** Osam tačaka koje leže u uglovima kocke za igru nisu mreža poligona: nema poligona, pa nema ni površine.

**Opšti slučaj.** 2048 tačaka uzorkovanih sa površine stolice koju je napravio generativni model nisu mreža poligona, iako leže na njenoj površini: to je [[Oblak tačaka|oblak tačaka]], bez zapisa o povezanosti.

## Napomene
- Mreža nije mreža piksela: broj temena i trouglova nije fiksan, a temena nemaju pravilan raspored. Model koji pravi mrežu mora da odredi i koordinate i povezanost, što je teže nego da popuni tabelu fiksne veličine.
- Pošto zadaje površinu, mreža se može direktno prikazati iz bilo kog ugla; oblak tačaka za to traži dodatni korak.
- Mreže koje pravi model mogu imati nepravilnosti, na primer rupe ili trouglove koji se seku, a takva svojstva mogu biti [[Trag generatora|tragovi generatora]].
