# Recherche: Auslieferungs-Assets, Favicon, App-Icons, Banner (Stand geprüft 2026-09-08)

Spezifikationsrecherche für ein Projekt bei der Auslieferung: welche Bilddateien und Icon-Formate tatsächlich gebraucht werden, in welchen Maßen und mit welchem Markup. Primärquellen zuerst (Apple, Google, Android, W3C, ogp.me, Meta, IAB), Sekundärquellen nur wo keine Primärquelle greifbar war, dann ausdrücklich markiert. Zwei Primärquellen ließen sich nicht direkt als Text abrufen (Apples HIG-Seiten sind clientseitig gerendertes JavaScript ohne Textinhalt in der Rohantwort, X/Twitters Karten-Dokumentation war unter developer.x.com und docs.x.com nicht erreichbar beziehungsweise nicht mehr auffindbar); das ist im Text vermerkt.

> [!TIP]
> Kennzeichnung je Aussage: `[Spec]` aus Primärquelle belegt, `[Sekundär]` nur aus zweiter Hand, `[Veraltet]` war einmal nötig, `[Ungeprüft]` konnte nicht belegt werden. Nummern in eckigen Klammern (`[Q3]`) verweisen auf die Quellentabelle am Ende.

## 1. Favicon

### 1.1 Minimaler Satz heute

Der historisch kursierende Satz aus zwei Dutzend PNG-Größen (16, 24, 32, 48, 57, 60, 64, 72, 76, 96, 114, 120, 144, 152, 180, 192, 512 …) ist für ein modernes Projekt Ballast. Was tatsächlich gebraucht wird, lässt sich aus den offiziellen Angaben zu `<link>`-Attributen und Praxis ableiten:

| Datei | Zweck | Beleg |
|---|---|---|
| `favicon.svg` | primäres Icon für alle Browser mit SVG-Favicon-Unterstützung, eine Datei für alle Größen, optional mit Dark-Mode-Umschaltung | [Sekundär, Q16] |
| `favicon.ico` | Fallback für Browser ohne SVG-Favicon-Unterstützung sowie für implizite Anfragen (`GET /favicon.ico`), Mehrgrößen-Container mit 16×16, 32×32, ggf. 48×48 | [Sekundär, Q16][Spec, Q1] |
| `apple-touch-icon.png` | 180×180, für „Zum Home-Bildschirm hinzufügen" auf iOS/iPadOS und als Fallback in einigen anderen Kontexten | [Spec, Q1] |
| Web-App-Manifest-Icons (192×192, 512×512, davon mindestens eines `maskable`) | nur wenn das Projekt ein PWA-Manifest hat (Abschnitt 2.3) | [Spec, Q8] |

Ein Projekt ohne PWA-Anspruch kommt also mit drei Dateien aus: `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`. Das deckt sich mit der sekundären, aber technisch gut belegten Einschätzung von Evil Martians, die exakt dieses Minimalschema (plus Manifest-Icons für PWA-Fälle) vorschlagen [Sekundär, Q16]. MDN selbst formuliert keine Empfehlung „das genügt", sondern zeigt nur die einzelnen `<link>`-Typen; die Verdichtung auf einen Minimalsatz ist hier sekundär hergeleitet.

`rel="shortcut icon"` taucht in der aktuellen MDN-Referenzseite zu `<link>` nicht mehr auf, nur `rel="icon"` [Spec, Q1]. Google Search Central listet `shortcut icon` weiterhin als unterstützten `rel`-Wert neben `icon`, `apple-touch-icon` und `apple-touch-icon-precomposed` [Spec, Q2]; das ist ein Hinweis darauf, dass die alte Schreibweise zur Kompatibilität in Suchergebnissen keinen Schaden anrichtet, aber für neuen Code nicht mehr die empfohlene Form ist.

### 1.2 Markup wörtlich

Minimalsatz ohne PWA:

```html
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

Beleg für die einzelnen Zeilen: `rel="icon"` mit `type="image/svg+xml"` und `sizes`-Attribut als offizielles Attributmuster [Spec, Q1]; `rel="apple-touch-icon"` mit optionalem `sizes`-Attribut, MDN zeigt explizit einen Satz für unterschiedliche Apple-Geräte:

```html
<!-- iPad Pro mit hochauflösendem Retina-Display -->
<link rel="apple-touch-icon" sizes="167x167" href="/apple-touch-icon-167x167.png">
<!-- iPhone mit 3x-Auflösung -->
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
<!-- iPad ohne Retina, iPad mini usw. -->
<link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
<!-- iPhone mit 2x-Auflösung und andere Geräte -->
<link rel="apple-touch-icon" href="/apple-touch-icon-120x120.png">
<!-- einfaches Favicon -->
<link rel="icon" href="/favicon.ico">
```

[Spec, Q1]. In der Praxis reicht eine einzelne 180×180-Datei ohne `sizes`-Attribut, weil iOS sie selbst herunterskaliert; das ist die gängige Vereinfachung, aber nicht wörtlich so von Apple oder MDN als „genügt allein" belegt, sondern sekundäre Praxis [Sekundär, Q16].

Für ein PWA-Projekt kommt zusätzlich:

```html
<link rel="manifest" href="/manifest.webmanifest">
```

[Sekundär, Q16], Inhalt des Manifests siehe Abschnitt 2.3.

### 1.3 Dark Mode im SVG-Favicon über prefers-color-scheme

Ein SVG-Favicon kann eingebettetes CSS mit einer `prefers-color-scheme`-Media-Query enthalten, wodurch eine einzelne Datei im Hell- und Dunkelmodus unterschiedlich aussieht. Beispiel-Technik:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500">
  <style>
    @media (prefers-color-scheme: dark) {
      .a { fill: #f0f0f0 }
    }
  </style>
  <path class="a" fill="#0f0f0f" d="…" />
</svg>
```

[Sekundär, Q16]. Wo das greift und wo nicht, ist uneinheitlich und in der recherchierten Sekundärliteratur nicht durch eine Primärquelle (MDN nennt SVG-Favicons in der aktuell abgerufenen `<link>`-Referenzseite überhaupt nicht) belegbar: Chromium (Chrome, Edge) und Firefox werten die Media-Query im Favicon-Kontext aus, Safari rendert SVG-Favicons zwar (Versionsangabe unsicher: mehrere Sekundärquellen nennen übereinstimmend Safari 15 als Beginn, nicht Safari 14, Safari 9 bis 14 nutzten stattdessen nur `mask-icon`), wertet die `prefers-color-scheme`-Query darin aber nicht aus und zeigt durchgehend die Hell-Variante [Ungeprüft, aus mehreren sich überschneidenden Sekundärquellen, keine davon developer.apple.com oder webkit.org]. Konkrete Versionsnummern für den Beginn der Chrome-/Firefox-Unterstützung (kursierend: Chrome ab 80, Firefox ab 41) konnten in dieser Recherche nicht gegen MDNs Browser-Compat-Daten oder eine andere Primärquelle geprüft werden [Ungeprüft].

### 1.4 Google-Anforderungen an Favicons in der Suche

Live von developers.google.com abgerufen (2026-09-08):

„Your favicon must be a square (1:1 aspect ratio) that's at least 8x8px. While the minimum size requirement is 8x8px, we recommend using a favicon that's larger than 48x48px so that it looks good on various surfaces." [Spec, Q2]

Unterstützte Dateiformate laut derselben Seite: BMP, GIF, ICO, PNG, JPEG, PPM, TIFF [Spec, Q2]. Crawlbarkeit: „Googlebot-Image must be able to crawl the favicon file and Googlebot must be able to crawl the home page; they cannot be blocked for crawling" [Spec, Q2], das heißt: Favicon-Pfad darf nicht per `robots.txt` gesperrt sein. Weitere Bedingungen aus derselben Seite: nur ein Favicon pro Hostname, die Favicon-URL muss stabil bleiben, unpassende Bildinhalte werden durch ein Standardicon ersetzt [Spec, Q2]. Empfohlenes Markup laut Google:

```html
<link rel="icon" href="/path/to/favicon.ico">
```

[Spec, Q2].

Hinweis zur Versionsabhängigkeit: Eine über Websuche gefundene, offenbar ältere Fassung derselben Google-Seite verlangte eine Größe als „Vielfaches von 48px" (48, 96, 144 px …) [Ungeprüft, nur aus Suchtreffer-Snippets, nicht aus der live abgerufenen Seite]. Die am 2026-09-08 live abgerufene Fassung nennt stattdessen nur noch „mindestens 8×8px, empfohlen größer als 48×48px" ohne Vielfaches-Pflicht [Spec, Q2]. Für dieses Dokument gilt die live geprüfte, aktuellere Fassung.

### 1.5 Warum 32 und 48 in der Praxis auftauchen

Für das genaue Anfrageverhalten der Browser (welche Pixelgröße wann angefordert wird) fand sich keine Primärquelle bei MDN, Chrome-, Firefox- oder Microsoft-Dokumentation. Die kursierende Erklärung aus mehreren sich deckenden Sekundärquellen: 32×32 wird auf hochauflösenden Bildschirmen (Retina, 4K) für schärfere Tab-Icons verwendet und erscheint zusätzlich im Windows-Taskleisten-Kontext bei angehefteten Seiten, 48×48 wird von Windows für angeheftete Taskleisten-Einträge und Desktop-Verknüpfungen sowie von manchen Browsern als Zwischengröße genutzt [Ungeprüft, Q18]. Das deckt sich mit dem oben belegten Mehrgrößen-`favicon.ico` (16/32/48) als praktischem Kompromiss, ist aber selbst nicht Google- oder MDN-belegt.

### 1.6 Veraltetes: mask-icon und browserconfig.xml

`rel="mask-icon"` (Safari Pinned-Tab-Icon, SVG mit `color`-Attribut) war ab OS X 10.11 nötig, weil Safari für angeheftete Tabs kein reguläres Favicon nutzte. Seit Safari 12 fällt Safari bei fehlendem `mask-icon` auf das reguläre Favicon zurück; ein `mask-icon` ist seither nur noch nötig, wenn die exakte Tab-Farbe kontrolliert werden soll, nicht mehr zur Grundfunktion [Sekundär, Q19, seit Safari 12/2018]. Selbst apple.com verwendet laut derselben Quelle inzwischen keinen `mask-icon` mehr [Sekundär, Q19].

`browserconfig.xml` mit `msapplication-TileImage` diente IE11 und dem alten EdgeHTML-basierten Edge zur Kachel-Darstellung beim Anheften an den Windows-Startbildschirm. Laut Microsofts eigener (als „Previous versions"/Altdokumentation geführter) Seite ist der Mechanismus an IE11/Windows 8.1/10 gebunden [Sekundär, Q20]. Der heutige Chromium-basierte Edge (seit 2020) hat dieses Kachel-System nicht mehr; eine explizite Primärquelle, die das Abschalten in Chromium-Edge datiert, ließ sich in dieser Recherche nicht finden, die Einschätzung „für aktuelle Projekte nicht mehr nötig" stützt sich auf die Alteinstufung der Microsoft-Doku plus die allgemein bekannte Umstellung von Edge auf Chromium [Ungeprüft, Q20]. Für ein 2026er-Projekt: `browserconfig.xml` **weglassen**, `[Veraltet]` seit dem EdgeHTML-Ende (2020).

## 2. App-Icon-Specs

### 2.1 iOS, iPadOS, macOS (Apple)

Apples eigene HIG-Seite zu App-Icons (`developer.apple.com/design/human-interface-guidelines/app-icons`) liefert bei direktem Abruf nur den Seitentitel zurück, der Seiteninhalt wird clientseitig nachgeladen und war mit den hier verfügbaren Werkzeugen nicht als Text extrahierbar [Ungeprüft, Quelle nicht auslesbar]. Die folgenden Angaben stammen stattdessen aus einem auf GitHub gespiegelten Abzug der offiziellen Apple-Doku-Texte (`Xcode/configuring-your-app-icon.md` und `Xcode/creating-your-app-icon-using-icon-composer.md`); das ist kein Apple-eigener Server, sondern eine Drittkopie, inhaltlich aber Apple-Dokumentationstext und daher als `[Spec]` mit Einschränkung geführt (Herkunft nicht am Ursprungsort verifizierbar):

- Ein einzelnes Quellbild reicht: „auto-generate all icon variations from a single 1024×1024 pixel image" für iOS, iPadOS, tvOS, watchOS; „this is the default behavior" in Xcode [Spec*, Q3]. Für visionOS ebenfalls „a single 1024×1024 pixel asset" [Spec*, Q3].
- macOS und tvOS brauchen dagegen weiterhin einen eigenen Asset-Satz je Größe („you need to supply an asset for each size") [Spec*, Q3]. visionOS und tvOS verwenden zusätzlich einen Stapel aus mehreren Bildebenen (bis zu 3 Ebenen bei visionOS, bis zu 5 bei tvOS) [Spec*, Q3].
- Aussehen-Varianten (Appearances) bei iOS/iPadOS seit iOS 18 (2024): **Light** (Standard, hell), **Dark** („provide your dark app icon with a transparent background so the system-provided background can show through“), **Tinted** („provide your tinted app icon as a grayscale image“) [Spec*, Q3]. Zur Benennung: Q3 schreibt wörtlich „iOS and iPadOS support three stylistic variations for app icons: Light, Dark, and Tinted“. Die verbreitete Bezeichnung **Any** stammt **nicht** aus Apples Dokumentation, sie ist der Feldname im Attributinspektor von Xcode [Sekundär].
- Alphakanal: belegt ist allein, dass die Dark-Variante mit transparentem Hintergrund geliefert wird und die Tinted-Variante als Graustufenbild [Spec*, Q3]. Die weitergehende Aussage, Light und Tinted müssten einen vollen, alphakanalfreien 1024×1024-Hintergrund liefern, steht so **nicht** in Q3, sie ist eine eigene Schlussfolgerung [Ungeprüft].
- Eckenradius/Maskierung: das System wendet automatisch eine plattformtypische Maske an („automatically generated treatment that is applied to all app icons … crafted intelligently to preserve design intent and maintain legibility"), das Quellbild selbst bleibt eckig [Spec*, Q3].
- **Icon Composer** (vorgestellt WWDC 2025, für iOS/iPadOS/macOS/watchOS-Icons mit „Liquid Glass"-Optik ab iOS 26/2025): erzeugt aus Ebenen eine mehrschichtige Icon-Datei, die mehrere Erscheinungsmodi in einer Datei bündelt. Laut Mirror-Dokumentation Modi „default, dark, mono" auf iOS/macOS, „mono" wiederum mit Clear- und Tinted-Varianten in Hell/Dunkel [Spec*, Q4]. Exportgrößen: iPhone/iPad/Mac-Leinwand 1024×1024, Apple-Watch-Leinwand 1088×1088 [Spec*, Q4]. Unterstützte Ebenenformate: SVG bevorzugt (Vektor), PNG/Raster für nicht-vektorfähige Effekte [Spec*, Q4]. Maximal vier Ebenengruppen [Spec*, Q4]. Das Tool generiert laut derselben Quelle automatisch abwärtskompatible Assets für ältere OS-Versionen ohne Liquid-Glass-Unterstützung [Spec*, Q4].
- Ergänzend aus WWDC25-Sessionankündigung (nur Titel/Snippet gesehen, nicht Volltext geprüft): „Icon Composer pairs with your existing design tool … create a single icon file that adapts to multiple Apple platforms … and appearance modes, including dark, tinted, and clear light/dark", mit sechs benannten Modi Default, Dark, Clear Light, Clear Dark, Tinted Light, Tinted Dark [Sekundär, aus Suchergebnis-Zusammenfassung, nicht direkt von developer.apple.com/videos abgerufen].

Geprüft zum 2026-09-08. Versionsabhängigkeit hier besonders hoch: die Any/Dark/Tinted-Logik gilt seit iOS 18 (2024), Icon Composer und die sechs Liquid-Glass-Modi seit iOS/iPadOS/macOS 26 (2025); ein Projekt, das nur ältere iOS-Versionen unterstützen muss, braucht nur das einzelne 1024×1024-Quellbild ohne Varianten.

### 2.2 Android

Von `developer.android.com/develop/ui/views/launch/icon_design_adaptive` live abgerufen:

| Maß | Wert | Beleg |
|---|---|---|
| Gesamtfläche des adaptiven Icons | 108×108 dp | [Spec, Q6] |
| Sichtbarer Bereich (Safe Zone) | 66×66 dp, zentriert | [Spec, Q6] |
| Reservierter Außenbereich | 18 dp je Seite (für Maskierung/Effekte) | [Spec, Q6] |
| Logo-Mindestgröße | 48×48 dp | [Spec, Q6] |
| Logo-Höchstgröße | 66×66 dp (Grenze der maskierten Sichtfläche) | [Spec, Q6] |

Struktur: zwei Ebenen für die Farbversion, **Foreground** (Icon-Inhalt) und **Background** (Hintergrundfarbe/-form), beide 108×108 dp, als Vektor oder Bitmap [Spec, Q6]. XML-Deklaration unter `res/mipmap-anydpi-v26/ic_launcher.xml`:

```xml
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_launcher_foreground" />
    <monochrome android:drawable="@drawable/ic_launcher_foreground" />
</adaptive-icon>
```

[Spec, Q6].

**Themed Icons** (nutzerseitiges Theming ab Android 13): eine einzelne monochrome Ebene (`monochrome`-Tag oben) erlaubt dem System, Hintergrundbild- und Themenfarben auf das Icon anzuwenden [Spec, Q6]. Ab „Android 16 QPR 2" werden laut derselben Quelle auch Apps ohne eigene monochrome Ebene automatisch themed [Spec, Q6]. Eine eigene, tiefer gehende Seite speziell zu Themed Icons (`developer.android.com/about/versions/13/features/themed-app-icons`) lieferte bei Abruf einen 404 [Ungeprüft, Seite unter dieser URL nicht mehr vorhanden oder verschoben]; die obigen Angaben stammen vollständig von der Adaptive-Icons-Hauptseite.

### 2.3 PWA: maskable Icons, Manifest, Mindestgrößen

Safe Zone laut web.dev: „The important parts of your icon, such as your logo, must be within a circular area in the center of the icon with a radius equal to 40% of the icon width." Der äußere Rand von 10 % kann auf manchen Plattformen abgeschnitten werden [Spec, Q7]. Bezogen auf ein 512×512-Icon entspricht der Sicherheitskreis damit einem Durchmesser von 409,6 px, was sich mit der sekundär gefundenen Zahl „zentraler Kreis von 409×409" deckt [Sekundär, Q16, konsistent mit Q7].

`purpose`-Werte im Manifest laut W3C-Spezifikation (`www.w3.org/TR/appmanifest/`): **any** (Standard, keine besonderen Einschränkungen), **maskable** („designed with icon masks and safe zone in mind", Inhalt außerhalb der Safe Zone darf wegmaskiert werden), **monochrome** (Graustufen-Icon, „only the alpha data is used") [Spec, Q9]. Die Spezifikation selbst nennt keine Pflichtgrößen wie 192×192/512×512, führt aber `sizes`, `src`, `type`, `purpose` als Struktur des Icon-Objekts [Spec, Q9].

Mindestgrößen 192 und 512 sind eine Chromium-/web.dev-Empfehlung, keine Manifest-Spec-Pflicht: „For Chromium, you must provide at least a 192x192 pixel icon and a 512x512 pixel icon." Installierbarkeit ist davon laut derselben Quelle nicht hart abhängig: „Users can install your web app even if it doesn't meet the installability criteria in Chrome" [Spec, Q8]. Empfehlung bei eigenem Zuschnitt: Schrittweite von 48 dp [Spec, Q8]. SVG-Icons werden von Chromium unterstützt, ein Raster-Fallback wird für Browser ohne SVG-Icon-Unterstützung empfohlen [Spec, Q8].

Kombination der Purpose-Werte: `"purpose": "any maskable"` ist laut web.dev die Schreibweise, um ein Icon für beide Zwecke zu nutzen [Spec, Q7], wird aber für echte maskable Icons davon abgeraten, weil das unnötiges Padding erzwingt und den Icon-Inhalt kleiner macht [Spec, Q7]. Praxisnahes Manifest-Fragment (aus Sekundärquelle, Struktur deckt sich mit der W3C-Spec):

```json
{
  "icons": [
    { "src": "/icon-192.png", "type": "image/png", "sizes": "192x192" },
    { "src": "/icon-512.png", "type": "image/png", "sizes": "512x512" },
    { "src": "/icon-mask.png", "type": "image/png", "sizes": "512x512", "purpose": "maskable" }
  ]
}
```

[Sekundär, Q16, Feldnamen durch Q7/Q9 gedeckt].

### 2.4 Windows Tiles und macOS: nur soweit noch relevant

Windows-Kacheln (`browserconfig.xml`, `msapplication-TileImage`) siehe Abschnitt 1.6: `[Veraltet]` für aktuelle Projekte, gebunden an IE11/altes Edge.

Für macOS als App-Plattform (nicht Web-Favicon) gilt dieselbe 1024×1024-Ausgangslogik wie iOS, allerdings ohne automatische Größengenerierung: „you need to supply an asset for each size" [Spec*, Q3]. Für eine reine Web-Auslieferung ist macOS/Safari durch den regulären Favicon- und `apple-touch-icon`-Satz aus Abschnitt 1 abgedeckt, ein gesondertes macOS-Icon-Set ist nur bei einer nativen App nötig.

## 3. Banner-Maße

### 3.1 Open Graph (ogp.me)

Pflicht-Properties laut ogp.me: `og:title`, `og:type`, `og:image`, `og:url` sind die vier grundsätzlich erforderlichen Properties, `og:image` gehört dazu [Spec, Q10]. Optionale, strukturierte Bild-Properties: `og:image:url` (identisch zu `og:image`), `og:image:secure_url`, `og:image:type` (MIME-Typ), `og:image:width`, `og:image:height`, `og:image:alt` [Spec, Q10]. Beispielmarkup wörtlich:

```html
<meta property="og:image" content="http://example.com/ogp.jpg" />
<meta property="og:image:secure_url" content="https://secure.example.com/ogp.jpg" />
<meta property="og:image:type" content="image/jpeg" />
<meta property="og:image:width" content="400" />
<meta property="og:image:height" content="300" />
<meta property="og:image:alt" content="A shiny red apple with a bite taken out" />
```

[Spec, Q10]. Die ogp.me-Spezifikation selbst nennt **keine** empfohlenen Bildmaße [Spec, Q10, explizit als Lücke in der Primärquelle].

Konkrete Maße kommen von Meta/Facebook, live abgerufen von developers.facebook.com: empfohlen „at least 1200 x 630 pixels for the best display on high resolution devices" [Spec, Q11]. Mindestmaße: „The minimum allowed image dimension is 200 x 200 pixels", für Beitragsvorschauen mit größerem Bild „600 x 315 pixels to display link page posts with larger images" [Spec, Q11]. Seitenverhältnis: „Try to keep your images as close to 1.91:1 aspect ratio as possible to display the full image in Feed without any cropping" [Spec, Q11]. Dateigrößengrenze: „The size of the image file must not exceed 8 MB" [Spec, Q11].

Unterstützte Formate laut derselben Facebook-Dokumentationsfamilie (Seite „sharing/webmasters", nicht die Bildmaß-Unterseite): explizit genannt werden JPEG (`image/jpeg`), GIF (`image/gif`), PNG (`image/png`) [Spec, Q12]. WebP oder AVIF werden dort **nicht** erwähnt [Spec, Q12, Abwesenheit als Befund]. Der Facebook-Crawler identifiziert sich als `facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)` und verlangt vom Server Unterstützung für gzip/deflate [Spec, Q12].

Praxisrichtwert für ein Projekt ohne plattformspezifische Varianten: **1200×630 px, 1.91:1, JPEG oder PNG, unter 8 MB.**

### 3.2 X/Twitter Card

Primärquelle nicht erreichbar: `developer.x.com/en/docs/x-for-websites/cards/overview/markup` und `developer.twitter.com/.../markup` lieferten bei Abruf einen HTTP-402-Fehler bzw. eine Weiterleitung auf `docs.x.com`, das als reine API-Produkt-Dokumentation ohne die alte „Cards for Websites"-Sektion erscheint; im dortigen Dokumentationsindex (`docs.x.com/llms.txt`) ließ sich kein Eintrag zu „Cards" finden [Ungeprüft, Primärquelle am 2026-09-08 nicht auffindbar bzw. nicht erreichbar]. Die alte Cards-für-Websites-Dokumentation könnte damit aus der aktuellen X-Doku entfernt oder verschoben worden sein; das konnte in dieser Recherche nicht abschließend geklärt werden.

Die folgenden Zahlen stammen ausschließlich aus mehreren, sich teils widersprechenden Sekundärquellen und sind entsprechend nur `[Sekundär]`/`[Ungeprüft]` zu werten:

| Angabe | Wert laut Sekundärquellen | Belastbarkeit |
|---|---|---|
| `summary_large_image`, empfohlene Maße | uneinheitlich zwischen 1200×630, 1200×628 und 1200×675 genannt | [Ungeprüft, widersprüchlich] |
| `summary_large_image`, Seitenverhältnis | teils 1.91:1, teils 2:1 genannt | [Ungeprüft, widersprüchlich] |
| `summary_large_image`, Mindestmaß | 300×157 px | [Ungeprüft] |
| `summary` (kleines Bild), Maß/Verhältnis | 1:1, Mindestgröße 144×144, empfohlen ab 400×400 für Retina | [Ungeprüft] |
| Bildgrößen-Spanne insgesamt | 144×144 bis 4096×4096 | [Ungeprüft] |
| Dateigrößengrenze | 5 MB | [Ungeprüft] |
| unterstützte Formate | JPG, PNG, WebP, GIF (nur erstes Frame) | [Ungeprüft] |

Beispielmarkup (aus Sekundärquellen zusammengesetzt, Feldnamen entsprechen dem allgemein bekannten Schema, aber nicht aus einer heute erreichbaren Primärquelle geprüft):

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Titel der Seite" />
<meta name="twitter:description" content="Beschreibung" />
<meta name="twitter:image" content="https://beispiel.de/bild.png" />
<meta name="twitter:image:alt" content="Bildbeschreibung" />
```

[Ungeprüft, Q22]. Bekannt und nicht strittig: fehlen `twitter:title`/`twitter:description`, greift X als Fallback auf die entsprechenden `og:title`/`og:description`-Werte zurück [Sekundär, Q22], das Bild dagegen offenbar nicht durchgängig, weshalb ein eigenes `twitter:image` empfohlen wird [Sekundär, Q22].

### 3.3 LinkedIn

Von linkedin.com/help live abgerufen: Mindestmaße „1200 (w) x 627 (h) pixels", empfohlenes Seitenverhältnis „1.91:1" [Spec, Q13]. Bilder unter 401 px Breite werden nur als Thumbnail dargestellt [Spec, Q13]. LinkedIn nutzt für die Vorschau dieselben Open-Graph-Tags wie Facebook (`og:image` etc.), es gibt kein eigenes `linkedin:image`-Tag [Spec, Q13, aus Kontext der Seite].

Praxisrichtwert LinkedIn: **1200×627 px, 1.91:1**, das liegt praktisch auf dem Facebook-Maß (1200×630), ein gemeinsames OG-Bild von 1200×630 bedient beide Plattformen.

### 3.4 IAB-Standardformate für Werbebanner

Primärquelle: „Fixed Size Ad Specifications" der IAB New Ad Portfolio, PDF von iab.com (© 2017 IAB Technology Laboratory), per `pdftotext` ausgelesen:

| Ad-Unit-Name | Feste Größe (px) | Max. Initial-Load (kB) | Max. Subload (kB) |
|---|---|---|---|
| Billboard | 970×250 | 250 | 500 |
| Smartphone Banner | 300×50 oder 320×50 | 50 | 100 |
| Leaderboard | 728×90 | 150 | 300 |
| Super Leaderboard / Pushdown | 970×90 | 200 | 400 |
| Portrait | 300×1050 | 250 | 500 |
| Skyscraper | 160×600 | 150 | 300 |
| Medium Rectangle | 300×250 | 150 | 300 |
| (unbenannt, „20x60") | 120×60 | 50 | 100 |
| Mobile Phone Interstitial | 640×1136, 750×1334 oder 1080×1920 | 300 | 600 |
| Feature Phone Small Banner | 120×20 | 5 | n/v |
| Feature Phone Medium Banner | 168×28 | 5 | n/v |
| Feature Phone Large Banner | 216×36 | 5 | n/v |

[Spec, Q14]. Größenberechnung: die Fixed-Size-Angaben gelten bei doppelter Dichte (2x), Beispiel 728×90 wird für die Rastergrößen-Einordnung als 728×90×4 = 262.080 Pixel gerechnet [Spec, Q14].

Wichtiger Befund zur Formatfalle bei „gängigen" Bannergrößen: viele Blogs listen zusätzlich 336×280 (Large Rectangle), 300×600 (Half Page) und 320×100 als „IAB-Standard". In der hier ausgelesenen offiziellen „New Ad Portfolio"-Spezifikation (2017, das aktuell von IAB verlinkte Fixed-Size-Dokument) tauchen diese drei **nicht** auf, nur Medium Rectangle (300×250), Skyscraper (160×600) und die oben gelistete Auswahl [Spec, Q14]. 336×280, 300×600, 320×100 stammen aus dem älteren, vor 2017 gültigen IAB-Größenkatalog und sind gegenüber der geprüften aktuellen Spezifikation `[Veraltet]`, auch wenn sie im programmatischen Anzeigenhandel weiterhin verbreitet vorkommen (das bestätigt eine begleitend abgerufene Sekundärquelle, ohne eigene Primärbelegzahl: „diversifying your ad inventory" nennt 320×50 als weiterhin relevant, IAB selbst schiebt den Fokus laut TechLab-FAQ inzwischen von festen Pixelgrößen auf flexible, seitenverhältnisbasierte Größenraster [Spec, Q15]).

Ergänzend aus derselben PDF-Quelle: „Interest-Based Advertising (IBA)"-Kennzeichnungspflicht bei verhaltensbasiertem Targeting (max. 5 kB), Audio in Anzeigen muss stummgeschaltet starten, maximal zehn hostinitiierte Dateianfragen beim Initial Load, CPU-Last-Obergrenze 30 % [Spec, Q14].

Geprüft zum 2026-09-08. Versionsabhängigkeit: Die 2017er New-Ad-Portfolio-Spezifikation ist die aktuell von iab.com verlinkte Fixed-Size-Referenz, das TechLab-FAQ-Dokument (undatiert eingesehen) beschreibt bereits eine Weiterentwicklung hin zu flexiblen, aspektverhältnisbasierten Rastern statt starrer Pixelgrößen [Spec, Q15]; ein neueres, vollständig flexibles Nachfolgedokument mit anderen Zahlen ist nicht auszuschließen und wurde in dieser Recherche nicht gefunden.

### 3.5 Formatfalle: WebP und AVIF bei Crawlern und Vorschaudiensten

Einzige direkt primärquellig geprüfte Aussage: Facebooks eigene Sharing-Dokumentation nennt für `og:image:type` ausdrücklich nur JPEG, GIF und PNG als Beispiel-MIME-Typen, WebP und AVIF werden dort nicht erwähnt [Spec, Q12, Abwesenheit als Befund, keine explizite Ausschlussaussage]. Das ist kein Beleg dafür, dass WebP/AVIF *nicht* funktionieren, nur dass sie offiziell nicht dokumentiert sind.

Alle konkreteren Aussagen zu WebP/AVIF-Unterstützung einzelner Crawler (Facebook, X, LinkedIn, Slack, Discord) stammen ausschließlich aus Blog-Tests Dritter und sind untereinander uneinheitlich: eine Quelle behauptet WebP funktioniere bei Facebook, X, LinkedIn, Slack, Discord, AVIF dagegen nur bei Facebook zuverlässig, während eine andere Quelle die Aussage trifft, aktuell könne AVIF bei keinem getesteten Anbieter zuverlässig verwendet werden [Ungeprüft, Q21, widersprüchliche Sekundärlage]. Für die Regeldatei folgt daraus: **als sicheren Standard JPEG oder PNG für `og:image` verwenden**, WebP nur mit Fallback-Strategie, AVIF für Social-Preview-Bilder vermeiden, weil keine der geprüften Primärquellen (Meta, ogp.me) es dokumentiert.

## Quellen

| Nr | Quelle | URL | abgerufen | was daraus stammt |
|---|---|---|---|---|
| Q1 | MDN, `<link>`-Referenz | https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link | 2026-09-08 | `rel="icon"`/`apple-touch-icon`-Markup, `sizes`-Attribut, CSP-Hinweis zu Favicons |
| Q2 | Google Search Central, Favicon in der Suche | https://developers.google.com/search/docs/appearance/favicon-in-search | 2026-09-08 | Mindestgröße 8×8px, Empfehlung >48×48px, Formate, Crawlbarkeit, unterstützte `rel`-Werte |
| Q3 | Apple-Doku-Textabzug (GitHub-Mirror), „Configuring your app icon" | https://raw.githubusercontent.com/livingston/apple-docs/main/documentation/Xcode/configuring-your-app-icon.md | 2026-09-08 | 1024×1024-Quellbild, Any/Dark/Tinted-Appearances, Alphakanal-Regeln, macOS/tvOS-Sonderfall |
| Q4 | Apple-Doku-Textabzug (GitHub-Mirror), „Creating your app icon using Icon Composer" | https://raw.githubusercontent.com/livingston/apple-docs/main/documentation/Xcode/creating-your-app-icon-using-icon-composer.md | 2026-09-08 | Icon Composer, Erscheinungsmodi, Exportgrößen 1024/1088 |
| Q5 | Apple HIG „App icons" (Originalseite, Inhalt nicht extrahierbar) | https://developer.apple.com/design/human-interface-guidelines/app-icons | 2026-09-08 | nur als Referenz genannt, Inhalt nicht auslesbar |
| Q6 | Android Developers, Adaptive Icons | https://developer.android.com/develop/ui/views/launch/icon_design_adaptive | 2026-09-08 | 108/66/18 dp, Foreground/Background-Ebenen, Themed Icons, XML-Beispiel |
| Q7 | web.dev, Maskable icon | https://web.dev/articles/maskable-icon | 2026-09-08 | Safe-Zone 40 %/10 %, `purpose`-Kombination, Empfehlung gegen „any maskable" bei echten maskable Icons |
| Q8 | web.dev, Add a web app manifest | https://web.dev/articles/add-manifest | 2026-09-08 | 192/512-Empfehlung für Chromium, Installierbarkeit, SVG-Fallback-Hinweis |
| Q9 | W3C, Web App Manifest (TR) | https://www.w3.org/TR/appmanifest/ | 2026-09-08 | `purpose`-Werte any/maskable/monochrome, Icon-Objektstruktur |
| Q10 | ogp.me | https://ogp.me/ | 2026-09-08 | Pflicht-Properties, `og:image`-Unterproperties, Beispielmarkup |
| Q11 | Meta for Developers, Sharing images | https://developers.facebook.com/docs/sharing/webmasters/images | 2026-09-08 | 1200×630 empfohlen, 200×200 Minimum, 1.91:1, 8 MB Grenze |
| Q12 | Meta for Developers, Sharing/Webmasters | https://developers.facebook.com/docs/sharing/webmasters/ | 2026-09-08 | og:image-Formate JPEG/GIF/PNG, Crawler-User-Agent |
| Q13 | LinkedIn Help | https://www.linkedin.com/help/linkedin/answer/a521928 | 2026-09-08 | 1200×627 Minimum, 1.91:1, 401px-Thumbnail-Schwelle |
| Q14 | IAB Technology Laboratory, New Ad Portfolio, Fixed Size Ad Specifications (PDF) | https://www.iab.com/wp-content/uploads/2019/04/IABNewAdPortfolio_LW_FixedSizeSpec.pdf | 2026-09-08 | Tabelle der Fixed-Size-Ad-Units, kB-Grenzen, 2x-Dichte-Berechnung |
| Q15 | IAB TechLab, FAQ New Ad Portfolio | https://interactiveadvertisingbureau.github.io/TechLabFAQ/docs/faq-new-ad-portfolio.html | 2026-09-08 | Umstieg von festen Pixelgrößen auf flexible aspektverhältnisbasierte Raster |
| Q16 | Evil Martians, „How to Favicon in 2021" | https://evilmartians.com/chronicles/how-to-favicon-in-2021-six-files-that-fit-most-needs | 2026-09-08 | Minimalsatz-Empfehlung, SVG-Dark-Mode-Technik, Apple-Touch-Icon-Padding-Hinweis, Manifest-Beispiel |
| Q17 | mehrere sich überschneidende Blog-/Guide-Quellen (u. a. owenconti.com, jwtoolbox.com, proicons.com) | diverse | 2026-09-08 | SVG-Favicon-Browserverhalten inkl. Safari-Sonderfall, als Sekundärlage ohne Primärabgleich |
| Q18 | favicon.io u. a. Generator-/Guide-Seiten | https://favicon.io/tutorials/favicon-sizes/ und ähnliche | 2026-09-08 | Erklärung 32px/48px-Nutzung durch Browser/Windows, unbelegt gegenüber Primärquelle |
| Q19 | GitHub-Issue-Diskussion und Yoast Dev Blog zu Safari mask-icon | https://github.com/gethomepage/homepage/issues/2323, https://yoast.com/developer-blog/safari-pinned-tab-icon-mask-icon/ | 2026-09-08 | Status mask-icon seit Safari 12, apple.com-Praxisbeispiel |
| Q20 | Microsoft Learn (Altdokumentation) und h5bp-Diskussion zu browserconfig.xml | https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/dn255024%28v=vs.85%29, https://github.com/h5bp/html5-boilerplate/pull/1697 | 2026-09-08 | Bindung an IE11/altes Edge, Diskussion um Ablösung durch Manifest |
| Q21 | mehrere widersprüchliche Blog-Tests zu WebP/AVIF bei Social-Crawlern | u. a. ctrl.blog, darekkay.com, joost.blog | 2026-09-08 | uneinheitliche Aussagen zu WebP-/AVIF-Unterstützung, als Formatfalle markiert |
| Q22 | mehrere widersprüchliche Guide-Seiten zu X/Twitter-Card-Maßen | u. a. og-image.org, screenhance.com, ogimage.io, opengraphplus.com | 2026-09-08 | Card-Maße und -Markup, da developer.x.com/docs.x.com am 2026-09-08 keine erreichbare Primärquelle lieferten |
