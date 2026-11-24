# Portfolio additions — GitHub + Asset Store audit

Audit run 2026-11-23. Sources: 973 commits authored by `eduardo-fernandes-3d` across 29 repos in
`kreativitas-studio`, 175 in your own repos, the `eduardo-fernandes-3d/AssetStore` repo (all nine
`asset/*` branches), and the live Unity Publisher Portal.

---

## Applied to the site

- **New `Asset Store` filter** with **18 cards** — every package on the publisher portal
  except Time Tracker Lite (it is the free cut-down of Time Tracker, so it would read as a
  duplicate). Hero images are the real store renders, pulled from the `asset/*` branches and
  from `main`, scaled to 960×540 and saved as `assets/work/store-*.jpg`.
- **Butterfly Catch restored.** The card existed in `index.html` before the `data.js`
  refactor and was dropped by it. `work.p` went back to "Three games on Poki".
- **ArtToolkit and VFXForge descriptions rewritten** — both badly undersold what the repos
  actually contain.
- **Bug fix in `index.html`:** `.card{display:flex}` overrode the `hidden` attribute, so the
  category filters set `aria-pressed` and nothing else — clicking a filter never hid a card.
  Added `.card[hidden]{display:none}`. This predates the `data.js` refactor; it has been
  broken since `ca73c0f`.

Verified at 1280×900: 27 cards total, the Asset Store filter shows exactly 18, no broken
images, no console errors, and the PT translations render on every new card.

---

## The Asset Store ledger (live, read from the portal)

19 packages. Publisher 142088, "Eduardo Fernandes" / Duzera Tools.

| Package | Price | Status |
|---|---|---|
| Gizmos Drawer | Free | Published Jun 11 2026 |
| Time Tracker - Work Diary | $15.00 | Published Oct 23 2026 |
| Time Tracker Lite - Work Diary | Free | Published Oct 23 2026 |
| Scene Notes - Sticky Notes | $7.99 | Published Oct 23 2026 |
| Gradient Atlas | Free | Published Nov 06 2026 |
| Simple VAT | $19.99 | Published Nov 16 2026 (v2.0.0) |
| Reference Hunter | $9.99 | **Pending** — #533 in queue |
| SDF Baker | $7.99 | **Pending** — #1071 in queue |
| Curve Texture | $4.99 | **Pending** — #1088 in queue |
| Sub Graph Library | $24.99 | **Pending** |
| Texture Workbench | $9.99 | **Pending** |
| Cable Draper | $24.99 | **Rejected** — submission limit reached |
| Floating Numbers | $24.99 | **Rejected** — submission limit reached |
| Impostor Baker | $29.99 | **Rejected** — submission limit reached |
| Room Maps | $24.99 | **Rejected** — submission limit reached |
| SimpleVAT Crowd | $34.99 | **Rejected** — submission limit reached |
| Sky Cycle | $29.99 | **Rejected** — submission limit reached |
| Surface Trails | $24.99 | **Rejected** — submission limit reached |
| Wind Field | $24.99 | **Rejected** — submission limit reached |

**All eight rejections carry the same reason: "Submission limit reached."** Not one is a
quality rejection. 5 pending + 8 bounced is consistent with Unity capping concurrent
submissions at 5 — the eight went in over the cap and were returned unreviewed. They are
finished packages with uploaded builds, filled listings and store media, and they should go
back in the queue as the pending five clear.

Because of that, the site labels them **Unreleased**, never "rejected" and never anything
implying they are on sale. "In review" is used for the five pending. That wording is
accurate whatever Unity decides later.

Also note, against the repo's own `IDEAS.md` (which is 17 days stale): **Gradient Atlas
shipped free, not $4.99**, **Scene Notes is $7.99, not $9.99**, and **Simple VAT is now
$19.99 at v2.0.0, not $15**. The site uses the live numbers.

---

## From GitHub — still not on the site

Ranked. None of these is applied; they need either an asset or a decision from you.

### 1. Snake vs Human — the Nov–Dec 2025 engineering pass
The strongest story in your whole commit history, and the site only shows the art side of
this game. In order, your commits:
- `WIP: VFX System to Particles System` → `Finishe Moving VFX System to Particles System`
- `Particles changed to ID instead of SO Reference`, `Changed VFX Pool Sizes`
- `Sprites to billboard` + `Text billboard shader / Remove look at camera`
- `Simplified snake shader` → `Change snake shader to HLSL`, after
  `Optimized uv calculation snake shader`
- `Texture Compression Fixes`, `Texture and Models Compression`
- `Environment more modular, effect for objects disappear on substage transition`
- `Removed old UI Particle System`, `Removed unused shaders`, `URP Quality Update`

Needs a before/after capture or a number to anchor it. Ask me and I'll draft the card.

### 2. DuduTween
`Kreativitas.Core`, Jan 2026: `WIP: DuduTween` (26 Jan) → `Dudu Tween now support async` →
`Dudu Tween Sequence` → `Removed DoTween and Toggle IDudu to Dudu` (30 Jan). Then its own
package: `Prime Tween Settings`, `MovePath and Settings`, `Image Alpha Tween`,
`Added Canvas Group Support`, `Self Initialize`. You replaced a third-party dependency
studio-wide with your own library. No image exists, so it would be a `noshot` tile.

### 3. Editor toolbox — Kreativitas.Core
Advanced Renamer (a window; assets, animations and sprites) · Skinned Mesh Changer ·
Custom Toolbar editor · Curve Preview Drawer · Material Instance Helper · object pool.

### 4. Environment Creator — Personal repo, Mar–Apr 2025
`WIP: Mask painting inside editor` · `WIP: Chunk based environment` / `Started Chunk
generator` · `WIP: Grass Instancer` + `Grass shader` · `Gradient Mapping fog` ·
`Clouds Additive / LUT` · `Shader now compatible with SRP Batcher` · `Shader Profiling tool
WIP`. Same repo as the URP Renderer Features card already on the site.

### 5. URP baseline across the studio
`URP Quality Settings and Scene Update` and `Fix MSAA in Renderer`, landed by you in
`UnityTemplate`, `Kreativitas.Meta`, `PaperGo` and `HorseRide` — you own the render settings
every new studio project starts from. Better as a line in About than a card.

### 6. Lower priority
- **ICleaner** — toon shader with configurable cel steps and multipass outlines
- **FrameDuels** — two-phone party game; Node server with rooms, teams, timers, a live big
  screen and 6 modes; every screen animated. Private repo, web not Unity.
- **Fx** — `Add ClaudeVFX library and Paper texture generation workflow` (16 Nov 2026)

---

## The six mobile games — resolved, and on the site

They are not unannounced. All six are **live on Google Play** under "Kreativitas Studio
Ltda", and each now has a card under the Games filter with its real store screenshot:

| Game | Package | Your commits |
|---|---|---|
| Pencil Pack | `com.kreativitasstudio.pencilpack` | 144 |
| Stack Away | `com.kreativitasstudio.stackaway` | 100 |
| Sort My Coins | `com.kreativitasstudio.sortmycoins` | 99 |
| Level Up Rings | `com.kreativitasstudio.leveluprings` | 72 |
| Layer Colors | `com.kreativitasstudio.layercolors` | 59 |
| Emoji Sort | `com.kreativitassstudio.emojisort` (note the triple `s`) | 59 |

They are mobile, not Poki — Pencil Pack carries a Lion Studios / AppLovin MAX / Adjust /
Facebook SDK stack, so the line is hypercasual publishing rather than web. `work.p` now
reads "Three games on Poki, six on Google Play".

### Four more on that developer page you also worked on
Not added — your commit counts are lower and I did not want to pad the grid, but they are
there if you want them: **Jam Drive Thru** (71 commits, a game jam build),
**Face Away** (10), **Cat Squad** (12, as `com.DefaultCompany.Cat_Squad`) and
**Pizza Paws** (1). The page also lists Mahjong Monster Arena, Snake Ball Bounce and
Snake Assault, which have no commits from you.
