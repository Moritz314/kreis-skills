# Rezept: Layouts jenseits gleicher Karten

CSS für Raster mit Gewichtung, redaktionelle Spalten, geteilte Flächen, vollbreite Bänder, Subgrid und ein Laufband. Regeln: S21 (Raster), S12 und S13 (Fokus), S27 (Zeilenlänge), S37 (Handy); Laufband BE22, S17, S18, S42. Raster auf jeder Stufe; Laufband ab `bewegung: 2`, Skript genügt `technik: statisch`.

## Gebrochenes Raster

Bild und Text überlappen an genau einer Stelle, alles andere sitzt auf dem Raster (S21).

```css
.broken-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  column-gap: clamp(1rem, 3vw, 2.5rem);
}

.broken-grid__image {
  grid-column: 1 / 8;
  grid-row: 1 / 3;
}

.broken-grid__text {
  grid-column: 6 / 13;
  grid-row: 2 / 4;
  /* overlaps the image's bottom two rows */
  align-self: end;
  background: var(--surface);
  padding: clamp(1.5rem, 4vw, 3rem);
}

.broken-grid__eyebrow {
  grid-column: 1 / 5;
  grid-row: 1;
  align-self: start;
}
```

## Bento

Kachelgröße folgt der Wichtigkeit.

```css
.bento {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  grid-auto-rows: 180px;
  gap: 1rem;
  grid-auto-flow: dense;
}

.bento__item {
  border-radius: 24px;
  overflow: hidden;
  position: relative;
}

.bento__item--hero { grid-column: span 2; grid-row: span 2; }
.bento__item--wide { grid-column: span 2; grid-row: span 1; }
.bento__item--tall { grid-column: span 1; grid-row: span 2; }
```

Fallen:
- `minmax(0, 1fr)` statt `1fr`. Sonst sprengt eine lange Zeichenkette ohne Umbruch (Adresse, Code, Zahl) die schmale Spur.
- `grid-auto-flow: dense` füllt Lücken, trennt aber DOM-Reihenfolge und Anzeige. Die Fokusreihenfolge springt (S12, S13). Mit bedienbaren Kacheln: `dense` weglassen und jede Kachel mit `grid-column` und `grid-row` setzen.

## Redaktionelle Spalte

Eine Lesespalte (S27), Zitat bricht in den Rand aus, Bild mit echtem Umfluss über `shape-outside`.

```css
.article {
  display: grid;
  grid-template-columns: 1fr min(65ch, 100%) 1fr;
  column-gap: 1.5rem;
}

.article > * { grid-column: 2; }

.pull-quote {
  grid-column: 1 / 4;
  font-size: clamp(1.5rem, 4vw, 2.25rem);
  font-style: italic;
  line-height: 1.2;
  padding-block: 1rem;
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}

.article__figure--inline {
  float: left;
  width: min(40%, 320px);
  margin: 0 1.5rem 1rem 0;
  shape-outside: polygon(0 0, 100% 0, 100% 80%, 60% 100%, 0 100%);
  clip-path: polygon(0 0, 100% 0, 100% 80%, 60% 100%, 0 100%);
}
```

Zeitungsraster mit Aufmacher:

```css
.magazine {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  grid-auto-flow: dense; /* same focus-order trap as bento */
  gap: 1.5rem;
}

.magazine__featured { grid-column: span 2; grid-row: span 2; }
```

## Geteilte Fläche

Zwei Hälften gleicher Höhe für genau zwei vergleichbare Dinge.

```css
.split-screen {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100dvh;
}

.split-screen__pane {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: clamp(2rem, 6vw, 6rem);
}

@media (max-width: 48rem) {
  .split-screen { grid-template-columns: 1fr; }
}

/* diagonal divider */
.split-screen--diagonal .split-screen__pane:first-child {
  clip-path: polygon(0 0, 100% 0, 88% 100%, 0 100%);
  margin-right: -8vw; /* pull the second pane under the cut edge */
}
```

Das Verhältnis darf vom 50 : 50 abweichen, wenn das Gewicht des Inhalts es verlangt.

## Laufband

Endlosband für eine lange Liste gleichartiger Einträge (Stimmen, Presse). Technik: Inhalt einmal kopieren, um genau `-50%` verschieben, dann ist die Naht unsichtbar. Das Tempo kommt in Pixeln je Sekunde aus `--marquee-speed`; das Skript rechnet daraus die Dauer (BE22). Ohne Skript und bei reduzierter Bewegung steht die Liste umbrochen und vollständig (S17, S19).

```html
<section class="marquee" aria-label="Pressestimmen">
  <button class="marquee__pause" type="button" aria-pressed="false">Laufband anhalten</button>
  <div class="marquee__viewport">
    <div class="marquee__track">
      <ul class="marquee__group">
        <!-- real items -->
      </ul>
      <ul class="marquee__group" aria-hidden="true" inert>
        <!-- exact copy -->
      </ul>
    </div>
  </div>
</section>
```

```css
.marquee { --marquee-speed: 40; /* px per second, example value */ }

/* static state: no script or reduced motion */
.marquee__group {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  margin: 0;
  padding: 0;
  list-style: none;
}
.marquee__group[aria-hidden],
.marquee__pause { display: none; }

/* running state, set by marquee.js */
.marquee.is-running .marquee__viewport {
  overflow: hidden;
  mask-image: linear-gradient(90deg, transparent, black 5%, black 95%, transparent);
}
.marquee.is-running .marquee__track {
  display: flex;
  width: max-content;
}
.marquee.is-running .marquee__group {
  flex-wrap: nowrap;
  flex-shrink: 0;
  padding-inline-end: 2rem; /* = gap, keeps the seam even */
}
.marquee.is-running .marquee__group[aria-hidden] { display: flex; }
.marquee.is-running .marquee__pause { display: inline-flex; }
```

```js
// marquee.js, loaded as an external file (S10)
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

for (const root of document.querySelectorAll('.marquee')) {
  const track = root.querySelector('.marquee__track');
  const button = root.querySelector('.marquee__pause');
  let anim = null;
  let width = 0;

  function start() {
    anim?.cancel();
    anim = null;
    root.classList.toggle('is-running', !reduce.matches);
    if (reduce.matches) return; // S17: static, complete list
    width = track.offsetWidth;
    const speed = parseFloat(getComputedStyle(root).getPropertyValue('--marquee-speed'));
    anim = track.animate(
      [{ transform: 'translateX(0)' }, { transform: 'translateX(-50%)' }],
      { duration: (width / 2 / speed) * 1000, iterations: Infinity, easing: 'linear' }
    );
    if (button.getAttribute('aria-pressed') === 'true') anim.pause();
  }

  // under the pointer: slow down, never stop (BE22)
  root.addEventListener('pointerenter', () => anim?.updatePlaybackRate(0.65));
  root.addEventListener('pointerleave', () => anim?.updatePlaybackRate(1));

  // real pause button (S18)
  button.addEventListener('click', () => {
    const paused = button.getAttribute('aria-pressed') !== 'true';
    button.setAttribute('aria-pressed', String(paused));
    if (anim) paused ? anim.pause() : anim.play();
  });

  // re-measure when items load or the viewport changes
  new ResizeObserver(() => { if (track.offsetWidth !== width) start(); }).observe(track);
  reduce.addEventListener('change', start);
}
```

Fallen:
- Beide Gruppen müssen gleich breit sein, sonst springt die Naht. Der Abstand nach dem letzten Eintrag (`padding-inline-end` gleich `gap`) gehört in die Gruppe.
- Die Kopie trägt `aria-hidden` (BE22) und `inert`. Ohne `inert` bleiben Links in der Kopie per Tab erreichbar.
- Nie `animation-play-state: paused` bei `:hover`. `updatePlaybackRate` ändert das Tempo ohne Sprung an der aktuellen Stelle.
- Bilder ohne `width` und `height` ändern die Breite nach dem Laden; der `ResizeObserver` rechnet dann neu (S36).
- Der Knopf steht vor dem Band im DOM, damit er vor den Links den Fokus bekommt; Größe nach S16.
- Kartenbreite folgt der Textlänge, nicht einer festen Breite mit abgeschnittenem Text. Tempo so wählen, dass ein Eintrag lesbar ist, bevor er austritt.

## Vollbreite Bänder im Wechsel

Vollbreite Bänder (Bild, Farbfläche, Film) wechseln mit einer schmalen Textspalte; Bild und Text tauschen die Seite ohne Änderung im Markup.

```css
.content-column {
  width: min(65ch, 100% - 2rem);
  margin-inline: auto;
}

.full-bleed {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  margin-right: calc(50% - 50vw);
}

.story-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  min-height: 80vh;
}

.story-section:nth-of-type(even) { direction: rtl; }
.story-section:nth-of-type(even) > * { direction: ltr; /* undo the flip for content */ }
```

Falle: `calc(50% - 50vw)` bricht, sobald irgendwo ein zu breites Kind einen Querbalken erzeugt. Schutz: `body { overflow-x: clip; }` (S37: kein Querüberlauf).

## Subgrid

Karten in einer Reihe richten Kopfzeile, Titel, Text und Knopf an denselben Linien aus, ohne Höhenabgleich per Skript.

```css
.card-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto auto 1fr auto; /* eyebrow / title / body / cta */
  gap: 1.5rem;
}

.card {
  display: grid;
  grid-row: span 4;
  grid-template-rows: subgrid;
  gap: inherit;
}

.card__title { grid-row: 2; }
.card__body  { grid-row: 3; }
.card__cta   { grid-row: 4; align-self: end; }
```

Unterstützung laut Quelle: Baseline Widely Available seit März 2026 (Chrome und Edge ab 117, Firefox, Safari ab 16), ohne Rückfall nutzbar. Für sehr alte Browser: feste `min-height` je Zeilenrolle oder Höhenabgleich per Skript.

## Quellen

- https://every-layout.dev/
- https://1linelayouts.com/
- https://superdesign.dev/styles/bento-grid
- https://css-tricks.com/responsive-grid-magazine-layout-in-just-20-lines-of-css/
- https://www.awwwards.com/websites/grid/
