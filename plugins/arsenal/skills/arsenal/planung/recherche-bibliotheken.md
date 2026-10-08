# Recherche: Kostenlose Quellen für UI, Bilder, Video, Icons, Schriften (Stand September 2026)

Grundlage für den Claude Code Skill `arsenal`. Bereits abgedeckt und nicht wiederholt: shadcn/ui, Radix, Aceternity UI, Magic UI, Origin UI, Originkit, 21st.dev, HeroUI, Awwwards, Mobbin, Land book, Recent Design, Siteinspire. Alle Angaben live per WebSearch/WebFetch geprüft.

## 1. UI Elemente: weitere freie Quellen

Geprüft wurden Motion Primitives, Cult UI, Uiverse, React Bits, Tailark, Skiper UI, Animata. Alle sieben existieren im September 2026 noch und sind kostenlos nutzbar. Fünf erreichen das Niveau von originkit.dev, getlayers.ai und manus.im, zwei sind für den Skill nur eingeschränkt brauchbar.

**Motion Primitives** (https://motion-primitives.com/, Code https://github.com/ibelick/motion-primitives). Über 50 animierte React/Next.js/Tailwind Komponenten, Kernbibliothek MIT lizenziert, komplett kostenlos. Installation per `npm i motion-primitives` oder Copy Paste aus der Doku. Geeignet für Dock Menüs, Text und Scroll Animationen, Glassmorphism Effekte. Eine separate Pro Ebene mit fertigen Templates existiert unter pro.motion-primitives.com, für den Skill reicht die freie Basis.

**Cult UI** (https://www.cult-ui.com/, Code https://github.com/nolly-studio/cult-ui). Komponentenbibliothek für shadcn/ui, MIT lizenziert im freien Kern, Installation über die shadcn CLI (Registry kompatibel) oder Copy Paste. Stark bei Micro Interactions und Framer Motion basierten Animationen, etwa Textwechsel oder Karten mit Tiefeneffekt. Eine Pro Version (pro.cult-ui.com) verbietet Weiterverkauf und Ableitung eigener Kits, betrifft den freien Teil aber nicht.

**React Bits** (https://reactbits.dev/, Code https://github.com/DavidHDev/react-bits). Über 110 animierte, interaktive React Komponenten, Lizenz MIT plus Commons Clause: frei nutzbar und modifizierbar auch kommerziell, nur der Weiterverkauf der Bibliothek selbst als Produkt ist untersagt. Installation per CLI Tool (jsrepo) oder Copy Paste, wahlweise mit oder ohne TypeScript, mit CSS oder Tailwind. Besonders stark bei Text Animationen, WebGL artigen Hintergrundeffekten und komplexen Hover States. 2026 Platz 2 in den JS Rising Stars, aktiv gepflegt. Eine Pro Version mit 134 weiteren Komponenten existiert separat.

**Tailark** (https://tailark.com/, Code https://github.com/tailark/blocks). Shadcn Registry für Marketing Blocks, komplett MIT lizenziert, Installation über die shadcn CLI direkt aus der Registry. Kein Animationsfokus, sondern fertige, konversionsoptimierte Sektionen wie Hero, Pricing, Testimonials, Footer. Dient eher der strukturellen als der choreografischen Qualität.

**Animata** (https://animata.design/, Code via GitHub, Studio Codse). Handgefertigte, theme aware Animationen und Komponenten in React, Tailwind, TypeScript, komplett MIT und open source, Copy Paste Modell plus optionale shadcn Registry Installation. Stark bei Border Effekten, Bento Grids, Widget Karten, Text Mirror Effekten.

Nicht als Hauptquelle empfohlen: **Uiverse.io** (https://uiverse.io/) ist MIT lizenziert und mit über 4000 Elementen die größte freie Sammlung, aber reine CSS/HTML Snippets von wechselnder Qualität ohne React Choreografie, eher Fundus für einzelne Buttons oder Inputs als für System Qualität. **Skiper UI** (https://skiper-ui.com/) hat nur 24 freie Komponenten, der Großteil (73 Premium Komponenten) kostet einmalig 129 US Dollar, daher nur eingeschränkt brauchbar.

### Warum wirkt fertiger Code aus diesen Quellen besser als Standard LLM Output

**Choreografie.** Diese Bibliotheken staffeln Animationen bewusst über definierte Stagger Delays (in Framer Motion via `staggerChildren`, in React Bits oft über Index basierte delay Props). Ein LLM ohne Referenz lässt Elemente meist gleichzeitig oder in willkürlicher Reihenfolge erscheinen.

**Easing.** Praktisch alle genannten Bibliotheken setzen auf Framer Motion mit physikalischen Spring Kurven (Masse, Steifigkeit, Dämpfung statt fixer Dauer), das erzeugt organische Bewegung mit leichtem Überschwingen. LLM Code verwendet reflexhaft `ease in out` oder `linear` mit fester Millisekundenzahl, was mechanisch wirkt.

**Abstände.** Die Komponenten folgen einem konsistenten Tailwind Token Raster (4px Basis, feste Abstufungen für Padding zwischen Icon, Label und Rand). LLM generierte Layouts variieren Abstände pro Komponente uneinheitlich.

**Zustände.** Die Bibliotheken liefern hover, focus, active, disabled, loading und teils empty States von Anfang an mit durchdachten Übergängen, weil sie für echten Produktiveinsatz gebaut wurden. Ein LLM implementiert im ersten Wurf meist nur den Grundzustand und höchstens hover, focus visible und Ladezustände fehlen häufig.

## 2. Stock Bilder

**Unsplash** (Lizenz https://unsplash.com/license, API Terms https://unsplash.com/api-terms). Die Unsplash Lizenz erlaubt kommerzielle und nicht kommerzielle Nutzung kostenlos, bei normalem Download ist keine Attribution nötig. Bei API Nutzung ist Attribution von Unsplash und Fotograf inklusive Rücklink zum Profil verpflichtend (sonst API Sperre), Format mit utm_source/utm_medium=referral (siehe https://help.unsplash.com/en/articles/2511315-guideline-attribution). Verboten: Weiterverkauf unveränderter Bilder als Stockware, Nachbau eines konkurrierenden Bilderdienstes durch Massensammlung. API Key kostenlos, Demo Modus mit niedrigem Rate Limit, Production Zugang auf Anfrage mit höherem Limit. Unsplash+ (kostenpflichtig) schließt zusätzlich KI Trainingsnutzung ausdrücklich aus (https://unsplash.com/plus/license), die kostenlose Basis äußert sich dazu nicht ausdrücklich.

**Pexels** (Lizenz https://www.pexels.com/license/, API https://www.pexels.com/api/documentation/). Kommerzielle und private Nutzung ohne Attribution erlaubt. Verboten ist eigenständiger Weiterverkauf oder Vertrieb (Poster, Wallpaper, Merchandise ohne wesentliche kreative Bearbeitung) sowie Verkauf auf anderen Stockplattformen. API kostenlos, Standardlimit 200 Anfragen pro Stunde und 20.000 pro Monat, Erhöhung auf Anfrage kostenlos (https://help.pexels.com/hc/en-us/articles/900005851863). Zur KI Trainingsnutzung existiert eine eigene FAQ (https://help.pexels.com/hc/en-us/articles/27292485713945-AI-and-ML-FAQ) ohne klares Verbot.

**Pixabay** (Content License https://pixabay.com/service/license-summary/, API https://pixabay.com/service/about/api/). Drei Lizenz Ären: vor 2019 CC0, 2019 bis April 2023 Pixabay License (Verbot von Standalone Verkauf), seit 17.04.2023 Content License mit CC0 artiger Rückkehr, KI generierte Uploads jetzt erlaubt. Aktuell: unwiderrufliches, weltweites, gebührenfreies Nutzungsrecht kommerziell und privat, keine Attribution nötig. KI Training ist bei Pixabay ausdrücklich gestattet, mit Opt out Möglichkeit für Urheber, das ist ein Gegensatz zu Unsplash+. API kostenlos und praktisch unlimitiert, keine Attribution bei API Nutzung nötig. Pixabay liegt zusätzlich bereits als MCP Server im System vor (`mcp__claude_ai_Pixabay__search_images`, `search_videos`, `download_image`), im Arsenal Skill direkt nutzbar ohne Extra Setup.

## 3. Stock Video

**Coverr** (https://coverr.co/license, https://coverr.co/terms). Unwiderrufliche, nicht exklusive, weltweite Lizenz für Download, Modifikation und kommerzielle Nutzung ohne Attribution und ohne Wasserzeichen. Verboten: Weiterverkauf oder Redistribution als eigenständiges Produkt, Nutzung auf konkurrierenden Stock oder Website Builder Diensten, und explizit KI Training beziehungsweise Dataset Nutzung.

**Mixkit** (https://mixkit.co/free-stock-video/, Lizenzinfo https://mixkit.co/llm-info/). Freie Lizenz für die meisten Videos, kommerziell nutzbar ohne Attribution, kein Wasserzeichen. Einzelne Clips stehen unter restriktiverer Lizenz nur für private oder edukative Zwecke, im UI gekennzeichnet, vor Download prüfen. Kein Aufbau eines Konkurrenzdienstes, keine Rohdatei Weitergabe.

**Videvo.** Stand 2026 kein eigenständiger Dienst mehr, die Marke wurde in Freepik/Magnific integriert. Die klassische kostenlose Attribution Lizenz existiert nur noch im Freepik Ökosystem, oft hinter Account oder Abo Schranken (siehe https://photutorial.com/videvo-net-review/). Als eigenständige freie Quelle 2026 nicht mehr verlässlich.

**Pexels Video** (https://www.pexels.com/license/). Gleiche Lizenz wie Pexels Fotos, kommerziell frei, keine Attribution, kein Wasserzeichen, direkter Download in mehreren Auflösungen bis 4K, großes und wachsendes Angebot, gleiche API wie Fotos.

**Empfehlung Hauptquelle: Pexels Video.** Begründung: einzige der vier Quellen mit stabiler, seit Jahren unveränderter Lizenz ohne Attributionspflicht und ohne Sonderfälle, im Gegensatz zu Mixkits gemischten Lizenzklassen und Videvos Auflösung in Freepik. Direkter API Zugang identisch zur ohnehin genutzten Pexels Bildquelle, das vereinheitlicht den Arsenal Workflow auf einen Client und ein Regelwerk für Bild und Video. Große Auswahl bis 4K, ideal für Web Hero Videos, kein Wasserzeichen, kein Account Zwang beim Download. Coverr ist qualitativ oft cineastischer kuratiert und ebenfalls attributionsfrei, taugt als Sekundärquelle für stilistisch konsistente Loop Hintergründe, sollte wegen des expliziten KI Trainingsverbots aber nicht in KI Nachbearbeitungspipelines eingespeist werden.

## 4. KI Bilder

**Leonardo AI** (MCP Server im System vorhanden, aktuell getrennt). Free Tier mit 150 schnellen Tokens pro Tag plus 150 Token Bank ohne Ansammlung, Free Ergebnisse sind öffentlich sichtbar, IP verbleibt bei Leonardo. Bezahlpläne: Essential 12 USD/Monat (8500 Tokens), Premium 30 USD/Monat (25000 Tokens), Ultimate 60 USD/Monat (60000 Tokens), Jahreszahlung spart bis zu 20 Prozent. Stärke ist das breite Funktionsspektrum (Bild, Video, Modelltraining, Editor) plus überhaupt ein Free Tier, was Midjourney fehlt. Quellen: https://www.eesel.ai/blog/leonardo-ai-pricing, https://fluxnote.io/guides/leonardo-ai-pricing-guide-2026.

Alternativen: **Midjourney** ohne Free Tier, 10 bis 120 USD/Monat, ästhetisch oft überzeugendste Ergebnisse (https://pxlpeak.com/blog/ai-tools/midjourney-pricing-plans). **Ideogram** mit nutzbarem Free Tier und günstigen Plänen 7 bis 48 USD/Monat, stark bei Text im Bild. **Flux** (Black Forest Labs) zweigeteilt: Flux.1 schnell ist frei unter Apache 2.0, Flux.1 dev ist frei nur nichtkommerziell, über API 0,003 bis 0,05 USD pro Bild, überzeugendste Fotorealistik. Quellen: https://www.aimagicx.com/blog/midjourney-vs-flux-vs-ideogram-image-comparison-2026, https://www.layer3labs.io/comparisons/flux-alternatives.

**Kriterien KI Bild versus Stockfoto.** KI wählen bei einem spezifischen, so nicht existierenden Motiv (exakte Markenfarben, ein Wesen, ein unmögliches Szenario) oder wenn kein passendes Stockfoto existiert. Stockfoto oder eigenes Foto wählen bei Bedarf an Authentizität und Glaubwürdigkeit, etwa echte Personen, echte Orte, Testimonials, dokumentarischer Anspruch, weil KI Bilder bei genauem Hinsehen Artefakte zeigen (Hände, Text, Symmetriefehler) und als KI erkannt Vertrauen kosten. Rechtlich gilt: ein rein KI generiertes Bild ist in den meisten Rechtsordnungen, insbesondere den USA, nicht urheberrechtlich schutzfähig, das kommerzielle Nutzungsrecht kommt vertraglich vom Anbieter, nicht aus Copyright. Praktisch relevanter als Trainingsdaten Fragen sind erkennbare reale Personen ohne Einwilligung und ungewollt reproduzierte Marken oder Figuren im Bild. Für Marketing, Social Media, Website und Präsentationsgrafik gilt das Risiko 2026 als überschaubar und rückläufig. Quellen: https://lumenci.com/blogs/ai-art-intellectual-property-challenges/, https://www.lovart.ai/blog/ai-art-copyright-2026.

## 5. Icons

**Lucide** (https://lucide.dev/license, https://lucide.dev/packages, Code https://github.com/lucide-icons/lucide). Lizenz ISC, circa 1600 bis 1798 Icons, Version 1.0 seit 2026 (v1.41.0 vom 04.09.2026), Fork von Feather Icons, durchgängiger Strichstil. Pakete für React, Vue, Svelte, Solid (mit Context Providern in v1) und Angular. Standard bei shadcn/ui, daher erste Wahl in Tailwind/shadcn Projekten (https://www.infoq.com/news/2026/06/lucide-v1-icons/).

**Phosphor Icons** (MIT Lizenz). Rund 1200 Basisicons mal sechs Gewichte (Thin, Light, Regular, Bold, Fill, Duotone) ergibt über 7200 Varianten, Pakete für React, Vue, Svelte, Flutter, Elm, Web Components. Wahl bei Bedarf an Gewichts und Stilvielfalt innerhalb eines Projekts. Quelle: https://www.moonb.io/blog/icon-libraries.

**Tabler Icons** (MIT Lizenz, Code https://github.com/tabler/tabler-icons). Mit 6100 bis 6184 Icons die größte Anzahl der vier, Pakete für React, Vue, Angular, Svelte, SolidJS, React Native, plus eigenes Figma Plugin (https://tabler.io/icons/packages, Figma https://www.figma.com/community/plugin/1169807996149376642/tabler-icons). Wahl bei Bedarf an sehr breiter, seltener Icon Abdeckung, etwa Business oder Dashboard Symbole.

**Heroicons** (MIT Lizenz, Code https://github.com/tailwindlabs/heroicons). Um die 300 handgezeichnete Icons in Outline und Solid, mit Mini Variante zusammen circa 1288 Icons, von den Tailwind Machern, First Party Pakete nur für React und Vue. Wahl wenn Icons stilistisch exakt zu Tailwind/shadcn passen sollen und ein kleineres, kuratiertes Set genügt.

## 6. Schriften

**Google Fonts** (fonts.google.com). Fast durchweg SIL Open Font License, einige Apache 2.0. Uneingeschränkte kommerzielle Nutzung, Self Hosting erlaubt, keine Attribution nötig. Größter Umfang, aber Schriften wie Inter, Roboto, Open Sans gelten inzwischen als generisch beziehungsweise übernutzt, weil sie Standardauswahl vieler Tools und damit auch von LLM generierten Designs sind.

**Fontshare** (fontshare.com/licenses/itf-ffl). ITF Free Font License: kommerzielle Nutzung ausdrücklich erlaubt für Client Arbeit, verkaufte Produkte, Marketing, Web und App, einzige Einschränkung ist das Verbot, die Font Dateien selbst weiterzuverkaufen oder auf anderen Font Plattformen weiterzuverteilen. Rund 100 Familien von Indian Type Foundry, dauerhaft kostenlos, kein Nutzungslimit.

**Velvetyne Type Foundry** (velvetyne.fr/about/faq). Libre beziehungsweise open source, meist OFL artige Lizenzen mit Copyleft Charakter: Nutzung, Modifikation und Weiterverbreitung für private und kommerzielle Zwecke erlaubt, Pflicht zur Nennung von Designer und Foundry, abgeleitete Werke müssen unter derselben Lizenz weiterverbreitet werden. Das unterscheidet Velvetyne von reinem OFL ohne Copyleft.

**Open Foundry** (open-foundry.com/about). Reine Kuratierungsplattform ohne eigenes Hosting, verlinkt auf Google Fonts, GitHub und andere Quellen. Die meisten gelisteten Schriften nutzen OFL, die Lizenz ist aber je Font einzeln zu prüfen.

### 8 empfohlene, charakterstarke, lizenzsichere Alternativen zu Inter und Roboto

1. **Space Grotesk** (Google Fonts, OFL). Geometrisch, technisch kantig mit Charakter. Einsatz: Headlines, Tech und Startup Branding.
2. **Schibsted Grotesk** (Google Fonts, OFL). Grotesk mit mehr Eigenheit als Inter, ursprünglich für Medien entwickelt. Einsatz: Headlines und UI.
3. **DM Sans** (Google Fonts, OFL). Weichere Kurven, kontemporär. Einsatz: Fließtext, Produkt UI.
4. **Fraunces** (Google Fonts, OFL). Warme Editorial Serife mit optischer Größenachse. Einsatz: Display und Editorial Headlines.
5. **Tan Pearl** (über Fontshare beziehungsweise Foundry Angebote, Lizenz vor Einsatz je Quelle prüfen). Hochkontrastreiche Display Serife. Einsatz: große Display Headlines, Fashion, Beauty, Luxus.
6. **Crimson Pro** (Google Fonts, OFL). Variable Buchtext Serife mit neun Schnitten. Einsatz: Fließtext, Longform.
7. **EB Garamond** (Google Fonts, OFL). Klassische Buchserife mit offenen Formen, kombiniert gut mit modernen Grotesken. Einsatz: editorialer Fließtext.
8. **JetBrains Mono** (Google Fonts und Fontshare, OFL). Tech Mono mit Charakter statt Standardmono. Einsatz: Code, technische UI Akzente.

Für unverwechselbare Display Fälle zusätzlich gezielt bei Velvetyne suchen, dort aber die Attributions und Copyleft Pflicht der jeweiligen Schrift beachten, bevor sie in ein kommerzielles Projekt geht.

## 7. Auswahlverfahren für Bild und Video statt Klischee

**Kriterienliste.** Motiv muss den konkreten Inhalt zeigen, nicht ein generisches Symbol dafür, also echtes Produkt oder echte Situation statt Weltkugel Symbol für „global". Lichtstimmung muss zur Markenatmosphäre passen, warme oder kühle Farbtemperatur konsistent zur Palette, natürliches Licht wie Fensterlicht, goldene Stunde oder diffuser Schatten wirkt glaubwürdiger als hartes Studioblitzlicht. Farbharmonie: Bildfarben gegen die Markenpalette prüfen, nach Stimmungsbegriffen suchen wie „warm minimal" oder „cool muted tones" statt nach generischen Keywords. Bildausschnitt so wählen, dass er zum Layout passt, etwa Negativraum für Text vorsehen, ohne wichtige Bildelemente zu beschneiden. Authentizität: unperfekte, beiläufige Momente statt gestellter Pose bevorzugen, sichtbare Unregelmäßigkeit und echte Umgebung statt steriles Studio.

**Verbotsliste typischer Klischees.** Händeschütteln im Anzug als Symbol für Deal oder Vertrauen. Aufgeräumter Schreibtisch mit unberührtem Notizbuch, Stift und Kaffeetasse mit perfekter Latte Art. Weltkugel mit leuchtenden Verbindungspunkten für „global" oder „Netzwerk". Kundenservice Person mit übertriebenem Lächeln vor leerem Monitor. Diverse Teamrunde, die gemeinsam auf ein Chart zeigt. Jubel Pose der Belegschaft im Kreis. Diese Bilder wirken technisch korrekt, aber emotional entkoppelt, weil Ausdruck und Umgebung zu perfekt inszeniert sind.

**Lizenz und Attributionsprüfung im Bauprozess.** Vor Verwendung Lizenztyp (CC0, CC BY, Editorial only, Standard oder Extended Lizenz) je Bild dokumentieren, nicht nachträglich rekonstruieren. Attribution im Format „Photo by [Name] on [Plattform], licensed under [Lizenz]" in einer Projekt Attributionsdatei mitführen (etwa CREDITS.md neben den Assets), nicht nur im UI. Lizenzdaten zusammen mit der Bilddatei ablegen, etwa als Sidecar JSON oder in IPTC Metadaten, damit sie bei Wiederverwendung nicht verloren gehen. Vor Veröffentlichung eine Checkliste abarbeiten: Quelle autorisiert, Lizenztyp erfasst, Attributionspflicht erfüllt falls nötig, Verwendungszweck redaktionell oder kommerziell mit Lizenzbedingung abgeglichen.

## Quellenübersicht (Auswahl)

UI: https://motion-primitives.com/, https://github.com/ibelick/motion-primitives, https://www.cult-ui.com/, https://github.com/nolly-studio/cult-ui, https://reactbits.dev/, https://github.com/DavidHDev/react-bits, https://tailark.com/, https://github.com/tailark/blocks, https://animata.design/, https://uiverse.io/, https://skiper-ui.com/

Bilder: https://unsplash.com/license, https://unsplash.com/api-terms, https://help.unsplash.com/en/articles/2511315-guideline-attribution, https://unsplash.com/plus/license, https://www.pexels.com/license/, https://www.pexels.com/api/documentation/, https://help.pexels.com/hc/en-us/articles/27292485713945-AI-and-ML-FAQ, https://pixabay.com/service/license-summary/, https://pixabay.com/service/about/api/

Video: https://coverr.co/license, https://coverr.co/terms, https://mixkit.co/free-stock-video/, https://mixkit.co/llm-info/, https://photutorial.com/videvo-net-review/

KI Bild: https://www.eesel.ai/blog/leonardo-ai-pricing, https://fluxnote.io/guides/leonardo-ai-pricing-guide-2026, https://pxlpeak.com/blog/ai-tools/midjourney-pricing-plans, https://www.aimagicx.com/blog/midjourney-vs-flux-vs-ideogram-image-comparison-2026, https://www.layer3labs.io/comparisons/flux-alternatives, https://lumenci.com/blogs/ai-art-intellectual-property-challenges/, https://www.lovart.ai/blog/ai-art-copyright-2026

Icons: https://lucide.dev/license, https://lucide.dev/packages, https://github.com/lucide-icons/lucide, https://www.infoq.com/news/2026/06/lucide-v1-icons/, https://www.moonb.io/blog/icon-libraries, https://github.com/tabler/tabler-icons, https://tabler.io/icons/packages, https://github.com/tailwindlabs/heroicons

Schriften: https://www.fontshare.com/licenses/itf-ffl, https://velvetyne.fr/about/faq/, https://open-foundry.com/about, https://diversekit.com/blog/26-best-free-fonts-for-ui-web-design-in-2026, https://madegooddesigns.com/best-new-google-fonts-2026/

Auswahlverfahren: https://www.dreamstime.com/blog/how-do-i-avoid-overused-cliche-stock-photos-my-marketing-76636, https://www.format.com/magazine/resources/photography/authentic-stock-photos-creatives, https://hautestock.co/how-to-choose-the-right-images-for-your-website/, https://picdefense.io/blog/ultimate-stock-image-license-verification-guide/, https://webcopyrightchecker.com/blog/image-attribution-requirements-guide
