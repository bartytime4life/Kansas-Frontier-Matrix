---
title: "🗃️ Kansas Frontier Matrix — DataCards Component Suite Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/components/DataCards/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-components-datacards-v1.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Component Overview"
intent: "web-components-datacards"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Dataset-dependent"
sensitivity_level: "Variable"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/components/DataCards/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../../schemas/json/web-components-datacards-readme.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-datacards-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-components-datacards-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-components-datacards-readme"
event_source_id: "ledger:web/src/components/DataCards/README.md"
immutability_status: "version-pinned"
ai_training_inclusion: false

ai_focusmode_usage: "Allowed with strict guardrails"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "unverified historical claims"
  - "speculative dataset descriptions"
  - "hallucinated metadata"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public / Dataset-Sensitive"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Review every 12 months"
sunset_policy: "Superseded upon next data-card system upgrade"
---

<div align="center">

# 🗃️ **Kansas Frontier Matrix — DataCards Component Suite Overview**  
`web/src/components/DataCards/README.md`

**Purpose:**  
Document the entire **DataCards UI component suite**, used across the Kansas Frontier Matrix Web Platform  
for presenting FAIR+CARE-governed dataset summaries, metadata, governance labels, spatial previews,  
temporal indicators, and provenance in compact, reusable card layouts.

DataCards power dataset browsing (STAC/DCAT), Story Node asset previews, and Focus Mode supplemental datasets.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v10.4](https://img.shields.io/badge/KFM%E2%80%93MDP-v10.4-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()  
[![WCAG AA](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-brightgreen)]()

</div>

---

## 📘 Overview

The DataCards Component Suite provides a **standardized, governance-aware card UI** for:

- Datasets (STAC/DCAT)
- Assets and document bundles
- Story Node-linked resources
- Focus Mode supplemental datasets

Key properties:

- WCAG 2.1 AA–compliant visual design and behavior  
- CARE-aware metadata presentation (masking, generalization, notices)  
- Provenance chips for source and processing lineage  
- Spatial and temporal mini-previews (when allowed by governance)  
- Deterministic rendering (no random layout or behavior)  
- Strict schema-validated props (JSON Schema + TS types)  
- No speculative, inferred, or fabricated metadata  

DataCards appear in:

- STAC/DCAT dataset lists  
- Story Node asset panels  
- Focus Mode related-datasets sidebars  
- DetailDrawer subviews  
- Map-adjacent resource listings and dataset pickers  

---

## 🧱 Directory Structure

Emoji-enhanced, component-level layout:

~~~text
web/src/components/DataCards/
│
├── 🗃️ DataCard.tsx                   # Universal dataset/narrative card container
├── 🏷️ DataCardHeader.tsx             # Title, dataset type, CARE badge, provenance chip
├── 🧾 DataCardMetadata.tsx           # Publisher, license, temporal, spatial, classification fields
├── 🗺️ DataCardPreview.tsx            # Spatial/temporal mini-map and interval previews
├── 🦶 DataCardFooter.tsx             # Actions: open, explore, open in map, provenance
├── ♿ DataCardA11yHelpers.tsx        # ARIA, keyboard scaffolding, a11y helpers
└── 🧱 DataCardSkeleton.tsx           # Loading skeleton (reduced-motion safe, non-revealing)
~~~

---

## 🧩 Component Responsibilities

### 🗃️ DataCard.tsx

**Role:**  
Main container that assembles all DataCard subcomponents into a coherent, governed card.

**Responsibilities:**

- Compose `DataCardHeader`, `DataCardMetadata`, `DataCardPreview`, `DataCardFooter`  
- Enforce **governance and CARE filters**:
  - Hide or mask content when `redaction_required` is true
  - Show generalization/masking notices when spatial/temporal details are blurred
  - Respect sovereignty constraints surfaced from metadata  
- Manage layout, spacing, and tokens in line with design system
- Ensure **keyboard focus** order and region semantics (e.g., `<article>` or `<section>` usage)
- Wire telemetry event hooks for interactions

**Telemetry Events:**

- `"datacard:open"` — card opened or expanded  
- `"datacard:hover"` — hover or focus events (non-PII aggregates only)  
- `"datacard:action"` — any explicit action (e.g., open in map, open detail drawer)  

---

### 🏷️ DataCardHeader.tsx

**Role:**  
Top-of-card visual identity and governance labeling.

**Displays:**

- Dataset / asset title  
- Dataset type or category (e.g., STAC collection, STAC item, Story Node asset)  
- CARE badge (e.g., Public, Dataset-sensitive, Sovereignty-controlled)  
- Provenance chip (summary of source, last updated, pipeline name)

**Accessibility:**

- Uses a semantic `<header>` within the card context  
- Clear, descriptive text for screen readers (no icon-only communication)  
- Color usage must **not** be the only carrier of meaning  

---

### 🧾 DataCardMetadata.tsx

**Role:**  
Structured metadata presentation.

**Displays (when available and allowed):**

- Publisher  
- Rights-holder  
- License (SPDX where possible)  
- Temporal extent (start/end; generalized if required)  
- Spatial extent (bbox, region, or generalized location)  
- Data type / format / size  
- Classification (Public, Dataset-sensitive, Sovereignty-controlled)

**Governance:**

- Any sensitive field must:
  - show a redaction or generalization indicator  
  - provide a tooltip or hint explaining why certain details are hidden  
- Must NOT display high-precision coordinates for sovereignty-controlled datasets  

---

### 🗺️ DataCardPreview.tsx

**Role:**  
Optional mini **spatial/temporal preview** of the dataset.

**Features:**

- Mini-map footprint:
  - H3-based generalization (e.g., r7+ cells)  
  - Coarse polygons only for sensitive layers  
- Temporal preview bar:
  - e.g., small bar showing coverage interval on a timeline axis  
- Simple coverage thumbnail imagery (non-sensitive)

**Governance:**

- MUST generalize coordinates for sensitive or sovereignty-controlled datasets  
- MUST refrain from drawing precise boundaries when `redaction_required` is true  
- MUST display clear text notice when preview is generalized or disabled  

**Accessibility:**

- Provide textual equivalents:
  - ARIA descriptions for the map footprint  
  - Text labels for temporal extent and coverage  

---

### 🦶 DataCardFooter.tsx

**Role:**  
Action bar for interacting with the dataset.

**Common actions:**

- Open dataset detail view (DetailDrawer / dedicated route)  
- Open dataset in MapView  
- View provenance details  
- Open in external data portal (if allowed)

**Governance:**

- Disable or hide actions that would violate sovereignty / CARE constraints  
- Provide tooltips or helper text explaining restricted actions  

**Telemetry:**

- `"datacard:action"` emitted with action type (e.g., `"open"`, `"open-map"`, `"view-provenance"`)  

---

### ♿ DataCardA11yHelpers.tsx

**Role:**  
Centralized accessibility utilities for all DataCard variants.

**Provides:**

- ARIA attributes & roles for:
  - Card containers  
  - Action buttons  
  - Preview regions  
- Keyboard navigation scaffolding:
  - Tab-order decisions  
  - Skip links where relevant  
- Reduced-motion behavior:
  - Respect `prefers-reduced-motion`  
  - Disable or simplify animations

**Requirements:**

- All DataCard variants must use these helpers to maintain WCAG 2.1 AA compliance  
- New subcomponents should not re-implement ARIA logic ad hoc  

---

### 🧱 DataCardSkeleton.tsx

**Role:**  
Loading state that preserves layout without revealing sensitive content.

**Behavior:**

- Provides a shimmer or placeholder layout that respects reduced-motion settings  
- Displays only generic shapes and lines, with no text from actual data  
- Does **not** leak any raw field values, bounding boxes, or sensitive hints  

---

## 🔐 Governance & FAIR+CARE Integration

DataCards are a **governance-critical** UI element. They MUST:

- Respect:
  - `classification`  
  - `care_label`  
  - `indigenous_rights_flag`  
  - `redaction_required`  
- Mask or generalize:
  - spatial extents for sensitive/sovereignty-controlled datasets  
  - temporal details if revealing them could be harmful  
- Prevent:
  - display of high-precision geometries for protected sites  
  - display of raw metadata for embargoed datasets  

**No speculation**:

- Never infer missing metadata values  
- Never fabricate dataset history or purpose  
- Flag any AI-generated descriptions as such and link to sources  

Governance violations (e.g., leaking a precise sacred site location) are considered **blocking CI failures** for this component.

---

## ♿ Accessibility Requirements (WCAG 2.1 AA)

DataCards MUST:

- Use semantic HTML:
  - `<article>`/`<section>` with meaningful headings  
  - `<header>`/`<footer>` for card segments  
- Provide ARIA roles & labels:
  - For card containers, previews, and action buttons  
- Maintain contrast:
  - Text vs. background ≥ 4.5:1  
- Support keyboard-only use:
  - Full interaction via Tab/Shift+Tab/Enter/Space  
- Respect user preferences:
  - `prefers-reduced-motion`  
  - High contrast mode  

Any A11y regression in tests must block merges.

---

## 📈 Telemetry Responsibilities

DataCards emit non-PII telemetry for behavioral insight and reliability monitoring.

Core events:

- `"datacard:open"`  
- `"datacard:hover"`  
- `"datacard:action"`  
- `"datacard:care-warning"` (when a governance/CARE warning is shown)  
- `"datacard:provenance-expand"`  

Telemetry must be:

- Aggregated, non-identifying  
- Schema-validated  
- Linked to the component version (for rollbacks and analysis)  
- Included in release telemetry bundles referenced by `telemetry_ref`  

---

## 🧪 Testing Requirements

Testing scope:

- **Unit tests**:
  - Rendering for all component variants  
  - Behavior with different governance flags (`redaction_required`, `indigenous_rights_flag`)  
  - Correct field rendering for typical dataset metadata  

- **Integration tests**:
  - DataCards in STAC/DCAT lists  
  - DataCards in Focus Mode panels  
  - DataCards in Story Node asset lists  

- **Governance tests**:
  - Sensitive dataset → no precise coordinates drawn  
  - Redacted fields show masking indicators  

- **Accessibility tests**:
  - Keyboard navigation (tab order, focus states)  
  - ARIA roles and labels present  
  - No color-only semantics  

- **Telemetry tests**:
  - Events emitted with expected names and payload shapes  

Test file placement:

~~~text
tests/unit/web/components/DataCards/**
tests/integration/web/components/DataCards/**
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                              |
|--------:|------------|----------------------------------------------------------------------|
| v10.4.0 | 2025-11-15 | Full DataCards suite documentation; governance + A11y + telemetry   |
| v10.3.2 | 2025-11-14 | Improved metadata + CARE disclosure patterns                        |
| v10.3.1 | 2025-11-13 | Initial DataCards component overview                                |

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Repo Docs Root](../../../../../README.md) •  
[Standards Index](../../../../../docs/standards/INDEX.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · WCAG 2.1 AA · STAC/DCAT-ready · CIDOC-CRM aligned · PROV-O lineage

**End of Document**

</div>