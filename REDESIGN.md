# Portfolio redesign — design document

Target reader: a recruiter or art lead who gives the page **30 seconds** before deciding
to keep scrolling or close the tab.

Direction: **follow the references.** Near-black page, one saturated accent, tag chips,
micro-label above every large heading, a sticky project rail. Light stays as a toggle.

The design is drawn out at full scale in [`design/paper.html`](design/paper.html) — open it in a
browser to read it as a page rather than as a spec.

---

## 1. What each reference contributes

| Reference | Taken | Left behind |
|---|---|---|
| **sheehanahmed.com** | The whole project-block grammar: sticky left "jump to a project" rail, client label → title with accent bar → one line → meta row → media. Red accent on near-black. You land *inside* the work. | Cramped sidebar type; no identity above the fold at all. |
| **maciejsojka.dev** | Ruthless edit — **5 projects on the entire page**. Hero is a *moving* render. Tag chips per project. Section rhythm: micro-label, then huge heading, then one paragraph. | The purple gradient wash behind Work history. |
| **franciscomurias.github.io** | Pill filter tabs over one grid. Letter-spaced wordmark. Video hero. | Thumbnail-grid-only; titles lost over busy images. |
| **cosmos.so board** | Typographic discipline: huge tight display type, micro-label bylines, label-and-paragraph specimen rows, images bleeding off the edge. | Its bone/off-white palette — inverted to dark here. |
| **Pinterest board** | One-sheet density: intro → what I do → tools → sections, no page-hopping. | Illustrated/playful styling — wrong register for tech art. |

**Shared DNA of the three dev sites**, which this design adopts wholesale:

- near-black page, one saturated accent, hairline rules
- every section: small uppercase label, then a large heading, then a single paragraph
- tech delivered as **chips**, not prose
- `View project →` as the only secondary link style
- experience as a compressed timeline, skills as grouped chips, contact as a closing block

---

## 2. Diagnosis of the current site

The typography is already good. The *information architecture* is what costs you the recruiter.

1. **Three scrolls before a real project.** A full viewport of slogan, then a stat row, then a
   "Browse by discipline" index, then a 29-card wall — the first case study is screen four.
   Sheehan puts project #1 above the fold. That one decision is most of the recruiter win.
2. **Two navigations.** The sticky nav and the "Browse by discipline" block say the same four
   things. One is dead weight.
3. **The 29-card index is a wall, not an entry point.** Equal-weight cards means nothing is
   selected, so the recruiter has to do the editing you should have done. Maciej shows five.
4. **Nothing moves.** You write shaders and VFX. The page proves that in prose and stills. The
   single strongest asset a technical artist has — footage — is buried. All three references
   lead with motion.
5. **Tech is buried in sentences.** The references all surface stack as chips you can scan in
   one pass.

---

## 3. New structure — 6 blocks instead of 9

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ■ sticky masthead · 56px                                                 │
│   EDUARDO FERNANDES                      Work  Experience  About  Contact │
│   Technical Artist                       EN|PT  ☼|☾  [ RÉSUMÉ ↓ ]        │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1 · HERO — identity over a moving render           ~78vh                │
│  ┌──────────────────────────────────────────────────────────────────┐    │
│  │  [ reel plays full-bleed behind, dimmed 55% ]                     │    │
│  │                                                                   │    │
│  │  SHADERS · TOOLS · GAME-READY ART                                 │    │
│  │                                                                   │    │
│  │  Eduardo "Duzera" Fernandes                                       │    │
│  │  Technical Artist                                                 │    │
│  │  Shaders, tools and art that holds up on a cheap Android.          │    │
│  │                                                                   │    │
│  │  [ SEE THE WORK ]   Résumé (PDF) →                                │    │
│  │                                                                   │    │
│  │  ── 2 ON POKI ──── 11M+ PLAYERS ──── 35k+ VOTES ──── ~200% FPS ── │    │
│  └──────────────────────────────────────────────────────────────────┘    │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│  2 · SELECTED WORK — 6 projects, one per screen                          │
│  ┌───────────────┬──────────────────────────────────────────────────┐    │
│  │ SELECTED WORK │  LIVE ON POKI · KREATIVITAS × CLAP CLAP           │    │
│  │   (sticky)    │                                                  │    │
│  │               │  ▌ Snake vs Human                                │    │
│  │ ▌Snake vs     │                                                  │    │
│  │  Human        │  An arcade shooter against ever-bigger serpents.  │    │
│  │               │                                                  │    │
│  │  Harvest Loop │  (Unity)(URP)(HLSL)(C#)(VFX)(Environment art)     │    │
│  │               │  ──────────────────────────────────────────────  │    │
│  │  URP Renderer │  ROLE      Environment · Props · VFX · UI · Skins │    │
│  │  Features     │  SHIPPED   10M+ players · 4.5★ / 31,502 votes     │    │
│  │               │  SINCE     The first prototype                    │    │
│  │  ~200% FPS    │  ──────────────────────────────────────────────  │    │
│  │  on Android   │                                                  │    │
│  │               │  ┌────────────────────────────────────────────┐  │    │
│  │  ArtToolkit   │  │  large media — bleeds to the right edge     │  │    │
│  │               │  └────────────────────────────────────────────┘  │    │
│  │  Gizmos       │  ┌────────┐┌────────┐┌────────┐                  │    │
│  │  Drawer       │  │ still  ││ still  ││ still  │                  │    │
│  │               │  └────────┘└────────┘└────────┘                  │    │
│  │               │                                                  │    │
│  │               │  Play on Poki →   Google Play →   App Store →    │    │
│  └───────────────┴──────────────────────────────────────────────────┘    │
│                        ... identical block, ×6                           │
│                                                                          │
│   ALSO SHIPPED — Pop&Play · Libras em Ação · hyper-casual titles ·        │
│                  Hired 2 Die: Moonlight Motel                            │
├──────────────────────────────────────────────────────────────────────────┤
│  3 · ARCHIVE — the other 23, as a dense list                             │
│      ( All )( Games )( Shaders )( Tools )( 3D )                          │
│      ▭ 2025  3D       Cyberpunk Creature    (ZBrush)(Maya)(Marmoset)  →  │
│      ▭ 2025  SHADER   Brazilian Sidewalks   (Substance Designer)      →  │
│      ▭ 2024  3D       Ink Protector         (Arnold)(NPR)             →  │
│      ... 48px thumbnail per row, accent bar slides in on hover           │
│      All 29 projects on ArtStation →                                     │
├──────────────────────────────────────────────────────────────────────────┤
│  4 · EXPERIENCE + ABOUT — one spread                                     │
│  ┌──────────────────────────┬───────────────────────────────────────┐    │
│  │ 2023 — now               │  ABOUT                                 │    │
│  │ KREATIVITAS STUDIO       │  Four years shipping art that runs.    │    │
│  │ Technical Artist         │                                        │    │
│  │ · every shader, documented│ 3 sentences. No more.                 │    │
│  │ · ~200% FPS on Android   │                                        │    │
│  │ (HLSL)(C#)(URP)(Maya)    │  ENGINES   (Unity URP)(Unreal)         │    │
│  │                          │  CODE      (HLSL)(C#)(Python/MEL)(JS)  │    │
│  │ 2025 — now  YELLOW PANDA │  3D        (Maya)(ZBrush)(Blender)     │    │
│  │ 2024 — now  UPLINK mentor│            (Substance)(Marmoset)       │    │
│  │ 2022 — now  FREELANCE    │  LANGUAGES (PT native)(EN pro)         │    │
│  │ 2023        ELECTRIC MONK│                                        │    │
│  │ 2023        UNISO        │  [ Résumé (PDF) ↓ ]                    │    │
│  └──────────────────────────┴───────────────────────────────────────┘    │
├──────────────────────────────────────────────────────────────────────────┤
│  5 · CONTACT — one line, enormous                                        │
│      eduardo2002.fernandes@gmail.com                                     │
│      Résumé ↓   ArtStation ↗   LinkedIn ↗   GitHub ↗                     │
└──────────────────────────────────────────────────────────────────────────┘
```

### Section intent

**1 · Hero.** Francisco's and Maciej's hero, not yours: the reel plays full-bleed *behind* the
type, dimmed, so the first thing on screen is work in motion with your name on top of it. Capped
at ~78vh so the first project peeks above the fold. The stat strip sits on the bottom rule as a
single line, not a four-card grid.

**2 · Selected work.** Six projects, not twenty-nine. The sticky rail is the single most
recruiter-friendly element in all five references — a table of contents that never leaves, so
someone hiring for shaders jumps to shaders in one click. Every block repeats the same grammar in
the same order: label → title → sentence → **chips** → meta rows → media → links. After the first
project the recruiter knows exactly where to look.

The six: **Snake vs Human**, **Harvest Loop**, **URP Renderer Features**, **~200% FPS mobile
pass**, **ArtToolkit (Colors + Particles)**, **Gizmos Drawer**. Two shipped games, two pieces of
rendering work, two pieces of tooling — one of them public on the Asset Store.

**3 · Archive.** The 29-card grid becomes rows. A recruiter reads text faster than images, and
ArtStation already does the gallery job. 48px thumbnail per row so it still looks like an artist
made it. Filter chips from Francisco.

**4 · Experience + About.** Current About, Experience, Mentorship and Skills are four blocks
saying one thing. Merged into one spread, Maciej's layout: timeline left, bio and skill chips
right. Mentorship demotes to a timeline row.

**5 · Contact.** The email at display size. Nothing else to decide.

---

## 4. Visual system

Near-black, one accent, flat, hairlines. Inverts cleanly to the existing light theme.

### Palette

| Token | Dark (default) | Light (toggle) | Use |
|---|---|---|---|
| `--bg` | `#0c0c0d` | `#f4f2ee` | page |
| `--surface` | `#141416` | `#ffffff` | media mats, archive rows, cards |
| `--surface-2` | `#1b1b1e` | `#f9f8f6` | row hover, chip fill |
| `--ink` | `#f2f0ed` | `#0d0d0c` | display + body |
| `--ink-60` | `#8f8c88` | `#5c5a56` | micro-labels, meta keys |
| `--rule` | `#26262a` | `#ddd9d2` | every hairline |
| `--accent` | `#e8452a` | `#c0351c` | title bar, active rail item, live dot, active chip |

Vermilion is Sheehan's red, pulled back a touch so it reads confident rather than alarming. It
appears on the page maybe six times. **No second colour, no gradient** — that is the one thing
Maciej's site does that this design does not copy.

### Type

| Role | Font | Size | Tracking |
|---|---|---|---|
| Wordmark | Inter Tight 700 | 15px uppercase | `0.18em` |
| Display (hero name) | Inter Tight 800 | `clamp(2.75rem, 6.5vw, 5.5rem)` / lh `0.95` | `-0.04em` |
| Project title | Inter Tight 800 | `clamp(1.9rem, 3.4vw, 3rem)` | `-0.035em` |
| Section heading | Inter Tight 700 | `clamp(1.8rem, 3vw, 2.5rem)` | `-0.03em` |
| Body | Inter 400 | 17px / lh 1.6, max **62ch** | `0` |
| Micro-label | Inter 600 | 11px uppercase | `0.14em` |
| Chip | JetBrains Mono 400 | 11px | `0.04em` |
| Meta / data | JetBrains Mono 400 | 13px | `0.02em` |

Mono on every number, chip and meta row — it is what makes the page read as technical without a
single neon pixel.

### Grid & chrome

- 12 columns, 1360px max, 80px gutters desktop / 24px mobile.
- Selected-work split: 200px sticky rail + content. Text never wider than 7 columns; media bleeds
  to the right edge.
- Hairline 1px `--rule`. Radius `0`; `2px` on buttons; chips are `2px` rectangles, **not** pills —
  the one place this design overrules the references, because pills plus mono reads like a dashboard.
- No shadows, no gradients, no glass, no glow.
- Primary action = solid `--accent` rectangle, `--bg` text, uppercase, `0.1em`. Secondary =
  underlined text link with `→`.

### Motion — exactly three

1. The hero reel, autoplay muted loop.
2. Media fades in on scroll, 240ms, once.
3. The rail's current project takes the accent bar; archive rows slide an accent bar in on hover.

No parallax, no text reveals, no scroll-jacking.

---

## 5. Recruiter speed budget

| Time | What they have |
|---|---|
| 0–8s | Name, role, one sentence, work moving behind it, four shipped numbers, résumé one click away |
| 8–30s | Snake vs Human in full — chips, role, players, rating, media |
| 30–90s | Rail-jump to whichever discipline they are hiring for |
| any time | Résumé button never leaves the sticky bar |

---

## 6. What gets deleted

- The "Summary / Browse by discipline" block — duplicate navigation.
- The 29-card image grid → dense archive list.
- The standalone Mentorship section → one timeline row.
- The 3D-work category counters → archive filter chips.
- The four-card stat grid → one stat strip on the hero's bottom rule.
- Full-viewport slogan hero → identity over a moving reel.

Nine sections become six. Roughly 1,425 lines of HTML should land near 900.

---

## 7. Open items

1. **The reel does not exist yet.** There are two gameplay captures
   (`harvestloop-gameplay.mp4`, `libras-game.mp4`), but the hero needs a 20s cut of shaders, VFX
   and gameplay. The design sheet stands in with the Harvest Loop capture. This is the one piece
   of new production the redesign asks for, and on a dark hero it matters more than it did on a
   light one — without it the hero is just type on black.
2. **No portrait in `assets/`.** Section 4 reads fine without one, so this is optional.
3. **Light theme.** Kept as a toggle, same structure, tokens flip per the table above.
4. **The rail needs scroll-spy on build.** The design sheet marks the active item statically;
   the real page needs an IntersectionObserver to move the accent bar as you scroll.
5. **The hero carries one gradient** — a dark scrim over the video so the type stays legible.
   It is functional contrast, not decoration, and it is the only gradient on the page.
6. **Mobile is specified but not phone-verified.** The breakpoint reflows at 900px and nothing
   overflows down to 734px, which is as narrow as the preview pane renders. Check it on a real
   phone before shipping — a recruiter opening the link from LinkedIn is on one.
