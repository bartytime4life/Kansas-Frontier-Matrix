---
title: "🏺 KFM v11.2.6 — Archaeology Story Node Ethics & Sovereignty Checklist"
path: "docs/story-nodes/domains/archaeology/notes/ethics-checklist.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · Indigenous Data Governance Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Checklist"
intent: "kfm-archaeology-ethics-checklist"
lifecycle_stage: "stable"

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

fair_category: "F1-A1-I1-R3"
care_label: "High Sensitivity · Indigenous-Linked"
classification: "Internal-Review (Must remain public-safe if committed)"
classification_scope_note: "This checklist is safe to publish; Story Node drafts are not unless generalized and approved."

sensitivity: "Cultural Heritage Governance (Non-site-specific)"
sensitivity_level: "Moderate/High (Process-level; no sensitive locations)"
public_exposure_risk: "Low (if no restricted details are added)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Indigenous Data Governance Board + Archaeology Domain Board"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 sovereignty rules"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:storynodes:archaeology:ethicschecklist:v11.2.6"
semantic_document_id: "kfm-storynodes-archaeology-ethicschecklist"
event_source_id: "ledger:storynodes/archaeology/ethicschecklist"

provenance_chain:
  - "docs/story-nodes/domains/archaeology/notes/ethics-checklist.md@v11.2.2"
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
  - "a11y-adaptations"
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
    - "🧭 How to Use This Checklist"
    - "✅ Ethics & Sovereignty Checklist"
    - "🕊 Reviewer Sign-off"
    - "🧠 Story Node & Focus Mode Integration"
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

# 🏺 **Archaeology Story Node — Ethics & Sovereignty Checklist (KFM v11)**  
### *CARE Principles · Indigenous Data Sovereignty · Masking Rules · Ethical Review*  

`docs/story-nodes/domains/archaeology/notes/ethics-checklist.md`

**Purpose**  
Provide a governed checklist for evaluating archaeology Story Nodes (Markdown or JSON), ensuring compliance with  
**FAIR+CARE**, **Indigenous data sovereignty**, and KFM v11 story-node publication guardrails.

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
                ├── 📄 backlog.md          # Draft pool & triage table
                └── ⚖️ ethics-checklist.md # This file — required checklist for review
~~~

---

## 📘 Overview

This checklist is mandatory for archaeology Story Nodes because archaeology narratives can intersect:

- culturally sensitive places and practices,
- living communities and Indigenous Nations,
- locations that must not be disclosed (even indirectly),
- archives with rights restrictions,
- interpretive uncertainty that can be misread as fact.

This document is **process-level and non-site-specific**. Do not add sensitive site details here.

---

## 🧭 How to Use This Checklist

Use this checklist **before** submitting any archaeology Story Node for review.

Rules:

- Every item must be **Yes**, **No**, or **N/A** with notes.
- Any **No** requires either:
  - remediation before review, or
  - a documented governance exception (rare; must reference the governance charter).

CI/CD gating expectations:

- Markdown/metadata checks apply to this file.
- Story Node linting and sovereignty checks apply to Story Node artifacts that this checklist gates.

---

## ✅ Ethics & Sovereignty Checklist

### 🔐 1) Sensitive Location Safety

| Question | Yes/No/N/A | Notes |
|----------|------------|-------|
| Is all spatial representation generalized (H3/county/region/watershed) with no precise coordinates? |  |  |
| Could any combination of narrative + generalized geometry still enable triangulation? |  |  |
| Are burial/sacred areas excluded or masked beyond recognition (or omitted entirely)? |  |  |
| Does the narrative avoid describing access routes, nearby landmarks, or landowner identifiers? |  |  |
| If “no-geometry” is required, is it enforced (metadata-only node or redacted geometry)? |  |  |

---

### ⚖ 2) Indigenous Data Sovereignty

| Question | Yes/No/N/A | Notes |
|----------|------------|-------|
| Does this Story Node require consultation with an Indigenous Nation/community or authorized steward? |  |  |
| If consultation is required, is the consultation status recorded (without including restricted content)? |  |  |
| Does the narrative avoid attribution claims that exceed evidence or permissions? |  |  |
| Is restricted Indigenous knowledge omitted (or stored only in approved restricted systems, not in-repo)? |  |  |
| Is CARE justification documented (collective benefit, authority to control, responsibility, ethics)? |  |  |

---

### 🧱 3) Observation vs Interpretation vs Speculation

| Question | Yes/No/N/A | Notes |
|----------|------------|-------|
| Are **observations** clearly separated from **interpretations**? |  |  |
| Are interpretations evidence-linked (citations, datasets, methods) and not overconfident? |  |  |
| Are uncertainties and confidence limits explicitly stated (dating precision, survey bias, preservation)? |  |  |
| Is speculation avoided or explicitly labeled as speculation (and minimized)? |  |  |

---

### 📦 4) Data Sources, Rights, and Provenance

| Question | Yes/No/N/A | Notes |
|----------|------------|-------|
| Are all cited sources public or cleared for release under stated rights/licenses? |  |  |
| Are restricted excavation forms, confidential site reports, or partner-restricted documents excluded? |  |  |
| Are archive scans and images used according to rights/licensing and properly attributed? |  |  |
| If STAC/DCAT/PROV assets are referenced, are IDs and licenses correct and stable? |  |  |

---

### 🌐 5) Spatial + Temporal Modeling

| Question | Yes/No/N/A | Notes |
|----------|------------|-------|
| Is geometry valid and generalized, and does spatial precision match the claim? |  |  |
| Are temporal ranges expressed using appropriate precision (intervals vs single dates)? |  |  |
| For multi-phase occupations, are phases modeled as separate nodes (or clearly separated sections) rather than blended? |  |  |
| If place names are used, are they non-sensitive and not effectively doxxing a location? |  |  |

---

### 🔗 6) Graph Relations and Linking Safety

| Question | Yes/No/N/A | Notes |
|----------|------------|-------|
| Are graph relationships chosen from approved patterns (no ad-hoc semantics)? |  |  |
| Are linked entities public-safe (no restricted node IDs, no confidential place nodes)? |  |  |
| Are reinterpretations handled via explicit “counterpoint/alternate interpretation” modeling where applicable? |  |  |
| Are provenance links provided for key claims (datasets, methods, curation activity)? |  |  |

---

### 🖼️ 7) Media and Derived Asset Safety

| Question | Yes/No/N/A | Notes |
|----------|------------|-------|
| Are images/maps/generalized figures non-sensitive and not revealing site features? |  |  |
| For geophysics/LiDAR/rasters: are they masked/generalized and not offering actionable detail? |  |  |
| Are thumbnails/preview assets safe at common zoom levels (no “zoom to reveal”)? |  |  |
| Are rights and licenses stated for each asset? |  |  |

---

### 🌱 8) Environmental & Cultural Context (Harm-Minimizing Narrative)

| Question | Yes/No/N/A | Notes |
|----------|------------|-------|
| Is environmental context generalized (avoid parcel-level specifics)? |  |  |
| Does the narrative avoid landowner identification or detailed site-adjacent infrastructure? |  |  |
| Does the narrative avoid unsupported cultural attributions and stereotypes? |  |  |
| Are regional terms preferred over site-specific identifiers and “treasure-hunt” framing avoided? |  |  |

---

### 🧪 9) CI/CD Readiness

| Question | Yes/No/N/A | Notes |
|----------|------------|-------|
| If JSON Story Node: validates against the applicable Story Node schema? |  |  |
| If Markdown Story Node: meets KFM-MDP rules (headings, links, footer, metadata)? |  |  |
| Passes sovereignty/CARE linting and sensitivity checks in CI? |  |  |
| All referenced links (STAC/DCAT/PROV/docs) resolve correctly in-repo? |  |  |

---

## 🕊 Reviewer Sign-off

| Reviewer Type | Name/Org | Approved? | Notes |
|---------------|----------|-----------|-------|
| Archaeology Domain Reviewer |  |  |  |
| Indigenous Data Reviewer / Authorized Steward |  |  |  |
| FAIR+CARE Council |  |  |  |
| Governance Board (if required) |  |  |  |

---

## 🧠 Story Node & Focus Mode Integration

This checklist is used as a governance guardrail for:

- Story Node promotion from `notes/` → canonical Story Node sets
- Focus Mode inclusion decisions (what can be shown, at what spatial precision, with what narrative constraints)
- audit trails (why a node was generalized, redacted, or blocked)

Focus Mode MAY reference checklist completion status as metadata.

Focus Mode MUST NOT:

- infer “approval” if sign-off is missing,
- auto-upgrade geometry precision,
- generate missing cultural attribution or consultation status.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Upgraded to KFM-MDP v11.2.6; aligned metadata refs, added directory layout, tightened public-safe rules, and clarified Focus Mode constraints. |
| v11.2.2 | 2025-11-30 | Initial governed sovereignty & ethics checklist for archaeology.         |
| v11.2.1 | 2025-11-29 | Added reviewer table, masking prompts, and CI readiness fields.          |

---

<div align="center">

🏺 **KFM v11.2.6 — Archaeology Ethics & Sovereignty Checklist**  
CARE-Aligned · Sovereignty-Aware · Governance-Ready

[⬅ Back to Notes README](./README.md) ·
[📄 Backlog](./backlog.md) ·
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
