#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pruefen.py — prüft das Register, bevor etwas veröffentlicht wird.

Was hier geprüft wird, ist genau das, was dir später jemand vorwerfen könnte:

  * Fehlt eine Auflösungsregel, ist sie zu dünn, oder nennt sie keine Quelle?
  * Liegt der Stichtag vor dem Aufstellen? (Dann wüsste man das Ergebnis schon.)
  * Wurde eine bereits veröffentlichte Datei nachträglich geändert?
  * Gibt es eine Auflösung zu einer Aussage, deren Stichtag noch nicht da ist?
  * Steht irgendwo eine Wahrscheinlichkeit von 0 oder 100 Prozent?

Aufruf:   python3 pruefen.py
Rückgabe: 0 wenn alles sauber, sonst 1. Taugt damit als Git-Hook und für CI.

Ohne Fremdbibliotheken. Die Schema-Dateien im Ordner schema/ beschreiben dasselbe
noch einmal maschinenlesbar, für Redakteure und spätere Werkzeuge.
"""

import json, os, re, subprocess, sys
from datetime import datetime

HIER = os.path.dirname(os.path.abspath(__file__))
AUS  = os.path.join(HIER, "aussagen")
AUF  = os.path.join(HIER, "aufloesungen")

ARTEN = {"vpi", "arbeitsmarkt", "stimmung", "quartalszahlen", "notenbank",
         "eroeffnung", "sonstiges"}
ID_MUSTER = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+$")
ZEIT_MUSTER = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$")

fehler, warnungen = [], []
def fehlt(datei, text): fehler.append(f"{datei}: {text}")
def warnt(datei, text): warnungen.append(f"{datei}: {text}")

def zeit(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M")

def lies(pfad):
    try:
        with open(pfad, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        fehlt(os.path.basename(pfad), f"kein gültiges JSON – {e}")
        return None

# ---------------------------------------------------------------- Aussagen

def pruefe_aussage(pfad):
    name = os.path.basename(pfad)
    d = lies(pfad)
    if d is None:
        return None

    pflicht = ["id", "aufgestellt", "stichtag", "frage", "p", "aufloesungsregel", "quelle", "art"]
    for k in pflicht:
        if k not in d or d[k] in ("", None):
            fehlt(name, f"Pflichtangabe fehlt: {k}")
    if fehler and any(name in f for f in fehler[-len(pflicht):]):
        return None

    if d["id"] != name[:-5]:
        fehlt(name, f"id ({d['id']}) passt nicht zum Dateinamen")
    if not ID_MUSTER.match(d["id"]):
        fehlt(name, "id muss JJJJ-MM-TT-kurzname sein, klein geschrieben")

    for k in ("aufgestellt", "stichtag"):
        if not ZEIT_MUSTER.match(str(d[k])):
            fehlt(name, f"{k} muss JJJJ-MM-TTThh:mm sein")
            return None

    auf, sti = zeit(d["aufgestellt"]), zeit(d["stichtag"])
    if sti <= auf:
        fehlt(name, "Stichtag liegt nicht nach dem Aufstellen – so wäre das Ergebnis schon bekannt")
    if not d["id"].startswith(d["aufgestellt"][:10]):
        fehlt(name, "das Datum in der id stimmt nicht mit 'aufgestellt' überein")

    p = d["p"]
    if not isinstance(p, (int, float)) or not (0.01 <= p <= 0.99):
        fehlt(name, f"p muss zwischen 0,01 und 0,99 liegen (ist {p}) – nie 0 und nie 1")
    g = d.get("grundrate", 0.5)
    if not (0.01 <= g <= 0.99):
        fehlt(name, f"grundrate muss zwischen 0,01 und 0,99 liegen (ist {g})")

    if d["art"] not in ARTEN:
        fehlt(name, f"unbekannte art '{d['art']}' – erlaubt: {', '.join(sorted(ARTEN))}")

    regel = d["aufloesungsregel"]
    if len(regel) < 60:
        fehlt(name, "die Auflösungsregel ist zu knapp, um sie später eindeutig anzuwenden")
    if not re.search(r"\d", regel):
        warnt(name, "in der Auflösungsregel steht keine Zahl – ist die Schwelle wirklich eindeutig?")
    if not re.search(r"gleich|exakt|identisch|Gleichstand", regel, re.I):
        warnt(name, "die Regel sagt nichts über Gleichstand – das ist der häufigste Streitfall")
    if not re.search(r"revision|erstver|vorläufig|Schnellschätzung", regel, re.I):
        warnt(name, "die Regel sagt nichts über spätere Revisionen der Zahl")
    if len(d["frage"]) < 25:
        fehlt(name, "die Frage ist zu knapp formuliert")
    if "?" not in d["frage"]:
        warnt(name, "die Frage endet nicht auf ein Fragezeichen – ist sie mit ja/nein beantwortbar?")

    d["_datei"] = name
    return d

# ---------------------------------------------------------------- Auflösungen

def pruefe_aufloesung(pfad, aussagen):
    name = os.path.basename(pfad)
    d = lies(pfad)
    if d is None:
        return None
    for k in ("id", "aufgeloest", "eingetreten", "beleg"):
        if k not in d:
            fehlt(name, f"Pflichtangabe fehlt: {k}")
            return None
    if d["id"] != name[:-5]:
        fehlt(name, "id passt nicht zum Dateinamen")
    if d["id"] not in aussagen:
        fehlt(name, "es gibt keine Aussage mit dieser id")
        return None
    if not isinstance(d["eingetreten"], bool):
        fehlt(name, "'eingetreten' muss true oder false sein – kein 'teilweise'")
    if len(str(d.get("beleg", ""))) < 15:
        fehlt(name, "der Beleg ist zu dünn: Welche Zahl wurde veröffentlicht, und wo steht sie?")
    if not ZEIT_MUSTER.match(str(d["aufgeloest"])):
        fehlt(name, "aufgeloest muss JJJJ-MM-TTThh:mm sein")
        return None
    if zeit(d["aufgeloest"]) < zeit(aussagen[d["id"]]["stichtag"]):
        fehlt(name, "aufgelöst vor dem Stichtag – das darf nicht sein")
    d["_datei"] = name
    return d

# ---------------------------------------------------------------- Unveränderlichkeit

def git_da():
    try:
        subprocess.run(["git", "rev-parse", "--git-dir"], cwd=HIER,
                       capture_output=True, check=True)
        return True
    except Exception:
        return False

def pruefe_unveraendert():
    """Regel 2: Eine eingetragene Zeile wird nie geändert, nur ergänzt.

    Eine Datei, die nach ihrem ersten Commit noch einmal geändert wurde, ist genau
    das, was der Nachweis ausschließen soll. Git weiß das – also fragen wir Git.
    """
    if not git_da():
        warnungen.append("kein Git-Verzeichnis – die Unveränderlichkeit kann nicht geprüft werden")
        return
    roh = subprocess.run(
        ["git", "log", "--diff-filter=M", "--name-only", "--pretty=format:",
         "--", "aussagen", "aufloesungen"],
        cwd=HIER, capture_output=True, text=True).stdout
    geaendert = sorted({z.strip() for z in roh.splitlines() if z.strip()})
    for g in geaendert:
        fehler.append(f"{g}: wurde nach der Veröffentlichung geändert – das verstößt gegen Regel 2")
    # nicht eingecheckte Änderungen an bereits veröffentlichten Dateien
    roh2 = subprocess.run(["git", "status", "--porcelain", "--", "aussagen", "aufloesungen"],
                          cwd=HIER, capture_output=True, text=True).stdout
    for z in roh2.splitlines():
        status, datei = z[:2], z[3:].strip()
        if status.strip() in ("M", "D", "MM", "AM", "R"):
            fehler.append(f"{datei}: geändert oder gelöscht, aber schon veröffentlicht (Status {status.strip()})")

# ---------------------------------------------------------------- Hauptlauf

def main():
    os.makedirs(AUS, exist_ok=True)
    os.makedirs(AUF, exist_ok=True)

    dateien = sorted(f for f in os.listdir(AUS) if f.endswith(".json"))
    aussagen = {}
    for f in dateien:
        d = pruefe_aussage(os.path.join(AUS, f))
        if d:
            if d["id"] in aussagen:
                fehlt(f, "diese id gibt es doppelt")
            aussagen[d["id"]] = d

    aufl = {}
    for f in sorted(x for x in os.listdir(AUF) if x.endswith(".json")):
        d = pruefe_aufloesung(os.path.join(AUF, f), aussagen)
        if d:
            aufl[d["id"]] = d

    # Offene Aussagen, deren Stichtag durch ist: erinnern, nicht bemängeln
    jetzt = datetime.now()
    for i, a in aussagen.items():
        if i not in aufl and zeit(a["stichtag"]) < jetzt:
            warnungen.append(f"{a['_datei']}: Stichtag ist vorbei, Auflösung fehlt noch")

    pruefe_unveraendert()

    print(f"Aussagen: {len(aussagen)}   Auflösungen: {len(aufl)}   "
          f"offen: {len(aussagen) - len(aufl)}")
    if warnungen:
        print("\nHinweise (kein Abbruch):")
        for w in warnungen:
            print("  ~ " + w)
    if fehler:
        print("\nFehler:")
        for f in fehler:
            print("  ! " + f)
        print(f"\n{len(fehler)} Fehler. Nichts veröffentlichen, bevor die weg sind.")
        return 1
    print("\nRegister in Ordnung.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
