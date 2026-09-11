# Einmalig einrichten

```bash
cd "THLLQ Register"
git init
git add -A
git commit -m "Register angelegt, noch leer"
cp haken/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

Dann auf GitHub ein **öffentliches** Verzeichnis anlegen und verbinden:

```bash
git remote add origin https://github.com/<dein-name>/thllq-register.git
git push -u origin main
```

Öffentlich ist keine Nebensache, sondern der ganze Punkt: Der Zeitstempel taugt
nur als Nachweis, wenn ihn jeder sehen kann.

## Jede Woche

```bash
python3 neu.py          # pro Aussage einmal
python3 pruefen.py
git add aussagen/ && git commit -m "Aussagen KW ..." && git push
```

## Wenn ein Stichtag durch ist

```bash
python3 aufloesen.py
python3 pruefen.py && python3 bauen.py
git add aufloesungen/ site/ && git commit -m "Auflösungen ..." && git push
```

## Die Website

`site/index.html` und `site/register.js` gehören zusammen ins selbe Verzeichnis.
`bauen.py` schreibt `register.js` neu; die Seite liest sie beim Laden. Fehlt die
Datei, zeigt die Seite den Tag-0-Zustand statt eines Fehlers.

Bei Cloudflare Pages oder Netlify als Veröffentlichungsverzeichnis `site/`
angeben — dann ist die Seite nach jedem Push aktuell.
