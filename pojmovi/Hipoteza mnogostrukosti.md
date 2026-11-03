---
tip: pojam
aliases: [manifold hypothesis, mnogostrukost, manifold]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, odeljak 5.11.3
---
# Hipoteza mnogostrukosti (manifold hypothesis)

## Definicija
Hipoteza mnogostrukosti je pretpostavka da primerci iz [[Raspodela podataka|raspodele podataka]] visoke dimenzije leže blizu podskupa znatno manje dimenzije (mnogostrukosti), pa se mogu opisati sa malo [[Latentna promenljiva|latentnih promenljivih]].

## Jednostavan primer
Raspodela kocke zadaje se sa pet slobodnih brojeva, jer šesti sledi iz uslova da je zbir jedan. Sve kocke iz modela sa parametrom θ ipak leže na jednoj liniji u tom petodimenzionalnom prostoru, pa ih opisuje jedan broj.

## Primer
Fotografija iz arhive agencije Vidik ima stotine hiljada brojeva, ali nasumično izabrane vrednosti piksela skoro nikad ne daju mutnu noćnu fotografiju saobraćajne nesreće. Takve fotografije zauzimaju sićušan deo prostora svih slika iste veličine, pa ih model može opisati sa znatno manje brojeva.

## Napomene
- Mnogostrukost se ovde može shvatiti intuitivno, kao zakrivljena površ manje dimenzije unutar prostora visoke dimenzije.
- Ovo je hipoteza, a ne dokazano svojstvo podataka. Ona objašnjava zašto [[Enkoder|enkoder]] može da sažme sadržaj bez velikog gubitka.
