---
title: "🛡️ Kansas Frontier Matrix — Governance UI Components Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/Governance/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-governance-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-governance"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium (dependent on dataset sensitivity)"
sensitivity_level: "Mixed"
public_exposure_risk: "Dataset-dependent"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/components/Governance/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E30 Right"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../schemas/json/web-components-governance-readme.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-governance-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-governance-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-governance-readme"
event_source_id: "ledger:web/src/components/Governance/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public (with CARE-governed exceptions)"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded on next governance-component update"
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

</div>

---

# 📘 Overview

Governance UI components enforce **ethical transparency** across the Web Platform by:

- Showing CARE labels  
- Displaying provenance chips & chains  
- Warning users about sovereignty or masking rules  
- Surfacing dataset licensing  
- Documenting transformation lineage  
- Marking AI-generated content  
- Showing sensitive-site generalization notices  
- Rendering governance drawers or modals with detailed metadata  

These components appear in:

- Focus Mode v2.5  
- Story Node v3 views  
- STAC/DCAT explorers  
- Map overlays  
- Dataset detail panels  
- Timeline contextual warnings  
- Any location where sensitive or regulated data appears  

---

# 🧱 Directory Structure

~~~text
web/src/components/Governance/
├── CAREBadge.tsx                 # CARE classification tag with tooltip context
├── LicenseTag.tsx                # SPDX license display
├── ProvenanceChip.tsx            # Inline chip showing provenance & lineage
├── ProvenanceTrail.tsx           # Expanded provenance visual graph
├── SovereigntyNotice.tsx         # Warning UI for Indigenous/sovereignty-governed data
├── MaskingIndicator.tsx          # Indicates H3 masking/redaction applied
├── GovernanceDrawer.tsx          # Slide-out panel with full governance metadata
├── AIGeneratedTag.tsx            # Marks AI-generated narrative segments
└── EthicsContextBlock.tsx        # Required ethical disclaimers + CARE explanations
~~~

---

# 🧩 Component Responsibilities

## 🎫 **CAREBadge.tsx**
Displays the CARE classification of the dataset or entity:

- Public  
- Low-Risk  
- Restricted  
- Sovereignty-Controlled  
- Cultural Protocol Required  

Must show:

- Tooltip with CARE principles  
- Link to governance reference  
- Color-coded WCAG-compliant palette  

---

## 📄 **LicenseTag.tsx**
Displays SPDX license metadata:

- MIT  
- CC-BY  
- Public Domain  
- Custom dataset licenses  

Must include:

- Tooltip for license text  
- Link to official SPDX reference  

---

## 🧬 **ProvenanceChip.tsx**
Shows immediate provenance metadata:

- Source  
- Rights-holder  
- Transformation step  
- Tool + version that generated the data  

Interactive: opens `ProvenanceTrail`.

---

## 🪢 **ProvenanceTrail.tsx**
Expanded provenance graph:

- PROV-O aligned  
- Chronological transformation chain  
- CARE and license metadata per step  
- Optional JSON-LD download  

---

## 🛑 **SovereigntyNotice.tsx**
Shown when data intersects:

- Tribal jurisdictions  
- Indigenous-controlled data  
- Sovereignty-governed cultural assets  

Must include:

- Clear warning  
- Explanation text  
- Link to CARE principles  
- Alternative generalization guidance  

---

## 🟡 **MaskingIndicator.tsx**
Shows that geometry has been:

- H3-generalized (default r7)  
- Masked or blurred  
- Coarse-gridded  
- Time-bucketed  

Must include:

- Reason for masking  
- What was removed  
- CARE justification  

---

## 🧰 **GovernanceDrawer.tsx**
A drawer displaying full governance metadata:

- CARE classification  
- License  
- Rights-holder  
- Provenance chain  
- Sovereignty rules  
- Dataset lineage  
- AI generation markers  

Accessible via keyboard and screen readers.

---

## 🤖 **AIGeneratedTag.tsx**
Marks content generated by AI:

- Summaries  
- Highlights  
- Explanatory narratives  

Must:

- Display model label  
- Include confidence or availability of provenance  
- Include hover text: *“AI-generated. Confirm with provenance sources.”*

---

## 📢 **EthicsContextBlock.tsx**
Displays legally or ethically required disclaimers:

- Cultural sensitivity warnings  
- Sovereignty statements  
- Historical uncertainty indicators  
- Explanatory safeguards for AI-derived narrative  

All text must be:

- Plain-language  
- Screen-reader-friendly  
- Non-speculative  

---

# 🔐 Governance Enforcement Logic

All components MUST:

- Respect `ai_transform_prohibited` rules  
- Never display precise restricted coordinates  
- Never show unmasked sensitive sites  
- Always include provenance  
- Always include CARE labels  
- Render A11y-compliant warnings  
- Use color palettes with contrast ≥ 4.5:1  
- Be fully keyboard-operable  

Violation of these rules → CI blocks merge.

---

# ♿ Accessibility Requirements

Governance components have **strict** A11y rules:

- Screen-reader friendly tooltips  
- ARIA-expanded regions for drawers  
- WCAG AA color tokens  
- No motion without `prefers-reduced-motion` check  
- Short, understandable explanatory text  

A11y failures → **Immediate CI failure**.

---

# 📈 Telemetry Responsibilities

Governance UI emits telemetry on:

- `"governance:view"`  
- `"governance:provenance-expanded"`  
- `"care:badge-hover"`  
- `"sovereignty:warning-shown"`  
- `"ai:disclaimer-shown"`  
- `"masking:indicator-toggle"`  

All telemetry must be:

- Non-PII  
- Schema-valid  
- Linked to release-level telemetry bundles  

Stored in:

`releases/<version>/focus-telemetry.json`

---

# 🧪 Testing Requirements

Each governance component requires:

- Unit tests  
- Accessibility tests (tooltips, drawers, aria, focus trapping)  
- Governance rule tests (CARE, provenance, masking)  
- Telemetry correctness tests  
- Snapshot tests (optional)  

Tests located at:

~~~text
tests/unit/web/components/governance/**
tests/integration/web/components/governance/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full governance component documentation; added CARE, AI-label, provenance, sovereignty, masking rules |
| v10.3.2 | 2025-11-14 | Expanded governance interactions + improved provenance UI |
| v10.3.1 | 2025-11-13 | Initial governance component overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  

</div>