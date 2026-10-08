#!/usr/bin/env bash
# Stuendlicher Lauf: sync.sh, bei Aenderungen committen und pushen.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
./sync.sh >/dev/null
git add -A
if git diff --cached --quiet; then exit 0; fi
git commit -q -m "Abgleich $(date +%F)"
git push github-kreis-skills:Moritz314/kreis-skills.git main
