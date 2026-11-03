---
tip: pojam
aliases: [perplexity, PPL]
izvor: D. Jurafsky, J. H. Martin, Speech and Language Processing, 3. izdanje (draft), pogl. 3
---
# Perpleksnost (perplexity)

## Definicija
Perpleksnost niza u odnosu na model je eksponencijalna funkcija prosečne negativne log-[[Verodostojnost|verodostojnosti]] njegovih tokena, pri čemu se verodostojnost svakog tokena računa uz uslov tokena pre njega. Što je perpleksnost niža, model je niz smatrao predvidljivijim.

PPL = exp( −(1/n) · Σ log p(xi | x1, …, xi−1) ), što je isto što i 1 / (proizvod verovatnoća)^(1/n)

## Jednostavan primer
Na kvizu sa ponuđenim odgovorima, ako si kod svakog pitanja bio neodlučan između 4 odgovora, tvoja „perpleksnost" je 4. Perpleksnost 20 znači da je model bio neodlučan kao da u svakom koraku bira ravnomerno između 20 tokena.

## Primer
Koristeći iste korake kao u [[Autoregresivna faktorizacija|autoregresivnoj faktorizaciji]]: „Danas je lep dan." ima korake 10%, 50%, 40% i 60% (proizvod 1,2%), pa je perpleksnost oko 3. Ista četiri tokena u obrnutom redosledu, „Dan lep je danas.", imaju korake 2%, 1%, 5% i 1% (proizvod 0,00001%), pa je perpleksnost oko 56. Model je bio mnogo iznenađeniji. Brojevi su ilustrativni.

## Kontraprimer
Perpleksnost nije svojstvo samog teksta. Zavisi od modela koji je meri: isti tekst jedan model smatra predvidljivim, a drugi iznenađujućim, pa svaki daje drugačiji broj.

## Napomene
- Na niskoj perpleksnosti zasniva se [[Detekcija bez žiga|detekcija bez žiga]] (P-Detektor).
- Perpleksnost se računa iz uslovnih verodostojnosti tokena, onih istih koji nastaju u [[Autoregresivna faktorizacija|autoregresivnoj faktorizaciji]].
- Za razliku od [[Entropija sadržaja|entropije sadržaja]], koja meri slobodu pri pisanju, perpleksnost meri iznenađenje gotovim tekstom.
