<div align="center">

# 🖼️ Story Image Assets

**Path:** `web/src/assets/images/story/`

_Optimized narrative media used by the Web UI’s StoryPanel / scrollytelling experiences._

[![scope](https://img.shields.io/badge/scope-web%2F%20ui-blue)](./)
[![performance](https://img.shields.io/badge/performance-keep%20it%20lightweight-success)](./)
[![accessibility](https://img.shields.io/badge/a11y-alt%20text%20required-orange)](./)
[![provenance](https://img.shields.io/badge/provenance-credit%20%26%20license%20required-purple)](./)

</div>

---

## 🧭 What belongs here

This folder contains **web-ready story images** that are **bundled with the frontend** (React/TS) and referenced by:

- 🧾 **Story markdown** (rendered in the StoryPanel)
- 🗺️ **Story state JSON** (the “scroll → map changes” choreography)
- 🧩 **Story UI components** (covers, thumbnails, inline figures, overlays)

> ✅ Think: “images that must reliably ship with the UI build and load fast.”

---

## 🧩 How this relates to Story Nodes (important)

KFM treats narrative content (Story Nodes) as *first-class* and governed content.  
The **canonical home for story markdown + story JSON + primary assets** is the Story Nodes area (docs side). The `web/` app is the presentation layer.

So, this directory should be treated as one of these patterns (pick one, project-wide):

1) **📦 UI mirror (recommended):** `web/src/assets/images/story/` holds **optimized copies** synced from Story Node folders.  
2) **🧷 UI-native:** this folder is the source of truth for images **only if** your story system is implemented entirely in the `web/` app.

> 🚫 Avoid “mystery duplicates.” If the same image exists in multiple places, decide which is canonical and document the sync rule.

---

## 📁 Expected folder layout

```text
web/src/assets/images/story/
├── 📄 README.md
├── 📁 _shared/                      # reusable story UI assets (frames, textures, common icons)
│   ├── 🖼️ parchment-texture.webp
│   └── 🖼️ divider-ornament.svg
├── 📁 _placeholders/                # skeleton / fallback media
│   ├── 🖼️ image-missing.webp
│   └── 🖼️ coming-soon.webp
└── 📁 <story-slug>/                 # one folder per published story
    ├── 📄 manifest.json             # optional: credits + captions + license + usage
    ├── 🖼️ 000_cover__v01.webp
    ├── 🖼️ 010_black-sunday__1935__v01.webp
    ├── 🖼️ 020_migration-map__1940__v01.webp
    └── 🖼️ 999_sources-collage__v01.webp
```

---

## 🏷️ Naming convention (stable URLs = fewer bugs)

**Goal:** predictable sorting + stable references from story JSON/markdown + easy diffing in PRs.

### ✅ Recommended pattern

```
<index>_<short-desc>__[<year-or-range>]__v<nn>.<ext>
```

Examples:
- `000_cover__v01.webp`
- `010_black-sunday__1935__v01.webp`
- `020_migration-map__1940__v02.webp`
- `110_portrait-mary-jane__1892-1901__v01.jpg`

**Rules**
- Use **lowercase-kebab** for `<short-desc>`
- Keep `<index>` **3 digits** to control ordering (`000`, `010`, `020`, …)
- Bump `vNN` when you change pixels (so caches don’t lie)
- If your story JSON references filenames, treat them as **API contracts** (don’t rename casually)

---

## 🧾 Provenance, credit, and licensing (non-negotiable)

Story media is part of the narrative “evidence surface.” Every image must have:

- **Credit line** (creator/organization)
- **Source** (archive, collection, link, accession ID if available)
- **License/rights** (public domain, CC BY, permission statement, etc.)
- **Date / time range** when known

### ✅ Recommended: sidecar `manifest.json`

Create `web/src/assets/images/story/<story-slug>/manifest.json`:

```json
{
  "storyId": "dust-bowl",
  "assets": [
    {
      "file": "010_black-sunday__1935__v01.webp",
      "alt": "Dust storm wall approaching farmland in Kansas, 1935.",
      "caption": "“Black Sunday” dust storm, 1935.",
      "credit": "Example Archive / Photographer Name",
      "license": "Public Domain",
      "source": "Archive collection ID or URL",
      "tags": ["dust-bowl", "1930s", "weather"]
    }
  ]
}
```

> 💡 Even if the UI doesn’t consume `manifest.json` yet, it’s an excellent governance + future-proofing move.

---

## ⚡ Performance rules (keep the story snappy)

### 🎯 Budgets (practical defaults)
- **Cover/hero:** ~250–400 KB (WebP/AVIF preferred)
- **Inline images:** ~80–200 KB
- **Thumbnails:** ~10–40 KB
- **Avoid “raw originals”** in this folder (put originals elsewhere, export web versions here)

### 🧰 Format guidance
- **Photos / scans:** `webp` (or `jpg` if needed)
- **Diagrams / crisp typography / transparency:** `png` (or `svg` if vector)
- **Tiny UI shapes / icons:** `svg`
- **Animations:** prefer CSS/Lottie; use `gif` only when truly necessary

> ✅ Correct format + compression matters. A beautiful story that loads slowly feels broken.

---

## ♿ Accessibility rules (story ≠ decoration)

### ✅ `alt` text is required for narrative images
- Be descriptive of *what the user needs to know*
- If the image is purely decorative: include `alt=""` (empty) **or** implement as a CSS background

### ✅ Prefer semantic figures for captioned media
When rendering story content (React or Markdown → HTML), use:

```html
<figure>
  <img src="..." alt="..." />
  <figcaption>Caption + credit + year.</figcaption>
</figure>
```

> 🧠 Screen readers and other assistive tech rely on meaningful `alt` text. Captions help everyone.

---

## 🔧 How to add a new story image (workflow)

1) 📁 Create (or use) a story folder: `web/src/assets/images/story/<story-slug>/`
2) 🖼️ Export **web-optimized** images (WebP preferred)
3) 🏷️ Name files using the convention above
4) 🧾 Add or update `manifest.json` (alt, caption, credit, license, source)
5) 🧪 Verify in the UI:
   - loads quickly
   - looks good on mobile
   - has correct caption/credit
   - no console errors / broken imports
6) ✅ PR checklist (below)

---

## ✅ PR checklist

- [ ] Files named with `NNN_desc__YYYY__vNN.ext`
- [ ] No uncompressed originals committed here
- [ ] `manifest.json` includes alt + caption + credit + license + source
- [ ] Visual check on mobile + desktop
- [ ] If referenced in story JSON/markdown, filenames match exactly
- [ ] No hotlinked external images in story content

---

## 🧯 Troubleshooting

### “My image works locally but not in production”
- If you referenced a **relative filesystem path** in markdown, bundlers may not copy it.
- Prefer **imports** (JS/TS) or a **known public asset base path**.

### “The image is blurry”
- Confirm the exported pixel size matches the largest display size.
- For text-heavy graphics, prefer `png`/`svg` or high-quality `webp`.

### “The UI feels slow”
- Re-check file sizes and format choices.
- Consider a thumbnail + click-to-expand pattern for very detailed scans.

---

## 🧠 Notes for future upgrades (nice-to-have)

- Add an `optimize:images` script (Sharp/Squoosh) to enforce budgets automatically 🛠️
- Generate responsive variants (`@1x`, `@2x`, `srcset`) for hero/cover images 📱
- Add CI checks to block oversized commits 🚦

---
