# eduardofernandes.dev — portfolio

Personal portfolio of Eduardo Fernandes — Technical Artist / 3D Artist.

Static site: `index.html`, two case-study pages, plus `assets/`. No build step.

Dark, single-theme layout: hero, a filterable work grid, about, contact. All of the
home page — colours, banner, texts, categories, projects, experience, links — lives in
`data.js` (`window.SITE`) and is rendered client-side. Every text field holds `en` and
`pt`; the case-study pages read only the colours from there and keep their own copy.

## Editing the site

Run `edit.cmd` (or `python serve.py`). It starts a small local server and opens the
editor: the site fills the window and a panel of fields sits over it. Click anything on
the site to jump to its fields, **Save** writes `data.js` to disk, **Publish** commits and
pushes. No folder picker, no downloads — any browser works.

**Fields** hides and shows the panel. Ctrl+S saves, Ctrl+Z / Ctrl+Shift+Z undo and redo;
cards, categories, roles and pills reorder by dragging their header. Dropping an image on
a picture field copies it into `assets/work/`. A project with a picture gets a **Framing**
box — drag the image to move it, wheel or the slider to zoom. It writes `fit: {x, y, z}` on
the card and leaves the key out when the framing is default. `x` and `y` are a CSS
`object-position` in percent (50/50 is centred, 0–100 walks the banner across whatever the
16:9 card cannot show), `z` is a `scale`. An image that is already 16:9 has nothing to walk
across, so it only responds to zoom.

Opening `editor.html` any other way (file://, plain `http.server`) still renders, but Save
and Publish have nothing to write to.

`snake-vs-human-skills.html` shows 13 abilities at three upgrade tiers each — 39 square
loops in `assets/skills/`, one `.mp4` and one `.webp` poster per clip. Clips play only
while on screen (IntersectionObserver) and carry no audio. They are re-encoded from the
2160×2160 source recordings:

```
ffmpeg -i IN.mp4 -an -vf "scale=540:540:flags=lanczos,fps=30" \
  -c:v libx264 -preset fast -crf 30 -pix_fmt yuv420p -movflags +faststart OUT.mp4
```

`frameduels.html` is a screenshot case study of FrameDuels, the film-guessing party game
(https://frameduels.onrender.com). Shots in `assets/work/frameduels-*.jpg` were captured from
the live game at 1440x900 (desktop) and 375x812 (phone).

Design source: `REDESIGN.md` (spec) and the Paper file *Portfolio — Redesign*.

Live at https://eduardofernandes3d.github.io

## Local preview

```
python serve.py
```

Site: http://localhost:8765/ · editor: http://localhost:8765/editor.html

