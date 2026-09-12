#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
heute.py — die taegliche Cash-Open-Aussage, in zwanzig Sekunden.

Frage, Auflösungsregel und Grundrate sind jeden Tag dieselben. Nur deine
Wahrscheinlichkeit und eine kurze Begründung kommen von dir. Genau deshalb
gibt es dieses Skript: Was man täglich tut, muss reibungslos sein, sonst
hält man es nicht zwei Jahre durch.

Aufruf:  python3 heute.py        (vor 15:30 MESZ)
"""

import json, os, re, sys
from datetime import datetime

HIER = os.path.dirname(os.path.abspath(__file__))
AUS  = os.path.join(HIER, "aussagen")

FRAGE = ("Entsteht heute zwischen 15:30 und 15:40 ein regelkonformes Setup "
         "nach Version 2.0?")
REGEL = ("Eingetreten, wenn zwischen 15:30 und 15:40 Uhr MESZ mindestens eine "
         "M1-Kerze mindestens 8 Ticks jenseits eines vor 15:30 markierten Levels "
         "schliesst, die Richtung dem Cash-Open-Filter entspricht und der Kurs "
         "beim Schluss dieser Kerze nicht mehr als 80 Ticks von diesem Level "
         "entfernt ist. Ein Schluss exakt auf der Linie zaehlt als nicht "
         "eingetreten. Ob ich tatsaechlich eingestiegen bin, spielt keine Rolle - "
         "es zaehlen allein die Bedingungen. Massgeblich ist die Erstaufzeichnung "
         "im eigenen Chart, festgehalten im Review derselben Session; spaetere "
         "Korrekturen bleiben unberuecksichtigt.")
QUELLE = "eigener Chart, Review derselben Session"
GRUNDRATE = 0.32   # gemessen: 16 Setups in 50 Sessions, 06.07.-11.09.2026

def main():
    jetzt = datetime.now()

    # Eine Aussage nach dem Ereignis ist wertlos. Das ist kein Hinweis, das ist eine Sperre.
    if (jetzt.hour, jetzt.minute) >= (15, 30):
        print(f"\n  Es ist {jetzt:%H:%M}. Das Fenster hat begonnen oder ist vorbei.")
        print("  Eine Aussage nach dem Ereignis ist wertlos - heute kein Eintrag mehr.")
        print("  Morgen vor 15:30 wieder.\n")
        return 1

    pfad = os.path.join(AUS, f"{jetzt:%Y-%m-%d}-open.json")
    if os.path.exists(pfad):
        print(f"\n  Fuer heute gibt es schon eine Aussage:\n    aussagen/{os.path.basename(pfad)}")
        print("  Eine veroeffentlichte Aussage wird nicht geaendert.\n")
        return 1

    print("\n" + "=" * 62)
    print(f"  CASH OPEN  {jetzt:%A, %d.%m.%Y}      noch {(15*60+30)-(jetzt.hour*60+jetzt.minute)} Min. bis 15:30")
    print("=" * 62)
    print(f"  {FRAGE}")
    print(f"\n  Grundrate: {GRUNDRATE:.0%}  (gemessen ueber 50 Sessions)")
    print("  Voranalyse fertig? Level markiert? Kalender geprueft?")
    print("  Wenn nein: erst das, dann hierher zurueck.\n")

    while True:
        p = input("  Deine Wahrscheinlichkeit (z. B. 0.38): ").strip().replace(",", ".")
        if re.fullmatch(r"0?\.\d+", p) and 0.01 <= float(p) <= 0.99:
            break
        print("     Zwischen 0.01 und 0.99, mit Punkt. Nie 0, nie 1.")

    ab = float(p) - GRUNDRATE
    print(f"     {abs(ab)*100:.0f} Punkte {'ueber' if ab>0 else 'unter' if ab<0 else 'auf'} der Grundrate.")

    print("\n  Begruendung - ein bis drei Saetze. Auch was dagegen spricht.")
    begr = input("  > ").strip()
    while len(begr) < 40:
        begr = input("  Zu knapp. Warum diese Zahl, und was spricht dagegen? ").strip()

    d = {"id": f"{jetzt:%Y-%m-%d}-open",
         "aufgestellt": jetzt.strftime("%Y-%m-%dT%H:%M"),
         "stichtag": jetzt.strftime("%Y-%m-%dT15:40"),
         "art": "eroeffnung", "frage": FRAGE,
         "p": float(p), "grundrate": GRUNDRATE,
         "aufloesungsregel": REGEL, "quelle": QUELLE,
         "konsens": f"Grundrate {GRUNDRATE:.0%}, gemessen ueber 50 Sessions (06.07.-11.09.2026)",
         "begruendung": begr}
    os.makedirs(AUS, exist_ok=True)
    with open(pfad, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1); f.write("\n")

    print(f"\n  Angelegt: aussagen/{jetzt:%Y-%m-%d}-open.json")
    print("\n  Jetzt veroeffentlichen - ohne Push ist nichts passiert:")
    print("    python3 pruefen.py")
    print("    GitHub Desktop: Commit  ->  PUSH")
    print(f"\n  Heute Abend nach dem Review:  python3 aufloesen.py\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
