---
title: "🎨 Logos Metadata (web/assets/logos/_meta)"
version: "v1.0.0"
status: "active"
doc_kind: "Asset Governance"
last_updated: "2026-01-14"
license: "Inherit repo LICENSE"
classification: "open"
doc_uuid: "urn:kfm:doc:web:assets:logos:meta:readme:v1.0.0"
---

# 🎨 Logos Meta (KFM Web)

![status](https://img.shields.io/badge/status-active-brightgreen)
![scope](https://img.shields.io/badge/scope-web%2Fassets%2Flogos-blue)
![policy](https://img.shields.io/badge/policy-provenance--first-6f42c1)
![format](https://img.shields.io/badge/assets-SVG%20%7C%20PNG%20%7C%20WEBP-informational)

> **Purpose:** `_meta/` is where KFM treats **logos as governed assets** — with provenance, licensing/trademark notes, integrity hashes, and a predictable manifest for the Web UI. 🧾🧬

---

## 🧭 Quick links

- [Folder contract](#-folder-contract)
- [Directory map](#-directory-map)
- [Naming conventions](#-naming-conventions)
- [Metadata schema](#-metadata-schema)
- [Manifest + how the UI consumes it](#-manifest--how-the-ui-consumes-it)
- [Licensing, trademarks, and attribution](#-licensing-trademarks-and-attribution)
- [Security notes for SVG](#-security-notes-for-svg)
- [Performance + caching](#-performance--caching)
- [Contribution checklist](#-contribution-checklist)

---

## 📜 Folder contract

This folder **must only contain** metadata + governance files. ✅  
This folder **must never contain** the “real” logo assets. ❌

### ✅ Good fits for `_meta/`
- A **manifest** that the Web UI can load to list/select logos
- A **schema** (or documented contract) for metadata validation
- **Attribution** text (required by licenses/trademarks) for UI/legal pages
- **Checksums** for integrity + cache busting workflows
- A **gallery index** (optional) for quick human review

### ❌ Not allowed in `_meta/`
- Primary logo binaries (`.svg`, `.png`, `.webp`) — those belong in sibling folders
- Raw design files (`.fig`, `.ai`, `.psd`) — keep those in design/workbench locations, not the runtime asset pipeline
- Random screenshots, exports, or “temp” files (CI should fail these)

---

## 🗺️ Directory map

Below is the **expected** structure around this folder (adjust names if your repo differs, but keep the intent):

```text
📦 web/
└─ 🎨 assets/
   └─ 🏷️ logos/
      ├─ 🧩 kfm/                 # KFM-owned marks (preferred canonical assets)
      ├─ 🤝 partners/            # 3rd-party/provider logos (with permission + metadata)
      ├─ 🧭 ui/                  # favicons, app icons, social preview marks
      └─ 🗂️ _meta/               # 👈 governance + metadata (this folder)
         ├─ README.md
         ├─ logos.manifest.json          # ✅ recommended (consumed by UI/build)
         ├─ logo-meta.schema.json        # ✅ recommended (validation)
         ├─ attributions.md              # ✅ recommended (UI/legal)
         ├─ checksums.sha256             # ✅ optional (integrity + auditing)
         └─ gallery.index.json           # ✅ optional (human-friendly review)
```

---

## 🧾 Asset taxonomy

We treat logos as **three different classes** (because licensing + usage differs):

| Class | Folder suggestion | Typical use | Rules |
|---|---|---|---|
| 🧩 **KFM-owned marks** | `../kfm/` | header, footer, splash, share cards | Modifiable **only** with maintainer approval; metadata required |
| 🤝 **Partner/provider logos** | `../partners/` | attribution panels, “data sources” UI | **Do not edit** unless license permits; store attribution + trademark notes |
| 🧭 **UI platform icons** | `../ui/` | favicon, PWA icons, app tiles | Must follow web platform size + caching conventions |

---

## 🏷️ Naming conventions

### 1) Stable IDs (don’t encode meaning 🧠)
Every logo gets an **ID** that should remain stable even if the artwork evolves.

**✅ Good:** `kfm_mark`, `kfm_wordmark`, `usgs_logo`  
**❌ Avoid:** `kfm_mark_blue_2026`, `kfm_mark_32px`, `new_logo_final_final2`

> Rule of thumb: file *paths* can include variants; **IDs should not**.

### 2) Filenames (predictable variants 📐)
Use this filename pattern where possible:

```
<id>[--<variant>][@<scale>].<ext>
```

Examples:
- `kfm_mark.svg` (canonical vector)
- `kfm_mark--mono.svg`
- `kfm_mark@1x.png`
- `kfm_mark@2x.png`
- `kfm_wordmark--dark.svg`

### 3) Variant vocabulary (keep it small)
Recommended variants:
- `default`
- `light` / `dark`
- `mono`
- `outline`
- `badge` (only if truly a distinct lockup)

---

## 🧬 Metadata schema

Each logo **must** have machine-readable metadata so the UI can:
- render correct asset for light/dark themes 🌗
- display attribution 🧾
- surface provenance 🧬
- validate integrity ✅

### Recommended file format
- One metadata file per logo ID:
  - `logo.<id>.json` (preferred for web projects)
  - or `logo.<id>.yml` (if you prefer YAML)

### Recommended minimum fields

```json
{
  "id": "kfm_mark",
  "displayName": "Kansas Frontier Matrix — Mark",
  "kind": "mark",
  "owner": "Kansas Frontier Matrix",
  "variants": [
    {
      "name": "default",
      "theme": ["light", "dark"],
      "files": {
        "svg": "../kfm/kfm_mark.svg",
        "png_1x": "../kfm/kfm_mark@1x.png",
        "png_2x": "../kfm/kfm_mark@2x.png"
      }
    }
  ],
  "accessibility": {
    "alt": "Kansas Frontier Matrix logo"
  },
  "license": {
    "spdx": "All-Rights-Reserved",
    "type": "trademark",
    "attributionRequired": false,
    "notes": "KFM mark. Do not modify without approval."
  },
  "provenance": {
    "source": "internal",
    "sourceNotes": "Created for KFM branding.",
    "createdAt": "2026-01-14",
    "updatedAt": "2026-01-14"
  },
  "integrity": {
    "sha256": {
      "../kfm/kfm_mark.svg": "<sha256-hex>",
      "../kfm/kfm_mark@1x.png": "<sha256-hex>",
      "../kfm/kfm_mark@2x.png": "<sha256-hex>"
    }
  },
  "tags": ["brand", "kfm", "primary"]
}
```

### Extra fields (optional but nice ✨)
- `minSizePx` / `preferredSizePx` (helps UI choose when space is tight)
- `safeArea` (percentage or px guidance)
- `palette` (for mono/brand color constraints)
- `notes` (human notes for reviewers)

---

## 📦 Manifest + how the UI consumes it

### Why a manifest?
The manifest is the **single “gatekeeper” list** of what the Web UI is allowed to load/render.  
This prevents “random assets” from accidentally becoming UI-visible.

### Recommended manifest
`logos.manifest.json` (in this folder), containing:
- list of logos
- pointer to each logo’s metadata file
- optional “featured” or “priority” ordering

Example:

```json
{
  "version": 1,
  "generatedAt": "2026-01-14T00:00:00Z",
  "logos": [
    { "id": "kfm_mark", "meta": "./logo.kfm_mark.json" },
    { "id": "kfm_wordmark", "meta": "./logo.kfm_wordmark.json" }
  ]
}
```

> 💡 Tip: Treat the manifest like an API contract — if a logo isn’t in the manifest, it **does not exist** to the UI.

---

## 🧾 Licensing, trademarks, and attribution

### 1) KFM-owned marks
- Default posture: **protected brand asset**
- Metadata should record:
  - owner
  - whether modifications are permitted
  - approval required (yes/no)

### 2) Third‑party / partner logos 🤝
- Assume **trademark restrictions** by default unless you have explicit license text.
- Metadata must include:
  - attribution text (if required)
  - where the logo came from (URL, email approval, doc, etc.)
  - usage constraints (e.g., “do not recolor”, “do not crop”)

### 3) Attribution output
Keep a central, human-readable attribution file:

- `attributions.md` ✅ recommended

Suggested structure:

```md
## 🤝 Partner / Provider Attributions

- **USGS** — Trademark of the U.S. Geological Survey. Used for attribution of data sources.
- **NOAA** — Used for attribution of data sources.
- **NASA** — Used for attribution of data sources.

> If an attribution is legally required, it must appear in the UI (e.g., footer, “About”, or layer/source panels).
```

---

## 🔒 Security notes for SVG

SVG is powerful… and can be dangerous if treated as “just an image”.

✅ Required hygiene:
- No `<script>` tags
- No external references (`href="https://..."`, remote fonts, remote images)
- No event handlers (`onload=`, `onclick=` etc.)
- Avoid `foreignObject` unless explicitly reviewed

Recommended:
- run an SVG optimizer/sanitizer step (CI) before merge
- enforce a strict Content Security Policy (CSP) in the web app when possible

---

## 🚀 Performance + caching

### Format guidance
- **SVG**: canonical for logos and crisp scaling ✅
- **PNG**: use when platform requires raster (favicons, some share cards)
- **WEBP**: great for large raster marks (optional, if your stack supports it)

### Cache busting (favicons are sticky 😅)
Browsers can aggressively cache favicons. If a favicon changes:
- prefer filename fingerprinting (e.g., `favicon.<hash>.png`)
- or append a version query param (last resort)

### Integrity hashes
If you maintain `checksums.sha256`, it should cover **all files referenced by metadata**.  
This supports:
- integrity audits ✅
- deterministic builds ✅
- provenance reviews ✅

---

## ♿ Accessibility rules

- Every logo used in UI should have an `alt` (or `aria-label`) defined in metadata
- Decorative-only logos should explicitly be marked decorative and hidden from screen readers
- Ensure sufficient contrast for mono variants against map baselayers (KFM is map-heavy 🗺️)

---

## 🧰 Contribution checklist

When adding or updating a logo, PR must include:

- [ ] ✅ Canonical asset present (usually SVG)
- [ ] ✅ Variants present (if used in light/dark UI)
- [ ] ✅ `logo.<id>.json` added/updated
- [ ] ✅ `logos.manifest.json` updated (or re-generated)
- [ ] ✅ Attribution updated (if needed)
- [ ] ✅ Integrity hashes updated (if you use `checksums.sha256`)
- [ ] ✅ Visual spot-check (small size + on-map background)
- [ ] ✅ No unreviewed third-party trademarks or unclear licensing

---

## 🧪 Suggested CI gates (optional but recommended)

- Validate all `logo.*.json` files against `logo-meta.schema.json`
- Validate that every manifest entry points to an existing metadata file
- Validate that every metadata `files.*` path exists
- Validate that every referenced asset has a checksum entry (if checksums are enabled)
- Lint SVGs for forbidden tags/attributes

---

## 📚 Project reference shelf

<details>
<summary>📦 Click to expand the project/library files this README aligns with</summary>

> This folder applies the same **provenance-first, governed-contract** philosophy used across KFM data + documentation — but for branding assets.

- 🧾 Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf
- 🧭 MARKDOWN_GUIDE_v13.md.gdoc
- 📝 Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx
- 🧠 Flexible Software Design (stable identifiers excerpt in F-H programming Books.pdf)
- 🗺️ Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf
- 📱 Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf
- 🧭 making-maps-a-visual-guide-to-map-design-for-gis.pdf
- 🌐 responsive-web-design-with-html5-and-css3.pdf
- 🎮 webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf
- 🖼️ compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf
- 🛰️ Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf
- 📈 regression-analysis-with-python.pdf
- 📊 Regression analysis using Python - slides-linear-regression.pdf
- 🧪 Understanding Statistics & Experimental Design.pdf
- 📉 graphical-data-analysis-with-r.pdf
- 🧬 Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf
- 🗃️ PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf
- 🏛️ Archaeological 3D GIS_26_01_12_17_53_09.pdf
- 🧩 Data Spaces.pdf
- ⚙️ Scalable Data Management for Future Hardware.pdf
- 🚀 Database Performance at Scale.pdf
- 🤖 On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf
- 🌍 Introduction to Digital Humanism.pdf
- 🧠 think-bayes-bayesian-statistics-in-python.pdf
- ☕ concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf
- 🧰 python-geospatial-analysis-cookbook.pdf
- 🧱 Generalized Topology Optimization for Structural Design.pdf
- 📐 Spectral Geometry of Graphs.pdf
- 📚 A programming Books.pdf
- 📚 B-C programming Books.pdf
- 📚 D-E programming Books.pdf
- 📚 F-H programming Books.pdf
- 📚 I-L programming Books.pdf
- 📚 M-N programming Books.pdf
- 📚 O-R programming Books.pdf
- 📚 S-T programming Books.pdf
- 📚 U-X programming Books.pdf
- (Security books are present in the library; this README uses them only for defensive hygiene guidance, not offensive workflows.)

</details>

---

## 🧾 Changelog

- **v1.0.0 (2026-01-14)** — Initial governed README for logo metadata.
