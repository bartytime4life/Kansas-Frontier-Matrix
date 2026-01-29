# 🗺️ Historical Mapping Templates (External) — `data/external/mappings/historical/templates/`

![Status](https://img.shields.io/badge/status-active_template_set-2ea44f)
![Domain](https://img.shields.io/badge/domain-historical-6f42c1)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-1f6feb)
![Outputs](https://img.shields.io/badge/outputs-COG%20%7C%20GeoJSON%20%7C%20Tiles%20%7C%20KMZ-8a2be2)
![Tools](https://img.shields.io/badge/tooling-QGIS%20%7C%20GDAL%20%7C%20Python%20%7C%20PostGIS-f59e0b)

> 🎯 **Purpose:** This folder holds **copy/paste templates** and **fill-in-the-blank stubs** for documenting + onboarding **external historical geospatial datasets** into **KFM** (Kansas Frontier Matrix) via the required, provenance-first pipeline.  
> 🧾 Everything here is designed to keep us aligned with **Raw → Processed → Catalog/Prov → Database → API → UI** (no shortcuts). :contentReference[oaicite:0]{index=0}

---

## 🔎 Quick Links (Project References)

- 🧠 **KFM Technical Blueprint** (pipeline order, governance, QA gates, UI expectations) :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}  
- 🧩 **KFM Historical Mapping Hub Design** (STAC-like schema + open-source workflow ideas) :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}  
- 🧭 **Repo / Data Structure Guide** (where things go + naming conventions) :contentReference[oaicite:5]{index=5}  
- 🎨 **Map Design + Metadata + Projections primer** (cartographic + metadata reminders) :contentReference[oaicite:6]{index=6}  
- 🪖 **Map Reading + Land Navigation** (grid systems, datum pitfalls, UTM/MGRS concepts) :contentReference[oaicite:7]{index=7}  
- ⏱️ **Time-Oriented Visualization** (interaction patterns for time sliders + temporal UX) :contentReference[oaicite:8]{index=8}  
- 🧱 **3D GIS (optional)** (ideas for 2.5D/3D layers & web 3D) :contentReference[oaicite:9]{index=9}  
- 🛰️ **Google Earth Engine (optional)** (time-series remote sensing & composites) :contentReference[oaicite:10]{index=10}  

---

## 🧰 What this folder is for

This directory provides **standard template files** you can copy into a new dataset mapping folder under:

```text
data/external/mappings/historical/<dataset_slug>/
```

These templates help you produce:

- ✅ A **human-readable mapping doc** (what it is, where it came from, how it was processed)
- ✅ **STAC** metadata (collection/item) for findability & machine indexing :contentReference[oaicite:11]{index=11}  
- ✅ **DCAT** metadata (catalog-ready record) :contentReference[oaicite:12]{index=12}  
- ✅ **W3C PROV** lineage record (the “map behind the map”) :contentReference[oaicite:13]{index=13}  
- ✅ A **QA checklist** to keep historical layers trustworthy (esp. scans + georeferencing)

> 🧷 Why this matters: KFM is explicitly designed so that **every layer is traceable to original sources** and merges only when metadata + provenance exist. :contentReference[oaicite:14]{index=14}

---

## 🧭 Where this fits in the KFM pipeline

```text
📥 Raw (read-only) 
   ↓
🧪 Processed (normalized, georeferenced, validated)
   ↓
🗂️ Catalog + Provenance (STAC/DCAT/PROV)
   ↓
🗄️ Database (PostGIS / graph)
   ↓
🔌 API (FastAPI)
   ↓
🖥️ UI (time slider, compare then-vs-now, 2D/3D)
```

**Non-negotiable:** do *not* “inject data into the UI” or skip metadata creation. That breaks the KFM contract. :contentReference[oaicite:15]{index=15}

---

## 🗂️ Recommended folder layout for a historical dataset mapping

> Copy templates from **this** folder into a new dataset folder.

```text
📁 data/
└─ 📁 external/
   └─ 📁 mappings/
      └─ 🏛️ historical/                              📜 historical mapping packs + publishing plans
         ├─ 📁 templates/                             👈 you are here (reusable stubs + checklists)
         └─ 📁 <dataset_slug>/                        🏷️ one dataset mapping bundle
            ├─ 📄 README.md                            📘 dataset mapping doc (human-readable runbook)
            ├─ 📄 stac.collection.json                 🛰️ STAC Collection (or 📄 stac.item.json for single layer)
            ├─ 📁 stac.items/                          ◻️ optional: STAC Items directory (multi-part datasets)
            ├─ 📄 dcat.dataset.jsonld                  🗂️ DCAT catalog record (JSON-LD discovery)
            ├─ 📄 prov.json                            🧬 PROV lineage record (inputs → activities → outputs)
            ├─ 📄 qa.checklist.md                      ✅ validation notes + acceptance bar
            └─ 📁 georef/                              ◻️ optional: georeferencing evidence bundle
               ├─ 📄 gcps.csv                          📍 control points (GCPs)
               ├─ 📝 georef.notes.md                    📝 transformation notes + CRS + residual summary
               └─ 🖼️ residuals.png                     📉 screenshots/evidence (residuals + overlay checks)
```

> ⚠️ The **actual data files** usually live under the appropriate `data/<domain>/{raw,work,processed}` convention (see repo guide). `mappings/` is the “paper trail” that connects the dataset to its final canonical outputs. :contentReference[oaicite:16]{index=16}

---

## 🧱 Template Index (what should exist in this folder)

> If any of these are missing today, create them using the stubs below.

### 📄 Documentation templates
- `TEMPLATE__HISTORICAL_DATASET_MAPPING.md`
- `TEMPLATE__GEOREFERENCE_NOTES.md`
- `TEMPLATE__QA_CHECKLIST.md`

### 🛰️ Metadata templates
- `TEMPLATE__STAC_COLLECTION.json`
- `TEMPLATE__STAC_ITEM.json`
- `TEMPLATE__DCAT_DATASET.jsonld`

### 🧾 Provenance templates
- `TEMPLATE__PROV.json`

### 🎨 Optional cartography templates
- `TEMPLATE__QGIS_STYLE.qml`
- `TEMPLATE__QGIS_LAYOUT.qpt`
- `TEMPLATE__QGIS_PROJECT.qgz` (usually too binary for README-only tracking; prefer notes + exports)

---

## 🚀 Quick Start (copy workflow)

1) **Create a dataset folder**  
   `data/external/mappings/historical/<dataset_slug>/`

2) **Copy the templates** you need from this directory.

3) Fill in **STAC/DCAT/PROV** + mapping doc.

4) Ensure your corresponding data went through:  
   **Raw → Processed → Catalog/Prov → Database → API → UI**. :contentReference[oaicite:17]{index=17}

5) Run validation (CI will likely check that processed outputs have matching metadata + provenance). :contentReference[oaicite:18]{index=18}

---

## 🧾 Template Stubs (copy/paste)

### 1) `TEMPLATE__HISTORICAL_DATASET_MAPPING.md`

```markdown
# <Dataset Title> — Mapping Doc 📘

## Overview 🧭
- **dataset_slug:** <provider__topic__region__timerange__v1>
- **Type:** (scan raster | vector | table | gazetteer | hybrid)
- **Theme:** (topography | land ownership | hydrology | settlements | environment | etc.)
- **Coverage:** (Kansas statewide | county | corridor | site)
- **Temporal coverage:** <start_year>–<end_year> (include uncertainty if needed)

## Source & Rights 🏛️
- **Source org:** <USGS / state archive / university / etc.>
- **Source link:** <URL or citation>
- **License:** <SPDX-ish label if possible; otherwise plain language>
- **Copyright / usage notes:** <not legal advice; what we believe is permitted>

## Raw Inputs 📥
- `data/.../raw/...`
- Formats: <TIFF / JPG / SHP / CSV / PDF>

## Processing Summary 🧪
- Tools used: <QGIS / GDAL / Python scripts>
- Key steps:
  1. <clean>
  2. <georeference>
  3. <warp/reproject>
  4. <tile/export>
- Output formats:
  - Raster: COG GeoTIFF
  - Vector: GeoJSON (and/or geopackage)
  - Optional: tiles / KMZ

## Spatial Reference 🗺️
- **Input CRS:** <EPSG or description>
- **Output CRS:** <EPSG:4326, EPSG:3857, etc.>
- **Datum:** <NAD83 / WGS84 / unknown>
- **Notes on accuracy:** <RMS, residuals, known limitations>

## Metadata Outputs 🛰️
- STAC: `stac.collection.json` / `stac.items/*.json`
- DCAT: `dcat.dataset.jsonld`
- PROV: `prov.json`

## QA & Review ✅
- Visual inspection done by: <name/handle>
- QA notes: <bullets>
- Known issues / TODOs: <bullets>

## Citation 📚
Provide recommended citation text for downstream users.
```

---

### 2) `TEMPLATE__STAC_ITEM.json` (historical layer)

> KFM uses STAC-style metadata as a first-class contract (single layer = item; multi-part = collection + items). :contentReference[oaicite:19]{index=19}

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "<dataset_slug>__<layer_slug>__v1",
  "properties": {
    "title": "<Human title>",
    "description": "<What it is, why it matters, and how it was derived.>",
    "datetime": null,
    "start_datetime": "<YYYY-MM-DDT00:00:00Z>",
    "end_datetime": "<YYYY-MM-DDT23:59:59Z>",
    "license": "<license-id-or-text>",
    "proj:epsg": 4326,

    "kfm:theme": "<topography|cadastral|hydrology|settlements|environment>",
    "kfm:source_org": "<org>",
    "kfm:source_citation": "<citation text>",
    "kfm:source_url": "<url>",
    "kfm:processing_summary": "<one-paragraph summary>",
    "kfm:accuracy_notes": "<RMS, residual notes, known distortions>"
  },
  "geometry": null,
  "bbox": null,
  "links": [
    { "rel": "about", "href": "./README.md", "type": "text/markdown", "title": "Mapping doc" },
    { "rel": "derived_from", "href": "./prov.json", "type": "application/json", "title": "Provenance (PROV)" }
  ],
  "assets": {
    "cog": {
      "href": "<relative/or/absolute/path/to/output.cog.tif>",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "title": "Cloud-Optimized GeoTIFF"
    },
    "geojson": {
      "href": "<path/to/output.geojson>",
      "type": "application/geo+json",
      "roles": ["data"],
      "title": "Vector output (if applicable)"
    },
    "source_scan": {
      "href": "<path/to/raw/source_scan.tif>",
      "type": "image/tiff",
      "roles": ["source"],
      "title": "Original scan (raw input)"
    }
  }
}
```

---

### 3) `TEMPLATE__PROV.json` (lineage / “map behind the map”)

> PROV should capture: raw inputs, script/tool versions, run time, outputs produced. :contentReference[oaicite:20]{index=20}

```json
{
  "prov:document": {
    "prov:entity": {
      "raw:source_1": {
        "prov:label": "Raw source file",
        "prov:type": "file",
        "kfm:path": "data/.../raw/<source>",
        "kfm:source_url": "<url>",
        "kfm:license": "<license>"
      },
      "out:processed_1": {
        "prov:label": "Processed output",
        "prov:type": "file",
        "kfm:path": "data/.../processed/<output>",
        "kfm:format": "COG|GeoJSON|Tiles|KMZ"
      }
    },
    "prov:activity": {
      "act:process_run": {
        "prov:label": "Historical dataset processing run",
        "prov:startTime": "<ISO-8601>",
        "prov:endTime": "<ISO-8601>",
        "kfm:tooling": ["QGIS", "GDAL", "Python"],
        "kfm:script": "src/pipelines/<script>.py",
        "kfm:script_git_commit": "<commit-sha>"
      }
    },
    "prov:wasGeneratedBy": {
      "wgb:1": {
        "prov:entity": "out:processed_1",
        "prov:activity": "act:process_run"
      }
    },
    "prov:used": {
      "used:1": {
        "prov:activity": "act:process_run",
        "prov:entity": "raw:source_1"
      }
    }
  }
}
```

---

### 4) `TEMPLATE__GEOREFERENCE_NOTES.md` (for scanned historical maps)

> The KFM mapping hub design expects scanned maps to be georeferenced and exported into open formats (COG/tiles/KMZ) using open-source tooling where possible. :contentReference[oaicite:21]{index=21}

```markdown
# Georeferencing Notes 🧷

## Inputs 📥
- Source scan: <path>
- Source map info:
  - Survey date:
  - Publication date:
  - Revision date:
  - Publisher:

## Control Points 📍
- GCP file: `georef/gcps.csv`
- Point selection strategy:
  - Prefer stable features (road intersections, river confluences, courthouse squares, section corners, etc.)
  - Avoid features likely to move over time (stream meanders, temporary structures)

## Transformation 🧠
- Method: <affine | polynomial | thin plate spline>
- Target CRS: <EPSG>
- Resampling: <nearest | bilinear | cubic>

## Error / Residuals 📉
- RMS error: <value + unit>
- Notes: <where distortion appears + why>

## Outputs 🧪
- Georeferenced raster: <COG path>
- Optional tiles/KMZ: <paths>
```

**GCP CSV header suggestion:**

```csv
id,source_x,source_y,map_x,map_y,notes
```

---

### 5) `TEMPLATE__QA_CHECKLIST.md`

> CI + maintainer review often focuses on metadata completeness, license clarity, and coordinate sanity checks. :contentReference[oaicite:22]{index=22}

```markdown
# QA Checklist ✅ (Historical Layer)

## Source Integrity 🏛️
- [ ] Source organization identified
- [ ] Source citation included
- [ ] License / usage permission documented (fail closed if missing) :contentReference[oaicite:23]{index=23}
- [ ] Dates captured (survey/publication/revision where available)

## Spatial Reference 🗺️
- [ ] Input CRS + datum recorded (and any ambiguity noted)
- [ ] Output CRS recorded (EPSG)
- [ ] Datum shift / transformation documented if applicable
- [ ] Bounding box sanity check (in correct hemisphere, expected region)

## Georeferencing (if scan) 🧷
- [ ] GCP count recorded
- [ ] RMS error recorded
- [ ] Residuals / screenshot evidence attached
- [ ] Known distortions described (paper stretch, scanning warp, cartographic generalization)

## Temporal Coverage ⏱️
- [ ] start/end date set (or year range)
- [ ] Uncertainty explained (if “circa”)
- [ ] Time is encoded for UI time slider compatibility (start_datetime/end_datetime)

## Outputs 🧪
- [ ] Processed outputs exist (COG/GeoJSON/etc.)
- [ ] STAC item/collection created
- [ ] DCAT record created
- [ ] PROV created and references script/tool versions

## Human Review 🧑‍🔬
- [ ] Visual check completed (symbology readable, alignment plausible)
- [ ] Known limitations documented (scale, cartographic bias, missing areas)
```

---

## 🗺️ Spatial Reference Notes (historical layers)

Historical datasets often carry **projection + datum quirks**. At minimum:

- Record **projection** (or EPSG), **datum**, and **units**.
- If you transform CRS, record:
  - the transformation method (if known)
  - tools used (GDAL/QGIS/Python)
  - expected positional uncertainty

> 🧠 Reminder: datum mismatches can produce large offsets (hundreds of meters). Document it; don’t hide it. :contentReference[oaicite:24]{index=24}

Common targets:
- 🌐 **EPSG:4326** for canonical storage / interoperability
- 🧭 **EPSG:3857** for web tiles
- 🧱 **UTM** for local analysis & grid overlays (especially when UI supports UTM/MGRS toggle ideas) :contentReference[oaicite:25]{index=25}

---

## ⏳ Temporal Modeling Tips (historical ≠ single date)

KFM’s UI roadmap explicitly includes **historical vs current comparisons** and time navigation. :contentReference[oaicite:26]{index=26}  
To support this:

- Prefer `start_datetime` + `end_datetime` over a single `datetime` when:
  - the map spans multiple years (e.g., survey vs publish)
  - the dataset is an aggregation (e.g., “1850–1890 land cover”)
- Include an uncertainty note if dates are approximate.

For deeper temporal UX patterns (brushing, linking, time sliders), see: :contentReference[oaicite:27]{index=27}

---

## 🎨 Mini Style Guide (so maps don’t look chaotic)

When you publish a historical layer, treat it like a **storytelling artifact**:

- Establish **visual hierarchy** (what should the user see first?)
- Avoid over-encoding (especially in “then vs now” compare views)
- Keep legends tight; annotate odd symbology from the original
- Always include metadata + sources (facts are free; representations may not be) :contentReference[oaicite:28]{index=28}

---

## 🧭 UI-Driven expectations (why templates ask for certain fields)

KFM’s blueprint anticipates classic navigation aids in the UI:

- 🧭 North arrow + scale bar
- 🧱 Optional grid overlay (lat/long or UTM)
- 📍 Coordinate display in multiple formats (lat/long + UTM/MGRS) :contentReference[oaicite:29]{index=29}

That’s why these templates explicitly capture:
- CRS/datum (so coordinate readouts aren’t misleading)
- time range (so the slider/comparison works)
- provenance (so the user can inspect “why this looks this way”)

---

## 🧠 Optional: 3D + “terrain-aware” historical layers

If a historical layer should support 2.5D/3D exploration (e.g., fortifications, earthworks, terrain interpretation):

- capture **elevation/DEM dependencies** in PROV
- record any mesh/orthophoto georeferencing steps
- keep reproducible validation routines (compare against physical evidence when possible) :contentReference[oaicite:30]{index=30}

---

## ✅ Definition of Done (DoD) for a new historical mapping entry

A historical dataset mapping folder is “done” when:

- [ ] `README.md` mapping doc exists and is filled in
- [ ] STAC + DCAT + PROV files exist (and cross-link each other) :contentReference[oaicite:31]{index=31}
- [ ] QA checklist completed
- [ ] License is explicit (no license = no merge) :contentReference[oaicite:32]{index=32}
- [ ] Outputs are in canonical processed formats (COG/GeoJSON/etc.)
- [ ] A reviewer can reproduce the processing at a high level from your notes

---

## 🧷 Suggested dataset slug convention

Keep it predictable:

```text
<provider>__<theme>__<region>__<temporal>__v<major>
```

Examples:
- `usgs__topo__kansas__1890__v1`
- `county_records__land_ownership__douglas_co__1872_1885__v1`
- `railroads_archive__infrastructure__kansas__1865_1910__v2`

---

## 📎 Want to improve these templates?

Open a PR that:
- adds a missing stub file, or
- tightens the required fields, or
- aligns structure with `docs/standards/*_PROFILE.md` expectations (STAC/DCAT/PROV). :contentReference[oaicite:33]{index=33}

💡 If you add a new template, update this README’s **Template Index** so it stays searchable.

