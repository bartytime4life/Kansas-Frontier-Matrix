# 🗂️ Processed Data Package — `data/processed/{{DOMAIN}}/{{DATASET}}/`

![Stage](https://img.shields.io/badge/stage-processed-blue)
![Evidence-First](https://img.shields.io/badge/evidence%E2%80%91first-STAC%20%2B%20DCAT%20%2B%20PROV-purple)
![Reproducible](https://img.shields.io/badge/reproducible-deterministic-success)
![License](https://img.shields.io/badge/license-TBD-lightgrey)
![Sensitivity](https://img.shields.io/badge/sensitivity-TBD-orange)

> [!TIP]
> This is a **template README** for a processed dataset/product in KFM. Replace all `{{TOKENS}}` before publishing ✅

---

## 🧭 Table of Contents
- [🚀 Quick Start](#-quick-start)
- [🧾 Quick Facts](#-quick-facts)
- [📌 What Lives Here (and What Must Not)](#-what-lives-here-and-what-must-not)
- [🗂️ Folder Layout](#-folder-layout)
- [📦 Artifacts](#-artifacts)
- [🧬 Evidence Triplet (Required)](#-evidence-triplet-required)
- [🕸️ Graph + API + UI Integration](#-graph--api--ui-integration)
- [🧪 QA, Policy Gates, and “Fail Closed”](#-qa-policy-gates-and-fail-closed)
- [🔁 Rebuild / Reproduce](#-rebuild--reproduce)
- [🔐 Sensitivity, Ethics, and Safe Sharing](#-sensitivity-ethics-and-safe-sharing)
- [📈 Versioning + Changelog](#-versioning--changelog)
- [📚 References](#-references)

---

## 🚀 Quick Start

**What is this folder?**  
This directory holds the **authoritative, reproducible outputs** of the `{{DATASET}}` pipeline for domain `{{DOMAIN}}` (final artifacts ready for catalogs → graph → API → UI).

**What do I do first?**
1. ✅ Confirm the **primary artifacts** exist (e.g., `GeoParquet`, `PMTiles`, `COG`, `3D Tiles`, `CSV`, etc.)
2. ✅ Confirm the **Evidence Triplet** exists: **STAC + DCAT + PROV**
3. ✅ Confirm the dataset is **loadable/servable** (PostGIS + API endpoints)
4. ✅ Confirm the UI layer config can reference the dataset **without bypassing the API**

---

## 🧾 Quick Facts

| Field | Value |
|---|---|
| KFM Dataset ID | `{{KFM_DATASET_ID}}` (example pattern: `kfm.ks.{{DOMAIN}}.{{DATASET}}.v{{VERSION}}`) |
| Domain | `{{DOMAIN}}` |
| Dataset / Product | `{{DATASET}}` |
| Version | `{{VERSION}}` (recommend: `vX.Y.Z` **or** `YYYYMMDD`) |
| Build Run ID | `{{RUN_ID}}` |
| Spatial coverage | `{{SPATIAL_COVERAGE}}` (bbox/geometry + place tags) |
| Temporal coverage | `{{TEMPORAL_RANGE}}` (start/end + resolution) |
| CRS / SRID | `{{CRS}}` (ex: `EPSG:4326`) |
| Update cadence | `{{CADENCE}}` (one-off / monthly / streaming / simulation) |
| License | `{{LICENSE}}` |
| Sensitivity | `{{SENSITIVITY}}` (public / restricted / embargoed / community-controlled) |
| Primary consumers | ✅ Neo4j Graph · ✅ PostGIS · ✅ API · ✅ MapLibre/Cesium · ✅ Story Nodes · ✅ Focus Mode |
| Maintainer(s) | `{{MAINTAINERS}}` |
| Contact | `{{CONTACT}}` |

---

## 📌 What Lives Here (and What Must Not)

### ✅ Lives here
- **Final outputs** only (post-ETL, validated, reproducible)
- **Packaging artifacts** optimized for:
  - analytics (e.g., `GeoParquet`)
  - visualization (e.g., `PMTiles`, `COG`, `3D Tiles`)
  - serving (e.g., DB-ready exports, tile-ready outputs)
- **Checksums and manifests** for integrity + reproducibility

### ❌ Must NOT live here
> [!IMPORTANT]
> **No manual edits.** If bytes change, it must be via pipeline code/config and must update provenance.  
> **No ad-hoc “mystery layers.”** If it’s in the platform, it must be cataloged and traceable.

---

## 🗂️ Folder Layout

> [!NOTE]
> Keep this folder **boringly consistent** across domains. Predictability is a feature 🧱

```text
data/
└─ ✅ processed/
   └─ 🗂️ {{DOMAIN}}/
      └─ 📦 {{DATASET}}/
         ├─ 📄 README.md                      # 👈 you are here 📌 Dataset product overview + how to consume + provenance pointers
         ├─ 📦 artifacts/                     # Final data products (publishable outputs: GeoParquet/COG/PMTiles/GeoJSON/etc.)
         ├─ 🧾 manifests/                     # Checksums + inventories + registry refs (what’s here, digests, versions)
         ├─ 🪵 logs/                          # Pipeline run logs (sanitized; link to audits/ for full receipts)
         ├─ 📤 exports/                       # Optional export shapes (DB-load exports, simplified views, denormalized tables)
         └─ 👀 quicklooks/                    # Optional previews (thumbnails, sample tiles, small extracts for fast review)
```

### ✅ Recommended subfolders (choose what fits)
- `artifacts/geoparquet/`
- `artifacts/pmtiles/`
- `artifacts/cog/`
- `artifacts/3dtiles/`
- `artifacts/geojson/` (only for *small* derived subsets)
- `manifests/sha256sums.txt`
- `manifests/inventory.json`
- `manifests/oci.json` (if using OCI artifact storage)
- `exports/postgis/` (e.g., `*.sql`, `*.dump`, `*.csv`)
- `quicklooks/` (small previews for docs/UI)

---

## 📦 Artifacts

Describe what you produced and why. KFM commonly maintains **dual outputs**: one for analysis, one for UI performance.

### ✅ Artifact inventory (fill in)
| Artifact | Path | Purpose | Notes |
|---|---|---|---|
| GeoParquet | `artifacts/geoparquet/{{DATASET}}.parquet` | analytics + query | columnar, compact |
| PMTiles | `artifacts/pmtiles/{{DATASET}}.pmtiles` | fast map rendering | static tile archive |
| COG(s) | `artifacts/cog/{{DATASET}}_{{YYYY}}.tif` | raster delivery | cloud-optimized |
| 3D Tiles (optional) | `artifacts/3dtiles/{{DATASET}}/tileset.json` | Cesium 3D | terrain/buildings/etc |
| Checksums | `manifests/sha256sums.txt` | integrity | required |
| Inventory | `manifests/inventory.json` | discoverability | list of files + metadata |

### 📌 Data Dictionary
- **Schema / fields:** `{{SCHEMA_REFERENCE}}`  
- **Units + domains:** `{{UNITS_REFERENCE}}`  
- **Null semantics:** `{{NULLS_REFERENCE}}`

> [!TIP]
> If this dataset supports the **timeline slider**, ensure every record has clear temporal fields (`datetime` or `start/end`) and that your STAC temporal metadata matches.

---

## 🧬 Evidence Triplet (Required)

> [!IMPORTANT]
> The dataset is not “published” in KFM until **STAC + DCAT + PROV** exist and validate.

### 🔗 Canonical pointers (fill in)
- **STAC Collection**: `data/stac/collections/{{STAC_COLLECTION_ID}}/collection.json`
- **STAC Items**: `data/stac/items/{{STAC_COLLECTION_ID}}/*.json` (or item subfolders)
- **DCAT Dataset**: `data/catalog/dcat/{{KFM_DATASET_ID}}.jsonld` *(path may vary by repo version)*
- **PROV Lineage**: `data/prov/{{KFM_DATASET_ID}}.prov.jsonld`

### 🧷 Cross-linking requirements
Ensure each record links to the others:
- STAC → links to DCAT + PROV
- DCAT → distribution links to STAC + artifacts
- PROV → references inputs + activity + agents + outputs (including hashes)

---

## 🕸️ Graph + API + UI Integration

### 🕸️ Knowledge Graph (Neo4j)
Describe how this dataset becomes queryable context:
- **Dataset node ID**: `{{KFM_DATASET_ID}}`
- **Primary entity types**: `{{ENTITY_TYPES}}` (Place / Event / Observation / Asset / etc.)
- **Key relationships**:
  - `(Dataset)-[:COVERS]->(Place)`
  - `(Dataset)-[:ABOUT]->(Theme)`
  - `(Dataset)-[:DERIVED_FROM]->(Dataset)`
  - `(Activity)-[:USED]->(Input)`
  - `(Activity)-[:GENERATED]->(Output)`

**Graph import artifacts (if generated):**
- `data/graph/csv/{{DOMAIN}}/{{DATASET}}/nodes.csv`
- `data/graph/csv/{{DOMAIN}}/{{DATASET}}/edges.csv`

---

### 🛰️ API layer
> [!NOTE]
> The UI should not hit databases directly; everything is served through governed APIs.

Fill in how the API exposes this dataset:
- **Dataset endpoint**: `GET /datasets/{{KFM_DATASET_ID}}`
- **Tile endpoint (vector)**: `GET /tiles/{{DATASET}}/{z}/{x}/{y}.pbf`
- **Raster endpoint**: `GET /cog/{{DATASET}}/{{YYYY}}`
- **Subset endpoint**: `POST /query/{{DATASET}}` (bbox/time/filters)

---

### 🗺️ UI integration (MapLibre / Cesium)
Document the intended layer config:
- **Layer ID**: `{{UI_LAYER_ID}}`
- **Legend / attribution** pulled from DCAT (source + license)
- **Timeline behavior**: `{{TIMELINE_RULES}}`

<details>
<summary>🧩 Example MapLibre source config (template)</summary>

```json
{
  "id": "{{UI_LAYER_ID}}",
  "type": "fill",
  "source": {
    "type": "vector",
    "tiles": ["{{KFM_API_BASE}}/tiles/{{DATASET}}/{z}/{x}/{y}.pbf"],
    "minzoom": 0,
    "maxzoom": 14
  },
  "source-layer": "{{MVT_SOURCE_LAYER}}",
  "paint": {}
}
```

</details>

<details>
<summary>🌍 Example Cesium 3D Tiles config (template)</summary>

```json
{
  "tilesetUrl": "{{KFM_API_BASE}}/3dtiles/{{DATASET}}/tileset.json",
  "show": true
}
```

</details>

---

## 🧪 QA, Policy Gates, and “Fail Closed”

> [!IMPORTANT]
> Treat **data + metadata + provenance** like code: validated, tested, reviewable ✅

### ✅ Publication checklist
- [ ] Artifacts exist in `data/processed/{{DOMAIN}}/{{DATASET}}/artifacts/`
- [ ] `manifests/sha256sums.txt` present and matches artifacts
- [ ] STAC validates (schema + geometry + time fields)
- [ ] DCAT validates (required fields, license, distributions)
- [ ] PROV validates (inputs + activity + agents + outputs)
- [ ] Provenance links are present in STAC/DCAT
- [ ] Sensitivity labeled and enforced (redaction/obfuscation where needed)
- [ ] Graph import (if applicable) has referential integrity (no dangling IDs)
- [ ] API endpoints return expected responses (tiles render, queries succeed)
- [ ] UI layer renders and shows correct attribution + provenance
- [ ] If used by Focus Mode: citations resolve to catalogs and artifacts

### 🧰 Suggested QA tests (pick what fits)
- Geometry validity (self-intersections, invalid rings)
- CRS correctness and consistent SRID
- Attribute constraints (enums/ranges)
- Temporal constraints (monotonic sequences, valid intervals)
- Duplicate detection (IDs, features, tiles)
- Tile sanity (min/max zoom, feature density)
- Performance budget checks (file size, tile count, query time)
- Policy conftest/OPA checks (license present, classification present, provenance updated)

---

## 🔁 Rebuild / Reproduce

### 🧱 Inputs
- Raw inputs live under: `data/raw/{{DOMAIN}}/...`
- Work intermediates live under: `data/work/{{DOMAIN}}/...`

### 🏗 Pipeline
- Pipeline entrypoint: `{{PIPELINE_PATH}}`
- Config: `{{CONFIG_PATH}}`
- Container / env: `{{ENV_PATH}}` (e.g., `Dockerfile`, `environment.yml`, `requirements.txt`)

<details>
<summary>▶️ Example run commands (template)</summary>

```bash
# (example) run deterministic pipeline
make kfm-run DOMAIN={{DOMAIN}} DATASET={{DATASET}} VERSION={{VERSION}}

# (example) validate metadata artifacts
make kfm-validate STAC={{STAC_COLLECTION_ID}} DCAT={{KFM_DATASET_ID}} PROV={{KFM_DATASET_ID}}

# (example) regenerate checksums
( cd data/processed/{{DOMAIN}}/{{DATASET}} && sha256sum $(find artifacts -type f | sort) > manifests/sha256sums.txt )
```

</details>

---

## 🔐 Sensitivity, Ethics, and Safe Sharing

### 🏷 Sensitivity classification
- Classification: `{{SENSITIVITY}}`
- Rationale: `{{SENSITIVITY_RATIONALE}}`
- Handling:
  - [ ] redact attributes
  - [ ] generalize/round coordinates
  - [ ] role-based access controls
  - [ ] embargo or community protocol

### 🤝 CARE-aware governance
If data includes culturally sensitive locations/materials, record:
- community authority / steward: `{{COMMUNITY_STEWARD}}`
- access protocol: `{{ACCESS_PROTOCOL}}`
- consent + restrictions: `{{CONSENT_NOTES}}`

> [!TIP]
> When in doubt, ship a **public-safe derivative** (generalized) + keep the high-precision version restricted.

---

## 📈 Versioning + Changelog

### 🔖 Version scheme
- Current: `{{VERSION}}`
- Prior: `{{PRIOR_VERSION}}`
- Deprecation / replacement: `{{REPLACED_BY}}`

### 📝 Changelog
| Version | Date | Change | Notes |
|---|---:|---|---|
| `v0.1.0` | `{{DATE}}` | Initial publish | baseline |
| `v0.2.0` | `{{DATE}}` | `{{CHANGE}}` | `{{NOTES}}` |

---

## 📚 References

### 📌 KFM “how it fits” docs (link to repo docs if present)
- `docs/MASTER_GUIDE_v13.md` (overall patterns)
- `docs/architecture/` (policy gates, layering, governance)
- `docs/data/{{DOMAIN}}/README.md` (domain runbook)
- `docs/guides/pipelines/` (pipeline conventions)

### 🧠 This package enables (examples)
- 🧭 Timeline filtering (4D exploration)
- 🗺️ Provenance-aware layers (Layer Info / Layer Provenance panels)
- 📖 Story Nodes referencing datasets/places
- 🤖 Focus Mode responses with citations and auditable context

---

## ✅ “Done Means…” (definition of done)
- The artifacts load/render correctly ✅
- STAC/DCAT/PROV validate + cross-link ✅
- Graph/API/UI can consume it without hacks ✅
- Sensitivity is respected end-to-end ✅
- A future maintainer can reproduce it ✅

---

