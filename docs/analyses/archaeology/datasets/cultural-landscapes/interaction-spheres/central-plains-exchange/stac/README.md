---
title: "🗂️🔄 Kansas Frontier Matrix — Central Plains Exchange Interaction Sphere STAC Documentation (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/README.md"
description: "STAC 1.0 Collection + Item documentation for the Central Plains Exchange interaction-sphere dataset in KFM v11, with KFM and CARE extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-sphere-central-plains-exchange-stac-v11.2.3"
doc_kind: "STAC Documentation"
intent: "central-plains-exchange-stac"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-central-plains-exchange-stac-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · STAC"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-central-plains-exchange-stac-v1.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

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
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🗂️🔄 STAC Metadata — Central Plains Exchange Interaction Sphere (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/README.md`

**Purpose**  
Provide the authoritative **STAC 1.0 documentation** for the **Central Plains Exchange Interaction Sphere** dataset in the Kansas Frontier Matrix (KFM) v11.

This STAC layer enables:

- Machine-readable dataset discovery and filtering.  
- FAIR+CARE-compliant, generalized spatial representation.  
- Consistent integration with:
  - Neo4j Knowledge Graph.  
  - Story Node v3 narratives.  
  - Focus Mode v3 interpretive overlays.  
  - MapLibre + Cesium visualization layers.  
  - DCAT metadata and PROV-O provenance.

For dataset context, see:

- `../README.md` (Central Plains Exchange interaction-sphere overview).

For global interaction-sphere STAC patterns, see:

- `../../stac/README.md`.

---

## 📘 Overview

The **Central Plains Exchange Interaction Sphere** represents a large, multi-era cultural region spanning the Republican, Smoky Hill, Solomon, Platte, and Kansas river systems and their prairie–riverine ecotones.

STAC metadata for this dataset captures:

- Generalized spatial extent (MultiPolygon + H3-based generalization).  
- Temporal coverage (ca. AD 900–1400, Central Plains Tradition).  
- Cultural-phase associations.  
- CARE sensitivity and review information.  
- Links to distribution assets (GeoJSON/COG).  
- Links to metadata (`../metadata/`) and provenance (`../provenance/`).

Sensitivity is **medium** and governed via generalization; tribal review is recommended where protohistoric overlaps arise but not mandatory for the baseline CPT-focused sphere.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/
├── 📄 README.md                               # This file
├── 📄 central-plains-exchange-v1.json         # STAC Item (interaction-sphere geometry)
└── 📂 collections/
    └── 📄 central-plains-exchange.json        # STAC Collection for this interaction sphere
~~~

- The Item `central-plains-exchange-v1.json` is grouped by the Collection `collections/central-plains-exchange.json`.  
- IDs and filenames must match across STAC, metadata, and provenance.

---

## 📦 STAC Item Requirements (`central-plains-exchange-v1.json`)

The STAC Item describes the **generalized interaction-sphere geometry** and core properties.

### 1️⃣ Core STAC Fields

| Field          | Example                               | Notes                            |
|----------------|----------------------------------------|----------------------------------|
| `stac_version` | `"1.0.0"`                             | Fixed for KFM v11 STAC Items     |
| `type`         | `"Feature"`                           | STAC Item type                   |
| `id`           | `"central-plains-exchange-v1"`        | Versioned, matches filename stem |
| `collection`   | `"central-plains-exchange"`           | Parent Collection ID             |
| `bbox`         | `[-103.0, 36.8, -94.5, 43.2]`         | Generalized bounding box         |
| `geometry`     | `Polygon` / `MultiPolygon`            | Generalized spatial extent       |

`geometry` must reflect **generalized** regions only, not site-precise areas.

### 2️⃣ KFM Cultural-Landscape Extensions (`properties.kfm:*`)

Minimum required `kfm:*` properties:

| Field                 | Description                                | Example                                        |
|-----------------------|--------------------------------------------|------------------------------------------------|
| `kfm:domain`          | Domain identifier                          | `"archaeology-cultural-landscapes"`           |
| `kfm:region_type`     | Landscape type                             | `"interaction_sphere"`                        |
| `kfm:culture_phase`   | Cultural phases represented                | `["CPT-Early","CPT-Middle","CPT-Late"]`       |
| `kfm:generalization`  | Spatial generalization method              | `"H3-r7"` or `"H3-r6"`                        |
| `kfm:provenance`      | Link to provenance JSON                    | `"../provenance/central-plains-exchange-v1.json"` |
| `kfm:review_cycle`    | Review cadence                             | `"Biannual"`                                   |

These values must be consistent with `../metadata/central-plains-exchange-v1.json` and the provenance record.

### 3️⃣ CARE Metadata (`properties.care:*`)

Expected CARE fields:

| Field                   | Value / Behavior                                     |
|-------------------------|------------------------------------------------------|
| `care:sensitivity`      | `"generalized"`                                      |
| `care:review`           | `"faircare"`                                         |
| `care:notes`            | For example: `"Generalization applied to avoid sensitive cultural inference; no site-level data included."` |
| `care:visibility_rules` | `"polygon-generalized"` (or `"h3-only"` for sensitive sublayers, if any) |
| `care:consent_status`   | `approved`, `conditional`, etc. (e.g., `"approved"`) |

CARE metadata must remain in sync across STAC, metadata, and provenance.

### 4️⃣ Temporal Properties

Temporal coverage must be OWL-Time–compatible and consistent:

| Field                         | Example                         |
|------------------------------|----------------------------------|
| `properties.start_datetime`  | `"0900-01-01T00:00:00Z"`        |
| `properties.end_datetime`    | `"1400-01-01T00:00:00Z"`        |

These dates must match DCAT `dct:temporal` and internal phase definitions.

### 5️⃣ Assets

Minimal `assets` block:

| Asset Key   | Description                          | Example                                      |
|-------------|--------------------------------------|----------------------------------------------|
| `data`      | Generalized geometry data            | GeoJSON / COG polygon dataset                |
| (optional) `thumbnail` | Preview image             | PNG / JPEG for quick map preview             |
| (optional) `metadata`  | Link to extended metadata | `"../metadata/central-plains-exchange-v1.json"` |

Example snippet:

~~~json
"assets": {
  "data": {
    "href": "../central-plains-exchange.geojson",
    "type": "application/geo+json",
    "roles": ["data"]
  }
}
~~~

---

## 📂 STAC Collection Requirements (`collections/central-plains-exchange.json`)

The Collection groups all Items for this interaction sphere.

### 1️⃣ STAC Core Fields

| Field          | Example                               |
|----------------|----------------------------------------|
| `stac_version` | `"1.0.0"`                             |
| `type`         | `"Collection"`                        |
| `id`           | `"central-plains-exchange"`           |
| `description`  | `"Generalized Central Plains Exchange interaction sphere"` |
| `license`      | `"CC-BY-4.0"`                         |

### 2️⃣ Extent

- `extent.spatial.bbox` must match or coarsely encompass the Item’s bbox.  
- `extent.temporal.interval` must represent the overall CPT span, for example:

~~~json
"extent": {
  "spatial": {
    "bbox": [[-103.0, 36.8, -94.5, 43.2]]
  },
  "temporal": {
    "interval": [["0900-01-01T00:00:00Z","1400-01-01T00:00:00Z"]]
  }
}
~~~

### 3️⃣ KFM & CARE Fields (Collection-Level)

At the Collection level, typical fields include:

| Field            | Value / Description                     |
|------------------|------------------------------------------|
| `kfm:domain`     | `"archaeology-cultural-landscapes"`     |
| `kfm:region_type`| `"interaction_sphere"`                  |
| `kfm:review_cycle` | `"Biannual"`                          |
| `care:sensitivity` | `"generalized"`                       |
| `care:review`    | `"faircare"`                            |
| `care:notes`     | Short summary of cultural-safety considerations |

These represent the least permissive conditions across all child Items.

### 4️⃣ Links (`links[]`)

The Collection should include:

- `self` and `root` links where relevant.  
- One or more `item` links pointing to `../central-plains-exchange-v1.json`.  
- Optional links to documentation and related Collections.

---

## 🧪 Validation Rules

The STAC Item and Collection must pass validation via interaction-sphere schemas:

- `stac-item-schema.json`  
- `stac-collection-schema.json`  
- `kfm-interaction-extension.json`  
- `care-sensitivity-extension.json`  
- `dcat-crosswalk.json` (for DCAT ↔ STAC consistency)  

Plus cross-link checks with:

- `../metadata/central-plains-exchange-v1.json`  
- `../provenance/central-plains-exchange-v1.json`

Validation is enforced via CI workflows, such as:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  

Any failure must be resolved before the dataset or its updates are released.

---

## 🧠 Integration Into KFM Ecosystem

### Knowledge Graph

STAC metadata contributes to:

**Nodes**

- `InteractionSphere` (Central Plains Exchange).  
- `CulturalPhase` (for CPT phases).  
- `GeneralizedRegion` and `MetadataRecord` nodes.  

**Relationships**

- `HAS_METADATA`  
- `HAS_PROVENANCE`  
- `HAS_CARE_SENSITIVITY`  
- `OCCURRED_DURING`  
- `ASSOCIATED_WITH` (to inventories, landscapes, and narratives)  

### Story Nodes & Focus Mode v3

STAC provides:

- Spatial and temporal scopes for narratives and maps.  
- Sensitivity and CARE cues for ethical framing.  
- Provenance references for explanation chips and “About this data” panels.

---

## 📊 STAC Item Overview (Illustrative)

| Item                               | Sensitivity  | Status   | Review    |
|------------------------------------|-------------|----------|-----------|
| `central-plains-exchange-v1.json` | generalized | 🟢 Active | FAIR+CARE |

Authoritative review status is recorded in metadata, provenance, and release manifests.

---

## 🔗 Related Specifications

- `../README.md`  
  – Central Plains Exchange interaction-sphere dataset overview.  
- `../metadata/README.md`  
  – Central Plains Exchange metadata specification.  
- `../provenance/README.md`  
  – Central Plains Exchange provenance logs.  
- `../../stac/README.md`  
  – Global interaction-sphere STAC catalog (Items + Collections).  

---

## 🕰 Version History

| Version   | Date       | Author                                   | Summary                                                                 |
|-----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council | Updated for KFM v11.2.3; aligned with interaction-sphere STAC schemas; clarified CARE/KFM fields and validation patterns. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Initial Central Plains Exchange STAC documentation; defined Item and Collection structures. |
| v10.0.0   | 2025-11-10 | Landscape Metadata Team                  | Prototype STAC draft and early catalog layout.                          |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Central Plains Exchange Dataset](../README.md)
