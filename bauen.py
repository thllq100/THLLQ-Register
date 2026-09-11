#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bauen.py — rechnet aus dem Register die Kalibrierungstafel und schreibt sie
für die Website heraus.

Erzeugt zwei Dateien in site/:
  register.js    window.THLLQ_REGISTER = {...}  — funktioniert auch per Doppelklick
                 auf die index.html, weil ein script-Tag kein fetch braucht.
  register.json  dasselbe als reines JSON, für alles andere.

Gerechnet wird:
  Trefferquote   Anteil eingetretener Aussagen
  Brier-Score    mittlerer quadratischer Abstand zwischen Ankündigung und Ausgang.
                 Kleiner ist besser, 0,25 ist der Wert für "immer 50 Prozent".
  Vorsprung      1 − Brier(wir) / Brier(Grundrate). Positiv heißt: besser als die
                 Grundrate. Das ist die einzige Zahl, die wirklich zählt.
  Schwierigkeit  mittlerer Abstand unserer Wahrscheinlichkeit zur Grundrate.
                 Ohne diese Zahl lässt sich eine Trefferquote schönrechnen, indem
                 man nur leichte Aussagen trifft.
  Wilson         95-Prozent-Intervall je Klasse. Bei kleinen n ist es breit, und
                 das soll man sehen.

Aufruf:  python3 bauen.py
"""

import json, math, os, sys
from datetime import datetime

HIER = os.path.dirname(os.path.abspath(__file__))
AUS  = os.path.join(HIER, "aussagen")
AUF  = os.path.join(HIER, "aufloesungen")
ZIEL = os.path.join(HIER, "site")

KLASSEN = [(0.00, 0.45), (0.45, 0.55), (0.55, 0.65), (0.65, 0.80), (0.80, 1.00)]
ARTNAMEN = {"vpi": "Verbraucherpreise", "arbeitsmarkt": "Arbeitsmarkt",
            "stimmung": "Stimmungsindikatoren", "quartalszahlen": "Quartalszahlen",
            "notenbank": "Notenbanken", "sonstiges": "Sonstiges"}

def wilson(k, n, z=1.96):
    """95-Prozent-Intervall für einen Anteil. Bei n=0 gibt es nichts zu sagen."""
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    mitte = (p + z * z / (2 * n)) / d
    rand = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, mitte - rand), min(1.0, mitte + rand))

def lies_ordner(pfad):
    if not os.path.isdir(pfad):
        return {}
    aus = {}
    for f in sorted(os.listdir(pfad)):
        if f.endswith(".json"):
            with open(os.path.join(pfad, f), encoding="utf-8") as h:
                d = json.load(h)
                aus[d["id"]] = d
    return aus

def rechne():
    aussagen = lies_ordner(AUS)
    aufl     = lies_ordner(AUF)

    zeilen = []
    for i, a in sorted(aussagen.items()):
        r = aufl.get(i)
        zeilen.append({
            "id": i, "frage": a["frage"], "p": a["p"],
            "grundrate": a.get("grundrate", 0.5), "art": a["art"],
            "aufgestellt": a["aufgestellt"], "stichtag": a["stichtag"],
            "regel": a["aufloesungsregel"], "quelle": a["quelle"],
            "konsens": a.get("konsens", ""), "begruendung": a.get("begruendung", ""),
            "o": (1 if r["eingetreten"] else 0) if r else None,
            "beleg": r["beleg"] if r else "",
            "aufgeloest": r["aufgeloest"] if r else "",
            "anmerkung": (r or {}).get("anmerkung", ""),
        })

    fertig = [z for z in zeilen if z["o"] is not None]
    n = len(fertig)

    stand = {"n": len(zeilen), "aufgeloest": n, "offen": len(zeilen) - n}
    if n:
        brier  = sum((z["p"] - z["o"]) ** 2 for z in fertig) / n
        brier0 = sum((z["grundrate"] - z["o"]) ** 2 for z in fertig) / n
        stand.update({
            "treffer":     sum(z["o"] for z in fertig) / n * 100,
            "brier":       brier,
            "brier_grund": brier0,
            "vorsprung":   (1 - brier / brier0) * 100 if brier0 > 0 else 0.0,
            "schwierigkeit": sum(abs(z["p"] - z["grundrate"]) for z in fertig) / n * 100,
        })

    # Kalibrierung je Klasse
    klassen = []
    for lo, hi in KLASSEN:
        g = [z for z in fertig if lo <= z["p"] < hi or (hi == 1.0 and z["p"] == 1.0)]
        if not g:
            continue
        k = sum(z["o"] for z in g)
        u, o = wilson(k, len(g))
        klassen.append({"lo": lo, "hi": hi, "n": len(g),
                        "angekuendigt": sum(z["p"] for z in g) / len(g) * 100,
                        "eingetreten": k / len(g) * 100,
                        "unten": u * 100, "oben": o * 100})

    # nach Quartal — damit sichtbar bleibt, wann es nicht lief
    quartale = {}
    for z in fertig:
        d = datetime.strptime(z["stichtag"], "%Y-%m-%dT%H:%M")
        key = f"{d.year} Q{(d.month - 1) // 3 + 1}"
        quartale.setdefault(key, []).append(z)
    q_liste = []
    for key, g in sorted(quartale.items()):
        b  = sum((z["p"] - z["o"]) ** 2 for z in g) / len(g)
        b0 = sum((z["grundrate"] - z["o"]) ** 2 for z in g) / len(g)
        q_liste.append({"quartal": key, "n": len(g),
                        "treffer": sum(z["o"] for z in g) / len(g) * 100,
                        "brier": b,
                        "vorsprung": (1 - b / b0) * 100 if b0 > 0 else 0.0})

    # nach Art — mit Grundrate, damit man sieht, was leicht war
    arten = []
    for schl, label in ARTNAMEN.items():
        g = [z for z in fertig if z["art"] == schl]
        if not g:
            continue
        arten.append({"art": label, "n": len(g),
                      "grundrate": sum(z["grundrate"] for z in g) / len(g) * 100,
                      "angekuendigt": sum(z["p"] for z in g) / len(g) * 100,
                      "eingetreten": sum(z["o"] for z in g) / len(g) * 100,
                      "schwierigkeit": sum(abs(z["p"] - z["grundrate"]) for z in g) / len(g) * 100})

    return {"erzeugt": datetime.now().strftime("%Y-%m-%dT%H:%M"),
            "stand": stand, "klassen": klassen, "quartale": q_liste,
            "arten": arten, "aussagen": zeilen}

def main():
    daten = rechne()
    os.makedirs(ZIEL, exist_ok=True)
    roh = json.dumps(daten, ensure_ascii=False, indent=1)
    with open(os.path.join(ZIEL, "register.json"), "w", encoding="utf-8") as f:
        f.write(roh + "\n")
    with open(os.path.join(ZIEL, "register.js"), "w", encoding="utf-8") as f:
        f.write("/* erzeugt von bauen.py – nicht von Hand ändern */\n"
                "window.THLLQ_REGISTER = " + roh + ";\n")
    s = daten["stand"]
    print(f"{s['n']} Aussagen, davon {s['aufgeloest']} aufgelöst, {s['offen']} offen")
    if s["aufgeloest"]:
        print(f"  Trefferquote   {s['treffer']:.1f} %")
        print(f"  Brier          {s['brier']:.4f}   (Grundrate {s['brier_grund']:.4f})")
        print(f"  Vorsprung      {s['vorsprung']:+.2f} %")
        print(f"  Schwierigkeit  {s['schwierigkeit']:.1f} Punkte")
        if s["aufgeloest"] < 50:
            print("\n  Unter 50 aufgelösten Aussagen heißt das noch nichts. "
                  "Die Zahlen stehen da, damit man den Aufbau sieht, nicht zum Auslegen.")
    else:
        print("  Noch nichts aufgelöst – die Tafel bleibt leer, und das ist richtig so.")
    print(f"\ngeschrieben: site/register.js und site/register.json")

if __name__ == "__main__":
    sys.exit(main() or 0)
