---
title: "📊 KFM v11.2.2 — Annual & Incremental Data Update Reports (Soils · DEM · Hydrology · Terrain · AI Layers)"
path: "docs/data/updates/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Annual Data Refresh System"
review_cycle: "Annual · FAIR+CARE Council · Data Integrity Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../releases/v11.2.2/slsa-attestation.json"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/data-updates-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-updates-v11.2.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Domain Overview"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "data-updates"
  applies_to:
    - "annual-diffs"
    - "incremental-diffs"
    - "soil"
    - "dem"
    - "hydrology"
    - "terrain"
    - "ai-layers"
    - "stac-update-sets"

semantic_intent:
  - "annual-diff"
  - "structural-refresh"
  - "metadata-diff"
  - "lineage-governance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Environmental"
sensitivity_level: "None"
public_exposure_risk: "Low"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "ISO-19115"
  - "FAIR+CARE"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:data:updates:index:v11.2.2"
semantic_document_id: "kfm-data-updates-index-v11.2.2"
event_source_id: "ledger:data-updates-index-v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 📊 **KFM v11.2.2 — Annual & Incremental Data Update Reports**  
`docs/data/updates/README.md`

**Purpose:**  
Provide the unified index for all **annual** and **incremental** statewide data difference (diff) reports within the Kansas Frontier Matrix.  
These diffs summarize year-to-year changes in **soils**, **DEM/terrain**, **hydrology**, **erosion/sediment models**, **AI affordance layers**, and related geospatial products.  
Each diff is STAC-registered, lineage-tracked, and provides mandatory rebuild signals for downstream pipelines.

</div>

---

## 📘 Overview

The **Data Updates Domain** exists to ensure that KFM remains synchronized with:

- **USDA NRCS annual soil releases** (SSURGO / gNATSGO)  
- **USGS 3DEP lidar & DEM updates**  
- **NHDPlusHR hydrography refreshes**  
- **NOAA/NASA environmental indices**  
- **Terrain derivative changes** (slope, aspect, roughness, etc.)  
- **AI environmental-affordance layers** derived from DEM + soils  
- **Cross-domain structural shifts** affecting Story Nodes or Focus Mode interpretations  

Each update cycle produces:

1. **Diff Report** — Changes between last and current year  
2. **STAC Diff Manifest** — Machine-readable change set  
3. **Pipeline Impact Summary** — Tiered rebuild requirements  
4. **Lineage Ledger Entry** — Provenance for all changed assets  
5. **Telemetry Record** — Metrics for drift, update volume, carbon/energy footprint  

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 data/
    └── 📁 updates/
        ├── 📄 README.md                         # This file (index)
        ├── 📄 kansas-2024-2025-diff.md          # Current annual diff report
        ├── 📄 2023-2024-diff.md                 # Previous annual cycle
        └── 📁 stac/                             # Optional doc-local copies/pointers for diff STAC records
            ├── 📄 kansas-2024-2025-diff.json
            └── 📄 2023-2024-diff.json
~~~

> **Normative:** Authoritative STAC Items for update diffs MUST live under `data/stac/` (per KFM-STAC v11);  
> this directory MAY include convenience copies or pointers for documentation browsing.

---

## 🧭 Context

### 🟦 Annual Structural Updates (Tier-1)

Triggered by major upstream data releases:

- SDA / gNATSGO  
- 3DEP DEM  
- Hydrology (NHDPlusHR)  
- Terrain derivations  
- Ecosystem or geomorphological updates  
- Heritage landscape interactions (if DEM-driven)  

Require **mandatory pipeline rebuilds**.

### 🟧 Incremental Updates (Tier-2)

Smaller diffs driven by:

- Replacement tiles  
- Minor attribute/table changes  
- Local hydrology fixes  
- AI feature-space refinements  
- Minor erosion/sediment predictor updates  

Optionally trigger downstream rebuilds depending on impact level.

### 🟩 Metadata-Only Updates (Tier-3)

Updates to:

- STAC metadata  
- Provenance chains  
- License updates  
- Contact or distribution info  
- Minor schema updates  

Do **not** require ETL rebuilds.

---

## 📦 Data & Metadata

Diff reports and their companion artifacts MUST capture (at minimum):

- **Diff period** (e.g., `2024–2025`)  
- **Changed assets** (datasets, tables, rasters, tiles, collections)  
- **Changed tiles** (where tiling is used; tile identifiers preferred over raw coordinate dumps)  
- **Impact tier** (Tier-1 / Tier-2 / Tier-3)  
- **Downstream dependency signals** (what pipelines must rebuild vs may rebuild)  
- **Checksums / hashes** for changed assets (multihash where supported)  

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

Every annual diff MUST:

- Publish a STAC Item under:  
  `data/stac/data-updates/<year-range>.json`
- Include:
  - `properties.diff_period`
  - `properties.changed_assets`
  - `properties.changed_tiles`
  - `kfm:impact_level` (Tier-1 / Tier-2 / Tier-3)

### DCAT

Each diff MUST be registered under the **DCAT Dataset Catalog** as a discoverable record, with:

- `dct:title`, `dct:description`, `dct:license`  
- Publisher/creator fields as appropriate  
- Linkage to the diff STAC Item and to impacted upstream datasets  

### PROV-O

Each diff MUST emit a provenance trace that links:

- Raw upstream releases → processed assets  
- The diff activity (annual or incremental) → the generated diff artifacts  
- The agent(s) responsible (scripts, CI bots, councils, maintainers)  

---

## 🧱 Architecture

Diff reports propagate rebuild signals to (examples):

- `soil-index/`  
- `soil-terrain/`  
- `hydrology/`  
- `dem/` and all derivatives  
- `ai/interpretations/environmental-affordances/`  
- `archaeology/settlement-morphology/`  
- `climate/derived-layers/`  

Pipelines consume:

- **Impact level**  
- **Changed tiles**  
- **Changed attributes**  
- **Dependency DAG** (auto-generated)  

---

## 🧪 Validation & CI/CD

Annual CI SHOULD include:

- Hash diffs of SDA + gNATSGO tiles  
- Tile inventory diffs for 3DEP DEM  
- Hydrology reburn audits  
- DEM derivation validity checks  
- Metadata drift detection  
- Telemetry ingestion (energy/carbon metrics)  
- KFM Lineage Ledger entry creation  

Failures SHOULD generate:

- `alerts/data-integrity/` tickets  
- OpenTelemetry error spans  
- Auto-mitigation or fallback to previous release  

---

## 🧠 Story Node & Focus Mode Integration

Annual diffs automatically update:

- **Environmental affordance Story Nodes**  
- **Hydrology-linked narratives**  
- **Terrain/soil interactions** shown in Focus Mode  
- **Archaeological landscape interpretations**  

Focus Mode v3 uses:

- `changed_tiles`  
- `changed_attributes`  
- `geomorphology updates`  
- `DEM visibility/relief changes`  

This ensures narrative accuracy across time.

---

## ⚖ FAIR+CARE & Governance

Telemetry and diff summaries MUST NOT include:

- Raw coordinates of sensitive sites beyond what is allowed in governed STAC outputs  
- Any non-governed or internal STAC drafts not intended for publication  
- PII/PHI or credential/secrets material  

Where necessary, summary metrics SHOULD be aggregated (e.g., counts per collection) rather than per-feature details.

All update reporting MUST remain consistent with:

- FAIR+CARE guidance (`ethics_ref`)  
- Governance baseline (`governance_ref`)  
- Sovereignty and masking constraints (`sovereignty_policy`)  

---

## 🕰️ Version History

| Version | Date       | Notes                                              |
|--------:|------------|----------------------------------------------------|
| v11.2.2 | 2025-11-28 | Converted to v11.2.2; emoji tree; metadata uplift  |
| v11.0.0 | 2025-11-28 | Initial domain introduction                        |

---

<div align="center">

### 🔗 Footer  
[🌐 KFM Home](../../../README.md) · [📚 Standards](../../standards/README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md) · [📦 STAC Catalog](../../../data/stac/)

</div>
