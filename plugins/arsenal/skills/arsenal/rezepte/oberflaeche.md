# Rezept: Bewegung in Anwendungen

Bedienteile, die wachsen, Leisten, die auf- und zugehen, Seitenblätter, Zustandsfarben, Goo-Filter und Überschwingen für die Art `anwendung` (Modul `software`), ab `bewegung: 1`. Regeln: Stamm S16, S17, S42 bis S51, Modul `bewegung` BE05, BE23. Code aus der Quelle übernommen und an den Stamm angeglichen, nicht neu im Browser geprüft.

Für alle Muster gilt: Dauern und Kurven aus der Tabelle im Stamm (S42 bis S45), als Variablen aus dem MASK (`--dauer-*`, `--kurve-rein`, `--kurve-raus`, `--kurve-ort`). Was wächst, verschiebt kein Layout (S51): Es legt sich über die Nachbarn, oder die Nachbarn weichen per `transform` aus. Tabs, Ansichtswechsel, Befehlspalette, Menüs und Kontextmenüs öffnen sofort, ohne diese Muster (S50).

## Punkt wird Pille

Ein kleines Bedienteil wächst bei Hover, Fokus oder Aktivierung zur beschrifteten Pille. Vorbild: die Ampelknöpfe am Apple-Fenster.

Bauweise in zwei Ebenen:
- **Grund:** wird mit `clip-path: inset(… round 999px)` aufgedeckt. Kein `scaleX`: Er macht aus runden Enden Ellipsen. Kein `width`: Das ist Layout und schiebt die Nachbarn.
- **Beschriftung:** eigene Ebene, nie in einem geclippten, skalierten oder gefilterten Teilbaum, sonst verliert der Text die Subpixel-Glättung. Bewegt wird nur `opacity`.

Die offene Breite ist eine Messung nach `document.fonts.ready`, nie geschätzt. Der Platz im Layout ist der geschlossene Punkt.

Dauer: Die Hover-Rückmeldung (Farbe, Schatten) bleibt in der Zeile „Rückmeldung“ der Tabelle. Der Aufbau der Pille ist ein Overlay, er nimmt die Zeile „kleine Wege“.

Kosten: `clip-path` mit `round` malt die Fläche jedes Bild neu auf der CPU (gemessen 41 bis 45 Paint-Ereignisse je Pille, 0 bei `inset()` ohne `round`). Fläche klein halten, die Zahl gleichzeitig wachsender Pillen deckeln, messen nach BE23.

Wechselt das Element wirklich seinen Platz im Layout (Karte wird Detail, Listeneintrag klappt im Fluss auf), ist Aufdecken falsch: FLIP mit `transform` (S46).

**Nachbarn weichen aus.** In einer Reihe rücken die Nachbarn per `transform` um die Mehrbreite zur Seite. Läge ein Nachbar ganz unter der Pille, bekommt er `inert`. Die Pille nimmt Zeigerereignisse an und reicht keinen Klick durch. `pointer-events: auto` erst in `transitionend` setzen, damit ein schneller Zeiger mitten in der Bewegung nicht durchklickt.

**Telefon.** Ohne Hover ist der Punkt ein gefüllter Kreis von 28 bis 32 px mit Symbol. Tippziel nach S16 als durchsichtiger Rand um den Kreis; nach WCAG 2.5.8 überlappt kein anderes Ziel im Umkreis von 24 px. Die Beschriftung steht immer auch als `aria-label`. Schließen bei `pointerdown` außerhalb, nicht beim zweiten Tipp. Neben einem Titel behält der Titel mindestens die halbe Kopfbreite, auch bei voller Pille. Hover nur unter `(hover: hover)` (TE13).

```html
<button class="ctl" type="button" data-open="false" aria-label="Veröffentlichen">
  <span class="ctl__ground" aria-hidden="true"></span>
  <span class="ctl__label">Veröffentlichen</span>
</button>
```

```css
.ctl {
  position: relative;
  display: inline-block;
  inline-size: var(--ctl-dot, 1.5rem);   /* the footprint the layout reserves */
  block-size: var(--ctl-dot, 1.5rem);
}
.ctl__ground {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: var(--ctl-open, 1.5rem);  /* set from JS after fonts are ready */
  background: var(--role-confirm-surface);
  border-radius: 999px;
  clip-path: inset(0 calc(var(--ctl-open) - var(--ctl-dot)) 0 0 round 999px);
  transition: clip-path var(--dauer-klein-raus) var(--kurve-raus);   /* closing */
}
.ctl[data-open="true"] .ctl__ground {
  clip-path: inset(0 0 0 0 round 999px);
  transition: clip-path var(--dauer-klein) var(--kurve-rein);        /* opening */
}

.ctl__label {                            /* own layer: no filter, no clip, no scale */
  position: relative;
  opacity: 0;
  transition: opacity var(--dauer-rueckmeldung) var(--kurve-raus);
}
.ctl[data-open="true"] .ctl__label {
  opacity: 1;
  transition: opacity var(--dauer-rueckmeldung) var(--kurve-rein);
}
```

```js
// The open width is a measurement, never a guess: a webfont swap changes it.
await document.fonts.ready
const ground = ctl.querySelector('.ctl__ground')
const label = ctl.querySelector('.ctl__label')
const w = Math.ceil(label.getBoundingClientRect().width) + PAD_INLINE * 2
ctl.style.setProperty('--ctl-open', `${w}px`)
// Re-measure on a locale change or a dynamic label change, not on every resize.

// Neighbours make way instead of being covered.
function makeWay(neighbours, open) {
  const shift = open ? w - dotWidth : 0
  neighbours.forEach((n) => { n.style.transform = `translateX(${shift}px)` })
}
// Hit area only once the shape really covers it.
ground.addEventListener('transitionend', () => {
  ground.style.pointerEvents = ctl.dataset.open === 'true' ? 'auto' : ''
})
```

Probe: `elementFromPoint()` an einem festen Punkt auf dem Weg der Pille liefert vor, während und nach dem Wachsen dasselbe Bedienteil. Layoutverschiebung 0. Tippziel im Box-Modell mindestens 44 × 44 px, zugänglicher Name in jedem Zustand nicht leer.

## Leisten auf und zu

Filter-, Befehls- oder Sendeleiste behalten ihren Platz in fester Höhe. Der Grund wächst als Overlay, nur über `clip-path: inset()` auf der Ebene mit dem Radius. Der Inhalt erscheint nur über `opacity`, ohne Skalierung.

**Falle:** kein `scaleY` auf derselben Ebene. `clip-path` wirkt in den unverformten Koordinaten, die Verformung staucht danach das Ergebnis: Geschlossen wird die Leiste `bar-min² / bar-max` hoch statt `bar-min`, und der Radius wird zur Ellipse. Ein Stauch-Effekt gehört auf eine eigene innere Ebene ohne Radius.

Zeitverhalten:
- Öffnen nach 120 ms Hover-Absicht; ein `pointerout` davor bricht ab. Nur für `pointerType` `mouse` und `pen`, denn `pointerover` feuert auch bei Touch direkt vor dem Klick.
- Klick, Tipp und `Tab` öffnen sofort. Öffnet die Leiste per Tastenkürzel oder ist sie die Befehlspalette: Endzustand ohne Übergang (S50).
- Schließen nach 400 ms; jedes neue `pointerover` bricht ab. Fokus in der Leiste oder ein nicht leeres Feld sperren das Schließen.
- `Escape` schließt und gibt den Fokus an ein benanntes Ziel, nie an einen vermuteten Auslöser (sonst `.focus()` auf `undefined`).
- Ungesendeter Entwurf zeigt sich in der geschlossenen Leiste (Punkt, gekürzte erste Zeile).

Deckt der offene Inhalt mehr als etwa ein Drittel der Fensterhöhe, ist es ein Seitenblatt (nächster Abschnitt). Nie zwei per Hover geöffnete Overlays in derselben Ecke: Die Schließzeiten streiten.

```css
.bar { position: relative; block-size: var(--bar-min); }  /* slot never changes */
.bar__ground {
  position: absolute; inset-inline: 0; inset-block-start: 0;
  block-size: var(--bar-max);          /* full height, overlays what is below */
  background: var(--surface-raised);
  border-radius: var(--radius-m);
  clip-path: inset(0 0 calc(var(--bar-max) - var(--bar-min)) 0 round var(--radius-m));
  transition: clip-path var(--dauer-klein-raus) var(--kurve-raus);
}
.bar[data-open="true"] .bar__ground {
  clip-path: inset(0 round var(--radius-m));
  transition: clip-path var(--dauer-klein) var(--kurve-rein);
}
.bar__content { position: relative; opacity: 0; transition: opacity var(--dauer-rueckmeldung) var(--kurve-raus); }
.bar[data-open="true"] .bar__content { opacity: 1; transition: opacity var(--dauer-rueckmeldung) var(--kurve-rein); }
.bar[data-instant] .bar__ground,
.bar[data-instant] .bar__content { transition: none; }   /* shortcut or command palette: instant (S50) */
```

```js
const OPEN_DELAY = 120
const CLOSE_DELAY = 400
const ground = bar.querySelector('.bar__ground')
const input = bar.querySelector('input, textarea')
let openTimer = null
let closeTimer = null
let lastOpener = null   // an outside trigger; stays null when opened by hover, tap or Tab

const open  = (trigger = null) => { clearTimeout(closeTimer); if (trigger) lastOpener = trigger; bar.dataset.open = 'true' }
const close = () => { if (isLocked()) return; bar.dataset.open = 'false'; lastOpener = null }
const isLocked = () => bar.contains(document.activeElement) || input.value.trim() !== ''

bar.addEventListener('pointerover', (e) => {
  if (e.pointerType !== 'mouse' && e.pointerType !== 'pen') return   // touch never hover-opens
  clearTimeout(closeTimer)
  openTimer = setTimeout(() => open(), OPEN_DELAY)
})
bar.addEventListener('pointerout', () => clearTimeout(openTimer))   // leaving before intent fires cancels it
bar.addEventListener('pointerleave', () => {
  clearTimeout(closeTimer)
  closeTimer = setTimeout(close, CLOSE_DELAY)
})
ground.addEventListener('pointerup', (e) => {
  if (e.pointerType === 'touch') open()            // tap opens immediately
})
bar.addEventListener('focusin', () => open())      // Tab in opens immediately, no intent delay
bar.addEventListener('focusout', (e) => {          // leaving by keyboard closes
  if (!bar.contains(e.relatedTarget)) close()
})
bar.addEventListener('keydown', (e) => {
  if (e.key !== 'Escape') return
  bar.dataset.open = 'false'
  ;(lastOpener ?? bar.nextElementSibling)?.focus()   // named target, never .focus() on an assumed opener
})
```

Probe: Beim Auf und Zu bleibt die `y`-Lage des ersten Elements unter der Leiste gleich, CLS 0. Geschlossen ist `bar__ground.getBoundingClientRect().height` genau `bar-min`. Ein Zeigerstrich, der binnen 120 ms wieder geht, ändert `data-open` nie. Raus und binnen 400 ms zurück: Die Leiste beginnt nie zu schließen. Nach `Escape` steht der Fokus auf dem Ziel, kein Fehler in der Konsole.

## Drei Gerüste: Seitenblatt, Liste mit Detail, Leiste am Rand

Erst benennen, dann bauen: Der Fokusvertrag hängt am Muster und lässt sich nicht nachrüsten.

| Muster | Fokusvertrag |
|---|---|
| **Seitenblatt**, gleitet über die Fläche | Vorher wählen. **Modal:** `role="dialog"`, `aria-modal="true"`, der Rest `inert`, Fokus gefangen; Klick außerhalb schließt. **Nicht modal:** kein `aria-modal`, kein `inert`, `Tab` darf hinaus. Eine Falle ohne `aria-modal` verletzt ARIA. Beide: `Escape` schließt, Fokus zurück an den Auslöser. |
| **Liste mit Detail** | Keine Falle, beide Bereiche per `Tab` in DOM-Reihenfolge. Ein neuer Eintrag tauscht das Detail sofort, ohne Übergang (S50), schließt nichts und setzt den Fokus auf die Detailüberschrift (`tabindex="-1"`, `focus()`). `Escape` im Detail führt zum gewählten Eintrag zurück. |
| **Leiste am Rand** (Rail) | Keine Falle, stiehlt nie den Fokus. Aufklappen zu Beschriftungen ist die Pille oben, je Eintrag. `Escape` klappt zu, ohne den Fokus zu bewegen. |

Das Blatt kommt mit `transform: translateX()` aus seiner Kante (S43), Weg und Kurve nach der Zeile „große Flächen“. Es drückt die Hauptspalte nie zusammen. Das Detail hat je Breite eine feste Spurbreite, die Rail reserviert ihre geschlossene Breite.

Breitenstufen (mehr sind erlaubt, weniger nicht):
- **unter 720 px:** eine Spalte, Blätter volle Breite, Liste mit Detail wird Liste, dann Detail mit Zurück; die Rail wird Leiste unten oder Menü.
- **720 bis 1024 px:** Blatt als Overlay fester Breite, Liste mit Detail nur bei schmalem Detail, Rail nur mit Symbolen.
- **ab 1024 px:** alle drei voll, Rail darf Beschriftungen zeigen.

Muss man den Blattinhalt mit der Fläche dahinter vergleichen, ist es Liste mit Detail.

```js
// Side sheet, the parts that are actually a contract.
let opener = null

function openSheet(trigger, { modal = true } = {}) {
  opener = trigger
  sheet.hidden = false
  if (modal) {
    sheet.setAttribute('aria-modal', 'true')
    sheet.setAttribute('role', 'dialog')
    for (const el of document.querySelectorAll('body > :not(#sheet-root)')) el.inert = true
  }
  sheet.querySelector('[autofocus], button, [href], input, select, textarea')?.focus()
}
function closeSheet() {
  const wasModal = sheet.getAttribute('aria-modal') === 'true'
  sheet.hidden = true
  sheet.removeAttribute('aria-modal')
  if (wasModal) for (const el of document.querySelectorAll('[inert]')) el.inert = false
  opener?.focus()                     // return, never drop focus to <body>
}
sheet.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeSheet() })
scrim?.addEventListener('pointerdown', closeSheet)   // only the modal variant renders a scrim to click
```

Probe: `document.activeElement` erfüllt den Vertrag nach Öffnen, nach einem `Tab`-Durchlauf, nach `Escape` und nach Klick außerhalb. Modal: Ein voller `Tab`-Durchlauf verlässt das Blatt nie. Nicht modal: `Tab` vom letzten Ziel im Blatt landet auf dem nächsten Ziel dahinter. Die Breite der Hauptspalte ist offen und geschlossen gleich.

## Zustandsfarben: drei bis fünf Rollen

Rollen zur Auswahl: Eingabe und Bestätigung, Optionen, Hinweise, Abbrechen und Schließen, Automatik (was das System selbst tat), Neutralgrau für Vergangenes (erledigt, abgelaufen, archiviert). Jede Rolle hat genau drei Stufen in OKLCH (S30): **Fläche** (wenig Chroma, Grund von Chips, Zeilen, Bannern), **Linie** (Rand, Trenner, Symbolstrich), **voll** (gefüllter Knopf, Punkt, Balken). Kontrast je Rolle und je Thema nach S14, Bedeutung nie allein über Farbe (S15). Farbstrategie: SW16. Läuft ein Projekt mit Website davor und Anwendung dahinter, gibt es zwei Paletten; das steht im MASK.

**Gelb ist die Ausnahme.** Ein Gelb, das weiße Schrift trägt, wirkt braun oder oliv. Die Hinweis-Rolle bekommt ein helles, sattes Gelb mit dunkler Schrift. Sie ist die einzige Rolle mit umgekehrter Schriftpolarität.

```css
:root {
  /* Confirmation role, three steps. Hues and chroma are examples. */
  --role-confirm-surface: oklch(0.96 0.03 150);
  --role-confirm-line:    oklch(0.72 0.11 150);
  --role-confirm-solid:   oklch(0.55 0.16 150);
  /* Notice role: the yellow exception, dark text on a bright chip. */
  --role-notice-solid:    oklch(0.86 0.17 95);
  --role-notice-on-solid: oklch(0.25 0.03 95);
}
```

Probe: jede Rollenfläche mit Text in beiden Themen gemessen; Graustufenbild unterscheidet jeden Zustand; kein Bauteil nutzt einen Farbwert außerhalb der Rollen.

## Goo-Filter (SVG)

`feGaussianBlur`, danach `feColorMatrix`, die den Alpharand wieder härtet. Zwei runde Formen, die sich nähern, wölben sich und fließen zusammen. Das zeigt: Zwei Dinge werden eins (ein Bedienteil teilt sich in Optionen, Punkte werden ein Balken). Nur auf der Formebene und nur, wo sich bewegte Formen wirklich berühren. **Text nie im gefilterten Teilbaum**, die Unschärfe zerstört die Glyphen; die Beschriftung liegt als Geschwister darüber.

Kosten: Ein SVG-Filter wird nicht vom Compositor getragen, der Teilbaum wird jedes Bild auf der CPU neu gerastert, und das wächst mit der Fläche. Prüffrage: Passt es ins Budget der Stufe (`regler.md`), gibt es ein Standbild und eine Telefonfassung (TE10)? Kontrast mit Filter neu prüfen, die Kantenhärtung ändert die Randfarbe.

```html
<svg width="0" height="0" aria-hidden="true">
  <filter id="goo">
    <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="blur"/>
    <feColorMatrix in="blur" type="matrix"
      values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -9" result="goo"/>
    <feBlend in="SourceGraphic" in2="goo"/>
  </filter>
</svg>
```

```css
.goo-shapes { filter: url(#goo); }        /* shapes only */
.goo-label  { position: relative; }        /* sibling, never a child */
@media (prefers-reduced-motion: reduce) { .goo-shapes { filter: none; } }  /* cross-fade start and end shapes instead */
```

## Überschwingen beim Aufbau eines Overlays

Wann es erlaubt ist und die Decke: BE05. Technik: ein Token für das ganze Projekt, einmal definiert, an jedem Overlay wiederverwendet. Das Element ist `position: absolute` oder `fixed`, der Rückweg läuft mit `--kurve-raus` ohne Überschwingen.

```css
.overlay { transition: transform var(--dauer-klein-raus) var(--kurve-raus); }  /* leaving: calm */
.overlay[data-entering="true"] {
  animation: arrive var(--dauer-klein) var(--kurve-ueberschwingen) both;
}
:root { --kurve-ueberschwingen: cubic-bezier(0.34, 1.4, 0.64, 1); }   /* the one token */
@keyframes arrive { from { transform: scale(0.96) } to { transform: none } }
.overlay { transform-origin: var(--origin, top center); }   /* S43: grows out of its trigger */

/* Spring-equivalent without a JS spring model: linear() sampled from a light spring.
   Chrome/Edge 113+, Firefox 112+, Safari 17.2+; the cubic-bezier above stays the fallback. */
@supports (animation-timing-function: linear(0, 1)) {
  :root {
    --kurve-ueberschwingen: linear(
      0, 0.42 10.4%, 0.83 22.1%, 1.05 32.6%, 1.14 40.5%,
      1.08 52.1%, 1.02 63.4%, 0.99 76.7%, 1 100%
    );
  }
}
```

```js
// S43: set the origin from the trigger, after the overlay is laid out and before it animates
function openFrom(trigger, overlay) {
  const t = trigger.getBoundingClientRect();
  const o = overlay.getBoundingClientRect();
  overlay.style.setProperty('--origin', `${t.left + t.width / 2 - o.left}px ${t.top + t.height / 2 - o.top}px`);
  overlay.dataset.entering = 'true';
}
```

Probe: Im Stylesheet nach Überschwing-Kurven suchen. Eine zweite, andere Kurve ist ein Befund; mehrere Elemente mit demselben Token nicht.

## Reine CSS-Bewegung messen

Lange Aufgaben mitschreiben, einmal im Leerlauf, einmal mit Bewegung, gleiche Maschine, gleiche Sitzung, beide Zahlen zusammen berichten (BE23, TE12). WebGL und Canvas messen nach `rezepte/shader.md` und `rezepte/3d.md`.

```js
const tasks = []
new PerformanceObserver((l) => tasks.push(...l.getEntries().map((e) => e.duration)))
  .observe({ entryTypes: ['longtask'] })
// Report for both runs: tasks.filter((d) => d > 16).length and Math.max(...tasks)
```

## Reduzierte Bewegung je Muster

Jedes Muster hat seinen eigenen Endzustand, kein globaler Block (S17). `clip-path`-Weg, `transform`-Weg und Überschwingen entfallen, das Element steht sofort in seiner Endgeometrie. Ein Überblenden unter 100 ms (`--dauer-rueckmeldung`) darf bleiben. Die Abfrage hört mit `change` mit, denn die Einstellung kann sich bei offener Seite ändern. Laufende Web-Animations werden abgebrochen, sonst ignorieren sie die CSS-Regel.

```js
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)')

function applyMotionPreference(reduced) {
  document.querySelectorAll('.ctl, .bar, .sheet, .overlay').forEach((el) => {
    el.getAnimations({ subtree: true }).forEach((a) => a.cancel())   // drop any in-flight WAAPI animation
    el.classList.toggle('motion-reduced', reduced)                    // CSS end-state below
  })
}

applyMotionPreference(reduceMotion.matches)                                      // read once at load...
reduceMotion.addEventListener('change', (e) => applyMotionPreference(e.matches)) // ...and again on every toggle
```

```css
.motion-reduced.ctl .ctl__ground { transition: none; }          /* clip-path jumps straight to its end state */
.motion-reduced.ctl .ctl__label { transition-duration: var(--dauer-rueckmeldung); }  /* a short opacity fade (under 100 ms) may stay */
.motion-reduced.bar .bar__ground { transition: none; }
.motion-reduced.sheet { transition: none; }                     /* the sheet appears in place, no travel */
.motion-reduced.overlay { transition: none; }
.motion-reduced.overlay[data-entering="true"] { animation: none; transform: none; }  /* no overshoot, no travel */
```

Probe: Einstellung mitten in einer Bewegung umschalten. `document.getAnimations()` liefert am Element nichts Laufendes, die Geometrie entspricht binnen eines Bildes dem Endzustand. Zurückschalten wirkt ohne Neuladen.

## Quellen

Die Quelle nennt keine Adressen. Genannt sind: WCAG 2.2 (2.5.8 Zielgröße, 1.4.1 Farbe), IBM Carbon und Material Design 3 (Bewegungstoken), Apple macOS (Ampelknöpfe als Vorbild).
