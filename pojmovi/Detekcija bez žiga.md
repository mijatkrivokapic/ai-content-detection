---
tip: pojam
aliases: [watermark-free detection, passive detection, detekcija bez vodenog žiga]
izvor: NIST AI 100-4, Reducing Risks Posed by Synthetic Content, 2024; R. Tang, Y.-N. Chuang, X. Hu, „The Science of Detecting LLM-Generated Text", Communications of the ACM, 2024
---
# Detekcija bez žiga (watermark-free detection)

## Definicija
Detekcija bez žiga je zaključivanje o poreklu sadržaja isključivo iz njegovih svojstava, bez [[Vodeni žig|žiga]] i bez ikakve saradnje generatora.

## Jednostavan primer
Nastavnik koji po stilu „oseća" da esej nije pisao učenik radi detekciju bez žiga: nema potpisa ni pečata, samo procenu na osnovu samog teksta. Takva procena može da bude pogrešna.

## Primer
P-Detektor meri [[Perpleksnost|perpleksnost]] eseja iz ugla Tekst-G i esej označava kao generisan ako je perpleksnost ispod praga, jer tekst koji je Tekst-G sam generisao iz njegovog ugla obično ima nisku perpleksnost: mašinski tekst nastaje biranjem verovatnih tokena.

## Kontraprimer
Student koji sam piše vrlo formalno, sa mnogo ustaljenih izraza, ima tekst sa niskom perpleksnošću. Detektor ga pogrešno označi kao mašinu: to je lažno pozitivan nalaz, odnosno lažna optužba.

## Napomene
- To je statistička procena, a ne provera. Stopa lažno pozitivnih nalaza nije unapred poznata, nego se meri na ljudskom sadržaju.
- Greši češće od provere žiga, posebno nad kratkim sadržajem, nad sadržajem generatora koje detektor nije video i nad ljudskim sadržajem koji liči na generisani.
- Mala izmena sadržaja, na primer parafraziranje, može ukloniti svojstva na koja se oslanja.
