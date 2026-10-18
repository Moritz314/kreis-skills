# Modul Technik

Laden ab `technik: inseln`, bei Video und bei den Befehlen `bauen` und `audit`. Sicherheit und Auslieferung im Stamm (S10, S38 bis S40), Budgets in `regler.md`. Code: `rezepte/astro.md`, `rezepte/shader.md`, `rezepte/3d.md`.

## Gerüst

- **TE01 Gerüst nach Umfang.** Bis fünf Seiten: statisches HTML und CSS von Hand. Ab mehr als fünf Seiten: Astro. Für Anwendungen mit viel Zustand im Browser (Verwaltung, Postfach, Aufgaben) ist Astro das falsche Werkzeug; dort ein übliches SPA-Gerüst.
- **TE02 Stand der Werkzeuge** (geprüft 08.09.2026): Astro 7.3.2, Tailwind CSS 4.3.3 über das Vite-Plugin, Node ab 22.12. Neuere Fassungen vor dem Einsatz an der offiziellen Quelle prüfen; Ungeprüftes heißt „ungeprüft“.
- **TE03 Inseln.** Nur was Bedienung braucht, wird eine Insel. `client:visible` ist der Standard; `client:load` nur für Teile, die oben stehen und sofort bedienbar sein müssen; `client:idle` für Teile, die bald gebraucht werden. Eine schwere Szene lädt mit `client:visible`. Prüffrage vor `client:load`: Muss sie vor allem anderen bedienbar sein, und hält die Seite trotzdem S39 und das Budget?
- **TE04 Cache.** nginx liefert `_astro/*` mit `Cache-Control: public, max-age=31536000, immutable`, HTML mit `no-cache`.

## CSP-Fallen (zu S10)

- **TE05 Weg festlegen, bevor gebaut wird.** Ohne `<ClientRouter />`: `security.csp: true` plus `build.inlineStylesheets: 'never'`; jede Seite trägt ihre CSP als `<meta>`. Trotzdem setzt nginx die übrigen Kopfzeilen aus S10 und `Content-Security-Policy: frame-ancestors 'self'`, denn `frame-ancestors` wirkt im `<meta>` nicht. Mit `<ClientRouter />`: CSP als nginx-Kopfzeile (`script-src 'self'`, `style-src 'self' 'unsafe-inline'`, `frame-ancestors 'self'`), kein `security.csp`, trotzdem `inlineStylesheets: 'never'`.
- **TE06 Kein rohes `<script>` in `.astro`.** Astro schreibt kleine Skripte ins HTML. Skripte als eigene Dateien einbinden. Radix (Unterbau von shadcn) setzt Inline-Styles; mit strengem `style-src` diese Teile meiden oder `'unsafe-inline'` für Styles hinnehmen.
- **TE07 Probe:** gebautes HTML nach `<script>` ohne `src` durchsuchen (0 Treffer; `type="application/ld+json"` zählt nicht, es wird nicht ausgeführt), aktiven CSP-Weg per `curl` prüfen, jede Insel im Browser auslösen und die Konsole auf „Refused“ lesen.
- **TE08 Thema-Skript** unter 1 KB, vor dem ersten Zeichnen (Form: Vorliebe in `behavior.md`, S10) (kein Aufblitzen des falschen Modus). Es wertet `?thema=hell` und `?thema=dunkel` aus (Messung im `audit`), sonst die gespeicherte Wahl, sonst den Systemmodus.

## Laden und Laufen

- **TE09 Schriften** als WOFF2 in festen Instanzen (eine variable Datei, wenn sie kleiner ist als die nötigen Instanzen), auf die genutzten Zeichen beschnitten, `font-display: swap` oder `optional`, die Hauptschrift vorgeladen. Messwerte gegen das Schriftbudget.
- **TE10 Canvas, Shader, 3D** laufen nur, solange sie im Bild sind (IntersectionObserver), und räumen beim Verlassen auf (Geometrie und Texturen freigeben, `requestAnimationFrame` abbrechen). Pixeldichte nach Budget. Auf dem Telefon gibt es eine eigene, leichtere Fassung, kein Weglassen; dazu ein Standbild als Rückfall und für reduzierte Bewegung.
- **TE11 Scroll und Rendern.** IntersectionObserver statt Scroll-Handler; Lese- und Schreibzugriffe je Bild in einem `requestAnimationFrame` bündeln; keine Layout-Messung beim Rendern; Listen über 50 Einträge virtualisieren; `preconnect` zu nötigen fremden Ursprüngen.
- **TE12 Long Tasks** werden bei 4-facher CPU-Drosselung gemessen, in der ersten Ansicht und in jedem Pin, gegen eine Leerlaufmessung derselben Seite.

## Bedienung im Gerät

- **TE13 Eingabearten.** Hover-Effekte nur unter `(hover: hover)`; Ziele für `(pointer: coarse)` groß genug (S16). Was bei Hover erscheint, erscheint auch bei `:focus-within`.
- **TE14 Telefon-Feinheiten:** `touch-action: manipulation` an Bedienelementen, `overscroll-behavior: contain` in Overlays und Schubladen, `env(safe-area-inset-*)` an festen Leisten, `theme-color` passend zu Hell und Dunkel.
- **TE15 Sprache und Zahlen:** Datum, Zahl und Währung über `Intl`; Marken- und Produktnamen mit `translate="no"`.

## Vorschau als Claude-Artefakt

- **TE16 Fremde Skripte** nur von `cdnjs.cloudflare.com`, `cdn.jsdelivr.net/npm/`, `cdn.tailwindcss.com` und `code.jquery.com`; alles andere scheitert still. Lucide über jsDelivr (`lucide@1.43.0/dist/umd/lucide.min.js`), three.js als UMD r128 über cdnjs oder als Modul per Importmap über jsDelivr (dort auch die Addons). Versionen fest angeben.
- **TE17 `.glb` wird nicht ausgeliefert:** das Modell als Base64-Text (`*.b64.txt`) daneben legen und mit `fetch().text()`, `atob` und `GLTFLoader.parse` laden. Das Gerüst setzt `<html>`, `<head>`, `<body>` selbst: für die Veröffentlichung eine Fassung ohne diese Tags.
