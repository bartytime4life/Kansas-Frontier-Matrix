---
title: "🗂️ Kansas Frontier Matrix — Interaction Sphere STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-interaction-spheres-stac-catalog-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Catalog"
intent: "interaction-spheres-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Interaction Sphere STAC Catalog**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/README.md`

**Purpose:**  
Provide the **authoritative STAC (SpatioTemporal Asset Catalog)** index for all **Interaction Sphere** datasets within the Kansas Frontier Matrix (KFM).  
Interaction Spheres model broad-scale patterns of **cultural connectivity, exchange, communication pathways, shared material culture, and eco-cultural co-adaptation**.

This catalog ensures Interaction Sphere datasets are:

- Machine-discoverable  
- FAIR+CARE aligned  
- STAC 1.0 compliant  
- Ontology-mapped to KFM’s Knowledge Graph (CIDOC-CRM + GeoSPARQL)  
- Governed ethically via CARE metadata  
- Fully integrated with Story Nodes and Focus Mode v2  

</div>

---

# 📘 Overview

This directory houses:

- **STAC Collections** for each group of Interaction Sphere datasets  
- **STAC Items** describing individual spheres  
- **Validation schemas** for Items/Collections  
- **Templates** for contributors  
- Crosswalks ensuring STAC ↔ DCAT ↔ PROV-O alignment  
- Machine-readable metadata for all cultural-interaction models

Interaction Spheres included:

- **Great Bend Aspect (v2)**  
- **Central Plains Exchange (v1)**  
- **Protohistoric Wichita (v1, high sensitivity)**  
- Future expansions (Caddoan borderlands, Plains-Apache exchanges, etc.)

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/stac/
├── README.md                                 # This file
├── collections/                              # Parent-level STAC Collections
│   ├── interaction-spheres.json              # Root Collection
│   ├── great-bend-aspect.json                # GBA Collection
│   ├── central-plains-exchange.json          # Central Plains Exchange Collection
│   └── protohistoric-wichita.json            # Protohistoric Wichita Collection
├── items/                                    # STAC Items
│   ├── great-bend-aspect-v2.json
│   ├── central-plains-exchange-v1.json
│   ├── protohistoric-wichita-v1.json
├── schemas/                                  # STAC, KFM, CARE validation schemas
└── templates/                                # Contributor templates (Items + Collections)
~~~

---

# 🧭 STAC Collections (Required)

Each Interaction Sphere must belong to a **STAC Collection**, grouping datasets by cultural domain.

### Minimum Required Fields

| Field | Description |
|---|---|
| `id` | Collection identifier |
| `description` | High-level summary |
| `extent` | Spatial + temporal coverage |
| `license` | SPDX identifier |
| `links` | References to STAC Items |
| `kfm:*` | Domain-specific metadata |
| `care:*` | Sensitivity metadata |

### Interaction Sphere Collections Provided

- **interaction-spheres.json** — Root interaction sphere collection  
- **great-bend-aspect.json**  
- **central-plains-exchange.json**  
- **protohistoric-wichita.json**

---

# 📦 STAC Item Requirements

Each STAC Item describing an Interaction Sphere must include:

### ✔ STAC Core
- `id`
- `type: "Feature"`
- `stac_version: "1.0.0"`
- `bbox`
- `geometry`
- `properties`
- `assets`

### ✔ KFM Interaction Sphere Metadata (`kfm:*`)
| Field | Description |
|---|---|
| `kfm:landscape_type` | `"interaction_sphere"` |
| `kfm:culture_phase` | Phase(s) defining the sphere |
| `kfm:source` | Source of synthesis (PD only) |
| `kfm:provenance` | PROV-O lineage file |
| `kfm:geometry_generalization` | `"H3-level-6"` / `"simplified-polygon"` |
| `kfm:review_cycle` | `"Biannual"` |

### ✔ CARE Cultural Safety Metadata (`care:*`)
| Field | Description |
|---|---|
| `care:sensitivity` | `"generalized"` / `"restricted-generalized"` |
| `care:review` | `"faircare"` / `"tribal"` |
| `care:notes` | Ethical considerations & safeguards |
| `care:visibility_rules` | `"polygon-generalized"` / `"h3-only"` |

### ✔ DCAT Crosswalk
- `dct:title`  
- `dct:description`  
- `dct:temporal`  
- `dct:license`  
- `dcat:distribution`  

### ✔ PROV-O Linkage
Every STAC Item must reference:

“kfm:provenance”: “../provenance/.json”

---

# 🌍 Spatial Requirements

- Must use **generalized polygons** or **H3 mosaics (levels 5–7)**  
- No depiction of sacred areas, sensitive sites, or settlement clusters  
- CRS must always be **EPSG:4326**  
- Geometry simplification required for public release  
- All sensitive datasets → `"h3-only"` visibility  

---

# 🕰️ Temporal Requirements

- OWL-Time compliant ranges (start + end datetime)  
- Cultural-phase-based temporal metadata  
- Multi-era spheres must list complete time spans  
- Temporal alignment with Story Node + Focus Mode timelines  

---

# ⚖️ Ethical, Cultural & CARE Governance

Interaction Spheres are culturally significant. Therefore:

### Required:
- FAIR+CARE review  
- Tribal review for protohistoric datasets  
- Cultural framing avoiding colonial language  
- Documentation of all ethical choices  
- Generalization or obfuscation of sensitive regions  

### Forbidden:
- `"restricted"` CARE classification  
- Exact cultural boundaries  
- Restricted ceremonial or oral-history content  

---

# 🧪 Validation Requirements

STAC Items and Collections must pass:

1. `stac-item-schema.json`  
2. `stac-collection-schema.json`  
3. `kfm-archaeology-extension.json`  
4. `care-sensitivity-extension.json`  
5. `dcat-crosswalk.json`  
6. Provenance linkage validation  
7. Spatial generalization validation  

CI workflows include:

- `artifact-stac-validate.yml`  
- `metadata-validate.yml`  
- `faircare-audit.yml`

---

# 🧠 KFM Ecosystem Integration

### Knowledge Graph
Nodes:
- `InteractionSphere`  
- `CulturalPhase`  
- `EnvironmentalRegion`  
- `CulturalRegion`  

Edges:
- `GENERALIZED_FROM`  
- `ASSOCIATED_WITH`  
- `OCCURRED_DURING`  
- `HAS_PROVENANCE`  
- `HAS_METADATA`  
- `CARE_SENSITIVITY`  

### Story Nodes
Used for:
- Cultural exchange narratives  
- Movement patterns  
- Multiregional synthesis  

### Focus Mode v2
Provides:
- Cultural overlay rendering  
- Provenance-aware interpretations  
- Ethical transparency prompts  

---

# 📊 Catalog Index

| STAC Item | Collection | Sensitivity | Review | Status |
|---|---|---|---|---|
| `great-bend-aspect-v2.json` | GBA | generalized | FAIR+CARE | 🟢 Active |
| `central-plains-exchange-v1.json` | CPE | generalized | FAIR+CARE | 🟢 Active |
| `protohistoric-wichita-v1.json` | Wichita | restricted-generalized | Tribal | 🟡 Needs Review |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Created full STAC catalog system for Interaction Spheres including STAC/DCAT/CARE alignment |
| v10.0.0 | 2025-11-10 | Landscape Metadata Team | Initial catalog scaffold |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Interaction Spheres](../README.md)

</div>