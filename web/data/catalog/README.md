# 🗃️ KFM Web Data Catalog (`web/data/catalog/`)

> Frontend-consumable **dataset catalog snapshot** for the Kansas Frontier Matrix (KFM) Map UI  
> ✅ **Contract-first** · 🧾 **Provenance-first** · 🧪 **Schema-validated** · 🗺️ **Map-ready**

This directory exists to make the web app fast, predictable, and “trustable-by-default”:
- ⚡ **Fast UI boot** (search, filters, layer browser)
- 🧭 **Consistent dataset detail panels** (extent, time range, license, attribution)
- 🔎 **Provenance UX** (“show me the sources”, “how was this derived?”)
- 📴 **Offline/demo mode** (optional: vendored metadata + previews)

**Important:** this is a *read-optimized* folder for the UI — not the canonical place where datasets are “published.”

---

## 🧠 Table of Contents

- [🎯 Purpose](#-purpose)
- [🧱 Non‑negotiables](#-nonnegotiables)
- [📦 What belongs here](#-what-belongs-here)
- [📁 Suggested layout](#-suggested-layout)
- [🧾 The catalog contract](#-the-catalog-contract)
  - [🛰️ STAC](#️-stac)
  - [📚 DCAT](#-dcat)
  - [🧬 PROV](#-prov)
  - [🧩 UI Manifest](#-ui-manifest)
- [➕ Adding or updating a dataset](#-adding-or-updating-a-dataset)
- [✅ Validation & CI gates](#-validation--ci-gates)
- [⚡ Performance budgets](#-performance-budgets)
- [🔐 Security, ethics, and sovereignty](#-security-ethics-and-sovereignty)
- [🧰 Troubleshooting](#-troubleshooting)
- [📚 Project reference shelf](#-project-reference-shelf)

---

## 🎯 Purpose

`web/data/catalog/` is the **frontend-facing index** the UI uses to render a coherent catalog experience without:
- re-parsing heavyweight metadata repeatedly,
- guessing missing context,
- or “hallucinating” layer details.

Think of it as a **cache + contract boundary**: the UI consumes **validated artifacts** (or pointers to them) and remains decoupled from how data is stored or processed upstream.

---

## 🧱 Non‑negotiables

KFM’s pipeline is intentionally strict. The catalog is how we enforce trust and traceability:

- 🔁 **Pipeline ordering is absolute**  
  ETL → **STAC/DCAT/PROV** → Graph → API → UI → Story Nodes → Focus Mode

- 🚧 **API boundary rule**  
  The UI should never talk to the graph directly — it consumes API responses or prebuilt catalog snapshots.

- 🧾 **Provenance-first publishing**  
  If it appears in the UI, it must have catalog records and lineage *before* it’s shown.

- ♻️ **Deterministic, idempotent ETL**  
  Same input + same config ⇒ same outputs. Re-runs shouldn’t create “mystery drift.”

---

## 📦 What belongs here

✅ Typical contents:
- 🗂️ `index.json` (or `catalog.json`) — a compact list used for **search + layer browser**
- 🧾 `datasets/<dataset-id>.json` — **UI manifests** (render hints, preview links, human text)
- 🛰️ `stac/…` — optional vendored STAC (Collections/Items) for offline mode
- 📚 `dcat/…` — optional vendored DCAT JSON‑LD entries
- 🧬 `prov/…` — optional vendored lineage bundles (or API links to them)
- 🖼️ `previews/…` — thumbnails, legend images, small “sparkline” summaries
- 🧩 `schemas/` (optional) — schema snapshots used by the web build

🚫 What does **not** belong here:
- 📥 raw inputs (that’s `data/raw/...`)
- 🗄️ processed heavy assets (COGs, GeoParquet, MBTiles, 3D tiles) unless they’re tiny demo fixtures
- 🔑 secrets, tokens, credentials, private endpoints
- 🧍 PII or sensitive locations unless redacted/generalized upstream

---

## 📁 Suggested layout

> The exact filenames can vary — but the *roles* should remain consistent.

```text
web/
└── 📁 data/
    └── 📁 catalog/
        ├── 📄 README.md
        ├── 📄 index.json                  # UI boot index (fast + small)
        ├── 📁 datasets/                   # per-dataset UI manifests
        │   ├── 📄 <dataset-id>.json
        │   └── 📄 ...
        ├── 📁 stac/                       # optional: vendored STAC
        │   ├── 📁 collections/
        │   └── 📁 items/
        ├── 📁 dcat/                       # optional: vendored DCAT JSON-LD
        ├── 📁 prov/                       # optional: vendored PROV bundles
        └── 📁 previews/                   # thumbnails, legends, mini-assets
```

---

## 🧾 The catalog contract

KFM uses three complementary “boundary artifacts” for dataset publication:

### 🛰️ STAC

**Best for:** geospatial assets (rasters, vectors, point clouds), spatial/temporal extents, assets & links.  
**UI needs from STAC:** bounding box, time range, asset URLs, CRS, and an ID that’s stable.

Recommended use in UI:
- show extent and time window quickly,
- choose render strategy (COG, vector tile, GeoJSON, 3D),
- surface attribution/licensing consistently.

### 📚 DCAT

**Best for:** dataset discovery, distributions, licensing/rights, organizational ownership, and catalog harvesting.  
**UI needs from DCAT:** title/description, license, publisher/maintainer, distributions (what formats exist, where they live).

Use DCAT when a dataset is:
- non-spatial (tabular, text corpora, OCR output),
- multi-distribution (GeoParquet + API + vector tiles),
- meant to be discoverable beyond the KFM UI.

### 🧬 PROV

**Best for:** lineage and trust. “What inputs + what process + what agent produced this output?”  
**UI needs from PROV:** a clean human-facing summary + a machine-readable bundle for audits.

Use PROV for:
- derived layers (interpolations, composites, indices),
- AI/ML outputs (classification maps, OCR corpora),
- any transformation chain you may need to defend or debug later.

---

### 🧩 UI Manifest

The UI should consume a **small, stable manifest** that:
- keeps the layer browser fast,
- includes render hints (but not hardcoded styling everywhere),
- *points* to canonical STAC/DCAT/PROV instead of duplicating full metadata.

#### Minimal fields (recommended)

```json
{
  "id": "usgs_historic_topo_1894",
  "title": "USGS Historical Topographic Map (Ellsworth County, 1894)",
  "domain": "historical",
  "description": "Digitized 1894 USGS topographic survey of Ellsworth County, Kansas.",
  "license": "Public Domain",

  "spatial": { "bbox": [-99.5, 38.3, -98.8, 38.9], "crs": "EPSG:4326" },
  "temporal": { "start": "1894-01-01", "end": "1894-12-31" },

  "refs": {
    "stac": { "collection": "historical_topos", "item": "usgs_historic_topo_1894" },
    "dcat": "data/catalog/dcat/usgs_historic_topo_1894.jsonld",
    "prov": "data/prov/usgs_historic_topo_1894.prov.jsonld"
  },

  "assets": {
    "primary": "data/processed/historical/topos/usgs_1894_ellsworth.cog.tif",
    "thumbnail": "previews/usgs_historic_topo_1894.webp",
    "legend": "previews/usgs_historic_topo_legend.svg"
  },

  "ui": {
    "layerType": "raster",
    "renderHint": "cog",
    "defaultVisible": false,
    "defaultOpacity": 0.75,
    "tags": ["topo", "historical", "usgs"]
  },

  "faircare": {
    "collective_benefit": "Preserves environmental and cartographic heritage of Kansas.",
    "authority_to_control": "Open",
    "responsibility": "Data Engineering & FAIR+CARE Council",
    "ethics": "Culturally neutral archival content"
  }
}
```

> ✅ Keep UI manifests compact. If it grows past “a couple KB per dataset,” you’re probably duplicating STAC/DCAT/PROV.

---

## ➕ Adding or updating a dataset

> The “right” workflow is upstream-first: **publish catalogs → export web snapshot**.

### 1) Stage the data (upstream)
- 📥 Put source manifests in `data/sources/` (preferred for external datasets)
- 📥 Place downloaded raw inputs under `data/raw/<domain>/`
- 🧪 Work intermediates in `data/work/<domain>/`
- 🗄️ Publish final outputs to `data/processed/<domain>/`

### 2) Publish the boundary artifacts (required)
For every dataset you intend to show:
- 🛰️ STAC Collection + Item(s)
- 📚 DCAT Dataset entry (JSON‑LD)
- 🧬 PROV lineage bundle

### 3) Export the web snapshot (this folder)
- Generate/update:
  - `web/data/catalog/index.json`
  - `web/data/catalog/datasets/<dataset-id>.json`
  - optional vendored `stac/`, `dcat/`, `prov/`, `previews/`

### 4) PR checklist ✅
- [ ] Dataset has a **stable ID** (don’t encode version numbers in the ID)
- [ ] License is explicit + attribution is present
- [ ] Spatial bbox + temporal range present (if applicable)
- [ ] STAC/DCAT/PROV references resolve (no broken paths)
- [ ] Preview thumbnail exists (or a good reason why it can’t)
- [ ] Any AI/analysis output has provenance + (if relevant) uncertainty notes
- [ ] No secrets, no PII, no sensitive coordinates without governance tags

---

## ✅ Validation & CI gates

Catalog stability comes from automation. Expect CI to enforce:
- 🧾 Markdown/doc hygiene (front-matter, required sections for governed docs)
- 🔗 Link/reference validation (no broken internal references)
- 🧪 JSON Schema validation (STAC/DCAT/PROV + UI manifests)
- 🧠 Graph integrity tests (if graph fixtures are involved)
- 🧷 API contract tests (responses match the contracts)
- 🔐 Security & governance scans (secrets, PII, sensitive location checks, classification regressions)

If CI fails, fix the **source artifact** (usually upstream catalogs), then re-export the snapshot.

---

## ⚡ Performance budgets

The catalog is one of the first things the UI loads. Keep it lean:

- 📦 **Index file budget:** aim for a small `index.json` (fast parse, minimal fields)
- 🧩 **Per-dataset manifest:** small, stable, and cacheable
- 🗺️ **Don’t embed big geometries** in the catalog  
  Prefer bbox + links to tiles/COGs/GeoParquet
- 🧱 Prefer web-native geospatial formats:
  - Raster: **COG** (Cloud-Optimized GeoTIFF)
  - Vector: **vector tiles** / GeoParquet / simplified GeoJSON for small layers
  - 3D: **3D Tiles / glTF** for Cesium-mode datasets
- 🖼️ Thumbnails/legends: use modern, compressed formats where possible

---

## 🔐 Security, ethics, and sovereignty

- 🔑 Treat everything in `web/` as potentially public.
- 🧍 Don’t include PII (names, addresses, private contact info) in manifests or previews.
- 🧭 For culturally or politically sensitive sites:
  - generalize extents,
  - restrict distributions,
  - tag sovereignty/ethics fields,
  - ensure governance review gates are met.
- 🧾 License clarity is mandatory (avoid “unknown”).
- 🤝 Accessibility matters (semantic HTML, ARIA, high-contrast considerations) — the catalog should expose the metadata the UI needs to do this well.

---

## 🧰 Troubleshooting

**“Layer shows up but has no details panel”**
- Likely missing `datasets/<dataset-id>.json` or broken `refs.*` paths.

**“Search works but map layer doesn’t render”**
- Check `ui.layerType` + `ui.renderHint` and whether `assets.primary` points to a supported distribution.

**“Provenance panel is empty”**
- Missing PROV reference, or PROV exists but doesn’t summarize key inputs/activities.

**“CI says schema invalid”**
- Validate the upstream STAC/DCAT/PROV first; the web snapshot should not “patch over” invalid metadata.

---

## 📚 Project reference shelf

These project docs/books directly inform how we structure this catalog (metadata, provenance, scaling, UI/UX):

### 🧭 Core KFM docs
- 🗂️ Master pipeline & repo contracts: `docs/MASTER_GUIDE_v13.md`
- 🛰️ STAC/DCAT/PROV profiles: `docs/standards/`
- 🧪 JSON Schemas: `schemas/`

### 🗺️ Mapping + geospatial engineering
- Python geospatial processing recipes (format conversions, pipelines, tooling)
- Cloud remote sensing workflows (e.g., GEE exports and derived products)
- Cartographic design guidance (legibility, legends, color and accessibility)
- 3D GIS + WebGL references (if Cesium/3D layers are enabled)

### 📊 Statistics / modeling / evidence artifacts
- Regression + Bayesian workflows (for derived evidence layers)
- Experimental design & replication (for claims supported by analysis outputs)
- Simulation guidance (for model-driven layers)

### 🗄️ Databases / scaling / “data spaces”
- Postgres/PostGIS best practices
- Data catalog interoperability concepts
- Performance-at-scale patterns (keep manifests small, data large)

### 🔐 Security + governance
- Defensive web security awareness (avoid leakage via metadata)
- Digital humanism / AI governance framing (for ethically grounded evidence UX)

---

🧩 **If you’re unsure:** don’t “hand-edit” the web snapshot. Fix the upstream catalogs and re-export.
