# 📄 PDF Chart Exports (Print-Ready)  

![format](https://img.shields.io/badge/format-PDF-blue)
![assets](https://img.shields.io/badge/type-generated%20asset-lightgrey)
![provenance](https://img.shields.io/badge/provenance-required-brightgreen)
![governance](https://img.shields.io/badge/governance-FAIR%2BCARE-informational)

> [!IMPORTANT]
> This folder is for **exported chart PDFs** used by the **KFM web UI** and (optionally) linked from **Story Nodes** / reports.  
> Treat these as **generated artifacts**: reproducible, provenance-linked, and safe to overwrite.

---

## 📍 Location

`web/assets/charts/exports/pdf/`

---

## 🎯 What belongs here

✅ **Do:**
- 📈 **Print-ready chart exports** (`.pdf`) — time series, distributions, comparisons, etc.
- 🧾 **Sidecar metadata** (`.meta.json`) for provenance + reproducibility (strongly recommended)
- 🖼️ Optional **thumbnails** (`.png`) for quick previews (if the UI uses them)
- 🧰 Optional **manifest/index** file (if the UI needs a catalog of available exports)

🚫 **Don’t:**
- ❌ Store raw datasets here (those belong in `data/…` with STAC/DCAT/PROV)
- ❌ Hand-edit exported PDFs (edits will drift + get overwritten)
- ❌ Export anything that bypasses governance (no “mystery charts” without evidence links)

---

## 🧭 Canonical vs. Cache (KFM governance alignment)

KFM’s pipeline is strict: **ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**.

📌 Practical implication for this directory:
- **Canonical evidence** (the “source of truth”) should live in governed outputs (e.g., `data/processed/…` + DCAT/STAC + PROV).
- This folder is best treated as a **UI-friendly distribution/cache** of those artifacts (or as build-time packaged equivalents).

> [!NOTE]
> If a PDF chart is referenced in a Story Node / Focus Mode, it must be **traceable to cataloged sources** and **lineage (PROV)**. If it can’t be traced, it shouldn’t ship.

---

## 🗂️ Recommended layout

You can keep it flat, but subfolders scale better.

```text
📁 web/
  └── 📁 assets/
      └── 📁 charts/
          └── 📁 exports/
              └── 📁 pdf/
                  ├── 📄 README.md
                  ├── 📄 manifest.json                (optional)
                  └── 📁 <chart-id>/                  (recommended)
                      ├── 📄 <name>.pdf
                      ├── 📄 <name>.meta.json         (recommended)
                      └── 🖼️ <name>.thumb.png         (optional)
```

---

## 🏷️ Naming convention (stable + readable)

Keep names:
- ✅ **kebab-case**
- ✅ **no spaces**
- ✅ **stable identifiers** + **time window**
- ✅ **safe for URLs** (assets get served by the web app)

**Template:**
```text
<chartId>__<scope>__<start>_<end>__v<schema>
```

**Examples:**
- `rainfall-timeseries__county-allen__1950-01_2020-12__v1.pdf`
- `ndvi-summary__huc8-10270104__2018-01_2024-12__v1.pdf`

> [!TIP]
> If a chart is parameterized (county, basin, station, scenario), encode that in `<scope>`.

---

## 🧾 Sidecar metadata (`.meta.json`) — strongly recommended

Every PDF should have a sidecar file with:
- 🧬 **evidence links** (STAC/DCAT + PROV)
- 🧪 **input query** (API endpoint + params)
- 🧱 **render settings** (page size, orientation, DPI, theme)
- 🔐 **sensitivity flags** (if applicable)
- 🔏 **hashes** (for integrity + cache-busting)

<details>
<summary><strong>📦 Minimal example: <code>&lt;name&gt;.meta.json</code></strong></summary>

```json
{
  "id": "rainfall-timeseries__county-allen__1950-01_2020-12",
  "title": "Allen County Rainfall (1950–2020)",
  "chartType": "timeseries",
  "generatedAt": "2026-01-15T00:00:00Z",

  "generator": {
    "tool": "kfm-chart-exporter",
    "version": "0.0.0",
    "git": { "commit": "<commit-sha>" }
  },

  "inputs": {
    "api": {
      "endpoint": "/api/metrics/rainfall",
      "params": {
        "scope": "county:allen",
        "start": "1950-01-01",
        "end": "2020-12-31",
        "aggregation": "monthly"
      }
    }
  },

  "evidence": {
    "stacItems": ["data/stac/items/<item>.json"],
    "dcatDataset": "data/catalog/dcat/<dataset>.json",
    "provBundle": "data/prov/<prov-bundle>.json"
  },

  "rendering": {
    "page": { "size": "letter", "orientation": "landscape" },
    "dpi": 300,
    "theme": "kfm-light",
    "font": "system"
  },

  "safety": {
    "sensitivity": "public",
    "redactionsApplied": []
  },

  "checksums": {
    "sha256": "<sha256>"
  },

  "license": {
    "spdx": "<SPDX-ID-or-Custom>",
    "attribution": "<required attribution text>"
  }
}
```
</details>

---

## 🗃️ Optional manifest (`manifest.json`)

If the UI needs to list/download exports without scanning the filesystem at runtime, keep a manifest here.

✅ Recommended fields:
- `id`, `title`, `pdfPath`, `metaPath`, `thumbPath`
- `updatedAt`, `tags`, `scope`, `timeRange`
- `evidenceRefs` (STAC/DCAT/PROV pointers)

> [!NOTE]
> If the repo already defines a schema for this (under `schemas/`), validate against it in CI.

---

## 🖨️ Rendering quality checklist (don’t ship ugly PDFs 😅)

✅ **Legibility**
- Axis labels readable at 100% zoom
- Units included (mm, °C, ppm, etc.)
- Title + subtitle includes scope/time window

✅ **Fidelity**
- Prefer **vector output** where possible (SVG → PDF)
- Embed fonts (avoid missing glyphs on other machines)
- Avoid raster screenshots unless necessary (then use sufficient DPI)

✅ **Accessibility**
- Don’t rely on color alone (use markers / patterns when relevant)
- High contrast for printed copies
- Keep margins for printers + binding

✅ **Evidence + context**
- Include a small caption/footnote in the PDF *or* in metadata:
  - data source(s)
  - processing method/run ID (via PROV)
  - licensing requirements

---

## 🔁 Generation workflow (tool-agnostic)

Because the KFM UI is React-based and charts live in `web/` components, the **best exports come from rendering the same chart components** used in the app.

Typical export flow:
1. 🧾 Start from a **chart spec** (what to query + how to render)
2. 🔌 Fetch data via the **governed API** (never directly from the graph)
3. 🎨 Render the chart (headless browser render or SVG export pipeline)
4. 📄 Write:
   - `.pdf`
   - `.meta.json`
   - optional `.thumb.png`
5. 🗂️ Update `manifest.json` (if used)

> [!IMPORTANT]
> Exports must respect KFM governance: provenance-linked content only, no sensitive location leaks, and AI annotations must be clearly labeled when present.

---

## 🔒 Governance & safety

- 🧭 **API boundary rule**: exporters should retrieve data through `src/server/` API contracts (not direct graph access).
- 🪶 **Sovereignty & sensitivity**: never export precise locations when a dataset is classified as sensitive (generalize, blur, or omit).
- 🤖 **AI transparency**: if a caption/annotation is AI-assisted, label it in metadata and preserve the underlying evidence links.

---

## ✅ Definition of done (DoD)

Before committing/exporting:
- [ ] PDF renders with no clipping or layout shifts
- [ ] `.meta.json` exists (or the export is explicitly marked “no provenance = no ship”)
- [ ] Evidence refs included (STAC/DCAT + PROV)
- [ ] Naming convention followed
- [ ] No sensitive data leaks (especially coordinates & restricted datasets)
- [ ] Optional: manifest updated + validated

---

## 🔗 Related (project) references

- 📘 `docs/MASTER_GUIDE_v13.md` (pipeline invariants + governance)
- 🧾 `docs/standards/` (STAC / DCAT / PROV profiles)
- 🧠 `docs/reports/story_nodes/` (governed narratives; citations required)
- 🌐 `web/` (React UI, chart components, asset packaging)

---