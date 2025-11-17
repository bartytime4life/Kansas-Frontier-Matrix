---
title: "🗂️ Kansas Frontier Matrix — Artifact Inventory STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-stac-catalog-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Catalog"
intent: "artifact-inventory-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Artifact Inventory STAC Catalog**  
`docs/analyses/archaeology/datasets/artifact-inventories/stac/README.md`

**Purpose:**  
Define the **authoritative STAC (SpatioTemporal Asset Catalog)** for all artifact inventory datasets in the Kansas Frontier Matrix (KFM).  
Ensures that artifact datasets are machine-discoverable, metadata-complete, culturally safe, and verifiably aligned with **STAC 1.0**, **DCAT 3.0**, **CIDOC-CRM**, **GeoSPARQL**, **PROV-O**, and **MCP-DL v6.3**.

This catalog enables:

- Graph and ETL ingestion  
- Artifact distribution modeling  
- Cultural-phase correlation  
- Story Node and Focus Mode v2 contextualization  
- FAIR+CARE-governed metadata access  
- Fully validated archaeological visualization layers  

</div>

---

## 📘 Overview

The STAC entries in this directory provide the **top-level metadata** for every artifact inventory dataset in KFM.  
Each STAC item corresponds to a cleaned, generalized, and culturally reviewed dataset located in:

- `inventories/`  
- `metadata/`  
- `provenance/`  

Only **public-domain**, **open-license**, or **tribally reviewed** datasets may be cataloged here.

No restricted or sensitive artifact inventories are permitted in STAC.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/
├── README.md                          # This file
├── items/                             # STAC Items for each artifact inventory dataset
├── collections/                       # STAC Collections grouping related inventories
├── schemas/                           # JSON Schema for artifact-specific STAC validation
└── examples/                          # Annotated STAC examples
~~~

---

## 📦 STAC Collection Requirements

Every artifact inventory category must have a **STAC Collection**, including:

| Collection | Purpose |
|---|---|
| `artifact-inventories.json` | Root-level index of all artifact inventory datasets |
| `lithics.json` | Lithic artifacts grouped collection |
| `ceramics.json` | Ceramic datasets |
| `metals.json` | Protohistoric/metal artifact inventories |
| `faunal.json` | Public-domain faunal datasets |

Collection files MUST include:

- Title & description  
- Temporal extent  
- Spatial extent (generalized)  
- License  
- Keywords  
- CARE sensitivity rollups  
- Links to child item files  
- Provider information  
- Dataset version history  

---

## 📦 STAC Item Requirements

Each STAC Item under `items/` must comply with **STAC 1.0.0** and KFM archaeology-specific extensions.

### Required Fields

| Field | Requirement |
|---|---|
| `id` | Unique artifact inventory identifier |
| `type` | `"Feature"` |
| `stac_version` | `"1.0.0"` |
| `bbox` | Bounding box using generalized or H3-derived extent |
| `geometry` | `MultiPoint` or generalized polygons |
| `assets.data.href` | Inventory CSV path |
| `properties.kfm:phase` | Cultural-phase attribution |
| `care:sensitivity` | `"general"`, `"generalized"`, `"restricted-generalized"` |
| `proj:*` | CRS & projection metadata |
| `kfm:provenance` | Path to PROV-O file |
| `dct:license` | SPDX license code |

### Required Extensions

| Extension | Purpose |
|---|---|
| `proj` | CRS, transform, shape |
| `version` | Version history tracking |
| `checksum` | SHA-256 validation |
| `scientific` | DOI, citations, data creators |
| `kfm` | Archaeology metadata fields |
| `care` | Sensitivity & cultural governance |

---

## 🌍 Spatial / Temporal Requirements

| Requirement | Rule |
|---|---|
| CRS | EPSG:4326 unless justified |
| Spatial precision | Must be generalized (H3 5–7) |
| Geometry | Multipoints or simplified polygons only |
| Temporal coverage | OWL-Time interval (`start`, `end`, `precision`) |
| Sensitivity | Must match CARE classification in metadata |

---

## 🧪 Validation Requirements

All STAC items MUST pass:

- STAC schema validation (`schemas/`)  
- KFM archaeology STAC extension validation  
- CARE sensitivity validation  
- SHA-256 checksum verification  
- Crosswalk with metadata and provenance files  
- Alignment with artifact inventory schema (in `inventories/`)  

CI pipeline for validation:  
`.github/workflows/artifact-stac-validate.yml`

---

## 🧠 Example STAC Item (Artifact Inventory)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "flint-hills-lithics-v1",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [[ /* generalized */ ]]
  },
  "properties": {
    "kfm:phase": "Late Prehistoric",
    "care:sensitivity": "generalized",
    "kfm:provenance": "provenance/flint-hills-lithics-v1.json"
  },
  "assets": {
    "data": {
      "href": "inventories/flint-hills-lithics-v1.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
~~~

---

## 📊 STAC Catalog Index

| Collection | Item Examples |
|---|---|
| `artifact-inventories.json` | `flint-hills-lithics-v1.json`, `prairie-ceramics-v1.json` |
| `lithics.json` | `flint-hills-lithics-v1.json` |
| `ceramics.json` | `prairie-ceramics-v1.json` |
| `metals.json` | `contact-era-metals-v1.json` |
| `faunal.json` | `fauna-open-v1.json` |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created artifact STAC catalog; added CARE governance, metadata rules, validation workflows; ensured box-safe formatting |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial structure of STAC catalog |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Artifact Inventories](../README.md)

</div>