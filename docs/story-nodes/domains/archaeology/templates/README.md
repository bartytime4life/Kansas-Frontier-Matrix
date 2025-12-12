---
title: "🏺🧩 KFM v11.2.6 — Archaeology Story Node Templates"
path: "docs/story-nodes/domains/archaeology/templates/README.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Template Directory README"
header_profile: "standard"
footer_profile: "standard"

domain: "archaeology"
intent: "kfm-archaeology-storynode-templates"
lifecycle_stage: "stable"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:storynodes:archaeology:templates:index:v11.2.6"
semantic_document_id: "kfm-storynodes-archaeology-templates-index-v11.2.6"
event_source_id: "ledger:docs/story-nodes/domains/archaeology/templates/README.md"

immutability_status: "version-pinned"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"

schema_ref: "../../../../../schemas/json/story-node.schema.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked (Templates + Public-Safe Examples)"
classification: "Generalized / Public-Safe"
sensitivity: "Cultural Heritage Authoring Templates (no site-disclosing details)"
sensitivity_level: "Moderate"
public_exposure_risk: "Low (when masking rules are followed)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Archaeology Domain Board + Indigenous Data Governance Board"

ttl_policy: "36 months"
sunset_policy: "Superseded by future v12 domain rewrite"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/domains/archaeology/templates/README.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "🗂️ Directory Layout"
    - "📘 Overview"
    - "🧩 Template Set"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE, Sovereignty & Masking"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "metadata-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
---

<div align="center">

# 🏺🧩 **Archaeology Story Node Templates (KFM v11.2.6)**  
### *Authoring Patterns · Schema Skeletons · Relation Models*  

`docs/story-nodes/domains/archaeology/templates/README.md`

**Purpose**  
Provide **authoring templates**, **schema-aligned skeletons**, and a **governed relation-pattern guide**  
for constructing archaeology Story Nodes in a safe, consistent, **FAIR+CARE** + **sovereignty-aware** way.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Domain-Archaeology-8b5a2b" />
<img src="https://img.shields.io/badge/Templates-Governed-brightgreen" />
<img src="https://img.shields.io/badge/Masking-Required-gold" />

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 story-nodes/
    └── 📂 domains/
        └── 🏺 archaeology/
            ├── 📄 README.md
            ├── 📝 notes/
            │   ├── 📄 README.md
            │   ├── 📄 backlog.md
            │   └── ⚖️ ethics-checklist.md
            └── 🧩 templates/
                ├── 📄 README.md                         # This file — template index
                ├── 📝 story-node-archaeology.md         # Markdown authoring template (normative for MD authors)
                ├── 🧩 story-node-archaeology.json       # JSON schema-aligned skeleton (schema-valid)
                └── 🔗 relation-patterns.md              # Governed graph relation patterns (normative)
~~~

**Layout expectations (normative)**  
- Templates MUST remain **public-safe** (no precise coordinates, no restricted site codes, no burial/sacred details).  
- Examples inside templates MUST stay **generalized** and **non-targetable**.  
- If `schema_ref` changes, the JSON skeleton MUST be regenerated and revalidated.

---

## 📘 Overview

This directory provides the **official archaeology authoring surface** for Story Nodes.

These templates enforce:

- **Generalized geometries** (H3, counties, broad regions; never precise site coordinates)  
- **Temporal discipline** (bounded intervals, stated precision, original labels)  
- **Safe graph relations** using governed patterns (no site-disclosing edges)  
- **Ontology alignment** suitable for KFM Story Node ingest + Neo4j integration  
- **FAIR+CARE compliance**, especially for Indigenous-linked or culturally sensitive contexts  

Use these templates when creating:

- generalized site or landscape nodes  
- survey / excavation / archival-processing activity nodes  
- non-invasive sensing nodes (e.g., geophysics summaries)  
- reinterpretation / counterpoint nodes (documented only)  
- multi-phase narratives (split into phase-safe nodes)

---

## 🧩 Template Set

### 📝 1) Markdown Template — `story-node-archaeology.md`
Author-friendly structure with:

- clear section prompts (Observation → Interpretation → Uncertainty)  
- explicit masking guidance  
- relations scaffold  
- sources + provenance prompts  
- optional media block (generalized only)

Use this when the Story Node will be maintained primarily as Markdown.

---

### 🧩 2) JSON Skeleton — `story-node-archaeology.json`
A schema-valid skeleton aligned to:

- `schema_ref` (`schemas/json/story-node.schema.json`)  

It SHOULD include:

- stable, public-safe ID placeholders  
- narrative blocks (with separations)  
- `spacetime` object (geometry + time bounds)  
- `relations[]` using patterns from `relation-patterns.md`  
- provenance-friendly hooks suitable for governance review

---

### 🔗 3) Relation Patterns — `relation-patterns.md`
The governed relation library defining safe edges such as:

- Story Node → generalized place (`about`)  
- Story Node → public document/dataset (`references`)  
- Story Node → reinterpretation (`counterpoint`)  
- feature/phase → generalized parent (`part-of`)  
- activity → organization (`carried-out-by`)  
- node → coarse region (`located-in`)  
- node → policy flag (`requires-review`)  

This file is **normative** for archaeology Story Node graph linking.

---

## 🧪 Validation & CI/CD

Minimum expectations for changes under this directory:

1. **Markdown lint** (KFM-MDP v11.2.6)
   - heading consistency
   - stable fences and spacing
   - footer link validity (where enforced)

2. **Schema validation**
   - `story-node-archaeology.json` MUST validate against `schema_ref`.

3. **Sovereignty / CARE checks**
   - templates MUST NOT contain:
     - precise coordinates
     - burial/sacred location indicators
     - restricted site codes or field-form content
     - restricted cultural knowledge

4. **Link integrity**
   - internal relative links MUST resolve (templates ↔ notes ↔ domain README ↔ governance docs)

---

## ⚖ FAIR+CARE, Sovereignty & Masking

**Non-negotiable**  
- All examples must remain **generalized** and **non-targetable**.  
- When in doubt, treat content as **sensitive** and require review via:
  - `../notes/ethics-checklist.md`
  - governance process referenced in the footer

Templates must guide authors to:

- separate observation vs interpretation  
- state uncertainty and limits  
- avoid unsupported affiliation claims  
- document masking decisions (H3 level / county / watershed, etc.)  
- flag review requirements (`requires-review`) for Indigenous-linked content

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Upgraded to KFM-MDP v11.2.6; corrected relative refs; expanded directory layout with folder emojis; clarified validation + sovereignty rules. |
| v11.2.2 | 2025-11-30 | Initial governed release of archaeology templates; synced with domain notes and Story Node telemetry references. |
| v11.2.1 | 2025-11-29 | Added Markdown + JSON templates and relation-pattern scaffolding.        |

---

<div align="center">

🏺🧩 **Archaeology Story Node Templates (v11.2.6)**  
Public-Safe Authoring · Sovereignty-Aware · Governance-Ready

[🏺 Archaeology Domain](../README.md) ·
[📝 Notes Index](../notes/README.md) ·
[📋 Backlog](../notes/backlog.md) ·
[⚖️ Ethics Checklist](../notes/ethics-checklist.md) ·
[🔗 Relation Patterns](./relation-patterns.md) ·
[📝 Markdown Template](./story-node-archaeology.md) ·
[🧩 JSON Skeleton](./story-node-archaeology.json) ·
[📚 Story Nodes Root](../../../README.md) ·
[📘 Docs Root](../../../../README.md) ·
[📘 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[🛡 Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🧾 Story Node Schema](../../../../../schemas/json/story-node.schema.json)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>
