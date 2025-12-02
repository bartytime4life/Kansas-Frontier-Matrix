---
title: "🗂️ Kansas Frontier Matrix — Artifact Inventory STAC Collections (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Domain-level STAC Collections for KFM v11 artifact inventories, grouping culturally governed datasets by material class, phase, and provenance."
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Tribal Sovereignty Review Board"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventory-stac-collections-v11.2.3"
doc_kind: "STAC Collections"
intent: "artifact-inventory-stac-collections"
semantic_document_id: "kfm-doc-archaeology-artifact-inventory-stac-collections-v11.2.3"
category: "Analyses · Archaeology · STAC Collections"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-artifact-stac-collections-v1.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

data_steward: "Archaeology & Heritage WG · Tribal Sovereignty Board"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🗂️ Kansas Frontier Matrix — Artifact Inventory STAC Collections (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/README.md`

**Purpose**  
Define the **STAC Collection layer** for artifact inventory datasets in the Kansas Frontier Matrix (KFM), enabling:

- Structured discovery and browsing of artifact inventories  
- FAIR+CARE and sovereignty-governed grouping by material, phase, and provenance  
- Consistent integration with KFM’s ETL, knowledge graph, Story Nodes, Focus Mode, and visualization layers  

All Collections in this directory must comply with:

- **STAC 1.0**  
- **DCAT 3.0**  
- **PROV-O**  
- **KFM Archaeology Extensions (KFM-OP v11)**  
- **CARE metadata and sovereignty policies**

---

## 📘 Overview

STAC Collections in this directory provide **high-level grouping metadata** for artifact inventories.

Each Collection acts as:

- A **semantic grouping node** in the KFM STAC tree  
- A **source of truth** for cultural and material categories  
- A **FAIR+CARE governance checkpoint** for artifact inventories  
- A **machine-readable metadata aggregator** for downstream systems  
- A **root reference** for STAC Items located in `../items/`

Collections support:

- Neo4j knowledge graph population  
- Story Node v3 material-culture narratives  
- Focus Mode v3 contextual reasoning  
- Notebook-based analysis pipelines  
- MapLibre/Cesium visualization metadata inheritance  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/collections/
├── 📄 README.md                           # This file
├── 📄 artifact-inventories.json           # Root collection for all artifact inventories
├── 📄 lithics.json                        # Lithic artifact collection
├── 📄 ceramics.json                       # Ceramic artifact collection
├── 📄 metals.json                         # Metal + protohistoric artifact collection
├── 📄 faunal.json                         # Public-domain faunal dataset collection
└── 📂 templates/                          # Collection template files and schemas
~~~

This layout is **normative**; CI should treat extra top-level files as a schema violation unless documented.

---

## 🧭 Required Structure for All STAC Collections

Every STAC Collection in this directory must include the following structures.

### Core Collection Fields

| Field              | Description                               |
|--------------------|-------------------------------------------|
| `id`               | Unique collection identifier              |
| `type`             | `"Collection"`                            |
| `stac_version`     | `"1.0.0"`                                 |
| `description`      | Summary of the grouped datasets           |
| `license`          | SPDX identifier (for example: `CC-BY-4.0`) |
| `extent.spatial`   | Generalized bounding box                  |
| `extent.temporal`  | OWL-Time compatible start/end interval    |
| `links`            | Self, root, and related item/collection links |

### KFM Collection Extensions (`kfm:*`)

| Field                    | Description                                                         |
|--------------------------|---------------------------------------------------------------------|
| `kfm:material_class`     | `"lithic"`, `"ceramic"`, `"metal"`, `"faunal"`, or `"mixed"`        |
| `kfm:domain`             | `"archaeology-artifact-inventories"`                               |
| `kfm:review_cycle`       | Text description (for example: `"Biannual"`)                       |
| `kfm:provenance_summary` | Brief summary of typical sources and processing for this grouping  |

### CARE and Sovereignty Metadata

| Field             | Allowed Values / Description                                |
|-------------------|------------------------------------------------------------|
| `care:sensitivity`| `general`, `generalized`, or `restricted-generalized`      |
| `care:review`     | `"faircare"`, `"tribal"`, `"none-required"`                |
| `care:notes`      | Explanation of cultural and sovereignty treatment          |

These fields must align with the **sovereignty policy** referenced in the front matter.

---

## 📚 Collection Descriptions

### `artifact-inventories.json` · Root Collection

Root-level Collection that links:

- All lithic artifact inventories  
- All ceramic artifact inventories  
- All metal / protohistoric artifact inventories  
- All public-domain faunal inventories  

- Spatial extent: generalized to the full Kansas region (H3-based generalization).  
- Temporal extent: Paleoindian through Historic periods.

This Collection is the **entry point** for artifact inventories in KFM’s public STAC catalog.

---

### `lithics.json`

Includes all **public-governed lithic artifact inventories** that pass sovereignty and CARE review.

Metadata typically includes:

- Raw material classes (for example: chert, quartzite, obsidian)  
- Tool categories (projectile point, scraper, core, etc.)  
- Phase and cultural attributions  
- H3-generalized spatial coverage  

Spatial and temporal extents must be derived from the child Items and generalized for safety.

---

### `ceramics.json`

Includes:

- Ceramic sherd and vessel inventories  
- Motif categories that have been **generalized** for cultural safety  
- Temporal phase distributions  
- Generalized site categories (no exact provenience)

Requires:

- CARE-sensitive motif filtering  
- Explicit **sovereignty review** for culturally meaningful patterns and motifs.

---

### `metals.json`

Includes:

- Protohistoric and contact-era metal artifacts  
- European trade goods and related contact materials  
- Tool/weapon fragments that have passed cultural review  

Requires:

- **Tribal cultural and sovereignty review** for any artifacts associated with contact-era or sensitive sites.  
- Stricter generalization rules for spatial coverage.

---

### `faunal.json`

Includes:

- Open-access zooarchaeological datasets  
- Pleistocene and Holocene public-domain faunal inventories  

Must exclude:

- Sacred species  
- Any fauna tightly coupled with restricted archaeological contexts or sacred landscapes.

---

## 🧪 Validation Requirements

All Collections must pass:

- STAC 1.0 Collection schema validation  
- KFM archaeology STAC extension validation (`kfm:*` and `care:*` blocks)  
- CARE and sovereignty metadata validation  
- License verification against SPDX mappings  
- Temporal consistency checks relative to child Items  
- Spatial generalization verification (H3-based, no exact site exposure)  
- Cross-referencing with STAC Items in `../items/` (IDs and links must match)

Validation is expected to run under a CI workflow such as:

- `.github/workflows/artifact-stac-validate.yml`

---

## 🧩 Example STAC Collection (Lithics · v11-Aligned)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "lithics",
  "description": "Public-governed lithic artifact inventories for prehistoric Kansas regions.",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": {
      "bbox": [[-102.1, 37.0, -94.6, 40.1]]
    },
    "temporal": {
      "interval": [["1200-01-01T00:00:00Z", "1500-01-01T00:00:00Z"]]
    }
  },
  "links": [],
  "kfm:material_class": "lithic",
  "kfm:domain": "archaeology-artifact-inventories",
  "kfm:review_cycle": "Biannual",
  "kfm:provenance_summary": "Aggregated from public-domain lithic catalogs with H3 generalization and sovereignty review.",
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "All lithic data generalized to H3 and reviewed for cultural and sovereignty safety."
}
~~~

This example is illustrative; canonical templates should live under `templates/`.

---

## 📊 Collection Index (Illustrative)

| Collection file              | Category  | Status   | Last review |
|-----------------------------|-----------|----------|-------------|
| `artifact-inventories.json` | Root      | 🟢 Active | 2025-11     |
| `lithics.json`              | Lithics   | 🟢 Active | 2025-11     |
| `ceramics.json`             | Ceramics  | 🟢 Active | 2025-10     |
| `metals.json`               | Metals    | 🟡 Review | 2025-09     |
| `faunal.json`               | Faunal    | 🟢 Active | 2025-11     |

The authoritative status and review dates should be maintained in the actual Collection JSON and/or registry, not only in this table.

---

## 🕰 Version History

| Version   | Date       | Summary                                                                                  |
|-----------|------------|------------------------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Aligned with KFM-MDP v11.2.2; added energy/carbon schemas; sovereignty fields; validation and governance clarified. |
| v10.4.0   | 2025-11-17 | Created artifact STAC Collection catalog; added metadata rules, CARE requirements, validation workflows. |
| v10.0.0   | 2025-11-10 | Initial STAC Collection directory setup.                                                 |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Artifact STAC Catalog](../README.md)