---
tip: pojam
aliases: [watermark embedding point, stage of watermark application, faza ugradnje žiga]
izvor: NIST AI 100-4, Reducing Risks Posed by Synthetic Content, 2024, odeljci 3.1.1.1 (stage of application) i 3.1.1.3
---
# Mesto ugradnje žiga (watermark embedding point)

## Definicija
Mesto ugradnje žiga je deo generisanja u koji se ugrađuje [[Vodeni žig|vodeni žig]]: parametri [[Generativni model|generativnog modela]], početni [[Gausov šum|šum]], [[Uzorkovanje|uzorkovanje]] ili gotov izlaz.

## Jednostavan primer
Program koji „baca“ virtuelnu kocku i posle svake trojke češće bira peticu ugrađuje žig pri uzorkovanju. Naknadna prepravka nekih brojeva u već zapisanom zapisniku, po pravilu koje zna samo onaj ko ga prepravlja, ugradnja je u gotov izlaz.

## Primer
Jezički model naloga „očevidac“ ugrađuje žig pri uzorkovanju: pre izbora svakog tokena pomera verovatnoće ka tokenima sa zelene liste. Model slika iz teksta ugrađuje žig u početni šum: iz šuma u koji je ugrađen obrazac nastaje fotografija poplave, a obrazac se kasnije može otkriti samo uz pristup modelu i [[Ključ žiga|ključu]].

## Kontraprimer
**Kocka.** Napomena „generisano programom“ zapisana iznad zapisnika nije ugradnja žiga, jer nije u samim brojevima.

**Agencija Vidik.** Metapodatak „napravljeno modelom slika iz teksta“ u fajlu fotografije nije ugradnja žiga, jer nije u samom sadržaju i može se obrisati bez promene slike.

## Napomene
- Ugradnja u parametre znači da je model treniran tako da svaki njegov izlaz nosi žig; ugradnja u početni šum i pri uzorkovanju dešava se tokom generisanja, a ugradnja u gotov izlaz posle njega.
- Ugradnja u gotov izlaz može se primeniti i na ljudski sadržaj, pa žig ugrađen na tom mestu ne dokazuje da je sadržaj generisan.
- Mesto ugradnje određuje ko može da ukloni žig: žig koji se ugrađuje u kodu za uzorkovanje, van parametara modela, može ukloniti svako ko ima model i taj kod, bez ponovnog treniranja.
