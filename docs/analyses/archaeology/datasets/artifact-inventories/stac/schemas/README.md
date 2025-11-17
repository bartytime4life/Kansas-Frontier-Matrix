---
title: "📐 Kansas Frontier Matrix — Artifact Inventory STAC Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-artifact-stac-schemas-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Schema Documentation"
intent: "artifact-inventory-stac-schemas"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Artifact Inventory STAC Schemas**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/README.md`

**Purpose:**  
Define and document the **STAC JSON Schema set** used to validate artifact inventory STAC Items and Collections within the Kansas Frontier Matrix (KFM).  
These schemas ensure compliance with:

- **STAC 1.0 Core Specification**  
- **Projection Extension (`proj`)**  
- **Scientific Extension (`sci`)**  
- **Versioning Extension (`version`)**  
- **Checksum Extension (`checksum`)**  
- **KFM Archaeology Extension (`kfm:*`)**  
- **CARE Cultural Safety Extension (`care:*`)**  
- **DCAT 3.0 Crosswalk Requirements**  
- **FAIR+CARE Ethical Standards**  

Every artifact dataset in KFM must pass validation using these schemas prior to ingestion into the metadata catalog, graph database, pipelines, or Focus Mode v2.

</div>

---

## 📘 Overview

The schemas in this directory define:

- Valid **STAC Item** structure for artifact inventories  
- Valid **STAC Collection** structure for artifact categories  
- **Domain-specific archaeological fields** (`kfm:*`)  
- **Cultural safety fields** (`care:*`)  
- Structural constraints for spatial, temporal, and provenance metadata  
- Required cross-linking to datasets in `inventories/`, metadata in `metadata/`, and provenance in `provenance/`

These schemas are used by:

- CI pipelines (`artifact-stac-validate.yml`)  
- Dataset ingestion scripts  
- Story Node + Focus Mode metadata generation  
- KFM catalog browsers and STAC viewers  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/
├── README.md                                # This file
├── stac-item-schema.json                     # Validator for artifact STAC Items
├── stac-collection-schema.json               # Validator for artifact STAC Collections
├── kfm-archaeology-extension.json            # Custom extension definitions
├── care-sensitivity-extension.json           # CARE cultural safety metadata schema
├── dcat-crosswalk.json                       # Ensures DCAT <-> STAC metadata alignment
└── templates/                                # Example templates for new schemas
~~~

---

## 📦 1. STAC Item Schema (Artifact Inventories)

Located at:  
`stac-item-schema.json`

This schema validates:

### ✔ Core STAC Fields
- `id`  
- `type = "Feature"`  
- `stac_version = "1.0.0"`  
- `bbox`  
- `geometry` (generalized only)  
- `properties.start_datetime`  
- `properties.end_datetime`  
- `assets.data`  
- `links.collection`

### ✔ KFM Archaeology Extension (`kfm:*`)
Required fields:

| Field | Description |
|---|---|
| `kfm:phase` | Cultural-phase label |
| `kfm:datatype` | `"artifact-inventory"` |
| `kfm:material_class` | `"lithic"`, `"ceramic"`, `"metal"`, `"faunal"` |
| `kfm:provenance` | Path to PROV-O file |
| `kfm:source` | Institution / archive |

### ✔ CARE Extension (`care:*`)
Validated fields:

| Field | Rules |
|---|---|
| `care:sensitivity` | Must be `"general"` or `"generalized"` |
| `care:review` | `"faircare"`, `"tribal"`, `"none-required"` |
| `care:notes` | Required for ceramics & metals |
| `care:visibility_rules` | `"h3-only"`, `"no-exact-points"` |

### ✔ Extensions Required
- `proj`  
- `version`  
- `checksum`  
- `sci`  
- `kfm`  
- `care`

All must be present or validation fails.

---

## 📦 2. STAC Collection Schema

Located at:  
`stac-collection-schema.json`

Validates:

- `type = "Collection"`  
- `extent.spatial.bbox`  
- `extent.temporal.interval`  
- `license` (SPDX)  
- `links` correctness  
- `kfm:material_class`, `kfm:domain`, `kfm:review_cycle`  
- `care:sensitivity`, `care:notes`, `care:review`  

Collections group Items logically and semantically across:

- **Lithics**
- **Ceramics**
- **Metals**
- **Faunal datasets**
- **Root artifact-inventories collection**

---

## 📦 3. KFM Archaeology Extension Schema

Located at:  
`kfm-archaeology-extension.json`

Defines archaeology-specific metadata fields:

| Field | Purpose |
|---|---|
| `kfm:phase` | Cultural-phase classification |
| `kfm:material_class` | Lithic / ceramic / etc. |
| `kfm:datatype` | `"artifact-inventory"` |
| `kfm:source` | Museum / repository |
| `kfm:provenance` | PROV-O lineage file path |
| `kfm:review_cycle` | Validation / dataset audit cycle |

This schema enforces **controlled vocabularies** to guarantee interoperability.

---

## 📦 4. CARE Sensitivity Schema

Located at:  
`care-sensitivity-extension.json`

Defines rules for:

- Cultural safety  
- Generalization requirements  
- Heritage protection  
- Tribal review fields  
- Ethical framing requirements  

Prohibits:

- `"restricted"` items in artifact inventories  
- Precise site coordinates  
- Excavation unit identifiers  
- Culturally sensitive object descriptions  

---

## 📦 5. DCAT Crosswalk Schema

Located at:  
`dcat-crosswalk.json`

Ensures STAC metadata aligns with required DCAT fields:

| DCAT Field | STAC Mapping |
|---|---|
| `dct:title` | `title` / `description` |
| `dct:license` | `license` |
| `dct:temporal` | `properties.start_datetime` / `end_datetime` |
| `dcat:distribution` | `assets.*.href` |
| `dcat:keyword` | `keywords` |

Ensures datasets remain valid for:

- Dataset catalogs  
- FAIR indexing  
- Future STAC API services  

---

## 🧪 Validation Pipeline

Schemas here power CI jobs:

- `.github/workflows/artifact-stac-validate.yml`
- `.github/workflows/metadata-validate.yml`
- `.github/workflows/faircare-audit.yml`

Validation steps:

1. STAC schema validation  
2. KFM extension validation  
3. CARE sensitivity review  
4. DCAT alignment check  
5. Checksum verification  
6. Provenance linkage validation  
7. Cross-file consistency across Inventory → Metadata → Provenance  

Only datasets passing all steps can be ingested.

---

## 🧠 Example: Minimal Schema Snippet

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Archaeology STAC Item Schema",
  "type": "object",
  "required": ["id", "stac_version", "type", "bbox", "geometry", "properties", "assets"],
  "properties": {
    "stac_version": { "const": "1.0.0" },
    "type": { "const": "Feature" }
  }
}
~~~

*(Full schemas located in this directory.)*

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added full schema suite for artifact inventories; integrated KFM + CARE extensions; ensured box-safe formatting |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial schema directory structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Artifact STAC Catalog](../README.md)

</div>