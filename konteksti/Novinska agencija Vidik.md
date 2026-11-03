---
tip: kontekst
uloga: primarni
---
# Novinska agencija Vidik

Vidik je izmišljena novinska agencija koja prikuplja fotografije, video snimke, audio zapise i tekstove od dopisnika, građana i sa društvenih mreža, proverava ih i objavljuje na svom portalu i prosleđuje medijima pretplatnicima. Pogodna je za ilustraciju teme jer prima sadržaj svih modaliteta iz izvora različite pouzdanosti, a objava generisanog sadržaja kao autentičnog direktno šteti njenom ugledu.

## Elementi

### Ljudi i uloge
- **Redakcija**: urednici i novinari koji odlučuju o objavi.
- **Dopisnici**: saradnici na terenu koji šalju materijal.
- **Građani očevici**: spoljni pošiljaoci materijala, identifikovani samo nalogom.
- **Nalog „očevidac“**: lažni nalog na prijemnom portalu, sa generisanom profilnom fotografijom; šalje redakciji snimak navodnog incidenta i opis događaja generisan jezičkim modelom, kao i fotografiju navodne poplave u centru Kraljeva generisanu iz prompta.

### Modeli kojima se služi nalog „očevidac“
- **Jezički model**: piše opis događaja; eksplicitni model sa rečnikom od oko 100 000 tokena.
- **Model lica (StyleGAN)**: pravi profilnu fotografiju; treniran na skupu FFHQ (oko 70 000 portreta sa Flickra). Fotografiju pravi iz vektora od 512 brojeva uzorkovanih iz standardne normalne raspodele; implicitni model.
- **Model slika iz teksta**: pravi fotografiju poplave iz prompta; radi u latentnom prostoru, sa enkoderom i dekoderom koji prevode između piksela i latentnog prostora.

### Sistemi
- **Prijemni portal**: aplikacija preko koje dopisnici i građani šalju materijal redakciji; pošiljalac ima nalog sa imenom i profilnom fotografijom.
- **Filter neželjene pošte**: klasifikator koji ocenjuje da li je poruka pristigla u redakciju neželjena.

### Podaci
- **Izveštaji dopisnika**: tekstovi koje dopisnici pišu sa terena, najčešće o saobraćajnim nesrećama na putevima i nevremenu; imaju prepoznatljiv rečnik (npr. „u krivini“).
- **Arhiva primljenih fotografija**: oko 40 000 fotografija koje su građani poslali preko prijemnog portala; pretežno noćni i mutni snimci telefonom sa mesta saobraćajnih nesreća i nevremena.

### Procesi
- **Prijem i provera materijala**: materijal pristigao preko prijemnog portala proverava se pre objave.
