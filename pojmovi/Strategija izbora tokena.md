---
tip: pojam
aliases: [decoding strategy, strategija izbora, strategija uzorkovanja]
izvor: A. Holtzman i dr., „The Curious Case of Neural Text Degeneration", ICLR 2020
---
# Strategija izbora tokena (decoding strategy)

## Definicija
Strategija izbora tokena je pravilo po kome se iz raspodele nad rečnikom bira sledeći [[Token|token]]. Pohlepni izbor uzima najverovatniji token. Top-k uzorkovanje uzorkuje samo iz k najverovatnijih tokena, a top-p uzorkovanje iz najmanjeg skupa najverovatnijih tokena čija ukupna verovatnoća dostiže p.

## Jednostavan primer
Birate film za gledanje. Pohlepno: uvek uzmete najbolje ocenjen. Top-k: nasumično birate među tri najbolje ocenjena. Top-p: nasumično birate među najbolje ocenjenim filmovima koji zajedno čine 90% svih glasova, a one sa vrlo malo glasova preskačete.

## Primer
Verovatnoće tokena posle „Danas je": lep 40%, petak 20%, dan 15%, kiša 12%, nebo 8%, ljubičasto 5%. Pohlepno Tekst-G uvek bira „lep". Top-k sa k = 3 bira slučajno među „lep", „petak" i „dan". Top-p sa p = 0,9 bira slučajno među prvih pet tokena, čiji zbir verovatnoća iznosi 95%, dok „ljubičasto" otpada.

## Kontraprimer
[[Temperatura]] nije strategija izbora tokena. Temperatura menja oblik raspodele, a strategija iz tako dobijene raspodele bira token. To su dva odvojena koraka istog procesa.

## Napomene
- Engleski termin „decoding strategy" ovde se ne prevodi kao „strategija dekodiranja", da se ne bi mešao sa pojmom [[Dekoder|dekoder]].
- Strategija i temperatura se obično koriste zajedno: prva bira token, druga oblikuje raspodelu iz koje se bira.
- Top-k i top-p unose slučajnost ([[Uzorkovanje]]), ali odsecaju najneverovatnije tokene da tekst ne bi izgubio smisao. Pohlepni izbor nije uzorkovanje, jer nema slučajnosti.
