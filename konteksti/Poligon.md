---
tip: kontekst
uloga: sekundarni
---
# Poligon

Izmišljeno okruženje sa nekoliko generativnih modela i detektora. Služi za primere u kojima je korisno imenovati konkretan model ili detektor, posebno kod generisanja teksta i detekcije. Preuzeto iz Pojmovnika (odeljak „Poligon za detekciju“) i korišćeno u beleškama iz prezentacije 3, runda 1. Glavni primer svakog pojma i dalje je iz konteksta [[Novinska agencija Vidik]].

## Elementi

### Generativni modeli
- **Tekst-G**: jezički model koji iz prompta piše tekstove na srpskom; rečnik od oko 100 000 tokena.
- **Slika-G**: model koji iz tekstualnog opisa pravi slike od 512×512 piksela, preko latentnog prostora oblika 64×64×4.
- **Lica-G**: model koji iz vektora od 512 brojeva pravi fotografije lica nepostojećih osoba, veličine 1024×1024 piksela.
- **Glas-G**: model koji iz teksta sintetiše govor, 16 000 uzoraka u sekundi.
- **Graf-G**: model koji generiše grafove društvene mreže (čvor je nalog, ivica je praćenje).
- **Oblik-G**: model koji iz tekstualnog opisa pravi 3D modele predmeta, kao mrežu poligona.

### Podaci
- **Korpus eseja**: studentski eseji na srpskom napisani pre pojave javno dostupnih jezičkih modela.
- **Foto-arhiva**: fotografije lica i scena snimljene fotoaparatom.

### Detektori
- **D-Klasifikator**: klasifikator koji za sliku kaže da li je ljudska ili generisana.
- **P-Detektor**: detektor koji tekst označava kao generisan kada mu je perpleksnost iz ugla Tekst-G niska.
- **Ž-Provera**: postupak koji tajnim ključem proverava da li tekst ili slika nose žig koji Tekst-G i Slika-G ugrađuju u svoj izlaz.
