#!/usr/bin/env bash
# Renders the resume HTML to ATS-readable PDFs and verifies the text extracts.
set -uo pipefail

CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
HERE="$(cd "$(dirname "$0")" && pwd)"
WIN="C:/Users/Duzera/Desktop/Du/Projetos Claude/Portfolio/resume"
URL="file:///C:/Users/Duzera/Desktop/Du/Projetos%20Claude/Portfolio/resume"
MAX_PAGES=2

mkdir -p "$HERE/out"

render() {
  "$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --user-data-dir="C:/Users/Duzera/AppData/Local/Temp/claude-chrome-pdf" \
    --virtual-time-budget=4000 \
    --print-to-pdf="$WIN/out/$2" "$URL/$1?v=$(date +%s)" 2>&1 |
    grep -E "bytes written|ERROR:comp"
}

render resume-en.html Eduardo-Fernandes-Resume.pdf
render resume-pt.html Eduardo-Fernandes-Curriculo.pdf

EN="$HERE/out/Eduardo-Fernandes-Resume"
PT="$HERE/out/Eduardo-Fernandes-Curriculo"

fail=0

echo "--- pages / size ---"
for f in "$EN" "$PT"; do
  pdftotext -enc UTF-8 "$f.pdf" "$f.txt"
  # pdftotext writes one form feed per page, including the last one
  pages=$(tr -cd '\014' < "$f.txt" | wc -c)
  printf '%s: %s page(s), %s KB\n' "$(basename "$f.pdf")" "$pages" "$(( $(stat -c%s "$f.pdf") / 1024 ))"
  if [ "$pages" -gt "$MAX_PAGES" ]; then
    echo "  OVER: more than $MAX_PAGES pages"
    fail=1
  fi
done

echo "--- ATS extraction check ---"
check() {
  grep -qF -- "$2" "$1.txt" || { echo "  MISSING in $(basename "$1"): $2"; fail=1; }
}

# Section headings must survive as whole words, or an ATS cannot find the
# sections at all. Tracking above 0.06em is what breaks them.
while IFS= read -r kw; do check "$EN" "$kw"; done <<'EOF'
Technical Artist
Kreativitas Studio
eduardo2002.fernandes@gmail.com
Shader Graph
Snake vs Human
Harvest Loop
Butterfly Catch
Pizza Paws
Yellow Panda
UpLink
Casulo Indie
Green Game Jam
Gizmos Drawer
Simple VAT
Scene Notes
Impostor Baker
ArtToolkit
DuduTween
VFXForge
Marmoset Toolbag
TypeScript
Associate Degree
SUMMARY
EXPERIENCE
UNITY ASSET STORE
OTHER PROJECTS
SKILLS
EDUCATION
LANGUAGES
PLATFORMS
TECHNICAL ART
PROGRAMMING
EOF

while IFS= read -r kw; do check "$PT" "$kw"; done <<'EOF'
Artista Técnico
São Paulo
otimização
Libras em Ação
Butterfly Catch
UpLink
Casulo Indie
Green Game Jam
Simple VAT
ArtToolkit
DuduTween
VFXForge
submódulos Git
Marmoset Toolbag
Tecnólogo
Português
RESUMO
EXPERIÊNCIA
UNITY ASSET STORE
OUTROS PROJETOS
HABILIDADES
FORMAÇÃO
IDIOMAS
PLATAFORMAS
PROGRAMAÇÃO
EOF

if [ "$fail" = 0 ]; then
  echo "OK: every keyword extracts cleanly, accents intact"
else
  echo "FAILED"
  exit 1
fi
