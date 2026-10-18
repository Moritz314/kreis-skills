# Rezept: Scroll-Choreografie, Textsplit, Zeiger-Effekte, View Transitions

Wie man Scroll-Bewegung baut. Regeln: S17 bis S20, S42, S45, S48, BE07, BE12 bis BE17, TE10, TE11, TE13. Natives CSS ab `technik: statisch`, GSAP ab `technik: inseln`, Shader und 3D ab `technik: webgl`; Pins ab `bewegung: 3` (`regler.md`). Prüffrage vor jedem Effekt: Passt es ins Budget der Stufe (`regler.md`), gibt es ein Standbild und eine Telefonfassung (TE10)?

## Werkzeug: natives CSS oder GSAP

Stand 09.2026: CSS Scroll-driven Animations (`animation-timeline`, `scroll()`, `view()`, `animation-range`, `timeline-scope`) ist ein W3C-Arbeitsentwurf. Chrome und Edge ab 115 (Juli 2023), Safari ab 26.0 (September 2025, mit `animation-range`). Firefox: caniuse nennt 158, stabil war Anfang September 2026 155/156, also noch nicht in Firefox stabil. MDN: „Limited availability, not Baseline“.

- **Nativ:** ein Element, Fortschritt linear zu Scroll (`scroll()`) oder Sichtbarkeit (`view()`). Läuft auf dem Compositor, ohne Skript, daher auch bei `technik: statisch`.
- **GSAP ScrollTrigger:** sobald Pins über mehrere Abschnitte, benannte Marken, Nachlauf für Schmuck (BE12), Rückrufe an Scrollpunkten oder waagrechte Scroll-Abschnitte nötig sind. Das kann nativ nicht.

## Natives CSS mit Rückfall

Der Ruhezustand ist der Endzustand. Animiert wird nur, wenn der Browser es kann und keine reduzierte Bewegung gewünscht ist. Firefox zeigt das fertige Layout.

```css
.reveal { transform: none; }

@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .reveal {
      animation: reveal-in linear both;
      animation-timeline: view();
      animation-range: entry 0% cover 30%;
    }
    @keyframes reveal-in {
      from { transform: translateY(24px); }
    }
  }
}
```

## GSAP und ScrollTrigger

Lizenz, geprüft 09.2026: Seit 29.04.2025 ist GSAP mit allen Plugins kostenlos (ScrollTrigger, ScrollSmoother, SplitText, MorphSVG, DrawSVG, Draggable, Flip, Physics2D). gsap.com/pricing: „GSAP is now 100% free for all users, thanks to Webflow's support.“ Frei nutzbar, nicht Open Source: kein Umverpacken, kein Konkurrenzprodukt; Kundenseiten und SaaS sind erlaubt. Notizen, die ScrollTrigger oder SplitText „kostenpflichtig“ nennen, sind veraltet.

```bash
npm install gsap
```

Pin mit Scrub. Die Überschrift bewegt sich und bleibt voll lesbar (BE13); die Bildunterschrift steht von Anfang an da und rückt nur.

```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

if (!reduce) {   // sonst bleibt der Ruhezustand stehen, alles sichtbar (S17)
  const tl = gsap.timeline({
    defaults: { ease: "none" },   // Scroll-Kopplung linear (BE12)
    scrollTrigger: {
      trigger: ".chapter-2",
      start: "top top",
      end: "+=150%",   // Pin-Länge aus dem Weg (BE12), höchstens +=200% (BE14)
      scrub: true,     // content couples 1:1; a number (lag) only for decoration (BE12)
      pin: true,
    },
  });
  tl.to(".chapter-2 .headline", { yPercent: -20 })
    .to(".chapter-2 .diagram", { scale: 1.15, rotate: 3 }, "<")   // "<" = mit dem vorigen starten
    .from(".chapter-2 .caption", { y: 24 }, "-=0.3");             // überlappt den vorigen Tween
}
```

Tiefe entsteht über verschiedene Wege je Ebene bei `scrub: true`; ein Nachlauf (`scrub` als Zahl) nur auf reinen Schmuck-Ebenen ohne Text (BE12). `pin: true` setzt das Element auf `position: fixed`; ein Pin-Spacer hält seinen Platz im Fluss.

## Mehrere Abschnitte mit Marken

```js
const tl = gsap.timeline({
  defaults: { ease: "none" },
  scrollTrigger: {
    trigger: ".story",
    start: "top top",
    end: "+=200%",   // Obergrenze nach BE14
    scrub: true,
    pin: true,
  },
});

tl.addLabel("intro")
  .to(".story .part-a", { xPercent: -40 })
  .addLabel("reveal")
  .to(".story .part-b", { xPercent: 40 }, "reveal")
  .from(".story .caption-2", { y: 24 }, "reveal+=0.2")
  .addLabel("outro")
  .to(".story .part-a, .story .part-b", { yPercent: -10 }, "outro");   // rücken weiter, verschwinden nicht
```

Marken adressieren Stufen nach Namen. Jede Stufe bekommt Scrollweg im Verhältnis ihrer Dauer in der Zeitleiste: eine Stufe verlängern heißt mehr Tween-Zeit zwischen den Marken, nicht `start`/`end` ändern.

Fallen:
- Der Pin-Spacer ändert die Dokumenthöhe. Scrollweg nach dem Einfügen von Inhalt messen; neue Tweens mitten in der Zeitleiste verschieben still den Weg jeder Marke.
- Pin in Pin erzeugt Layout-Flattern. Beide zusammen testen.
- Einmalige Einblendungen mit GSAP enden mit `clearProps` für die gesetzten Eigenschaften. Sonst kämpft eine CSS-`transition` auf derselben Eigenschaft gegen den Tween (gemessen: 12 px Fehlstand).
- Viele Marken auf einer Zeitleiste fühlen sich gleich schnell an. Schwere Teile über eigene Zeitleisten mit eigenem Scrollweg führen.
- Probe: Standbild je Pin-Viertel (BE14), Kreuzungsprobe (BE16).

## Zerlegung (Explosionszeichnung)

| Bau | Aufwand | Größe, Last | Passt für |
|---|---|---|---|
| CSS-Transform-Ketten | gering bis mittel: ein `div` je Teil, per `transform` auseinander, nativ (`scroll()`) oder GSAP `scrub` | sehr klein; GSAP plus ScrollTrigger einige Dutzend KB; Compositor | flache, schematische Darstellung, wenige Ebenen |
| SVG-Gruppen | mittel: jedes Teil eine eigene, sauber verankerte `<g>` (Transform erbt auf Kinder, MDN) | sehr klein, verlustfrei skalierbar | Icons, Diagramme, Infografik |
| 3D-Modell mit getrennten Teilen | hoch: Modell in benannte Knoten, Kamera, Licht, WebGL (Three.js, React Three Fiber, Babylon.js, glTF). `GLTFLoader` liefert `gltf.scene` als `THREE.Group`, die Meshes animieren einzeln | stark schwankend, keine belastbare Zahl für einfache Produkte. Belegt: Figuren mit etwa 30.000 Dreiecken und 2K-Textur 5 bis 15 MB unkomprimiert; Draco/Meshopt und KTX2 sparen 10 bis 70 % | echte 3D-Produkte, Maschinen; Code in `rezepte/3d.md` |
| Bildfolge | hoch in der Herstellung: 60 bis 150 vorgerenderte Bilder; Einbau einfach (Bildindex aus Scrollfortschritt, `drawImage` auf Canvas, meist mit GSAP-Scrub und Pin) | kann groß werden; WebP/AVIF, Sprite-Sheets, Bilder einzeln nachladen | fotorealistisches Produkt, Apple-Muster |

Schematisch: CSS oder SVG. 3D lohnt sich nur, wenn freie Kamera oder Drehung selbst die Aussage ist; geht es nur um die Zerlegung, liefert die Bildfolge dasselbe mit weniger Risiko zur Laufzeit.

## Textsplit mit SplitText

Seit der Freigabe 2025 im Paket `gsap`. Wörter starten sichtbar und rücken nur (BE07); keine Zeilenmaske für Inhalt.

```js
import { gsap } from "gsap";
import { SplitText } from "gsap/SplitText";
import { CustomEase } from "gsap/CustomEase";
gsap.registerPlugin(SplitText, CustomEase);
CustomEase.create("enter", "0.05,0.7,0.1,1"); // entry curve from the table in the stamm (BE04)

if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
  SplitText.create(".hero-headline", {
    type: "lines, words",
    autoSplit: true,   // teilt bei Größenänderung und Schriftladen neu (API ab v3.13)
    onSplit(self) {
      return gsap.from(self.words, {
        y: 24,
        duration: 0.8,   // staging token, from bewegung: 2 (BE04)
        stagger: 0.03,   // S48
        ease: "enter",
      });
    },
  });
}
```

Nur echten, fertigen Text teilen: Zeilenumbrüche bestimmen den Rhythmus. Wortweise ist billiger als zeichenweise. Ohne Abhängigkeit: Wörter von Hand in `<span>` legen, IntersectionObserver plus `element.animate()` (Web Animations API), wenn nur ein einmaliger Wort-Einstieg gebraucht wird.

## Motion (React)

Lizenz, geprüft 09.2026: MIT. Paket heißt seit 2025 `motion` (vorher `framer-motion`, löst noch auf, wird nicht mehr entwickelt). Import aus `motion/react` oder `motion`. Doku: motion.dev.

```bash
npm install motion
```

Lesefortschritt, linear am Scroll. Der Balken sitzt unten im festen Kopf (S39); ohne festen Kopf entfällt er.

```jsx
import { motion, useScroll } from "motion/react";

function ScrollProgress() {
  const { scrollYProgress } = useScroll();
  return (
    <motion.div
      style={{
        scaleX: scrollYProgress,
        transformOrigin: "0% 50%",
        position: "absolute", left: 0, right: 0, bottom: 0, height: 3, // inside the header
      }}
    />
  );
}
```

Fortschritt an etwas Echtes binden: Artikellänge, nummerierte Schritte. Kinder staffeln mit `transition: { delayChildren: i * 0.03 }` (S48).

## Magnetknopf und Zeiger-Effekte

Ohne Bibliothek. Der Effekt folgt dem Zeiger, der Systemzeiger bleibt sichtbar (S20). Nur bei Hover-Geräten (TE13), nicht bei reduzierter Bewegung.

```html
<button class="magnetic"><span>Get started</span></button>
```
```css
.magnetic { transition: transform var(--dauer-klein) var(--kurve-ort); will-change: transform; }  /* S42: change of place */
.magnetic span { display: inline-block; transition: transform var(--dauer-klein) var(--kurve-ort); }
```
```js
const ok = matchMedia("(hover: hover)").matches &&
           !matchMedia("(prefers-reduced-motion: reduce)").matches;

if (ok) document.querySelectorAll(".magnetic").forEach((el) => {
  const strength = 0.35;      // Hülle bewegt sich weniger
  const strengthInner = 0.6;  // Beschriftung mehr: geschichteter Zug
  const span = el.querySelector("span");

  el.addEventListener("pointermove", (e) => {
    const r = el.getBoundingClientRect();
    const x = e.clientX - (r.left + r.width / 2);
    const y = e.clientY - (r.top + r.height / 2);
    el.style.transform = `translate(${x * strength}px, ${y * strength}px)`;
    span.style.transform = `translate(${x * strengthInner}px, ${y * strengthInner}px)`;
  });
  el.addEventListener("pointerleave", () => {
    el.style.transform = "translate(0, 0)";
    span.style.transform = "translate(0, 0)";
  });
});
```

Zugbereich begrenzen: Listener auf etwa das 1,5-Fache der Knopffläche, nicht auf das ganze Fenster.

## Hintergrund am Zeiger, Canvas im Bild

Bausteine: Pointer Events für die Position, `<canvas>` oder WebGL, ein Uniform reicht die Zeigerposition an den Fragment-Shader (Muster belegt in Fachartikeln, z. B. Codrops zur Bulge-Verzerrung, nicht in einer Norm). Lokal am Knopf oder an der Karte kostet es wenig. Ein Vollbild-Shader rechnet jedes Pixel in jedem Bild neu und zieht auf dem Telefon Akku; Shader-Code in `rezepte/shader.md`.

```js
const canvas = document.querySelector(".shader-bg");
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
const dpr = matchMedia("(pointer: coarse)").matches ? 1 : Math.min(devicePixelRatio, 1.5);
canvas.width = canvas.clientWidth * dpr;
canvas.height = canvas.clientHeight * dpr;

let rafId = null;
function renderLoop(t) {
  draw(t);
  rafId = requestAnimationFrame(renderLoop);
}

if (reduce) {
  draw(0);   // Standbild (S17, TE10)
} else {
  const io = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) {
      if (!rafId) rafId = requestAnimationFrame(renderLoop);
    } else if (rafId) {
      cancelAnimationFrame(rafId);
      rafId = null;
    }
  }, { threshold: 0 });
  io.observe(canvas);
}
```

`requestAnimationFrame` pausiert in Hintergrund-Tabs von selbst (MDN); der Observer pausiert zusätzlich außerhalb des Bildes. Bei WebGL beim Verlassen Geometrie und Texturen freigeben (TE10, `rezepte/3d.md`).

## View Transitions

Browser-eigener Übergang zwischen DOM-Zuständen (SPA) oder Seiten (MPA), gemeinsame Elemente über `view-transition-name`. Kein Skript für den Mechanismus.

Stand 09.2026 (caniuse): global etwa 91,75 %. Im Dokument: Chrome/Edge 111+, Safari 18+. Zwischen Dokumenten: Chrome/Edge 126+, Safari 18.2+. Firefox ab 144 (in 143 hinter Schalter); Firefox zwischen Dokumenten ist sehr neu, vor dem Einsatz an caniuse prüfen. Immer Funktion abfragen.

```js
function navigateTo(newState) {
  if (!document.startViewTransition ||
      matchMedia("(prefers-reduced-motion: reduce)").matches) {
    applyState(newState);   // sofortiger Wechsel, kein Fehler
    return;
  }
  document.startViewTransition(() => applyState(newState));
}
```
```css
/* gemeinsames Element: in beiden Zuständen vorhanden */
.product-thumb { view-transition-name: product-hero; }

::view-transition-old(product-hero),
::view-transition-new(product-hero) {
  animation-duration: var(--dauer-gross);          /* S45 */
  animation-timing-function: var(--kurve-ort);     /* S42: change of place */
}
```

Dauer und Kurve der Pseudo-Elemente immer selbst setzen. `view-transition-name` nur an die ein bis zwei Elemente, die die Bedeutung tragen (S46).

## Quellen

- https://gsap.com/showcase/
- https://gsap.com/docs/v3/Plugins/SplitText/
- https://motion.dev/examples
- https://tympanus.net/codrops/
- https://developer.chrome.com/docs/web-platform/view-transitions
