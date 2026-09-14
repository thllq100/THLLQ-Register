/* erzeugt von bauen.py – nicht von Hand ändern */
window.THLLQ_REGISTER = {
 "erzeugt": "2026-09-14T16:02",
 "stand": {
  "n": 2,
  "aufgeloest": 1,
  "offen": 1,
  "treffer": 0.0,
  "brier": 0.1024,
  "brier_grund": 0.1024,
  "vorsprung": 0.0,
  "schwierigkeit": 0.0
 },
 "klassen": [
  {
   "lo": 0.0,
   "hi": 0.45,
   "n": 1,
   "angekuendigt": 32.0,
   "eingetreten": 0.0,
   "unten": 0.0,
   "oben": 79.34567085261071
  }
 ],
 "quartale": [
  {
   "quartal": "2026 Q3",
   "n": 1,
   "treffer": 0.0,
   "brier": 0.1024,
   "vorsprung": 0.0
  }
 ],
 "arten": [
  {
   "art": "Cash Open",
   "n": 1,
   "grundrate": 32.0,
   "angekuendigt": 32.0,
   "eingetreten": 0.0,
   "schwierigkeit": 0.0
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
   "o": null,
   "beleg": "",
   "aufgeloest": "",
   "anmerkung": ""
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
  }
 ]
};
