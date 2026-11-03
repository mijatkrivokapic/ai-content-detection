# Baza znanja: Detekcija AI-generisanog sadržaja

Baza znanja nalik udžbeniku, koju tim gradi kroz runde prezentacija. Sadrži pojmove sa definicijama, primerima i vezama, potrebne da se opiše i reši jedan konkretan problem.

- **Tema:** generativni modeli i detekcija sadržaja koji su oni generisali (tekst, slika, audio, video).
- **Problem:** projektovanje sistema za detekciju generisanog sadržaja u procesu verifikacije materijala koji novinska agencija prima pre objave.
- **Jezik:** srpski, latinica; engleski termin u zagradi.

Tačna podešavanja su u [`_meta/konfiguracija.md`](_meta/konfiguracija.md), a svi dogovori tima u [`_meta/odluke.md`](_meta/odluke.md).

## Struktura

```
_meta/
  konfiguracija.md        tema, problem, publika, konteksti
  odluke.md               dogovori: pretpostavljeni pojmovi, konvencije, promene, otvorena pitanja
konteksti/                izmišljeni svetovi iz kojih se uzimaju primeri
  Novinska agencija Vidik.md   primarni kontekst (glavni primer svakog pojma)
  Kocka.md                     sekundarni kontekst (jednostavan primer)
  Poligon.md                   sekundarni kontekst (imenovani modeli i detektori)
pojmovi/                  jedna beleška po pojmu, naziv = srpski termin u nominativu
runde/
  runda-1/
    README.md             pregled runde: uloge, prezentacije, pojmovi
    urednici.md           urednički pregled runde
    prezentacija-1/       materijal prezentacije (slajdovi, izvorni kod)
    prezentacija-2/
    prezentacija-3/
.claude/skills/baza-znanja/   uputstvo i šabloni za rad sa Claude-om
```

Folderi `_meta/`, `konteksti/` i `pojmovi/` čine samu bazu. Folder `runde/` čuva materijale i preglede po rundama.

## Ko šta dodaje i gde

| Uloga | Šta dodaje | Gde |
|---|---|---|
| Prezenter | Po jednu belešku za svaki svoj pojam | `pojmovi/` |
| Prezenter | Slajdove, PDF ili izvorni kod prezentacije | `runde/runda-N/prezentacija-K/` |
| Prezenter | Novi detalj konteksta koji uvodi primer | odgovarajući fajl u `konteksti/` |
| Urednik | Urednički pregled runde | `runde/runda-N/urednici.md` |
| Urednik | Dogovore tima (nazivi, pretpostavljeni pojmovi, promene) | `_meta/odluke.md` |
| Lovac na slepe mrlje | Pojmove koji nedostaju i nejasna mesta | `runde/runda-N/slepe-mrlje.md` |
| Svi | Pregled runde kada se završi | `runde/runda-N/README.md` |

## Grane i pull requestovi

- Svako radi na svojoj grani, nikad direktno na `main`.
- Naziv grane: `runda-N-prezentacija-K` za prezentere, `runda-N-urednici` za urednike.
- Rad se predaje kroz pull request; urednici pregledaju PR-ove svoje runde.
- Automatski fajlovi (`__pycache__`, `*.pyc`, Manim `media/`) ne idu na repozitorijum; to obezbeđuje `.gitignore`.

## Pravila za beleške pojmova

Kratak pregled; puna pravila su u [`.claude/skills/baza-znanja/SKILL.md`](.claude/skills/baza-znanja/SKILL.md) i u `_meta/odluke.md`.

- [ ] Pre pisanja proveriti `pojmovi/` i `_meta/odluke.md`: da li pojam ili bliski pojam već postoji ili je pretpostavljen.
- [ ] Šablon [`pojam.md`](.claude/skills/baza-znanja/assets/pojam.md): Definicija, Jednostavan primer (Kocka), Primer (agencija Vidik), po potrebi Kontraprimer, Sekundarni primeri, Napomene.
- [ ] Postojeće pojmove linkovati, sa padežom: `[[Verodostojnost|verodostojnosti]]`.
- [ ] Termini iz odluka: primerak, prompt, trening skup.
- [ ] Izvor u zaglavlju: knjiga, standard ili rad sa najsličnijom definicijom.

## Rad u Obsidianu

Otvoriti koren repozitorijuma kao Obsidian vault. Linkovi `[[...]]` tada vode od pojma do pojma, a engleski nazivi iz `aliases` rade u pretrazi. Na GitHubu se ti linkovi prikazuju kao običan tekst.

## Runde

| Runda | Tema | Status |
|---|---|---|
| [Runda 1](runde/runda-1/README.md) | Osnove generisanja, reprezentacija i latentni prostor, jezički model | završena |
| [Runda 2](runde/runda-2/README.md) | Arhitekture generatora, ostali mediji, od generisanja ka detekciji | u pripremi |
