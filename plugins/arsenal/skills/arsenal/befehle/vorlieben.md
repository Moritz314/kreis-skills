# vorlieben

Pflegt die stehenden Vorlieben: ein Satz je Regel, mit Datum und Herkunft. Jeder Befehl liest sie vor der Arbeit.

**Aufruf:** `vorlieben` (zeigen, Alias `behavior`), `vorlieben neu "<satz>" [projekt]`, `vorlieben aendern <n> "<satz>"`, `vorlieben loeschen <n>`
**Datei:** `behavior.md` im Zustandsordner (Pfade in `SKILL.md`); fehlt sie, legt dieser Befehl sie an.

- Format je Zeile: `- JJJJ-MM-TT [<projekt oder global>] <ein Satz>.` Prosa wird abgelehnt; nach einem knapperen Satz fragen.
- `<n>` ist die Stelle in der Liste oder ein eindeutiges Textstück. Kein Treffer: Liste zeigen, nicht raten.
- Lehnt <dein-name> in `politur` oder `kritik` einen Vorschlag ab oder korrigiert ihn, einmal fragen: „Als Vorliebe speichern?“ Nur nach Ja schreiben, nie zweimal fragen.
- Vorrang: Eine Vorliebe gilt vor Stamm, Modulen und Branche, aber nie vor Pflicht (Vorrang in `SKILL.md`). Eine Ausnahme nur für ein Projekt steht im ARMOURY.
