---
tip: pojam
aliases: [generator artifact, generator fingerprint, trag generisanja, otisak generatora]
izvor: Nema ustaljene definicije; videti, na primer, J. Frank i dr., „Leveraging Frequency Analysis for Deep Fake Image Recognition“, ICML 2020, i R. Durall, M. Keuper, J. Keuper, „Watch your Up-Convolution“, CVPR 2020 (izvori nisu proveravani)
---
# Trag generatora (generator artifact)

## Definicija
Trag generatora je svojstvo samog sadržaja nekog primerka koje potiče od [[Generativni model|generativnog modela]] koji ga je proizveo, odnosno od razlike između [[Raspodela modela|raspodele modela]] i [[Raspodela podataka|raspodele podataka]] ili od samog postupka generisanja, i koje primerci iz raspodele podataka nemaju ili imaju znatno ređe.

## Jednostavan primer
Aparat za bacanje kocke nepravilnog oblika zbog mehaničke mane nikad ne baca isti broj dva puta zaredom. Nijedan pojedinačni ishod to ne odaje, ali u zapisniku od 600 bacanja prava kocka ponavlja prethodni broj oko 100 puta (u šestini slučajeva), a aparat nijednom. Ta razlika potiče od mehanizma koji pravi ishode, a ne od samih brojeva, pa je trag aparata.

## Primer
Fotografija koju pravi Lica-G može nositi dva traga. Jedan je vidljiv: različite minđuše na levom i desnom uhu. Drugi se ne vidi golim okom: neki generatori sliku grade povećavanjem rezolucije i pritom prave pravilno ponavljanje, koje se u [[Frekvencijski domen|frekvencijskom domenu]] pokazuje kao izdvojeni vrhovi na visokim frekvencijama, kakve snimci fotoaparatom nemaju. Oba traga potiču od modela, a ne od lica osobe na fotografiji.

## Kontraprimer
**Opšti slučaj.** Metapodatak u slici koji beleži alat kojim je napravljena nije trag generatora: nije svojstvo samog sadržaja i može se obrisati bez promene slike. Žig koji generator ugrađuje u svoj izlaz takođe nije trag generatora, iako ga generator ostavlja: ugrađuje se namerno, zadat je tajnim ključem i proverava se ključem ([[Vodeni žig]]), dok trag nastaje nenamerno i može se uočiti bez ključa.

## Napomene
- Trag je uvek trag u odnosu na raspodelu podataka: svojstvo koje razlikuje fotografije Lica-G od fotografija lica iz Foto-arhive ne mora da ih razlikuje od snimaka lica nekim drugim fotoaparatom.
- Tragovi zavise od generatora: novi modeli mogu ukloniti poznate tragove, pa se tragovi jednog generatora često ne prenose na drugi.
- Smanjenje fotografije i kompresija mogu uništiti tragove u visokim frekvencijama, što je čest slučaj sa sadržajem sa društvenih mreža.
- Kod teksta trag je statistički, na primer niska [[Perpleksnost|perpleksnost]] iz ugla modela. Gde model nema slobode izbora, nema ni traga ([[Entropija sadržaja]]).
- [[Detekcija bez žiga]] zasniva se na tragovima. Prisustvo traga ne dokazuje poreklo, jer ljudski sadržaj može imati isto svojstvo, a odsustvo traga ne dokazuje da je sadržaj ljudski.
- „Generator“ je ovde generativni model u celini, a ne deo [[Generativna suparnička mreža|GAN-a]].
