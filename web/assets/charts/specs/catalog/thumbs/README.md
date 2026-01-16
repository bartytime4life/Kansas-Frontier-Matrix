# 📊 Chart Catalog Thumbnails (`web/assets/charts/specs/catalog/thumbs/`)

![asset](https://img.shields.io/badge/asset-thumbnails-2ea44f)
![scope](https://img.shields.io/badge/scope-web%20ui-blue)
![formats](https://img.shields.io/badge/preferred-webp%20%7C%20png-informational)
![governance](https://img.shields.io/badge/provenance-required-critical)

Tiny images. Big UX impact. ✨  
This folder holds **thumbnail previews** for the **Chart Spec Catalog** used by the KFM web UI. The goal is to make chart browsing fast, visual, and consistent—without inflating bundle size or breaking provenance principles.

> 🧭 **Provenance-first reminder:** every preview should be traceable to a single chart spec (same `id` / slug), and should not introduce “new claims” beyond what the spec/data already represent.

---

## ✅ What lives here

- 🖼️ **Thumbnail images** that visually represent a chart spec (gallery cards, pickers, catalogs)
- 🧩 (Optional) **Retina variants** for high-DPI screens (`@2x`)
- 🧾 (Optional) **Manifest metadata** if/when we automate validation (see below)

---

## 🚫 What does *not* live here

- ❌ Full-size chart renders (use a dedicated `renders/` or story asset folder)
- ❌ Data exports, CSVs, GeoJSON, STAC, etc.
- ❌ Random screenshots that aren’t tied to a spec (no orphan images)

---

## 🗂️ Folder map

```text
📁 web/
└─ 📁 assets/
   └─ 📁 charts/
      └─ 📁 specs/
         └─ 📁 catalog/
            ├─ 📄 catalog.json              (index of chart specs — if present)
            ├─ 📁 thumbs/                   (you are here ✅)
            │  ├─ 📄 README.md
            │  ├─ 🖼️ <spec_id>.webp
            │  ├─ 🖼️ <spec_id>@2x.webp      (optional)
            │  └─ 🖼️ <spec_id>.png          (fallback / transparency)
            └─ 📁 ...                       (spec JSON, schemas, helpers, etc.)
```

---

## 🧩 Naming contract (must-follow)

> **Rule of thumb:** if the chart spec is named `X`, the thumbnail is also named `X`.  
> This makes thumbnails deterministic build artifacts and easy to validate.

| Item | Requirement | Example |
|------|-------------|---------|
| Base filename | **Must match** the chart spec identifier (`spec_id`) | `precip_timeseries` |
| Allowed chars | `a-z`, `0-9`, `_` or `-` (pick one style per catalog) | `soil-moisture_v1` |
| Extension | Prefer `.webp`, allow `.png` | `soil-moisture_v1.webp` |
| Retina | Optional `@2x` suffix | `soil-moisture_v1@2x.webp` |

### ✅ Recommended slug style
- Prefer: `kebab-case` for web assets (`soil-moisture_v1.webp`)
- Acceptable: `snake_case` if the catalog already uses it (`soil_moisture_v1.webp`)
- Avoid: spaces, uppercase, non-ASCII, and “final_v3_REAL.webp” 😅

---

## 🖼️ Image specs (recommended defaults)

| Spec | Default | Notes |
|------|---------|------|
| Aspect ratio | **16:9** | Works well in cards/grids |
| Base size | **512×288** | Crisp but small |
| Retina | **1024×576** (`@2x`) | Optional for premium UI polish |
| Color space | sRGB | Predictable rendering |
| Background | Transparent or solid | Stay consistent across the catalog |
| Max weight | ~150–250 KB (soft cap) | Keep the UI snappy 🚀 |

> 🧠 Why separate thumbnail files (instead of embedding thumbnails inside JPEG metadata)?  
> Many JPEG/JFIF thumbnail structures exist but are “rarely used” in practice, so we keep thumbs as explicit, cacheable web assets.  [oai_citation:0‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)

---

## 🧱 Visual style guidelines

Keep thumbnails consistent so the catalog feels “designed,” not “dumped.”

- 🎯 **Focus on the shape of the data** (trend, distribution, clusters)
- 🧼 Prefer **clean margins** and a **neutral background**
- 🔤 Avoid tiny text (it becomes noise at thumbnail scale)
- 🧩 Use the **same theme** (gridlines / axis weight / font scale) across the set
- 🧭 If the chart has a legend, consider a simplified legend or omit it

---

## 🔁 Adding or updating a thumbnail

1. **Identify the spec id**  
   - Find the chart spec identifier used by the catalog (the thing the UI indexes by).
2. **Render the chart** (preferred)  
   - Generate the preview from the spec itself (deterministic + reproducible).
3. **Export** as `webp` (preferred) or `png` (fallback).
4. **Name it** exactly: `<spec_id>.webp` (and optionally `@2x`).
5. **Verify locally**  
   - Image opens, correct dimensions, looks readable at ~200px width.
6. **Commit** with the spec change in the same PR (spec + thumb stay in sync ✅).

---

## 🧪 QA checklist (Definition of Done ✅)

- [ ] Filename matches spec id exactly  
- [ ] Correct aspect ratio + size (or intentionally documented)  
- [ ] File size is reasonable (no multi‑MB thumbs)  
- [ ] No copyrighted imagery unless explicitly allowed + documented  
- [ ] Thumbnail is visually consistent with the catalog set  
- [ ] Spec + thumbnail updated in the same PR

> 📌 KFM governance leans “contract-first” and “deterministic pipeline” for artifacts; apply the same mindset here (stable inputs → stable outputs).  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔮 Optional: manifest (if we automate validation)

If/when we add automated checks, we can introduce a lightweight manifest like:

```json
{
  "precip_timeseries": {
    "file": "precip_timeseries.webp",
    "w": 512,
    "h": 288,
    "alt": "Precipitation time series chart preview"
  }
}
```

This enables:
- ✅ CI checks for missing thumbs
- ✅ Dimension validation
- ✅ Basic accessibility (alt text used in the catalog UI)

---

## 📚 References (project grounding)

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- MARKDOWN_GUIDE_v13 (contract-first + deterministic pipeline principles)  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Compressed Image File Formats (JPEG/JFIF thumbnail notes)  [oai_citation:6‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi) [oai_citation:7‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)  
