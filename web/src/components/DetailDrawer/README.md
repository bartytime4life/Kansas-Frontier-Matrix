---
title: "📂 Kansas Frontier Matrix — DetailDrawer Component Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/DetailDrawer/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/web-detaildrawer-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-detaildrawer-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public with CARE/sovereignty exceptions"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "frontend-detaildrawer"
semantic_intent:
  - "UI-component"
  - "contextual-detail"
  - "governance-ui"
  - "provenance-ui"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium (content-dependent)"
sensitivity_level: "Variable"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/DetailDrawer/README.md@v10.4.0"
  - "web/src/components/DetailDrawer/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../../schemas/json/web-components-detaildrawer-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-detaildrawer-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-detaildrawer-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-components-detaildrawer-readme-v11"
event_source_id: "ledger:web/src/components/DetailDrawer/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict safeguards"
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

# 📂 **Kansas Frontier Matrix — DetailDrawer Component Overview**  
`web/src/components/DetailDrawer/README.md`

**Purpose:**  
Document the **DetailDrawer component suite**, a core UI pattern used throughout the KFM Web Platform for  
displaying deep, contextual, governance-aware content in a slide-out drawer.  
DetailDrawer acts as an **ethical detail view**, delivering narrative, metadata, provenance, CARE labels,  
and interaction tools without navigating away from the current page.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)]()  
[![WCAG AA+](https://img.shields.io/badge/A11y-WCAG%202.1%20AA%2B-brightgreen)]()

</div>

---

## 📘 Overview

The **DetailDrawer Suite** provides governed, contextual side panels for:

- Dataset and asset detail views (STAC/DCAT)  
- Story Node deep-dive narratives  
- Governance and CARE explanations  
- Focus Mode supplemental detail panes  
- Layer information panels and map-adjacent details  

Key properties:

- Slide-out drawers with reduced-motion aware transitions  
- CARE/sovereignty-aware content masking and warnings  
- Deep metadata and provenance rendering  
- Story Node v3 compatible narrative integration (read-only; no speculation)  
- Keyboard and screen-reader friendly interaction  
- Telemetry-emitting interactions for usage analytics  

DetailDrawer is the primary pattern for **“stay-on-page” rich detail** in the KFM web client.

---

## 🗂️ Directory Structure

Emoji-enhanced v11 layout:

~~~text
web/src/components/DetailDrawer/
│
├── 📂 DetailDrawer.tsx              # Main drawer container (layout, ARIA, focus management)
├── 🏷️ DrawerHeader.tsx             # Title, entity type, CARE label, close button, provenance chip
├── 📄 DrawerSection.tsx            # Reusable styled section block (semantic <section>)
├── 📊 DrawerMetadata.tsx           # Metadata list + masking/redaction indicators
├── 🧬 DrawerProvenance.tsx         # Full PROV-O lineage panel + JSON-LD export
├── ⚠️ DrawerCAREBlock.tsx          # CARE/sovereignty/cultural warnings + explanation
├── 🧭 DrawerFooter.tsx             # Actions, links, dataset tools, Focus Mode launch
└── ♿ DrawerA11yHelpers.tsx        # Screen-reader descriptions, keyboard scaffolding, announcements
~~~

Any new subcomponent MUST be added here and documented in “Component Responsibilities”.

---

## 🧩 Component Responsibilities

### 📂 DetailDrawer.tsx

**Role:**  
Primary container that controls open/close lifecycle, layout, and overall governance behavior.

**Responsibilities:**

- Render slide-out drawer with:
  - Reduced-motion aware transitions  
  - Proper ARIA roles (`role="dialog"` / `aria-modal="true"` or `role="complementary"`)  
- Focus management:
  - Trap focus while open  
  - Return focus to invoking element on close  
- Integrate governance contexts:
  - `GovernanceContext`  
  - `CAREContext`  
  - `A11yContext`  
- Respect `redaction_required` and `indigenous_rights_flag`:
  - Block or generalize content when appropriate  
  - Ensure CAREBlock is shown before any sensitive content  

**Telemetry:**

- `"drawer:open"` — drawer opens  
- `"drawer:close"` — drawer closes  
- `"drawer:section-expand"` — collapsible section expanded/collapsed  

---

### 🏷️ DrawerHeader.tsx

**Role:**  
Topmost header area for the drawer.

**Displays:**

- Entity title (dataset, Story Node, event, etc.)  
- Entity type label (e.g., “Dataset”, “Story Node”, “Event”)  
- CARE badge (classification)  
- Provenance chip (source + last-updated summary)  
- Close button (with keyboard + SR support)

**Accessibility:**

- Uses `<header>` within the drawer context  
- Exposes accessible name for the dialog via `aria-labelledby`  
- Close button must be reachable by keyboard and labeled (e.g., `"Close detail drawer"`)

---

### 📄 DrawerSection.tsx

**Role:**  
Reusable component for drawer content sections.

**Responsibilities:**

- Render a semantic `<section>` with:
  - Section heading (`<h2>` / `<h3>` depending on hierarchy)  
  - Optional descriptive text  
- Maintain proper heading order within the drawer  
- Never inject speculative, unverified text  
- Serve as the container for DataCards, metadata blocks, Story Node excerpts, etc.

---

### 📊 DrawerMetadata.tsx

**Role:**  
Metadata-focused section for the drawer.

**Displays (when available and allowed):**

- Rights-holder  
- License (SPDX)  
- Source archive / system  
- Dataset type & size  
- Temporal extent (with precision and generalization)  
- Spatial extent (generalized when required)  

**Governance:**

- Fields subject to masking or redaction must:
  - Show a redaction indicator (icon + tooltip / SR text)  
  - Avoid showing raw values (e.g., exact coordinates for sacred sites)  
- AI-generated metadata MUST be labeled as such and linked to provenance when present.

---

### 🧬 DrawerProvenance.tsx

**Role:**  
Full provenance and lineage view.

**Responsibilities:**

- Render PROV-O lineage:
  - producers, activities, transformations, agents  
- Present supply-chain artifacts:
  - SBOM reference  
  - manifest reference  
- Provide a **JSON-LD / provenance export** link for inspection  
- Never invent or complete missing lineage—only show factual, recorded links  

**Telemetry:**

- `"drawer:provenance-open"` — fired when provenance panel becomes visible  

---

### ⚠️ DrawerCAREBlock.tsx

**Role:**  
Dedicated block for CARE + sovereignty warnings and explanations.

**Responsibilities:**

- Surface:
  - Sovereignty warnings  
  - Cultural sensitivity disclaimers  
  - Explanation of H3 generalization and masking behavior  
  - CARE classification details  
- MUST be rendered **before any potentially sensitive content** in the drawer  
- Provide clear user understanding of why some data is hidden or generalized  

---

### 🧭 DrawerFooter.tsx

**Role:**  
Bottom action bar for the drawer.

**Common actions:**

- Open detailed dataset view  
- Open in MapView  
- Launch Focus Mode on the entity  
- Download metadata / JSON-LD  
- Open external documentation (if allowed)

**Governance:**

- Actions that would violate CARE or sovereignty rules:
  - MUST be disabled or hidden  
  - MUST include explanatory tooltip or SR-only text  

**Telemetry:**

- `"drawer:action"` — logged with action type (e.g., `"open-focus"`, `"open-map"`)  

---

### ♿ DrawerA11yHelpers.tsx

**Role:**  
Shared A11y utilities used by all drawer components.

**Provides:**

- ARIA roles, labels, and descriptions  
- Focus management utilities  
- Live-region announcements for open/close events  
- Hooks for `prefers-reduced-motion` and other user preferences  

**Requirement:**  
All new behavior in DetailDrawer suite MUST use these helpers, not ad-hoc ARIA logic.

---

## 🔐 Governance & FAIR+CARE Integration

The DetailDrawer Suite is a **governance-critical** UI surface. It MUST:

- Honor:
  - `classification`  
  - `care_label`  
  - `indigenous_rights_flag`  
  - `redaction_required`  
- Present CARE and sovereignty state clearly and early in the drawer  
- Mask / generalize:
  - Spatial data  
  - Temporal precision  
  - Sensitive metadata fields  
- Indicate:
  - When content is masked  
  - When metadata is incomplete or unknown  
- Never:
  - Invent historical claims  
  - Speculate about tribal intentions, lineage, or sacredness  
  - De-anonymize entities or individuals  

Governance test failures must block merges in CI.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA+)

DetailDrawer v11.2.2 MUST:

- Use semantic HTML structure:
  - `<aside>` or `<section>` for container  
  - `<header>` & `<footer>` per drawer  
- Provide:
  - ARIA roles (`role="dialog"`/`"complementary"`)  
  - `aria-modal` when appropriate  
  - `aria-labelledby` linking to the title  
- Maintain proper heading order and labelling  
- Allow keyboard-only control:
  - Open, close, navigate sections  
- Respect `prefers-reduced-motion` with:
  - simplified or disabled transitions when requested  
- Avoid color-only semantics:
  - icons/text used alongside color differences  

Any A11y regression is a **hard CI failure**.

---

## 📈 Telemetry Responsibilities

Telemetry is required for reliability, behavior analysis, and governance monitoring.

Events include:

- `"drawer:open"`  
- `"drawer:close"`  
- `"drawer:section-expand"`  
- `"drawer:provenance-open"`  
- `"drawer:care-warning"`  
- `"drawer:action"`  

**Constraints:**

- No PII or detailed user behavior trails  
- Event payloads MUST follow `telemetry_schema`  
- Must be linked to component version and environment  

---

## 🧪 Testing Requirements

Tests MUST cover:

- **Unit**:
  - Each subcomponent renders with expected props  
  - Governance behavior (masking, redaction) per props  
- **Integration**:
  - Drawer with Story Nodes  
  - Drawer with STAC/DCAT datasets  
  - Drawer in Focus Mode contexts  
- **Accessibility**:
  - Keyboard tab/shift-tab coverage  
  - Focus trap works correctly  
  - ARIA attributes and roles  
- **Governance**:
  - Sensitive datasets → masked fields, warnings shown  
  - Sovereignty flags → coordinates generalization  
- **Telemetry**:
  - All required events emitted with correct shape  

Test locations:

~~~text
tests/unit/web/components/DetailDrawer/**
tests/integration/web/components/DetailDrawer/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                             |
|--------:|------------|-----------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2 standards; governance + A11y v11 |
| v10.4.0 | 2025-11-15 | Full drawer documentation with governance/A11y      |
| v10.3.2 | 2025-11-14 | Added CARE/provenance improvements                  |
| v10.3.1 | 2025-11-13 | Initial DetailDrawer overview                       |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../../../README.md) •  
[Standards Index](../../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · CIDOC-CRM · OWL-Time · STAC/DCAT · PROV-O · WCAG 2.1 AA+ · SLSA Level 3

**End of Document**

</div>