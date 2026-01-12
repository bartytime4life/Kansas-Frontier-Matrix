---
title: "KFM Standard — DCAT Profile"
path: "docs/standards/KFM_DCAT_PROFILE.md"
version: "v11.0.0"
last_updated: "2026-01-12"
status: "draft"
doc_kind: "Standard"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:standards:dcat-profile:v11.0.0"
semantic_document_id: "kfm-standard-dcat-profile-v11.0.0"
event_source_id: "ledger:kfm:doc:standards:dcat-profile:v11.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Standard — DCAT Profile 🗂️🌾

![KFM](https://img.shields.io/badge/KFM-Standard-2ea44f)
![Profile](https://img.shields.io/badge/KFM--DCAT-v11.0.0-blue)
![Status](https://img.shields.io/badge/Status-draft-yellow)
![License](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-guardrails-ff69b4)
![Jurisdiction](https://img.shields.io/badge/Jurisdiction-US--KS-informational)

**Profile ID:** `KFM-DCAT v11.0.0`

> ✅ **DCAT in KFM = dataset-level discovery + interoperability layer**  
> STAC describes *assets* (spatial/temporal); PROV describes *lineage*; DCAT describes *datasets + distributions + services* that bind the system together.

---

## 🧭 Quicklinks
- [📘 Overview](#-overview)
- [🧨 Non-negotiables](#-non-negotiables)
- [🗂️ Directory Layout](#️-directory-layout)
- [🗺️ Diagrams](#️-diagrams)
- [📦 Data & Metadata](#-data--metadata)
- [🌐 STAC, DCAT & PROV Alignment](#-stac-dcat--prov-alignment)
- [🧱 KFM Extensions](#-kfm-extensions)
- [🧪 Validation & QA](#-validation--qa)
- [🧾 Examples](#-examples)
- [📚 External References](#-external-references)

---

## 📘 Overview

### Purpose 🎯
Define how KFM publishes dataset and service metadata using DCAT, including:

- **Canonical placement + file layout** under `data/catalog/dcat/`
- **Minimum required fields** + **controlled values**
- **Mapping** between:
  - STAC Collections/Items ↔ DCAT Datasets/Distributions
  - PROV bundles ↔ DCAT provenance hooks
- **Operational contract** for any pipeline step that emits/consumes DCAT:
  - catalog builder
  - graph ingest
  - API metadata exposure
  - external catalog export/harvesting
  - UI provenance/attribution overlays

### Scope ✅ / ❌
| In scope ✅ | Out of scope ❌ |
|---|---|
| DCAT Dataset & Distribution records for KFM datasets | Full RDF / Linked Data tutorial |
| DCAT Catalog record(s) for repo/deployment | Full API endpoint specs (see API contracts) |
| DCAT DataService records for KFM APIs | Ontology design (see KFM-ONTO) |
| STAC+PROV → DCAT mapping rules | UI/UX rendering details |

### Audience 👥
- **Primary:** Data engineers, catalog maintainers, pipeline authors
- **Secondary:** Graph ingestion maintainers, API developers, doc authors, QA reviewers

### Definitions 📚
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **DCAT**: Data Catalog Vocabulary for describing datasets and services
  - **Dataset**: A logical dataset exposed by KFM (human-meaningful unit)
  - **Distribution**: A concrete access method for a dataset (file, endpoint, STAC link, tile package)
  - **Catalog**: A collection of datasets and services
  - **DataService**: An API/service providing access to datasets
  - **STAC Collection/Item**: Asset-level metadata for geospatial/temporal artifacts
  - **PROV bundle**: Lineage record capturing activities, agents, entities (inputs → work → outputs)

### Key artifacts 🔑
| Artifact | Path / identifier | Notes |
|---|---|---|
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` | Governs KFM-DCAT constraints |
| DCAT records | `data/catalog/dcat/` | Datasets, services, (optional) catalog root |
| STAC collections/items | `data/stac/collections/`, `data/stac/items/` | Canonical asset metadata |
| PROV bundles | `data/prov/` | Canonical lineage bundles |
| Catalog QA tool | `tools/validation/catalog_qa/` | CI gate for metadata quality |
| Policy Pack | `tools/validation/policy/` | OPA/Conftest governance checks (as code) |
| Schemas/shapes | `schemas/dcat/` | JSON Schema/SHACL (when adopted) |

### Definition of done ✅
- [ ] Front-matter complete and valid
- [ ] `data/catalog/dcat/` naming + placement rules are explicit
- [ ] MUST/SHOULD/MAY constraints are enumerated
- [ ] STAC/DCAT/PROV linkage rules are defined (cross-layer references)
- [ ] Sensitivity, classification, and redaction handling is stated
- [ ] Validation steps are listed + repeatable in CI and locally
- [ ] Examples include **(a)** dataset **(b)** service **(c)** distribution checksums

---

## 🧨 Non-negotiables

> These are “pipeline physics” 🧲 — if you break them, downstream trust breaks.

1. **Canonical ordering MUST be preserved**  
   `ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode`

2. **Boundary artifacts MUST exist before “published”** ✅  
   For every dataset (including AI/analysis outputs), publication requires:
   - STAC record(s)
   - DCAT dataset entry
   - PROV lineage bundle

3. **Atomic publish** 🧾  
   Pipelines MUST stage outputs, validate everything, then promote *all-or-nothing*:
   - data → `data/processed/…`
   - metadata → STAC/DCAT/PROV canonical folders  
   Partial publication is not allowed.

4. **Classification cannot loosen downstream** 🔒  
   No output artifact may be **less restricted** than any input it derives from.

---

## 🗂️ Directory Layout

### Canonical repository paths 🧱
| Area | Path | What lives here |
|---|---|---|
| Source manifests | `data/sources/` | External dataset manifests (URLs, licenses, source info) |
| Raw data | `data/raw/<domain>/` | Ingested/unprocessed inputs |
| Working data | `data/work/<domain>/` | Intermediate transformations |
| Processed data | `data/processed/<domain>/` | Final curated outputs (official artifacts) |
| STAC catalogs | `data/stac/` | Collections + Items |
| DCAT catalogs | `data/catalog/dcat/` | Dataset entries + DataServices + optional catalog root |
| PROV lineage | `data/prov/<run_id>/bundle.jsonld` | Provenance bundles per pipeline run |
| Schemas | `schemas/` | JSON Schemas / SHACL shapes (DCAT/STAC/PROV/story/telemetry) |
| Pipelines | `src/pipelines/` | ETL + normalization + packaging code |
| Graph | `src/graph/` | Graph ingest + ontology bindings + constraints |
| API boundary | `src/server/` | API impl + contracts + redaction |
| UI | `web/` | React + MapLibre (+ optional Cesium) |
| Validation tools | `tools/validation/` | Catalog QA + policy checks |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative markdown + assets |

> 🧩 **Legacy notes (v12→v13):**  
> Some older docs reference `data/catalog/` for STAC or `data/provenance/` for lineage.  
> **v13 canonical homes** are `data/stac/` and `data/prov/`. New work MUST use canonical paths.

### Expected file tree 📁
~~~text
📁 docs/
└── 📁 standards/
    └── 📄 KFM_DCAT_PROFILE.md

📁 data/
├── 📁 sources/
│   └── 📄 <source_manifest>.yml
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   │   └── 📄 <collection_id>.json
│   └── 📁 items/
│       └── 📄 <item_id>.json
├── 📁 catalog/
│   └── 📁 dcat/
│       ├── 📄 catalog.jsonld              (optional)
│       ├── 📁 datasets/
│       │   └── 📄 <dataset_id>.jsonld
│       └── 📁 services/
│           └── 📄 <service_id>.jsonld
└── 📁 prov/
    └── 📁 <run_id>/
        └── 📄 bundle.jsonld

📁 tools/
└── 📁 validation/
    ├── 📁 catalog_qa/
    └── 📁 policy/
        ├── 📄 conftest.yaml
        └── 📄 *.rego

📁 schemas/
└── 📁 dcat/
    ├── 📄 kfm-dcat.dataset.schema.json     (optional)
    └── 📄 kfm-dcat.service.schema.json     (optional)
~~~

---

## 🗺️ Diagrams

### System dataflow (canonical) 🧬
~~~mermaid
flowchart LR
  subgraph Data["Data (staged → published)"]
    A["Raw Sources<br/>data/raw + data/sources"] --> B["ETL + Normalization<br/>src/pipelines"]
    B --> C["STAC Items + Collections<br/>data/stac"]
    C --> D["DCAT Dataset Views<br/>data/catalog/dcat"]
    C --> E["PROV Lineage Bundles<br/>data/prov"]
  end

  C --> G["Neo4j Graph<br/>(references catalogs)"]
  G --> H["API Layer<br/>(contracts + redaction)"]
  H --> I["Map UI<br/>React · MapLibre · (optional) Cesium"]
  I --> J["Story Nodes<br/>(governed narratives)"]
  J --> K["Focus Mode<br/>(provenance-linked context bundle)"]
~~~

### DCAT object model (KFM minimal + services) 🧱
~~~mermaid
flowchart TB
  Catalog[dcat:Catalog] -->|dcat:dataset| Dataset[dcat:Dataset]
  Dataset -->|dcat:distribution| Dist[dcat:Distribution]
  Service[dcat:DataService] -->|dcat:servesDataset| Dataset
  Dist -->|dcat:accessService| Service
  Dataset -->|dct:provenance or prov:wasGeneratedBy| Prov[PROV bundle / Activity]
  Dataset -->|dct:relation / dcat:landingPage| STAC[STAC Collection/Items]
~~~

---

## 📦 Data & Metadata

### Inputs 📥
| Input | Format | Location | Notes |
|---|---|---|---|
| Source manifests | YAML/JSON | `data/sources/` | External references (URLs, license, attribution) |
| Raw datasets | mixed | `data/raw/<domain>/` | Ingested inputs |
| Working datasets | mixed | `data/work/<domain>/` | Intermediate transforms |
| Processed artifacts | mixed | `data/processed/<domain>/` | Final outputs that distributions reference |
| STAC collections/items | JSON | `data/stac/collections/`, `data/stac/items/` | Spatial/temporal extents + asset links |
| PROV bundles | JSON-LD | `data/prov/<run_id>/bundle.jsonld` | Lineage, parameters, agents, run IDs/commit |
| Domain docs | Markdown | `docs/data/<domain>/` | Dataset intent, constraints, runbooks |
| Schemas/shapes | JSON / TTL | `schemas/` | Validation targets (when implemented) |

### Outputs 📤
| Output | Format | Location | Notes |
|---|---|---|---|
| DCAT datasets | JSON-LD (canonical) | `data/catalog/dcat/datasets/<dataset_id>.jsonld` | One per semantic dataset |
| DCAT services | JSON-LD (canonical) | `data/catalog/dcat/services/<service_id>.jsonld` | APIs, tile services, GraphQL, etc. |
| DCAT catalog | JSON-LD | `data/catalog/dcat/catalog.jsonld` | Optional root catalog for harvesters |

### Sensitivity & redaction 🔐
- Every DCAT Dataset record MUST include machine-readable **access metadata** enabling enforcement:
  - `dct:accessRights` (controlled)
  - KFM extensions (see [KFM Extensions](#-kfm-extensions)) for classification/sensitivity propagation
- If a dataset or distribution contains sensitive locations, DCAT records SHOULD:
  - provide generalized `dct:spatial` bounds, **or**
  - omit public spatial extents and rely on restricted channels
- Public-facing catalogs MUST NOT reveal restricted coordinates, identifiers, or inferred sensitive locations.

### Quality signals ✅
A dataset is “catalog-clean” when:
- Required terms are present and non-empty
- All distributions resolve (files exist; endpoints reachable in deployment)
- PROV linkage exists and references a recorded run/activity
- License is present and valid for intended exposure
- Version traceability exists (linking updates and revisions)
- CI metadata gates pass (Catalog QA + Policy Pack)

---

## 🌐 STAC, DCAT & PROV Alignment

### Normative language 📌
- **MUST**: required for publication
- **SHOULD**: required unless documented exception exists
- **MAY**: optional

### Alignment policy (required) 🧩
Every dataset or “evidence artifact” (analysis output, AI-generated layer, simulation result) MUST have:
1) STAC Collection + Item(s) (even for many non-spatial datasets, a Collection is recommended for consistency)  
2) DCAT Dataset entry (discovery + distributions)  
3) PROV bundle (end-to-end lineage)

---

## 🧭 DCAT (KFM-DCAT) Rules

### Serialization rules (KFM canonical) 🧾
- **Canonical serialization:** JSON-LD (`*.jsonld`) ✅
- **Optional export formats:** Turtle / RDF/XML MAY be generated, but MUST be semantically equivalent to JSON-LD.
- `@context` MUST include at least:
  - `dcat`, `dct`, `prov`
- KFM records SHOULD define a `kfm:` namespace for project-specific fields (see [KFM Extensions](#-kfm-extensions)).

### File placement & naming rules 📌
- Each dataset MUST have **exactly one** DCAT dataset record at:
  - `data/catalog/dcat/datasets/<dataset_id>.jsonld`
- Each DataService SHOULD have **exactly one** service record at:
  - `data/catalog/dcat/services/<service_id>.jsonld`
- Dataset IDs MUST be stable across rebuilds for the same semantic dataset.
- Recommended dataset identifier patterns:
  - **URN IRI (preferred):** `urn:kfm:dataset:<domain>:<dataset_slug>:v<semver>`
  - **Human-friendly key (allowed as alias):** `kfm.<region>.<theme>.<year_range>.v<major>`
- File naming SHOULD mirror the identifier in filesystem-safe form:
  - `<domain>__<dataset_slug>__v<semver>.jsonld`

### Minimum required terms (Dataset) ✅
Each `dcat:Dataset` MUST include:

1) **Identity & description**
- `dct:identifier` (stable unique identifier)
- `dct:title`
- `dct:description`

2) **Rights & governance**
- `dct:license`
- `dct:accessRights` (controlled value)
- `dct:publisher` OR `dct:creator` (attribution support)

3) **Access**
- At least one `dcat:distribution`

4) **Provenance linkage**
- One of:
  - `dct:provenance` → PROV bundle path/IRI, OR
  - `prov:wasGeneratedBy` → Activity IRI (with bundle discoverable)

Each `dcat:Dataset` SHOULD include:
- `dct:issued` and `dct:modified`
- `dcat:keyword` (≥ 1 keyword)
- `dcat:theme` (controlled-ish; see vocab section)
- `dct:spatial` and `dct:temporal` when applicable
- `dct:accrualPeriodicity` for updated/streaming datasets
- `dcat:landingPage` to docs/UI page for humans

### Minimum required terms (Distribution) ✅
Each `dcat:Distribution` MUST include:
- `dct:format` (use IANA media type where possible)
- One of:
  - `dcat:accessURL`
  - `dcat:downloadURL`

Each `dcat:Distribution` SHOULD include:
- `spdx:checksum` for file-based artifacts (SHA-256 preferred)
- `dct:license` when distribution-specific
- `dct:conformsTo` when a schema/standard applies (STAC, GeoJSON, COG, GeoParquet, PMTiles, OGC API, etc.)
- `dcat:accessService` when access is via `dcat:DataService`

### Minimum required terms (DataService) ✅
Each `dcat:DataService` MUST include:
- `dct:title`
- `dct:description`
- `dcat:endpointURL`

Each `dcat:DataService` SHOULD include:
- `dcat:endpointDescription` (e.g., OpenAPI/GraphQL schema URL or repo path)
- `dct:conformsTo` (API contract identifier)
- `dcat:servesDataset` (one or more dataset identifiers)
- `dct:license` and `dct:accessRights` when service-specific

---

## 🔗 Cross-layer Linkage Rules (STAC ↔ DCAT ↔ PROV ↔ Graph)

### STAC Items → Data (required) 🧷
- STAC Items MUST point to actual data assets (files or endpoints) in:
  - `data/processed/**` (or stable equivalent storage)
- STAC records MUST carry source attribution + license where applicable.

### DCAT → STAC / Data (required) 🧭
A DCAT Dataset MUST include at least one of:
- A Distribution linking to the STAC Collection JSON (`dcat:accessURL`), OR
- Direct Distributions linking to the underlying data artifacts, OR
- `dct:relation` entries pointing to STAC Items/Collections (recommended for “asset-heavy” datasets)

### PROV end-to-end (required) 🧾
- PROV bundles MUST link:
  - raw inputs → work intermediates → processed outputs
- PROV bundles SHOULD identify:
  - run ID
  - pipeline id/name
  - commit hash (or container/image digest)
  - parameters/config used

### Graph references catalogs (required principle) 🧠
- Graph nodes SHOULD store **references** (STAC IDs, DCAT IDs, DOIs, IRIs), not bulky payloads.
- The graph models **relationships**, while catalogs store **artifact metadata**.

---

## 🧱 KFM Extensions

> KFM extends base DCAT with project-specific fields (e.g., provenance references, uncertainty indicators).  
> These fields MUST NOT replace DCAT terms; they complement them.

### Namespace (recommended) 🏷️
In JSON-LD `@context`, define:

~~~json
{
  "kfm": "urn:kfm:terms:",
  "spdx": "http://spdx.org/rdf/terms#",
  "schema": "https://schema.org/"
}
~~~

### Required KFM extension fields (Dataset) ✅
Each dataset record MUST include KFM governance + traceability fields (either embedded or resolvable via PROV):

- `kfm:classification` — e.g. `open | restricted | embargoed | internal`
- `kfm:sensitivity` — e.g. `public | sensitive_locations | pii | cultural_sensitive | mixed`
- `kfm:jurisdiction` — e.g. `US-KS`
- One of:
  - `kfm:runId` (pipeline run UUID / stable run key), OR
  - `kfm:sourceEventId` (ledger/event id), OR
  - both (preferred)

Each dataset SHOULD include:
- `kfm:commitSha` (or image digest)
- `kfm:domain` (maps to `data/<stage>/<domain>/`)
- `kfm:artifactStage` (raw/work/processed)
- `kfm:uncertainty` (see below) when dataset is modeled/derived

### Uncertainty indicators (recommended) 📈
For modeled/derived datasets (simulations, regressions, bias-corrected sensors, AI extraction), dataset records SHOULD include a structured uncertainty block, e.g.:

- `kfm:uncertaintyMethod` (string)
- `kfm:confidence` (0–1)
- `kfm:qualityFlags` (array)
- `kfm:assumptionsRef` (link to method card / MCP run)

> 💡 This allows UI + Focus Mode to surface “how sure are we?” alongside provenance.

### Checksums (recommended) 🔐
For file-based distributions, include:

- `spdx:checksum` with SHA-256 (preferred), e.g.:
  - `spdx:algorithm`: `"SHA256"`
  - `spdx:checksumValue`: `"<hex>"`

This supports deterministic packaging + change detection (ETags/checksums) and improves auditability.

---

## 🧷 Controlled Values (Recommended)

### Access rights (`dct:accessRights`) 🔐
KFM SHOULD use one of:
- `public`
- `restricted`
- `embargoed`
- `internal`

### Formats (`dct:format`) 📦
Use IANA media types when available:
- GeoJSON: `application/geo+json`
- JSON / JSON-LD: `application/json`, `application/ld+json`
- Parquet / GeoParquet: `application/vnd.apache.parquet`
- TIFF/GeoTIFF/COG: `image/tiff` (and add `dct:conformsTo` for GeoTIFF/COG)
- CSV: `text/csv`
- PMTiles: use `application/octet-stream` + `dct:conformsTo` (until a stable media type is adopted)

### Standards (`dct:conformsTo`) 🧾
Use canonical spec references (examples):
- STAC spec
- DCAT v3
- PROV-O
- GeoJSON
- OGC API Features / WMS / WFS (if used)
- PMTiles spec
- GeoParquet spec
- OpenAPI / GraphQL schema references

---

## 🧪 Validation & QA

### CI gates (expected) ✅
Before merge/publish, new or modified DCAT records SHOULD pass:

1) **Catalog QA Gate** (`tools/validation/catalog_qa/`)
- required fields present
- links resolve (STAC/PROV/data)
- license/access fields present
- format/media types reasonable

2) **Policy Gate** (`tools/validation/policy/` via OPA/Conftest)
- FAIR/CARE rules
- sensitive location handling
- classification propagation (“no loosening”)
- retention / provenance requirements

3) **Schema validation (when schemas exist)**
- JSON Schema and/or SHACL shapes in `schemas/dcat/`

4) **Reproducibility + traceability checks**
- run IDs present
- provenance link exists
- checksums for file distributions (recommended)
- commit SHA (or image digest) recorded (recommended)

> 🧠 Treat metadata like code: if it doesn’t pass tests, it doesn’t ship.

---

## 🧾 Examples

> These examples are illustrative. Replace identifiers, paths, and checksums with real values.

### Example A — Minimal Dataset (JSON-LD) ✅
~~~json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "kfm": "urn:kfm:terms:"
  },
  "@id": "urn:kfm:dataset:environment:air_quality_nowcast:v1.0.0",
  "@type": "dcat:Dataset",

  "dct:identifier": "urn:kfm:dataset:environment:air_quality_nowcast:v1.0.0",
  "dct:title": "Kansas Air Quality NowCast (Bias-Corrected)",
  "dct:description": "Bias-corrected air quality series with QC flags and reproducible processing metadata.",
  "dct:license": "CC-BY-4.0",
  "dct:accessRights": "public",

  "dct:issued": "2026-01-01",
  "dct:modified": "2026-01-10",
  "dct:accrualPeriodicity": "http://purl.org/cld/freq/daily",

  "dcat:keyword": ["kansas", "air quality", "nowcast", "environment"],
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:format": "application/ld+json",
      "dcat:accessURL": "data/stac/collections/air_quality_nowcast.json",
      "dct:conformsTo": "https://stacspec.org/"
    },
    {
      "@type": "dcat:Distribution",
      "dct:format": "application/vnd.apache.parquet",
      "dcat:downloadURL": "data/processed/environment/air_quality/air_quality_nowcast__v1.0.0.parquet",
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "<sha256-hex>"
      },
      "dct:conformsTo": "https://github.com/opengeoparquet/geo-parquet"
    }
  ],

  "dct:provenance": "data/prov/2026-01-10_air_quality_run/bundle.jsonld",

  "kfm:domain": "environment",
  "kfm:artifactStage": "processed",
  "kfm:classification": "open",
  "kfm:sensitivity": "public",
  "kfm:jurisdiction": "US-KS",
  "kfm:runId": "2026-01-10_air_quality_run",
  "kfm:commitSha": "<git-sha>",
  "kfm:uncertaintyMethod": "quantile-mapping + gamma-tail",
  "kfm:confidence": 0.85,
  "kfm:qualityFlags": ["stale-data-check", "insufficient-reference-check"]
}
~~~

### Example B — DataService (JSON-LD) ✅
~~~json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "kfm": "urn:kfm:terms:"
  },
  "@id": "urn:kfm:service:api:geodata:v1",
  "@type": "dcat:DataService",
  "dct:title": "KFM GeoData API (REST)",
  "dct:description": "REST API for dataset discovery and geospatial retrieval (GeoJSON, tiles, metadata).",
  "dcat:endpointURL": "<https://kfm.example/api/v1/>",
  "dcat:endpointDescription": "src/server/contracts/openapi.yaml",
  "dct:conformsTo": "urn:kfm:contract:api:geodata:v1",
  "dcat:servesDataset": [
    "urn:kfm:dataset:environment:air_quality_nowcast:v1.0.0"
  ],
  "dct:accessRights": "public",
  "kfm:classification": "open"
}
~~~

### Example C — Optional root Catalog (JSON-LD) 📚
~~~json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/"
  },
  "@id": "urn:kfm:catalog:main:v1",
  "@type": "dcat:Catalog",
  "dct:title": "Kansas Frontier Matrix — DCAT Catalog",
  "dct:description": "Repository-level DCAT catalog for external harvesting and internal discovery.",
  "dcat:dataset": [
    "urn:kfm:dataset:environment:air_quality_nowcast:v1.0.0"
  ]
}
~~~

---

## 📚 External References
~~~text
DCAT v3 (W3C): https://www.w3.org/TR/vocab-dcat-3/
PROV-O (W3C): https://www.w3.org/TR/prov-o/
STAC: https://stacspec.org/
~~~
