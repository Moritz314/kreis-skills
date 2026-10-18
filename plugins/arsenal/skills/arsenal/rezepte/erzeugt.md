# Rezept: Film mit ffmpeg, Linien mit SVG

Geprüft am 18.10.2026 mit ffmpeg auf dem Kern-Server (Testfilme 2880 × 1800 und 3840 × 2400, 30 Bilder/s). Regeln: Modul `erzeugt`, Modul `medien` ME13 bis ME15.

## Klassen aus einem Master

Breite je Klasse = breiteste Anzeige der Klasse × 2 (S34, ME13). Beispiel für eine Bühne über die volle Breite, höchstens 1440 CSS-px: groß (ab 1280 px) 2880, Tablet (ab 768 px) 2560, Telefon 1536. Der Master ist mindestens so breit wie die größte Klasse.

```bash
# per class MP4 (H.264) and WebM (VP9), no audio
for w in 2880 2560 1536; do
  ffmpeg -i master.mp4 -vf "scale=$w:-2:flags=lanczos" -c:v libx264 -preset slow -crf 20 \
    -pix_fmt yuv420p -movflags +faststart -an film-$w.mp4
  ffmpeg -i master.mp4 -vf "scale=$w:-2:flags=lanczos" -c:v libvpx-vp9 -b:v 0 -crf 34 \
    -row-mt 1 -an film-$w.webm
done
# then check weight against ME13; too heavy: calmer motif (ME09), raise crf only while the 2x crop stays clean
```

## Poster ist Bild 0

```bash
# one poster per class; the phone poster stays under 30 KB (lower -quality if needed)
for w in 2880 2560 1536; do
  ffmpeg -i film-$w.mp4 -frames:v 1 -c:v libwebp -quality 80 poster-$w.webp
done
# check: poster against frame 0, PSNR above 35 dB (test: 45.7 dB)
ffmpeg -i film-2880.mp4 -frames:v 1 bild0.png
ffmpeg -i poster-2880.webp -i bild0.png -lavfi psnr -f null - 2>&1 | grep -o "average:[0-9.]*"
```

## Schleife ohne Naht

Die letzten 0,5 s blenden in den Anfang über; der Film wird 0,5 s kürzer und läuft nahtlos.

```bash
ffmpeg -i master.mp4 -filter_complex \
 "[0:v]split[a][b];[a]trim=0:2.5,setpts=PTS-STARTPTS[haupt];[b]trim=2.5:3,setpts=PTS-STARTPTS[ende];\
  [ende][haupt]xfade=transition=fade:duration=0.5:offset=0[aus]" \
 -map "[aus]" -c:v libx264 -crf 20 -pix_fmt yuv420p schleife.mp4
```

Für eine Länge L: `trim=0:L-0.5` und `trim=L-0.5:L`.

## Einbinden

Ohne `autoplay`: Das Skript startet den Film nach `load`, lässt bei reduzierter Bewegung das Poster stehen und pausiert außerhalb des Fensters (ME15, S18). Das Poster liegt als `<picture>` hinter dem Film, damit jedes Fenster nur sein Poster lädt. Fertige Fassung: Baustein K2.

```html
<!-- in <head>, only when the film is in the first view (LCP, S39): one preload per class (ME14) -->
<link rel="preload" as="image" href="poster-2880.webp" media="(min-width: 1280px)" fetchpriority="high">
<link rel="preload" as="image" href="poster-2560.webp" media="(min-width: 768px) and (max-width: 1279px)" fetchpriority="high">
<link rel="preload" as="image" href="poster-1536.webp" media="(max-width: 767px)" fetchpriority="high">

<div class="film">
  <picture>
    <source srcset="poster-2880.webp" media="(min-width: 1280px)">
    <source srcset="poster-2560.webp" media="(min-width: 768px)">
    <img src="poster-1536.webp" width="1440" height="900" alt="" fetchpriority="high">
  </picture>
  <video class="stage" muted loop playsinline preload="metadata" width="1440" height="900">
    <source src="film-2880.webm" type="video/webm" media="(min-width: 1280px)">
    <source src="film-2880.mp4" type="video/mp4" media="(min-width: 1280px)">
    <source src="film-2560.webm" type="video/webm" media="(min-width: 768px)">
    <source src="film-2560.mp4" type="video/mp4" media="(min-width: 768px)">
    <source src="film-1536.webm" type="video/webm">
    <source src="film-1536.mp4" type="video/mp4">
  </video>
  <button class="pause" aria-pressed="false" aria-label="Film anhalten">…</button>
</div>
<script type="module" src="/js/film.js"></script>
```

```css
.film { position: relative; max-width: 1440px; }
.film img, .film video { display: block; width: 100%; height: auto; }
.film video { position: absolute; inset: 0; height: 100%; object-fit: cover; }
```

```js
// /js/film.js
const video = document.querySelector('video.stage');
const button = document.querySelector('button.pause');
let paused = matchMedia('(prefers-reduced-motion: reduce)').matches; // reduced motion: poster stays
let inView = false;
button.setAttribute('aria-pressed', String(paused));

const update = () => (inView && !paused ? video.play().catch(() => {}) : video.pause());

// start after load; with an intro, start after the intro instead (ME15)
addEventListener('load', () => {
  new IntersectionObserver(([e]) => { inView = e.isIntersecting; update(); }).observe(video);
});
button.addEventListener('click', () => {
  paused = !paused;
  button.setAttribute('aria-pressed', String(paused));
  update();
});
```

## Linie, die sich zeichnet (SVG, nur Schmuck)

```html
<svg viewBox="0 0 400 120" aria-hidden="true">
  <path class="linie" pathLength="1" d="M10 100 C 120 10, 280 10, 390 100"/>
</svg>
```

```css
.linie { fill: none; stroke: currentColor; stroke-width: 2;
         stroke-dasharray: 1; stroke-dashoffset: 0; }
@media (prefers-reduced-motion: no-preference) {
  .linie { animation: zeichnen var(--dauer-inszenierung) var(--kurve-rein) both; }
  @keyframes zeichnen { from { stroke-dashoffset: 1; } }
}
```

Der Endzustand steht ohne Animation (`stroke-dashoffset: 0`); bei reduzierter Bewegung ist die Linie sofort ganz da. Schmuckbewegung, ab `bewegung: 2`; Dauer und Kurve aus dem MASK (Tabelle im Stamm). Für Text nicht verwenden (S19).
