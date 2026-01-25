<!--
📌 Path: web/assets/3d/archaeology/sites/<site-slug>/thumbs/README.md
🎯 Purpose: Web-ready preview images ("thumbs") for this archaeology 3D site package.
-->

# 🖼️ Thumbs for `<site-slug>` (Archaeology 3D Site)

![asset](https://img.shields.io/badge/asset-thumbnails-blue)
![domain](https://img.shields.io/badge/domain-archaeology%20%2F%203D-blueviolet)
![ui](https://img.shields.io/badge/UI-MapLibre%20%2B%20Cesium-informational)
![governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-orange)
![provenance](https://img.shields.io/badge/provenance-required-success)

This folder contains **thumbnail images** used by the KFM web UI (and future AR / Story experiences) to represent this site in:
- 🔎 search results & discovery cards
- 🧩 layer/site panels (2D & 3D)
- 📚 Story Nodes / narrative “cards”
- 📦 offline data packs (lightweight previews)

> [!IMPORTANT]
> **This folder is treated as web-public by default.**
> Do **not** place restricted imagery here (e.g., anything that reveals sensitive site locations or community-restricted media).

---

## 📂 Where you are

```text
🌐 web/
└── 🧰 assets/
    └── 🧊 3d/
        └── 🏺 archaeology/
            └── 🏞️ sites/
                └── 🏷️ <site-slug>/
                    └── 🖼️ thumbs/
                        ├── 📄 README.md                   👈 📍 you are here
                        ├── 🧾 thumbs.json                 ✅ required (manifest)
                        ├── 🖼️ thumb-512.webp              ✅ required (card preview)
                        ├── 🏞️ thumb-1024.webp             ⭐ recommended (hero/expanded)
                        ├── 🧱 thumb-square-256.webp        ✅ required (square tile/icon)
                        ├── 🧱 thumb-square-512.webp        ⭐ recommended (square tile/icon @2x)
                        ├── 🌫️ blurhash.txt                (optional)
                        ├── 🏷️ ATTRIBUTION.md              (optional)
                        └── 📜 LICENSE.md                   (optional)
```

---

## ✅ Folder contract

### Required files
| File | Role | Target usage |
|---|---|---|
| `thumbs.json` | 🧾 Manifest (metadata + provenance) | UI + validators + future catalog sync |
| `thumb-512.webp` | 🖼️ Standard “card” thumbnail | Search results / lists / layer cards |
| `thumb-square-256.webp` | 🧱 Square icon thumbnail | Compact grids / chips / placeholders |

### Recommended files
| File | Role | Why it matters |
|---|---|---|
| `thumb-1024.webp` | 🖼️ Hero / expanded view | Crisp on high-DPI + Story Node headers |
| `thumb-square-512.webp` | 🧱 Square @2x | Clean on retina + AR selectors |
| `blurhash.txt` | 🌫️ LQ placeholder | Faster perceived loading (optional) |

> [!TIP]
> Keep names stable. The UI can rely on predictable filenames **and** the manifest.

---

## 📐 Image specs

### Formats
- ✅ Prefer **WebP**: `.webp`
- ✅ Use `.png` only when transparency is required (rare for site previews)
- ✅ Use `.jpg` only for compatibility fallbacks (if needed)

### Dimensions & aspect ratios (recommended standard)
| Asset | Size | Aspect |
|---|---:|---:|
| `thumb-512.webp` | 512×288 | 16:9 |
| `thumb-1024.webp` | 1024×576 | 16:9 |
| `thumb-square-256.webp` | 256×256 | 1:1 |
| `thumb-square-512.webp` | 512×512 | 1:1 |

### Visual guidelines (what makes a “good” thumb)
- 🎯 **Readable at small sizes** (major shapes/features visible)
- 🌤️ **Neutral lighting / high contrast**
- 🧭 Avoid UI overlays (scale bars, coordinate readouts, debug HUDs)
- 🧼 Avoid busy basemap labels (and anything that “gives away” exact location)
- 🧠 Prefer a **3/4 oblique view** for 3D assets (depth + recognizability)

---

## 🔒 Sensitive sites & ethical handling (FAIR + CARE mindset)

Some archaeology/cultural heritage assets must be handled with extra care.

**If anything about this site is sensitive:**
- Do **not** include imagery that can be reverse-located (distinct aerial landmarks, labeled streets, GPS EXIF, etc.)
- Prefer “non-locational” previews:
  - artifact photo (with permission)
  - close-up texture detail
  - schematic silhouette / stylized render
  - generalized 3D model preview on a neutral background

> [!WARNING]
> If the site’s classification is **not** `public`, do not store thumbs here.  
> Use a restricted asset channel/store and only ship safe/public derivatives into `web/assets/`.

---

## ♿ Accessibility expectations

Even for thumbnails, treat accessibility as a first-class requirement:
- Every image must have **alt text** in `thumbs.json`
- Alt text should be:
  - short (1 sentence)
  - descriptive (what it is, not “image of…”)
  - non-sensitive (don’t include restricted details)

Optional: include a longer `caption` for Story Nodes.

---

## ⚡ Performance budgets

Thumbnails should be **fast** (especially on mobile + offline packs).

Suggested budgets:
- `thumb-512.webp` ≤ **150 KB**
- `thumb-1024.webp` ≤ **350 KB**
- `thumb-square-256.webp` ≤ **80 KB**
- `thumb-square-512.webp` ≤ **180 KB**

Additional rules:
- Strip metadata (EXIF/GPS) ✅
- sRGB color space ✅
- Avoid alpha unless needed ✅

---

## 🧾 `thumbs.json` manifest

This manifest is the **mini data contract** for the thumbs folder: it tells the UI what exists, how to use it, and how it was created.

### Example `thumbs.json`
```json
{
  "site": {
    "slug": "<site-slug>",
    "kfm_id": "kfm.archaeology.site.<site-slug>",
    "classification": "public",
    "notes": "Public-safe thumbs only."
  },
  "thumbnails": [
    {
      "id": "card",
      "file": "thumb-512.webp",
      "width": 512,
      "height": 288,
      "mime": "image/webp",
      "sha256": "<sha256-hex>",
      "alt": "Oblique 3D view of the site model highlighting the main mound structure.",
      "caption": "Preview render derived from the public 3D tileset.",
      "license": "CC-BY-4.0",
      "attribution": "KFM / Contributors",
      "source": {
        "derived_from": [
          "../tileset/tileset.json"
        ],
        "method": "render+screenshot+optimize",
        "tooling": [
          "CesiumJS",
          "ImageMagick|sharp"
        ],
        "recipe_ref": "thumbs.recipe.json"
      },
      "created_at": "YYYY-MM-DD",
      "created_by": "human",
      "review": {
        "sensitivity_checked": true,
        "location_reveal_risk": "low"
      }
    }
  ]
}
```

### Optional: `thumbs.recipe.json`
If you generate thumbs from a 3D viewer/camera, store a “recipe” so the result is reproducible:
- camera heading/pitch/roll
- distance/fov
- render preset (lighting/shadows)
- background color
- output sizes + quality targets

---

## 🛠️ Generation tips (repeatable + clean)

### Strip metadata (EXIF/GPS)
```bash
# ImageMagick (strip profiles/metadata)
magick input.png -strip output.webp
```

### Generate 16:9 thumbs (crop-to-fit)
```bash
magick source.png \
  -resize 1024x576^ \
  -gravity center \
  -extent 1024x576 \
  -strip \
  -quality 82 \
  thumb-1024.webp
```

### Generate square thumbs
```bash
magick source.png \
  -resize 512x512^ \
  -gravity center \
  -extent 512x512 \
  -strip \
  -quality 82 \
  thumb-square-512.webp
```

> [!NOTE]
> The exact tooling is flexible (Node `sharp`, ImageMagick, etc.).  
> What matters is **repeatability**, **provenance**, and **web performance**.

---

## 🤖 AI assistance (optional, always human-reviewed)

AI can help with:
- smart crop suggestions (saliency / subject detection)
- draft alt text proposals
- quality checks (file size, contrast, text legibility)

Rules of engagement:
- ✅ AI output is a **proposal**, not an authority
- ✅ record AI involvement in `thumbs.json` (`created_by: "ai-assisted"`, add tool/version)
- ✅ a human reviews for sensitivity, accuracy, and licensing

---

## ✅ QA checklist (PR-ready)

- [ ] Files present: required thumbs + `thumbs.json`
- [ ] Sizes match the contract (dimensions + formats)
- [ ] **No EXIF/GPS metadata**
- [ ] File sizes within budget
- [ ] Alt text exists and is non-sensitive
- [ ] License + attribution included
- [ ] If site is sensitive: only public-safe imagery shipped here
- [ ] `sha256` updated in manifest (if used)

---

## 🔗 Integration hints (UI / Story Nodes)

### Example: site-level metadata linking thumbs (illustrative)
```json
{
  "thumbnails": {
    "card": "thumbs/thumb-512.webp",
    "hero": "thumbs/thumb-1024.webp",
    "square": "thumbs/thumb-square-256.webp"
  }
}
```

### Example: Story Node using a thumb as a cover
```json
{
  "coverImage": "web/assets/3d/archaeology/sites/<site-slug>/thumbs/thumb-1024.webp",
  "coverAlt": "Oblique 3D view of the site model highlighting the main mound structure."
}
```

---

## 📚 Project references used to shape this folder

<details>
<summary><strong>Click to expand 📚</strong></summary>

### Core KFM docs (architecture + governance)
- 📄 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**  
  (standards, metadata expectations, licensing mindset)
- 🧱 **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf**  
  (2D/3D UX, Cesium integration, Story Nodes)
- 🧭🤖 **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf**  
  (human-in-the-loop AI, evidence/citation expectations)
- 🧩 **Kansas Frontier Matrix – Comprehensive UI System Overview.pdf**  
  (accessibility, performance, offline packs, AR direction)
- 📥 **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf**  
  (policy pack thinking, classification propagation, provenance-first publishing)
- 💡 **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf**  
  (layer provenance panels, evolving UX patterns)
- 🚀 **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf**  
  (AR/hybrid storytelling + cultural protocol awareness)
- 🧠 **Additional Project Ideas.pdf**  
  (domain integration consistency; archaeology artifact catalogs as a target domain)

### Reference libraries (implementation support)
- 🧠 **AI Concepts & more.pdf** (portfolio library: ML/AI references)
- 🗺️ **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf**  
  (portfolio library: WebGL + archaeology + virtual world references)
- 💻 **Various programming langurages & resources 1.pdf**  
  (portfolio library: JS/TS/web dev & tooling)
- 🧰 **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf**  
  (portfolio library: data engineering / governance / reproducibility concepts)

</details>

