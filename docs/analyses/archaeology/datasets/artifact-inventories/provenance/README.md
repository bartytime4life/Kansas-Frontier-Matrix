---
title: "🧬 Kansas Frontier Matrix — Artifact Inventory Provenance Logs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/provenance/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-inventory-provenance-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Provenance Logs"
intent: "artifact-inventory-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Artifact Inventory Provenance Logs**  
`docs/analyses/archaeology/datasets/artifact-inventories/provenance/README.md`

**Purpose:**  
Serve as the authoritative **provenance repository** for all artifact inventory datasets used in the Kansas Frontier Matrix (KFM).  
These logs capture **data lineage**, **methodological transparency**, and **ethical review trails**, ensuring compliance with **FAIR+CARE**, **PROV-O**, **STAC 1.0**, **DCAT 3.0**, and **MCP-DL v6.3**.

Every artifact inventory MUST include a corresponding provenance record in this directory.

</div>

---

## 📘 Overview

Provenance logs in this directory document:

- **Source origins** (museum, archive, academic repository, PD dataset)  
- **Data acquisition method** (download, scraping, API fetch)  
- **Processing steps** (cleaning, categorization, normalization)  
- **Cultural review** (FAIR+CARE; tribal or expert review notes)  
- **Generalization steps** (H3 mapping, coordinate removal)  
- **Transformations** (schema harmonization, encoding conversion)  
- **Analyst & reviewer attribution**  
- **Version history** for each artifact inventory  

Each provenance file acts as the ground-truth metadata chain linking raw data to final KFM-ready datasets.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/provenance/
├── README.md                                   # This file
├── flint-hills-lithics-v1.json                 # Provenance for lithic inventory
├── prairie-ceramics-v1.json                    # Provenance for ceramic inventory
├── contact-era-metals-v1.json                  # Provenance (pending review)
├── fauna-open-v1.json                          # Provenance for open-access fauna dataset
└── templates/                                  # Provenance JSON-LD template definitions
~~~

---

## 📦 Required PROV-O Components (All Provenance Files)

Each provenance log MUST include the following PROV-O structures:

### ✔ Entities

| Field | Description | Example |
|---|---|---|
| `prov:Entity` | Raw or processed dataset | `"artifact_inventory_raw.csv"` |
| `prov:label` | Descriptive label | `"Flint Hills Lithics Inventory - Raw"` |
| `prov:type` | `"Dataset"` or `"File"` | `"Dataset"` |

### ✔ Activities

| Field | Description | Example |
|---|---|---|
| `prov:Activity` | A data processing step | `"Cleaning"`, `"Normalization"` |
| `prov:startTime` | ISO timestamp | `"2025-10-01T14:32:00Z"` |
| `prov:endTime` | ISO timestamp | `"2025-10-01T15:10:00Z"` |

### ✔ Agents

| Field | Description | Example |
|---|---|---|
| `prov:Agent` | Person or organization | `"Kansas Frontier Matrix Archaeology WG"` |
| `prov:type` | `"Person"` or `"Organization"` | `"Person"` |
| `prov:actedOnBehalfOf` | Group/committee responsible | `"FAIR+CARE Council"` |

### ✔ Relations

| Relation | Description |
|---|---|
| `prov:wasDerivedFrom` | Raw → cleaned dataset |
| `prov:wasGeneratedBy` | Activity → dataset |
| `prov:used` | Activity uses an Entity |
| `prov:wasAttributedTo` | Dataset attributed to Agent |

### ✔ CARE Metadata Layer

| Field | Description |
|---|---|
| `care:sensitivity` | `"general"`, `"generalized"`, `"restricted-generalized"` |
| `care:review` | `"tribal"`, `"faircare"`, `"none-required"` |
| `care:notes` | Cultural review notes |
| `care:visibility_rules` | `"h3-only"`, `"no-exact-points"` |

---

## 🧪 Provenance Log Template (JSON-LD)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },
  "prov:Entity": {
    "raw": {
      "prov:label": "Raw Artifact Inventory",
      "prov:type": "Dataset",
      "kfm:source": "WSU Open Collections"
    },
    "processed": {
      "prov:label": "Processed Artifact Inventory",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v1"
    }
  },
  "prov:Activity": {
    "cleaning": {
      "prov:startTime": "2025-10-01T14:32:00Z",
      "prov:endTime": "2025-10-01T15:10:00Z",
      "prov:type": "Cleaning"
    }
  },
  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "J. Barta"
    },
    "reviewer": {
      "prov:type": "Person",
      "prov:label": "FAIR+CARE Council"
    }
  },
  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "processed", "prov:usedEntity": "raw" }
  ],
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Decorative motif categories reviewed for cultural sensitivity."
}
~~~

---

## 🗺️ Integration Into KFM Ecosystem

Provenance files support:

### **Metadata Layer**
- STAC Items (`stac/`) reference provenance entries  
- DCAT metadata crosslinks provenance and source institutions  

### **Knowledge Graph (Neo4j)**
- `Artifact` → `provenance` links  
- `ArtifactInventory` → `prov:wasGeneratedBy`  

### **Focus Mode v2**
- Provenance chips appear in AI-generated summaries  
- AI contextualization respects CARE constraints via provenance flags  

### **Story Nodes**
- Provide narrative-level data origins and ethical context  

---

## 📊 Provenance File Index

| Provenance File | Dataset | Status | Last Review | Notes |
|---|---|---|---|---|
| `flint-hills-lithics-v1.json` | Lithics | 🟢 Active | 2025-11 | Fully validated |
| `prairie-ceramics-v1.json` | Ceramics | 🟢 Active | 2025-10 | CARE review complete |
| `contact-era-metals-v1.json` | Protohistoric Metals | 🟡 Needs Review | 2025-09 | Tribal consultation pending |
| `fauna-open-v1.json` | Faunal (PD only) | 🟢 Active | 2025-11 | Verified PD provenance |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Added provenance structure, PROV-O/CARE requirements, validation rules, and index |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial provenance framework |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Artifact Inventories](../README.md)

</div>