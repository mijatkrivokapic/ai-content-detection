<!-- Pojmovi iz prezentacije 3 (sekvencijalno generisanje, kontrola i detekcija). Svaki blok ispod je zasebna beleška. -->

---
tip: pojam
aliases: [large language model, LLM, jezički model]
izvor: A. Vaswani i dr., „Attention Is All You Need", NeurIPS 2017; T. Brown i dr., „Language Models are Few-Shot Learners", NeurIPS 2020
---
# Veliki jezički model (large language model, LLM)

## Definicija
Veliki jezički model je [[Eksplicitni generativni model|eksplicitni generativni model]] nad nizovima [[Token|tokena]], najčešće autoregresivni transformer, koji uslovne verovatnoće iz [[Autoregresivna faktorizacija|autoregresivne faktorizacije]] računa neuronskom mrežom sa velikim brojem parametara, treniranom na velikom skupu tekstova.

## Jednostavan primer
Predlog sledeće reči na telefonu radi na istom principu: na osnovu onoga što je već napisano nudi reč koja najverovatnije sledi. Veliki jezički model je tako nešto, samo mnogo moćnije, pa tako može da napiše ceo esej.

## Primer
Tekst-G iz uputstva „napiši esej o klimatskim promenama" piše esej token po token. Za svaki sledeći token iz [[Kontekst|konteksta]] računa [[Logit|logite]] za svih oko 100 000 tokena rečnika, pretvara ih u raspodelu pomoću [[Softmax|softmax-a]] i iz nje bira token, sve dok ne izabere token za kraj teksta. Pošto je eksplicitan model, za bilo koji tekst, bio on ljudski ili generisan, može da izračuna [[Verodostojnost|verodostojnost]].

## Kontraprimer
Lica-G pravi fotografije lica nepostojećih osoba, ali je [[Implicitni generativni model|implicitni generativni model]]: ne daje verodostojnost i ne radi sa tokenima, pa nije veliki jezički model.

## Napomene
- Autoregresivni transformer nije vezan za tekst: isti postupak se primenjuje na svaki sadržaj predstavljen nizom tokena, na primer na proteinske sekvence. U prezentaciji se pojam ograničava na generisanje teksta.
- Radi jednostavnosti, u prezentaciji je jedan token jedna reč, iako je token najčešće deo reči.
- Veliki jezički model je polazna tačka celog izlaganja: sledeći pojmovi opisuju kako on računa, šta vidi, kako ocenjuje i bira tokene, i kako se njegov izlaz proverava.

<!-- ================================================== -->

---
tip: pojam
aliases: [autoregressive factorization]
izvor: Y. Bengio, R. Ducharme, P. Vincent, C. Jauvin, „A Neural Probabilistic Language Model", Journal of Machine Learning Research 3, 2003
---
# Autoregresivna faktorizacija (autoregressive factorization)

## Definicija
Autoregresivna faktorizacija je razlaganje verovatnoće niza na proizvod uslovnih verovatnoća njegovih elemenata, pri čemu se verovatnoća svakog elementa računa uz uslov svih elemenata pre njega.

p(x1, …, xn) = ∏ p(xi | x1, …, xi−1)

## Jednostavan primer
Verovatnoća da iz špila od 52 karte zaredom izvučeš dva asa nije 4/52 puta 4/52, nego 4/52 puta 3/51. Druga verovatnoća se računa uz uslov da je prvi izvučeni as već izašao. Autoregresivna faktorizacija radi isto, samo sa rečima umesto karata.

## Primer
Tekst-G rečenici „Danas je lep dan." dodeljuje verovatnoću kao proizvod četiri koraka: P(Danas) = 10%, P(je | Danas) = 50%, P(lep | Danas je) = 40% i P(dan | Danas je lep) = 60%. Proizvod je 1,2%. Isto razlaganje omogućava i pisanje: model izabere „Danas", pa „je" uz uslov „Danas", i tako dalje, token po token. Brojevi su ilustrativni.

## Kontraprimer
Ista četiri tokena u obrnutom redosledu, „Dan lep je danas.", imaju korake od 2%, 1%, 5% i 1%, pa proizvod iznosi svega 0,00001%. Kada bi se tokeni birali nezavisno, bez uslova, redosled ne bi bio važan i obe rečenice bile bi jednako verovatne.

## Napomene
- Razlaganje je tačno za svaku raspodelu nad nizovima, jer sledi iz pravila proizvoda verovatnoće. Modeli se razlikuju samo po tome kako aproksimiraju uslovne verovatnoće.
- Isti postupak služi i za ocenjivanje gotovog teksta (množenje verovatnoća) i za pisanje novog.
- Ono što stoji iza „uz uslov" je [[Kontekst]]. [[Perpleksnost]] se računa iz istih koraka.
- [[Veliki jezički model]] je primena ove faktorizacije.

<!-- ================================================== -->

---
tip: pojam
aliases: [context]
izvor: T. Brown i dr., „Language Models are Few-Shot Learners", NeurIPS 2020
---
# Kontekst (context)

## Definicija
Kontekst je deo niza koji prethodi elementu koji model trenutno generiše, zajedno sa zadatim uslovom, na osnovu kog model računa raspodelu verovatnoće tog elementa.

## Jednostavan primer
Kada prijatelj započne „Pada…", skoro sigurno znaš da sledi „kiša". Znaš to zato što čuješ šta je pre toga rečeno, a ne zato što gledaš unapred. Kontekst je upravo ono što je do sada rečeno.

## Primer
Kada Tekst-G piše peti token eseja, kontekst čine uputstvo „napiši esej o klimatskim promenama" i četiri već napisana tokena („Klima se menja brzo"). Za šesti token kontekst se produžava za upravo izabrani peti token.

## Kontraprimer
Tokeni koji tek dolaze nisu deo konteksta: model ih još nije napisao i ne mogu da utiču na izbor trenutnog tokena. Model nikada ne „gleda unapred".

## Napomene
- Uslov je ono što je zadato spolja ([[Uslovno generisanje|uslovno generisanje]]), a kontekst obuhvata i tokene koje je model sam generisao.
- Najveća dužina konteksta koju model može da obradi naziva se kontekstni prozor (context window).
- Kontekst je „uslov" iz [[Autoregresivna faktorizacija|autoregresivne faktorizacije]]; iz njega model računa [[Logit|logite]].

<!-- ================================================== -->

---
tip: pojam
aliases: [logit, logits]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, odeljak 6.2.2
---
# Logit (logit)

## Definicija
Logit je realan broj koji model dodeljuje jednoj od mogućih vrednosti izlaza pre normalizacije. [[Softmax]] pretvara logite svih mogućih vrednosti u raspodelu verovatnoće, tako da veći logit daje veću verovatnoću.

## Jednostavan primer
Žiri na takmičenju daje poene svakom takmičaru. Poeni su sirove ocene i još nisu procenti: tek kada se pretvore u udeo glasova dobijamo verovatnoće. Logit je takav sirov poen.

## Primer
Posle konteksta „Danas je" Tekst-G tokenu „lep" dodeljuje logit 5,1, a tokenu „petak" logit 4,4 (i tako za svih oko 100 000 tokena rečnika). Softmax nad celim rečnikom to pretvara u verovatnoće 40% i 20%. Razlika logita od 0,7 znači otprilike dvostruko veću verovatnoću, jer je e na 0,7 približno 2.

## Kontraprimer
Logit nije verovatnoća. Može biti negativan (−1,2) ili veći od 1 (5,1), a zbir logita ne daje 100%.

## Napomene
- U statistici „logit" označava logaritam šanse, log(p / (1 − p)). U dubokom učenju termin se koristi šire, za svaki izlaz pre softmax-a.
- Na logitima se primenjuju [[Temperatura|temperatura]] (deli ih) i [[Vodeni žig|vodeni žig]] (dodaje malu vrednost logitima tokena sa zelene liste).
- Logite model računa iz [[Kontekst|konteksta]].

<!-- ================================================== -->

---
tip: pojam
aliases: [softmax]
izvor: I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, MIT Press, 2016, odeljak 6.2.2
---
# Softmax (softmax)

## Definicija
Softmax je funkcija koja skup realnih brojeva ([[Logit|logita]]) pretvara u raspodelu verovatnoće: svaki broj se stepenuje (exp), a zatim podeli zbirom svih stepenovanih brojeva, pa su rezultati pozitivni i u zbiru daju 1.

p(i) = exp(z(i)) / Σ exp(z(j)), gde je z(i) logit tokena i

## Jednostavan primer
Podela nagrade srazmerno poenima: takmičar sa više poena dobija veći udeo, a svi udeli zajedno daju celu nagradu (100%). Razlika je u tome što softmax poene prvo stepenuje, pa i ocene koje su negativne daju pozitivan udeo.

## Primer
Tri tokena imaju logite 2, 1 i 0. Stepenovanjem se dobijaju brojevi 7,4, 2,7 i 1 (zbir 11,1). Deljenjem svakog zbirom dobijaju se verovatnoće 67%, 24% i 9%, koje daju 100%. Tekst-G isto radi nad celim rečnikom od oko 100 000 tokena.

## Kontraprimer
Ocene se ne mogu prosto podeliti njihovim zbirom: negativne ocene bi dale negativne „procente". Zato se prvo stepenuju, tako da svi brojevi postanu pozitivni.

## Napomene
- Veći logit uvek daje veću verovatnoću, ali softmax ističe razlike: mala razlika u logitima daje primetnu razliku u verovatnoći.
- [[Temperatura]] se primenjuje tako što se logiti podele temperaturom pre softmax-a.
- Pojam nije u osnovnoj listi, ali je potreban da bi se razumeli [[Logit]] i [[Temperatura]].

<!-- ================================================== -->

---
tip: pojam
aliases: [temperature]
izvor: A. Holtzman i dr., „The Curious Case of Neural Text Degeneration", ICLR 2020
---
# Temperatura (temperature)

## Definicija
Temperatura je pozitivan parametar kojim se pre primene [[Softmax|softmax-a]] dele svi [[Logit|logiti]]. Vrednost manja od 1 koncentriše raspodelu na najverovatnije vrednosti, a vrednost veća od 1 je izravnava.

p(i) = exp(z(i) / T) / Σ exp(z(j) / T)

## Jednostavan primer
Zamisli da u restoranu uvek naručuješ najpopularnije jelo (niska temperatura) ili da nasumično biraš sa celog jelovnika (visoka temperatura). Niska temperatura daje sigurne, predvidljive izbore, a visoka raznovrsnije, ali i neobičnije.

## Primer
Neka „lep" ima logit veći za 0,7 od „petak". Pri temperaturi 1 „lep" je oko 2 puta verovatniji od „petka". Pri temperaturi 0,5 razlika logita postaje 1,4, pa je „lep" oko 4 puta verovatniji (jedna reč dominira i tekst je siguran, ali ponavljajući). Pri temperaturi 2 razlika postaje 0,35, pa je „lep" verovatniji samo oko 1,4 puta (raspodela je skoro ravna i tekst je raznovrstan, ali nepredvidiv).

## Kontraprimer
Pri temperaturi koja teži nuli, model uvek bira token sa najvećom verovatnoćom. Tada nema slučajnosti, isto uputstvo uvek daje isti tekst, a uzorkovanje prelazi u pohlepni izbor.

## Napomene
- Uzorkovanje sa temperaturom i dalje je [[Uzorkovanje|uzorkovanje]], samo iz izmenjene raspodele.
- Temperatura ne bira token, nego samo oblikuje raspodelu. Token iz nje bira [[Strategija izbora tokena|strategija izbora tokena]].

<!-- ================================================== -->

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

<!-- ================================================== -->

---
tip: pojam
aliases: [content entropy, entropija]
izvor: J. Kirchenbauer i dr., „A Watermark for Large Language Models", ICML 2023. Termin „entropija sadržaja" nije ustaljen.
---
# Entropija sadržaja (content entropy)

## Definicija
Entropija sadržaja je prosečna Šenonova entropija raspodela iz kojih su uzorkovanjem izabrani elementi tog sadržaja. Meri koliko je slobode izbora model imao pri njegovom generisanju.

H(p) = −Σ p(v) · log p(v)

## Jednostavan primer
Popunjavanje formulara sa unapred ispisanim poljima ima malo slobode (niska entropija), a pisanje slobodnog sastava na zadatu temu mnogo (visoka entropija). Entropija meri koliko je izbora autor zaista imao.

## Primer
Na zahtev da napiše funkciju koja sabira dva broja, Tekst-G posle `return a +` bira „b" sa verovatnoćom 99%, pa je entropija te raspodele skoro nula. U eseju o klimatskim promenama skoro svaki sledeći token ima desetine verovatnih kandidata, pa je entropija eseja visoka.

## Kontraprimer
Entropija ne meri dužinu ni težinu teksta. Dugačak, složen tekst koji model piše gotovo bez izbora ima nisku entropiju.

## Napomene
- Definicija je precizna i izračunljiva za nizove tokena. Za slike i druge medije pojam se koristi u prenesenom smislu.
- Entropija sadržaja meri neizvesnost raspodela iz kojih se biralo, a [[Perpleksnost]] meri koliko je model iznenađen izborima koji su stvarno napravljeni.
- Kada je entropija niska, malo je prostora i za [[Vodeni žig|vodeni žig]] i za tragove generatora: posle `return a +` žig ne može da pomeri izbor tokena „b".
- Raspodele iz kojih se računa entropija dobijaju se iz [[Logit|logita]] pomoću [[Softmax|softmax-a]].

<!-- ================================================== -->

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

<!-- ================================================== -->

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

<!-- ================================================== -->

---
tip: pojam
aliases: [watermark, vodeni žig u tekstu]
izvor: J. Kirchenbauer i dr., „A Watermark for Large Language Models", ICML 2023; NIST AI 100-4, 2024
---
# Vodeni žig (watermark)

## Definicija
Vodeni žig je skriveni signal ugrađen u sam sadržaj, pri generisanju ili posle njega, koji nosi informaciju o poreklu sadržaja i čije se prisustvo proverava tajnim ključem.

## Jednostavan primer
Novčanica ima skriven znak koji se ne vidi golim okom, ali se otkriva uz posebno svetlo. Vodeni žig u tekstu je takav skriven obrazac, a ključ je „svetlo" kojim se proverava.

## Primer
Tekst-G ugrađuje žig pri [[Uzorkovanje|uzorkovanju]]. Pre izbora svakog tokena tajni ključ i prethodni token pseudoslučajno određuju zelenu listu, četvrtinu rečnika, a [[Logit|logitima]] tokena sa zelene liste dodaje se ista mala vrednost. U običnom tekstu otprilike svaki četvrti token je zelen, a esej sa žigom sadrži znatno više zelenih tokena nego što bi slučajno imao. Taj obrazac vidi samo onaj ko ima ključ: prebroji zelene tokene i statistički proveri da ih je previše za slučajnost.

## Kontraprimer
Kada model nema izbora (posle `return a +` skoro sigurno sledi „b"), nema šta da se pomeri, pa žig ne može da se ugradi. Takođe, odsustvo žiga ne dokazuje da je tekst napisao čovek.

## Napomene
- Žig nije vidljiv vodeni znak (na primer logo preko slike) i nije metapodatak: ugrađen je u sam sadržaj.
- Žig u uzorkovanju zavisi od [[Entropija sadržaja|entropije sadržaja]], jer pomera izbore koje model ima.
- Odsustvo žiga ne dokazuje da je sadržaj ljudski, jer žig ne nose ni sadržaj drugih generatora ni sadržaj iz kog je žig uklonjen.
- Za razliku od [[Detekcija bez žiga|detekcije bez žiga]], provera žiga zahteva saradnju generatora i tajni ključ, ali ima unapred kontrolisanu stopu lažno pozitivnih nalaza.
