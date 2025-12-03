---
title: "📑📝 Kansas Frontier Matrix — Annotated Metadata Templates for Interaction Spheres (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/annotated/README.md"
description: "Annotated JSON metadata templates for KFM v11 interaction-sphere datasets, explaining DCAT, KFM, and CARE fields line by line."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:interaction-sphere-metadata-annotated-templates-v11.2.3"
doc_kind: "Annotated Templates"
intent: "interaction-sphere-metadata-annotated-templates"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-interaction-spheres-metadata-annotated-templates-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Metadata · Templates"

sbom_ref: "../../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-interaction-spheres-metadata-annotated-templates-v1.json"
energy_schema: "../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

data_steward: "Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/annotated/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📑📝 Annotated Metadata Templates — Interaction Spheres (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/annotated/README.md`

**Purpose**  
Provide fully **annotated examples** of interaction-sphere metadata templates used in the Kansas Frontier Matrix (KFM) v11.

These annotated templates teach contributors how to:

- Create **FAIR+CARE-compliant** metadata.  
- Align metadata with **DCAT 3.0**, **KFM extensions**, and **CARE**.  
- Keep metadata consistent with **STAC Items/Collections** and **PROV-O provenance**.  
- Pass all KFM CI/CD validation checks.

The artifacts here are **reference-only** and MUST NOT be used directly as production metadata.

---

## 📘 Overview

These annotated templates include:

- Line-by-line commentary via `_comment` keys.  
- Example values and recommended patterns.  
- Controlled vocabulary hints (for `kfm:*` and `care:*` fields).  
- Spatial and cultural-safety constraints.  
- Guidance on STAC/DCAT/PROV-O linkage.  
- Explanations of KFM archaeology / cultural-landscape semantics.

They are meant to be read alongside:

- `../README.md` (interaction-sphere metadata templates).  
- `../../README.md` (metadata standards for interaction spheres).  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/annotated/
├── 📄 README.md                          # This file
├── 📄 template-metadata-annotated.json   # Full annotated interaction-sphere metadata example
├── 📄 dcat-block-annotated.json          # Annotated DCAT-only snippet
├── 📄 care-block-annotated.json          # Annotated CARE-only snippet
└── 📄 kfm-block-annotated.json           # Annotated KFM extension snippet
~~~

Use these files to understand how to fill in the non-annotated templates in `../`.

---

## 🧩 Annotated Full Metadata Template (Educational)

**File:** `template-metadata-annotated.json` (educational example)

~~~json
{
  "_comment": "==== DCAT METADATA BLOCK ====",

  "dct:title": "INTERACTION SPHERE NAME vX",
  "_comment_dct_title": "Human-readable title; should align with the STAC Item/Collection naming and version.",

  "dct:description": "Generalized description of cultural interaction sphere.",
  "_comment_desc": "Avoid colonial or essentialist terminology; emphasize interpretive nature and uncertainty.",

  "dct:license": "CC-BY-4.0",
  "_comment_license": "KFM requires open, PD-compatible licenses for public-governed datasets.",

  "dct:temporal": "YYYY–YYYY",
  "_comment_temporal": "Represents the total cultural-phase duration; must align with STAC temporal extent and KFM phase ontology.",

  "dcat:keyword": ["interaction sphere", "archaeology", "Kansas"],
  "_comment_keywords": "Keywords improve findability in catalogs and graph-based search.",

  "dcat:distribution": "../../stac/items/INTERACTION-SPHERE-ID-vX.json",
  "_comment_distribution": "Must link directly to the companion STAC Item file in the local stac/items/ directory.",


  "_comment_kfm": "==== KFM CULTURAL-LANDSCAPE BLOCK ====",

  "kfm:domain": "archaeology-cultural-landscapes",
  "_comment_kfm_domain": "Domain identifier shared by all cultural-landscape interaction-sphere datasets.",

  "kfm:landscape_type": "interaction_sphere",
  "_comment_landscape_type": "Controlled vocabulary; see interaction-sphere metadata standards.",

  "kfm:culture_phase": ["PHASE-A", "PHASE-B"],
  "_comment_culture_phase": "List of cultural phases represented (e.g., Late Prehistoric, Protohistoric-Wichita).",

  "kfm:generalization": "H3-r7",
  "_comment_generalization": "Records the spatial generalization level applied; must match STAC and provenance.",

  "kfm:source": "Public-domain archaeological synthesis and approved ethnohistoric summaries",
  "_comment_source": "Describe the main lines of evidence and ensure they are PD/open or used with appropriate permissions.",

  "kfm:provenance": "../../provenance/INTERACTION-SPHERE-ID-vX.json",
  "_comment_provenance": "Link to PROV-O provenance JSON-LD tracking raw → generalized → processed lineage.",

  "kfm:schema_version": "v11.0.0",
  "_comment_schema_version": "Version of this metadata schema/template; helps track schema upgrades over time.",


  "_comment_care": "==== CARE CULTURAL SAFETY BLOCK ====",

  "care:sensitivity": "generalized",
  "_comment_sensitivity": "Typical values: 'general', 'generalized', 'restricted-generalized'. 'restricted' is not used in public-governed layers.",

  "care:review": "faircare",
  "_comment_review": "Use 'tribal' when descendant-sensitive or protohistoric/ethnohistoric content is involved.",

  "care:notes": "Generalization applied to protect cultural landscapes and avoid site-level inference.",
  "_comment_notes": "Explain key ethical decisions: what was removed, generalized, or kept internal; record review outcomes.",

  "care:visibility_rules": "polygon-generalized",
  "_comment_visibility": "Controls user-visible spatial fidelity. Use 'h3-only' for the highest sensitivity interaction spheres.",

  "care:consent_status": "approved",
  "_comment_consent_status": "Consent state as defined in KFM CARE vocabularies (e.g., approved, conditional, not-approved, not-applicable)."
}
~~~

This JSON is **not** loaded as-is; it is a guide for how fields should be structured and explained.

---

## 🧩 Annotated DCAT Block

**File:** `dcat-block-annotated.json`

~~~json
{
  "dct:title": "DATASET TITLE",
  "_comment_title": "Readable dataset title; should be consistent with STAC and Story Node naming patterns.",

  "dct:description": "Meaningful summary of dataset purpose and scope.",
  "_comment_desc": "Summarize the interaction sphere at a generalized level; avoid naming specific sites or sensitive places.",

  "dct:license": "CC-BY-4.0",
  "_comment_license": "License must remain compatible with KFM’s public-governed distribution policies.",

  "dct:temporal": "YYYY–YYYY",
  "_comment_timeline": "Represents temporal coverage; must align with STAC temporal extent and KFM's phase ontology.",

  "dcat:keyword": ["tag1", "tag2"],
  "_comment_keywords": "Use a small set of focused tags supporting search and graph-based topic clustering.",

  "dcat:distribution": "PATH/TO/STAC-ITEM.json",
  "_comment_distribution": "Path (relative or URL) to the STAC Item; ensures DCAT ↔ STAC crosswalk."
}
~~~

---

## 🧩 Annotated KFM Block

**File:** `kfm-block-annotated.json`

~~~json
{
  "kfm:domain": "archaeology-cultural-landscapes",
  "_comment_kfm_domain": "Domain tag that joins this metadata to the interaction-sphere ecosystem.",

  "kfm:landscape_type": "interaction_sphere",
  "_comment_landscape_type": "Must be one of the allowed landscape types (e.g., interaction_sphere, exchange_zone).",

  "kfm:culture_phase": ["PHASE-A", "PHASE-B"],
  "_comment_phases": "Used to attach this dataset to phases in the KFM timeline and graph (CulturalPhase nodes).",

  "kfm:generalization": "H3-r7",
  "_comment_generalization": "Describes spatial generalization; coordinate-level detail must never surface in public layers.",

  "kfm:source": "Public domain archive",
  "_comment_source": "Brief description of primary sources; ensure rights/permissions are compatible with CARE.",

  "kfm:provenance": "PATH/TO/PROVENANCE.json",
  "_comment_provenance": "Connects metadata to PROV-O records, enabling lineage-aware Story Nodes and Focus Mode.",

  "kfm:schema_version": "v11.0.0",
  "_comment_schema_version": "Tracks which version of the KFM metadata schema this record follows."
}
~~~

---

## 🧩 Annotated CARE Block

**File:** `care-block-annotated.json`

~~~json
{
  "care:sensitivity": "generalized",
  "_comment_sensitivity": "For higher sensitivity (e.g., Protohistoric Wichita), use 'restricted-generalized'; avoid 'restricted' in public-facing zones.",

  "care:review": "faircare",
  "_comment_review": "Switch to 'tribal' when descendant-community or sovereignty review is required.",

  "care:notes": "Generalization applied to protect culturally meaningful landscapes.",
  "_comment_notes": "Document key redactions, generalizations, and the rationale behind them.",

  "care:visibility_rules": "polygon-generalized",
  "_comment_visibility": "Controls the level of geometry detail. 'h3-only' is recommended for the most sensitive spheres.",

  "care:consent_status": "approved",
  "_comment_consent_status": "Use 'conditional' if ongoing negotiation or partial approval is in place."
}
~~~

---

## 🧪 Validation Expectations

Annotated templates are **didactic**, but they must still be consistent with:

- `metadata-core-schema.json`  
- `dcat-metadata-schema.json`  
- `care-metadata-schema.json`  
- `provenance-link-schema.json`  
- `stac-crosswalk-schema.json`  

They are not validated in production CI, but they guide records that **are** validated by:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  
- `.github/workflows/artifact-stac-validate.yml`  

Production metadata derived from the non-annotated templates must satisfy all schema and CI checks.

---

## 🔗 Related Specifications

- `../README.md`  
  – Non-annotated interaction-sphere metadata templates.  
- `../../README.md`  
  – Interaction-sphere metadata standards.  
- `../../schemas/README.md`  
  – Metadata schema definitions and crosswalks.  
- `../../../stac/README.md`  
  – STAC catalog documentation for interaction spheres.  
- `../../../provenance/templates/README.md`  
  – Provenance templates for interaction spheres.

---

## 🕰 Version History

| Version   | Date       | Author                                                   | Summary                                                                 |
|-----------|------------|----------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee | Updated for KFM v11.2.3; aligned with interaction-sphere metadata standards and CARE vocabulary; added energy/carbon telemetry references. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council               | Regenerated annotated templates; ensured KFM-MDP v10.4 compliance and box-safe formatting. |
| v10.0.0   | 2025-11-10 | Metadata Training Team                                  | Initial annotated template set for training purposes.                   |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Metadata Template Library](../README.md)
