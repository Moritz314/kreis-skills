# Prüfung zum Modul Anti-KI

Befehle und Schnipsel zu `regeln/anti-ki.md` (AK01 bis AK26). Ein Treffer ist eine Frage an den Entwurf, kein Urteil. Vor den Befehlen setzen:

```bash
D="<Ordner der Seite>"
INC=(--include='*.html' --include='*.css' --include='*.scss' --include='*.js' --include='*.jsx' --include='*.ts' --include='*.tsx' --include='*.vue' --include='*.svelte' --include='*.astro')
```

Den Quelltext-Scan übernimmt `werkzeuge/scan_antipatterns.py` (Befehl `audit`); er kennt keine Radius-Regel, die Punkte zu AK01 bis AK03 ersetzt er nicht.

## Befehle je Regel

| Regel | Befehl |
|---|---|
| AK01 Radien zählen | `grep -rhoE 'border-radius:\s*[^;}"]+' "${INC[@]}" "$D" \| sort \| uniq -c \| sort -rn` (S23: höchstens drei Werte); Tailwind-Standard: `grep -rnoE '\brounded-(lg\|xl\|2xl\|3xl\|4xl)\b' "${INC[@]}" "$D"`; Schnipsel R |
| AK03 Karten-Reihe | `grep -rnE 'grid-template-columns:\s*repeat\((3\|4),\s*(1fr\|minmax\(0,\s*1fr\))\)\|\b(sm:\|md:\|lg:)?grid-cols-(3\|4)\b' "${INC[@]}" "$D"`, dann prüfen, ob die Kinder dieselbe Struktur haben |
| AK04 Bento | `grep -rnE 'grid-auto-flow:\s*dense\|(col\|row)-span-[2-4]\|grid-(column\|row):\s*span\s*[2-4]' "${INC[@]}" "$D"` |
| AK05 Geister-Karte | Schnipsel S |
| AK06 Schatten | `grep -rnE 'rgba?\(\s*0\s*,\s*0\s*,\s*0\s*,\|rgb\(0 0 0 /\|\bshadow-(sm\|md\|lg\|xl\|2xl)\b' "${INC[@]}" "$D"`; alle: `grep -rhoE 'box-shadow:\s*[^;}"]+' "${INC[@]}" "$D" \| sort \| uniq -c` |
| AK07, AK12 Icons, Emoji | `grep -rnP '[\x{1F300}-\x{1FAFF}\x{2600}-\x{27BF}]' "${INC[@]}" "$D"`; `grep -rnoiE 'lucide\|(Sparkles\|Zap\|Shield\|Rocket)\b' "${INC[@]}" "$D"` |
| AK08 Glühen, Glas | `grep -rnE 'box-shadow:\s*0(px)?\s+0(px)?\s+[1-9][0-9]*px\|text-shadow\|backdrop-filter\|backdrop-blur\|filter:\s*blur' "${INC[@]}" "$D"` |
| AK09 Palette | `grep -rnoiE '#(6366f1\|4f46e5\|8b5cf6\|7c3aed\|a855f7\|9333ea\|10b981\|06b6d4\|d97757\|f4f1ea\|0f172a\|09090b\|18181b)\b' "${INC[@]}" "$D"`; `grep -rnoE '\b(bg\|text\|from\|to\|via\|border)-(indigo\|violet\|purple)-[0-9]{3}\b' "${INC[@]}" "$D"` |
| AK11 Schrift | `grep -rnoiE "font-family:\s*[^;}\"]+\|family=[A-Za-z+]+" "${INC[@]}" "$D" \| sort \| uniq -c`; Schnipsel F |
| AK13, AK14 Verläufe | `grep -rnE '(linear\|radial\|conic)-gradient\|bg-gradient-to-\|\bfrom-[a-z]+-[0-9]{2,3}\b' "${INC[@]}" "$D"`; Verlaufstext: `grep -rnE 'background-clip:\s*text\|bg-clip-text\|text-fill-color:\s*transparent' "${INC[@]}" "$D"`; jeden Treffer als Linie, Maske, Foto oder Fläche einordnen |
| AK15 Akzentwort | Blick auf `em`, `i`, `span` in `h1` und `h2` |
| AK17 Hero | Bildschirmfoto der ersten Ansicht bei 1440 px und 440 px; `grep -rnoiE '#(ff5f57\|febc2e\|28c840)\b' "${INC[@]}" "$D"` |
| AK18 Aufbau | `grep -noE '<section[^>]*>' "$D"/*.html`, Abschnitte gegen die Liste zählen |
| AK19 Rhythmus | Schnipsel A; Tailwind: `grep -rhoE '\b(p\|py\|pt\|pb\|m\|my\|mt\|mb\|gap\|space-y)-[0-9]+\b' "${INC[@]}" "$D" \| sort \| uniq -c` (stammen alle aus 4, 6, 8, ist es das Warnzeichen) |
| Einheits-Einblendung (BE03) | `grep -rnoE 'data-aos\|fade-?(in-?)?up\|animate-fade\|whileInView\|translateY\((1[0-9]\|2[0-9]\|3[0-9]\|40)px\)' "${INC[@]}" "$D" \| wc -l`; über 3 Treffer prüfen |
| AK23 Wörter | `grep -rnoiE '\b(nahtlos\w*\|ganzheitlich\w*\|maßgeschneidert\w*\|innovativ\w*\|revolution\w*\|bahnbrechend\w*\|wegweisend\w*\|zukunftssicher\w*\|Mehrwert\|Synergie\w*\|Komplettlösung\w*\|Rundum-sorglos\|All-in-One\|Next[ -]Level\|Game[ -]Changer\|State of the Art\|entfessel\w*\|transformier\w*\|mühelos\|Handumdrehen\|spielend leicht\|eintauchen\|neu gedacht\|Ihr Partner für\|Willkommen bei\|Wir bei\|schnelllebig\w*\|Bereit für\|mehr als nur\|Stell dir vor\|Kurz gesagt\|Herzstück\|seamless\w*\|unlock\w*\|elevat\w*\|supercharg\w*\|streamlin\w*\|empower\w*\|leverag\w*\|delve\w*\|cutting-edge\|unleash\w*\|tapestry\|world-class\|look no further)\b' "$D" --include='*.html' --include='*.jsx' --include='*.tsx' --include='*.vue' --include='*.svelte' --include='*.astro' --include='*.md'`; Muster: `grep -rnoiE 'nicht nur\b.{0,60}\bsondern auch\|es ist nicht\b.{0,40}\bes ist\|egal ob\b.{0,60}\boder\|whether you.re' "$D" --include='*.html'`; Gedankenstriche: `grep -rnP '[\x{2013}\x{2014}]' "$D" --include='*.html'` (Bereiche wie 8–10 Uhr nach S29 ausnehmen) |

## Schnipsel für die Konsole der gerenderten Seite

Bei 1440 px und im Handymaß ausführen; mit Playwright als `page.evaluate(...)`.

**R: Radius zu Elementart.** Jede Zeile einer Ebene zuordnen (Behälter, Steuerelement, Medium); höchstens drei Werte (S23); verschachtelt nach AK01.

```js
(() => { const m = {}; for (const el of document.querySelectorAll('body *')) { const r = getComputedStyle(el).borderTopLeftRadius; if (!r || r === '0px') continue; const k = el.tagName.toLowerCase() + (typeof el.className === 'string' && el.className ? '.' + el.className.trim().split(/\s+/)[0] : ''); (m[r] ??= new Set()).add(k); } return Object.fromEntries(Object.entries(m).map(([r, s]) => [r, [...s].slice(0, 12).join(' ')])); })()
```

**S: Geister-Karten (AK05).** Erwartet: leere Liste, außer schwebenden Ebenen.

```js
[...document.querySelectorAll('body *')].filter(el => { const s = getComputedStyle(el); const bw = parseFloat(s.borderTopWidth); const blur = [...s.boxShadow.matchAll(/(-?\d+(?:\.\d+)?)px\s+(-?\d+(?:\.\d+)?)px\s+(\d+(?:\.\d+)?)px/g)].some(m => +m[3] >= 8); return bw >= 1 && s.borderTopStyle !== 'none' && blur; }).map(el => el.tagName + '.' + el.className)
```

**F: Schriften (AK11).** `benutzt` gegen `geladen` halten.

```js
({ benutzt: [...new Set([...document.querySelectorAll('body *')].map(e => getComputedStyle(e).fontFamily.split(',')[0].trim()))], geladen: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight) })
```

**A: Abschnittsabstände (AK19).** Websites: `werte` mit mindestens zwei Einträgen und `verhaeltnis` ab 1,4.

```js
(() => { const v = [...document.querySelectorAll('main > *, section, [data-surface]')].map(s => { const c = getComputedStyle(s); return Math.round(parseFloat(c.paddingTop) + parseFloat(c.marginTop)); }).filter(x => x > 0); const u = [...new Set(v)].sort((a, b) => a - b); return { werte: u, verhaeltnis: u.length ? +(u.at(-1) / u[0]).toFixed(2) : null }; })()
```
