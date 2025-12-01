---
title: "🗃️ Kansas Frontier Matrix — DataCards Component Suite Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/DataCards/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/web-datacards-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-datacards-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public / Dataset-Sensitive"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "frontend-datacards"
semantic_intent:
  - "UI-component"
  - "dataset-metadata"
  - "governance-ui"
  - "provenance-ui"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Aware · Dataset Dependent"
sensitivity: "Variable"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

ttl_policy: "12 months"
sunset_policy: "Superseded upon next DataCards system upgrade"
immutability_status: "version-pinned"

json_schema_ref: "../../../../../schemas/json/web-components-datacards-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-datacards-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-datacards-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-datacards-readme-v11"
event_source_id: "ledger:web/src/components/DataCards/README.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with guardrails"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "speculative-content"
  - "hallucinated-metadata"
  - "unverified-claims"

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

provenance_chain:
  - "web/src/components/DataCards/README.md@v10.4.0"
  - "web/src/components/DataCards/README.md@v10.3.2"
---

<div align="center">

# 🗃️ **Kansas Frontier Matrix — DataCards Component Suite Overview**  
`web/src/components/DataCards/README.md`

**Purpose:**  
The **DataCards Suite** provides FAIR+CARE-governed, metadata-rich, provenance-linked UI components  
used throughout the Kansas Frontier Matrix v11 Web Client.  
They render spatial/temporal previews, dataset classifications, licenses, CARE badges,  
and provenance details in a consistent, accessible, deterministic format.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()  
[![SLSA Level 3](https://img.shields.io/badge/SLSA-Level%203-orange)]()

</div>

---

## 📘 Overview

DataCards v11 implement a **governed metadata UI framework** used for:

- STAC/DCAT dataset browsing  
- Story Node asset previews  
- Focus Mode contextual dataset lists  
- MapView adjacent dataset listings  
- Provenance and governance detail access  

**Core principles:**

- CARE-enforced masking & generalization  
- DCAT/STAC-aligned metadata display  
- Provenance chip integration  
- No speculative, inferred, or hallucinated metadata  
- Deterministic rendering (schema + TS type driven)  
- WCAG AA+ accessibility  
- Telemetry-emitting interactions  

---

## 🗂️ Directory Structure

~~~text
web/src/components/DataCards/
│
├── 🗃️ DataCard.tsx                   # Universal governed dataset/narrative card container
├── 🏷️ DataCardHeader.tsx             # Title, CARE badge, dataset-type label, provenance chip
├── 🧾 DataCardMetadata.tsx           # Key fields: publisher, license, time, space, rights
├── 🗺️ DataCardPreview.tsx            # Spatial/temporal preview with CARE-aware generalization
├── 🦶 DataCardFooter.tsx             # Open, explore, provenance actions
├── ♿ DataCardA11yHelpers.tsx        # ARIA scaffolding, focus order, a11y utilities
└── 🧱 DataCardSkeleton.tsx           # Non-sensitive loading state (no leaked metadata)
~~~

This structure is **mandatory**; any changes must be documented here.

---

## 🧩 Component Responsibilities

### 🗃️ DataCard.tsx
- Core wrapper: composes header, metadata, preview, footer  
- Enforces:
  - redaction rules  
  - sovereignty/CARE masking  
  - metadata hiding or generalization  
- Telemetry hooks (`datacard:*` events)  
- Deterministic rendering based on schema + props  
- Works as `<article>` with correct roles/regions  

---

### 🏷️ DataCardHeader.tsx
- Shows dataset title, dataset type, CARE badge, and provenance chip  
- `<header>` region—screen-reader discoverable  
- High-contrast tokens, no color-only semantics  
- CARE badge pulls classification from metadata, not inference  

---

### 🧾 DataCardMetadata.tsx
- Shows key dataset fields with dynamic masking logic  
- Supports:
  - publisher  
  - rights-holder  
  - license (SPDX)  
  - temporal extent  
  - spatial extent (H3 generalized)  
  - classification  
- Fields flagged as sensitive show **CARE-redaction tooltip**  
- No hallucinated or inferred metadata allowed  

---

### 🗺️ DataCardPreview.tsx
- Spatial mini-map preview:
  - H3-r7+ generalization applied  
  - No precise geometries for sovereignty-controlled datasets  
- Temporal mini-bar for intervals  
- All visuals require **textual equivalents**  
- Preview automatically disabled if `redaction_required = true`  

---

### 🦶 DataCardFooter.tsx
- Provides contextual actions:
  - Open dataset view  
  - Open in MapView  
  - View provenance  
- Restricted datasets → actions disabled with explanatory tooltip  
- Telemetry event: `"datacard:action"`  

---

### ♿ DataCardA11yHelpers.tsx
- Unified accessibility engine for DataCards  
- Provides:
  - ARIA labels  
  - Landmark roles  
  - Focus order utilities  
  - Reduced-motion alternatives  
- Required for WCAG AA+ compliance  

---

### 🧱 DataCardSkeleton.tsx
- Skeleton state with:
  - Reduced-motion shimmer  
  - High-contrast placeholders  
  - No reveal of sensitive fields  

---

## 🔐 Governance & FAIR+CARE Integration

DataCards v11 must:

- Enforce all CARE classifications  
- Mask spatial/temporal precision appropriately  
- Never display sovereign or sacred site coordinates  
- Display provenance metadata **for every dataset**  
- Label all AI-generated content (!), with source links  
- Block or annotate missing metadata instead of guessing  
- Follow Indigenous Data Sovereignty policy for all tribal datasets  

Governance & CARE checks are **CI-blocking**.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

DataCards must:

- Provide semantic HTML structure (`<article>`, `<header>`, `<footer>`)  
- Support full keyboard access  
- Maintain 4.5:1 contrast  
- Avoid color-only signals  
- Respect `prefers-reduced-motion`  
- Provide ARIA labels for all preview visualizations  

A11y failures → **CI BLOCK**.

---

## 📈 Telemetry Responsibilities

Events MUST be emitted on:

- `"datacard:open"`  
- `"datacard:hover"`  
- `"datacard:action"`  
- `"datacard:care-warning"`  
- `"datacard:provenance-expand"`  

OpenTelemetry schema MUST match `telemetry_schema` above.

All telemetry MUST be:

- non-PII  
- provenance-linked  
- tied to component version  

---

## 🧪 Testing Requirements

Required test coverage:

- Unit:  
  - Rendering  
  - Field masking  
  - Header/metadata/preview/footer logic  

- Integration:  
  - Focus Mode interactions  
  - STAC/DCAT dataset lists  
  - Story Node asset panels  

- Governance:  
  - Sovereignty masking  
  - Sensitive metadata blocking  
  - Generalization logic  

- Accessibility:
  - Keyboard paths  
  - ARIA correctness  
  - Contrast + reduced-motion  

- Telemetry:
  - Exact event shapes  
  - Emission on correct actions  

Test locations:

~~~text
tests/unit/web/components/DataCards/**
tests/integration/web/components/DataCards/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-30 | Full v11 upgrade: governance, metadata, A11y, telemetry, masking |
| v10.4.0 | 2025-11-15 | Previous major update (pre-v11 standards) |
| v10.3.2 | 2025-11-14 | CARE disclosure refinements |
| v10.3.1 | 2025-11-13 | Initial DataCards overview |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../../README.md) •  
[Standards Index](../../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE • CIDOC-CRM • OWL-Time • GeoSPARQL • STAC/DCAT • PROV-O • SLSA Level 3

**♻️ Sustainability:**  
Energy & Carbon Telemetry Enabled (ISO 50001 / ISO 14064)

**End of Document**

</div>