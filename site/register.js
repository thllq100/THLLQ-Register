/* erzeugt von bauen.py – nicht von Hand ändern */
window.THLLQ_REGISTER = {
 "erzeugt": "2026-09-19T12:53",
 "stand": {
  "n": 4,
  "aufgeloest": 4,
  "offen": 0,
  "taeglich": {
   "seit": "2026-09-14",
   "handelstage": 5,
   "aussagen": 3,
   "ausgelassen": 2
  },
  "treffer": 50.0,
  "brier": 0.33935,
  "brier_grund": 0.2133,
  "vorsprung": -59.095171120487564,
  "schwierigkeit": 12.5
 },
 "klassen": [
  {
   "lo": 0.0,
   "hi": 0.45,
   "n": 2,
   "angekuendigt": 28.500000000000004,
   "eingetreten": 50.0,
   "unten": 9.452865480086615,
   "oben": 90.54713451991339
  },
  {
   "lo": 0.55,
   "hi": 0.65,
   "n": 1,
   "angekuendigt": 55.00000000000001,
   "eingetreten": 100.0,
   "unten": 20.654329147389294,
   "oben": 100.0
  },
  {
   "lo": 0.65,
   "hi": 0.8,
   "n": 1,
   "angekuendigt": 70.0,
   "eingetreten": 0.0,
   "unten": 0.0,
   "oben": 79.34567085261071
  }
 ],
 "quartale": [
  {
   "quartal": "2026 Q3",
   "n": 4,
   "treffer": 50.0,
   "brier": 0.33935,
   "vorsprung": -59.095171120487564
  }
 ],
 "arten": [
  {
   "art": "Stimmungsindikatoren",
   "n": 1,
   "grundrate": 50.0,
   "angekuendigt": 55.00000000000001,
   "eingetreten": 100.0,
   "schwierigkeit": 5.000000000000004
  },
  {
   "art": "Cash Open",
   "n": 3,
   "grundrate": 45.333333333333336,
   "angekuendigt": 42.333333333333336,
   "eingetreten": 33.33333333333333,
   "schwierigkeit": 15.0
  }
 ],
 "aussagen": [
  {
   "id": "2026-09-12-zew-september",
   "frage": "Liegt der ZEW-Index der Konjunkturerwartungen für Deutschland im September 2026 über der Konsensschätzung?",
   "p": 0.55,
   "grundrate": 0.5,
   "art": "stimmung",
   "aufgestellt": "2026-09-12T11:21",
   "stichtag": "2026-09-15T11:00",
   "regel": "Eingetreten, wenn der vom ZEW am 15.09.2026 um 11:00 Uhr veröffentlichte Saldo der Konjunkturerwartungen für Deutschland über 34,0 Punkten liegt. Exakt 34,0 zählt als nicht eingetreten. Maßgeblich ist die Erstveröffentlichung; spätere Revisionen bleiben unberücksichtigt.",
   "quelle": "ZEW – Leibniz-Zentrum für Europäische Wirtschaftsforschung, Mannheim",
   "konsens": "34,0 Punkte (Trading Economics, abgerufen 12.09.2026)",
   "begruendung": "Der Konsens liegt bei 34,0 und damit fast genau auf dem Augustwert, obwohl der Index im August stark gestiegen ist. Ich glaube, dass die Prognostiker nach so einem Sprung zu vorsichtig sind und am alten Wert hängen bleiben. Dagegen spricht, dass es nach starken Anstiegen oft wieder runtergeht, und ich habe meine Vermutung noch nie nachgerechnet. Darum nur 0.55 und nicht mehr. Die Schwelle von 34,0 Punkten entspricht dem Konsens vom 12.09.2026 und bleibt unveraendert, auch wenn sich die Erwartung bis zum Stichtag verschiebt.",
   "o": 1,
   "beleg": "ZEW-Index der Konjunkturerwartungen fuer Deutschland, September 2026: 34,7 Punkte (Vormonat 34,2). Veroeffentlicht vom ZEW Mannheim am 15.09.2026 um 11:05 Uhr, uebereinstimmend gemeldet von finanzen.ch und finanznachrichten.de. Schwelle der Aussage war 34,0.",
   "aufgeloest": "2026-09-15T19:41",
   "anmerkung": "Der von mir am 12.09. notierte Konsens lag bei 34,0 (Trading Economics). Dow Jones erhob 40,0, weshalb die Presse von einer Enttaeuschung sprach. Maßgeblich ist die in der Regel genannte Schwelle."
  },
  {
   "id": "2026-09-14-open",
   "frage": "Entsteht heute zwischen 15:30 und 15:40 ein regelkonformes Setup nach Version 2.0?",
   "p": 0.32,
   "grundrate": 0.32,
   "art": "eroeffnung",
   "aufgestellt": "2026-09-14T15:06",
   "stichtag": "2026-09-14T15:40",
   "regel": "Eingetreten, wenn zwischen 15:30 und 15:40 Uhr MESZ mindestens eine M1-Kerze mindestens 8 Ticks jenseits eines vor 15:30 markierten Levels schliesst, die Richtung dem Cash-Open-Filter entspricht und der Kurs beim Schluss dieser Kerze nicht mehr als 80 Ticks von diesem Level entfernt ist. Ein Schluss exakt auf der Linie zaehlt als nicht eingetreten. Ob ich tatsaechlich eingestiegen bin, spielt keine Rolle - es zaehlen allein die Bedingungen. Massgeblich ist die Erstaufzeichnung im eigenen Chart, festgehalten im Review derselben Session; spaetere Korrekturen bleiben unberuecksichtigt.",
   "quelle": "eigener Chart, Review derselben Session",
   "konsens": "Grundrate 32%, gemessen ueber 50 Sessions (06.07.-11.09.2026)",
   "begruendung": "Der Markt hat heute mit einem Gap aus dem Wochenende eröffnet. Gaps machen die Cash Open nach meiner Erfahrung schwieriger: Der Kurs chopt im Gap, und die Levels aus der Vorbereitung liegen nicht mehr dort, wo tatsächlich gehandelt wird. Von 9:00 bis 11:00 lief eine Short-Struktur über rund 600 Ticks. Die Seite ist damit klar — Long ist für mich heute als Momentum-Trade ausgeschlossen, weil es die schwache Seite ist und dort kein tragfähiges Momentum zustande kommt. Für Short gilt die Einschränkung, dass nur ein Einstieg am Tagestief taugt, nicht am Tageshoch: Im Gap ziehen starke Ablehnungen, und ein Trend mit großen Pullbacks gibt keine sauberen Swings. Ich setze deshalb ___ statt der Grundrate von 0,32. Dagegen spricht, dass ich den Zusammenhang zwischen Gap-Eröffnungen und Setup-Häufigkeit bisher nur beobachtet und nicht gemessen habe; in meinen 50 ausgewerteten Sessions sind zu wenige Gap-Tage, um das zu belegen. Weiter von der Grundrate weg gehe ich deshalb nicht.",
   "o": 0,
   "beleg": "Kein Level im Fenster 15:30-15:40 erreicht; keine M1-Kerze schliesst 8 Ticks jenseits einer vor 15:30 markierten Linie. Belegt durch den eigenen M1-Chart NQ, aufgezeichnet im Review vom 14.09.2026.",
   "aufgeloest": "2026-09-14T16:00",
   "anmerkung": "Die 8-Tick-Schwelle dieser Regel entspricht nicht genau meinem tatsaechlichen Vorgehen; sie wird ab dem naechsten Eintrag praezisiert."
  },
  {
   "id": "2026-09-17-trend",
   "frage": "Laeuft der Nasdaq heute ab 15:30 mindestens 200 Ticks in eine Richtung, bevor er 100 Ticks in die Gegenrichtung laeuft?",
   "p": 0.25,
   "grundrate": 0.52,
   "art": "eroeffnung",
   "aufgestellt": "2026-09-17T12:20",
   "stichtag": "2026-09-17T17:00",
   "regel": "Bezugspunkt ist der Eroeffnungskurs der Minutenkerze 15:30 im Nasdaq-100-Future (NQ, fortlaufender Kontrakt, Zeitzone Europe/Berlin). Eingetreten, wenn der Kurs bis 17:00 Uhr in einer der beiden Richtungen 200 Ticks (50,00 Punkte) vom Bezugspunkt erreicht, ohne vorher in der Gegenrichtung 100 Ticks (25,00 Punkte) erreicht zu haben. Gemessen werden Hoch und Tief der Minutenkerzen; eine Beruehrung genuegt, ein Schluss ist nicht noetig. Enthaelt dieselbe Minutenkerze beide Marken, laesst sich die Reihenfolge nicht feststellen und die Richtung gilt als gescheitert. Ob ich gehandelt habe, spielt keine Rolle - es zaehlt allein der Kursverlauf. Wird bis 17:00 Uhr keine der beiden 200er-Marken erreicht, gilt die Aussage als nicht eingetreten.",
   "quelle": "Minutendaten des NQ-Future, nachpruefbar in jedem Chart",
   "konsens": "Grundrate 52% - 26 von 50 Sessions, 06.07.-11.09.2026. Vertrauensintervall 0,39 bis 0,65",
   "begruendung": "Ich gewichte die letzten Sessions staerker als die Gesamtstichprobe: In den letzten acht Handelstagen haben nur zwei die 200 Ticks erreicht, bevor 100 Ticks in die Gegenrichtung liefen - gegenueber einer gemessenen Grundrate von 0,52 ueber 50 Sessions. Dazu ist der Markt heute bereits vor 15:30 deutlich gelaufen; ich erwarte im Cash Open eher eine Akkumulation von Volumen als die Bildung neuer Extreme, also ein Verdichten statt eines frischen Impulses. Dagegen spricht zweierlei: Ein starker Vorlauf zwischen 09:00 und 15:00 veraendert die Eintrittsquote ueber alle 50 Sessions kaum - 0,56 gegen 0,48, die Vertrauensintervalle ueberlappen fast vollstaendig -, und acht Handelstage koennen einen Regimewechsel nicht von Zufall unterscheiden: das Intervall fuer 2 von 8 reicht von 0,07 bis 0,59 und enthaelt 0,52.",
   "o": 1,
   "beleg": "Bezugspunkt 29718,25 (Eroeffnung Minutenkerze 15:30). Die Marke 200 Ticks nach unten (29668,25) wurde um 15:34 erreicht. In der Gegenrichtung lief der Kurs nach 15:30 zu keinem Zeitpunkt ueber den Bezugspunkt hinaus; das hoechste Hoch im Fenster war 29718,25, die Marke +100 Ticks (29743,25) wurde nie beruehrt. Tief im Fenster 29605,50, das sind 451 Ticks unter dem Bezugspunkt. NQ M1, fortlaufender Kontrakt, Europe/Berlin.",
   "aufgeloest": "2026-09-17T18:06",
   "anmerkung": ""
  },
  {
   "id": "2026-09-18-trend",
   "frage": "Laeuft der Nasdaq heute ab 15:30 mindestens 200 Ticks in eine Richtung, bevor er 100 Ticks in die Gegenrichtung laeuft?",
   "p": 0.7,
   "grundrate": 0.52,
   "art": "eroeffnung",
   "aufgestellt": "2026-09-18T13:41",
   "stichtag": "2026-09-18T17:00",
   "regel": "Bezugspunkt ist der Eroeffnungskurs der Minutenkerze 15:30 im Nasdaq-100-Future (NQ, fortlaufender Kontrakt, Zeitzone Europe/Berlin). Eingetreten, wenn der Kurs bis 17:00 Uhr in einer der beiden Richtungen 200 Ticks (50,00 Punkte) vom Bezugspunkt erreicht, ohne vorher in der Gegenrichtung 100 Ticks (25,00 Punkte) erreicht zu haben. Gemessen werden Hoch und Tief der Minutenkerzen; eine Beruehrung genuegt, ein Schluss ist nicht noetig. Enthaelt dieselbe Minutenkerze beide Marken, laesst sich die Reihenfolge nicht feststellen und die Richtung gilt als gescheitert. Ob ich gehandelt habe, spielt keine Rolle - es zaehlt allein der Kursverlauf. Wird bis 17:00 Uhr keine der beiden 200er-Marken erreicht, gilt die Aussage als nicht eingetreten.",
   "quelle": "Minutendaten des NQ-Future, nachpruefbar in jedem Chart",
   "konsens": "Grundrate 52% - 26 von 50 Sessions, 06.07.-11.09.2026. Vertrauensintervall 0,39 bis 0,65",
   "begruendung": "Im Weekly-Volumenprofil liegt ein ausgepraegter High-Volume-Node, der heute angelaufen werden kann, und die Volatilitaet passt dazu. Freitag ist fuer mich ohnehin ein Tag mit Volatilitaet, weil zum Wochenschluss Positionen geschlossen werden. Die Session von 5:00 bis 9:00 lief durchgehend trendig, und das Volumenprofil von gestern und heute steigt, mit dem Volumen nach oben verlagert. Damit kann der Kurs heute in beide Richtungen laufen: nach oben weiter steigen oder nach unten zum grossen Volumenberg von gestern.",
   "o": 0,
   "beleg": "Bezugspunkt 29814,25 (Eroeffnung Minutenkerze 15:30). Die Marke +100 Ticks (29839,25) wurde zuerst beruehrt; damit war die Short-Richtung ausgeschieden, bevor sie ihr Ziel bei 29764,25 erreichte. Die Long-Richtung erreichte ihr Ziel bei 29864,25 nicht - das hoechste Hoch im Fenster lag bei 29844,75, also 122 Ticks ueber dem Bezugspunkt. Tief im Fenster 29692,75, das sind 486 Ticks unter dem Bezugspunkt. Keine der beiden 200er-Marken wurde regelkonform erreicht. NQ M1, fortlaufender Kontrakt, Europe/Berlin.",
   "aufgeloest": "2026-09-18T19:05",
   "anmerkung": "486 Ticks Bewegung und trotzdem nicht eingetreten: Die Gegenbewegung von 122 Ticks kam zuerst. Gefragt ist ein sauberer Lauf ab der Eroeffnung, nicht die Groesse der Bewegung."
  }
 ]
};
