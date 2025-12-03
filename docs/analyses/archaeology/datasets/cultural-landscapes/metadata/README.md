---
title: "🌄 Kansas Frontier Matrix — Cultural Landscape Metadata Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/metadata/README.md"
description: "Global metadata standard for KFM v11 cultural landscape datasets (regions, routes, interaction spheres, resource areas), aligned with DCAT, STAC, KFM, CARE, and PROV-O."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-metadata-standards-v11.2.3"
doc_kind: "Metadata Standard"
intent: "cultural-landscape-metadata"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-metadata-standards-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Metadata"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-metadata-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "Cultural / Historical / Archaeological"
sensitivity_level: "Medium"
indigenous_rights_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/metadata/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🌄 Kansas Frontier Matrix — Cultural Landscape Metadata Standards (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/metadata/README.md`

**Purpose**  
Define the **metadata specification** for all **cultural landscape datasets** within the Kansas Frontier Matrix (KFM), including:

- Settlement regions  
- Interaction spheres  
- Resource procurement zones  
- Ancient trails and mobility routes  
- Generalized territorial / cultural regions  
- Environmental–cultural synthesis layers  

These standards ensure all cultural-landscape metadata is:

- FAIR+CARE and sovereignty aligned.  
- Compatible with **STAC 1.0**, **DCAT 3.0**, **KFM extensions (`kfm:*`)**, **CARE (`care:*`)**, and **PROV-O**.  
- Ready for **Story Node v3**, **Focus Mode v3**, MapLibre/Cesium, and graph ingestion.

---

## 📘 Overview

Cultural landscape metadata must provide:

- Ethical representation of culturally significant geographies.  
- Protection of Indigenous sovereignty and sensitive knowledge.  
- Spatial generalization of vulnerable areas.  
- Temporal context using culturally grounded phases.  
- Transparent provenance and review history.  
- Machine-readability for ETL, catalogs, graph queries, and AI narratives.  

This directory contains metadata JSON files for cultural landscape datasets under:

- `regions/`  
- `routes/`  
- `interaction-spheres/`  
- `resource-areas/`  

and shared templates and schemas used across these categories.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/metadata/
├── 📄 README.md                            # This file (global standards)
├── 📄 great-bend-aspect-v2.json            # Interaction sphere metadata (example)
├── 📄 central-plains-exchange-v1.json      # Interaction sphere metadata (example)
├── 📄 protohistoric-wichita-v2.json        # High-sensitivity interaction sphere metadata
├── 📂 templates/                           # Non-annotated metadata templates
└── 📂 schemas/                             # JSON Schemas validating all metadata files
~~~

Individual subtrees (e.g., interaction-spheres) may have their own metadata READMEs; this file defines the **global baseline** for all cultural landscape metadata.

---

## 📦 Required Metadata Components

Each cultural landscape metadata JSON MUST include:

1. **DCAT 3.0 dataset metadata**  
2. **KFM cultural-landscape extension fields (`kfm:*`)**  
3. **CARE cultural-safety metadata (`care:*`)**  
4. **Provenance link (`kfm:provenance`)**  
5. **STAC crosswalk alignment** with associated Items/Collections  

---

### 1️⃣ DCAT 3.0 Fields

Required DCAT fields:

| Field             | Description                                      |
|-------------------|--------------------------------------------------|
| `dct:title`       | Dataset name (human-readable)                    |
| `dct:description` | Generalized summary of the cultural landscape    |
| `dct:license`     | License (e.g., `"CC-BY-4.0"` or `"CC0-1.0"`)     |
| `dct:temporal`    | OWL-Time–compatible time span (text or structured) |
| `dct:creator`     | Dataset steward or institution                   |
| `dcat:keyword`    | Tags (e.g., `"archaeology"`, `"cultural-landscape"`, `"region"`) |
| `dcat:distribution` | Link to STAC Item or primary asset            |

These values must be reflected in STAC Collections/Items and in release manifests.

---

### 2️⃣ KFM Cultural-Landscape Metadata (`kfm:*`)

KFM extensions capture archaeological and landscape semantics.

Typical required fields:

| Field                       | Description                                      | Example                 |
|-----------------------------|--------------------------------------------------|-------------------------|
| `kfm:domain`                | Domain identifier                               | `"archaeology-cultural-landscapes"` |
| `kfm:landscape_type` / `kfm:region_type` | Class of landscape (region, route, sphere, resource) | `"interaction_sphere"` |
| `kfm:culture_phase`         | Cultural phase(s) represented                    | `["Late Prehistoric","Protohistoric-Wichita"]` |
| `kfm:generalization`        | Spatial generalization method                    | `"H3-r7"` or `"simplified-polygon"` |
| `kfm:source`                | Primary data sources description                 | `"Kansas Historical Society archives and PD syntheses"` |
| `kfm:provenance`            | Path to PROV-O provenance file                   | `"../provenance/great-bend-aspect-v2.json"` |
| `kfm:schema_version`        | Metadata schema/template version                 | `"v11.0.0"` or later |

Subcategory standards (e.g., interaction-spheres) may define additional required KFM fields.

---

### 3️⃣ CARE Cultural-Safety Metadata (`care:*`)

All cultural landscape metadata MUST include CARE fields, tuned to sensitivity level.

| Field                | Allowed / Example Values                               | Purpose                                   |
|----------------------|--------------------------------------------------------|-------------------------------------------|
| `care:sensitivity`   | `"general"`, `"generalized"`, `"restricted-generalized"` | Overall sensitivity classification         |
| `care:review`        | `"faircare"`, `"tribal"`, `"none-required"`            | Indicates review authority                 |
| `care:notes`         | Free-text note                                         | Explains cultural-safety decisions         |
| `care:visibility_rules` | `"h3-only"`, `"no-exact-points"`, `"polygon-generalized"` | Controls public spatial fidelity   |
| `care:consent_status`| `approved`, `conditional`, `not-approved`, `not-applicable` | Clarifies consent state for public use |

**Rules:**

- `care:sensitivity = "restricted"` is **never** used in public KFM repositories.  
- `care:sensitivity = "restricted-generalized"` requires **tribal review** and strict visibility rules (often `"h3-only"`).  
- Territorial or sacred landscapes must be generalized at coarse scales and may require additional governance (or exclusion).

---

### 4️⃣ Provenance Metadata (PROV-O Link)

All metadata must link to a PROV-O lineage record:

| Field             | Description                      |
|-------------------|----------------------------------|
| `kfm:provenance`  | Relative path to provenance JSON |

The referenced provenance file must describe:

- Data sources and extraction methods.  
- GIS/generalization steps.  
- Cultural and ethical review events (FAIR+CARE, tribal when needed).  
- Modeling assumptions and uncertainty.  

Subtree provenance standards (e.g., for interaction spheres) add more detailed requirements.

---

### 5️⃣ STAC Alignment Requirements

Metadata must align with associated STAC Collections/Items:

| Metadata Field        | STAC Field                                  |
|-----------------------|---------------------------------------------|
| `dct:title`           | STAC `id`/`title`/`description`             |
| `kfm:culture_phase`   | STAC `properties.kfm:culture_phase`        |
| `care:sensitivity`    | STAC `properties.care:sensitivity`         |
| `kfm:provenance`      | STAC `properties.kfm:provenance`           |
| `dcat:distribution`   | STAC `assets.data.href` or Item path       |

Alignment is enforced by crosswalk schemas under `schemas/`.

---

## 🌍 Spatial Metadata Requirements

All cultural landscape metadata must reflect generalized, privacy-preserving spatial representations.

Required practices:

- CRS: **EPSG:4326** unless a strong justification is provided.  
- Bounding boxes: generalized BBOX covering the cultural landscape region.  
- Generalization method:
  - H3 mosaics or topological simplification documented in `kfm:generalization` and provenance.  
- Public metadata must **not** describe exact sacred/ceremonial polygons or reveal protected site locations.

---

## 🕰 Temporal Metadata Requirements

Temporal metadata must:

- Specify earliest and latest dates relevant to the dataset.  
- Use ISO 8601 date strings or clearly labeled ranges (e.g., `"AD 1300–1600"`).  
- Prefer OWL-Time–compatible structures in STAC and DCAT.  
- Align with KFM’s cultural-phase ontology by mapping phases to time intervals.

Uncertainty notes are encouraged where ranges are approximate or overlapping.

---

## 🧠 Integration Into KFM Ecosystem

### Knowledge Graph

Metadata records help populate and connect:

**Nodes**

- `CulturalLandscape` (or subtypes such as `InteractionSphere`, `CulturalRegion`, `Route`, `ResourceArea`).  
- `CulturalPhase`.  
- `MetadataRecord`.  
- CARE and governance-related nodes.

**Relationships**

- `HAS_METADATA`  
- `HAS_PROVENANCE`  
- `OCCURRED_DURING`  
- `ASSOCIATED_WITH`  
- `GENERALIZED_FROM`  
- `HAS_CARE_SENSITIVITY`  

### Story Nodes & Focus Mode v3

Metadata fields support:

- Culture-aware narratives and timeline synchronization.  
- Region-based story mapping and overlays.  
- Ethical warnings, sensitivity badges, and provenance chips.  
- Filtered, sovereignty-aligned responses in Focus Mode v3.

---

## 🧪 Validation Requirements

All cultural landscape metadata must pass validation against schemas in `schemas/`, including (names may vary):

- `metadata-core-schema.json`  
- `dcat-metadata-schema.json`  
- `care-metadata-schema.json`  
- `provenance-link-schema.json`  
- `stac-crosswalk-schema.json`  

CI workflows enforcing these validations include:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  
- `.github/workflows/artifact-stac-validate.yml`  

Validation ensures:

- Cultural safety and sovereignty compliance.  
- Spatial generalization is adequately documented.  
- Metadata completeness and consistency.  
- Proper linkage to STAC and provenance artifacts.

---

## 🕰 Version History

| Version   | Date       | Author                                   | Summary                                                                 |
|-----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council | Upgraded to KFM v11.2.3; added energy/carbon telemetry references; aligned with interaction-sphere metadata standards and CARE vocabularies. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Established cultural landscape metadata standards; defined DCAT/STAC/CARE requirements. |
| v10.0.0   | 2025-11-10 | Landscape Metadata Team                  | Initial metadata directory scaffold.                                   |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscapes](../README.md)
