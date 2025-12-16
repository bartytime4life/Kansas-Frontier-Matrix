---
title: "⚖️ Kansas Frontier Matrix — Governance UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/Governance/README.md"
version: "v11.2.2"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
status: "Active / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: ""
previous_version_hash: ""
doc_integrity_checksum: ""

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/web-governance-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-governance-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public (with CARE-governed exceptions)"
jurisdiction: "Kansas / United States"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

header_profile: "standard"
footer_profile: "standard"
layout_profile: "immediate-one-branch-with-descriptions-and-emojis"
fencing_profile: "outer-backticks-inner-tildes-v1"

doc_kind: "Component Overview"
intent: "frontend-governance"
semantic_intent:
  - "UI-component"
  - "governance-ui"
  - "provenance-ui"
  - "care-sovereignty-ui"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium (dependent on dataset sensitivity)"
sensitivity_level: "Mixed"
public_exposure_risk: "Dataset-dependent"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/Governance/README.md@v11.2.2"
  - "web/src/components/Governance/README.md@v10.4.0"
  - "web/src/components/Governance/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E30 Right"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../schemas/json/web-components-governance-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-governance-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-governance-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-governance-readme-v11"
event_source_id: "ledger:web/src/components/Governance/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "unverified-architectural-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "🔐 Governance & FAIR+CARE Integration"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# ⚖️ **Kansas Frontier Matrix — Governance UI Components Overview**
`web/src/components/Governance/README.md`

**Purpose**  
Define the governed set of **ethics + governance UI components** used across the KFM Web Platform to surface:

- CARE labels and sensitivity cues
- Sovereignty / cultural protocol notices
- Masking / generalization indicators (spatial + temporal)
- License, rights-holder, and attribution requirements
- Provenance / lineage affordances (PROV-aligned references)
- AI-generated content markers and explainability framing (UI-side)
- Trust cues that point to release artifacts (SBOM / manifest / attestations) when available

These components are a **non-optional trust surface**: the UI never decides policy, but it MUST render and respect policy outcomes returned by governed APIs and catalogs.

[![Web Components](https://img.shields.io/badge/web%2Fsrc%2Fcomponents-README-blue)](../README.md) ·
[![Web Source Architecture](https://img.shields.io/badge/web%2Fsrc-ARCHITECTURE-blueviolet)](../../ARCHITECTURE.md) ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange)](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[![Sovereignty](https://img.shields.io/badge/Sovereignty-Policy-brightgreen)](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[![A11y](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)](../../../../docs/standards/INDEX.md)

</div>

---

## 📘 Overview

Governance UI components enforce **ethical transparency** across the KFM Web Platform by making governance state visible and unavoidable wherever governed content appears.

### Where these components appear

- Focus Mode v3 panels and explainability surfaces
- Story Node v3 cards and detail views
- STAC/DCAT dataset explorers and previews
- Map overlays, tooltips, and selection panels
- DetailDrawer headers/sections and any “why limited?” affordance

### Non-goals (hard boundaries)

Governance UI components MUST NOT:

- Perform policy decisions (backend/catalogs are authoritative)
- Reconstruct, infer, or “work around” masked precision
- Introduce new historical claims or speculative interpretations
- Call APIs directly (components are presentation-layer only)

### Pipeline position

~~~mermaid
flowchart TD
  A["Catalogs + APIs
STAC · DCAT · JSON-LD · REST/GraphQL"] --> B["Validated DTOs + Governance Flags
CARE · Sovereignty · Masking · License · Provenance"]
  B --> C["Governance UI Components
Badges · Notices · Provenance Chips · Drawers"]
  C --> D["User Understanding
Why limited · Where from · How to use"]
  C --> E["Privacy-safe Telemetry
Schema-validated · Aggregated · No PII"]
~~~

---

## 🗂️ Directory Structure

This suite lives in:

~~~text
web/src/components/Governance/
├── README.md                  # This document
├── CAREBadge.tsx              # CARE classification badge (no inference; fully accessible)
├── LicenseTag.tsx             # SPDX/license display + “use constraints” affordances
├── ProvenanceChip.tsx         # Compact “where did this come from?” chip
├── ProvenanceTrail.tsx        # Expanded provenance/lineage rendering (PROV-aligned, UI-side)
├── SovereigntyNotice.tsx      # Sovereignty/cultural protocol warning UI
├── MaskingIndicator.tsx       # “Generalized / masked / restricted” indicator with reason text
├── GovernanceDrawer.tsx       # Slide-out panel for full governance context (optional, UX-driven)
├── AIGeneratedTag.tsx         # Marker for AI-generated segments (explicit flags only)
└── EthicsContextBlock.tsx     # Plain-language ethical context + limitations (no speculation)
~~~

If the directory contents differ from this list, update this README to match the folder.

---

## 🧩 Component Responsibilities

This section is **contract-level**: it defines what each component MUST do regardless of styling framework choices.

### CAREBadge.tsx

**Role**  
Display the CARE classification for an entity (dataset, Story Node, focus summary, asset preview).

**Responsibilities**

- Render a CARE label that is:
  - visible
  - keyboard reachable (if interactive)
  - screen-reader legible
- Provide an explanation affordance (tooltip, popover, or inline help text) that:
  - does not rely on color alone
  - links to FAIR+CARE guidance when appropriate

**Hard boundaries**

- Must not infer the CARE label; it is provided as props/state.
- Must not downgrade or “soften” severity presentation.

---

### LicenseTag.tsx

**Role**  
Present license and use constraints in a compact, consistent way (SPDX and/or governed labels).

**Responsibilities**

- Display the supplied license identifier and short label.
- Provide a “how may I use this?” affordance that:
  - keeps attribution visible
  - does not hide restrictions behind deep navigation

**Hard boundaries**

- Never assumes a license (no defaults when missing).
- Never suggests permissions beyond what metadata declares.

---

### ProvenanceChip.tsx

**Role**  
Provide a compact provenance summary and a clear path to deeper inspection.

**Responsibilities**

- Display high-signal provenance cues such as:
  - source / dataset ID (or catalog reference)
  - publishing steward (when provided)
  - transformation hint (“derived”, “digitized”, “validated”, etc. when provided)
- Provide an activation path (click/keyboard) to open:
  - `ProvenanceTrail` and/or
  - `GovernanceDrawer` (if the UX uses a drawer)

**Hard boundaries**

- Must not fabricate missing lineage.
- Must not compress lineage into a misleading claim.

---

### ProvenanceTrail.tsx

**Role**  
Render detailed provenance and lineage affordances aligned with PROV concepts (UI-side rendering of recorded provenance).

**Responsibilities**

- Render a stable, accessible structure (list/tree) for:
  - entities (artifacts)
  - activities (transformations)
  - agents (publishers/tools/organizations) where provided
- Surface release confidence cues as links/references when available:
  - SBOM reference
  - manifest reference
  - attestations/signatures (if provided by upstream payloads)
- Provide an export/inspection affordance (e.g., “View JSON-LD provenance”) when such exports exist upstream.

**Hard boundaries**

- No invented nodes or inferred relationships.
- No leaking of masked identifiers or restricted coordinates through labels.

---

### SovereigntyNotice.tsx

**Role**  
High-priority warning UI for sovereignty-, cultural protocol-, or Indigenous-rights-governed content.

**Responsibilities**

- Display whenever upstream flags indicate sovereignty governance applies.
- Explain, in plain language:
  - that the content is governed
  - what user-visible limitations exist (masked, generalized, restricted)
  - where to learn more (link to sovereignty policy)

**Hard boundaries**

- Must not appear after sensitive content; it must be adjacent to or precede sensitive detail surfaces.
- Must not include sensitive location detail in the warning text itself.

---

### MaskingIndicator.tsx

**Role**  
Indicate that generalization, masking, or restriction has been applied.

**Responsibilities**

- Display the masking mode as an explicit status:
  - clear
  - generalized (e.g., grid/H3-style aggregation or reduced precision)
  - masked (fields hidden)
  - restricted (only high-level summary allowed)
- Provide a “why” explanation that:
  - states *that* masking occurred
  - states *why* at a high level (policy category or governance flag)
  - never reveals the original values

**Hard boundaries**

- Must not include raw unmasked values in tooltips, ARIA labels, or copy-to-clipboard helpers.
- Must not allow user toggles that remove enforced masking.

---

### GovernanceDrawer.tsx

**Role**  
A governed, accessible container for “full governance context” (optional UX pattern).

**Responsibilities**

- Aggregate governance-related UI in one place:
  - CAREBadge
  - SovereigntyNotice
  - MaskingIndicator
  - LicenseTag
  - ProvenanceTrail
  - AI markers and limitations text (if applicable)
- Enforce safe overlay behavior:
  - focus management
  - keyboard operability
  - non-leaky error states (no internal IDs in user messages)

**Hard boundaries**

- Must not provide an “override” path for policy outcomes.
- Must not fetch additional governed data directly (container stays in presentation layer).

---

### AIGeneratedTag.tsx

**Role**  
Mark AI-generated segments as AI-generated, with explicit upstream flags.

**Responsibilities**

- Label AI-generated content clearly and consistently.
- Provide a plain-language tooltip/help:
  - what AI-generated means in KFM
  - where to verify (evidence/provenance affordance)

**Hard boundaries**

- Never applied by inference.
- Must not imply certainty where model outputs are probabilistic.

---

### EthicsContextBlock.tsx

**Role**  
Provide required ethical disclaimers and interpretive constraints in plain language.

**Responsibilities**

- Render only policy-approved, non-speculative text blocks such as:
  - cultural sensitivity notices
  - limitations due to redaction/masking
  - “multiple perspectives may exist” framing when required by policy
- Maintain stable reading order and a11y semantics.

**Hard boundaries**

- Must not add unverified historical claims.
- Must not speculate on intent, sacredness, or community positions.

---

## 🔐 Governance & FAIR+CARE Integration

Governance components are a **governance-critical UI surface** and MUST implement defense-in-depth.

### Non-negotiable behaviors

- Always surface CARE label and masking state where governed content is shown.
- Always honor:
  - `indigenous_rights_flag`
  - `redaction_required`
  - sovereignty flags
  - license/use constraints
- Never provide UI affordances that:
  - hide governance overlays for governed assets
  - reconstruct masked precision from derived cues (labels, geometry, timeline granularity)
  - downgrade restrictions to “warnings”

### Safe rendering requirements (anti-leak)

Governance components MUST treat the following as potential leak channels:

- Tooltip content
- ARIA labels/descriptions
- Copy-to-clipboard helpers
- Telemetry payloads
- “Debug” error displays

If policy requires masking, all of the above MUST reflect the masked/generalized representation only.

### Integration with other governed UI patterns

Common composition points include:

- DetailDrawer header and provenance sections (see `../DetailDrawer/README.md`)
- Focus Mode panels and “why am I seeing this?” affordances
- Catalog explorer cards (STAC/DCAT previews)

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

Governance UI must remain usable for keyboard-only and assistive technology users.

Minimum requirements:

- Tooltips/popovers are keyboard operable and dismissible.
- Severity and classification do not rely on color alone.
- Icons include accessible names (SR-only text when needed).
- Notices are placed in reading order and are not visually-only overlays.
- Drawers/overlays:
  - have correct ARIA roles (`dialog` or `complementary`)
  - provide `aria-labelledby`
  - manage focus and return focus on close
- Animations and transitions respect `prefers-reduced-motion`.

Any accessibility regression in governance components is treated as a **hard failure** because it blocks users from understanding policy outcomes.

---

## 📈 Telemetry Responsibilities

Governance UI components are often the first point where users encounter governance outcomes. Telemetry supports reliability, compliance reporting, and UX improvement.

### Principles

Telemetry MUST be:

- schema-validated (`telemetry_schema`)
- aggregated / privacy-safe (no PII)
- governance-aware (include coarse flags such as redaction applied, not raw values)

### Recommended event families (names are contract-level; schema governs final shape)

- `governance:view` — a governance surface became visible
- `governance:why_limited_open` — user opened a “why limited?” explainer
- `governance:provenance_open` — provenance trail opened/expanded
- `governance:license_view` — license/use constraints expanded
- `governance:sovereignty_notice_shown` — sovereignty notice rendered (non-sensitive boolean)
- `governance:masking_explained` — masking explanation viewed
- `governance:ai_marker_view` — AI marker tooltip/help viewed

### Minimum event shape

~~~json
{
  "event_name": "governance:view",
  "ts": "2025-12-16T00:00:00Z",
  "component": "Governance",
  "component_version": "v11.2.2",
  "surface": "detaildrawer",
  "entity_type": "dataset",
  "entity_id": "kfm:dataset:example-id",
  "care_label": "Public / Medium",
  "redaction_applied": true,
  "result": "ok"
}
~~~

Telemetry MUST NOT include:

- free-form user input
- raw excerpts from governed sources
- precise coordinates when masking is required
- stable cross-session identifiers

---

## 🧪 Testing Requirements

Testing must demonstrate that governance components are:

- correct (render expected props)
- safe (no leaks under masking/redaction)
- accessible (keyboard + screen reader)
- telemetry-consistent (events emitted via governed pathways)

### Required coverage

- **Unit**
  - renders all labels/states without inference
  - tooltips/popovers have accessible names
  - masking indicators never expose raw values
- **Integration**
  - Focus Mode panel composition
  - Story Node + DetailDrawer composition
  - STAC/DCAT explorer composition
- **Governance safety**
  - sovereignty flags force notices and suppress unsafe detail
  - redaction_required drives generalized/masked UI
- **Accessibility**
  - keyboard access to all interactive governance affordances
  - drawer/panel roles and focus behavior
- **Telemetry**
  - events emitted through the telemetry layer with schema-valid payloads

Suggested test locations:

~~~text
tests/unit/web/components/Governance/**
tests/integration/web/components/Governance/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-12-16 | Documentation refresh: aligned to KFM-MDP v11.2.6; clarified governance boundaries (render-only), anti-leak requirements (tooltips/ARIA/telemetry), trust-cue references (SBOM/manifest), and composition patterns with Focus/Story/DetailDrawer. |
| v10.4.0 | 2025-11-15 | Full governance component documentation; CARE, AI-label, provenance, masking rules. |
| v10.3.2 | 2025-11-14 | Expanded governance interactions and improved provenance UI. |

---

## ⚖️ Footer

**Governance links**  
[Docs Root](../../../../README.md) •
[Standards Index](../../../../docs/standards/INDEX.md) •
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) •
[Sovereignty Policy](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) •
[Web Architecture](../../../ARCHITECTURE.md) •
[Components Overview](../README.md)

**Compliance**  
FAIR+CARE · CIDOC-CRM · OWL-Time · STAC/DCAT · PROV-O · WCAG 2.1 AA+ · SLSA-aligned provenance

**End of document**
