---
title: "📑 Kansas Frontier Matrix — Interaction Sphere Metadata Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/README.md"
description: "Template library for JSON metadata describing KFM v11 cultural-landscape interaction spheres (DCAT + KFM + CARE)."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:interaction-sphere-metadata-templates-v11.2.3"
doc_kind: "Template Library"
intent: "interaction-sphere-metadata-templates"
semantic_document_id: "kfm-doc-archaeology-cultural-landscapes-interaction-spheres-metadata-templates-v11.2.3"
category: "Analyses · Archaeology · Cultural Landscapes · Metadata · Templates"

sbom_ref: "../../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-interaction-spheres-metadata-templates-v1.json"
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
  - "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📑 Interaction Sphere Metadata Templates (v11)

`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/README.md`

**Purpose**  
Provide the official **metadata templates** for building new **interaction-sphere metadata JSON files** in the Kansas Frontier Matrix (KFM) v11.

Templates in this directory enforce:

- **FAIR+CARE** cultural safety and sovereignty alignment  
- **DCAT 3.0** dataset metadata standards  
- **KFM cultural-landscape extensions (`kfm:*`)**  
- Consistency with **STAC Items/Collections** and PROV-O provenance  
- Compatibility with Story Node v3 and Focus Mode v3  
- CI/CD validation under **MCP-DL v6.3**

All metadata created from these templates is stored in:

- `docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/`

---

## 📘 Overview

Interaction spheres represent broad cultural networks involving:

- Exchange and interaction  
- Shared material culture and technology  
- Ecological co-adaptation  
- Settlement and movement connectivity  

Because these cultural landscapes may touch on **sensitive archaeological and Indigenous knowledge**, metadata must guarantee:

- Ethical rigor and culturally respectful framing  
- Spatial de-identification and generalization (no site-level detail)  
- Validation-friendly, schema-aligned JSON structures  
- Explicit linkage to provenance records (PROV-O)  
- Clear CARE and sovereignty metadata used by all downstream systems

These templates are aligned with the standards defined in:

- `../README.md` (Interaction Sphere Metadata Standards)  
- `../../stac/schemas/README.md` (Interaction Sphere STAC Schemas)  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/metadata/templates/
├── 📄 README.md                           # This file
├── 📄 template-metadata.json              # Full interaction-sphere metadata template
├── 📄 template-dcat-block.json            # DCAT-only snippet
├── 📄 template-care-block.json            # CARE-only snippet
├── 📄 template-kfm-block.json             # KFM extension snippet
└── 📂 annotated/                          # Annotated versions for learning
    ├── 📄 README.md
    ├── 📄 template-metadata-annotated.json
    ├── 📄 dcat-block-annotated.json
    ├── 📄 care-block-annotated.json
    └── 📄 kfm-block-annotated.json
~~~

Contributors should start from these templates when creating metadata for new or updated interaction-sphere datasets.

---

## 📦 Full Interaction Sphere Metadata Template (Minimal JSON)

**File:** `template-metadata.json`

This template is intended to be copied and filled per interaction-sphere dataset:

~~~json
{
  "dct:title": "INTERACTION SPHERE NAME vX",
  "dct:description": "Generalized description of the interaction sphere.",
  "dct:license": "CC-BY-4.0",
  "dct:temporal": "YYYY–YYYY",
  "dct:creator": "Cultural Landscape Working Group",
  "dcat:keyword": ["interaction sphere", "archaeology", "Kansas"],
  "dcat:distribution": "../../stac/items/INTERACTION-SPHERE-ID-vX.json",

  "kfm:domain": "archaeology-cultural-landscapes",
  "kfm:landscape_type": "interaction_sphere",
  "kfm:culture_phase": ["PHASE-1", "PHASE-2"],
  "kfm:generalization": "H3-r7",
  "kfm:source": "Public-domain archaeological syntheses and approved ethnohistoric summaries",
  "kfm:provenance": "../../provenance/INTERACTION-SPHERE-ID-vX.json",
  "kfm:schema_version": "v11.0.0",

  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Generalization applied to protect cultural landscapes and avoid site-level inference.",
  "care:visibility_rules": "polygon-generalized",
  "care:consent_status": "approved"
}
~~~

Dataset authors must adapt:

- Title, description, temporal span, keywords.  
- `kfm:culture_phase`, `kfm:generalization`, and `kfm:provenance`.  
- CARE fields according to dataset sensitivity (e.g., protohistoric spheres may require `restricted-generalized` and `tribal` review).

---

## ✔ DCAT Metadata Block Template

**File:** `template-dcat-block.json`

For DCAT-only snippets:

~~~json
{
  "dct:title": "DATASET TITLE",
  "dct:description": "Human-readable generalized description.",
  "dct:license": "CC-BY-4.0",
  "dct:temporal": "YYYY–YYYY",
  "dct:creator": "Cultural Landscape Working Group",
  "dcat:keyword": ["tag1", "tag2", "interaction sphere"],
  "dcat:distribution": "PATH/TO/STAC-ITEM.json"
}
~~~

This block must crosswalk cleanly to STAC and provenance (IDs, license, temporal extent).

---

## ✔ KFM Cultural-Landscape Block Template

**File:** `template-kfm-block.json`

For KFM extension fields used by interaction spheres:

~~~json
{
  "kfm:domain": "archaeology-cultural-landscapes",
  "kfm:landscape_type": "interaction_sphere",
  "kfm:culture_phase": ["PHASE-A", "PHASE-B"],
  "kfm:generalization": "H3-r7",
  "kfm:source": "PD or institution/repository name",
  "kfm:provenance": "PATH/TO/PROVENANCE.json",
  "kfm:schema_version": "v11.0.0"
}
~~~

Values must align with the **STAC Item properties** and **provenance JSON**.

---

## ✔ CARE Metadata Block Template

**File:** `template-care-block.json`

For CARE-only snippets:

~~~json
{
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Generalization applied to protect cultural landscapes; no site-level information included.",
  "care:visibility_rules": "polygon-generalized",
  "care:consent_status": "approved"
}
~~~

For higher-sensitivity cases (for example, Protohistoric Wichita), these values will differ:

- `care:sensitivity`: `"restricted-generalized"`  
- `care:review`: `"tribal"`  
- `care:visibility_rules`: `"h3-only"`  
- `care:consent_status`: often `"conditional"` until full approval.

---

## 🧪 Validation Requirements

All metadata produced from these templates must pass:

- Interaction-sphere metadata schemas in `../schemas/`, including:
  - `metadata-core-schema.json`  
  - `dcat-metadata-schema.json`  
  - `care-metadata-schema.json`  
  - `provenance-link-schema.json`  
  - `stac-crosswalk-schema.json`  

Validation is enforced by CI workflows, such as:

- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  
- `.github/workflows/artifact-stac-validate.yml`  

Any validation failure must be resolved before metadata is considered governed and accepted.

---

## 🧠 Integration Into KFM Ecosystem

### Knowledge Graph Nodes

Metadata built from these templates drives creation/enrichment of:

- `InteractionSphere` nodes  
- `CulturalPhase` nodes  
- `MetadataRecord` nodes  
- CARE-related nodes (`CareSensitivityState`, etc.)  

### Relationships

- `HAS_METADATA` (InteractionSphere → MetadataRecord)  
- `HAS_CARE_SENSITIVITY` (InteractionSphere → CARE node)  
- `HAS_PROVENANCE` (via metadata → provenance linkage)  
- `OCCURRED_DURING` (InteractionSphere → CulturalPhase/TimeInterval)  
- `GENERALIZED_FROM` (linking to generalized spatial representations)  

### Story Nodes & Focus Mode

Metadata fields created using these templates support:

- Sphere-level narratives and timelines.  
- Sensitivity badges and warning banners.  
- Provenance chips in Story Node and Focus Mode views.  
- Proper scoping of time and space for map overlays and narratives.

---

## 🕰 Version History

| Version   | Date       | Author                                                   | Summary                                                                 |
|-----------|------------|----------------------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee | Updated for KFM v11.2.3; aligned with interaction-sphere metadata standards and global KFM templates; added energy/carbon telemetry references. |
| v10.4.0   | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council               | Regenerated interaction-sphere metadata templates; ensured KFM-MDP v10.4 compliance and tilde-fenced directory layouts. |
| v10.0.0   | 2025-11-10 | Metadata Team                                            | Initial template drafts and directory structure.                         |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Interaction Sphere Metadata](../README.md)
