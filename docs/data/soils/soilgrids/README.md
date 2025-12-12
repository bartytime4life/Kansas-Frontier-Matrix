---
title: "🌱 Kansas Frontier Matrix — SoilGrids 250 m Ingest & STAC Materialization Pipeline"
path: "docs/data/soils/soilgrids/README.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Soils & Land Systems Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Data Pipeline Specification"
intent: "soilgrids-global-soils-ingest"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "soils"
  applies_to:
    - "data/sources/soils/soilgrids/**"
    - "data/raw/soils/soilgrids/**"
    - "data/processed/soils/soilgrids/**"
    - "data/stac/soils/soilgrids/**"
    - "src/etl/soils/soilgrids/**"
    - "mcp/runs/**"

fair_category: "F4-A2-I2-R1"
care_label: "C2-A1-R1-E1"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "Soils & Land Systems Board"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:soils:soilgrids:pipeline:v11.2.6"
semantic_document_id: "kfm-doc-soils-soilgrids-pipeline"
event_source_id: "ledger:data/soils/soilgrids"
doc_integrity_checksum_algo: "sha256"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/data/soils/soilgrids/README.md@v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🌱 SoilGrids 250 m — Kansas Ingest & Catalog Pipeline
`docs/data/soils/soilgrids/README.md` · v11.2.6 · Stable / Governed

**Purpose**  
Deterministically ingest **ISRIC SoilGrids 250 m** products and materialize **Kansas-scoped**, provenance-complete derivatives (**COG + GeoParquet index + STAC/DCAT/PROV**) suitable for graph/API/Story Node integration.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/License-CC--BY_4.0-black" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

This document defines the canonical KFM pipeline for producing Kansas-scoped SoilGrids derivatives with complete lineage and catalog interoperability.

### Outputs (normative)

For each supported SoilGrids upstream release and each Kansas-scoped product variant, the pipeline MUST emit:

- **COG raster(s)** (Kansas-clipped) with deterministic build settings.
- **GeoParquet index** for discovery/filtering (footprints + key properties).
- **STAC Collection + Items** with stable IDs and resolvable asset links.
- **DCAT mirror** sufficient for external catalog interoperability.
- **PROV-O lineage** linking raw → subset/warp → COG → index → publish.

### Non-negotiable rules

- Source assets are **never mutated**; all KFM outputs are derived artifacts.
- Every step is **config-driven, replayable, idempotent**, and checksum-addressable.
- SoilGrids products are **predictions**; outputs MUST preserve uncertainty semantics and MUST NOT be described as direct measurements.

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 data/
    └── 📁 soils/
        └── 📁 soilgrids/
            └── 📄 README.md                          🌱 This pipeline spec

data/
├── 📁 sources/
│   └── 📁 soils/
│       └── 📁 soilgrids/
│           ├── 📄 source.manifest.yaml               📜 Source manifest (uri/license/retrieval/checksums)
│           ├── 📄 access_policy.yaml                 ⚖️ Restrictions / stewardship notes (if any)
│           └── 📁 upstream_metadata/                 🧾 Immutable upstream metadata snapshots
│
├── 📁 raw/
│   └── 📁 soils/
│       └── 📁 soilgrids/
│           └── 📁 <upstream_version>/                🌍 Raw references or downloaded assets (immutable)
│
├── 📁 processed/
│   └── 📁 soils/
│       └── 📁 soilgrids/
│           └── 📁 <upstream_version>/
│               ├── 📁 kansas/                        🗺️ Kansas-scoped COG derivatives
│               └── 📁 indices/                       🧩 GeoParquet indices + sidecars
│
└── 📁 stac/
    └── 📁 soils/
        └── 📁 soilgrids/
            └── 📁 <upstream_version>/                🛰️ STAC Collections + Items (published artifacts)

src/
└── 📁 etl/
    └── 📁 soils/
        └── 📁 soilgrids/
            ├── 📄 pipeline.py                        🧰 Deterministic orchestrator
            ├── 📄 config.schema.json                 ✅ Config schema (version-pinned)
            ├── 📁 configs/                           🧾 Replay configs (inputs/options/boundaries)
            └── 📁 validators/                        🔍 COG/STAC/DCAT/PROV validation hooks

mcp/
└── 📁 runs/
    └── 📁 soils_soilgrids/
        └── 📁 <run_id>/                              🧪 Logs + config snapshot + checksums + reports
~~~

---

## 🧭 Context

### Authoritative source

- **Producer**: ISRIC – World Soil Information
- **Product**: SoilGrids (250 m) global soil property predictions
- **License**: CC-BY 4.0 (attribution REQUIRED)

### Access modes (common upstream patterns)

- Web Coverage Service (WCS) for spatial subsetting (where available)
- Bulk raster access (e.g., WebDAV / published file listings / VRT manifests)
- Google Earth Engine collection access (where policy permits)

### Interpretation guardrail

SoilGrids layers are **modeled predictions**. Downstream use MUST preserve:

- modeling nature (predictions, not samples),
- uncertainty/quantiles where provided,
- provenance to upstream release and KFM processing activities.

---

## 🧱 Architecture

### Pipeline placement

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph/API → Story Nodes.

### Determinism contract (normative)

A run MUST be reproducible from:

- versioned config (stored with the run),
- pinned toolchain versions,
- recorded source URIs + checksums,
- recorded Kansas boundary asset identifier + checksum,
- stable output naming (derived from config + upstream version + product keys).

### Canonical stages

1. **Source registration**
   - write `data/sources/soils/soilgrids/source.manifest.yaml`
   - capture upstream metadata snapshot (no edits)

2. **Acquire**
   - WCS subset request definition OR immutable raw download reference
   - record retrieval date and checksums (where materialized)

3. **Normalize**
   - CRS/tiling/nodata normalization per config (only if required)

4. **Kansas scoping**
   - clip/mask to governed Kansas boundary geometry
   - preserve boundary reference in metadata + provenance

5. **Materialize**
   - generate Kansas-scoped COG(s)
   - generate GeoParquet index artifacts

6. **Validate**
   - COG validation + schema checks
   - STAC validation + link resolution
   - PROV validation (no dangling references)

7. **Publish**
   - STAC Collection + Item emission
   - DCAT mirror (native or mapped)

---

## 📦 Data & Metadata

### Kansas scoping boundary (normative)

The Kansas boundary used for clipping MUST be:

- versioned and governed,
- referenced in run config,
- linked in PROV via `prov:used`,
- represented in STAC properties as processing context.

### GeoParquet index minimum schema

~~~yaml
columns:
  asset_id: string
  stac_item_id: string
  upstream_version: string
  property: string
  depth_interval: string|null
  statistic: string|null
  units: string|null
  crs: string
  bbox: struct
  href: string
  checksum_sha256: string
  nodata: number|null
  created_at: string
  run_id: string
~~~

### COG requirements (normative)

COG creation MUST:

- preserve nodata semantics,
- embed overviews where configured,
- record checksum and key raster metadata as STAC asset fields or sidecars.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (normative)

This pipeline MUST publish:

- **1+ STAC Collections** per upstream release (and/or product family)
- **STAC Items** representing Kansas-scoped raster products

Each Item MUST include:

- `geometry`/`bbox` for Kansas-scoped footprint
- stable `id` and consistent item naming policy
- `assets` including:
  - `cog` (Kansas-scoped raster)
  - `index` (GeoParquet index, item-level or collection-level policy)
  - `metadata` (optional upstream snapshot reference)
  - `prov` (PROV bundle reference)

### DCAT (minimum)

- Collection-level records SHOULD be representable as `dcat:Dataset`
- Distributions SHOULD describe each downloadable artifact (COG, index, provenance)

### PROV-O (normative)

Every published Item MUST be traceable via:

- `prov:Entity` for raw source, intermediate (if any), COG, index, STAC JSON
- `prov:Activity` for acquire, normalize, clip, build, validate, publish
- `prov:Agent` for ISRIC (source), KFM pipeline runner, stewarding boards (when attested)

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Upstream SoilGrids release"] --> B["Source manifest + metadata snapshot"]
  B --> C["Acquire: WCS subset OR immutable raw reference"]
  C --> D["Normalize: CRS/tiling/nodata (config)"]
  D --> E["Subset: Kansas boundary clip/mask"]
  E --> F["Materialize: COG derivatives"]
  F --> G["Build: GeoParquet index"]
  G --> H["Validate: COG + STAC + PROV"]
  H --> I["Publish: STAC Collection + Items + DCAT mirror"]
~~~

This flow is deterministic: each stage is config-driven and emits provenance that links inputs to outputs.

---

## 🧠 Story Node & Focus Mode Integration

This pipeline enables Story Nodes that reference SoilGrids-derived evidence layers, such as:

- soil carbon and productivity context in agronomy narratives,
- erosion susceptibility context for hydrology and land-use change,
- environmental baselines for archaeology and settlement interpretation.

Rules:

- Story Nodes MUST reference cataloged STAC Items (no ad-hoc files).
- Narrative MUST clearly label SoilGrids as modeled predictions with limits and uncertainty.

---

## 🧪 Validation & CI/CD

A run is not publishable unless all checks pass:

- source manifest validation (license, retrieval date, checksums, access policy)
- COG validation (format, tiling/overviews policy, bounds/nodata readability)
- GeoParquet validation (schema + spatial footprint fields + checksums)
- STAC validation (conformance + resolvable assets + geometry/bbox consistency)
- PROV validation (no dangling references; required entities/activities/agents)

Common failure causes:

- missing `~~~text` fencing for directory layouts
- unapproved H2 headings (emoji/text mismatch)
- missing required front-matter keys (IDs, governance refs, provenance chain)
- mixed fence styles (backticks inside committed docs)

---

## ⚖ FAIR+CARE & Governance

- FAIR: stable identifiers, catalog records, and provenance are required for reuse.
- CARE: sovereignty and harm minimization apply when combining soils layers with sensitive overlays.
- Prohibited uses include individual-level inference or de-masking restricted overlays.

Binding references:

- Governance: `governance_ref`
- Ethics: `ethics_ref`
- Sovereignty: `sovereignty_policy`

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| v11.2.6 | 2025-12-12 | Applied KFM-MDP v11.2.6 requirements: added release-pinned provenance refs, ensured approved H2 set, enforced tilde-only internal fencing, and standardized purpose + footer governance links. |

---

<div align="center">

**Docs Root** · [📑 Standards Index](../../../standards/README.md) · [🔁 Workflows](../../../workflows/README.md)

[⚖️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🧬 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix · CC-BY 4.0

</div>
