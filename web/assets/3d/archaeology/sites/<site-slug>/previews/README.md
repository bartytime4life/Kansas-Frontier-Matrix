# 🖼️ 3D Site Previews (Archaeology) — `previews/`

![KFM](https://img.shields.io/badge/KFM-3D%20Archaeology-blue)
![Evidence-First](https://img.shields.io/badge/principle-evidence--first-success)
![2D+3D](https://img.shields.io/badge/viewers-MapLibre%20%2B%20Cesium-informational)
![Media](https://img.shields.io/badge/media-WebP%20%7C%20AVIF%20%7C%20MP4-orange)
![Governance](https://img.shields.io/badge/governance-policy%20pack-critical)

> **Purpose:** This folder holds **web-friendly, fast-loading preview media** (thumbs/posters/clips) for a site’s 3D archaeology assets.  
> Think of it as the UI “cover art” + “teaser trailer” — **not** the authoritative dataset. 🧾➡️🖼️

---

## 📍 Location (you are here)

`web/assets/3d/archaeology/sites/<site-slug>/previews/`

✅ Keep paths **relative** and **stable** so Story Nodes + UI galleries don’t break.

---

## 🧭 Per-site TODOs (copy/paste checklist)

- [ ] Replace **`<site-slug>`** references (if you pasted this from a template).
- [ ] Add `previews.manifest.json` (required) 📦
- [ ] Add `thumb.webp` (required) 🧷
- [ ] Confirm `classification` + location precision rules 🔒
- [ ] Add credits/licensing + evidence links 🧾
- [ ] Strip EXIF / geo-tags from all images & video 🧼

---

## 📦 What belongs in `previews/` (and what doesn’t)

### ✅ Belongs here
- **Thumbnails** (cards, search results, mini-galleries)
- **Posters / hero images** (site landing pages, Story Node headers)
- **Short clips** (orbit teaser, flythrough teaser)
- **Context snapshots** (generalized map context, scale view, stratigraphy diagram)

### 🚫 Does *not* belong here
- Full-res scans / raw photogrammetry outputs 🧱
- Full 3D tilesets / heavy GLBs (put those in the 3D asset area or artifact storage) 🗃️
- Anything that leaks restricted coordinates or sensitive details 🔐

---

## 🧱 Recommended folder layout

```text
web/assets/3d/archaeology/sites/<site-slug>/
├─ previews/ 🖼️
│  ├─ README.md
│  ├─ previews.manifest.json   # required ✅
│  ├─ thumb.webp               # required ✅
│  ├─ poster.webp              # recommended ⭐
│  ├─ orbit.mp4                # optional 🎞️
│  ├─ context.webp             # optional 🗺️ (must respect sensitivity)
│  ├─ wireframe.webp           # optional 🧵 (QA: mesh/tiles quality)
│  └─ time/                    # optional ⏳ (multi-era posters)
│     ├─ 1850_poster.webp
│     └─ 1930_poster.webp
└─ (elsewhere)
   ├─ models/ / tilesets/ / scans/  # authoritative 3D assets live elsewhere
   └─ sources/ / catalogs/          # evidence + provenance live elsewhere
```

---

## ✅ Required deliverables

| File | Why it exists | Min spec |
|---|---|---|
| `previews.manifest.json` | Single source of truth: what previews exist + how to use them | Valid JSON, includes `classification`, `assets[]`, `license`, `attribution` |
| `thumb.webp` | Small image for lists/cards/search | Square (recommended), lightweight |

---

## ⭐ Recommended deliverables

| File | Use | Suggested target |
|---|---|---|
| `poster.webp` | Hero/cover image for the site | 16:9 or 3:2, visually clean |
| `orbit.mp4` | Short teaser clip | ~5–12s, muted by default |
| `context.webp` | 2D context snapshot | **Generalized** if location is sensitive |
| `wireframe.webp` | QA preview of geometry quality | Same camera as poster if possible |
| `time/<era>_poster.webp` | 4D / timeline eras | Match era naming to timeline/story |

---

## 🧩 Naming rules (boring on purpose ✅)

- Use **kebab-case** file names.  
- Avoid coordinates in file names (no `39.05_-96.12.webp`) 🚫
- Prefer **purpose-first** names:
  - `thumb.webp`, `poster.webp`, `context.webp`, `orbit.mp4`
- For multi-era:
  - `time/<YYYY>_poster.webp` or `time/<YYYY-YYYY>_poster.webp`

---

## 🧾 `previews.manifest.json` (recommended schema)

This manifest lets the UI and Story tooling:
- discover what media exists,
- render it accessibly (alt text),
- enforce sensitivity/governance (classification),
- and keep evidence/provenance attached to visuals. 🧠🧾

### Example (copy/paste)

```json
{
  "site_slug": "<site-slug>",
  "title": "<Human readable site name>",
  "preview_manifest_version": 1,

  "classification": {
    "level": "public",
    "location_precision_m": 5000,
    "notes": "If restricted, use generalized context images only."
  },

  "license": "CC-BY-4.0",
  "attribution": "Photo/Render: <Name/Org>. Data sources listed under provenance.",

  "assets": [
    {
      "id": "thumb",
      "type": "image",
      "src": "thumb.webp",
      "width": 512,
      "height": 512,
      "alt": "Generalized overview preview of <site name> (no exact location).",
      "caption": "Preview for UI cards."
    },
    {
      "id": "poster",
      "type": "image",
      "src": "poster.webp",
      "width": 1920,
      "height": 1080,
      "alt": "3D overview render of <site name> showing major features.",
      "caption": "Hero image used by the site landing page and Story headers."
    },
    {
      "id": "orbit",
      "type": "video",
      "src": "orbit.mp4",
      "duration_s": 8,
      "captions": [],
      "alt": "Short orbit teaser around the site model (muted by default)."
    }
  ],

  "reconstruction": {
    "level": "measured",
    "disclaimer": "If interpretive reconstruction is used, label it clearly and link evidence."
  },

  "provenance": {
    "evidence_triplet": {
      "stac_item": "",
      "dcat_record": "",
      "prov_activity": ""
    },
    "hashes": {
      "thumb.webp": "sha256:<fill>",
      "poster.webp": "sha256:<fill>",
      "orbit.mp4": "sha256:<fill>"
    }
  },

  "qa": {
    "exif_stripped": true,
    "no_precise_coords_in_text": true,
    "size_budgets_met": true
  }
}
```

---

## 🔒 Sensitivity + cultural protocols (non-negotiable)

> ⚠️ Archaeology data can be sensitive. Treat previews as **publishable outputs** that can leak location/context.

Minimum practices:
- **If classification isn’t known → do not publish previews** (fail-closed mindset) 🔒
- **Generalize location** in any “context” imagery (use region/area, not a pin)
- Remove geo-EXIF and camera metadata from exported media 🧼
- Don’t embed coordinates in filenames, alt text, captions, or overlays 🚫
- If a site is culturally sensitive, ensure previews respect access protocols (CARE-aligned behavior) 🪶

---

## 🧠 Evidence-first previews (trust-building UI)

Previews should never become “pretty truth”. ✨➡️❌  
If a preview shows an interpretation or reconstruction:
- Label it in `reconstruction.level`
- Add a short disclaimer
- Link to evidence via the provenance fields (STAC/DCAT/PROV) 🧾

---

## ⚡ Performance budgets (keep the UI snappy)

Suggested budgets (tune as needed):
- `thumb.webp` ≤ **150 KB**
- `poster.webp` ≤ **600 KB**
- `orbit.mp4` ≤ **3–6 MB**

General tips:
- Prefer WebP/AVIF for images 🖼️
- Prefer short MP4 clips for motion 🎞️
- Avoid UI chrome (no debug overlays) 🙅

---

## ♿ Accessibility & credits

For every asset:
- Provide **alt text** in the manifest (required for meaningful UI rendering) ♿
- Provide attribution & license
- For video: include captions or note “no spoken content” if purely visual

---

## 🔗 Using previews in Story Nodes

If your Story Node needs a hero/cover, reference the preview asset **by relative path**:

```md
![<short alt>](../../../../assets/3d/archaeology/sites/<site-slug>/previews/poster.webp)
```

Or in a Story config JSON (example pattern):

```json
{
  "media": {
    "hero": "web/assets/3d/archaeology/sites/<site-slug>/previews/poster.webp",
    "thumb": "web/assets/3d/archaeology/sites/<site-slug>/previews/thumb.webp",
    "gallery": [
      "web/assets/3d/archaeology/sites/<site-slug>/previews/context.webp"
    ]
  }
}
```

---

## 🧰 Suggested tooling (pick your poison 🧪)

- **Blender** (consistent renders)
- **Cesium viewer** (camera-matched screenshots)
- **Three.js** (scripted preview rendering)
- **ffmpeg** (video encoding)
- **ImageMagick** (format conversion)

<details>
  <summary>📎 Optional: lightweight command recipes</summary>

```bash
# Convert PNG -> WebP (quality 82)
magick input.png -strip -quality 82 output.webp

# Encode a short MP4 teaser (H.264)
ffmpeg -i input.mov -an -vf "scale=1920:-2" -t 10 -crf 23 -preset medium orbit.mp4
```
</details>

---

## ✅ PR / commit checklist

- [ ] `previews.manifest.json` added/updated
- [ ] All preview files referenced in the manifest exist
- [ ] Sizes meet budget targets
- [ ] No EXIF / geotags / coordinate leaks
- [ ] Classification + reconstruction labeling completed
- [ ] License + attribution present
- [ ] Evidence links included (when applicable)

---

### 🧠 Guiding principle (tl;dr)

**Fast previews, strong provenance, zero accidental leakage.** ✅🔒🧾

