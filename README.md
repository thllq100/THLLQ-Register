# THLLQ — Register der Aussagen

Dieses Verzeichnis ist der Nachweis. Alles andere auf der Website wird daraus erzeugt.

Der Gedanke dahinter ist einfach: Eine Trefferquote ist wertlos, wenn man nicht
nachprüfen kann, dass die Aussage vor dem Ereignis dastand. Git kann das. Jeder
Commit trägt einen Zeitstempel in einer Kette von Prüfsummen — wer einen alten
Eintrag nachträglich ändert, ändert jede Prüfsumme danach mit, und das sieht man.
Deshalb liegt das Register öffentlich, und deshalb wird hier nie etwas überschrieben.

## Die vier Regeln

1. **Die Auflösungsregel steht vor dem Ereignis fest.** Wortlaut, Quelle, Zeitpunkt
   und der Umgang mit Gleichstand werden mit der Aussage veröffentlicht.
2. **Eine eingetragene Datei wird nie geändert, nur ergänzt.** Die Auflösung kommt
   in eine eigene Datei, damit die Aussage unangetastet bleibt. `pruefen.py` fragt
   Git, ob sich jemand nicht daran gehalten hat.
3. **Maßgeblich ist die Erstveröffentlichung.** Spätere Revisionen einer Statistik
   ändern nichts am Ausgang.
4. **Veröffentlicht wird alles.** Auch was danebengeht, auch die schlechten Quartale.

## Aufbau

```
aussagen/2026-09-15-vpi-de-september.json      nach dem Commit unveränderlich
aufloesungen/2026-09-15-vpi-de-september.json  kommt später dazu
schema/                                        beschreibt beide Formate
site/register.js                               erzeugt, für die Website
site/register.json                             dasselbe als reines JSON
```

## Ablauf

**Eine Aussage veröffentlichen**

```bash
python3 neu.py                 # fragt der Reihe nach, Regel vor Wahrscheinlichkeit
python3 pruefen.py             # muss ohne Fehler durchlaufen
git add aussagen/ && git commit -m "Aussage: ..." && git push
```

Ab dem Push steht der Zeitstempel öffentlich. Vorher ist nichts passiert — eine
Aussage, die nur lokal liegt, zählt nicht und darf auch nicht in den Brief.

**Eine Aussage auflösen**

```bash
python3 aufloesen.py           # zeigt die Regel, aber nicht die Wahrscheinlichkeit
python3 pruefen.py && python3 bauen.py
git add aufloesungen/ site/ && git commit -m "Auflösung: ..." && git push
```

Dass beim Auflösen die eigene Wahrscheinlichkeit verdeckt bleibt, ist kein Spleen.
Wer weiß, was er angekündigt hat, legt eine unscharfe Regel unbewusst günstig aus.
Besser ist, die Regel vorher scharf zu formulieren — und wenn sie es doch nicht war,
gehört das in die Anmerkung.

**Automatisch prüfen lassen**

```bash
cp haken/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

Danach lässt Git keinen Commit mehr durch, der das Register beschädigt.

## Was gerechnet wird

| | |
|---|---|
| Trefferquote | Anteil eingetretener Aussagen |
| Brier-Score | mittlerer quadratischer Abstand zwischen Ankündigung und Ausgang; kleiner ist besser, 0,25 entspricht „immer 50 %" |
| Vorsprung | 1 − Brier(wir) / Brier(Grundrate). Die einzige Zahl, die wirklich zählt |
| Schwierigkeit | mittlerer Abstand zur Grundrate. Ohne sie lässt sich eine Trefferquote schönrechnen |
| Wilson-Intervall | 95 % je Klasse. Bei wenigen Fällen ist es breit, und das soll man sehen |

## Ab wann etwas aussagekräftig ist

| aufgelöste Aussagen | was sich sagen lässt |
|---|---|
| 50 | erster Zwischenstand, Richtung erkennbar, statistisch noch nichts |
| 200 | Kalibrierung je Klasse mit brauchbarem Intervall |
| 350 | ein deutlicher Vorsprung wird sichtbar |
| 700 | auch ein kleiner Vorsprung lässt sich von null unterscheiden |

Bei fünf bis acht Aussagen pro Woche sind das etwa drei, acht, zwölf und
vierundzwanzig Monate.

## Vorher lesen

`../rueckrechnung_ergebnis.md` — die Prüfung, die dazu geführt hat, dass hier keine
Indexrichtungen stehen. Wochenrichtung von S&P 500, DAX und Nasdaq ist über 5.800
getestete Wochen nicht vorhersagbar, auch nicht mit der Positionierung aus den
CFTC-Berichten. Das Register beginnt deshalb dort, wo es keine öffentliche
Grundrate zum Nachschlagen gibt.
