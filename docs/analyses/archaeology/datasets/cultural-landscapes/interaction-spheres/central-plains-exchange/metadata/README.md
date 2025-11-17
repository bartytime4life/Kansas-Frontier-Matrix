---
title: "🔄📑 Kansas Frontier Matrix — Central Plains Exchange Interaction Sphere Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/metadata/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape WG · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-central-plains-exchange-metadata-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Metadata"
intent: "central-plains-exchange-metadata"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🔄📑 **Central Plains Exchange Interaction Sphere Metadata**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/metadata/README.md`

**Purpose:**  
Provide the full **DCAT + STAC-aligned + CARE-governed metadata specification** for the **Central Plains Exchange Interaction Sphere** dataset within the Kansas Frontier Matrix (KFM).  
This metadata governs transparency, cultural safety, ontology mapping, and reproducibility for this multi-phase cultural-interaction region.

</div>

---

# 📘 Overview

The **Central Plains Exchange Interaction Sphere** is a multi-century cultural network zone associated with:

- Central Plains Tradition (CPT) communities  
- Cross-drainage interaction between Republican, Solomon, Smoky Hill & Platte rivers  
- Shared ceramic, lithic, and architectural traits  
- Long-distance material exchange  
- Paleoenvironmental drivers (prairie–riverine ecotones)  

This metadata file documents:

- Dataset-level description  
- Cultural and ethical considerations  
- Temporal boundaries  
- Spatial generalization methods  
- FAIR+CARE classification  
- KFM-specific archaeological metadata schema fields  
- Linkage to STAC + PROV-O provenance files  

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/metadata/
├── README.md                            # This file
└── central-plains-exchange-v1.json      # Primary metadata for this dataset
~~~

---

# 📦 Required Metadata (DCAT + KFM + CARE)

Each Interaction Sphere metadata file must include **all** required values from:

- **DCAT 3.0**
- **KFM Archaeology Metadata Standard**
- **CARE cultural governance**

The `central-plains-exchange-v1.json` file contains:

---

## ✔ DCAT 3.0 Fields

| Field | Example | Purpose |
|---|---|---|
| `dct:title` | `"Central Plains Exchange Interaction Sphere v1"` | Human-readable dataset title |
| `dct:description` | `"Generalized multi-phase cultural interaction region across Central Plains drainages"` | Dataset summary |
| `dct:license` | `"CC-BY-4.0"` | Open data requirement |
| `dct:temporal` | `"AD 900–1400"` | OWL-Time-compliant time span |
| `dcat:keyword` | `["CPT", "exchange zone", "archaeology", "Kansas"]` | Searchability |
| `dcat:distribution` | `"../../stac/central-plains-exchange-v1.json"` | STAC mapping |

---

## ✔ KFM Cultural Landscape Metadata

| Field | Value | Description |
|---|---|---|
| `kfm:landscape_type` | `"interaction_sphere"` | Required for this dataset category |
| `kfm:culture_phase` | `["CPT-Early","CPT-Middle","CPT-Late"]` | Cultural phases represented |
| `kfm:geometry_generalization` | `"H3-level-6"` | Spatial generalization for safety |
| `kfm:source` | `"Archaeological synthesis (PD)"` | Dataset provenance |
| `kfm:provenance` | `"../../provenance/central-plains-exchange-v1.json"` | PROV-O lineage |
| `kfm:schema_version` | `"1.0.0"` | Metadata schema version |

---

## ✔ CARE Cultural Safety Metadata

Interaction Spheres must always include CARE metadata.

| CARE Field | Allowed Values | Notes |
|---|---|---|
| `care:sensitivity` | `"generalized"` | Standard for spheres without protohistoric sensitivity |
| `care:review` | `"faircare"` | Cultural safety committee review |
| `care:notes` | `"Generalization applied to protect sensitive landscapes."` | Summary of decisions |
| `care:visibility_rules` | `"polygon-generalized"` | Public-facing geometry constraints |

Prohibited:
- `"restricted"`  
- Exact boundaries  
- Sensitive heritage data  

---

# 🌍 Spatial Metadata Requirements

Required elements:

- CRS: **EPSG:4326**  
- Geometry: generalized `MultiPolygon`  
- Bounding box must reflect generalized extent  
- H3 generalization or polygon simplification required  
- Sensitive locations fully removed  

Dataset does **not** contain:

- Exact site coordinates  
- Sacred places  
- Survey-level data  

---

# 🕰️ Temporal Metadata Requirements

- Earliest + latest cultural-phase dates  
- OWL-Time compliant formatting  
- Notes on uncertainty allowed  
- Multi-era metadata required for CPT-wide interactions  

---

# ⚖️ Ethical & Cultural Governance

This dataset intersects with areas of regional heritage but **does not** include protohistoric or highly sensitive content.  
Still, the following are required:

- FAIR+CARE ethics review  
- Neutral language avoiding colonial framing  
- Transparency in generalization choices  
- Alignment with descendant community expectations  
- Exclusion of sacred, restricted, or harmful content  

---

# 🧪 Provenance Linkage

The metadata file references:  
`../../provenance/central-plains-exchange-v1.json`

Provenance logs include:

- Evidence synthesis  
- GIS generalization  
- Literature/PD sources  
- Cultural review notes  
- Versioning & steps taken  

---

# 🧠 Integration Into KFM Ecosystem

### Knowledge Graph
Metadata generates/links to:

- `InteractionSphere`  
- `CulturalPhase`  
- `GeneralizedRegion`  

Edges:

- `HAS_METADATA`  
- `HAS_PROVENANCE`  
- `OCCURRED_DURING`  
- `ASSOCIATED_WITH`  

### Story Nodes
Provides:

- Cultural-phase context  
- Interaction-network framing  
- Landscape-scale narratives  

### Focus Mode v2
Metadata powers:

- Sensitivity badges  
- Provenance-chip overlays  
- Context-aware cultural explanations  

---

# 📊 Metadata Summary Table

| Field | Value |
|---|---|
| Title | Central Plains Exchange Interaction Sphere v1 |
| Geometry | MultiPolygon (generalized, H3-level-6) |
| Sensitivity | generalized |
| Review | FAIR+CARE |
| Cultural Phases | CPT Early/Middle/Late |
| Provenance | Included |
| Status | 🟢 Active |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE | Initial metadata release for Central Plains Exchange Interaction Sphere |
| v0.1 | 2025-11-10 | Landscape Metadata Team | Prototype metadata draft |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Central Plains Exchange Dataset](../README.md)

</div>