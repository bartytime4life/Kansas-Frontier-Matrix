---
title: "🧬 Kansas Frontier Matrix — Artifact Inventory Provenance Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/provenance/templates/README.md"
description: "Template library for PROV-O + CARE JSON-LD provenance logs for KFM v11 artifact inventories."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventory-provenance-templates-v11.2.3"
doc_kind: "Template Library"
intent: "artifact-inventory-provenance-templates"
semantic_document_id: "kfm-doc-archaeology-artifact-inventory-provenance-templates-v11.2.3"
category: "Analyses · Archaeology · Provenance · Templates"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-artifact-inventory-provenance-templates-v1.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

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

data_steward: "Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/provenance/templates/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🧬 Kansas Frontier Matrix — Artifact Inventory Provenance Templates (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/provenance/templates/README.md`

**Purpose**  
Provide a library of **PROV-O + CARE JSON-LD templates** for artifact inventory provenance logs in KFM v11.

These templates ensure that provenance records are:

- Structurally complete and PROV-O–compliant  
- Culturally safe and sovereignty-aligned (CARE + sovereignty policy)  
- Compatible with KFM archaeology pipelines, STAC, and DCAT  
- Ready for ingestion into the KFM knowledge graph, Story Nodes, and Focus Mode v3  

Every artifact inventory MUST have a provenance JSON derived from one of these templates.

---

## 📘 Overview

Templates in this directory help contributors produce standardized, machine-readable provenance logs describing:

- **Origins**  
  - Source repositories (museums, archives, universities, PD portals, field projects).  
- **Transformations**  
  - Cleaning, normalization, classification, column mapping, encoding fixes.  
- **Cultural and sovereignty review**  
  - FAIR+CARE and tribal review activities, outcomes, and conditions.  
- **Spatial generalization**  
  - H3 level used, coordinate removal, precision reduction, any redaction.  
- **Uncertainty and assumptions**  
  - Known limitations, approximations, or interpretive steps.  
- **Tools and pipelines**  
  - Scripts, versions, container images, and configuration IDs.  
- **Version lineage**  
  - Raw → v1 → vN transitions and reasons for major changes.

These logs are critical for:

- Ethical governance and auditability  
- Scientific reproducibility  
- Explainable AI behavior in Focus Mode  
- Story Node provenance chips and narrative context  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/provenance/templates/
├── 📄 README.md                           # This file (template library index)
├── 📄 template_provenance_lithics.json    # Lithic artifact inventory provenance template
├── 📄 template_provenance_ceramics.json   # Ceramic artifact inventory provenance template
├── 📄 template_provenance_metals.json     # Protohistoric / metal artifact provenance template
├── 📄 template_provenance_faunal.json     # Faunal (public-domain oriented) provenance template
└── 📂 annotated/                          # Annotated templates with explanatory comments
~~~

This layout is **normative** for artifact-inventory provenance templates.

---

## 🧩 Common Template Structure

All provenance templates follow a **JSON-LD PROV-O pattern** with KFM and CARE namespaces.

### Required top-level components

- `@context`  
  - Includes `prov`, `care`, and `kfm` namespaces.  
- `prov:Entity`  
  - Describes raw and processed datasets.  
- `prov:Activity`  
  - Describes processing, generalization, and review steps.  
- `prov:Agent`  
  - Describes analysts, working groups, councils, and tribal reviewers.  
- PROV-O relations  
  - `prov:wasDerivedFrom`, `prov:wasGeneratedBy`, `prov:used`, `prov:wasAttributedTo`.  
- CARE & KFM fields  
  - `care:sensitivity`, `care:review`, `care:notes`, `care:visibility_rules`.  
  - `kfm:provenance_version`, `kfm:source`, `kfm:generalization`, etc.

Templates are intentionally minimal but enforce the core structure required by KFM’s provenance schema.

---

## 🧱 Template — Lithic Artifact Provenance (Minimal)

`template_provenance_lithics.json` (illustrative pattern):

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
      "kfm:provenance_version": "v11"
    }
  },

  "prov:Activity": {
    "cleaning": {
      "prov:type": "Cleaning",
      "prov:startTime": "YYYY-MM-DDThh:mm:ssZ",
      "prov:endTime": "YYYY-MM-DDThh:mm:ssZ",
      "kfm:steps": [
        "column standardization",
        "type harmonization",
        "duplicate removal"
      ]
    },
    "generalization": {
      "prov:type": "SpatialGeneralization",
      "prov:startTime": "YYYY-MM-DDThh:mm:ssZ",
      "prov:endTime": "YYYY-MM-DDThh:mm:ssZ",
      "kfm:generalization": "H3-r7"
    }
  },

  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "ANALYST NAME"
    },
    "reviewer": {
      "prov:type": "Organization",
      "prov:label": "FAIR+CARE Council"
    }
  },

  "prov:wasDerivedFrom": [
    {
      "prov:generatedEntity": "processed",
      "prov:usedEntity": "raw"
    }
  ],

  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Spatial generalization applied using H3-r7; no site-level coordinates retained.",
  "care:visibility_rules": "no-exact-points"
}
~~~

---

## 🧱 Template — Ceramic Artifact Provenance (Motif-Sensitive)

`template_provenance_ceramics.json` (motif-aware pattern):

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
      "care:notes": "Raw motif fields may include culturally restricted designs."
    },
    "processed": {
      "prov:label": "Processed Ceramic Inventory",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v11",
      "care:notes": "Restricted motifs removed or generalized prior to publication."
    }
  },

  "prov:Activity": {
    "motif_filtering": {
      "prov:type": "Filtering",
      "prov:startTime": "YYYY-MM-DDThh:mm:ssZ",
      "prov:endTime": "YYYY-MM-DDThh:mm:ssZ",
      "kfm:steps": [
        "remove restricted motifs",
        "generalize motif classes",
        "apply CARE motif policy"
      ]
    }
  },

  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "ANALYST NAME"
    },
    "reviewer": {
      "prov:type": "Organization",
      "prov:label": "FAIR+CARE Council"
    }
  },

  "prov:wasDerivedFrom": [
    {
      "prov:generatedEntity": "processed",
      "prov:usedEntity": "raw"
    }
  ],

  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Motif categories generalized to protect cultural knowledge; restricted designs removed.",
  "care:visibility_rules": "no-exact-points"
}
~~~

---

## 🧱 Template — Metals / Protohistoric Provenance (Tribal Review)

`template_provenance_metals.json` (sovereignty-focused):

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
      "kfm:provenance_version": "v11",
      "care:notes": "Dataset filtered and generalized following tribal review."
    }
  },

  "prov:Activity": {
    "cultural_consultation": {
      "prov:type": "Consultation",
      "prov:startTime": "YYYY-MM-DDThh:mm:ssZ",
      "prov:endTime": "YYYY-MM-DDThh:mm:ssZ",
      "kfm:steps": [
        "tribal consultation",
        "ethical filtering based on feedback"
      ]
    }
  },

  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "ANALYST NAME"
    },
    "tribal_reviewer": {
      "prov:type": "Organization",
      "prov:label": "Tribal Heritage Office"
    }
  },

  "prov:wasDerivedFrom": [
    {
      "prov:generatedEntity": "processed",
      "prov:usedEntity": "raw"
    }
  ],

  "care:sensitivity": "restricted-generalized",
  "care:review": "tribal",
  "care:notes": "Contact-era metal artifacts reviewed by tribal representatives; sensitive associations generalized.",
  "care:visibility_rules": "h3-only"
}
~~~

---

## 🧱 Template — Faunal Provenance (Public-Domain Oriented)

`template_provenance_faunal.json`:

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
      "kfm:provenance_version": "v11"
    }
  },

  "prov:Activity": {
    "cleaning": {
      "prov:type": "Cleaning",
      "kfm:steps": [
        "remove non-faunal records",
        "normalize species names",
        "drop ambiguous identifications"
      ]
    }
  },

  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "ANALYST NAME"
    }
  },

  "prov:wasDerivedFrom": [
    {
      "prov:generatedEntity": "processed",
      "prov:usedEntity": "raw"
    }
  ],

  "care:sensitivity": "general",
  "care:review": "none-required",
  "care:notes": "Dataset verified PD-safe; sacred species and sensitive contexts removed as needed."
}
~~~

---

## 🧪 Validation Requirements

Provenance logs generated from these templates must satisfy:

- **Schema validation**  
  - Against KFM’s PROV-O/CARE provenance schema (see `stac/schemas/`).  
- **CARE validation**  
  - `care:*` fields must use allowed values and match governance decisions.  
- **Cross-linking checks**  
  - STAC Items refer to the correct provenance file via `kfm:provenance`.  
  - Paths align with actual file locations in `../provenance/`.  

Validation is enforced via CI workflows such as:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  
- Any FAIR+CARE governance audit workflows configured for KFM v11.

---

## 🧠 Integration Within KFM

- **STAC & DCAT**  
  - STAC Items use `properties.kfm:provenance` to link to provenance JSON.  
  - DCAT manifests can expose provenance URIs and summaries.

- **Knowledge Graph**  
  - Provenance entities and activities are converted into graph nodes and edges.  
  - CARE and sovereignty flags propagate into graph-level views.

- **Story Nodes & Focus Mode v3**  
  - Provenance records drive provenance chips, sensitivity-aware responses, and AI transparency.  
  - CARE and sovereignty metadata from provenance logs guide how stories and analyses are presented.

---

## 🕰 Version History

| Version   | Date       | Author                                             | Summary                                                                 |
|-----------|------------|----------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee | Updated templates to KFM v11.2.3; added energy/carbon telemetry refs; clarified sovereignty and Focus Mode v3 integration. |
| v10.4.0   | 2025-11-17 | Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee | Created provenance template suite with PROV-O + CARE patterns and validation guidance. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team                             | Initial provenance template directory scaffold.                         |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Provenance](../README.md)
