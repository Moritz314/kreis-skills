#!/usr/bin/env bash
# kreis-skills sync: copy skills from the private skill tree, sanitize, abort on any leftover, package.
# Idempotent. Output: list of removed/replaced places (file, kind, count) - never the values.
set -euo pipefail
HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SRC=${KREIS_SKILLS_SRC:-$HOME/.claude/skills}
SKILLS=(arsenal impeccable web-design-guidelines)
OWNER_URL="https://github.com/Moritz314/kreis-skills"
STAGE=$(mktemp -d); trap 'rm -rf "$STAGE"' EXIT
mkdir -p "$STAGE/out"

for s in "${SKILLS[@]}"; do
  [ -f "$SRC/$s/SKILL.md" ] || { echo "ABBRUCH: $SRC/$s/SKILL.md fehlt" >&2; exit 2; }
  rsync -a --exclude='.git' --exclude='node_modules' --exclude='*.zip' "$SRC/$s/" "$STAGE/out/$s/"
  [ -d "$HERE/static/$s" ] && cp -a "$HERE/static/$s/." "$STAGE/out/$s/"
done

# ---- sanitize (perl): replacements, line deletions, dropping of planning files that are too internal
cat > "$STAGE/san.pl" <<'PERL'
use strict; use warnings;
my $root = shift;
my @files = map { chomp; $_ } <STDIN>;
# [label, regex, replacement, internal?]  internal? = file in planung/ with such a hit is dropped entirely
my @rep = (
 ['Pfad (Windows-Nutzerordner)', qr{[A-Za-z]:[\\/]+Users[\\/]+Spaek(?:[\\/][^\s`"'\)<>,;]*)?}, '<dein-ordner>', 1],
 ['Pfad (Linux privat)',         qr{/(?:home/moritz|srv/syncthing|root/sync)(?:/[^\s`"'\)<>,;]*)?}, '<dein-ordner>', 1],
 ['Vault-Verweis',               qr{claude-mem}, '<memory-vault>', 1],
 ['Server-IP',                   qr{\b(?:217\.160|87\.106|31\.70|85\.215)\.\d+\.\d+|\b100\.(?:6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.\d+\.\d+}, '<server-ip>', 1],
 ['E-Mail-Adresse',              qr{\b[\w.+-]+@(?:web\.de|gmail\.com|gmx\.[a-z]+|kreis[\w.-]*\.[a-z]+)\b}i, '<email>', 1],
 ['Domain (privat)',             qr{\b(?:[\w-]+\.)?(?:moritzkreis\.de|topcharge\.tech|noctus\.events|kreissystems[\w.]*)\b}i, '<deine-domain>', 1],
 ['Projekt-/Kundenname',         qr{\b(?:TopCharge|Kontor|Stadtreklame|Noctus|Signalbox|SCCS|DRAGui|Schul-Tools)\b}, '<internal-project>', 1],
 ['Infrastruktur-Name',          qr{\b(?:Kraken|Powerhouse|Tailscale|Syncthing|Obsidian|Wachhund)\b}, '<infrastructure>', 1],
 ['Vorname Nutzer (de)',         qr{von Moritz\b}, 'vom Nutzer', 0],
 ['Vorname Nutzer',              qr{\bMoritz(?:\x{2019}s|\'s)?}, 'the user', 0],
 ['Firmenname',                  qr{\bKreis[ -]Systems\b}, '<studio>', 0],
 ['Beispiel-Token (Demo) ersetzt', qr{\bghp_[A-DF-Za-z0-9][A-Za-z0-9]{19,}}, 'ghp_EXAMPLE000000000000000000000000000', 0],
 ['Begriff harness (Testumgebung in impeccable)', qr{harness}i, 'testbed', 0],
);
# line deletions: [label, file regex, line regex]
my @del = (
 ['Abschnitt Kontingent/Wachhund', qr{commands/build\.md$}, qr{^(?:\d+\. \*\*(?:Kontingent check|Wachhund registration)|8\. Deregister the wachhund|- Kontingent insufficient|- \*\*Ein Lauf vom Windows-PC)}i],
 ['Pfadtabelle (Infrastruktur)',   qr{arsenal/SKILL\.md$}, qr{^\| (?:Linux \(Kraken\)|Linux \(other servers\)) \|}],
);
# literal edits: [label, file regex, regex, replacement]
my @edit = (
 ['Pfadtabelle ersetzt', qr{arsenal/SKILL\.md$}, qr{^\| Windows \| .*$}, '| Any | `<dein-ordner>/arsenal/` (a folder of your choice; sync it if several machines share it) |'],
 ['Satz Syncthing',      qr{arsenal/SKILL\.md$}, qr{live in the Syncthing tree so every instance on every server sees the same data}, 'live in a state folder of your choice so every instance sees the same data'],
 ['Nummerierung',        qr{commands/build\.md$}, qr{^9\. Report what}, '8. Report what'],
 ['Abschnittstitel',     qr{commands/build\.md$}, qr{^## Lehren aus dem learn\.-Bau.*$}, '## Lessons from a large build'],
);
my %rows;  # file => label => n
my $dropped = 0;
for my $f (@files) {
  my $rel = $f; $rel =~ s{^\Q$root\E/}{};
  next if $rel =~ m{modern-screenshot\.umd\.js$};
  next unless $rel =~ m{\.(md|js|mjs|html|json|svg|txt|css)$};
  open my $in, '<:raw', $f or die; local $/; my $t = <$in>; close $in;
  my $orig = $t;
  if ($rel =~ m{^arsenal/planung/}) {
    my $internal = 0;
    for my $r (@rep) { next unless $r->[3]; $internal = 1 if $t =~ $r->[1]; }
    if ($internal) { unlink $f or die; $rows{$rel}{'Datei weggelassen (interne Bezuege)'} = 1; $dropped++; next; }
  }
  for my $d (@del) {
    next unless $rel =~ $d->[1];
    my $n = 0; my @l = split /(?<=\n)/, $t;
    @l = grep { if ($_ =~ $d->[2]) { $n++; 0 } else { 1 } } @l;
    $t = join '', @l; $rows{$rel}{$d->[0]} += $n if $n;
  }
  for my $e (@edit) {
    next unless $rel =~ $e->[1];
    my $n = ($t =~ s/$e->[2]/$e->[3]/mg); $rows{$rel}{$e->[0]} += $n if $n;
  }
  for my $r (@rep) {
    my $re = $r->[1]; my $to = $r->[2];
    my $n = ($t =~ s/$re/$to/g); $rows{$rel}{$r->[0]} += $n if $n;
  }
  if ($t ne $orig) { open my $o, '>:raw', $f or die; print $o $t; close $o; }
}
print "BEREINIGUNG (Datei | Art | Anzahl)\n";
for my $f (sort keys %rows) { for my $l (sort keys %{$rows{$f}}) { print "  $f | $l | $rows{$f}{$l}\n"; } }
PERL
find "$STAGE/out" -type f | perl "$STAGE/san.pl" "$STAGE/out" | tee "$STAGE/report.txt"

# ---- final scan: any hit aborts (only file names and kind are printed)
declare -A PAT=(
 [Geheimnis-Muster]='sk_[A-Za-z0-9]{12,}|sk-ant-|ghp_[A-DF-Za-z0-9][A-Za-z0-9]{19,}|github_pat_|xox[bapr]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|eyJ[A-Za-z0-9_-]{20,}\.eyJ|BEGIN [A-Z ]*PRIVATE KEY'
 [Passwortzeile]='(passwor[dt]|passwd|secret|api[_-]?key|token)[A-Za-z_]*["'"'"']?[ ]*[:=][ ]*["'"'"'][A-Za-z0-9!@#$%^&*_.+/-]{12,}["'"'"']'
 [Verbindungs-URL]='[a-z][a-z0-9+.-]*://[^/ "'"'"'@:]+:[^/ "'"'"'@]+@'
 [Server-IP]='(217\.160|87\.106|31\.70|85\.215)\.[0-9]+\.[0-9]+'
 [Tailscale-IP]='100\.(6[4-9]|[7-9][0-9]|1[01][0-9]|12[0-7])\.[0-9]+\.[0-9]+'
 [Privater-Pfad]='/home/moritz|Users.Spaek|/srv/syncthing|/root/sync|claude-mem'
 [E-Mail]='[A-Za-z0-9._+-]+@(web\.de|gmail\.com|gmx\.[a-z]+)'
 [Namen-Intern]='Moritz|Spaek|Kreis[ -]Systems|kreissystems|moritzkreis|topcharge|Kontor|Stadtreklame|Noctus|Signalbox|DRAGui|Kraken|Powerhouse|Tailscale|Syncthing|Obsidian|Wachhund|kontingent'
 [Verbotener-Name-harness]='[Hh][Aa][Rr][Nn][Ee][Ss][Ss]'
)
bad=0
for k in "${!PAT[@]}"; do
  hits=$(grep -rIlE -i --exclude=LICENSE -e "${PAT[$k]}" "$STAGE/out" 2>/dev/null | grep -v 'modern-screenshot.umd.js$' || true)
  [ "$k" = Geheimnis-Muster ] && hits=$(grep -rIlE -e "${PAT[$k]}" "$STAGE/out" 2>/dev/null || true)
  [ "$k" = Passwortzeile ] && hits=$(grep -rIlE -i --exclude=LICENSE -e "${PAT[$k]}" "$STAGE/out" 2>/dev/null || true)
  if [ -n "$hits" ]; then echo "$hits" | sed "s|$STAGE/out/|SENSIBEL [$k] |"; bad=1; fi
done
# vendored minified file: only secret-style patterns
grep -IlE -e "${PAT[Geheimnis-Muster]}" "$STAGE/out/impeccable/scripts/modern-screenshot.umd.js" >/dev/null 2>&1 && { echo "SENSIBEL [Geheimnis-Muster] impeccable/scripts/modern-screenshot.umd.js"; bad=1; }
# file/path names
if find "$STAGE/out" | grep -qiE 'harness|moritz|spaek|kontor'; then echo "SENSIBEL [Dateiname]"; bad=1; fi
[ $bad -eq 0 ] || { echo "ABBRUCH: sensible Reste gefunden, nichts uebernommen." >&2; exit 3; }
echo "Pruefung bestanden: keine sensiblen Reste."

# ---- install into repo
declare -A DESC=(
 [arsenal]="Technical building blocks for ambitious UI: shaders, 3D, scroll choreography, curated free libraries, ready-made animated components, plus plan/build/critics commands."
 [impeccable]="Design skill for frontend interfaces: shape, critique, audit, polish, animate, harden, adapt and more (Apache-2.0, by Paul Bakaus)."
 [web-design-guidelines]="Review UI code against the Web Interface Guidelines (accessibility, UX, best practices). MIT, by Vercel."
)
declare -A LIC=([arsenal]=MIT [impeccable]=Apache-2.0 [web-design-guidelines]=MIT)
declare -A CAT=([arsenal]=design [impeccable]=design [web-design-guidelines]=development)
mkdir -p "$HERE/plugins" "$HERE/dist" "$HERE/.claude-plugin"
for s in "${SKILLS[@]}"; do
  P="$HERE/plugins/$s"; mkdir -p "$P/skills/$s" "$P/.claude-plugin"
  rsync -a --delete "$STAGE/out/$s/" "$P/skills/$s/"
  cat > "$P/.claude-plugin/plugin.json" <<JSON
{
  "name": "$s",
  "description": "${DESC[$s]}",
  "version": "1.0.0",
  "author": { "name": "Kreis Systems", "url": "$OWNER_URL" },
  "homepage": "$OWNER_URL",
  "repository": "$OWNER_URL",
  "license": "${LIC[$s]}",
  "keywords": ["design", "frontend", "ui"]
}
JSON
  # zip for claude.ai: folder with SKILL.md at its root, deterministic
  Z="$STAGE/zip"; rm -rf "$Z"; mkdir -p "$Z"; cp -a "$STAGE/out/$s" "$Z/$s"
  find "$Z" -exec touch -d '2026-01-01 00:00:00' {} +
  rm -f "$HERE/dist/$s.zip"
  python3 -I - "$Z" "$s" "$HERE/dist/$s.zip" <<'PY'
import os, sys, zipfile
z, s, out = sys.argv[1:4]
files = sorted(os.path.join(d, f)[len(z)+1:] for d, _, fs in os.walk(os.path.join(z, s)) for f in fs)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
    for rel in files:
        zi = zipfile.ZipInfo(rel, (2026, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED; zi.external_attr = 0o644 << 16
        zf.writestr(zi, open(os.path.join(z, rel), "rb").read())
PY
done
{
  echo '{'
  echo '  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",'
  echo '  "name": "kreis-skills",'
  echo '  "description": "Design and frontend skills: arsenal, impeccable, web-design-guidelines",'
  echo '  "owner": { "name": "Kreis Systems", "url": "'"$OWNER_URL"'" },'
  echo '  "plugins": ['
  n=${#SKILLS[@]}; i=0
  for s in "${SKILLS[@]}"; do
    i=$((i+1)); sep=,; [ $i -eq $n ] && sep=
    echo '    {'
    echo '      "name": "'"$s"'",'
    echo '      "description": "'"${DESC[$s]}"'",'
    echo '      "source": "./plugins/'"$s"'",'
    echo '      "category": "'"${CAT[$s]}"'",'
    echo '      "homepage": "'"$OWNER_URL"'"'
    echo "    }$sep"
  done
  echo '  ]'
  echo '}'
} > "$HERE/.claude-plugin/marketplace.json"
python3 -c "import json;json.load(open('$HERE/.claude-plugin/marketplace.json'))"
echo "Fertig: plugins/, dist/*.zip, .claude-plugin/marketplace.json"
