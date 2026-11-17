---
tip: pojam
aliases: [VAE, variational autoencoder, autoenkoder]
izvor: D. P. Kingma, M. Welling, „Auto-Encoding Variational Bayes“, ICLR 2014
---
# Varijacioni autoenkoder (variational autoencoder, VAE)

## Definicija
Varijacioni autoenkoder je [[Eksplicitni generativni model|eksplicitni generativni model]] koji se sastoji od [[Enkoder|enkodera]] i [[Dekoder|dekodera]], treniranih zajedno tako da dekoder tačku [[Latentni prostor|latentnog prostora]] preslikava u primerak, a enkoder za primerak zadaje raspodelu [[Latentna promenljiva|latentne promenljive]] (njenu sredinu i rasipanje) koja se drži bliskom [[Apriorna raspodela|apriornoj raspodeli]]. Novi primerci dobijaju se [[Uzorkovanje|uzorkovanjem]] tačke iz apriorne raspodele i njenim dekodiranjem.

## Jednostavan primer
U džepu su crvena poštena i plava nameštena kocka, a apriorna raspodela boje je 1/2 : 1/2. Dekoder je pravilo „iz boje u ishode“: crvena daje šesticu u šestini bacanja, plava u polovini. Beleži se samo da li je pala šestica. Enkoder za zapisnik od 10 bacanja sa 5 šestica ne kaže „plava“, nego zadaje raspodelu boje: plava oko 0,95, crvena oko 0,05. Za generisanje se boja izvuče iz apriorne raspodele i dekoduje u zapisnik. U ovom primeru enkoder tu raspodelu računa tačno, Bajesovim pravilom; kod VAE je aproksimira neuronska mreža.

## Primer
Slika-G ima autoenkoder koji prevodi između piksela i latentnog prostora, a takav autoenkoder je obično varijacioni. Za sliku od 512×512 piksela (786 432 broja) enkoder daje sredinu i rasipanje za latentni prostor oblika 64×64×4 (16 384 broja), tačka se dobija kao z = μ + σ · ε, a dekoder je vraća u sliku. Latentni prostor ima 48 puta manje brojeva od slike. Zahvaljujući apriornoj raspodeli bliskoj standardnoj normalnoj, i tačka uzorkovana iz šuma daje upotrebljivu sliku.

## Kontraprimer
**Opšti slučaj.** Enkoder i dekoder koji fotografiju sažimaju i vraćaju ([[Rekonstrukcija|rekonstrukcija]]) čine običan autoenkoder, a ne varijacioni, ako enkoder daje jednu tačku i nema apriorne raspodele: nasumična tačka latentnog prostora tada može dati besmislenu sliku, pa se iz takvog modela ne mogu uzorkovati novi primerci.

## Napomene
- Treniranje maksimizuje donju granicu [[Verodostojnost|verodostojnosti]] koja ima dva člana: tačnost rekonstrukcije i [[KL divergencija|KL divergenciju]] između raspodele koju daje enkoder i apriorne raspodele. Zato je VAE eksplicitan, ali donja granica može biti znatno manja od stvarne verodostojnosti (videti [[Eksplicitni generativni model]]).
- Enkoder daje sredinu μ i rasipanje σ, a konkretna tačka nastaje dodavanjem [[Gausov šum|Gausovog šuma]] ε (videti [[Latentna promenljiva]]).
- Slike iz VAE su često mutnije od slika iz GAN-a.
