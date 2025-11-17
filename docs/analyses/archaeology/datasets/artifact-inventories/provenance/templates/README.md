---
title: "🧬 Kansas Frontier Matrix — Artifact Inventory Provenance Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/provenance/templates/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-inventory-provenance-templates-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Template Library"
intent: "artifact-inventory-provenance-templates"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Artifact Inventory Provenance Templates**  
`docs/analyses/archaeology/datasets/artifact-inventories/provenance/templates/README.md`

**Purpose:**  
Provide a library of **validated PROV-O lineage templates** for all artifact inventory datasets within the Kansas Frontier Matrix (KFM).  
These templates ensure contributors generate provenance logs that are:

- Complete  
- Culturally safe  
- FAIR+CARE–aligned  
- Compatible with KFM archaeology pipelines  
- Valid under **W3C PROV-O**, **DCAT**, **STAC**, and **CIDOC-CRM**  
- Traceable through ETL → Graph → Story Nodes → Focus Mode v2  

Every artifact inventory must include a provenance JSON built from one of these templates.

</div>

---

## 📘 Overview

The templates in this directory allow contributors to produce standardized, machine-readable **provenance logs** describing:

- Dataset origins (PD archives, museums, universities)  
- Transformations applied (cleaning, classification, harmonization)  
- Cultural review processes (FAIR+CARE + tribal review when required)  
- Generalization procedures (H3 level, coordinate obfuscation)  
- Uncertainty, assumptions, and biases  
- Scripts, pipelines, and versions used  
- Dataset lineage from raw → processed → published  

These logs are critical for:

- Ethical governance  
- Reproducibility  
- Validation  
- AI interpretability  
- KFM governance reports  
- Story Node provenance chips  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/provenance/templates/
├── README.md                           # This file
├── template_provenance_lithics.json    # Lithic artifact provenance template
├── template_provenance_ceramics.json   # Ceramic dataset provenance template
├── template_provenance_metals.json     # Protohistoric metal provenance template
├── template_provenance_faunal.json     # Faunal (PD-only) provenance template
└── annotated/                          # Annotated templates with explanatory comments
~~~

---

# 🧩 Template Structure Overview (All Provenance Files)

Each template follows the **W3C PROV-O JSON-LD pattern**, with KFM archaeological extensions.

### Required Components

| Component | Purpose |
|---|---|
| `@context` | Defines JSON-LD namespaces for PROV, CARE, KFM |
| `prov:Entity` | Raw & processed datasets |
| `prov:Activity` | Cleaning, filtering, classification steps |
| `prov:Agent` | Analysts, reviewers, institutions |
| `prov:wasDerivedFrom` | Raw → processed lineage |
| `care:*` | Cultural-safety metadata |
| `kfm:*` | Domain-specific provenance metadata |
| `dct:` | Crosswalk for DCAT metadata where relevant |

---

## 🧱 Template — Lithic Artifact Provenance (Minimal)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },

  "prov:Entity": {
    "raw": {
      "prov:label": "Raw Lithic Dataset",
      "prov:type": "Dataset",
      "kfm:source": "INSTITUTION",
      "kfm:collection_method": "download"
    },
    "processed": {
      "prov:label": "Processed Lithic Inventory",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v1"
    }
  },

  "prov:Activity": {
    "cleaning": {
      "prov:type": "Cleaning",
      "prov:startTime": "YYYY-MM-DDThh:mm:ssZ",
      "prov:endTime": "YYYY-MM-DDThh:mm:ssZ",
      "kfm:steps": ["column standardization", "type harmonization"]
    }
  },

  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "ANALYST NAME"
    },
    "reviewer": {
      "prov:type": "Group",
      "prov:label": "FAIR+CARE Council"
    }
  },

  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "processed", "prov:usedEntity": "raw" }
  ],

  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Spatial generalization applied using H3 level 6."
}
~~~

---

## 🧱 Template — Ceramic Artifact Provenance (Motif-Sensitive)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },

  "prov:Entity": {
    "raw": {
      "prov:label": "Raw Ceramic Motif Dataset",
      "prov:type": "Dataset",
      "kfm:source": "INSTITUTION",
      "care:notes": "Some motif fields required masking."
    },
    "processed": {
      "prov:label": "Processed Ceramic Inventory",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v1",
      "care:notes": "Restricted motifs removed before publication."
    }
  },

  "prov:Activity": {
    "motif_filtering": {
      "prov:type": "Filtering",
      "prov:startTime": "YYYY-MM-DDThh:mm:ssZ",
      "prov:endTime": "YYYY-MM-DDThh:mm:ssZ",
      "kfm:steps": ["remove restricted motifs", "reclassify generalized categories"]
    }
  },

  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "ANALYST NAME"
    },
    "reviewer": {
      "prov:type": "Group",
      "prov:label": "FAIR+CARE Council"
    }
  },

  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "processed", "prov:usedEntity": "raw" }
  ],

  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Motif generalization required to protect cultural knowledge."
}
~~~

---

## 🧱 Template — Metals / Protohistoric Provenance (Tribal Review Required)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },

  "prov:Entity": {
    "raw": {
      "prov:label": "Raw Protohistoric Metal Dataset",
      "prov:type": "Dataset",
      "kfm:source": "INSTITUTION"
    },
    "processed": {
      "prov:label": "Processed Metal Inventory",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v1",
      "care:notes": "Generalized after tribal review."
    }
  },

  "prov:Activity": {
    "cultural_consultation": {
      "prov:type": "Consultation",
      "prov:startTime": "YYYY-MM-DDThh:mm:ssZ",
      "prov:endTime": "YYYY-MM-DDThh:mm:ssZ",
      "kfm:steps": ["tribal consultation", "ethical filtering"]
    }
  },

  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "ANALYST NAME"
    },
    "tribal_reviewer": {
      "prov:type": "Group",
      "prov:label": "Tribal Heritage Office"
    }
  },

  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "processed", "prov:usedEntity": "raw" }
  ],

  "care:sensitivity": "restricted-generalized",
  "care:review": "tribal",
  "care:notes": "Contact-era metal artifacts require tribal consultation before dataset publication."
}
~~~

---

## 🧱 Template — Faunal Provenance (PD-Only)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },

  "prov:Entity": {
    "raw": {
      "prov:label": "Raw Faunal Dataset (PD)",
      "prov:type": "Dataset",
      "kfm:source": "Public Domain Repository"
    },
    "processed": {
      "prov:label": "Processed Faunal Dataset",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v1"
    }
  },

  "prov:Activity": {
    "cleaning": {
      "prov:type": "Cleaning",
      "kfm:steps": ["remove non-faunal records", "normalize species names"]
    }
  },

  "prov:Agent": {
    "analyst": { "prov:label": "ANALYST NAME" }
  },

  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "processed", "prov:usedEntity": "raw" }
  ],

  "care:sensitivity": "general",
  "care:review": "none-required"
}
~~~

---

# 🧪 Validation Requirements

All provenance logs produced from these templates must pass:

- **PROV-O structural validation**  
- **CARE cultural review validation**  
- **KFM provenance schema checks**  
- **DCAT/STAC crosswalk checks**  
- **CI pipelines:**  
  - `metadata-validate.yml`  
  - `artifact-stac-validate.yml`  
  - `faircare-audit.yml`  

Any mismatch halts ingestion.

---

# 🧠 Integration Into KFM

### Knowledge Graph
Provenance produces:

- `Dataset` → `PROV` edges  
- `Agent` nodes (analysts, councils, tribal reviewers)  
- `Activity` nodes for cleaning, filtering, consultation  

### Story Nodes
Provenance chips show:

- Data origins  
- Ethical review paths  
- Transformation logs  

### Focus Mode v2
Uses provenance to produce explainable narratives.

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council · Metadata Subcommittee | Created full provenance template suite with cultural safety logic and PROV-O mappings |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team | Initial template directory |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Provenance Templates](../README.md)

</div>