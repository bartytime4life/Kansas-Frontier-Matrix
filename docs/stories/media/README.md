# 🎬 `docs/stories/media` — Story Media Library

![Provenance Required](https://img.shields.io/badge/provenance-required-1f6feb)
![Accessible Media](https://img.shields.io/badge/a11y-alt%20%2B%20captions%20%2B%20transcripts-brightgreen)
![Web-Ready](https://img.shields.io/badge/web--ready-optimized-orange)
![KFM](https://img.shields.io/badge/KFM-evidence--first-6f42c1)

> 🧭 **Purpose:** This folder holds **web-ready media assets** used by `docs/stories/*` (images, audio, video, map exports, diagrams, small downloads).  
> 🧾 **Rule:** If it appears in a story, it must be **traceable** (“map behind the map”) and **safe to publish**.

---

## ✨ Principles (KFM Storytelling Standard)

### 1) 🧾 Evidence-first, always
Every asset must have enough metadata to answer:
- **Where did this come from?**
- **What license allows us to use it?**
- **What processing did we do?**
- **How do we reproduce it?**

This aligns with KFM’s “truth path” and provenance-driven architecture (Raw ➜ Processed ➜ Catalog ➜ DB ➜ API ➜ UI/AI).  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 2) ⚡ Web-friendly by default
This is the docs/UI layer. Prefer **optimized derivatives** (thumbnails, compressed images, short clips), not raw data dumps.

### 3) ♿ Accessibility is non-negotiable
- Images: **alt text**
- Video: **captions** (or at minimum a transcript)
- Audio: **transcript**
- Avoid text baked into images when possible

(Use semantic patterns like `<figure>` + `<figcaption>` for captions.)  [oai_citation:1‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

### 4) 🧩 Consistency beats cleverness
Consistent naming, predictable structure, and clean navigation reduce cognitive load and keep stories usable.  [oai_citation:2‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)

---

## 🗂️ Recommended Folder Layout

```text
docs/
└─ stories/
   ├─ <story-slug>.md
   └─ media/
      ├─ README.md               👈 you are here
      ├─ shared/                ♻️ reusable across stories
      │  ├─ images/
      │  ├─ icons/
      │  └─ maps/
      └─ <story-slug>/           🧵 story-specific assets
         ├─ images/
         ├─ maps/
         ├─ audio/
         ├─ video/
         ├─ downloads/
         └─ media.yaml           ✅ REQUIRED manifest (see below)
```

**Rules of thumb**
- ✅ Put assets in `media/<story-slug>/...` unless they’re genuinely reusable → then use `media/shared/...`.
- ✅ Keep **source-of-truth datasets** out of this folder (see “🚫 What not to commit” below).

---

## 🔗 How to Reference Media in Stories

### ✅ Simple image (Markdown)
```md
![Dust Bowl aerial photo (1930s), cropped to western Kansas](./media/dust-bowl/images/dustbowl_aerial_1930s.webp)
```

### ✅ Figure + caption (HTML for stronger semantics)
```html
<figure>
  <img
    src="./media/dust-bowl/images/ndvi_trend_1934_1954.webp"
    alt="NDVI trend map comparing 1934 and 1954 across Kansas counties."
  />
  <figcaption>
    NDVI trend (1934→1954). Derived from curated remote sensing pipeline outputs.
  </figcaption>
</figure>
```
Semantic figures/captions are the preferred pattern for story media.  [oai_citation:3‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)

### ✅ Video embed (HTML)
```html
<video controls preload="metadata" width="100%">
  <source src="./media/dust-bowl/video/dustbowl_timeline_30s.mp4" type="video/mp4" />
  Sorry — your browser doesn’t support embedded video.
</video>
<p><em>Captions/transcript required in <code>media.yaml</code>.</em></p>
```

---

## 🧾 REQUIRED: `media.yaml` Manifest (Per Story)

Each story folder **must** include a `media.yaml` file documenting every asset used.

### ✅ Minimal schema (required fields)
- `id` — stable identifier (kebab-case)
- `type` — `image | map | audio | video | download`
- `file` — relative file path from this story’s media folder
- `title`
- `alt` — required for images/maps
- `caption` — recommended
- `credit`
- `license` — explicit (e.g., `Public Domain`, `CC BY 4.0`, etc.)
- `source` — where it came from (URL or archive reference)
- `acquired` — `YYYY-MM-DD`
- `provenance` — short list of steps or transform notes
- `sha256` — checksum for integrity

### 🧩 Example `media.yaml`
```yaml
story: dust-bowl
assets:
  - id: dustbowl_aerial_1930s
    type: image
    file: images/dustbowl_aerial_1930s.webp
    title: "Dust Bowl aerial photo (1930s)"
    alt: "Aerial view of wind-eroded farmland with visible dust drift patterns."
    caption: "A representative Dust Bowl-era aerial image used for narrative context."
    credit: "Public domain / archive source (see source)"
    license: "Public Domain"
    source: "ARCHIVE_REF_OR_URL_HERE"
    acquired: "2026-02-05"
    provenance:
      - "Cropped to Kansas-relevant area"
      - "Converted to WebP for docs performance"
      - "Color corrected for readability (non-destructive intent)"
    sha256: "REPLACE_WITH_REAL_SHA256"

  - id: ndvi_trend_1934_1954
    type: map
    file: maps/ndvi_trend_1934_1954.webp
    title: "NDVI trend map (1934→1954)"
    alt: "Kansas county choropleth map showing NDVI trend differences between 1934 and 1954."
    caption: "Derived from remote sensing pipeline outputs; see linked dataset in source."
    credit: "KFM pipeline output"
    license: "CC BY 4.0 (or project license)"
    source: "KFM_DATASET_ID_OR_STAC_ITEM_URL"
    acquired: "2026-02-05"
    provenance:
      - "Rendered from PostGIS query output"
      - "Exported at 1600px width"
      - "Legend + scale bar added"
    sha256: "REPLACE_WITH_REAL_SHA256"
```

> 🔎 **Why a manifest?** KFM’s value proposition is transparency: every layer, chart, and narrative element is traceable and governed.  [oai_citation:4‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🖼️ Image Standards

### ✅ Pick the right format
Use the format that matches the content:

| Content | Preferred | Avoid | Why |
|---|---|---|---|
| Photos | `.webp` (or `.jpg`) | `.png` | Photos compress well with lossy formats |
| Diagrams / UI screenshots | `.webp` or `.png` | ultra-large `.jpg` | Sharp edges + text need lossless-ish handling |
| Icons / simple shapes | `.svg` | raster icons | Scales cleanly |
| Transparency needed | `.png` or `.webp` | `.jpg` | JPEG has no alpha |

Background context: bitmap vs vector tradeoffs, and lossy vs lossless compression matter for readability and storage.  [oai_citation:5‡Various Programming Concepts.pdf](sediment://file_00000000e86c71fd9eceb7eec4bba22e)

### 📏 Size budgets (docs-friendly)
- **Images:** aim for **≤ 400 KB** each (exceptions allowed for hero images)
- **Hero images/maps:** aim for **≤ 1.2 MB**
- **Max width:** 1600–2000px is usually plenty for docs

### 🎨 Color & clarity
- Prefer **sRGB** exports
- Avoid exporting CMYK-only assets
- If the asset contains text, verify readability on mobile widths

---

## 🗺️ Map & GIS Media Standards

### ✅ What belongs here
Put **story-friendly derivatives** here:
- map screenshots / exported panels
- annotated diagrams
- small GeoJSON snippets used purely for teaching/demos
- thumbnails/posters

### 🧱 What does *not* belong here
KFM’s architecture expects big geospatial assets to live in the governed data pipeline (object storage + catalogs + provenance). This folder is the docs UI layer.  [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

So **do not commit**:
- raw satellite scenes / large rasters
- LiDAR point clouds
- large shapefiles / file geodatabases
- multi-GB tilesets
- anything that should live in PostGIS / STAC / catalog

### 🧭 Design considerations (for exported maps)
Keep map exports consistent across stories:
- include a **legend** when needed
- include a **scale bar** when meaningful
- use consistent naming for layers
- avoid ambiguous color ramps (be mindful of colorblind accessibility)
- label your geography/timeframe clearly in caption + manifest

---

## 🎧 Audio Standards

- Preferred: `.mp3` (or `.ogg` if needed)
- Always include:
  - transcript text (in `media.yaml` or as `audio/<id>.md`)
  - source + license
- Keep clips short for docs usage

---

## 🎞️ Video Standards

- Preferred: `.mp4` (H.264/AAC)
- Must include:
  - captions or transcript
  - source + license
- Keep it small:
  - target **≤ 20 MB** per clip for docs
  - if bigger, host externally (object storage/CDN) and link

---

## 🧪 Optimization Tips (Suggested Commands)

> ✅ These are optional, but recommended for performance hygiene.

### Convert PNG/JPG to WebP (example)
```bash
# Example using cwebp (install separately)
cwebp -q 80 input.png -o output.webp
```

### Compute SHA256 checksum
```bash
# macOS / Linux
shasum -a 256 path/to/file.webp

# Windows (PowerShell)
Get-FileHash path\to\file.webp -Algorithm SHA256
```

---

## ✅ PR Checklist (Media)

Before merging story media:
- [ ] Files placed under correct story slug folder ✅
- [ ] `media.yaml` updated with **every** referenced asset ✅
- [ ] License + source included (no “unknown license”) ✅
- [ ] Alt text present for every image/map ✅
- [ ] Captions/transcripts provided where required ✅
- [ ] File sizes are reasonable (web-friendly) ✅
- [ ] Links in story render correctly in GitHub/docs build ✅

---

## 🚫 Hard “No” List (Governance & Safety)

Do not add:
- private / sensitive personal data (PII)
- restricted Indigenous site locations (unless explicitly permitted + governed)
- copyrighted material without permission/license
- secrets, keys, tokens, credentials
- “mystery files” without provenance

KFM’s governance model assumes we can explain and defend every asset we publish.  [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 📚 Reference Library (Project Sources)

These references inform the standards used in this folder:

- **Kansas Frontier Matrix — Comprehensive System Documentation** (provenance-first, governed pipeline, UI/AI architecture).  [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- **Professional Web Design: Techniques and Templates (5e)** (usability, consistency, planning, and accessibility-minded design patterns).  [oai_citation:9‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- **Learn to Code HTML & CSS** (semantic media patterns like figures/captions and web-safe presentation habits).  [oai_citation:10‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- **Compressed Image File Formats (JPEG/PNG/GIF, etc.)** (bitmap vs vector concepts; compression considerations; format tradeoffs).  [oai_citation:11‡Various Programming Concepts.pdf](sediment://file_00000000e86c71fd9eceb7eec4bba22e)  
- **Node.js (Apress) — Foundations** (event-driven performance mindset relevant to serving media efficiently in web apps).  [oai_citation:12‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  

---

## 🙌 Quick Start Template (Copy/Paste)

1) Create folder:
```text
docs/stories/media/<story-slug>/
```

2) Add files under:
```text
images/ maps/ audio/ video/ downloads/
```

3) Add/Update:
```text
docs/stories/media/<story-slug>/media.yaml
```

4) Reference assets in your story with relative paths:
```md
![Alt text](./media/<story-slug>/images/example.webp)
```

✅ Done. Your story now has traceable, web-ready media.