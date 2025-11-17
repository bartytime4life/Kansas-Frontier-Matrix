---
title: "📑📝 Kansas Frontier Matrix — Annotated Metadata Templates for Interaction Spheres (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/annotated/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-interaction-spheres-metadata-annotated-templates-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Annotated Templates"
intent: "interaction-sphere-metadata-annotated-templates"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📑📝 **Annotated Metadata Templates — Interaction Spheres**

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/annotated/README.md`

**Purpose:**  
Provide fully annotated examples of Interaction Sphere metadata templates used in the Kansas Frontier Matrix (KFM).  
These annotated templates teach contributors how to create FAIR+CARE compliant metadata that passes all KFM CI/CD validation requirements.

</div>

---

## 📘 Overview

These annotated templates include:

- Line-by-line commentary  
- Example values  
- Controlled vocabulary rules  
- Spatial and cultural-safety constraints  
- STAC/DCAT/PROV-O linkage guidance  
- KFM archaeology extension explanations  

They are reference-only and not used directly as production metadata.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/annotated/
├── README.md
├── template-metadata-annotated.json
├── dcat-block-annotated.json
├── care-block-annotated.json
└── kfm-block-annotated.json
~~~

---

## 🧩 Annotated Full Metadata Template (Education-Only)

~~~json
{
  "_comment": "==== DCAT METADATA BLOCK ====",

  "dct:title": "INTERACTION SPHERE NAME vX",
  "_comment_dct_title": "Human-readable title matching STAC Item/Collection naming.",

  "dct:description": "Generalized description of cultural interaction sphere.",
  "_comment_desc": "Must avoid colonial terminology; use culturally neutral language.",

  "dct:license": "CC-BY-4.0",
  "_comment_license": "KFM requires PD-compatible open licensing.",

  "dct:temporal": "YYYY–YYYY",
  "_comment_temporal": "Represents total cultural phase duration (OWL-Time aligned).",

  "dcat:keyword": ["interaction sphere", "archaeology", "Kansas"],
  "_comment_keywords": "Improves findability and semantic indexing.",

  "dcat:distribution": "../../stac/INTERACTION-SPHERE-ID-vX.json",
  "_comment_distribution": "Must link directly to companion STAC Item.",


  "_comment": "==== KFM ARCHAEOLOGY BLOCK ====",

  "kfm:landscape_type": "interaction_sphere",
  "_comment_landscape_type": "Controlled vocabulary enforced by archaeology schema.",

  "kfm:culture_phase": ["PHASE-A", "PHASE-B"],
  "_comment_culture_phase": "Aligns metadata with KFM chronology & Focus Mode timelines.",

  "kfm:geometry_generalization": "H3-level-6",
  "_comment_generalization": "All interaction spheres require H3 or simplified polygon generalization.",

  "kfm:source": "Public domain synthesis",
  "_comment_source": "Original dataset must be PD or verifiably non-restricted.",

  "kfm:provenance": "../../provenance/INTERACTION-SPHERE-ID-vX.json",
  "_comment_provenance": "Points to PROV-O lineage tracking raw→generalized→processed.",

  "kfm:schema_version": "1.0.0",
  "_comment_schema_version": "Version tied to repository governance cycles.",


  "_comment": "==== CARE CULTURAL SAFETY BLOCK ====",

  "care:sensitivity": "generalized",
  "_comment_sensitivity": "Allowed: 'generalized', 'restricted-generalized'. Forbidden: 'restricted'.",

  "care:review": "faircare",
  "_comment_review": "Use 'tribal' for protohistoric or descendant-sensitive datasets.",

  "care:notes": "Generalization applied to protect cultural sovereignty.",
  "_comment_notes": "Explain ethical choices, removed info, and review outcomes.",

  "care:visibility_rules": "polygon-generalized",
  "_comment_visibility": "Controls public visibility of spatial data; 'h3-only' for highest sensitivity."
}
~~~

---

## 🧩 Annotated DCAT Block

~~~json
{
  "dct:title": "DATASET TITLE",
  "_comment_title": "Readable title aligned with STAC naming.",

  "dct:description": "Meaningful summary of dataset purpose.",
  "_comment_desc": "Avoid precise site references; maintain cultural neutrality.",

  "dct:license": "CC-BY-4.0",
  "_comment_license": "All KFM datasets must be public-domain compatible.",

  "dct:temporal": "YYYY–YYYY",
  "_comment_timeline": "Phase-spanning temporal description using OWL-Time logic.",

  "dcat:keyword": ["tag1", "tag2"],
  "_comment_keywords": "Tags supporting semantic search pipelines.",

  "dcat:distribution": "PATH/TO/STAC-ITEM.json",
  "_comment_distribution": "References STAC Item path in stac/ directory."
}
~~~

---

## 🧩 Annotated KFM Block

~~~json
{
  "kfm:landscape_type": "interaction_sphere",
  "_comment_landscape_type": "Classification used throughout KFM schemas.",

  "kfm:culture_phase": ["PHASE-A", "PHASE-B"],
  "_comment_phases": "Used by timelines, story nodes, and graph relationships.",

  "kfm:geometry_generalization": "H3-level-6",
  "_comment_generalization": "Generalization guarantees spatial safety and CARE compliance.",

  "kfm:source": "Public domain archive",
  "_comment_source": "Source must be PD, Open Access, or permissible via FAIR+CARE.",

  "kfm:provenance": "PATH/TO/PROVENANCE.json",
  "_comment_provenance": "Links metadata to its PROV-O lineage document.",

  "kfm:schema_version": "1.0.0",
  "_comment_schema_version": "Ensures validation consistency as repository evolves."
}
~~~

---

## 🧩 Annotated CARE Block

~~~json
{
  "care:sensitivity": "generalized",
  "_comment_sensitivity": "Use 'restricted-generalized' for protohistoric or high-sensitivity spheres.",

  "care:review": "faircare",
  "_comment_review": "Tribal review required for descendant-sensitive materials.",

  "care:notes": "Generalization applied to protect culturally meaningful landscapes.",
  "_comment_notes": "Document all ethical considerations, exclusions, filtering strategies.",

  "care:visibility_rules": "polygon-generalized",
  "_comment_visibility": "Controls user-visible spatial fidelity to prevent sensitive inference."
}
~~~

---

## 🧪 Validation Expectations

Annotated templates must align with:

- `metadata-core-schema.json`  
- `dcat-metadata-schema.json`  
- `care-metadata-schema.json`  
- `provenance-link-schema.json`  
- `stac-crosswalk-schema.json`  

CI/CD validation pipelines:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  
- `.github/workflows/artifact-stac-validate.yml`  

Failure → CI rejection.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Fully regenerated annotated templates; removed all box-breaking causes |
| v10.0.0 | 2025-11-10 | Metadata Training Team | Initial annotated template set |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Template Library](../README.md)

</div>