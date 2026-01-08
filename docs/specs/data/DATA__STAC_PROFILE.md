<div align="center">

# 🛰️ **KFM-STAC v11** — STAC Profile for Kansas-Matrix-System

**Canonical catalog contract for geospatial + historical + evidence artifacts**  
`data/stac/**` ➜ discovery ➜ governance ➜ graph ingestion ➜ APIs ➜ UI

<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0.0-purple" />
<img alt="Profile" src="https://img.shields.io/badge/KFM--STAC-v11.0.0-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Required-gold" />
<img alt="PROV" src="https://img.shields.io/badge/PROV--O-Linked-brightgreen" />
<img alt="DCAT" src="https://img.shields.io/badge/DCAT-3.0-informational" />

</div>

---

## 🎯 What this profile does

KFM-STAC v11 defines **how we publish STAC Catalog / Collection / Item JSON** so that every dataset (including “evidence artifacts” like model outputs, OCR corpora, or redacted attachments) is:

- 🔎 **Discoverable** (consistent metadata + predictable layout)
- 🧾 **Auditable** (PROV link required)
- 🔁 **Reproducible** (run IDs, deterministic IDs, immutable references)
- ⚖️ **Governable** (FAIR+CARE fields + generalization/redaction rules)
- 🧠 **Graph-ready** (stable identifiers + cross-links to DCAT/PROV for KG ingestion)

> ✅ **Normative language**: **MUST / SHOULD / MAY** are used with RFC 2119 intent.

---

## 🧭 Canonical pipeline contract

KFM treats metadata as **boundary artifacts** required *before* anything is “published”:

**ETL → STAC/DCAT/PROV → Graph → API → UI**

- STAC/DCAT/PROV are the “interface layer” between processing and downstream consumption.
- UI/Focus Mode **must not** hard-code datasets; it discovers them via catalogs/APIs.

---

## 🗂️ Where STAC lives (repo contract)

### 📁 Required directory layout

```text
📁 data/
├── 📁 raw/                    # upstream source drops (immutable-as-possible)
├── 📁 work/                   # intermediate transforms (cacheable)
├── 📁 processed/              # published data products (COG/GeoParquet/PMTiles/etc.)
├── 📁 prov/                   # PROV bundles (JSON-LD)
├── 📁 catalog/
│   └── 📁 dcat/               # DCAT datasets + distributions (JSON-LD)
└── 📁 stac/                   # ✅ this profile governs everything here
    ├── 📄 catalog.json        # root STAC Catalog
    ├── 📁 <domain>/           # domain catalogs (ex: soils, water, climate, landcover)
    │   ├── 📄 catalog.json
    │   ├── 📄 collection.json
    │   └── 📁 items/
    │       ├── 📄 <item-id>.json
    │       └── 📄 ...
    └── 📁 _schemas/           # optional: local JSON Schemas / policy bundles
```

### 🧩 Domain expansion rule (when adding a new domain)

When adding a new domain, you MUST:

1. Keep domain files isolated in `data/raw/<domain>/`, `data/work/<domain>/`, `data/processed/<domain>/`
2. Publish catalog records to canonical locations:  
   `data/stac/`, `data/catalog/dcat/`, `data/prov/`
3. Extend governed profiles (KFM-STAC/KFM-DCAT/KFM-PROV) instead of creating ad-hoc fields
4. Add a runbook: `docs/data/<domain>/README.md` (ETL steps, sources, gotchas)

---

## 🧱 Conformance classes

KFM-STAC v11 defines **conformance by “kind”**:

| Conformance class | Applies to | Notes |
|---|---|---|
| 🟣 **Base** | all Catalog/Collection/Item | required everywhere |
| 🗺️ **Geo** | Items with geometry/bbox | requires Projection ext |
| 🧊 **Raster** | COG / raster outputs | requires Raster ext |
| 🧱 **Vector** | GeoParquet / GeoJSON / tiles | strongly recommends file checksums + tiling assets |
| 🧪 **Evidence** | model outputs, OCR corpora, reports | geometry MAY be null; provenance MUST be strong |
| 🪪 **Restricted** | sensitive / sovereign datasets | requires CARE fields + generalization/redaction rules |

---

## 🧩 Required STAC extensions (v11)

### ✅ Always required (all KFM Items)

- **File extension** (checksums, size, metadata):  
  `https://stac-extensions.github.io/file/v2.1.0/schema.json`
- **Version extension** (explicit versioning + lifecycle):  
  `https://stac-extensions.github.io/version/v1.2.0/schema.json`

### ✅ Required for geospatial Items

- **Projection extension** (CRS and transforms):  
  `https://stac-extensions.github.io/projection/v2.0.0/schema.json`

### ✅ Required when relevant

- **Raster extension** (COG / raster bands):  
  `https://stac-extensions.github.io/raster/v1.1.0/schema.json`
- **EO extension** (earth observation properties):  
  `https://stac-extensions.github.io/eo/v1.1.0/schema.json`
- **Processing extension** (processing lineage / algorithm metadata):  
  `https://stac-extensions.github.io/processing/v1.2.0/schema.json`
- **Classification extension** (classes/legends/values):  
  `https://stac-extensions.github.io/classification/v2.0.0/schema.json`

> ⚠️ Note: KFM uses **File extension** (not the deprecated/legacy “checksum extension”) for asset checksums.

---

## 🧾 Object requirements

### 1) 📄 STAC Catalog (root + domain)

**Root catalog** (`data/stac/catalog.json`) MUST include:

- `stac_version: "1.0.0"`
- `type: "Catalog"`
- `id` (stable)
- `description`
- `links[]` including:
  - `rel: "self"`
  - `rel: "root"` (for root catalog)
  - `rel: "child"` for each domain catalog
  - `rel: "conformance"` or `rel: "describedby"` to this spec file (recommended)

**Domain catalog** (`data/stac/<domain>/catalog.json`) MUST include:

- same as above
- `links[]` to its domain `collection.json` and/or `items/`

---

### 2) 🧺 STAC Collection

Each domain should have **at least one Collection** (e.g., `data/stac/soils/collection.json`).

Collection MUST include:

- `stac_version: "1.0.0"`
- `type: "Collection"`
- `id` (stable)
- `title`
- `description`
- `license` (SPDX string or "proprietary"; URL recommended via `links`)
- `extent.spatial.bbox`
- `extent.temporal.interval`
- `providers[]` (at least one)
- `keywords[]` (recommended for DCAT keyword alignment)

Collection SHOULD include:

- `summaries` (for common fields like variables, resolution, quality labels)
- `assets` (for collection-level artifacts like README, schema, tileset index)

---

### 3) 📦 STAC Item (the workhorse)

#### 🧷 Minimum KFM Item (Base conformance)

Each Item MUST include:

- `stac_version: "1.0.0"`
- `type: "Feature"`
- `id` (deterministic; see ID policy below)
- `collection` (collection id)
- `properties.datetime` OR (`properties.start_datetime` + `properties.end_datetime`)
- `properties.license` (KFM-required field; see license policy)
- `assets` (non-empty object)
- `links[]` containing at least:
  - `rel: "self"`
  - `rel: "collection"`
  - **one provenance link**: `rel: "prov"` (required)

Geospatial Items MUST include:

- `geometry` (GeoJSON) OR `null` (allowed only for Evidence/Restricted cases)
- `bbox` (array) OR `null`/omitted if geometry is null
- `stac_extensions` including Projection extension
- `properties.proj:epsg` OR alternative projection fields per Projection ext

---

## 🧬 KFM custom fields (`kfm:*` namespace)

KFM adds a small, governed set of custom properties. These MUST live under:

- Item `properties["kfm:*"]` (preferred)
- or top-level (only if required by a tooling constraint)

### ✅ Required KFM fields (all Items)

| Field | Type | Description |
|---|---|---|
| `kfm:domain` | string | domain slug (e.g., `soils`, `water`, `climate`, `landcover`, `history`) |
| `kfm:run_id` | string | pipeline run identifier (see deterministic rules) |
| `kfm:qa_status` | string | `pass` \| `warn` \| `fail` |
| `kfm:care_status` | string | `public` \| `restricted` \| `sensitive` \| `sovereign` \| `unknown` |
| `kfm:generalization` | string | generalization policy tag (or `none`) |

### ✅ Required when applicable

| Field | Type | When required |
|---|---|---|
| `kfm:source_sha256` | string | when any upstream source artifact is persisted |
| `kfm:artifact_sha256` | string | when a primary output asset exists |
| `kfm:commit_sha` | string | when produced by CI/CD or committed ETL |
| `kfm:energy_telemetry_ref` | string | when telemetry is captured for the run |
| `kfm:sbom_ref` | string | when software provenance/SBOM exists |
| `kfm:sensitivity_notes` | string | when `kfm:care_status != public` |
| `kfm:access_policy_ref` | string | when restricted/sovereign governance applies |

> 🎛️ Keep `kfm:*` small and **schema-governed**. If you need new fields, extend the profile—don’t invent one-offs.

---

## 🧾 Deterministic IDs & run IDs (non-negotiable)

### ✅ Item `id` policy

Item `id` MUST be **deterministic** given:

- dataset identifier (domain + collection)
- source identifiers (URLs, IDs, publication date, etc.)
- processing config digest (parameters, code version, model hash)
- artifact digest (hash of outputs)

Recommended shape:

- `"<domain>--<collection>--<run_id>"`
- OR `"<dataset_slug>--v<semver>--<short_hash>"`

### ✅ `kfm:run_id` policy

`kfm:run_id` MUST be stable and reproducible for a run and SHOULD include:

- date stamp
- short content/config hash
- optionally CI run number

Example:

- `run-2026-01-02-6b0e0b`

---

## ⚖️ FAIR+CARE + generalization rules

### ✅ Geometry redaction / generalization

KFM permits `geometry: null` (or heavily generalized geometry) ONLY when:

- the Item is non-geospatial evidence, **or**
- governance requires redaction/generalization (restricted/sovereign)

If geometry is omitted or generalized, the Item MUST:

- set `kfm:care_status` appropriately
- set `kfm:generalization` to a known policy tag, e.g.:
  - `none`
  - `bbox_simplified_5km`
  - `h3_aggregation_r4` (example)
  - `centroid_only`
  - `geometry_null_sensitive`

### ✅ Don’ts (CARE guardrails)

- 🚫 Do not publish raw protected coordinates in STAC if policy forbids it
- 🚫 Do not re-identify locations via “helpful” joins in downstream APIs
- 🚫 Do not store restricted identifiers in logs / DLQs / public metadata blobs

---

## 🔗 Links & cross-catalog alignment

### ✅ Required STAC link relations

Each Item MUST include these link relations:

| rel | required | purpose |
|---|---:|---|
| `self` | ✅ | the Item JSON URL/path |
| `collection` | ✅ | owning Collection |
| `root` | ✅ recommended | root catalog |
| `prov` | ✅ | provenance bundle (PROV-O JSON-LD) |

### ✅ Recommended cross-links (KFM interoperability)

- `rel: "describedby"` → DCAT dataset JSON-LD record
- `rel: "via"` → upstream landing page / DOI / source API
- `rel: "license"` → license URL text (even if `properties.license` is a code)

---

## 🧾 Assets: roles, keys, formats

### ✅ Asset key conventions

KFM standard asset keys (RECOMMENDED):

| key | typical roles | typical format |
|---|---|---|
| `data` | `["data"]` | GeoParquet / GeoJSON / COG |
| `tiles` | `["tiles"]` | PMTiles / MBTiles |
| `thumbnail` | `["thumbnail"]` | PNG/JPEG |
| `legend` | `["legend"]` | SVG/PNG/JSON |
| `style` | `["style"]` | MapLibre style JSON / QGIS style |
| `metadata` | `["metadata"]` | DCAT JSON-LD |
| `provenance` | `["metadata","provenance"]` | PROV JSON-LD |
| `report` | `["metadata","overview"]` | PDF/HTML/MD |

### ✅ File integrity fields (required)

Each asset MUST include File extension fields as applicable:

- `type` (IANA media type)
- `file:checksum` (multihash) ✅
- `file:size` (bytes) ✅ recommended
- `file:created`, `file:modified` (recommended)

### ✅ Recommended media types

- `application/geo+json`
- `application/geoparquet`
- `image/tiff; application=geotiff; profile=cloud-optimized` (COG)
- `application/vnd.pmtiles`
- `image/png`
- `image/jpeg`
- `application/ld+json` (JSON-LD: DCAT/PROV)
- `text/markdown`

---

## 🧪 Validation & CI gates

### ✅ Required validation stages

KFM expects automated gates (local + CI):

1. **STAC schema validation** (base spec + required extensions)
2. **KFM-STAC policy validation** (presence of `prov` link, license, care status, etc.)
3. **Cross-artifact consistency checks**:
   - Item assets ↔ DCAT distributions (1:1)
   - Item ↔ PROV bundle (resolves and is reachable)
   - Checksums match file content
4. **Governance checks**:
   - generalization rules enforced
   - restricted fields redacted

### 🧰 Minimal sanity checks (recommended)

At minimum, a pre-merge job should fail if an Item is missing:

- `id`
- `bbox` or explicit null-handling rule
- `properties.datetime`
- `properties.license`
- `assets` non-empty
- `links` includes `rel="prov"`

---

## 🧾 Example: Vector layer Item (GeoParquet + PMTiles)

> This is a template-style example (trim for real usage). Replace placeholders with real values.

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/version/v1.2.0/schema.json",
    "https://stac-extensions.github.io/projection/v2.0.0/schema.json"
  ],
  "id": "soils--soilgrids_250m--run-2026-01-02-6b0e0b",
  "collection": "soils--soilgrids_250m",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[-102.05, 36.99], [-94.60, 36.99], [-94.60, 40.00], [-102.05, 40.00], [-102.05, 36.99]]]
  },
  "bbox": [-102.05, 36.99, -94.60, 40.00],
  "properties": {
    "datetime": "2026-01-02T00:00:00Z",
    "license": "CC-BY-4.0",

    "kfm:domain": "soils",
    "kfm:run_id": "run-2026-01-02-6b0e0b",
    "kfm:qa_status": "pass",
    "kfm:care_status": "public",
    "kfm:generalization": "none",

    "proj:epsg": 4326
  },
  "assets": {
    "data": {
      "href": "data/processed/soils/soilgrids_250m/kansas_soils.geoparquet",
      "type": "application/geoparquet",
      "roles": ["data"],
      "title": "Kansas soils (GeoParquet)",
      "file:checksum": "1220aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "file:size": 123456789
    },
    "tiles": {
      "href": "data/processed/soils/soilgrids_250m/kansas_soils.pmtiles",
      "type": "application/vnd.pmtiles",
      "roles": ["tiles"],
      "title": "Kansas soils (PMTiles)",
      "file:checksum": "1220bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
      "file:size": 987654321
    },
    "provenance": {
      "href": "data/prov/soils/run-2026-01-02-6b0e0b.prov.jsonld",
      "type": "application/ld+json",
      "roles": ["metadata", "provenance"],
      "title": "PROV-O lineage bundle",
      "file:checksum": "1220cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
    },
    "metadata": {
      "href": "data/catalog/dcat/soils/soilgrids_250m/run-2026-01-02-6b0e0b.dcat.jsonld",
      "type": "application/ld+json",
      "roles": ["metadata"],
      "title": "DCAT 3.0 dataset descriptor",
      "file:checksum": "1220dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
    }
  },
  "links": [
    { "rel": "self", "href": "data/stac/soils/items/soils--soilgrids_250m--run-2026-01-02-6b0e0b.json", "type": "application/json" },
    { "rel": "collection", "href": "data/stac/soils/collection.json", "type": "application/json" },
    { "rel": "prov", "href": "data/prov/soils/run-2026-01-02-6b0e0b.prov.jsonld", "type": "application/ld+json" },
    { "rel": "describedby", "href": "data/catalog/dcat/soils/soilgrids_250m/run-2026-01-02-6b0e0b.dcat.jsonld", "type": "application/ld+json" }
  ]
}
```

---

## 🧠 Evidence artifacts (AI/analysis outputs)

KFM treats evidence artifacts as **first-class datasets**:

- store under `data/processed/...`
- publish STAC Item for them
- publish DCAT dataset record
- publish PROV activity capturing:
  - inputs
  - algorithm/model
  - parameters/config
  - confidence/uncertainty metrics (where relevant)

If the artifact yields new graph entities/relations, those MUST be loaded into Neo4j with explicit provenance pointing back to the artifact.

---

## 🔒 Security & integrity (minimum expectations)

- ✅ Every asset has a checksum (`file:checksum`)
- ✅ Provenance exists and is linked via `rel="prov"`
- ✅ Metadata includes license and CARE classification
- ✅ Avoid injection-style vulnerabilities in any catalog tooling (parameterize queries; never string-concat Cypher/SQL)

---

## 📚 Reference shelf (project library used to shape this profile)

This spec is intentionally informed by the project’s full library:

### 🗺️ Geospatial & remote sensing
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`

### 🧊 Data management, catalogs, interoperability
- `Data Spaces.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`

### 🧪 Modeling, statistics, uncertainty, validation
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `graphical-data-analysis-with-r.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`

### 🧠 Graph + systems thinking
- `Spectral Geometry of Graphs.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx`

### 🧑‍⚖️ Ethics, humanism, and governance
- `Introduction to Digital Humanism.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`

### 🛡️ Security & secure engineering
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### 🌐 UI + web delivery
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 📦 Implementation library indexes (language/tool coverage)
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

### 🧩 KFM internal drafting inputs
- `Latest Ideas.docx`
- `Other Ideas.docx`
- `MARKDOWN_GUIDE_v13.md.gdoc`

---

## ✅ KFM-STAC v11 conformance checklist (copy/paste)

- [ ] Item validates as STAC 1.0.0 Feature
- [ ] `stac_extensions` includes File + Version (+ Projection if geospatial)
- [ ] Deterministic `id` and `kfm:run_id` present
- [ ] `properties.datetime` and `properties.license` present
- [ ] `assets` non-empty and each asset has `file:checksum`
- [ ] `links` contains `rel="prov"`
- [ ] `kfm:care_status` and `kfm:generalization` set (even if `none`)
- [ ] DCAT & PROV exist and are cross-linked (recommended, but expected for publish)
- [ ] Sensitive/restricted datasets do not leak protected geometry/identifiers

---

## 🧾 Changelog

| Version | Date | Notes |
|---|---|---|
| v11.0.0 | 2026-01-08 | Initial consolidated STAC profile spec for Kansas-Matrix-System |

---

## 🔜 TODO (next specs that pair with this one)

- `docs/specs/data/DATA__DCAT_PROFILE.md`
- `docs/specs/data/DATA__PROV_PROFILE.md`
- `docs/specs/data/DATA__CATALOG_VALIDATION.md` (Rego + schema + CI pipeline)
- `data/stac/_schemas/kfm-stac-v11.schema.json` (machine-checkable constraints)

