---
title: "📑 Kansas Frontier Matrix — Interaction Sphere Metadata Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-interaction-spheres-metadata-templates-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Template Library"
intent: "interaction-sphere-metadata-templates"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📑 **Interaction Sphere Metadata Templates**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/README.md`

**Purpose:**  
Provide the official **metadata templates** for building new **Interaction Sphere metadata JSON files** within the Kansas Frontier Matrix (KFM).  
These templates enforce:

- FAIR+CARE cultural safety  
- STAC/DCAT/PROV-O alignment  
- Spatial + temporal generalization rules  
- KFM archaeology schema consistency  
- Story Node + Focus Mode compatibility  
- Full CI/CD validation under MCP-DL v6.3  

</div>

---

## 📘 Overview

Interaction Spheres represent broad cultural networks involving:

- Exchange and interaction  
- Shared material culture  
- Ecological co-adaptation  
- Settlement and mobility connectivity  

Because these cultural landscapes may touch on sensitive archaeological and ethnographic knowledge, metadata must guarantee:

- Ethical rigor and cultural neutrality  
- Spatial de-identification and generalization  
- Validation-friendly JSON structure  
- Explicit linkage to provenance records  

All metadata created from these templates is stored in:

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/`

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/
├── README.md
├── template-metadata.json
├── template-dcat-block.json
├── template-care-block.json
├── template-kfm-block.json
└── annotated/
    ├── README.md
    ├── template-metadata-annotated.json
    ├── dcat-block-annotated.json
    ├── care-block-annotated.json
    └── kfm-block-annotated.json
~~~

---

## 📦 Full Interaction Sphere Metadata Template (Minimal JSON)

~~~json
{
  "dct:title": "INTERACTION SPHERE NAME vX",
  "dct:description": "Generalized description of the interaction sphere.",
  "dct:license": "CC-BY-4.0",
  "dct:temporal": "YYYY–YYYY",
  "dcat:keyword": ["interaction sphere", "archaeology", "Kansas"],
  "dcat:distribution": "../../stac/INTERACTION-SPHERE-ID-vX.json",

  "kfm:landscape_type": "interaction_sphere",
  "kfm:culture_phase": ["PHASE-1", "PHASE-2"],
  "kfm:geometry_generalization": "H3-level-6",
  "kfm:source": "Public-domain archaeological synthesis",
  "kfm:provenance": "../../provenance/INTERACTION-SPHERE-ID-vX.json",
  "kfm:schema_version": "1.0.0",

  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Generalization applied for cultural safety.",
  "care:visibility_rules": "polygon-generalized"
}
~~~

---

## ✔ DCAT Metadata Block Template

~~~json
{
  "dct:title": "DATASET TITLE",
  "dct:description": "Human-readable description.",
  "dct:license": "CC-BY-4.0",
  "dct:temporal": "YYYY–YYYY",
  "dcat:keyword": ["tag1", "tag2"],
  "dcat:distribution": "PATH/TO/STAC-ITEM.json"
}
~~~

---

## ✔ KFM Archaeology Block Template

~~~json
{
  "kfm:landscape_type": "interaction_sphere",
  "kfm:culture_phase": ["PHASE-A", "PHASE-B"],
  "kfm:geometry_generalization": "H3-level-6",
  "kfm:source": "PD or institution name",
  "kfm:provenance": "PATH/TO/PROVENANCE.json",
  "kfm:schema_version": "1.0.0"
}
~~~

---

## ✔ CARE Metadata Block Template

~~~json
{
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Generalization applied to protect cultural landscapes.",
  "care:visibility_rules": "polygon-generalized"
}
~~~

---

## 🧪 Validation Requirements

All metadata produced from these templates must pass:

- `metadata-core-schema.json`  
- `dcat-metadata-schema.json`  
- `care-metadata-schema.json`  
- `provenance-link-schema.json`  
- `stac-crosswalk-schema.json`  

Validation is enforced by:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  
- `.github/workflows/artifact-stac-validate.yml`  

Any failure results in CI rejection and blocks ingestion.

---

## 🧠 Integration Into KFM Ecosystem

### Knowledge Graph Nodes

- `InteractionSphere`  
- `CulturalPhase`  
- `GeneralizedRegion`  
- `MetadataRecord`  

### Relationships

- `HAS_METADATA`  
- `OCCURRED_DURING`  
- `GENERALIZED_FROM`  
- `HAS_PROVENANCE`  
- `CARE_SENSITIVITY`  

### Story Nodes & Focus Mode

Metadata produced with these templates supports:

- Sphere-level narratives  
- Multiphase cultural interaction arcs  
- Sensitivity badges and provenance chips  
- Context-aware Focus Mode explanations  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------|------|--------|---------|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Regenerated to fix box-breaking issues; ensured KFM-MDP v10.4 compliance and tilde-fence directory layout |
| v10.0.0 | 2025-11-10 | Metadata Team | Initial template drafts |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Interaction Sphere Metadata](../README.md)

</div>