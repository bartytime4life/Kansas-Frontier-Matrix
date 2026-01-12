---
title: "DCAT Schemas (API Contracts)"
path: "api/contracts/schemas/dcat/README.md"
status: "active"
last_updated: "2026-01-12"
---

# 🗂️ DCAT Schemas (API Contracts)

![contract-first](https://img.shields.io/badge/contract--first-yes-2ea44f)
![standard](https://img.shields.io/badge/standard-DCAT-blue)
![format](https://img.shields.io/badge/format-JSON--LD-0b7285)
![schema](https://img.shields.io/badge/spec-JSON%20Schema-orange)
![catalogs](https://img.shields.io/badge/catalogs-STAC%20%2B%20DCAT%20%2B%20PROV-6f42c1)
![ci](https://img.shields.io/badge/CI-catalog%20QA%20gate-critical)

High-level, **contract-first** JSON Schemas for KFM’s **DCAT discovery layer**. DCAT is the “front door” for finding datasets (including AI-derived evidence artifacts), and it must stay **in sync** with STAC (assets) + PROV (lineage) + API contracts. 🧭

> [!IMPORTANT]
> This folder is **contracts/schemas** (rules).  
> **Actual DCAT outputs** live under `data/catalog/dcat/` and are produced via the ETL → catalogs pipeline.

---

## 🔗 Quick links

- 📘 **Normative profile (source of truth):** `docs/standards/KFM_DCAT_PROFILE.md`
- 🧱 **System pipeline + contract rules:** `docs/MASTER_GUIDE_v13.md`
- 🧪 **Catalog QA tooling:** `tools/validation/catalog_qa/`
- 🗃️ **Generated DCAT catalogs:** `data/catalog/dcat/`
- 🛰️ **STAC catalogs:** `data/stac/`
- 🧬 **PROV bundles:** `data/prov/`

> [!NOTE]
> In the v13 structure, the repo’s canonical schema home is `schemas/dcat/`.  
> If your build treats `api/contracts/schemas/dcat/` as a mirror for API packaging, keep it **byte-for-byte in sync** (symlink or copy step) to avoid schema drift. ✅

---

## 🧭 Where DCAT fits in KFM

KFM uses open standards so external tools can discover + consume data with minimal friction: **GeoJSON**, **COG**, **STAC**, **DCAT**, **PROV**, and governed **REST/OpenAPI + GraphQL** APIs. 🌍

### 🧩 Layer responsibilities (mental model)

| Layer | Standard / Artifact | Answers | Lives (canonical) |
|---|---|---|---|
| Discovery | **DCAT** (Dataset + Distributions) | “What datasets exist? Where do I get them?” | `data/catalog/dcat/` |
| Geospatial assets | **STAC** (Collections + Items) | “What are the spatial/temporal extents + assets?” | `data/stac/` |
| Lineage & reproducibility | **PROV-O** (activities/entities/agents) | “How was it produced? From what inputs? With what params?” | `data/prov/` |
| Relationships | **Neo4j graph** | “How does it connect to people/places/events?” | `src/graph/` + `data/graph/` exports |
| Access & governance | **API contracts** | “What can the UI/clients request + receive?” | `src/server/contracts/` (and/or `api/contracts/`) |
| Narrative | **Story Nodes + Focus Mode** | “What claims do we present (traceable)?” | `docs/reports/story_nodes/` |

### 🧱 Non‑negotiable ordering (contract enforcement)

```mermaid
flowchart LR
  A[🛰️ ETL pipelines] --> B[🗂️ STAC/DCAT/PROV catalogs]
  B --> C[🧠 Neo4j graph]
  C --> D[🔌 Contracted APIs (REST/GraphQL)]
  D --> E[🗺️ UI (React/Map)]
  E --> F[📝 Story Nodes]
  F --> G[🎯 Focus Mode]
```

> [!WARNING]
> No stage may **leapfrog** a prior stage’s contracts/outputs.  
> If something shows up in the UI, it must be reachable via the **API** (with redaction/classification rules), and traceable to **catalog + provenance**. 🧾

---

## 📁 What lives in this folder

> Adjust filenames below to match the actual schema files in this directory.

```text
📁 api/contracts/schemas/dcat/
├── 📄 README.md
├── 📄 catalog.schema.json            # dcat:Catalog (+ datasets)
├── 📄 dataset.schema.json            # dcat:Dataset (KFM profile)
├── 📄 distribution.schema.json       # dcat:Distribution (KFM profile)
├── 📄 agent.schema.json              # prov:Agent / publisher (if modeled)
├── 📄 common.schema.json             # shared defs: identifiers, links, enums
└── 📄 contexts/                      # optional JSON-LD context helpers
```

### ✅ Contract scope

These schemas are intended to validate **KFM-shaped DCAT JSON‑LD**, not the entire DCAT universe.

- ✅ Enforce **minimum required discovery fields** (title/description/license/keywords/distributions)
- ✅ Enforce **cross-layer linkage** (DCAT → STAC, DCAT → data assets, DCAT ↔ PROV)
- ✅ Enforce **identifier + versioning invariants**
- ✅ Support **governance metadata** (access rights, sensitivity/classification, redaction-aware distributions)
- ✅ Provide stable footing for **OpenAPI/GraphQL** payload contracts

---

## 📌 KFM DCAT invariants

### 1) Minimum required fields (baseline) 🧱

Every `dcat:Dataset` **must** include at least:

- `dct:title`
- `dct:description`
- `dct:license`
- `dcat:keyword` (non-empty list)
- `dcat:distribution` (non-empty list with working links)

> [!TIP]
> Treat DCAT as **human-friendly discovery** + **machine-harvestable index**.  
> Deep geospatial detail belongs in **STAC**, not DCAT. 🛰️

### 2) Distribution rules (DCAT → the goods) 📦

Each `dcat:Distribution` should:

- Provide **exactly one** primary retrieval link:
  - `dcat:downloadURL` (direct file)
  - `dcat:accessURL` (service endpoint / landing page / STAC entry)
- Declare a `dcat:mediaType` (examples: `application/geo+json`, `image/tiff`, `text/csv`, `application/json`)
- Prefer stable, versioned URLs/paths (avoid “latest” without versioning)

KFM expectation: **at least one distribution points to STAC** (Collection/Item) *or* to a stable data endpoint. 🔗

### 3) Provenance linkage (DCAT ↔ PROV) 🧬

DCAT records must link to provenance so datasets are reproducible and auditable:

- Use `prov:wasGeneratedBy` and/or `dct:provenance` to point to a PROV activity/bundle
- The referenced PROV should identify:
  - raw inputs → work intermediates → processed outputs
  - pipeline run identifier and/or commit hash
  - parameters/config that produced the output
  - responsible agents (human and/or software), timestamps, confidence metrics where applicable

### 4) Versioning + identifiers 🏷️

KFM is versioned at the dataset level and system level. For dataset identifiers:

- Prefer deterministic IDs (example pattern): `kfm.<region>.<domain>.<dataset>.<year_range>.v<major>`
- When a dataset is updated:
  - increment dataset version
  - link previous version using `prov:wasRevisionOf` (or an equivalent profile field)

---

## 🧩 KFM profile extensions (beyond base DCAT)

KFM extends base standards via `docs/standards/KFM_DCAT_PROFILE.md` to include project-specific fields, such as:

- 🔁 **Provenance pointers** (easy join with PROV bundles)
- 🎯 **Uncertainty / confidence indicators** for derived outputs (especially AI/ML or modeled layers)
- 🔐 **Access rights & sensitivity classification** to support redaction and sovereignty rules
- 🧭 **STAC pointers** for geospatial asset detail

> [!NOTE]
> If you need new metadata fields for a domain, **extend the profile + schema** rather than adding ad‑hoc keys. This keeps the catalogs harvestable and the APIs stable. ✅

---

## 🧪 Validation (local + CI)

KFM treats metadata like code: **no dataset is accepted without valid catalogs**. ✅

### A) Catalog QA tool (recommended) 🛠️

Use the repo’s catalog QA tooling to scan for:
- missing required fields
- broken links
- invalid/unknown licenses
- cross-link inconsistencies (DCAT ↔ STAC ↔ PROV)

➡️ See: `tools/validation/catalog_qa/`

### B) JSON Schema validation (example commands) ✅

> Replace filenames/paths based on your repo tooling.

**AJV (Node)**
```bash
npx ajv-cli validate \
  -s api/contracts/schemas/dcat/dataset.schema.json \
  -d data/catalog/dcat/**/*.jsonld \
  --all-errors
```

**Python**
```bash
python -m jsonschema \
  -i data/catalog/dcat/example.dataset.jsonld \
  api/contracts/schemas/dcat/dataset.schema.json
```

> [!IMPORTANT]
> CI is expected to run schema validation + link checks as a **required gate**. If you change schemas, add/adjust contract tests accordingly. 🧪

---

## 🧾 Examples (KFM-shaped DCAT JSON‑LD)

<details>
<summary><strong>📄 Example: dcat:Dataset (with STAC + PROV links)</strong></summary>

```json
{
  "@context": [
    "https://www.w3.org/ns/dcat.jsonld",
    {
      "dct": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "kfm": "https://kfm.example/ns#"
    }
  ],
  "@id": "urn:kfm:dataset:kfm.ks.hydrology.stream_gauges.1880-2020.v1",
  "@type": "dcat:Dataset",

  "dct:title": "Kansas Stream Gauge Observations (1880–2020)",
  "dct:description": "Cleaned, standardized stream gauge observations compiled from historical and modern sources. See STAC for spatial coverage and assets.",
  "dct:license": { "@id": "https://spdx.org/licenses/CC-BY-4.0" },

  "dcat:keyword": ["kansas", "hydrology", "stream gauges"],
  "dct:spatial": "Kansas, USA",
  "dct:temporal": "1880-01-01/2020-12-31",

  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "STAC Collection",
      "dcat:mediaType": "application/json",
      "dcat:accessURL": { "@id": "data/stac/collections/stream-gauges/collection.json" }
    },
    {
      "@type": "dcat:Distribution",
      "dct:title": "Processed CSV",
      "dcat:mediaType": "text/csv",
      "dcat:downloadURL": { "@id": "data/processed/hydrology/stream_gauges/stream_gauges.csv" }
    }
  ],

  "prov:wasGeneratedBy": { "@id": "data/prov/hydrology/stream_gauges/prov.jsonld" },
  "prov:wasRevisionOf": { "@id": "urn:kfm:dataset:kfm.ks.hydrology.stream_gauges.1880-2020.v0" },

  "kfm:uncertainty": {
    "method": "sensor_error_model_v2",
    "confidence": 0.93
  },
  "kfm:access": {
    "classification": "public",
    "notes": "If sensitive, distributions may be redacted or generalized by API policy."
  }
}
```
</details>

<details>
<summary><strong>📚 Example: dcat:Catalog (dataset index)</strong></summary>

```json
{
  "@context": [
    "https://www.w3.org/ns/dcat.jsonld",
    {
      "dct": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "urn:kfm:catalog:main",
  "@type": "dcat:Catalog",

  "dct:title": "Kansas Frontier Matrix — Dataset Catalog",
  "dct:description": "Discovery catalog for KFM datasets. Use STAC for asset-level metadata; use PROV for lineage.",
  "dcat:dataset": [
    { "@id": "urn:kfm:dataset:kfm.ks.hydrology.stream_gauges.1880-2020.v1" },
    { "@id": "urn:kfm:dataset:kfm.ks.historical.land_treaties.1800-1900.v2" }
  ]
}
```
</details>

---

## 🧱 How to extend or change these schemas

When adding/changing DCAT metadata fields, follow the contract-first workflow:

1. 📘 Update the normative profile: `docs/standards/KFM_DCAT_PROFILE.md`
2. 🧩 Update JSON Schemas in this folder (and/or canonical `schemas/dcat/`)
3. 🧪 Add/adjust validation + contract tests (`tests/` and/or `tools/validation/catalog_qa/`)
4. 🔌 If an API payload changes, update OpenAPI/GraphQL contracts (contract first!)  
5. 🏷️ Bump versions + document breaking changes (`CHANGELOG.md`, release notes)

> [!WARNING]
> Breaking schema changes must coordinate with API/UI consumers (or introduce a versioned endpoint / negotiation strategy). Contracts are promises. 🤝

---

## 🔐 Governance & safety notes

- **Sovereignty & sensitivity:** metadata must not leak restricted details; access rights/classification must be explicit.
- **Redaction-aware distributions:** restricted datasets may appear in DCAT for discovery, but distribution links may be omitted, gated, or generalized.
- **UI safety:** treat title/description/keywords as untrusted input; avoid rendering raw HTML without sanitization. 🧼

---

## ❓ FAQ

**Why DCAT if we already have STAC?**  
DCAT is the **catalog of datasets** (discovery + harvesting). STAC is the **catalog of assets** (geospatial metadata + files/services). They complement each other. 🧩

**Where do the real catalogs live?**  
Generated DCAT JSON‑LD lives under `data/catalog/dcat/`. This folder is schema/contracts for validation and API guarantees. 🗃️

**Do AI/ML artifacts need DCAT too?**  
Yes. Treat derived artifacts like any dataset: store under `data/processed/`, create STAC/DCAT entries, and capture lineage in PROV (including parameters + confidence metrics). 🤖🧾

---

## 📚 References (standards)

- DCAT (W3C Data Catalog Vocabulary): https://www.w3.org/TR/vocab-dcat/
- PROV-O (W3C Provenance Ontology): https://www.w3.org/TR/prov-o/
- STAC (SpatioTemporal Asset Catalog): https://stacspec.org/
