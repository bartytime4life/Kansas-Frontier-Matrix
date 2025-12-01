---
title: "🛡️ Kansas Frontier Matrix — Governance UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/Governance/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/web-governance-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-governance-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public (with CARE-governed exceptions)"
jurisdiction: "Kansas / United States"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
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
ai_transform_prohibited:
  - "summaries"
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
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 🛡️ **Kansas Frontier Matrix — Governance UI Components Overview**  
`web/src/components/Governance/README.md`

**Purpose:**  
Define the complete set of **governance- and ethics-oriented UI components** used throughout  
the KFM Web Platform to display CARE metadata, provenance chains, sovereignty warnings, masking  
information, license metadata, and ethical context requirements.  

These components ensure the frontend displays sensitive data ethically, transparently, and in  
strict compliance with FAIR+CARE Council policies.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

Governance UI components enforce **ethical transparency** across the KFM Web Platform by:

- Rendering CARE labels and classification badges  
- Displaying provenance chips & full PROV-O provenance trails  
- Warning users about sovereignty, cultural protocols, and masking rules  
- Surfacing dataset licensing and rights-holder information  
- Documenting transformation lineage and source tools  
- Marking AI-generated content and linking to model cards / evidence  
- Showing sensitive-site generalization (H3 masking, temporal bucketing)  
- Rendering governance drawers or panels with complete governance metadata  

These components appear in:

- Focus Mode v3 panels  
- Story Node v3 views  
- STAC/DCAT explorers  
- Map overlays and tooltips  
- Dataset detail panels  
- Timeline contextual warnings  
- Any location where sensitive or governed data appears  

---

## 🗂️ Directory Structure

~~~text
web/src/components/Governance/
│
├── 🎫 CAREBadge.tsx                # CARE classification tag with tooltip context
├── 📄 LicenseTag.tsx               # SPDX license display & license tooltip/link
├── 🧬 ProvenanceChip.tsx           # Inline chip showing immediate provenance & lineage hint
├── 🪢 ProvenanceTrail.tsx          # Expanded provenance visual chain/graph view
├── 🛑 SovereigntyNotice.tsx        # Warning UI for Indigenous/sovereignty-governed data
├── 🟡 MaskingIndicator.tsx         # Indicates H3 masking/redaction/temporal bucketing
├── 🧰 GovernanceDrawer.tsx         # Slide-out panel with full governance/metadata details
├── 🤖 AIGeneratedTag.tsx           # Marks AI-generated narrative segments clearly
└── 📢 EthicsContextBlock.tsx       # Required ethical disclaimers + CARE explanations
~~~

Any new governance component MUST be added to this structure and documented below.

---

## 🧩 Component Responsibilities

### 🎫 CAREBadge.tsx

**Role:**  
Visual, accessible badge indicating CARE classification for a dataset or entity.

**Responsibilities:**

- Display CARE classification (examples):
  - Public  
  - Low-Risk  
  - Restricted  
  - Sovereignty-Controlled  
  - Cultural Protocol Required  
- Provide a tooltip and/or assistive text describing:
  - Meaning of the classification  
  - Link to CARE guidelines / FAIR+CARE guide  

**Requirements:**

- Use a WCAG AA+-compliant color palette (never color-only semantics)  
- Accept classification as a prop (no inference inside the component)  

---

### 📄 LicenseTag.tsx

**Role:**  
Present SPDX license metadata in a compact, consistent way.

**Responsibilities:**

- Display:
  - SPDX identifier (e.g., `MIT`, `CC-BY-4.0`, `CC0-1.0`)  
  - Short label (e.g., “CC-BY 4.0”)  
- Provide:
  - Tooltip summarizing license  
  - Optional link to official SPDX or license text  

**Requirements:**

- Never assume a license; only render what is provided by metadata  
- Support “Custom” labels for non-standard or composite licenses  

---

### 🧬 ProvenanceChip.tsx

**Role:**  
Inline provenance summary for quick context.

**Displays:**

- Immediate source (archive, system, dataset)  
- Rights-holder or publisher (if available)  
- High-level transformation step (e.g., “OCR + NER v1.3”)  

**Interactions:**

- On click/activation → open `ProvenanceTrail` or `GovernanceDrawer` with full details  

**Requirements:**

- Must not invent or compress lineage beyond what is encoded in metadata  
- Accepts a precomputed provenance summary from the backend rather than inferring it  

---

### 🪢 ProvenanceTrail.tsx

**Role:**  
Detailed provenance and lineage view, aligned with PROV-O.

**Responsibilities:**

- Render the chain of:
  - `prov:Entity` (data artifacts)  
  - `prov:Activity` (ETL jobs, AI processes)  
  - `prov:Agent` (institutions, software)  
- Show:
  - Timestamps / time intervals  
  - Tools + versions (e.g., OCR engine, model version)  
  - CARE and license info per step when available  
- Provide:
  - JSON-LD / provenance export link for auditing  

**Requirements:**

- No invented nodes; show only documented provenance from backend/graph  
- Must be accessible to screen readers (list/tree with labels)  

---

### 🛑 SovereigntyNotice.tsx

**Role:**  
High-priority warning for Indigenous / sovereignty-governed data.

**Responsibilities:**

- Appear whenever:
  - Data intersects tribal jurisdictions  
  - Data is governed by Indigenous sovereignty policies  
  - Cultural/sacred sites may be implicated  
- Provide:
  - Clear textual warning  
  - Link to sovereignty and Indigenous data protection policy  
  - Explanation of any generalization or omissions applied due to sovereignty  

**Requirements:**

- Must be visible before or adjacent to any sensitive visualization/metadata  
- Support SR-only text for additional context where needed  

---

### 🟡 MaskingIndicator.tsx

**Role:**  
Indicate that masking / generalization has been applied.

**Responsibilities:**

- Show when:
  - H3-grid generalization is applied to geometry  
  - Spatial resolution is decreased  
  - Temporal resolution is bucketed (e.g., year-only)  
  - Certain fields are elided entirely  
- Provide:
  - Reason for masking/generalization  
  - Explanation of what has been removed or coarsened  

**Requirements:**

- Must never reveal the original unmasked values  
- Must be tied to explicit flags from metadata (no inference)  

---

### 🧰 GovernanceDrawer.tsx

**Role:**  
Slide-out drawer or panel that aggregates all governance-related metadata in one place.

**Displays:**

- CARE classification and labels  
- License & rights-holder  
- Sovereignty & cultural notices  
- ProvenanceTrail (full lineage)  
- AI usage & model details  
- Masking/generalization explanations  

**A11y:**

- Keyboard accessible  
- Uses ARIA roles (`dialog` / `complementary`) and `aria-labelledby`  
- Has focus trapping and return-to-origin behavior  

---

### 🤖 AIGeneratedTag.tsx

**Role:**  
Single, clear marker for AI-generated content segments.

**Responsibilities:**

- Label content as “AI-generated” when flagged from props  
- Provide:
  - Model name or ID (if supplied)  
  - Tooltip explaining that content is generated by an AI system  
  - Prompt to “Confirm with provenance documents”  

**Requirements:**

- Never applied by inference; only when a backend/graph explicitly flags content as AI-generated  

---

### 📢 EthicsContextBlock.tsx

**Role:**  
Display ethically mandated disclaimers and contextual statements.

**Responsibilities:**

- Present:
  - Cultural sensitivity warnings  
  - Historical uncertainty notes  
  - Interpretive constraints (e.g., “multiple perspectives exist”)  
  - AI narrative limitations and disclaimers  
- Provide:
  - Clear, plain-language explanations  
  - Optional links to longer explanatory resources  

**Requirements:**

- Text must be **non-speculative** and grounded in governance policy  
- Support screen-reader reading order and heading structure  

---

## 🔐 Governance & FAIR+CARE Integration

Governance components are central to KFM’s ethics.

They MUST:

- Respect:
  - `care_label`  
  - `classification`  
  - `indigenous_rights_flag`  
  - `redaction_required`  
- Never display:
  - High-precision coordinates for sovereignty-controlled or sensitive sites  
  - Full metadata that has been flagged for masking or embargo  
- Always:
  - Show CARE classification where applicable  
  - Attach provenance context for data transformations  
  - Mark AI-generated narrative segments when present  
  - Provide clear, accessible warnings when data is generalized or redacted  

**Governance rule violations are CI-blocking failures.**

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

Governance components MUST:

- Provide accessible tooltips (keyboard + SR)  
- Use semantic elements (`<span>`, `<button>`, `<section>`, etc.) with ARIA when necessary  
- Avoid reliance on color alone to convey classification / severity  
- Respect `prefers-reduced-motion` for animations (e.g., drawer transitions)  
- Maintain high color contrast (≥ 4.5:1 for text/icons)  

A11y regressions **must** be caught by tests and block merges.

---

## 📈 Telemetry Responsibilities

Governance UI components emit telemetry events (via higher-level wiring) such as:

- `"governance:view"` — a governance panel or drawer was viewed  
- `"governance:provenance-expanded"` — provenance details expanded  
- `"governance:drawer-open"` — GovernanceDrawer opened  
- `"care:badge-hover"` — CAREBadge hovered or focused  
- `"sovereignty:warning-shown"` — SovereigntyNotice displayed  
- `"ai:disclaimer-shown"` — AI disclaimer or EthicsContextBlock displayed  
- `"masking:indicator-toggle"` — masking details expanded/collapsed  

Telemetry MUST:

- Be non-PII  
- Respect CARE and privacy constraints  
- Match the schema specified in `telemetry_schema`  
- Be tied to component version for analysis and future audits  

---

## 🧪 Testing Requirements

Testing scope:

- **Unit tests:**
  - Rendering across different CARE classifications and license types  
  - Behavior when sovereignty flags are set  
  - Presence of required tooltips and labels  

- **Integration tests:**
  - Governance UI in Focus Mode panels  
  - Governance UI in dataset detail views and Story Node contexts  

- **Governance tests:**
  - Masking/hiding of sensitive data  
  - Proper display of warnings and disclaimers  

- **Accessibility tests:**
  - Keyboard access to tooltips, drawers, and warnings  
  - ARIA roles and labels correctness  
  - Color contrast checks (automated where possible)  

- **Telemetry tests:**
  - Emission of expected events on interaction  

Test file layout:

~~~text
tests/unit/web/components/Governance/**
tests/integration/web/components/Governance/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2 standards; added telemetry v2 and A11y clarifications |
| v10.4.0 | 2025-11-15 | Full governance component documentation; CARE, AI-label, provenance, masking rules |
| v10.3.2 | 2025-11-14 | Expanded governance interactions & improved provenance UI              |
| v10.3.1 | 2025-11-13 | Initial governance component overview                                  |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../README.md) •  
[Standards Index](../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · CIDOC-CRM · OWL-Time · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>