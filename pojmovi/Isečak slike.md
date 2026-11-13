---
tip: pojam
aliases: [patch, image patch, isečak, deo slike]
izvor: A. Dosovitskiy i dr., „An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale“, ICLR 2021
---
# Isečak slike (patch)

## Definicija
Isečak slike je povezan pravougaoni deo slike fiksne veličine (kod videa, deo koji obuhvata i nekoliko uzastopnih kadrova), koji se uzima kao jedan element niza kojim se slika ili video predstavljaju modelu. Niz isečaka ima za sliku istu ulogu koju niz [[Token|tokena]] ima za tekst: model ga obrađuje element po element. Isečak ipak nije token.

## Jednostavan primer
Fotografija kocke za igru veličine 64×64 piksela deli se na 16 isečaka veličine 16×16, raspoređenih u mrežu 4×4. Svaki isečak ima 16 · 16 · 3 = 768 brojeva (tri za svaki piksel). Umesto 4 096 piksela model dobija niz od 16 elemenata i zna koje mesto u slici svaki od njih zauzima.

## Primer
Fotografija lica od 1024×1024 piksela koju pravi Lica-G deli se na 64 · 64 = 4 096 isečaka veličine 16×16, svaki sa 768 brojeva. Snimak od 16 kadrova iste veličine, sa isečcima koji obuhvataju po dva kadra (16×16×2), ima 8 · 4 096 = 32 768 isečaka.

## Kontraprimer
**Kocka.** Pikseli fotografije kocke izabrani nasumično, na primer 256 od njih, nisu isečak: isečak je povezan deo slike.

**Opšti slučaj.** Verzija fotografije lica smanjena na 256×256 piksela nije isečak: obuhvata ceo sadržaj slike, a ne njen deo.

## Napomene
- Isečak nije token: njegove vrednosti su brojevi koji mogu biti proizvoljni, a ne izbor iz konačnog rečnika (videti [[Token]]). Slika se može pretvoriti i u tokene iz konačnog rečnika; tada su elementi niza tokeni, a ne isečci.
- Vektor koji model pravi od isečka nije [[Ugrađivanje|ugrađivanje]] u smislu te beleške, jer isečak nije diskretan element.
- Izbor veličine isečka određuje koliko elemenata model obrađuje: manji isečci daju duži niz.
- Prevod „isečak“ nije ustaljen; alternative su „deo slike“ i „blok slike“. „Zakrpa“ se izbegava jer u softverskom inženjerstvu znači bezbednosni patch.
