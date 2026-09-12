#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
neu.py — legt eine neue Aussage an, im Dialog.

Der Sinn ist nicht Bequemlichkeit, sondern Disziplin: Die Fragen kommen in der
Reihenfolge, in der man sie ehrlich beantworten muss. Die Wahrscheinlichkeit wird
zuletzt gefragt — erst die Regel, dann die Zahl. Wer es umgekehrt macht, biegt
sich die Regel zur Zahl zurecht, meist ohne es zu merken.

Aufruf:  python3 neu.py
"""

import json, os, re, sys
from datetime import datetime

HIER = os.path.dirname(os.path.abspath(__file__))
AUS  = os.path.join(HIER, "aussagen")
ARTEN = ["vpi", "arbeitsmarkt", "stimmung", "quartalszahlen", "notenbank",
         "eroeffnung", "sonstiges"]

def frag(text, pruef=None, hinweis=""):
    while True:
        w = input("  " + text + " ").strip()
        if pruef is None or pruef(w):
            return w
        print("     " + (hinweis or "Bitte noch einmal."))

def zeitfrage(text):
    def ok(w):
        try:
            datetime.strptime(w, "%Y-%m-%dT%H:%M"); return True
        except ValueError:
            return False
    return frag(text, ok, "Format: 2026-09-30T08:00")

def main():
    print("\n" + "=" * 62)
    print("  NEUE AUSSAGE")
    print("=" * 62)
    print("  Erst die Frage und die Regel, dann die Wahrscheinlichkeit.")
    print("  Diese Reihenfolge ist Absicht.\n")

    frage = frag("Die Frage (mit Fragezeichen, ja/nein-beantwortbar):",
                 lambda w: len(w) >= 25, "Zu knapp. Was genau soll entschieden werden?")
    print(f"\n  Arten: {', '.join(ARTEN)}")
    art = frag("Art:", lambda w: w in ARTEN, "Bitte eine aus der Liste.")
    konsens = frag("Konsens/Erwartung, gegen die gemessen wird (mit Stand und Herkunft):")
    quelle  = frag("Wer veröffentlicht die entscheidende Zahl?", lambda w: len(w) >= 5)

    print("\n  Auflösungsregel. Sie muss vier Dinge sagen:")
    print("    1. Welche Zahl entscheidet und ab welcher Schwelle")
    print("    2. Wann und wo sie veröffentlicht wird")
    print("    3. Was bei exaktem Gleichstand gilt")
    print("    4. Ob spätere Revisionen zählen (Antwort: nein, die Erstveröffentlichung gilt)")
    regel = frag("Regel:", lambda w: len(w) >= 60,
                 "Zu knapp. Ein Fremder muss sie in einem Jahr anwenden können.")

    stichtag = zeitfrage("Stichtag (JJJJ-MM-TTThh:mm):")

    print("\n  Jetzt erst die Zahl.")
    grund = frag("Grundrate dieser Frage [0.5]:",
                 lambda w: w == "" or re.match(r"^0?\.\d+$", w), "Etwa 0.5") or "0.5"
    p = frag("Unsere Wahrscheinlichkeit für ja, z. B. 0.62:",
             lambda w: re.match(r"^0?\.\d+$", w or "") and 0.01 <= float(w) <= 0.99,
             "Zwischen 0.01 und 0.99. Nie 0, nie 1.")
    begr = frag("Begründung — auch das, was dagegen spricht:")

    kurz = frag("Kurzname für die Datei (klein, mit Bindestrichen):",
                lambda w: re.match(r"^[a-z0-9-]+$", w or ""), "Nur a-z, 0-9 und Bindestriche.")

    jetzt = datetime.now()
    d = {"id": f"{jetzt:%Y-%m-%d}-{kurz}",
         "aufgestellt": jetzt.strftime("%Y-%m-%dT%H:%M"),
         "stichtag": stichtag, "art": art, "frage": frage,
         "p": float(p), "grundrate": float(grund),
         "aufloesungsregel": regel, "quelle": quelle,
         "konsens": konsens, "begruendung": begr}

    os.makedirs(AUS, exist_ok=True)
    pfad = os.path.join(AUS, d["id"] + ".json")
    if os.path.exists(pfad):
        sys.exit(f"\n  {pfad} gibt es schon. Anderen Kurznamen wählen.")
    with open(pfad, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")

    print(f"\n  Angelegt: aussagen/{d['id']}.json")
    print("\n  Jetzt prüfen und veröffentlichen:")
    print("    python3 pruefen.py")
    print(f"    git add aussagen/{d['id']}.json")
    print(f'    git commit -m "Aussage: {kurz}"')
    print("    git push")
    print("\n  Ab dem Push ist der Zeitstempel öffentlich. Davor ist nichts passiert.")

if __name__ == "__main__":
    main()
