---
title: "🔄🧬 Kansas Frontier Matrix — Central Plains Exchange Interaction Sphere Provenance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/provenance/README.md"
description: "PROV-O + CARE provenance logs for the Central Plains Exchange interaction-sphere dataset in KFM v11, documenting lineage, generalization, and FAIR+CARE review."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council (Tribal Review Not Required for This Sphere)"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-sphere-central-plains-exchange-provenance-v11.2.3"
doc_kind: "Provenance Record Index"
intent: "cultural-landscape-interaction-sphere-central-plains-exchange-provenance"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-central-plains-exchange-provenance-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Provenance"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-central-plains-exchange-provenance-v1.json"
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
care_label: "CARE-Compliant (Generalized)"
sensitivity: "Cultural / Historical / Archaeological"
sensitivity_level: "Medium"
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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/provenance/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🔄🧬 Central Plains Exchange Interaction Sphere — Provenance Logs (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/provenance/README.md`

**Purpose**  
Provide the authoritative **provenance index** for the **Central Plains Exchange Interaction Sphere** within the Kansas Frontier Matrix (KFM).

These provenance records ensure transparent documentation of:

- Dataset origins and source evidence.  
- GIS transformation and spatial generalization.  
- Cultural and ethical review under FAIR+CARE.  
- Methodological and modeling decisions.  
- Data lineage from **raw → generalized → processed**.  

This dataset is **moderate sensitivity** (CPT-focused, not protohistoric). It may be published following standard FAIR+CARE review; tribal review is **not required** but may be sought if later phases or overlaps warrant it.

---

## 📘 Overview

Provenance logs in this directory describe:

- **Source data** used to construct the interaction sphere:
  - Archaeological literature, regional syntheses, PD GIS data, environmental layers.  
- **Generalization workflow**:
  - H3 mosaics, polygon simplification, and boundary smoothing.  
- **Interpretive basis**:
  - How CPT interaction zones were inferred and delimited.  
- **Ethics and governance**:
  - FAIR+CARE review steps and sensitivity classification.  
- **Uncertainty and limitations**:
  - Model assumptions, bias discussions, and confidence levels.  
- **Versioning**:
  - Clear indication of provenance version tied to dataset release.

All logs are PROV-O JSON-LD documents, making them suitable for:

- ETL pipelines.  
- Neo4j ingestion.  
- Story Node v3 narratives.  
- Focus Mode v3 explanations.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/provenance/
├── 📄 README.md                               # This file
└── 📄 central-plains-exchange-v1.json         # PROV-O provenance for v1
~~~

Future versions (v2, etc.) should be added as separate JSON-LD files and linked from STAC + metadata.

---

## 🧩 Required PROV-O Components

All provenance logs must conform to:

- **JSON-LD** serialization.  
- **PROV-O** core structures (Entities, Activities, Agents, Relations).  
- KFM + CARE extension schemas for interaction spheres.

### 1️⃣ `@context`

Each provenance file MUST define:

- `"prov"` — W3C PROV-O vocabulary (`http://www.w3.org/ns/prov#`).  
- `"care"` — CARE extension namespace.  
- `"kfm"` — KFM core/extension namespace.  
- `"dct"` — DCAT terms (`http://purl.org/dc/terms/`).  

`"crm"` (CIDOC-CRM) is optional, used only when advanced heritage semantics are required.

---

### 2️⃣ `prov:Entity`

Required entities:

| Entity Key | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| `raw`      | Aggregated public-domain cultural/landscape sources (no restricted content) |
| `generalized` | H3/polygon generalized interaction sphere geometry                        |
| `processed`| Final KFM-ready dataset used by STAC Item(s)                               |

Optional:

- `interpretive` — explicitly modeled or synthetic cultural-synthesis layers.

`raw` must **not** include:

- Site-precise coordinates.  
- Sacred or ceremonial landscapes.  
- Restricted ethnographic or oral-historical content.  

Each `prov:Entity` should have:

- `prov:type` (usually `"Dataset"`).  
- `prov:label`.  
- `kfm:source` (for `raw`) and `kfm:provenance_version` (for `processed`).

---

### 3️⃣ `prov:Activity`

Required activity categories (names may vary, but semantics must match):

| Activity Key       | Description                                                              |
|--------------------|--------------------------------------------------------------------------|
| `generalization`   | H3-level derivation, polygon simplification, boundary smoothing.         |
| `integration`      | Combining archaeological, environmental, and other evidence.             |
| `cleaning`         | Attribute normalization, CRS harmonization, naming standards.            |
| `faircare_review`  | FAIR+CARE cultural and ethical review.                                   |
| `temporal_alignment` | Mapping phases to OWL-Time intervals and harmonizing temporal models. |

Each `prov:Activity` must include:

- `prov:type`.  
- `prov:startTime` and `prov:endTime` (ISO 8601).  
- `kfm:steps` — array summarizing the main actions taken.

---

### 4️⃣ `prov:Agent`

Agents must capture responsibility and oversight:

| Agent Type         | Example                                       |
|--------------------|-----------------------------------------------|
| Analyst            | Archaeologist / GIS specialist                |
| FAIR+CARE Reviewer | FAIR+CARE Council or equivalent group         |
| Source Institution | Public-domain archive, repository, or project |

Tribal agents are **optional** for this sphere but may be added if consultations occur.

Each agent should include:

- `prov:type` (`"Person"` or `"Organization"`).  
- `prov:label` (name or role).  

---

### 5️⃣ Lineage Relationships

All provenance records must include the core PROV-O relations:

- `prov:wasDerivedFrom` — chain `raw → generalized → processed`.  
- `prov:wasGeneratedBy` — link entities to the activities that created them.  
- `prov:used` — link activities to input entities.  
- `prov:wasAttributedTo` — attribute entities to agents.

These relations make lineage machine-traceable and graph-ready.

---

## ⚖️ CARE Cultural Safety Requirements

Although this sphere is **moderate sensitivity**, CARE governance still applies.

Required top-level CARE fields in the provenance JSON:

| Field                | Recommended Value / Notes                               |
|----------------------|--------------------------------------------------------|
| `care:sensitivity`   | `"generalized"`                                        |
| `care:review`        | `"faircare"`                                           |
| `care:notes`         | Narrative explaining removed or downscaled content and generalization rationale. |
| `care:visibility_rules` | `"polygon-generalized"` (or `"h3-only"` if later tightened) |

Forbidden for public-governed interaction spheres:

- `care:sensitivity = "restricted"`.  
- Exact boundaries or shapes that permit inference of protected sites.  
- Sacred or sensitive knowledge and site coordinates.

CARE settings must be consistent with metadata (`../metadata/`) and STAC (`../stac/`).

---

## 🧪 Example Provenance Snippet (Illustrative)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#",
    "dct": "http://purl.org/dc/terms/"
  },
  "prov:Entity": {
    "raw": {
      "prov:type": "Dataset",
      "prov:label": "Archaeological synthesis of CPT interaction networks",
      "kfm:source": "Public domain literature and regional survey data"
    },
    "generalized": {
      "prov:type": "Dataset",
      "prov:label": "Generalized Central Plains Exchange interaction sphere (H3-r7)",
      "care:notes": "Geomorphology-based boundary adjustment and removal of site-precise features."
    },
    "processed": {
      "prov:type": "Dataset",
      "prov:label": "Central Plains Exchange Interaction Sphere v1",
      "kfm:provenance_version": "v1"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "SpatialGeneralization",
      "prov:startTime": "2025-10-16T13:25:00Z",
      "prov:endTime": "2025-10-16T14:02:00Z",
      "kfm:steps": [
        "H3 indexing (level 7)",
        "polygon simplification",
        "boundary smoothing"
      ]
    },
    "faircare_review": {
      "prov:type": "Review",
      "prov:endTime": "2025-10-17T17:40:00Z",
      "kfm:steps": [
        "ethical language audit",
        "sensitivity classification as generalized"
      ]
    }
  },
  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "A. Barta"
    },
    "faircare": {
      "prov:type": "Organization",
      "prov:label": "FAIR+CARE Council"
    }
  },
  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "generalized", "prov:usedEntity": "raw" },
    { "prov:generatedEntity": "processed", "prov:usedEntity": "generalized" }
  ],
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Spatial generalization and attribute filtering applied to avoid revealing culturally meaningful landscapes.",
  "care:visibility_rules": "polygon-generalized"
}
~~~

This example is illustrative; actual provenance contents must follow KFM provenance schemas and refer to real activities and agents.

---

## 🧠 Integration Into KFM Ecosystem

### Knowledge Graph

Provenance logs contribute to:

**Nodes**

- `InteractionSphere` (Central Plains Exchange).  
- `GeneralizedRegion` entities.  
- `ProvenanceActivity` nodes (generalization, cleaning, integration, review).  
- `ReviewEvent` nodes (FAIR+CARE review).  
- `CareSensitivityState` or similar CARE-related nodes.

**Relationships**

- `HAS_PROVENANCE` (InteractionSphere → ProvenanceRecord).  
- `GENERALIZED_FROM` (Processed ↔ Generalized ↔ Raw datasets).  
- `REVIEWED_BY` (ProvenanceRecord → Agents).  
- `HAS_CARE_SENSITIVITY` (InteractionSphere → CARE state node).

### Story Nodes & Focus Mode v3

- Provide provenance-backed context for narratives about CPT exchanges and connectivity.  
- Enable Focus Mode to show provenance chips, warnings, and uncertainty notes.  
- Support ethical, transparent reasoning about the interaction sphere.

---

## 📊 Provenance Index (Illustrative)

| Provenance File                  | Version | Sensitivity  | Review     | Status   |
|----------------------------------|---------|--------------|-----------|----------|
| `central-plains-exchange-v1.json` | v1      | generalized  | FAIR+CARE | 🟢 Active |

Authoritative status and review metadata are maintained in manifests, metadata, and governance records.

---

## 🔗 Related Specifications

- `../README.md`  
  – Central Plains Exchange interaction-sphere dataset overview.  
- `../stac/README.md`  
  – Central Plains Exchange STAC documentation (Collection + Item).  
- `../metadata/README.md`  
  – Central Plains Exchange metadata specification.  
- `../../provenance/README.md`  
  – Global interaction-sphere provenance standards and templates.

---

## 🕰 Version History

| Version   | Date       | Author                                             | Summary                                                                 |
|-----------|------------|----------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council          | Updated for KFM v11.2.3; aligned with global interaction-sphere provenance standards; added telemetry refs and clarified CARE semantics. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council          | Initial Central Plains Exchange provenance index and PROV-O requirements. |
| v10.0.0   | 2025-11-10 | Landscape Provenance Team                          | Prototype lineage and generalization workflow notes.                    |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Central Plains Exchange Dataset](../README.md)
