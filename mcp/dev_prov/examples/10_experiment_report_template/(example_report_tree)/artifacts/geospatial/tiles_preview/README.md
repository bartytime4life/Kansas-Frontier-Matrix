# 🗺️ `tiles_preview/` — Geospatial Tiles Quicklook

![artifact](https://img.shields.io/badge/artifact-geospatial_tiles-2ea44f)
![purpose](https://img.shields.io/badge/purpose-human_quicklook-blue)
![formats](https://img.shields.io/badge/formats-MVT%20%7C%20PMTiles%20%7C%20COG-lightgrey)
![provenance](https://img.shields.io/badge/provenance-STAC%2FDCAT%2FPROV-important)
![governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-orange)
![viewer](https://img.shields.io/badge/viewer-MapLibre%20%2B%20Cesium-9cf)

> [!NOTE]
> This folder is **preview-grade** (human quicklook + QA + experiment report storytelling).  
> The **canonical** data lives in the geospatial artifacts + catalogs (**STAC/DCAT/PROV**) and is served via the API tile endpoints. ✅

---

## 🔎 Why this exists

KFM is built around “**the map behind the map**”: every visualization should have inspectable *source, license, and preparation summary*. `tiles_preview/` is where experiment reports stash **fast, glanceable previews** of tile outputs so reviewers can validate a run without spinning up the full stack.

Typical uses:

- ✅ “Does this tileset render correctly at expected zooms?”
- ✅ “Are bounds/time ranges correct?”
- ✅ “Do styles/legends match the semantics?”
- ✅ “Is licensing/sensitivity respected in what we’re showing?”
- ✅ “Can this preview be embedded in a report, story, or Pulse Thread?”

---

## 🧭 Contents at a glance

```text
📁 tiles_preview/
├─ 📄 README.md                 👈 you are here
├─ 🌐 index.html                # optional: interactive preview viewer (MapLibre)
├─ 🎨 style.json                # optional: MapLibre style (or layer style)
├─ 🧾 tilejson.json             # optional: TileJSON for MVT/XYZ sources
├─ 🧷 metadata.json             # ✅ recommended: preview manifest (machine + human)
├─ 🖼️ preview.png               # ✅ recommended: static screenshot quicklook
├─ 🗺️ legend.png                # optional: legend graphic
├─ 🧬 prov.jsonld               # optional: PROV snippet for this tileset/preview build
├─ 📝 notes.md                  # optional: analyst notes, QA notes, caveats
└─ 📁 thumbnails/               # optional: multiple screenshots (e.g., per zoom/time)
```

> [!TIP]
> Even if you skip `index.html`, **always** include at least `preview.png` + `metadata.json`.  
> Those two files are the “minimum viable quicklook” for reports and audits.

---

## 🚀 Quick start: view the interactive preview (if present)

### 1) Start a local static server (recommended)
From this folder:

```bash
python -m http.server 8000
```

Then open:

- `http://localhost:8000/index.html`

### 2) Why not just double-click `index.html`?
Many browsers block tile/font fetches in `file://` mode (CORS + relative asset paths). A local server avoids the usual blank-map surprise. 🧯

---

## 🧩 How this fits the KFM stack (and why previews are **not** canonical)

KFM’s guiding separation:

- **PostGIS stores geo truth** (vectors/rasters)
- **Catalogs describe the assets** (STAC/DCAT)
- **Graph links the context** (knowledge + provenance)

This folder sits *alongside* the canonical pipeline as a **review surface**, not as the data-of-record.

```mermaid
flowchart LR
  raw[📥 raw inputs\n(immutable evidence)] --> work[🧪 work/transform]
  work --> processed[📦 processed assets\n(GeoParquet/COG/etc)]
  processed --> catalogs[📚 catalogs\nSTAC + DCAT + PROV]
  processed --> tiles[🧱 tilesets\n(MVT/PMTiles/XYZ/MBTiles)]
  tiles --> preview[🗺️ tiles_preview/\n(this folder)]
  catalogs --> api[🔌 API\n/tiles/* endpoints]
  api --> ui[🖥️ UI\nMapLibre/Cesium]
  preview --> report[🧾 Experiment Report\n+ QA + storytelling]
```

---

## 🧱 Common generation patterns (choose what fits the dataset)

### A) Dynamic tiles served from PostGIS (MVT)
Best for: frequently-updated layers, interactive filtering, server-side generalization.

- UI calls an API endpoint like:  
  `GET /tiles/<layer>/{z}/{x}/{y}.pbf`
- API executes a parameterized SQL template using **`ST_AsMVT`** (Mapbox Vector Tiles).

**Preview implication:** `index.html` can point at the dev/staging endpoint and render live tiles for QA.

---

### B) Static vector tiles packaged as **PMTiles**
Best for: heavy layers, offline packs, CDN/static hosting, report bundles.

A strong KFM pattern is generating **two artifacts from the same source**:

- **GeoParquet** (analysis-friendly)
- **PMTiles** (visualization-friendly, pregenerated pyramid)

**Preview implication:** `index.html` can load a local `*.pmtiles` (or a hosted one) and render it client-side fast.

---

### C) Raster imagery served as **COG** (+ optional pre-tiling)
Best for: large rasters (land cover, NDVI composites, aerial imagery).

- **COGs** allow partial reads (range requests), so the UI/API can fetch only what’s needed.
- For very heavy rasters or “base layer” use, you may also pre-generate XYZ tiles / MBTiles for speed.

**Preview implication:** include `preview.png` that demonstrates expected raster rendering + legend/color ramp.

---

## 🧾 `metadata.json` — the preview manifest contract (recommended)

This is where the “evidence-first” habit becomes tangible for previews.  
Treat it like a tiny STAC-like quicklook summary.

### ✅ Suggested minimal schema
```json
{
  "layer_id": "landcover",
  "title": "Landcover (example)",
  "kind": "vector_tiles",
  "primary_format": "pmtiles",
  "crs": "EPSG:4326",
  "bounds_wgs84": [-102.05, 36.99, -94.59, 40.00],
  "minzoom": 0,
  "maxzoom": 14,
  "time": { "enabled": false },

  "license": "CC-BY-4.0",
  "sensitivity": "public",

  "hashes": {
    "pmtiles": "sha256:<digest>",
    "geoparquet": "sha256:<digest>"
  },

  "catalog_refs": {
    "stac_collection": "../catalog/stac/collections/<id>.json",
    "stac_item": "../catalog/stac/items/<id>.json",
    "dcat_dataset": "../catalog/dcat/<id>.json",
    "prov_bundle": "../provenance/<run_id>.prov.jsonld"
  },

  "generated_by": {
    "pipeline": "<pipeline_name>",
    "run_id": "<run_id>",
    "code_version": "<git_sha>",
    "generated_at": "2026-01-22T00:00:00Z"
  },

  "qa": {
    "known_caveats": ["<optional>"],
    "reviewed_by": ["<optional>"]
  }
}
```

> [!IMPORTANT]
> Your preview manifest should always include **license + sensitivity** so it’s obvious whether the preview can be shared publicly. 🔐

---

## ⏱ Time-enabled layers (timeline / 4D previews)

If the layer changes over time (historical boundaries, drought progression, railroad expansion, etc.), make time **first-class** in the preview:

Recommended additions:

- `epochs.json` (list of available years/periods)
- `thumbnails/` with `preview_YYYY.png`
- A UI affordance in `index.html` (timeline slider / drop-down)
- Document the URL contract if time is passed as query params (example):
  - `index.html?t=1935`
  - `index.html?start=1935-01-01&end=1936-01-01`

> [!TIP]
> Time previews are best when your screenshot set shows the same viewport across multiple epochs (easy visual diff).

---

## 🔐 Governance, licensing, and sensitivity

KFM governance isn’t “optional later” — it’s designed to be enforced in the workflow (including previews).

Guidelines for this folder:

- ✅ If a dataset is **restricted/sensitive**, don’t place raw/high-res previews here unless the report repo is appropriately access-controlled.
- ✅ Prefer **generalized / aggregated / redacted** previews for public artifacts.
- ✅ Ensure metadata includes:
  - `license` (or “unknown” + remediation note)
  - `sensitivity` (`public | restricted | internal`, etc.)
- ✅ If policy-as-code is enabled (OPA/Conftest style), `metadata.json` should be structured so CI can gate on it.

CARE principles also matter for community/heritage data: previews should support **collective benefit**, **authority to control**, and **responsibility & ethics** (especially when working with culturally sensitive locations). 🌾🪶

---

## 🤖 AI + explainability hooks (why preview metadata matters)

KFM’s AI layer is intended to be **source-grounded and citation-forward**, with explainability surfaced in the UI. Tile previews become dramatically more useful when they carry the “receipts”:

- ✅ `metadata.json` links to STAC/DCAT/PROV
- ✅ `notes.md` captures how to interpret the layer
- ✅ `legend.png` prevents misleading visualization

This makes it possible for an assistant (or a report generator) to say:  
“Here’s the map result, here’s the provenance, here’s the license, here’s the processing summary.” 🔎

---

## 📣 Pulse Threads & narrative overlays (optional but powerful)

If your experiment produces a narrative artifact (e.g., a Pulse Thread tied to a region/time), consider adding:

- `pulse_overlay.geojson` (points/polygons for the narrative anchors)
- `pulse_excerpt.md` (short narrative + citations)
- A toggle in `index.html` to overlay these markers

This keeps emergent stories *geotagged, versioned, and evidence-backed* — ideal for report-style deliverables.

---

## ✅ Author checklist (copy into PR / report)

- [ ] `preview.png` renders the expected area and symbology
- [ ] `metadata.json` includes **license + sensitivity**
- [ ] Bounds + zoom ranges look correct
- [ ] If time-enabled: includes epochs + at least 2 time-slice previews
- [ ] Preview references canonical STAC/DCAT/PROV (no “mystery layers”)
- [ ] Any caveats are written in `notes.md`
- [ ] No restricted content accidentally placed in a public report

---

## 🧯 Troubleshooting

**Blank map in `index.html`**
- Start a local server (`python -m http.server`) instead of `file://`
- Verify `tilejson.json` URLs and that `{z}/{x}/{y}` paths match your tile server
- Confirm `style.json` sources/layers match the tileset layer names

**Tiles load but styling looks wrong**
- MVT layer names often differ from dataset IDs—update `style.json` accordingly
- Provide a `legend.png` (or embed legend HTML)

**Repo is getting huge**
- Don’t commit full tilesets into reports unless intended.
- Prefer:
  - hosted PMTiles (static)
  - or OCI-distributed artifacts referenced by digest
  - plus local `preview.png` + `metadata.json`

---

## 🔗 Related (typical) sibling artifacts in the report tree

Depending on how your experiment report tree is laid out, these folders often exist nearby:

- `../tiles/` — canonical tile artifacts (PMTiles/MBTiles/XYZ folders)
- `../catalog/` — STAC/DCAT entries
- `../../provenance/` — PROV bundles / run manifests
- `../samples/` — tiny GeoJSON/CSV samples for sanity checks

---

## 📚 Project docs & references (recommended reading)

- 📥 **Data Intake & pipeline patterns** (validation gates, PostGIS tile serving, checksums)
- 🧱 **Architecture & UI transparency** (Layer Info, Layer Provenance, offline pack concepts)
- 🧬 **STAC/DCAT/PROV alignment** (catalog + provenance-first publishing)
- 🗺️ **Mapping hub design** (MapLibre static hosting + timeline concepts)
- 🤖 **AI system overview** (citation discipline + explainability surfaces)
- 🧪 **Experiment/report discipline** (reproducible research + structured artifacts)
- 🧰 **Geospatial analysis cookbook** (visualization + tile-serving techniques)

> [!NOTE]
> Keep previews “small and honest”: they should help humans verify outcomes, not become a second shadow source of truth.
