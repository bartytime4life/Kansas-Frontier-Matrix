---
title: "📑 Kansas Frontier Matrix — Cultural Landscape Metadata Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/metadata/templates/README.md"
description: "Template library for DCAT + KFM + CARE JSON metadata describing KFM v11 cultural landscape datasets (regions, routes, interaction spheres, resource areas)."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:cultural-landscape-metadata-templates-v11.2.3"
doc_kind: "Template Library"
intent: "cultural-landscape-metadata-templates"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-metadata-templates-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Metadata · Templates"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-metadata-templates-v1.json"
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
care_label: "CARE-Compliant"
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
  - "docs/analyses/archaeology/datasets/cultural-landscapes/metadata/templates/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📑 Cultural Landscape Metadata Templates (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/metadata/templates/README.md`

**Purpose**  
Provide the official **metadata templates** for building JSON metadata files for all **cultural landscape datasets** in KFM v11:

- Regions and cultural areas  
- Interaction spheres  
- Mobility routes and trails  
- Resource procurement zones  
- Environmental–cultural synthesis layers  

These templates enforce:

- **DCAT 3.0** dataset metadata  
- **KFM cultural-landscape extensions (`kfm:*`)**  
- **CARE** cultural-safety metadata (`care:*`)  
- Provenance cross-linking to **PROV-O** logs  
- Alignment with KFM’s cultural-landscape metadata standards and STAC schemas  

Metadata created from these templates is stored in:

- `docs/analyses/archaeology/datasets/cultural-landscapes/metadata/`

---

## 📘 Overview

Cultural landscape metadata must:

- Respect Indigenous sovereignty and cultural sensitivity.  
- Use generalized spatial representations (no site-level detail).  
- Provide clear temporal context via phase/time intervals.  
- Link to provenance, STAC, and catalogs for full reproducibility.  
- Be validation-friendly and compatible with Story Nodes and Focus Mode v3.

This directory provides **non-annotated templates**; annotated “how-to” examples are expected to live in a sibling `annotated/` directory if needed.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/metadata/templates/
├── README.md                         # This file
├── template-metadata.json            # Full cultural-landscape metadata template
├── template-dcat-block.json          # DCAT-only snippet
├── template-kfm-block.json           # KFM cultural-landscape snippet
└── template-care-block.json          # CARE snippet
~~~

(An `annotated/` subdirectory may be added for training-oriented examples.)

---

## 📦 Full Cultural-Landscape Metadata Template (Minimal JSON)

**File:** `template-metadata.json`  

Used for any single cultural landscape dataset (region, route, interaction sphere, resource area).

~~~text
{
  "dct:title": "DATASET TITLE vX",
  "dct:description": "Generalized description of the cultural landscape dataset.",
  "dct:license": "CC-BY-4.0",
  "dct:temporal": "YYYY–YYYY",
  "dct:creator": "Cultural Landscape Working Group",
  "dcat:keyword": ["archaeology", "cultural-landscape", "Kansas"],
  "dcat:distribution": "../stac/items/DATASET-ID-vX.json",

  "kfm:domain": "archaeology-cultural-landscapes",
  "kfm:landscape_type": "interaction_sphere",
  "kfm:culture_phase": ["PHASE-1", "PHASE-2"],
  "kfm:generalization": "H3-r7",
  "kfm:source": "Public-domain archaeological syntheses and approved archives",
  "kfm:provenance": "../provenance/DATASET-ID-vX.json",
  "kfm:schema_version": "v11.0.0",

  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Generalization and redaction applied to protect cultural landscapes.",
  "care:visibility_rules": "polygon-generalized",
  "care:consent_status": "approved"
}
~~~

**Notes:**

- `kfm:landscape_type` may be `region`, `route`, `interaction_sphere`, `resource_area`, etc., depending on the dataset.  
- For high-sensitivity datasets (e.g., protohistoric interaction spheres), CARE values differ (e.g., `restricted-generalized`, `tribal`, `"h3-only"`).

---

## ✔ DCAT Metadata Block Template

**File:** `template-dcat-block.json`

For DCAT-only snippets reused across datasets.

~~~text
{
  "dct:title": "DATASET TITLE",
  "dct:description": "Generalized human-readable summary.",
  "dct:license": "CC-BY-4.0",
  "dct:temporal": "YYYY–YYYY",
  "dct:creator": "Cultural Landscape Working Group",
  "dcat:keyword": ["tag1", "tag2", "cultural-landscape"],
  "dcat:distribution": "PATH/TO/STAC-ITEM.json"
}
~~~

---

## ✔ KFM Cultural-Landscape Block Template

**File:** `template-kfm-block.json`

Encapsulates KFM extensions for cultural landscapes.

~~~text
{
  "kfm:domain": "archaeology-cultural-landscapes",
  "kfm:landscape_type": "interaction_sphere",
  "kfm:culture_phase": ["PHASE-A", "PHASE-B"],
  "kfm:generalization": "H3-r7",
  "kfm:source": "PD archives or institution names",
  "kfm:provenance": "PATH/TO/PROVENANCE.json",
  "kfm:schema_version": "v11.0.0"
}
~~~

Dataset authors must:

- Choose an appropriate `kfm:landscape_type` (`region`, `route`, `interaction_sphere`, `resource_area`, etc.).  
- Keep `kfm:generalization` consistent with STAC and provenance.

---

## ✔ CARE Metadata Block Template

**File:** `template-care-block.json`

Encodes CARE cultural-safety settings.

~~~text
{
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Generalization applied to avoid exposing sensitive or sacred locations.",
  "care:visibility_rules": "polygon-generalized",
  "care:consent_status": "approved"
}
~~~

For elevated- and high-sensitivity datasets:

- `care:sensitivity` may be `"restricted-generalized"`.  
- `care:review` may be `"tribal"` (mandatory for some interaction spheres).  
- `care:visibility_rules` may be `"h3-only"`.  

These stricter patterns are defined in subcategory standards (e.g., interaction-sphere metadata).

---

## 🧪 Validation Requirements

Metadata files created from these templates must pass all relevant schemas in:

- `docs/analyses/archaeology/datasets/cultural-landscapes/metadata/schemas/`

Typically including:

- `metadata-core-schema.json`  
- `dcat-metadata-schema.json`  
- `care-metadata-schema.json`  
- `provenance-link-schema.json`  
- `stac-crosswalk.json`  

CI workflows enforcing these include:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  
- `.github/workflows/artifact-stac-validate.yml`  

Any metadata failing validation must be corrected before merge or release.

---

## 🧠 Integration Into KFM Ecosystem

Templates here are designed so their outputs:

- Integrate cleanly with STAC Items/Collections via crosswalk schemas.  
- Provide canonical metadata for Neo4j nodes (e.g., `CulturalLandscape`, `InteractionSphere`, `Route`).  
- Supply CARE and provenance metadata used by Story Nodes and Focus Mode v3.  
- Enable reproducible cataloging and governance for all cultural landscape datasets.

---

## 🕰 Version History

| Version   | Date       | Author                                   | Summary                                                                 |
|-----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape Working Group · FAIR+CARE Council | Upgraded to KFM v11.2.3; added energy/carbon telemetry refs; aligned with global cultural-landscape metadata standards and interaction-sphere template patterns. |
| v10.4.0   | 2025-11-17 | Cultural Landscape Working Group · FAIR+CARE Council | Initial cultural landscape metadata templates; defined DCAT/KFM/CARE blocks and validation expectations. |
| v10.0.0   | 2025-11-10 | Landscape Metadata Team                  | Prototype templates and directory scaffold.                             |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Aligned  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscape Metadata Standards](../README.md)

