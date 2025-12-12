---
title: "🏺 KFM v11.2.6 — Archaeology Story Node Backlog"
path: "docs/story-nodes/domains/archaeology/notes/backlog.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Archaeology Domain Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Backlog"
intent: "kfm-archaeology-storynode-backlog"
lifecycle_stage: "draft-pool"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked"
classification: "Generalized / Public-Safe (Internal-Prep)"
sensitivity: "Cultural Heritage Notes (Generalized)"
sensitivity_level: "Moderate (Generalized)"
public_exposure_risk: "Low (if rules followed)"
classification_scope_note: "In-repo file; MUST remain public-safe and generalized."

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Archaeology Domain Board"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 months"
sunset_policy: "Archived when incorporated into official Story Node sets"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:storynodes:archaeology:backlog:v11.2.6"
semantic_document_id: "kfm-storynodes-archaeology-backlog"
event_source_id: "ledger:storynodes/archaeology/backlog"

provenance_chain:
  - "docs/story-nodes/domains/archaeology/notes/backlog.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

header_profile: "standard"
footer_profile: "standard"
layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "timeline-generation"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "🗂️ Directory Layout"
    - "📘 Usage Notes"
    - "🏷️ Status Vocabulary"
    - "🗂️ Backlog Items"
    - "🧾 Backlog Item Template"
    - "🧠 Story Node & Focus Mode Integration"
    - "⚖ Sovereignty & Ethics Reminders"
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

# 🏺 **Archaeology Story Node Backlog (KFM v11)**  
### *Draft Concepts · Pending Reviews · Preliminary Notes*  

`docs/story-nodes/domains/archaeology/notes/backlog.md`

**Purpose**  
Maintain a curated list of **draft Story Node concepts** awaiting review, generalization, consultation,  
or conversion to final **Markdown/JSON Story Nodes** for the archaeology domain.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 story-nodes/
    └── 📂 domains/
        └── 🏺 archaeology/
            └── 📝 notes/
                ├── 📄 README.md           # Notes directory rules + guardrails
                ├── 📄 backlog.md          # This file — draft pool & triage table
                └── ⚖️ ethics-checklist.md # CARE + sovereignty review checklist
~~~

---

## 📘 Usage Notes

This backlog is a **staging area**. Nothing here is final.

Because this file lives in-repo, it MUST remain:

- **Public-safe** (even if “internal-prep”)
- **Generalized** (no coordinates, no site codes, no triangulation risk)
- **Sovereignty-aware** (Indigenous-linked content requires explicit review paths)
- **CARE-aligned** (minimize harm; avoid over-claims; respect authority to control)
- **Ready for triage** (each item must have a concrete next action)

If a draft cannot be made public-safe, it does not belong here.

---

## 🏷️ Status Vocabulary

Use these bounded status values (avoid free-form strings):

- `concept` — idea exists; not yet scoped  
- `research` — sources/datasets being identified (still generalized)  
- `outline` — narrative shape drafted; missing details/citations  
- `draft` — candidate story exists; needs review  
- `blocked` — waiting on consultation, permissions, or governance decision  
- `ready-for-review` — prepared for archaeology + sovereignty review  
- `approved` — approved to convert into canonical Story Node artifact  
- `promoted` — moved into official Story Node set (outside `notes/`)  
- `archived` — retired or merged into another item  

---

## 🗂️ Backlog Items

Structured backlog table (newest items should be added near the top).

| ID (Tentative) | Title / Topic | Status | Sensitivity / CARE Notes | Next Action |
|----------------|---------------|--------|---------------------------|------------|
| TBD-001 | Protohistoric camp (Smoky Hill region — generalized) | draft | Needs sovereignty review; decide masking level; avoid location triangulation | Prepare v11 Story Node outline + governance questions |
| TBD-002 | Arkansas River corridor survey (composite — generalized) | outline | Multi-season aggregation; ensure composite geometry rules | Define timeline window + dataset refs (STAC/DCAT if available) |
| TBD-003 | Walnut Basin lithic scatter (generalized) | draft | Sparse evidence; must include uncertainty framing | Write fact/interpretation split + confidence notes |
| TBD-004 | Historic fort periphery geophysics (generalized) | draft | Non-invasive; still avoid precise grid/line locations | Identify publishable assets; add governance notes |
| TBD-005 | Multi-phase Central Plains village (generalized) | concept | Requires phase separation; avoid cultural over-claims | Plan 2–3 node structure + time ranges |
| TBD-006 | 1930s WPA excavation archive (generalized) | outline | Do not include internal forms; link only published scans | Assemble public citations + archive provenance notes |
| TBD-007 | Post-contact trade corridors (regional — non-site) | research | Prefer regional story; low site sensitivity | Draft regional spatial scope + periodization |
| TBD-008 | Early Holocene occupation indicators (multi-county — generalized) | research | Broad scale; emphasize uncertainty + methods | Establish uncertainty language + candidate datasets |

Rules:

- Keep “Title / Topic” generalized (no site numbers, no excavation-unit identifiers).
- “Sensitivity / CARE Notes” describe constraints, not sensitive details.
- “Next Action” must be specific and governance-aware.

---

## 🧾 Backlog Item Template

Use this template when adding a new item (copy into the table row fields; do not add sensitive details):

~~~text
ID: TBD-###
Title/Topic: <generalized>
Status: concept | research | outline | draft | blocked | ready-for-review | approved | promoted | archived
Sensitivity/CARE Notes: <why it might be sensitive + what must be generalized>
Next Action: <single concrete next step + which board/council if applicable>
~~~

---

## 🧠 Story Node & Focus Mode Integration

This backlog is a **seedbed** for future Story Nodes.

Expected promotion path:

- Backlog entry (this file)  
  → reviewed outline (still generalized)  
  → canonical Story Node artifact (Markdown/JSON) with:
  - clear **facts vs interpretation** separation,
  - stable IDs,
  - links to governed sources (STAC/DCAT/PROV and/or approved citations),
  - explicit spatial/temporal scope and masking decisions.

Focus Mode MAY:

- generate a “Backlog heatmap” (counts by status, theme, or review queue),
- produce “ready-for-review” rollups for the Archaeology Domain Board,
- surface governance blockers (as metadata), without exposing sensitive content.

Focus Mode MUST NOT:

- infer precise locations,
- auto-fill missing details,
- convert backlog items into publishable Story Nodes without governance review.

---

## ⚖ Sovereignty & Ethics Reminders

Always note which items require:

- Tribal consultation / partner review (where applicable)
- Masking adjustments (H3 generalization, county-only, region-only, or no-geometry)
- Restricted knowledge removal (never store restricted details here)
- Narrative review for cultural sensitivity
- CARE justification (why the story is appropriate and how it avoids harm)

If an item is `blocked`, record the **governance reason** (policy/approval needed), not the restricted content.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Aligned with KFM-MDP v11.2.6: added signature/attestation refs, schema refs, origin-root provenance, and Story Node integration section. |
| v11.2.2 | 2025-11-30 | Initial governed backlog structure added to archaeology domain.                                       |
| v11.2.1 | 2025-11-29 | Added table structure + draft item schema.                                                            |

---

<div align="center">

🏺 **KFM v11.2.6 — Archaeology Story Node Backlog**  
Draft Pool · Sovereignty-Aware · FAIR+CARE-Aligned

[⬅ Back to Notes README](./README.md) ·
[⚖ Ethics Checklist](./ethics-checklist.md) ·
[📂 Archaeology Domain](../README.md) ·
[📂 Story Nodes Root](../../../README.md) ·
[📚 Docs Home](../../../../README.md) ·
[📘 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[🛡 Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>
