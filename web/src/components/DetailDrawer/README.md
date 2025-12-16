---
title: "📂 Kansas Frontier Matrix — DetailDrawer Component Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/DetailDrawer/README.md"
version: "v11.2.2"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/web-detaildrawer-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-components-detaildrawer-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public with CARE/sovereignty exceptions"
jurisdiction: "United States / Kansas"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
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
  - "web/src/components/DetailDrawer/README.md@v11.2.2"
  - "web/src/components/DetailDrawer/README.md@v10.4.0"
  - "web/src/components/DetailDrawer/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "WebPageElement"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../schemas/json/web-components-detaildrawer-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-components-detaildrawer-readme-v11-shape.ttl"
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
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "unverified-architectural-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Structure"
    - "🧩 Component Responsibilities"
    - "🔐 Governance & FAIR+CARE Integration"
    - "♿ Accessibility Requirements"
    - "📈 Telemetry Responsibilities"
    - "🧪 Testing Requirements"
    - "🕰 Version History"
    - "⚖️ Footer"
---

<div align="center">

# 📂 **Kansas Frontier Matrix — DetailDrawer Component Overview**
`web/src/components/DetailDrawer/README.md`

**Purpose**
Document the **DetailDrawer component suite**, a core UI pattern used throughout the KFM Web Platform for
displaying deep, contextual, governance-aware content in a slide-out drawer.

DetailDrawer acts as an **ethical detail view**, delivering narrative, metadata, provenance, CARE labels,
and interaction tools without forcing a full-page navigation.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />

</div>

---

## 📘 Overview

DetailDrawer is the primary **stay-on-page** pattern for presenting entity details in the KFM web client
alongside the map, timeline, and search results panels.

It is designed to render **facts and governed metadata** sourced from:
- STAC/DCAT catalogs and API responses (frontend never queries the graph directly)
- Provenance bundles aligned to PROV-O and release manifests
- Governance flags required for CARE and sovereignty compliance

Common entity types shown in DetailDrawer:
- Datasets and assets (STAC Collections / Items, DCAT datasets)
- Story Nodes and Focus Mode context panels
- Map layer metadata and time-filtered layer descriptions
- Governance and provenance explainers

Non-goals:
- Editing or mutating governed records from the public UI
- Reconstructing missing provenance or completing partial lineage
- Generating new historical claims or speculative narrative

### Pipeline position

~~~mermaid
flowchart TD
  A["User interaction<br/>Map · Timeline · Search"] --> B["DetailDrawer opens"]
  B --> C["Fetch detail payload<br/>API + Catalogs"]
  C --> D["Apply governance gating<br/>CARE · Sovereignty · Redaction"]
  D --> E["Render sections<br/>Narrative · Metadata · Provenance · Actions"]
  E --> F["Emit privacy-safe telemetry<br/>Schema validated"]
~~~

### Redaction modes

DetailDrawer MUST support clear, user-comprehensible redaction outcomes:
- **Clear**: data is safe to display at full precision
- **Generalized**: time and space are reduced in precision (for example, grid-based masking)
- **Masked**: sensitive fields are hidden but the record remains discoverable
- **Restricted**: only a high-level summary and governance notice are shown

In all modes, the UI must explain **what changed** and **why**.

---

## 🗂️ Directory Structure

The component suite lives in:

~~~text
📁 web/src/components/DetailDrawer/
├── 📄 README.md                         # This document
├── 📄 DetailDrawer.tsx                  # Drawer container, lifecycle, focus management
├── 📄 DrawerHeader.tsx                  # Title, type label, close control, governance chips
├── 📄 DrawerSection.tsx                 # Section scaffold and consistent semantics
├── 📄 DrawerMetadata.tsx                # Metadata rendering with masking indicators
├── 📄 DrawerProvenance.tsx              # Provenance rendering and export affordances
├── 📄 DrawerCAREBlock.tsx               # CARE and sovereignty notices and explanations
├── 📄 DrawerFooter.tsx                  # Action row and deep links (governance-aware)
└── 📄 DrawerA11yHelpers.tsx             # Shared accessibility helpers and announcements
~~~

If the directory contents differ from this list, update this README to match the folder.
CI linting and human review treat this README as a contract surface for the component suite.

---

## 🧩 Component Responsibilities

This section is written at the **contract level**: it defines what each part of the suite MUST do,
independent of state-management library choices or styling frameworks.

### DetailDrawer container

Responsibilities:
- Provide a stable open/close lifecycle (controlled, deterministic, testable)
- Render as a semantic overlay:
  - `role="dialog"` and `aria-modal="true"` when it behaves as a modal
  - `role="complementary"` when it behaves as a non-modal side panel
- Trap focus while open and restore focus on close
- Respect user motion preferences (reduced motion)
- Avoid layout shift when opening and closing (no surprise page reflow)

Data boundary rules:
- DetailDrawer MUST consume entity details via the Web data access layer (API + catalogs)
- It MUST NOT embed direct knowledge-graph queries in the frontend

Error and loading states:
- Provide a governed loading state (no partial sensitive content during load)
- Provide a not-found state that does not leak internal IDs or access policy

### DrawerHeader

Responsibilities:
- Present entity title and entity type
- Provide a close control with keyboard and screen-reader support
- Surface high-signal governance chips early:
  - CARE label and any redaction indicators
  - provenance freshness indicator when available

Minimum A11y:
- The title MUST be wired to `aria-labelledby` for the dialog
- The close control MUST have a visible label or an accessible name

### DrawerSection

Responsibilities:
- Provide consistent section structure using semantic elements:
  - `<section>` and a correctly ordered heading element
- Support collapsible sections when needed without breaking heading order
- Keep content rendering deterministic:
  - stable keys for lists
  - no random IDs in the markup

### DrawerMetadata

Responsibilities:
- Render metadata that helps users understand:
  - what the entity is
  - where it came from
  - how it may be used (license, rights, attribution)
- Display masking and generalization explicitly:
  - do not show exact coordinates when redaction is required
  - do not show more temporal precision than the governance flags allow

Security requirements:
- Never render untrusted HTML
- Treat all text as data unless explicitly sanitized by a governed sanitizer

### DrawerProvenance

Responsibilities:
- Render provenance and lineage as recorded:
  - do not invent missing links or “fill gaps”
- Provide an export affordance for inspection:
  - JSON-LD when available
  - links to manifest and SBOM references when present

Expected content:
- producer or source references
- transformation steps and validators
- release artifact references (manifest, SBOM) where applicable

### DrawerCAREBlock

Responsibilities:
- Render early and prominently when:
  - indigenous rights are flagged
  - redaction is required
  - CARE classification is above baseline public safety
- Explain why values are masked or generalized
- Provide a user-facing explanation that is:
  - non-technical
  - non-accusatory
  - consistent with FAIR+CARE governance language

### DrawerFooter

Responsibilities:
- Present actions and deep links that remain within governance boundaries
- Disable or hide actions that could violate policy and provide an explanation
- Avoid dark patterns:
  - do not “nudge” users toward restricted actions
  - do not present blocked actions as errors when they are policy outcomes

### DrawerA11yHelpers

Responsibilities:
- Centralize focus-management helpers, live-region announcements, and keyboard patterns
- Provide reusable helpers so the suite does not drift into inconsistent ARIA patterns
- Provide a single place to align with WCAG updates and project-wide A11y conventions

---

## 🔐 Governance & FAIR+CARE Integration

DetailDrawer is a governance-critical UI surface. It MUST implement defense-in-depth:
- The API layer should already enforce redaction and access policy
- The UI MUST still apply governance rules to prevent accidental leakage through rendering, copying,
  telemetry, or edge-case formatting

Required governance behaviors:
- Always show CARE label and redaction status before sensitive fields
- When redaction is required:
  - do not show raw coordinates
  - do not show precise temporal stamps if precision is restricted
  - do not show raw excerpts that include private information without review
- Provide clear notices that distinguish:
  - missing data
  - redacted data
  - restricted data

AI and narrative constraints:
- Any AI-assisted content displayed in the drawer MUST be traceable to governed sources
- The drawer MUST label AI-derived text as AI-derived and link to provenance when provided
- The drawer MUST refuse to display speculative additions or unverified historical claims

---

## ♿ Accessibility Requirements

DetailDrawer MUST meet WCAG 2.1 AA+ expectations and remain operable by keyboard and assistive
technology across supported browsers.

Minimum requirements:
- Keyboard support:
  - open, close, and navigate without a mouse
  - `Escape` closes when modal behavior is in use
- Focus management:
  - focus is trapped within the drawer when modal
  - focus returns to the invoking element on close
- Screen reader support:
  - dialog name and description are announced
  - redaction notices are announced when present
- Motion and animation:
  - transitions respect reduced-motion preferences
- Visual clarity:
  - information is not conveyed by color alone
  - zoom and text scaling do not break layout

Recommended automated checks:
- Lighthouse CI accessibility checks as part of the web validation pipeline
- A11y regression tests for focus trap, keyboard order, and dialog labelling

---

## 📈 Telemetry Responsibilities

DetailDrawer emits telemetry to support reliability, governance auditing, and UX evaluation.

Telemetry MUST be:
- schema-validated against `telemetry_schema`
- privacy-safe: no secrets, no PII, and no exact sensitive coordinates
- governance-aware: include redaction and CARE status as non-sensitive flags

### Required event families

- `drawer:open`
- `drawer:close`
- `drawer:section-toggle`
- `drawer:provenance-view`
- `drawer:care-notice`
- `drawer:action`

### Minimum event shape

~~~json
{
  "event_name": "drawer:open",
  "ts": "2025-12-16T00:00:00Z",
  "component": "DetailDrawer",
  "component_version": "v11.2.2",
  "entity_type": "dataset",
  "entity_id": "kfm:dataset:example-id",
  "care_label": "Public / Medium",
  "redaction_applied": true,
  "result": "ok"
}
~~~

Telemetry must not include:
- free-form user input
- raw excerpts from restricted sources
- user identifiers or stable cross-session tracking identifiers

---

## 🧪 Testing Requirements

Testing must demonstrate that DetailDrawer is:
- correct under normal content
- safe under sensitive content
- accessible under keyboard and assistive technology use
- stable under large metadata payloads

Required test coverage:
- Governance:
  - sensitive entities show CAREBlock before detail fields
  - redacted fields do not render at full precision
- Accessibility:
  - correct roles, labels, and focus behavior
  - keyboard-only navigation for all interactive elements
- Telemetry:
  - events emit on open, close, and actions
  - event payloads validate against the telemetry schema
- Integration:
  - map-click or timeline selection opens the drawer with correct entity context
  - Story Node and Focus Mode contexts render without speculative content

If the web test stack includes browser-driven integration tests, include a scenario that:
- loads a map view
- selects a known entity
- validates that the drawer opens, announces its title, and applies redaction indicators correctly

---

## 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-12-16 | Documentation refresh: corrected relative references; aligned to KFM-MDP v11.2.6; clarified API-only data boundaries, redaction modes, telemetry privacy rules, and A11y expectations. |
| v10.4.0 | 2025-11-15 | Full drawer documentation with governance and accessibility foundations. |
| v10.3.2 | 2025-11-14 | Added CARE and provenance improvements. |

---

## ⚖️ Footer

<div align="center">

**Governance links**
[Docs Root](../../../../README.md) •
[Standards Index](../../../../docs/standards/INDEX.md) •
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) •
[Web Architecture](../../../../web/ARCHITECTURE.md)

**Compliance**
FAIR+CARE · CIDOC-CRM · OWL-Time · STAC/DCAT · PROV-O · WCAG 2.1 AA+ · SLSA-aligned provenance

**End of document**

</div>
