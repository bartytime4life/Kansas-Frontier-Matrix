---
title: "📑 Kansas Frontier Matrix — Artifact Inventory Metadata Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/metadata/README.md"
description: "Metadata specification for KFM v11 artifact inventories, aligning DCAT, STAC, CARE, and KFM archaeology extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventory-metadata-v11.2.3"
doc_kind: "Metadata Standard"
intent: "artifact-inventory-metadata"
semantic_document_id: "kfm-doc-archaeology-artifact-inventory-metadata-v11.2.3"
category: "Analyses · Archaeology · Metadata"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-inventory-metadata-v1.json"
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
immutability_status: "mutable-plan"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Archaeology Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/metadata/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📑 Kansas Frontier Matrix — Artifact Inventory Metadata Standards (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/metadata/README.md`

**Purpose**  
Define the complete **metadata specification** for all artifact inventory datasets within the Kansas Frontier Matrix (KFM) v11.

This standard ensures alignment with:

- **FAIR+CARE** and sovereignty policies  
- **STAC 1.0** (Items + Collections)  
- **DCAT 3.0**  
- **CIDOC-CRM**, **GeoSPARQL**, **OWL-Time**, **ISO 19115**  
- **KFM-OP v11** (ontology) and **MCP-DL v6.3** (documentation-first)  

Metadata in this directory supports:

- Neo4j graph ingestion and reasoning  
- Story Node and Focus Mode v3 generation  
- Archaeological visualization (MapLibre + Cesium)  
- Predictive and phase-based modeling  
- Artifact classification reproducibility and provenance traceability  

Only **public-domain**, **open-license**, or **sovereignty-approved** inventories may be represented here.

---

## 📘 Overview

Each metadata file in this directory provides machine-readable description, governance, and cultural-safety fields for:

- Lithic datasets  
- Ceramic datasets  
- Metal / protohistoric datasets  
- Faunal (public-domain oriented) datasets  
- Additional open-access artifact tables that meet governance criteria  

No sensitive, culturally restricted, or non-consented artifact information may appear in this directory.

Metadata is stored as **JSON-LD**, combining:

- **DCAT 3.0 Dataset metadata**  
- **STAC 1.0 Item metadata** (mirroring entries in `stac/items/`)  
- **CARE** cultural safety metadata  
- **KFM archaeology extension** (`kfm:*`) references to provenance, Collections, and inventories  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/metadata/
├── 📄 README.md                           # This file
├── 📄 flint-hills-lithics-v11.json        # DCAT + STAC + CARE + KFM metadata
├── 📄 prairie-ceramics-v11.json           # Ceramic inventory metadata
├── 📄 contact-era-metals-v11.json         # Protohistoric metals metadata (governed)
├── 📄 fauna-open-v11.json                 # Faunal (public-domain oriented) metadata
└── 📂 schemas/                            # JSON schemas for metadata validation
~~~

This layout is **normative** for artifact-inventory metadata in KFM v11.

---

## 📦 Required Metadata Layers

Each metadata file MUST integrate the following layers.

### 1️⃣ DCAT 3.0 Dataset Metadata

Required DCAT fields:

| Field              | Description                       | Example                                          |
|--------------------|-----------------------------------|--------------------------------------------------|
| `dct:title`        | Dataset title                     | `"Flint Hills Lithic Inventory v11"`            |
| `dct:description`  | Summary of dataset                | `"Generalized lithic inventory, culturally reviewed."` |
| `dct:license`      | SPDX license code                 | `"CC-BY-4.0"`                                    |
| `dct:creator`      | Source institution / custodian    | `"WSU Open Collections"`                         |
| `dct:temporal`     | Temporal coverage (OWL-Time)      | `"1200–1400 CE"` or interval representation      |
| `dct:spatial`      | Generalized spatial description   | `"Kansas, Flint Hills region (generalized)"`     |
| `dcat:distribution`| Path/URL to main distribution     | `"inventories/flint-hills-lithics-v11.csv"`      |
| `dcat:keyword`     | Tags / keywords                   | `["lithic", "inventory", "Kansas", "archaeology"]` |

DCAT metadata must be consistent with STAC, CARE, and provenance layers.

---

### 2️⃣ STAC 1.0 Item Metadata (Mirrored)

Metadata files must align with the corresponding STAC Item in `stac/items/`.

Required STAC fields:

| STAC Field                | Description                              | Example                                         |
|---------------------------|------------------------------------------|-------------------------------------------------|
| `stac_version`            | STAC version                             | `"1.0.0"`                                       |
| `type`                    | STAC type                               | `"Feature"`                                     |
| `id`                      | Unique dataset ID                        | `"flint-hills-lithics-v11"`                    |
| `bbox`                    | Generalized bounding box                 | `[-101.2, 37.5, -95.4, 40.1]`                  |
| `geometry`                | Generalized geometry (no site-precise)   | `MultiPoint`                                    |
| `properties.kfm:domain`   | Domain identifier                        | `"archaeology-artifact-inventories"`           |
| `properties.kfm:phase`    | Cultural-phase name                      | `"Late Prehistoric"`                           |
| `properties.kfm:material_class` | Material class                    | `"lithic"`                                      |
| `properties.kfm:generalization` | Spatial generalization level       | `"H3-r7"`                                       |
| `properties.kfm:provenance`     | Provenance log path                | `"provenance/flint-hills-lithics-v11.json"`    |
| `assets.data.href`        | Inventory file path                      | `"inventories/flint-hills-lithics-v11.csv"`    |
| `assets.data.type`        | MIME type                                | `"text/csv"`                                    |

Metadata and STAC Item MUST remain in sync, especially for:

- `id`  
- `kfm:phase`  
- `kfm:material_class`  
- `kfm:provenance`  
- asset paths  

---

### 3️⃣ CARE Cultural-Safety Metadata

All artifact inventory metadata MUST include CARE fields, consistent with STAC and provenance.

Required CARE fields:

| CARE Field              | Description                     | Allowed Values                                     |
|-------------------------|---------------------------------|---------------------------------------------------|
| `care:sensitivity`      | Sensitivity class               | `"general"`, `"generalized"`, `"restricted-generalized"` |
| `care:review`           | Review authority                | `"faircare"`, `"tribal"`, `"none-required"`       |
| `care:notes`            | Cultural context / review notes | Free text; required for `generalized` or `restricted-generalized` |
| `care:visibility_rules` | Visibility constraints          | `"h3-only"`, `"no-exact-points"`                  |

Forbidden:

- `care:sensitivity = "restricted"` for metadata in this public-governed directory.  
- Any fields that expose sacred sites, burials, or culturally restricted information.  
- Precise provenience, excavation-unit IDs, or sensitive photo references.

---

### 4️⃣ KFM Archaeology & Governance Fields (`kfm:*`)

Metadata files must also include key KFM fields for governance and graph integration:

| Field                | Description                                   |
|----------------------|-----------------------------------------------|
| `kfm:domain`         | Must be `"archaeology-artifact-inventories"` |
| `kfm:phase`          | Cultural phase (as above)                    |
| `kfm:material_class` | Material class for this inventory            |
| `kfm:datatype`       | Typically `"artifact-inventory"`             |
| `kfm:provenance`     | Path to JSON-LD provenance log               |
| `kfm:source`         | Source institution or repository             |

These fields must match the corresponding STAC & provenance artifacts.

---

## 🧪 Validation Requirements

All artifact-inventory metadata must pass:

- **JSON Schema validation**  
  - Against metadata schemas in `metadata/schemas/`.  
- **DCAT 3.0 validation**  
  - Required DCAT fields present and consistent.  
- **STAC alignment checks**  
  - IDs, paths, and `kfm:*` fields consistent with STAC Items.  
- **CARE validation**  
  - `care:*` values allowed and consistent with generalization and sovereignty policy.  
- **Crosswalk alignment**  
  - With:
    - STAC Item in `stac/items/`  
    - Provenance log in `provenance/`  
    - Collection metadata in `stac/collections/` where applicable  

Validation workflows (illustrative):

- `docs/analyses/archaeology/validation/`  
- `.github/workflows/artifact-metadata-validate.yml`  
- `.github/workflows/artifact-stac-validate.yml`  

Any failure must block ingestion and release.

---

## 🛰️ Integration Into the KFM Ecosystem

Metadata in this directory feeds multiple layers:

### Knowledge Graph (Neo4j)

- Drives creation of:
  - `ArtifactInventory`, `MaterialClass`, `CulturalPhase`, and `GeneralizedSite` nodes.  
- Establishes relationships:
  - `HAS_INVENTORY`, `BELONGS_TO_PHASE`, `HAS_MATERIAL_CLASS`, `HAS_CARE_SENSITIVITY`, `HAS_PROVENANCE`.

### Story Nodes

- Provides:
  - Material-culture context  
  - Temporal placement  
  - Sensitivity-aware narrative framing  
  - Provenance summary for each Story Node referencing artifact inventories  

### Focus Mode v3

- Uses metadata to:
  - Filter responses based on CARE & sovereignty rules  
  - Render provenance chips and dataset references  
  - Provide context-aware explanations of artifact distributions and phases  

### Visualization

- Supports:
  - H3-based artifact density maps  
  - Temporal distribution overlays  
  - Material/phase-based symbology and filters  

---

## 📄 Example Metadata Snippet (v11-Aligned)

Illustrative example for a lithic inventory:

~~~json
{
  "dct:title": "Flint Hills Lithic Inventory v11",
  "dct:description": "Generalized lithic artifact dataset for the Flint Hills region, reviewed under FAIR+CARE.",
  "dct:license": "CC-BY-4.0",
  "dct:creator": "WSU Open Collections",
  "dct:temporal": "1200–1400 CE",
  "dct:spatial": "Kansas, Flint Hills region (generalized)",
  "dcat:distribution": "inventories/flint-hills-lithics-v11.csv",
  "dcat:keyword": ["lithic", "inventory", "Kansas", "archaeology"],

  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "flint-hills-lithics-v11",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": []
  },
  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "kfm:phase": "Late Prehistoric",
    "kfm:material_class": "lithic",
    "kfm:generalization": "H3-r7",
    "kfm:provenance": "provenance/flint-hills-lithics-v11.json",
    "care:sensitivity": "generalized",
    "care:review": "faircare",
    "care:notes": "Coordinates generalized via H3-r7 and reviewed for cultural safety.",
    "care:visibility_rules": "no-exact-points"
  },
  "assets": {
    "data": {
      "href": "inventories/flint-hills-lithics-v11.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
~~~

This snippet is illustrative; canonical constraints are defined by schemas in `metadata/schemas/`.

---

## 🕰 Version History

| Version   | Date       | Author                           | Summary                                                                 |
|-----------|------------|----------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · FAIR+CARE Council | Updated to KFM v11.2.3; added energy/carbon telemetry refs; aligned with STAC/CARE/KFM v11 patterns and Focus Mode v3. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created metadata standards for artifact inventories; defined STAC/DCAT/CARE rules and validation paths. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team           | Initial structure and baseline metadata guidance.                        |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Artifact Inventories](../README.md)
