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

FRAGE = ("Laeuft der Nasdaq heute ab 15:30 mindestens 200 Ticks in eine Richtung, "
         "bevor er 100 Ticks in die Gegenrichtung laeuft?")
REGEL = ("Bezugspunkt ist der Eroeffnungskurs der Minutenkerze 15:30 im Nasdaq-100-Future "
         "(NQ, fortlaufender Kontrakt, Zeitzone Europe/Berlin). Eingetreten, wenn der Kurs "
         "bis 17:00 Uhr in einer der beiden Richtungen 200 Ticks (50,00 Punkte) vom "
         "Bezugspunkt erreicht, ohne vorher in der Gegenrichtung 100 Ticks (25,00 Punkte) "
         "erreicht zu haben. Gemessen werden Hoch und Tief der Minutenkerzen; eine "
         "Beruehrung genuegt, ein Schluss ist nicht noetig. Enthaelt dieselbe Minutenkerze "
         "beide Marken, laesst sich die Reihenfolge nicht feststellen und die Richtung gilt "
         "als gescheitert. Ob ich gehandelt habe, spielt keine Rolle - es zaehlt allein der "
         "Kursverlauf. Wird bis 17:00 Uhr keine der beiden 200er-Marken erreicht, gilt die "
         "Aussage als nicht eingetreten.")
QUELLE = "Minutendaten des NQ-Future, nachpruefbar in jedem Chart"
GRUNDRATE = 0.64   # gemessen: 164 von 258 Sessions, 19.09.2025-18.09.2026
#
# Die Grundrate ist die Eintrittsquote der letzten zwoelf Monate abgeschlossener
# Sessions. Sie wird am ersten Handelstag jedes Quartals neu berechnet und gilt
# dann unveraendert bis zum naechsten Quartal. Jede Aenderung wird im Freitags-
# brief mit neuer Zahl und Anzahl der Sessions genannt.
#
# Warum ueberhaupt neu gemessen wird: Die Schwelle steht in Ticks fest, der Index
# steigt. 50 Punkte waren 2010 zweieinhalb Prozent vom Kurs und sind heute 0,18 %.
# Die Grundrate driftet deshalb nach oben, ohne dass sich der Markt aendert.
# Gemessen ueber 4.185 Sessions seit 2010: mit mitwachsender Schwelle liegt die
# Trendneigung durchgehend bei rund 0,64 - die Drift kommt allein vom Indexstand.
# Die alte Grundrate 0,52 stammte aus 50 Sommersessions und war zu niedrig.

def main():
    jetzt = datetime.now()

    # Eine Aussage nach dem Ereignis ist wertlos. Das ist kein Hinweis, das ist eine Sperre.
    if (jetzt.hour, jetzt.minute) >= (15, 30):
        print(f"\n  Es ist {jetzt:%H:%M}. Das Fenster hat begonnen oder ist vorbei.")
        print("  Eine Aussage nach dem Ereignis ist wertlos - heute kein Eintrag mehr.")
        print("  Morgen vor 15:30 wieder.\n")
        return 1

    pfad = os.path.join(AUS, f"{jetzt:%Y-%m-%d}-trend.json")
    if os.path.exists(pfad):
        print(f"\n  Fuer heute gibt es schon eine Aussage:\n    aussagen/{os.path.basename(pfad)}")
        print("  Eine veroeffentlichte Aussage wird nicht geaendert.\n")
        return 1

    print("\n" + "=" * 62)
    print(f"  TRENDTAG - JA ODER NEIN  {jetzt:%A, %d.%m.%Y}      noch {(15*60+30)-(jetzt.hour*60+jetzt.minute)} Min. bis 15:30")
    print("=" * 62)
    print(f"  {FRAGE}")
    print(f"\n  Grundrate: {GRUNDRATE:.0%}  (gemessen ueber 258 Sessions, letzte 12 Monate)")
    print("  Vorlauf angesehen? Kalender geprueft? Gap beachtet?")
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

    d = {"id": f"{jetzt:%Y-%m-%d}-trend",
         "aufgestellt": jetzt.strftime("%Y-%m-%dT%H:%M"),
         "stichtag": jetzt.strftime("%Y-%m-%dT17:00"),
         "art": "eroeffnung", "frage": FRAGE,
         "p": float(p), "grundrate": GRUNDRATE,
         "aufloesungsregel": REGEL, "quelle": QUELLE,
         "konsens": f"Grundrate {GRUNDRATE:.0%} - 164 von 258 Sessions, 19.09.2025-18.09.2026. "
                    f"Vertrauensintervall 0,58 bis 0,69. Quelle: eigene Auswertung der Minutendaten, NQ fortlaufend, Databento GLBX.MDP3",
         "begruendung": begr}
    os.makedirs(AUS, exist_ok=True)
    with open(pfad, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1); f.write("\n")

    print(f"\n  Angelegt: aussagen/{jetzt:%Y-%m-%d}-trend.json")
    print("\n  Jetzt veroeffentlichen - ohne Push ist nichts passiert:")
    print("    python3 pruefen.py")
    print("    GitHub Desktop: Commit  ->  PUSH")
    print(f"\n  Heute Abend nach dem Review:  python3 aufloesen.py\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
