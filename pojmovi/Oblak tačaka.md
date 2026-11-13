---
tip: pojam
aliases: [point cloud, skup tačaka]
izvor: C. R. Qi, H. Su, K. Mo, L. J. Guibas, „PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation“, CVPR 2017
---
# Oblak tačaka (point cloud)

## Definicija
Oblak tačaka je [[Reprezentacija medija|reprezentacija]] trodimenzionalnog predmeta ili scene kao neuređenog skupa tačaka u prostoru, od kojih je svaka zadata koordinatama (po potrebi i dodatnim osobinama, na primer bojom), bez zapisa o tome kako su tačke povezane.

## Jednostavan primer
Na površini kocke za igru nasumično se izabere 2 048 tačaka. Dobijeni oblak ne kaže koje tačke pripadaju istoj strani, osim što se to može zaključiti iz njihovog položaja. Ako se tačke ispišu drugim redosledom, to je isti oblak.

## Primer
Iz mreže koju pravi Oblik-G uzorkuje se 2 048 tačaka sa površine stolice. Rezultat je tabela od 2 048 redova sa po tri broja (x, y, z). Redosled redova nema značenja, a drugi uzorak istih 2 048 tačaka daje nešto drugačiji oblak iste stolice.

## Kontraprimer
**Kocka.** Šest tačkica na gornjoj strani kocke za igru nisu oblak tačaka predmeta: to je šara na njenoj površini.

**Opšti slučaj.** [[Mreža poligona|Mreža poligona]] koju pravi generativni model nije oblak tačaka, iako su njena temena skup tačaka: mreža zadaje i povezanost.

## Napomene
- Broj tačaka nije fiksan i redosled ne postoji, pa se oblak ne može tretirati kao mreža piksela.
- Tačka oblaka nije piksel: piksel ima fiksno mesto u mreži slike, a tačka samo koordinate.
- Oblak ne zadaje površinu, pa je za prikaz iz izabranog ugla potreban dodatni korak.
