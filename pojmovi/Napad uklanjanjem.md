---
tip: pojam
aliases: [removal attack, scrubbing attack, evasion attack, napad izbegavanjem]
izvor: K. Krishna i dr., „Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense", NeurIPS 2023; N. Jovanović, R. Staab, M. Vechev, „Watermark Stealing in Large Language Models", ICML 2024
---
# Napad uklanjanjem (removal attack)

## Definicija
Napad uklanjanjem je namerna izmena [[Generisani sadržaj|generisanog]] primerka koja zadržava njegov smisao, a uklanja ili slabi signal na koji se [[Detektor|detektor]] oslanja, [[Vodeni žig|vodeni žig]] ili [[Trag generatora|trag generatora]], tako da detektor primerak više ne označi kao generisan. Šta napadač sme i može da izmeni određuje [[Model pretnje|model pretnje]].

## Jednostavan primer
Varalica u zapisniku bacanja plave kocke prepravi svaku drugu šesticu u neki drugi broj. U prepravljenom zapisniku šestica se javlja u oko četvrtini bacanja umesto u polovini, pa pravilo „bar 4 šestice u 10 bacanja“ plavu kocku otkriva u oko 22% provera umesto u 83%.

## Primer
Nalog „očevidac“ pre slanja agenciji Vidik provuče opis događaja kroz drugi jezički model koji ga parafrazira: smisao ostaje isti, ali su tokeni drugačiji, pa nestaje i niska [[Perpleksnost|perpleksnost]] i obrazac zelenih tokena. Fotografiju poplave smanji, blago iseče i ponovo kompresuje, čime oslabi tragove generatora u pikselima. Detektor koji agencija koristi oba primerka označi kao ljudska.

## Kontraprimer
**Agencija Vidik.** Kada redakcija sama smanji i kompresuje fotografiju za portal, tragovi generatora mogu da oslabe, ali to nije napad uklanjanjem: izmena nije napravljena da bi se izbegao detektor. Takve slučajne izmene ipak utiču na [[Robusnost detekcije|robusnost detekcije]].

**Agencija Vidik.** Napadač koji opis događaja sam napiše nije izveo napad uklanjanjem, jer primerak nikad nije bio generisan i nema šta da se ukloni.

## Sekundarni primeri
**Poligon.** Govor koji je napravio Glas-G pusti se preko zvučnika i ponovo snimi mikrofonom; promene u [[Spektrogram|spektrogramu]] mogu da oslabe žig ugrađen u zvuk. 3D model koji je napravio Oblik-G pojednostavi se tako da [[Mreža poligona|mreža poligona]] ima upola manje poligona; žig ugrađen u položaje temena time može da nestane.

## Napomene
- U ovoj bazi pojam obuhvata i uklanjanje žiga i izbegavanje detekcije bez žiga. U literaturi se za uklanjanje žiga koristi i termin scrubbing, a za izbegavanje naučenog detektora evasion.
- Parafraziranje je najpoznatiji napad uklanjanjem na tekst: Krishna i dr. pokazuju da parafraziranje spušta stopu otkrivanja detektora DetectGPT sa 70,3% na 4,6%, pri stopi lažno pozitivnih nalaza od 1%.
- Napad je uspešan samo ako izmenjeni primerak napadaču i dalje služi: parafraza koja menja smisao opisa događaja nije korisna nalogu „očevidac“.
