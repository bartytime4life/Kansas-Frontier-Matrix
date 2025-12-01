---
title: "🎯 Kansas Frontier Matrix — FocusMode Primitives Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/FocusMode/primitives/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/web-focusmode-primitives-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-components-focusmode-primitives-v2.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public (with CARE-governance constraints)"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "frontend-focusmode-primitives"
semantic_intent:
  - "UI-component"
  - "low-level-primitive"
  - "focus-mode"
  - "governance-ui"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium (entity-dependent)"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/focus/README.md@v10.3.2"
  - "web/src/components/FocusMode/README.md@v10.4.0"
  - "web/src/components/FocusMode/primitives/README.md@v10.4.0"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../../../schemas/json/web-components-focusmode-primitives-v11.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/web-components-focusmode-primitives-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-focusmode-primitives-v11.2.2"
semantic_document_id: "kfm-doc-web-components-focusmode-primitives-v11"
event_source_id: "ledger:web/src/components/FocusMode/primitives/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Prohibited (UI primitives only)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "summaries"
  - "narrative-expansion"
  - "speculative-additions"
  - "unverified-historical-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "🔐 Governance & FAIR+CARE Integration"
    - "♿ Accessibility Requirements (WCAG 2.1 AA+)"
    - "📈 Telemetry Requirements"
    - "🧪 Testing Expectations"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 🎯 **Kansas Frontier Matrix — FocusMode Primitives Overview**  
`web/src/components/FocusMode/primitives/README.md`

**Purpose:**  
Describe the **legacy-but-supported FocusMode UI primitives**, housed under  
`web/src/components/FocusMode/primitives/` for compatibility, modularity,  
and deterministic integration into **Focus Mode v3**.  

These primitives are **low-level UI building blocks** used internally by higher-order FocusMode components  
(e.g., `FocusSummary`, `ExplainabilitySection`, `RelationsPanel`) and remain FAIR+CARE-governed,  
WCAG-compliant, and maintained for backward stability.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

**FocusMode primitives** are:

- Lightweight, composable UI elements  
- Contained entirely within the `FocusMode/` domain  
- Used as **internal implementation tools** for v3 FocusMode components  
- Never imported outside the `FocusMode/` folder  
- Required for certain cross-component rendering paths and fallback behaviors  
- Fully FAIR+CARE governed and WCAG 2.1 AA+ accessible  

These primitives **must not** contain:

- Business logic  
- Backend calls or data fetching  
- Narrative inference or AI summarization  
- Unmasked sensitive data  
- Speculative AI-driven expansions or invented relationships  

They are strictly **presentation primitives** and must remain deterministic and predictable.

---

## 🗂️ Directory Structure

~~~text
web/src/components/FocusMode/primitives/
│
├── 🧩 FocusPanel.tsx               # Legacy unified focus panel wrapper/layout primitive
├── 📇 RelatedEntityCard.tsx        # Older related entity card primitive
├── 📜 FocusNarrative.tsx           # Legacy narrative text block (pre-refactor)
├── 🤖 ExplanationBlock.tsx         # Early SHAP/LIME explanation renderer
└── ⚠️ CARENotices.tsx              # CARE / sovereignty / ethics warning block
~~~

Any additions or changes MUST be updated here and documented below.

---

## 🧩 Component Responsibilities

### 🧩 FocusPanel.tsx

**Role:**  
Pre-refactor panel layout component once used as the main Focus Mode container; now a structural primitive.

**Responsibilities:**

- Provide consistent margin/padding/layout for nested focus content  
- Serve as a **wrapper** for sections within FocusMode (e.g., summary, narrative)  
- Never fetch data or apply business logic  
- Pass through governance and A11y props used by higher-level components  

**Governance:**

- Must never directly render prohibited detail (sensitive fields must already be masked by parent components)  
- Must accept and pass CARE banners/provenance metadata down without altering them  

---

### 📇 RelatedEntityCard.tsx

**Role:**  
Legacy card primitive for displaying related entities in FocusMode v2.x; still used internally for some relation lists.

**Displays:**

- Entity name / label  
- Entity type (person, place, event, document, Story Node)  
- Short description or snippet (non-speculative)  

**Usage:**

- Secondary relation lists  
- Inline previews in `RelationsPanel`  
- Fallback rendering when new card variants are not applied  

**Governance:**

- Must indicate sovereignty-controlled relations via styling/labels passed from parent  
- Must generalize or hide sensitive relation metadata as instructed by parent props  
- Must never fabricate descriptions or types  

---

### 📜 FocusNarrative.tsx

**Role:**  
Legacy narrative presentation block, now used purely for **displaying text** supplied by the backend / Story Nodes.

**Responsibilities:**

- Render narrative text segments received purely as props  
- Highlight inline provenance or references if provided by parent component  
- Provide a clean, readable block layout compatible with A11y helpers  

**Governance:**

- MUST NOT generate or infer narrative text itself  
- MUST NOT alter narrative content beyond simple formatting (line breaks, emphasis)  
- MUST display or accept AI-labeling flags from parent to indicate AI-originating segments  

---

### 🤖 ExplanationBlock.tsx

**Role:**  
Early explainability primitive for showing SHAP/LIME-like attributions; now wrapped by `ExplainabilitySection.tsx`.

**Responsibilities:**

- Display influence weights and feature attributions for AI model decisions  
- Display model identifier and source if passed in props  
- Present simple bar/label structure that higher-level components fill with exact values  

**Governance:**

- All values MUST be supplied from backend payloads; no calculations in the component beyond formatting  
- MUST NOT fabricate, interpolate, or “smooth” attributions; show them exactly as provided  
- MUST label explainability content as model behavior explanation, **not** historical fact  

---

### ⚠️ CARENotices.tsx

**Role:**  
Primitive block for rendering CARE, sovereignty, and ethics warnings.

**Responsibilities:**

- Display:
  - Sovereignty warnings  
  - Cultural sensitivity or sacred site notices  
  - Generalization/masking explanations  
  - CARE classification labels (e.g. “Sovereignty-controlled”)  

- Provide:
  - A clear, visible section for these warnings  
  - Hooks for screen-reader context (via A11y helpers)  

**Usage:**

- Typically included at the top of FocusMode panels where sensitive information might appear  
- Higher-level components must ensure CARENotices appears **before** sensitive content  

---

## 🔐 Governance & FAIR+CARE Integration

Even as low-level primitives, these components are part of a governance-critical surface.

They MUST:

- Respect all governance & CARE props provided by higher-level components  
- Never bypass or weaken masking logic (e.g., never un-generalize spatial extents)  
- Never generate narrative or metadata from thin air — only display props passed down  
- Support labeling of AI-generated content via prop flags and A11y hints  
- Work with the **Indigenous Data Protection** policy: never reveal sensitive location details directly  

Violating governance expectations is a **CI-blocking failure**.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

FocusMode primitives MUST:

- Use semantic HTML where appropriate (e.g., `<section>`, `<p>`, `<div>` with ARIA role where necessary)  
- Delegate ARIA roles and labels to `FocusA11yHelpers` (in parent directory) for consistency  
- Respect `prefers-reduced-motion` by avoiding heavy animations in their own implementation  
- Keep text readable and high contrast (≥ 4.5:1)  
- Ensure clickable elements are keyboard focusable when used as interactive surfaces (parent components usually wrap them)  

Any change diminishing accessibility must be caught in tests and block merges.

---

## 📈 Telemetry Requirements

Primitives themselves:

- DO NOT emit telemetry directly  
- MUST expose stable props / event handlers so that higher-level FocusMode components can emit telemetry accurately  

Expectations:

- No PII or sensitive content in events triggered by interactions with these primitives  
- No event name changes that silently break upstream telemetry without tests  

If a primitive changes behavior in a way that affects higher-level telemetry, tests for those higher-level events MUST be updated.

---

## 🧪 Testing Expectations

Each primitive MUST be covered by:

- Unit tests:
  - Rendering with typical / edge-case props  
  - Governance-related props (e.g., flags that alter styling or content visibility)  
- A11y checks (where relevant in isolation):
  - ARIA attributes present on key wrappers  
  - No inaccessible text-only icons without SR text  
- Governance & masking tests:
  - Confirm that the primitive does not unmask or reveal hidden props  

Test file layout:

~~~text
tests/unit/web/components/FocusMode/primitives/**
tests/integration/web/components/FocusMode/primitives/**    # only where primitives are used in context
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                        |
|--------:|------------|----------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2 standards; clarified primitive-only role   |
| v10.4.0 | 2025-11-15 | Added primitives overview; aligned with Focus Mode v2.5        |
| v10.3.2 | 2025-11-14 | Legacy `focus/` → `FocusMode/primitives/` migration            |
| v10.3.1 | 2025-11-13 | Focus primitives created under old `focus/` folder             |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../../../README.md) •  
[Standards Index](../../../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · CIDOC-CRM · OWL-Time · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>