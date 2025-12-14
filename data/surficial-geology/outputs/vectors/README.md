---
title: "🧭 Surficial Geology — Vector Outputs"
path: "data/surficial-geology/outputs/vectors/README.md"

version: "v0.1.0"
last_updated: "2025-12-14"
release_stage: "Draft / In-Progress"
content_stability: "draft"

status: "Active"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"

scope:
  domain: "surficial-geology"
  applies_to:
    - "data/surficial-geology/outputs/vectors/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:outputs-vectors-readme:v0.1.0"
semantic_document_id: "surficial-geology-outputs-vectors-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:outputs-vectors-readme:v0.1.0"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-relationship-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🧭 **Surficial Geology — Vector Outputs**
`data/surficial-geology/outputs/vectors/README.md`

**Purpose**  
Define what belongs in `outputs/vectors/`, how vector deliverables are named/versioned, and how they are linked into **STAC/DCAT/PROV** for downstream ingestion (graph/API/UI).

</div>

---

## 📘 Overview

This folder contains the **vector distribution artifacts** for the Surficial Geology domain. Items here are:

- **Derived** (never the authoritative source of truth)
- **Deterministic** (re-creatable from tracked inputs + pinned config)
- **Distribution-ready** (usable by API consumers, analysts, and map tooling)

This folder is a child of `data/surficial-geology/outputs/`. If something here is wrong, fix the pipeline/config that generates it—do not patch files in-place.

---

## 🗂️ Directory Layout

~~~text
📁 vectors/                                      — Vector distributions (this directory)
├── 📄 README.md                                 — This file (rules + expectations)
├── 📄 surficial_geology_ks_v<ver>.gpkg           — Canonical vector export (GeoPackage)
├── 📄 surficial_geology_ks_v<ver>.geojson        — Interchange export (often simplified)
└── 📄 surficial_geology_ks_v<ver>.parquet        — Analytics export (GeoParquet; optional)
~~~

Notes:

- `<ver>` is the output version token chosen by the generating pipeline (e.g., `v2025.12.14` or `v0.3.0`).
- Checksums and broader sidecar metadata are maintained at `data/surficial-geology/outputs/` (see parent README).

---

## 🧭 Context

Vectors in this folder are the “human and system friendly” layer in the KFM data path:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

These vector exports typically serve three purposes:

1. **Canonical distribution** for users and analysts (GeoPackage / GeoParquet).
2. **Interchange** for lightweight tooling and simple integrations (GeoJSON).
3. **Catalog + provenance anchoring** so each distributed file is traceable to inputs and a build run.

---

## 📦 Data & Metadata

### Canonical formats

- **GeoPackage (`.gpkg`)** is the preferred canonical distribution format:
  - supports multiple layers
  - preserves geometry types and field types robustly
  - stable for long-term archiving and GIS tooling
- **GeoJSON (`.geojson`)** is for interoperability:
  - keep it small and predictable
  - prefer simplification and/or filtering for interchange
- **GeoParquet (`.parquet`)** is optional, for analytics:
  - must include GeoParquet-compatible metadata (geometry + CRS)
  - recommended only if produced deterministically by the pipeline

### Naming and versioning

- Use lowercase, underscore-separated stems: `surficial_geology_ks_*`.
- Every file name MUST include `_v<ver>`.
- Prefer **one** canonical file per format per version (avoid duplicates and ad-hoc suffixes).

### CRS and geometry expectations

- CRS MUST be explicitly recorded in the file (format-native where possible).
- Geometries MUST be valid and consistent with the layer’s contract.
- Avoid mixed geometry types in a single layer unless the contract explicitly allows it.

### Attribute schema and sidecars

Field definitions are governed outside this folder:

- `outputs/metadata/attributes.schema.json` is the authoritative field dictionary for distributions.
- `outputs/metadata/export.manifest.json` inventories distribution artifacts and build parameters.
- `outputs/checksums.sha256` MUST include hashes for committed files under `outputs/vectors/`.

Do not redefine schemas here—reference the domain’s `attributes.schema.json`.

### “Do not hand-edit” rule

If a vector export needs changes:

- update the deterministic pipeline (inputs/config/code)
- regenerate vectors
- regenerate checksums + provenance summaries
- update catalogs (STAC/DCAT) if asset lists/paths changed

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

Vector exports are referenced as STAC assets from the relevant Surficial Geology Item(s)/Collection(s) under `data/stac/`.

Recommended asset patterns:

~~~json
{
  "assets": {
    "vectors_gpkg": {
      "href": "data/surficial-geology/outputs/vectors/surficial_geology_ks_v<ver>.gpkg",
      "type": "application/geopackage+sqlite3",
      "roles": ["data"]
    },
    "vectors_geojson": {
      "href": "data/surficial-geology/outputs/vectors/surficial_geology_ks_v<ver>.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
~~~

(Exact asset keys and roles are governed by the producing pipeline and catalog conventions; keep them stable once published.)

### DCAT

Each file corresponds to a `dcat:Distribution` for the Surficial Geology `dcat:Dataset`, including:

- `dct:format` / `mediaType`
- license/rights from authoritative source manifests and catalog records (do not guess)

### PROV

- Each output file is a `prov:Entity`.
- Each generating run is a `prov:Activity`.
- Entities MUST link to the generating activity with `prov:wasGeneratedBy`, and back to inputs with `prov:wasDerivedFrom`.
- Run logs/config snapshots live under `mcp/runs/` and should be referenced by the PROV summary used by this dataset.

---

## 🧪 Validation & CI/CD

Minimum acceptance checks before committing vector outputs:

- **Checksums**: `outputs/checksums.sha256` updated and matches file contents.
- **Schema**: `outputs/metadata/attributes.schema.json` updated if fields changed.
- **Geometry**:
  - valid geometries
  - consistent CRS
  - spatial extent matches the domain contract (no “runaway” geometries)
- **Catalog integrity**:
  - STAC/DCAT references point to exact output paths and versions
  - PROV references the producing run and input entities
- **Governance scans**:
  - no secrets
  - no PII
  - no disallowed sensitive precision per sovereignty policy

---

## ⚖ FAIR+CARE & Governance

Even “public” geospatial layers can contribute to harmful inference when combined with other data. For any distribution:

- apply appropriate aggregation/generalization where required
- record any risk-mitigating decisions in catalogs (STAC/DCAT) and provenance (PROV)
- respect Indigenous data protection constraints and avoid releasing sensitive precision when flagged

See linked governance and sovereignty policies in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `outputs/vectors/` README defining vector deliverables, naming/versioning rules, and STAC/DCAT/PROV linkage expectations. |

---

<div align="center">

🧭 **Surficial Geology — Vector Outputs**  
KFM Data Layer · Vector Distributions · Provenance-First

[📘 Docs Root](../../../../docs/README.md) ·
[📂 Standards Index](../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

