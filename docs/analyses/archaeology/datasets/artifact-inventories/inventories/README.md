---
title: "🏺 Kansas Frontier Matrix — Artifact Inventory Files (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/inventories/README.md"
description: "Canonical, cleaned, culturally-reviewed artifact inventory tables for KFM v11 archaeology analyses."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventory-files-v11.2.3"
doc_kind: "Dataset Subcategory"
intent: "artifact-inventory-files"
semantic_document_id: "kfm-doc-archaeology-artifact-inventory-files-v11.2.3"
category: "Analyses · Archaeology · Artifact Inventories"

sbom_ref: "releases/v11.2.3/sbom.spdx.json"
manifest_ref: "releases/v11.2.3/manifest.zip"
telemetry_ref: "releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/archaeology-artifact-inventory-files-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Cultural / Archaeological / Heritage"
sensitivity_level: "High"
indigenous_rights_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
immutability_status: "version-pinned"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Archaeology Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/inventories/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Artifact Inventory Files (v11)**  

`docs/analyses/archaeology/datasets/artifact-inventories/inventories/README.md`

**Purpose**  
Serve as the **canonical index** for **cleaned, normalized, culturally-reviewed** artifact inventory tables that power archaeological analysis, mapping, cultural-phase timelines, and AI-assisted narratives within the Kansas Frontier Matrix (KFM).

</div>

---

## 🗂️ Directory Layout

```text
KansasFrontierMatrix/
├── 📁 docs/
│   └── 📁 analyses/
│       └── 📁 archaeology/
│           └── 📁 datasets/
│               └── 📁 artifact-inventories/
│                   └── 📁 inventories/
│                       📄 README.md                       # ← This file (index)
│                       📄 flint-hills-lithics-v11.csv     # Cleaned lithic inventory (generalized, PD/open-license)
│                       📄 prairie-ceramics-v11.csv        # Ceramic types + motifs (motifs generalized)
│                       📄 contact-era-metals-v11.csv      # Protohistoric metal artifacts (governed, tribal review)
│                       📄 fauna-open-v11.csv              # Faunal dataset (public-domain oriented, filtered)
│                       …                                  # Additional curated inventory tables
├── 📁 data/
│   └── 📁 analyses/
│       └── 📁 archaeology/
│           └── 📁 artifact-inventories/
│               ├── 📁 inventories-raw/                    # Source inventories pre-cleaning (restricted)
│               └── 📁 inventories-cleaned/                # Materialized cleaned tables (mirrors this index)
└── 📁 metadata/
    └── 📁 archaeology/
        └── 📁 artifact-inventories/
            ├── 📁 stac/
            │   └── 📄 flint-hills-lithics-v11.item.json
            ├── 📁 dcat/
            │   └── 📄 flint-hills-lithics-v11.dcat.json
            └── 📁 provenance/
                └── 📄 flint-hills-lithics-v11.prov.json
```

File naming in this directory MUST align with:

- Metadata entries in `metadata/archaeology/artifact-inventories/**`  
- STAC Items in `metadata/.../stac/`  
- Provenance logs in `metadata/.../provenance/`

---

## 📘 Overview

Files in this directory are **processed artifact inventories** that have been:

- Cleaned and schema-normalized to KFM archaeology standards,  
- Culturally reviewed and CARE-tagged,  
- Spatially generalized using H3 (no site-level coordinates),  
- Linked to:
  - A STAC Item in `metadata/archaeology/artifact-inventories/stac/`,  
  - A DCAT record in `metadata/archaeology/artifact-inventories/dcat/`,  
  - A PROV-O provenance log in `metadata/archaeology/artifact-inventories/provenance/`.

These tables are the **final validated artifact inventories** used for:

- Neo4j knowledge graph ingestion,  
- Story Node creation and updates,  
- Focus Mode v3 material-culture explanations,  
- Archaeological pattern modeling and phase reconstructions,  
- MapLibre / Cesium layers (H3-based density and distribution maps),  
- Cross-dataset joins (stratigraphy, paleoenvironment, cultural landscapes, archives).

Only datasets that are:

- **Open-license or clearly specified license**,  
- **FAIR+CARE-approved**, and  
- **Sovereignty-governed**  

may be stored here.

Prohibited content in these inventories:

- Human remains or funerary items,  
- Sacred or ceremonial items, or restricted regalia,  
- Unprovenanced or illicitly obtained artifacts,  
- Exact coordinates, excavation units, or protected-site identifiers,  
- Any descriptors that violate sovereignty or CARE constraints.

All spatial references MUST be generalized using **H3** (typical levels r5–r7) or coarser representations, per sovereignty and CARE guidance.

---

## 📋 Required Schema (All Inventory Tables)

Every inventory file in this directory MUST conform to the standardized schema below.  
Fields may be extended, but required columns MUST NOT be removed or renamed without governance review.

| Field                  | Description                                                       | Required |
|------------------------|-------------------------------------------------------------------|----------|
| `artifact_id`          | UUID or stable ID for each artifact record                       | ✔        |
| `material`             | Material descriptor (e.g., lithic/ceramic/metal/bone)            | ✔        |
| `artifact_type`        | Standardized artifact classification term                        | ✔        |
| `culture_phase`        | Cultural-phase label (e.g., `Late Prehistoric`)                  | ✔        |
| `dating_method`        | Basis for dating (typology, layer, radiocarbon, etc.)           | ✔        |
| `temporal_range_start` | Start of time range (ISO 8601 or normalized textual interval)    | ✔        |
| `temporal_range_end`   | End of time range (ISO 8601 or normalized textual interval)      | ✔        |
| `location_h3`          | H3 index (level 5–7 or coarser where required)                   | ✔        |
| `site_class`           | Generalized site category (e.g., village/camp/other/unknown)     | ✔        |
| `quantity`             | Count or measurement for this artifact entry                     | ✔        |
| `description`          | Neutral, culturally safe description                             | ✔        |
| `source`               | Repository or dataset source reference                           | ✔        |
| `provenance_file`      | Relative path to PROV-O JSON for this inventory                  | ✔        |

**Forbidden fields (MUST NOT appear):**

- Exact latitude/longitude or UTM/easting/northing fields,  
- Excavation unit codes, feature IDs, structure numbers tied to sensitive sites,  
- Personally identifiable information (names, addresses, etc.),  
- Free-text provenience notes tied to protected or confidential locations,  
- Internal collection identifiers that violate repository or Tribal policy.

If such fields exist in the source, they MUST be stripped, generalized, or separated into a restricted storage location before data enters this directory.

---

## 🧭 Dataset Inventory Index (Illustrative)

> The authoritative inventory index is derived automatically from directory contents + STAC/DCAT/PROV metadata.  
> The table below is illustrative, not normative.

| Dataset                      | Category             | Status   | Last Review | Notes                                                   |
|-----------------------------|----------------------|----------|-------------|---------------------------------------------------------|
| `flint-hills-lithics-v11.csv`   | Lithics              | 🟢 Active | 2025-11     | PD/open, generalized via H3; CARE review completed.     |
| `prairie-ceramics-v11.csv`      | Ceramics             | 🟢 Active | 2025-11     | Motif categories generalized; CARE notes in provenance. |
| `contact-era-metals-v11.csv`    | Protohistoric Metals | 🟡 Review | 2025-09     | Tribal review in progress; restricted-generalized.      |
| `fauna-open-v11.csv`            | Faunal (PD-oriented) | 🟢 Active | 2025-11     | Sacred species and sensitive contexts removed.          |

---

## 🧪 Data Quality & Validation Requirements

Each inventory table MUST pass three layers of validation:

### 1️⃣ Scientific & Structural Validation

- **Schema adherence**  
  - All required columns present and correctly typed.  
- **Classification checks**  
  - `artifact_type` values align with controlled vocabularies.  
  - `material` values map correctly to `kfm:material_class` or equivalent ontology terms.  
- **Internal consistency**  
  - Temporal ranges are logically ordered (`temporal_range_start <= temporal_range_end`).  
  - Quantities are non-negative and within plausible ranges.

### 2️⃣ Cultural & Sovereignty Validation (FAIR+CARE)

- Descriptions use neutral, respectful language.  
- Sensitive categories (burials, sacred items, restricted motifs) are removed or excluded prior to inclusion here.  
- `location_h3` levels comply with sovereignty policy and CARE generalization rules.  
- Inventory is confirmed to be:
  - Appropriately licensed,  
  - Approved by affected communities/repositories when required.  

### 3️⃣ Technical & Metadata Validation

- A valid **STAC Item** exists and passes STAC validation.  
- A metadata/DCAT record exists and passes metadata schema validation.  
- A PROV-O provenance file exists and passes provenance schema validation.  
- H3 generalization is consistent across inventory, STAC, and provenance entries.  
- Files are UTF-8 encoded and ready for downstream ETL.

Validation is enforced via CI workflows, e.g.:

- `.github/workflows/archaeology-artifacts-stac-validate.yml`  
- `.github/workflows/archaeology-artifacts-metadata-validate.yml`  
- `.github/workflows/faircare-archaeology-audit.yml`  

---

## 🛰️ Integration Into KFM Systems

### Knowledge Graph (Neo4j)

Inventory tables are ingested to create or enrich:

**Nodes**

- `:Artifact`  
- `:ArtifactType`  
- `:Material`  
- `:CulturalPhase`  
- `:GeneralizedSite`  
- `:InventoryDatasetVersion`

**Relationships**

- `(:Artifact)-[:BELONGS_TO]->(:InventoryDatasetVersion)`  
- `(:Artifact)-[:FOUND_AT]->(:GeneralizedSite)` (via `location_h3`)  
- `(:Artifact)-[:DATED_TO]->(:TimeInterval)`  
- `(:Artifact)-[:TYPED_AS]->(:ArtifactType)`  
- `(:Artifact)-[:HAS_MATERIAL]->(:Material)`  
- `(:CulturalPhase)-[:SUPPORTED_BY]->(:InventoryDatasetVersion)`

### Focus Mode v3 & Story Nodes

Inventories support:

- Material-culture summaries anchored in specific cultural phases and regions,  
- Phase-based patterns and distributions rendered as safe H3 density maps,  
- Evidence-backed stories for Focus Mode that can cite counts and distributions rather than site-level details.

Story Nodes must:

- Reference inventories by dataset version IDs and STAC Items,  
- Surface only generalized spatial and contextual information,  
- Clearly mark where content has been generalized or redacted for sovereignty and CARE.

---

## 📦 Example Artifact Inventory Snippet

```csv
artifact_id,material,artifact_type,culture_phase,dating_method,temporal_range_start,temporal_range_end,location_h3,site_class,quantity,description,source,provenance_file
"uuid-1234","lithic","projectile_point","Late Prehistoric","typology","1200 CE","1400 CE","872830fffffffff","village","1","Triangular point with smoothed edges; description generalized.","WSU Open Collections","provenance/flint-hills-lithics-v11.json"
```

This example is illustrative; actual vocabularies, code lists, and constraints for each field are defined in the hydrology & archaeology schema documentation and referenced by the provenance file.

---

## 🕰️ Version History

| Version | Date       | Author / Steward                      | Summary                                                                 |
|--------:|------------|----------------------------------------|-------------------------------------------------------------------------|
| v11.2.3 | 2025-12-02 | Archaeology WG · FAIR+CARE Council     | Updated to KFM v11.2.3; aligned with v11 STAC/metadata/provenance standards; added telemetry references. |
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council     | Added inventory file index, schema & validation rules, cultural protections, and KFM integration details. |
| v10.0.0 | 2025-11-10 | Artifact Dataset Team                  | Initial structure and placeholder inventory support.                    |

---

<div align="center">

🏺 **Kansas Frontier Matrix — Artifact Inventory Files**  

[⬅ Artifact Inventories Index](../README.md) ·  
[📜 Project History Archive](../../../../../history/README.md) ·  
[⚖️ Root Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
