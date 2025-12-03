---
title: "🏺🧬 Kansas Frontier Matrix — Great Bend Aspect Interaction Sphere Provenance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/provenance/README.md"
description: "PROV-O + CARE provenance logs for the Great Bend Aspect interaction-sphere dataset in KFM v11, documenting lineage, generalization, and FAIR+CARE review."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Review Recommended"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-interaction-sphere-great-bend-aspect-provenance-v11.2.3"
doc_kind: "Provenance Record Index"
intent: "great-bend-aspect-provenance"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-great-bend-aspect-provenance-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Provenance"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-great-bend-aspect-provenance-v1.json"
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
care_label: "CARE-Compliant (Elevated Sensitivity)"
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
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/provenance/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🏺🧬 Great Bend Aspect Interaction Sphere — Provenance Logs (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/provenance/README.md`

**Purpose**  
Serve as the **provenance record index** for the **Great Bend Aspect (GBA) Interaction Sphere** in KFM v11, documenting:

- Data origins and citations.  
- Spatial generalization and masking steps.  
- Cultural-phase synthesis and modeling choices.  
- FAIR+CARE ethical review outcomes.  
- Optional tribal advisory review notes.  
- Lineage from **raw → generalized → processed** representations.  

These logs use **PROV-O JSON-LD** plus CARE and KFM extensions to ensure machine readability, graph compatibility, and reproducibility.

---

## 📘 Overview

The provenance logs in this folder record:

- **Source evidence**:
  - Public-domain archaeological literature and syntheses.  
  - Approved open datasets and environmental covariates.  
- **Processing and generalization**:
  - H3 mosaics, polygon simplification, and boundary smoothing.  
- **Cultural synthesis**:
  - How interaction spheres were interpreted from multiple lines of evidence.  
- **Ethical and CARE review**:
  - FAIR+CARE review for cultural safety and neutrality.  
  - Tribal advisory review notes where consultation is sought.  
- **Uncertainty and limitations**:
  - Statements of interpretive uncertainty and model assumptions.  

These provenance records are integral for:

- KFM **Knowledge Graph** ingestion.  
- Story Node v3 narratives.  
- Focus Mode v3 explanation chips and ethical framing.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/provenance/
├── 📄 README.md                         # This file
└── 📄 great-bend-aspect-v2.json         # PROV-O lineage & cultural review metadata (v2)
~~~

Additional versioned provenance files (for earlier or internal iterations) may be added as needed, but `v2` is the authoritative lineage for KFM v11.

---

## 🧩 Required PROV-O Components for GBA Provenance

All provenance files MUST:

- Be valid **JSON-LD**.  
- Conform to **PROV-O** and KFM provenance schemas.  
- Include top-level CARE fields appropriate for **elevated sensitivity**.

### 1️⃣ `@context`

Each provenance JSON MUST include:

- `"prov"` — `http://www.w3.org/ns/prov#` (PROV-O core).  
- `"care"` — CARE cultural-sensitivity extension namespace.  
- `"kfm"` — KFM core/extension namespace.  
- `"dct"` — `http://purl.org/dc/terms/` (for DCAT-aligned provenance metadata).  

Optional:

- `"crm"` — CIDOC-CRM mapping, if advanced heritage modeling is used.

---

### 2️⃣ `prov:Entity`

Entities must model the main dataset states:

| Entity Key     | Description                                                       |
|----------------|-------------------------------------------------------------------|
| `raw`          | Aggregated public-domain archaeological syntheses (no restricted data). |
| `generalized`  | Spatially obfuscated form (for example, H3-level mosaic + simplified polygons). |
| `processed`    | Final dataset used in STAC Item(s) and public-governed KFM layers. |
| `interpretive` | (Optional) explicitly modeled cultural synthesis layers.          |

`raw` MUST NOT include:

- Site-precise coordinates.  
- Ceremonial or sacred landscape geometries.  
- Restricted oral histories or ethnographic content.  
- Non-consented high-resolution archaeological data.

Each `prov:Entity` should include:

- `prov:type` (usually `"Dataset"`).  
- `prov:label`.  
- `kfm:source` and `kfm:provenance_version` where applicable.

---

### 3️⃣ `prov:Activity`

Activities document each transformation and review event, such as:

| Activity Key        | Purpose                                                     |
|---------------------|-------------------------------------------------------------|
| `generalization`    | Creation of H3 mosaic, polygon simplification, and masking. |
| `cleaning`          | Harmonization of attributes, CRS normalization, naming.     |
| `integration`       | Multi-source archaeological and environmental synthesis.    |
| `faircare_review`   | FAIR+CARE ethical review of content and generalization.     |
| `tribal_advisory_review` | (Recommended) involvement of descendant communities. |

Each `prov:Activity` MUST include:

- `prov:type`.  
- `prov:startTime` and `prov:endTime` (ISO 8601).  
- `kfm:steps`: array detailing major pipeline actions.

---

### 4️⃣ `prov:Agent`

Agents represent responsible people and organizations:

| Agent Type           | Examples                                      |
|----------------------|-----------------------------------------------|
| Analyst              | GIS or archaeology specialist                 |
| FAIR+CARE Reviewer   | FAIR+CARE Council members                     |
| Tribal Advisory (optional) | Wichita-affiliated or other tribal heritage offices |
| Source Institution   | Public-domain archives, repositories, or institutions |

Agent entries should respect privacy/sovereignty constraints; roles and groups may be used in place of individual names where appropriate.

---

### 5️⃣ Lineage Relationships

Each provenance file MUST define:

- `prov:wasDerivedFrom` — chaining `raw → generalized → processed`.  
- `prov:wasGeneratedBy` — linking entities to generating activities.  
- `prov:used` — linking activities to the entities they consume.  
- `prov:wasAttributedTo` — linking entities to agents for responsibility and credit.

These relations jointly encode the reproducible lineage from initial sources to final KFM datasets.

---

## ⚖️ CARE Cultural-Safety Requirements (Elevated Sensitivity)

While the Great Bend Aspect is not flagged as high-sensitive to the same degree as, for example, Protohistoric Wichita, it still has **elevated sensitivity**, especially in protohistoric contexts.

### Required CARE Fields (Top-Level)

| Field                | Expected Values / Notes                                 |
|----------------------|---------------------------------------------------------|
| `care:sensitivity`   | `"generalized"`                                         |
| `care:review`        | `"faircare"` (tribal advisory review **recommended**)   |
| `care:notes`         | Required; must describe generalization and redaction decisions. |
| `care:visibility_rules` | `"polygon-generalized"` or `"h3-only"` where tighter protection is needed |

### Forbidden

- `care:sensitivity = "restricted"` in public-governed provenance.  
- Any indication that would expose sacred or ceremonial locations.  
- Direct inclusion of restricted oral histories without explicit, documented consent.

CARE metadata in provenance MUST align with:

- STAC Item CARE fields (`../stac/great-bend-aspect-v2.json`).  
- Metadata CARE fields (`../metadata/great-bend-aspect-v2.json`).

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
      "prov:label": "Late Prehistoric and Protohistoric GBA synthesis from PD archaeological literature",
      "kfm:source": "Open archaeological syntheses and regional survey reports"
    },
    "generalized": {
      "prov:type": "Dataset",
      "prov:label": "Generalized GBA interaction sphere (H3-r7 MultiPolygon)",
      "care:notes": "Settlement clusters and any sensitive localities removed prior to H3 aggregation and polygon simplification."
    },
    "processed": {
      "prov:type": "Dataset",
      "prov:label": "Great Bend Aspect Interaction Sphere v2",
      "kfm:provenance_version": "v2"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "SpatialGeneralization",
      "prov:startTime": "2025-10-14T13:12:00Z",
      "prov:endTime": "2025-10-14T13:55:00Z",
      "kfm:steps": [
        "H3 mosaic derivation (level 7)",
        "polygon simplification",
        "boundary smoothing",
        "removal of any site-precise and sacred features"
      ]
    },
    "faircare_review": {
      "prov:type": "Review",
      "prov:endTime": "2025-10-15T17:30:00Z",
      "kfm:steps": [
        "ethical language audit",
        "cultural sensitivity classification",
        "confirmation of generalization thresholds"
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
  "care:notes": "Spatial generalization and attribute filtering applied; no sacred or site-precise information included.",
  "care:visibility_rules": "polygon-generalized"
}
~~~

This example is illustrative; authoritative constraints are defined by provenance schemas under `../../provenance/` and `../../stac/schemas/`.

---

## 🧠 Integration Into KFM Ecosystem

### Knowledge Graph

From the Great Bend Aspect provenance logs, KFM ingests:

**Nodes**

- `InteractionSphere` (Great Bend Aspect).  
- `GeneralizedRegion` entities derived from the generalized polygons.  
- `ProvenanceActivity` nodes (generalization, cleaning, review).  
- `ReviewEvent` nodes (FAIR+CARE reviews; any tribal advisory events).  

**Relationships**

- `HAS_PROVENANCE` (InteractionSphere → ProvenanceRecord).  
- `GENERALIZED_FROM` (Processed ↔ Generalized ↔ Raw Entities).  
- `REVIEWED_BY` (ProvenanceRecord → Agents/Organizations).  
- `HAS_CARE_SENSITIVITY` (InteractionSphere → CARE state node).  

### Story Nodes & Focus Mode v3

- Story Nodes use provenance to:
  - Ground narratives in documented lineage and generalization choices.  
  - Display provenance chips and context banners.  

- Focus Mode uses CARE + provenance to:
  - Bound responses spatiotemporally and ethically.  
  - Avoid exposing unsafe detail.  
  - Surface warnings and disclaimers for interpretive content.

---

## 🔗 Related Specifications

- `../README.md`  
  – Great Bend Aspect interaction-sphere dataset overview.  
- `../stac/README.md`  
  – Great Bend Aspect STAC catalog (Collection + Item).  
- `../metadata/README.md`  
  – Great Bend Aspect metadata specification.  
- `../../provenance/README.md`  
  – Global interaction-sphere provenance standards and templates.

---

## 🕰 Version History

| Version   | Date       | Author                                             | Summary                                                                 |
|-----------|------------|----------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council          | Updated for KFM v11.2.3; aligned with interaction-sphere provenance standards; added telemetry refs and clarified CARE semantics. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council          | Initial Great Bend Aspect provenance index; defined PROV-O and CARE requirements for elevated sensitivity. |
| v10.0.0   | 2025-11-10 | Landscape Provenance Team                          | Prototype lineage description and generalization workflow notes.       |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Great Bend Aspect Dataset](../README.md)
