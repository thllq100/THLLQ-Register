#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aufloesen.py — trägt den Ausgang einer Aussage ein.

Die Auflösung kommt in eine eigene Datei. Die Aussage selbst bleibt Byte für Byte
so, wie sie veröffentlicht wurde — das ist der Grund, warum man dem Zeitstempel
später glauben kann.

Das Skript zeigt dir vor der Eingabe noch einmal die Regel im Wortlaut, aber nicht
die Wahrscheinlichkeit. Wer beim Auflösen weiß, was er angekündigt hat, legt die
Regel unbewusst günstig aus. Das ist keine Unterstellung, das ist gut untersucht.

Aufruf:  python3 aufloesen.py
"""

import json, os, sys
from datetime import datetime

HIER = os.path.dirname(os.path.abspath(__file__))
AUS  = os.path.join(HIER, "aussagen")
AUF  = os.path.join(HIER, "aufloesungen")

def main():
    if not os.path.isdir(AUS):
        sys.exit("Kein Ordner aussagen/ gefunden.")
    offen = []
    jetzt = datetime.now()
    for f in sorted(os.listdir(AUS)):
        if not f.endswith(".json"):
            continue
        with open(os.path.join(AUS, f), encoding="utf-8") as h:
            a = json.load(h)
        if os.path.exists(os.path.join(AUF, a["id"] + ".json")):
            continue
        if datetime.strptime(a["stichtag"], "%Y-%m-%dT%H:%M") <= jetzt:
            offen.append(a)

    if not offen:
        print("Nichts fällig. Alle Aussagen mit vergangenem Stichtag sind aufgelöst.")
        return

    print("\n" + "=" * 62)
    print("  FÄLLIGE AUSSAGEN")
    print("=" * 62)
    for i, a in enumerate(offen, 1):
        print(f"  [{i}] {a['stichtag'][:10]}  {a['frage'][:64]}")
    w = input(f"\n  Welche auflösen [1-{len(offen)}]? ").strip()
    if not w.isdigit() or not (1 <= int(w) <= len(offen)):
        sys.exit("  Abgebrochen.")
    a = offen[int(w) - 1]

    print("\n" + "-" * 62)
    print("  " + a["frage"])
    print("-" * 62)
    print("  Regel:  " + a["aufloesungsregel"])
    print("  Quelle: " + a["quelle"])
    if a.get("konsens"):
        print("  Konsens: " + a["konsens"])
    print("\n  (Die angekündigte Wahrscheinlichkeit wird hier bewusst nicht gezeigt.)")

    # Der Beleg ist das, womit ein Fremder nachrechnet. Eine Kursfrage hat keine
    # veröffentlichte Zahl, sondern einen Verlauf - also wird anders gefragt.
    if a.get("art") == "eroeffnung":
        print("\n  Muster: Bezugspunkt 24.812,25 (Eroeffnung M1 15:30). 200 Ticks nach oben")
        print("          um 16:04 erreicht, Gegenrichtung vorher hoechstens 60 Ticks.")
        beleg = input("\n  Welche Marke zuerst, um welche Uhrzeit, und wo lag der Bezugspunkt? ").strip()
        while len(beleg) < 30:
            beleg = input("  Bitte nachpruefbar: Marke, Uhrzeit und Bezugspunkt. ").strip()
    else:
        beleg = input("\n  Welche Zahl wurde veröffentlicht, und wo steht sie? ").strip()
        while len(beleg) < 15:
            beleg = input("  Bitte nachprüfbar: Zahl und Fundstelle. ").strip()
    e = input("  Eingetreten? [j/n] ").strip().lower()
    while e not in ("j", "n"):
        e = input("  Bitte j oder n. Kein 'teilweise'. ").strip().lower()
    anm = input("  Anmerkung (optional, ändert nichts am Ausgang): ").strip()

    d = {"id": a["id"], "aufgeloest": jetzt.strftime("%Y-%m-%dT%H:%M"),
         "eingetreten": e == "j", "beleg": beleg}
    if anm:
        d["anmerkung"] = anm

    os.makedirs(AUF, exist_ok=True)
    with open(os.path.join(AUF, a["id"] + ".json"), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")

    print(f"\n  Angelegt: aufloesungen/{a['id']}.json")
    print(f"  Angekündigt waren {a['p']*100:.0f} % — "
          f"{'getroffen' if (e=='j') == (a['p']>=0.5) else 'danebengelegen'}.")
    print("\n    python3 pruefen.py && python3 bauen.py")
    print(f"    git add aufloesungen/{a['id']}.json site/")
    print(f'    git commit -m "Auflösung: {a["id"]}"')

if __name__ == "__main__":
    main()
