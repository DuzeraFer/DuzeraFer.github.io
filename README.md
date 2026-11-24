# eduardofernandes.dev — portfolio

Personal portfolio of Eduardo Fernandes — Technical Artist / 3D Artist.

Static site: `index.html`, one case-study page, plus `assets/`. No build step.

Dark, single-theme layout: hero, a filterable work grid, about, contact. All of the
home page — colours, banner, texts, categories, projects, experience, links — lives in
`data.js` (`window.SITE`) and is rendered client-side. Every text field holds `en` and
`pt`; the case-study page reads only the colours from there and keeps its own copy.

## Editing the site

Open `editor.html` through the local server, press **Connect folder** and pick this
folder: Save then writes `data.js` straight to disk and dropping an image on a picture
field copies it into `assets/work/`. Needs Chrome or Edge for the folder access —
anywhere else, edit and use **Download data.js** to replace the file by hand.
Changes are live once `data.js` is committed and pushed.

**Preview** opens the site beside the form and it repaints as you type — no reload. Turn
on **Click to edit** and clicking anything in that preview jumps straight to its fields.
Ctrl+Z / Ctrl+Shift+Z undo and redo; cards, categories, roles and pills reorder by
dragging their header. A project with a picture gets a **Framing** box — drag the image
to move it, wheel or the slider to zoom. It writes `fit: {x, y, z}` on the card (pan as a
percentage of the card, then a scale) and leaves the key out when the framing is default.

`snake-vs-human-skills.html` shows 13 abilities at three upgrade tiers each — 39 square
loops in `assets/skills/`, one `.mp4` and one `.webp` poster per clip. Clips play only
while on screen (IntersectionObserver) and carry no audio. They are re-encoded from the
2160×2160 source recordings:

```
ffmpeg -i IN.mp4 -an -vf "scale=540:540:flags=lanczos,fps=30" \
  -c:v libx264 -preset fast -crf 30 -pix_fmt yuv420p -movflags +faststart OUT.mp4
```

Design source: `REDESIGN.md` (spec) and the Paper file *Portfolio — Redesign*.

Live at https://eduardofernandes3d.github.io

## Local preview

```
python -m http.server 8765
```

Site: http://localhost:8765/ · editor: http://localhost:8765/editor.html

