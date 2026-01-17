<!--
📍 Location: web/assets/media/screenshots/README.md
🎯 Purpose: Curated screenshot library + naming + provenance rules
-->

# 📸 Screenshots

![asset](https://img.shields.io/badge/asset-screenshots-informational)
![scope](https://img.shields.io/badge/scope-web%20ui%20%26%20docs-blue)
![rule](https://img.shields.io/badge/principle-provenance--first-orange)

Curated screenshots used for **docs**, **UI review**, **release notes**, and **visual QA** across the Kansas Frontier Matrix (KFM) web experience.

📌 **Folder:** `web/assets/media/screenshots/`

---

## 🧭 Quick Links

- ⬆️ Repo root: `../../../../README.md`
- 🌐 Web root: `../../../`
- 🧰 Assets root: `../../`

> [!NOTE]
> If you’re adding a new kind of screenshot (new feature area / workflow), add a subfolder **and** update the tree below so it stays discoverable.

---

## 🧠 What this folder is

This is a **long-lived, organized** library of screenshots that we expect to keep around:
- to explain features to users,
- to show “before vs after” for UI changes,
- to document workflows (especially map + data interactions),
- and to support provenance-first storytelling (where visuals are evidence, not vibes).

---

## ✅ What goes here

- 🖥️ **UI feature screenshots** used in docs / guides / Story Nodes
- 🔁 **Before/After** screenshots for notable UI changes (when we want to keep a permanent record)
- 🧪 **Visual QA baselines** (hand-curated, not auto-generated)
- 🧾 **Release highlight images** (stable + optimized)

---

## 🚫 What does *not* go here

- 🔐 Anything with secrets, tokens, private keys, personal data, or internal-only URLs
- 🧑‍🤝‍🧑 User-generated content that isn’t explicitly approved for inclusion
- 🤖 Bulk automated test artifacts (put those in your test output / CI artifacts)
- 🪨 Raw uncompressed captures (optimize before committing)

> [!IMPORTANT]
> Assume screenshots may be seen by the public and may ship with the web bundle. **Redact first.** Optimize always.

---

## 🗂️ Suggested folder structure

Keep organization by **surface area** (where in the UI) and **workflow** (what the user is doing).

```text
web/
└─ 📁 assets/
   └─ 🎞️ media/
      └─ 📸 screenshots/
         ├─ ✅📄 README.md              # you are here 📌 Screenshot rules (naming, sizes, redaction, reuse)
         │
         ├─ 🧭 ui/                      # UI surfaces (stable screenshots for docs/catalog/marketing)
         │  ├─ 🗺️ map-viewer/           # Main map: layers, legend, timeline, inspector
         │  ├─ 🗂️ data-catalog/         # Dataset browsing: metadata, filters, search, provenance panels
         │  ├─ 📚 story-nodes/          # Narratives: steps, citations/evidence, embedded media
         │  └─ ⚙️ settings/             # Preferences, account/session, accessibility toggles
         │
         ├─ 🔁 workflows/               # End-to-end user journeys (multi-step sequences)
         │  ├─ ➕🧩 add-a-layer/         # Add a layer: choose → preview → enable → verify legend/provenance
         │  ├─ 🕰️↔️ compare-time-ranges/ # Compare time: scrub timeline → swap layers → diff views
         │  └─ 📤🗺️ export-map/         # Export: screenshot/print/share flows + attribution/citations
         │
         ├─ 🗞️ releases/               # Curated “what’s new” visuals per release/month
         │  └─ 📅 2026-01/              # Release screenshots for January 2026
         │
         └─ 🗄️ _archive/               # Older screenshots kept for reference (not referenced by current docs/UI)
```

> [!TIP]
> If you’re unsure: **start in `ui/`**, and only create a new top-level folder if it’s clearly a different purpose.

---

## 🏷️ Naming convention

Use **kebab-case**, include a **date**, and bake in the “what/where/state” so the file makes sense even in isolation.

### Recommended pattern

`YYYY-MM-DD__surface__feature__state__viewport__theme.ext`

- `surface` → `map-viewer`, `data-catalog`, `story-nodes`, etc.
- `feature` → `layer-list`, `timeline`, `search`, `filters`, `details-panel`
- `state` → `before`, `after`, `open`, `closed`, `error`, `empty`, `populated`
- `viewport` → `desktop-1440w`, `tablet-1024w`, `mobile-390w`
- `theme` → `light`, `dark`
- `ext` → prefer `webp`, use `png` if necessary (see performance section)

### Examples ✅

- `2026-01-15__map-viewer__layer-list__open__desktop-1440w__light.webp`
- `2026-01-15__data-catalog__filters__populated__desktop-1440w__dark.webp`
- `2026-01-15__story-nodes__citation-panel__open__mobile-390w__light.png`

---

## 🧾 Metadata sidecar (recommended)

For anything used in documentation, release notes, or “evidence screenshots”, add a sidecar metadata file:

`<same-name>.meta.json`

Example:

```json
{
  "title": "Layer list open on the Map Viewer",
  "captured_at": "2026-01-15",
  "captured_by": "your-handle",
  "purpose": "docs",
  "app": {
    "route": "/map",
    "commit": "abc1234",
    "version": "dev"
  },
  "viewport": {
    "width": 1440,
    "height": 900,
    "device": "desktop"
  },
  "state": {
    "theme": "light",
    "layers_enabled": ["county-boundaries", "historic-railroads"],
    "timeline": "1910-01-01 → 1920-12-31",
    "center": { "lat": 38.5, "lng": -98.0 },
    "zoom": 6
  },
  "notes": "Captured with sample dataset + redacted user info."
}
```

> [!TIP]
> Sidecar metadata makes screenshots **auditable and reproducible** (and helps future you understand what you were looking at 😄).

---

## 🎛️ Capture standards

Keep screenshots consistent so comparisons stay meaningful.

- 🧭 **Prefer stable UI states** (no loading spinners, no hover tooltips, no flashing cursors)
- 🧱 **Use standard viewports**
  - Desktop: `1440×900`
  - Mobile: `390×844` (or your agreed baseline)
- 🌗 **Theme:** capture in the theme that best matches the docs/release context (`light` by default)
- 🧼 **Clean data:** use sample/demo datasets unless you have explicit approval
- 🕵️ **Redact:** blur or remove identifiers (emails, tokens, internal endpoints)

---

## ⚡ Performance & file formats

Screenshots are assets. Assets affect:
- repo weight 📦
- download size 📉
- page performance ⚡

### Preferred formats
- ✅ **WebP** for most screenshots (small + good quality)
- ✅ **PNG** when text/UI becomes blurry in WebP, or when transparency is needed

### Size budget (guideline)
- 🎯 Aim for **≤ 500KB** per screenshot (smaller if it’s going to be used frequently)

### Optional optimization commands

```bash
# If you have ImageMagick installed:
magick input.png -strip -quality 85 output.webp

# If you want PNG lossless optimization:
# (tool availability varies by machine)
oxipng -o 4 -i 0 *.png
```

> [!NOTE]
> Don’t stress about tooling differences — just make sure files are “reasonably optimized” before committing.

---

## 🔗 Using screenshots in Markdown

Use **relative paths** so images render on GitHub and inside our docs pipeline.

```md
![Layer list open in Map Viewer](./ui/map-viewer/2026-01-15__map-viewer__layer-list__open__desktop-1440w__light.webp)
```

### Captions (optional)
```md
*Figure: The layer list panel open with timeline controls visible.*
```

---

## 🔁 Pull Requests & reviews

For UI changes, always include screenshots in the PR description:

- **Before**
- **After**
- **Any edge states** (empty/error/loading) if relevant

If the screenshot is important long-term (docs, release notes, regression baseline), also commit it here using the conventions above.

---

## ✅ Definition of Done checklist

When adding/updating screenshots in this folder:

- [ ] File name follows the pattern (date + surface + state + viewport + theme)
- [ ] No secrets / PII / sensitive info visible
- [ ] Image is optimized (reasonable size)
- [ ] Alt text exists wherever the image is referenced
- [ ] (Recommended) `.meta.json` added for doc/release/evidence screenshots
- [ ] Folder tree updated if you created new directories

---

## 🧹 Housekeeping

- Move outdated-but-kept screenshots into `/_archive/`
- Prefer updating existing screenshots over adding duplicates
- If an image is no longer referenced anywhere, consider removing it (or archiving if it documents an important milestone)

---

⬆️ **Back to top:** [Screenshots](#-screenshots)
