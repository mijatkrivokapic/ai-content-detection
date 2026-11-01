---
tip: pojam
aliases: [Kullback–Leibler divergence, Kulbek-Lajblerova divergencija, relativna entropija, relative entropy]
izvor: T. M. Cover, J. A. Thomas, Elements of Information Theory, 2. izdanje, Wiley, 2006, odeljak 2.3
---
# KL divergencija (Kullback–Leibler divergence)

## Definicija
KL divergencija KL(P‖Q) meri koliko manju verovatnoću raspodela Q, u proseku i na logaritamskoj skali, dodeljuje primercima koji potiču iz raspodele P nego što im dodeljuje sama P. Izračunava se kao očekivana vrednost logaritma količnika P(x)/Q(x), gde je x primerak [[Uzorkovanje|uzorkovan]] iz P. Kod neprekidnih vrednosti umesto verovatnoća koriste se gustine.

## Jednostavan primer
P je raspodela poštene kocke, a Q raspodela nameštene kocke, koja šesticu daje sa verovatnoćom 1/2, a svaki od ostalih brojeva sa 1/10.

| Ishod | P(x) | Q(x) | P(x)/Q(x) | ln(P(x)/Q(x)) |
|---|---|---|---|---|
| 1–5 (svaki) | 1/6 | 1/10 | 1,67 | 0,51 |
| 6 | 1/6 | 1/2 | 0,33 | −1,10 |

KL(P‖Q) je prosek poslednje kolone po bacanjima poštene kocke: 5/6 · 0,51 + 1/6 · (−1,10) ≈ 0,24. Nameštena kocka šestici daje veću verovatnoću nego poštena, ali ostalim brojevima manju, pa je u proseku lošiji opis: kako je e^0,24 ≈ 1,27, ona bacanjima poštene kocke dodeljuje u proseku oko 1,3 puta manju verovatnoću. Obrnuto, KL(Q‖P) ≈ 0,29; vrednosti se razlikuju jer se u prvom slučaju bacanja posmatraju iz P, a u drugom iz Q.

## Primer
Posle reči „Nesreća se dogodila u“ sledeća reč u izveštajima dopisnika agencije Vidik ima raspodelu P, a jezički model naloga „očevidac“ raspodelu Q:

| | centru | noći | Kraljevu | krivini | ostalo |
|---|---|---|---|---|---|
| P (dopisnici) | 0,20 | 0,30 | 0,10 | 0,30 | 0,10 |
| Q (model) | 0,40 | 0,25 | 0,10 | 0,004 | 0,246 |

KL(P‖Q) ≈ 1,12, a KL(Q‖P) ≈ 0,44 (prirodni logaritam). Kako je e^1,12 ≈ 3,1, model rečima dopisnika u proseku dodeljuje oko 3 puta manju verovatnoću nego što im dodeljuje njihova stvarna raspodela. Razlika potiče najviše od reči „krivini“, koju dopisnici često koriste jer izveštavaju o nesrećama na putu, a kojoj model daje gotovo nultu verovatnoću. KL(P‖Q) posmatra primerke iz P, pa „krivinu“ vidi često i za nju strogo kažnjava Q. KL(Q‖P) posmatra primerke iz Q, u kojima se „krivina“ skoro ne javlja, pa taj propust gotovo ne primećuje.

## Napomene
- Formula: KL(P‖Q) = Σₓ P(x) · log(P(x)/Q(x)). Kod neprekidnih vrednosti zbir postaje integral, a verovatnoće gustine.
- Vrednost e^KL je geometrijski, a ne aritmetički prosek količnika P(x)/Q(x) po primercima iz P; zato tumačenje „Q daje u proseku toliko puta manju verovatnoću“ važi u geometrijskom smislu.
- KL divergencija je uvek nenegativna i jednaka je nuli samo kada su P i Q iste raspodele. U opštem slučaju KL(P‖Q) ≠ KL(Q‖P), pa nije udaljenost u matematičkom smislu.
- Ako Q dodeljuje verovatnoću nula primerku koji pod P ima pozitivnu verovatnoću, KL(P‖Q) je beskonačna.
- KL(P‖Q) određuje i koliko se lako primerci iz P razlikuju od primeraka iz Q: što je veća, to je potrebno manje primeraka da bi se pouzdano zaključilo da potiču iz P, a ne iz Q (Černof-Štajnova lema; Cover i Thomas, odeljak 11.8). Za detekciju to znači da je generisani sadržaj teže razlikovati od ljudskog što je raspodela modela bliža raspodeli ljudskog sadržaja.
- [[Metoda maksimalne verodostojnosti]] ekvivalentna je minimizaciji KL([[Raspodela podataka|raspodela podataka]] ‖ [[Raspodela modela|raspodela modela]]), procenjene na trening skupu.