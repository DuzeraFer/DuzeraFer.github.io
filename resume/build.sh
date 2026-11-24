#!/usr/bin/env bash
# Renders the resume HTML to ATS-readable PDFs and verifies the text extracts.
set -uo pipefail

CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
HERE="$(cd "$(dirname "$0")" && pwd)"
WIN="C:/Users/Duzera/Desktop/Du/Projetos Claude/Portfolio/resume"
URL="file:///C:/Users/Duzera/Desktop/Du/Projetos%20Claude/Portfolio/resume"

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

echo "--- pages / size ---"
for f in "$EN" "$PT"; do
  pdftotext -enc UTF-8 "$f.pdf" "$f.txt"
  # pdftotext writes one form feed per page, including the last one
  pages=$(tr -cd '\014' < "$f.txt" | wc -c)
  printf '%s: %s page(s), %s KB\n' "$(basename "$f.pdf")" "$pages" "$(( $(stat -c%s "$f.pdf") / 1024 ))"
  [ "$pages" -eq 1 ] || echo "  WARN: expected a single page"
done

echo "--- ATS extraction check ---"
fail=0
check() {
  grep -qF -- "$2" "$1.txt" || { echo "  MISSING in $(basename "$1"): $2"; fail=1; }
}

# Section headings must survive as whole words, or an ATS cannot find the
# sections at all. Tracking above 0.06em is what breaks them.
while IFS= read -r kw; do check "$EN" "$kw"; done <<'EOF'
Technical Artist
Technical Artist / 3D Artist
Kreativitas Studio
eduardo2002.fernandes@gmail.com
Shader Graph
Snake vs Human
Harvest Loop
Butterfly Catch
Yellow Panda
Gizmos Drawer
UpLink
Casulo Indie
Green Game Jam
Associate Degree
SUMMARY
EXPERIENCE
PROJECTS
SKILLS
EDUCATION
PLATFORMS
TECHNICAL ART
PROGRAMMING
LANGUAGES
EOF

while IFS= read -r kw; do check "$PT" "$kw"; done <<'EOF'
Artista Técnico
Artista Técnico / Artista 3D
São Paulo
otimização
Libras em Ação
Butterfly Catch
UpLink
Green Game Jam
Tecnólogo
Português
RESUMO
EXPERIÊNCIA
PROJETOS
HABILIDADES
FORMAÇÃO
PLATAFORMAS
PROGRAMAÇÃO
IDIOMAS
EOF

if [ "$fail" = 0 ]; then
  echo "OK: every keyword extracts cleanly, accents intact"
else
  echo "FAILED"
  exit 1
fi
