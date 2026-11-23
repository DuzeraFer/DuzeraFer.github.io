# eduardofernandes.dev — portfolio

Personal portfolio of Eduardo Fernandes — Technical Artist / 3D Artist.

Static site: `index.html`, one case-study page, plus `assets/`. No build step.

Dark, single-theme layout: hero, a filterable 9-card work grid, about, contact.
EN/PT copy lives in the `PT` dictionary at the bottom of each page; English is read
from the markup via `data-i18n`.

`snake-vs-human-skills.html` shows 13 abilities at three upgrade tiers each — 39 square
loops in `assets/skills/`, one `.mp4` and one `.webp` poster per clip. Clips play only
while on screen (IntersectionObserver) and carry no audio. They are re-encoded from the
2160×2160 source recordings:

```
ffmpeg -i IN.mp4 -an -vf "scale=540:540:flags=lanczos,fps=30" \
  -c:v libx264 -preset fast -crf 30 -pix_fmt yuv420p -movflags +faststart OUT.mp4
```

Design source: `REDESIGN.md` (spec) and the Paper file *Portfolio — Redesign*.

Live at https://duzerafer.github.io

## Local preview

```
python -m http.server 8765
```
