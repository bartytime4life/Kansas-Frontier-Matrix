---
title: "🗂️ Kansas Frontier Matrix — Artifact Inventory STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Authoritative STAC 1.0 catalog for KFM v11 artifact inventories, enforcing FAIR+CARE, sovereignty governance, and generalized spatial exposure."
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Tribal Sovereignty Review Board"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventory-stac-catalog-v11.2.3"
doc_kind: "STAC Catalog"
intent: "artifact-inventory-stac"
semantic_document_id: "kfm-doc-archaeology-artifact-inventory-stac-catalog-v11.2.3"
category: "Analyses · Archaeology · STAC Catalog"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-stac-catalog-v1.json"
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

data_steward: "Archaeology & Heritage WG · Tribal Sovereignty Board"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🗂️ Kansas Frontier Matrix — Artifact Inventory STAC Catalog (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/README.md`

**Purpose**  
Define the **authoritative STAC (SpatioTemporal Asset Catalog)** for all **public-governed artifact inventory datasets** in KFM v11.

Ensure that artifact datasets are:

- Machine-discoverable  
- Metadata-complete  
- Culturally safe and sovereignty-aligned  
- Validated against: STAC 1.0, DCAT 3.0, CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O, KFM-OP v11, MCP-DL v6.3  

This catalog underpins:

- Graph and ETL ingestion  
- Artifact distribution modeling  
- Cultural-phase correlation  
- Story Node v3 and Focus Mode v3 contextualization  
- FAIR+CARE-governed metadata access  
- Archaeological visualization layers that are generalised and safe

---

## 📘 Overview

The STAC entries in this directory provide **top-level metadata** for every **governed, public** artifact inventory dataset in KFM.

Each STAC Collection or Item corresponds to a **cleaned, generalized, sovereignty-reviewed** dataset located under:

- `../inventories/` – standardized artifact inventory tables  
- `../metadata/` – DCAT and governance metadata  
- `../provenance/` – PROV-O lineage bundles  

Only datasets that meet all of the following are cataloged here:

- Public-domain or open-license (for example: CC0, CC-BY)  
- Culturally reviewed and sovereignty-approved  
- Spatially generalized using H3-based methods  

Sensitive or sovereignty-restricted inventories are maintained in **separate, governed registries** and are not exposed in this public STAC catalog.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/
├── 📄 README.md                          # This file (STAC catalog index)
├── 📂 items/                             # STAC Items for each artifact inventory dataset
├── 📂 collections/                       # STAC Collections grouping related inventories
├── 📂 schemas/                           # JSON Schema for artifact-specific STAC validation
└── 📂 examples/                          # Annotated STAC examples (documentation and tests)
~~~

This layout is **normative** for STAC structures in this directory.

---

## 📦 STAC Collections

Every artifact inventory category must have at least one **STAC Collection**.

### Required Collections

| Collection                   | Purpose                                               |
|-----------------------------|-------------------------------------------------------|
| `artifact-inventories.json` | Root-level index of all artifact inventory datasets   |
| `lithics.json`              | Lithic artifact inventories                           |
| `ceramics.json`             | Ceramic inventories                                   |
| `metals.json`               | Contact/metal artifact inventories                    |
| `faunal.json`               | Public-domain faunal inventories                      |

### Required Collection Fields

Collections must include:

- Core fields  
  - `id`, `type`, `stac_version`  
  - `description`, `license`, `keywords[]`  
  - `extent.spatial` (generalized bounding box)  
  - `extent.temporal` (OWL-Time compatible interval)  

- KFM and FAIR+CARE fields  
  - `kfm:domain = "archaeology-artifact-inventories"`  
  - `kfm:version`, `kfm:release_stage`  
  - `care:sensitivity_rollup` (for example: `"generalized-high"`)  
  - `care:sovereignty` (for example: `"governed"`)  

- Linkage  
  - `links[]` pointing to:
    - Child Items  
    - Parent Collections (where present)  
    - DCAT and PROV-O resources  
    - Governance documentation and policies  

---

## 📦 STAC Items

Each STAC Item under `items/` must comply with **STAC 1.0.0** and KFM archaeology extensions.

### Core Fields

| Field                           | Requirement / Notes                                      |
|---------------------------------|---------------------------------------------------------|
| `id`                            | Unique artifact inventory identifier                    |
| `type`                          | `"Feature"`                                             |
| `stac_version`                  | `"1.0.0"`                                               |
| `bbox`                          | Generalized extent derived from H3 footprints           |
| `geometry`                      | `MultiPoint` or simplified polygon geometry only        |
| `properties.datetime`           | `null` or representative mid-interval                   |
| `assets.data.href`              | Inventory CSV/Parquet path                              |
| `properties.kfm:phase`          | Cultural-phase attribution                              |
| `properties.kfm:domain`         | `"archaeology-artifact-inventories"`                    |
| `properties.care:sensitivity`   | `"generalized"` or `"restricted-generalized"`           |
| `properties.kfm:generalization` | H3 level (for example: `"H3-r7"`, `"H3-r8"`)            |
| `properties.kfm:provenance`     | Path to PROV-O file in `../provenance/`                |
| `properties.dct:license`        | SPDX license code (for example: `CC-BY-4.0`)           |

### Required Extensions

| Extension     | Purpose                                              |
|--------------|------------------------------------------------------|
| `proj`       | CRS, transform, and raster/grid shape where relevant |
| `checksum`   | SHA-256 validation of main assets                    |
| `version`    | Version tracking                                     |
| `scientific` | Citations, creators, DOIs, related works             |
| `kfm`        | Domain, release stage, internal contract/versioning  |
| `care`       | Sensitivity, sovereignty, consent and review fields  |

Items that do not validate against all required extensions must not be merged into the catalog.

---

## 🌍 Spatial and Temporal Rules

| Aspect            | Rule                                                                 |
|-------------------|----------------------------------------------------------------------|
| CRS               | EPSG:4326 (WGS84), unless justified and documented                  |
| Spatial precision | Coordinates derived from H3 r7–r10 centroids                        |
| Geometry types    | `MultiPoint`, `Polygon`, or `MultiPolygon` with generalized shapes  |
| Site exposure     | No geometry may uniquely identify a specific site or context        |
| Temporal coverage | OWL-Time interval (`start`, `end`, `precision`) in `properties`     |
| Sensitivity       | `care:sensitivity` and `kfm:generalization` must be consistent      |

---

## 🧪 Validation and CI

All Collections and Items must pass:

- STAC core schema validation using definitions in `schemas/`  
- KFM archaeology STAC extension validation (KFM and CARE blocks)  
- CARE sensitivity validation against sovereignty policies  
- SHA-256 checksum validation for all `assets.data` and key metadata files  
- Crosswalk checks:
  - `items/` ↔ `../inventories/` (IDs and paths)  
  - `items/` ↔ `../metadata/` (DCAT alignment)  
  - `items/` ↔ `../provenance/` (PROV-O chains)  

Example CI workflow (normative):

- `.github/workflows/artifact-stac-validate.yml`  
  - STAC schema validation  
  - Extension validation (KFM and CARE)  
  - Checksum verification  
  - Governance and sensitivity gates  

Any failure prevents catalog updates from being accepted.

---

## 🧠 Example STAC Item (Artifact Inventory)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "artifact-inventory-flint-hills-lithics-v11",
  "bbox": [-101.3, 37.6, -95.3, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      /* H3-r7 generalized centroids only */
    ]
  },
  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "kfm:phase": "Late Prehistoric",
    "kfm:generalization": "H3-r7",
    "care:sensitivity": "generalized",
    "care:sovereignty": "protected",
    "kfm:provenance": "../provenance/flint-hills-lithics-v11.json",
    "dct:license": "CC-BY-4.0",
    "datetime": null
  },
  "assets": {
    "data": {
      "href": "../inventories/flint-hills-lithics-v11.csv",
      "type": "text/csv",
      "roles": ["data"]
    },
    "metadata": {
      "href": "../metadata/flint-hills-lithics-v11.json",
      "type": "application/json",
      "roles": ["metadata"]
    }
  }
}
~~~

This example is illustrative; authoritative schemas and examples live in `schemas/` and `examples/`.

---

## 📊 STAC Catalog Index (Illustrative)

| Collection                   | Item examples                                                |
|-----------------------------|--------------------------------------------------------------|
| `artifact-inventories.json` | `flint-hills-lithics-v11.json`, `prairie-ceramics-v11.json` |
| `lithics.json`              | `flint-hills-lithics-v11.json`                              |
| `ceramics.json`             | `prairie-ceramics-v11.json`                                 |
| `metals.json`               | `contact-era-metals-v11.json`                               |
| `faunal.json`               | `fauna-open-v11.json`                                       |

The canonical index is computed from the actual contents of `collections/` during CI.

---

## 🔗 Integration

### Knowledge Graph

- STAC Items map to `ArtifactInventory` nodes.  
- Spatial properties are linked using GeoSPARQL-compatible geometries and H3 indices.  
- PROV-O references from `kfm:provenance` connect to ingestion and validation activities.

### Story Node v3 and Focus Mode v3

- Story Nodes referencing artifact inventories must link by:
  - STAC `id`  
  - `semantic_document_id` for this README  
- Focus Mode v3 uses this catalog as the **trusted discovery layer** for artifact inventories and only surfaces datasets that pass all validation and governance checks.

---

## 🕰 Version History

| Version   | Date       | Summary                                                                                         |
|-----------|------------|-------------------------------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Aligned to KFM-MDP v11.2.2; updated paths and schemas; added energy/carbon refs; clarified CI and governance rules. |
| v10.4.0   | 2025-11-17 | Created artifact STAC catalog; added CARE governance, metadata rules, validation workflows.    |
| v10.0.0   | 2025-11-10 | Initial artifact inventory STAC catalog structure.                                              |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Artifact Inventories](../README.md)