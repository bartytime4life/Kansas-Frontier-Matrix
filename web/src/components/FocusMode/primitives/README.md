---
title: "🎯 Kansas Frontier Matrix — FocusMode Primitives Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/FocusMode/primitives/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-components-focusmode-primitives-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-focusmode-primitives"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium (entity-dependent)"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/focus/README.md@v10.3.2"
  - "web/src/components/FocusMode/README.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../../schemas/json/web-components-focusmode-primitives.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/web-components-focusmode-primitives-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-focusmode-primitives-v10.4.0"
semantic_document_id: "kfm-doc-web-components-focusmode-primitives"
event_source_id: "ledger:web/src/components/FocusMode/primitives/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Prohibited (UI primitives only)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "narrative expansion"
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public (with CARE-governance constraints)"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review every release"
sunset_policy: "Superseded upon FocusMode v3 primitive refactor"
---

<div align="center">

# 🎯 **Kansas Frontier Matrix — FocusMode Primitives Overview**  
`web/src/components/FocusMode/primitives/README.md`

**Purpose:**  
Document the **legacy-but-supported FocusMode UI primitives**, now housed under  
`web/src/components/FocusMode/primitives/` for compatibility, modularity,  
and deterministic integration into **Focus Mode v2.5**.  
These primitives serve as **low-level UI building blocks** used internally by the  
higher-order components in `FocusMode/` (e.g., `FocusSummary`, `ExplainabilitySection`, `RelationsPanel`).  

They remain FAIR+CARE-governed, WCAG-compliant, and maintained for backward stability.

</div>

---

# 📘 Overview

FocusMode primitives are:

- Lightweight, composable UI elements  
- Contained entirely within FocusMode’s domain  
- Used as internal implementation tools  
- Never imported outside the `FocusMode/` folder  
- Required for certain cross-component rendering paths  
- Fully FAIR+CARE governed  
- Fully WCAG 2.1 AA accessible  

These components **must not** contain:

- Business logic  
- Backend calls  
- Narrative inference  
- Unmasked sensitive data  
- Speculative AI-driven expansions

They must strictly serve as **presentation primitives**.

---

# 🧱 Directory Structure (Labeled)

~~~text
web/src/components/FocusMode/primitives/
├── FocusPanel.tsx                 # Legacy unified focus panel wrapper
├── RelatedEntityCard.tsx          # Older related entity card primitive
├── FocusNarrative.tsx             # Legacy narrative block (pre-refactor)
├── ExplanationBlock.tsx           # Early SHAP/LIME explanation renderer
└── CARENotices.tsx                # CARE / sovereignty / ethics warning block
~~~

---

# 🧩 Component Responsibilities

## 📦 **FocusPanel.tsx**
A pre-refactor panel layout component once used as the main Focus Mode container.

Now serves as:

- A structural primitive for sectioning  
- A legacy wrapper for nested content  
- A controlled layout surface for certain fallback views  

Governance:
- Must never display prohibited detail  
- Must pass through CARE banners and provenance metadata  

---

## 🧭 **RelatedEntityCard.tsx**
Old format card for displaying:

- Entity names  
- Types  
- Short descriptions  

Still used internally for:

- Secondary relation listings  
- Inline previews within the RelationsPanel  

Governance:
- Must identify sovereignty-controlled relations  
- Must generalize sensitive spatial or cultural links  

---

## 📝 **FocusNarrative.tsx**
Legacy narrative presentation block.

Now used for:

- Simple text bodies  
- Non-AI, non-speculative entity descriptions  
- Internal composition inside FocusSummary  

Governance:
- MUST refuse speculative output  
- MUST annotate uncertain info with provenance signals  

---

## 🤖 **ExplanationBlock.tsx**
Early SHAP/LIME explainability UI primitive.

Now:

- Wrapped by `ExplainabilitySection.tsx`  
- Presents influence weights  
- Shows explainability attributions  

Governance:
- MUST show model name + source  
- MUST avoid fabricating explanations  

---

## ⚠️ **CARENotices.tsx**
Displays governance-critical notices:

- Sovereignty warnings  
- Cultural protocol disclaimers  
- Generalization explanations  
- CARE classification labels  

All Focus Mode pages must surface this component  
**before** showing sensitive context.

---

# 🔐 Governance & FAIR+CARE Integration

Each primitive must:

- Propagate CARE metadata  
- Mask or generalize sensitive fields/events  
- Display provenance clearly  
- Obey sovereignty restrictions  
- Forbid display of unverified details  
- Forbid AI-generated or speculative narrative rendering  

Violations → **CI BLOCKER**

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

FocusMode primitives must:

- Provide proper ARIA semantics  
- Respect reduced-motion settings  
- Maintain keyboard operability  
- Use high-contrast color tokens  
- Provide SR-only equivalents for non-text media  

Accessibility regressions → **merge blocked**

---

# 📈 Telemetry Requirements

Although primitives do not emit telemetry on their own,  
they must cooperate with the telemetry system by:

- Exposing stable props/events for higher-level components  
- Ensuring internal changes do not break event chains  
- Not emitting PII or sensitive details  

---

# 🧪 Testing Expectations

Each primitive must include:

- Unit tests  
- A11y tests  
- Governance & masking tests  
- Snapshot tests (only for stable UI patterns)  

Test locations:

~~~text
tests/unit/web/components/FocusMode/primitives/**
tests/integration/web/components/FocusMode/primitives/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Added primitives overview; aligned with Focus Mode v2.5 refactor |
| v10.3.2 | 2025-11-14 | Legacy focus/ → FocusMode/primitives migration |
| v10.3.1 | 2025-11-13 | Focus primitives created under old focus/ folder |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1  

</div>

