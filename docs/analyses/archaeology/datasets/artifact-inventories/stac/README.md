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

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Artifact Inventory STAC Catalog (v11)**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/README.md`

**Purpose:**  
Define the **authoritative STAC (SpatioTemporal Asset Catalog)** for all **public-governed artifact inventory datasets** in KFM v11.  

Ensures that artifact datasets are **machine-discoverable**, **metadata-complete**, **culturally safe**, and verifiably aligned with:

**STAC 1.0 · DCAT 3.0 · CIDOC-CRM · GeoSPARQL · OWL-Time · PROV-O · KFM-OP v11 · MCP-DL v6.3**

This catalog enables:

- Graph and ETL ingestion  
- Artifact distribution modeling  
- Cultural-phase correlation  
- Story Node v3 + Focus Mode v3 contextualization  
- FAIR+CARE-governed metadata access  
- Fully validated archaeological visualization layers  

</div>

---

## 📘 Overview

The STAC entries in this directory provide **top-level, machine-readable metadata** for every **governed, public** artifact inventory dataset in KFM.

Each STAC Item or Collection corresponds to a **cleaned, generalized, sovereignty-reviewed** dataset located under the parent directory:

- `../inventories/` — standardized tabular artifact inventories  
- `../metadata/` — DCAT/CARE/governance metadata  
- `../provenance/` — PROV-O lineage bundles  

Only datasets that are:

- **Public-domain** or **open-license (e.g., CC0, CC-BY)**  
- **Culturally reviewed and sovereignty-approved**  
- **Spatially generalized (H3-based)**  

may be cataloged here.

Sensitive or sovereignty-restricted artifact inventories are **not** represented in this public STAC catalog; they are maintained in **separate, governed registries** referenced only via generalized indicators.

---

## 🗂️ Directory Layout (v11 · Normative)

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/
├── 📄 README.md                          # This file (STAC catalog index)
├── 📂 items/                             # STAC Items for each artifact inventory dataset
├── 📂 collections/                       # STAC Collections grouping related inventories
├── 📂 schemas/                           # JSON Schema for artifact-specific STAC validation
└── 📂 examples/                          # Annotated STAC examples (documentation & testing)
~~~

This layout is **normative**; CI will fail if additional STAC-bearing directories appear here without documentation.

---

## 📦 STAC Collection Requirements (v11)

Every artifact inventory category MUST have at least one **STAC Collection**.

### Required Collections

| Collection                        | Purpose                                               |
|----------------------------------|-------------------------------------------------------|
| `artifact-inventories.json`      | Root-level index of all artifact inventory datasets   |
| `lithics.json`                   | Lithic artifacts grouped collection                   |
| `ceramics.json`                  | Ceramic datasets                                      |
| `metals.json`                    | Contact/metal artifact inventories                    |
| `faunal.json`                    | Public-domain faunal datasets                         |

### Required Collection Fields

Collections MUST include (STAC 1.0 + KFM extensions):

- **Core:**
  - `id`, `type`, `stac_version`  
  - `description`, `license`, `keywords[]`  
  - `extent.spatial` (generalized bbox)  
  - `extent.temporal` (OWL-Time compatible interval)  

- **KFM / FAIR+CARE:**
  - `kfm:domain = "archaeology-artifact-inventories"`  
  - `kfm:version` and `kfm:release_stage`  
  - `care:sensitivity_rollup` (e.g., `"generalized-high"`)  
  - `care:sovereignty` (e.g., `"governed"`)  

- **Linkage:**
  - `links[]` to:
    - child Items  
    - parent Collections  
    - DCAT and PROV-O records  
    - governance documentation  

---

## 📦 STAC Item Requirements (v11)

Each STAC Item under `items/` must comply with **STAC 1.0.0** and KFM archaeology extension rules.

### Core Required Fields

| Field                         | Requirement / Notes                                      |
|-------------------------------|---------------------------------------------------------|
| `id`                          | Unique artifact inventory identifier                    |
| `type`                        | `"Feature"`                                             |
| `stac_version`                | `"1.0.0"`                                               |
| `bbox`                        | Generalized extent derived from H3 footprint            |
| `geometry`                    | `MultiPoint` or simplified polygons (no exact sites)   |
| `properties.datetime`         | `null` or representative mid-interval                   |
| `assets.data.href`            | Inventory CSV/Parquet path (repository or remote)      |
| `properties.kfm:phase`        | Cultural-phase attribution                              |
| `properties.kfm:domain`       | `"archaeology-artifact-inventories"`                    |
| `properties.care:sensitivity` | `"generalized"` / `"restricted-generalized"`            |
| `properties.kfm:generalization` | e.g., `"H3-r7"` / `"H3-r8"`                           |
| `properties.kfm:provenance`   | Path to PROV-O file in `../provenance/`                |
| `properties.dct:license`      | SPDX code (`CC-BY-4.0`, `CC0-1.0`, etc.)               |

### Required Extensions

| Extension   | Purpose                                              |
|------------|------------------------------------------------------|
| `proj`     | CRS, transform, raster/grid shape where applicable   |
| `checksum` | SHA-256 validation of primary assets                 |
| `version`  | Version tracking (`version` extension or KFM fields) |
| `scientific` | Citations, creators, DOIs, related works          |
| `kfm`      | Domain, contract version, governance anchors         |
| `care`     | Sensitivity, sovereignty, consent & review metadata  |

No Item may be accepted into the catalog without passing all extension validations.

---

## 🌍 Spatial & Temporal Rules (v11)

| Aspect              | Rule                                                                 |
|---------------------|----------------------------------------------------------------------|
| CRS                 | EPSG:4326 (WGS84) unless explicitly justified and documented        |
| Spatial precision   | Coordinates MUST be generalized from H3 r7–r10 centroids            |
| Geometry types      | `MultiPoint`, generalized `Polygon`, or `MultiPolygon` only         |
| Site exposure       | No geometry may uniquely identify a specific site or context         |
| Temporal coverage   | OWL-Time interval (`start`, `end`, `precision`) in properties       |
| Sensitivity linkage | `care:sensitivity` and `kfm:generalization` must be consistent      |

---

## 🧪 Validation & CI Requirements

All STAC Items and Collections MUST pass:

- **STAC core schema validation** using the schemas in `schemas/`  
- **KFM archaeology STAC extension validation** (care + kfm blocks)  
- **CARE sensitivity validation** against governance policies  
- **SHA-256 checksum verification** for all `assets.data` and critical sidecars  
- **Crosswalk checks**:
  - `items/` ↔ `../inventories/` (ID + file path)  
  - `items/` ↔ `../metadata/` (DCAT alignment)  
  - `items/` ↔ `../provenance/` (PROV-O chains)  

CI pipeline (normative example):

- `.github/workflows/artifact-stac-validate.yml`  
  - Step 1: STAC schema validate  
  - Step 2: extension validate (kfm + care)  
  - Step 3: checksum validation  
  - Step 4: governance gate (sensitivity + sovereignty rules)  

Any failure → catalog update is blocked.

---

## 🧠 Example STAC Item (Artifact Inventory · v11-Aligned)

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

This example is **illustrative**; canonical schemas live under `schemas/`.

---

## 📊 STAC Catalog Index (Illustrative)

| Collection                   | Item Examples                                                |
|-----------------------------|--------------------------------------------------------------|
| `artifact-inventories.json` | `flint-hills-lithics-v11.json`, `prairie-ceramics-v11.json` |
| `lithics.json`              | `flint-hills-lithics-v11.json`                              |
| `ceramics.json`             | `prairie-ceramics-v11.json`                                 |
| `metals.json`               | `contact-era-metals-v11.json`                               |
| `faunal.json`               | `fauna-open-v11.json`                                       |

The **authoritative** index is derived from actual contents of `collections/` during CI validation.

---

## 🔗 Integration with Graph, Story Nodes, and Focus Mode

- **Neo4j / Knowledge Graph:**
  - STAC Items map to `ArtifactInventory` nodes with links to:
    - `Artifact`, `GeneralizedSite`, `Collection`, `StoryNode`  
  - Spatial aspects are represented using **GeoSPARQL** and H3 indices.

- **Story Node v3:**
  - Story Nodes referencing artifact inventories must:
    - Link back via `semantic_document_id` and STAC `id`.  
    - Respect CARE and sovereignty flags from the STAC properties.

- **Focus Mode v3:**
  - Uses this catalog as the **trusted discovery layer** for artifact inventories.  
  - Only inventories that have passed STAC + governance validation are exposed to Focus Mode for reasoning.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                                         |
|-----------|------------|-------------------------------------------------------------------------------------------------|
| **v11.2.3** | 2025-12-02 | v11 alignment; added energy/carbon schemas; sovereignty/gov fields; CI/validation clarified; Focus v3 integration. |
| v10.4.0   | 2025-11-17 | Created artifact STAC catalog; added CARE governance, metadata rules, validation workflows.    |
| v10.0.0   | 2025-11-10 | Initial structure of artifact inventory STAC catalog.                                           |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Artifact Inventories](../README.md)

</div>