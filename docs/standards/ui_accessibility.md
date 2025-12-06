---
title: "♿ Kansas Frontier Matrix — UI Accessibility & Inclusion Super-Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/ui_accessibility.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual / FAIR+CARE Council & Accessibility Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "releases/v11.2.2/signature.sig"
attestation_ref: "releases/v11.2.2/slsa-attestation.json"
sbom_ref: "releases/v11.2.2/sbom.spdx.json"
manifest_ref: "releases/v11.2.2/manifest.zip"
telemetry_ref: "releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-ui-accessibility-v11.2.2.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "ui-accessibility-superstandard"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "ui-accessibility"
  applies_to:
    - "all-frontend"
    - "all-ui"
    - "docs-rendering"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Sensitivity"
sensitivity: "General (non-PII; normative user-impacting guidance)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Accessibility Board & FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by next major UI accessibility standard"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/standards/ui_accessibility.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "schemas/json/kfm-ui-accessibility-superstandard-v11.2.2.schema.json"
shape_schema_ref: "schemas/shacl/kfm-ui-accessibility-superstandard-v11.2.2-shape.ttl"

story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:docs:standards:ui-accessibility-superstandard:v11.2.2"
semantic_document_id: "kfm-ui-accessibility-superstandard"
event_source_id: "ledger:kfm:doc:standards:ui-accessibility-superstandard:v11.2.2"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "inventing-compliance-status"
  - "overriding-governance-decisions"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - semantic-highlighting
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - inventing-compliance-status
    - overriding-governance-decisions
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# ♿ **Kansas Frontier Matrix — UI Accessibility & Inclusion Super-Standard**  
`docs/standards/ui_accessibility.md`

**Purpose**  
Define the **binding accessibility & inclusion requirements** for all KFM user interfaces (web, maps, 3D, Story Nodes, Focus Mode, explainability views, docs) so that they are usable, understandable, and equitable for the widest possible range of people, in alignment with **WCAG 2.1 AA+**, **FAIR+CARE**, and **MCP-DL v6.3**.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]() ·
[![KFM-MDP v11.2.4](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.4-purple)]() ·
[![Accessibility · WCAG 2.1 AA+](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold)]()

</div>

---

## 📘 Overview

### Scope

This standard applies to *all* KFM user-facing surfaces, including:

- React + MapLibre frontends (`web/`)  
- Focus Mode v3 UI and overlays  
- Story Node v3 narrative/reader experiences  
- Cesium 3D scenes and time-based visualizations  
- Charts and data visualizations (SVG/Canvas/WebGL)  
- API-driven explainability dashboards  
- Rendered documentation (Markdown → HTML)

All of these MUST meet:

- **WCAG 2.1 AA+**  
- **WAI-ARIA** best practices  
- **FAIR+CARE** equity and sovereignty expectations  
- **KFM-MDP** documentation and metadata rules  

### Principles

KFM extends WCAG’s POUR with two KFM-specific principles:

| Principle      | Defined By  | Focus                                             |
|----------------|------------|---------------------------------------------------|
| Perceivable    | WCAG       | Content can be perceived in multiple ways         |
| Operable       | WCAG       | Interfaces can be operated via keyboard/AT        |
| Understandable | WCAG       | Flows are clear, predictable, and consistent      |
| Robust         | WCAG       | Works with current and future AT/tech             |
| Respectful     | KFM/FAIR+CARE | Language and framing respect users’ identities |
| Equitable      | KFM        | Designs support diverse sensory/cognitive realities |

These principles govern all detailed requirements that follow.

---

## 🗂️ Directory Layout

~~~text
📂 KansasFrontierMatrix/
└── 📂 docs/
    ├── 📂 standards/
    │   ├── 📄 README.md                        # Standards index
    │   ├── 📄 ui_accessibility.md              # ♿ UI Accessibility & Inclusion Super-Standard (this file)
    │   ├── 📄 telemetry_standards.md           # 📊 Telemetry & sustainability standard
    │   ├── 📄 licensing.md                     # ⚖ Licensing & SPDX usage
    │   ├── 📄 markdown_rules.md                # 📝 Legacy markdown rules (pre-MDP v11)
    │   ├── 📄 kfm_markdown_protocol_v11.2.4.md # 📑 KFM Markdown Authoring Protocol
    │   ├── 📂 governance/
    │   │   ├── 📄 README.md                    # 🏛️ Governance & Ethical Oversight Framework
    │   │   ├── 📄 ROOT-GOVERNANCE.md           # 🏛️ Root Governance Charter
    │   │   └── 📂 releases/                    # 🏛️ Governance release packets (v10.2.0, v10.2.3, v10.4+)
    │   ├── 📂 faircare/
    │   │   └── 📄 FAIRCARE-GUIDE.md            # ⚖ FAIR+CARE Governance Guide
    │   └── 📂 sovereignty/
    │       └── 📄 INDIGENOUS-DATA-PROTECTION.md# 🪶 Indigenous Data Protection Policy
    ├── 📂 architecture/                        # System + UI architecture docs
    ├── 📂 guides/                              # Developer & operator guides
    ├── 📂 data/                                # Data contracts & schemas
    ├── 📂 analyses/                            # Analyses and case studies
    └── 📄 glossary.md                          # Shared vocabulary
~~~

**Author rules**

- This file is the **canonical root** for UI accessibility and inclusion requirements.  
- Any UI- or component-specific guide MUST link back here and state how it complies or intentionally constrains scope.  
- New accessibility-related standards MUST either:
  - Extend this document (new subsections under existing H2s), or  
  - Live in `docs/standards/` with:
    - `governance_ref: "governance/ROOT-GOVERNANCE.md"`, and  
    - Cross-links from this file under **⚖ FAIR+CARE & Governance**.

---

## 🧭 Context

### Relationship to Other Standards

- **Root Governance & FAIR+CARE**  
  - `governance/ROOT-GOVERNANCE.md` defines who has final authority over accessibility and inclusion.  
  - `faircare/FAIRCARE-GUIDE.md` defines how accessibility intersects with cultural and Indigenous data governance.

- **Markdown & Documentation Standards**  
  - `kfm_markdown_protocol_v11.2.4.md` sets documentation structure.  
  - This UI standard assumes all user-facing documentation is:
    - Properly structured for assistive tech, and  
    - Ready for Focus Mode & Story Node ingestion.

- **Telemetry & Sustainability**  
  - `telemetry_standards.md` explains how a11y metrics are recorded and used.  
  - This document defines which *accessibility signals* MUST be captured.

### A11y as Non-Negotiable Infrastructure

Accessibility is treated as:

- A **hard requirement**, not a best-effort aspiration.  
- A cross-cutting concern across architecture, pipelines, and governance.  
- A domain where governance can explicitly **block releases** that fail critical checks (see CI section).

---

## 🧱 Architecture

> This section encodes the **concrete UI requirements** that designers and engineers must implement.

### Core Accessibility Requirements (All UIs)

#### Keyboard Interaction

All interactive elements MUST:

- Be reachable by `Tab` / `Shift+Tab`.  
- Support activation via `Enter` and/or `Space`.  
- Provide a visible, high-contrast focus ring.

Minimum baseline:

~~~css
:focus-visible {
  outline: 3px solid #2e7dff;
  outline-offset: 3px;
}
~~~

Complex widgets (menus, tablists, sliders, treeviews) MUST implement expected keyboard behavior per WAI-ARIA Authoring Practices (arrow keys, Home/End, etc.).

#### Color, Contrast, and Themes

- Text contrast ratio:
  - ≥ **4.5:1** for normal text.  
  - ≥ **3:1** for large text.  
- Focus indicators and key icons: ≥ **3:1** contrast with surroundings.  
- Both light AND dark themes MUST meet WCAG ratios.  
- State MUST NOT rely on color alone:
  - Use icons, text, or patterns to distinguish error/success/info states.

#### Text, Structure, and Layout

- Use semantic headings in logical order (`h1`–`h4`), matching visual & logical structure.  
- Provide “Skip to main content” or equivalent jump links for major UIs.

Example:

~~~html
<a class="skip-link" href="#main">Skip to main content</a>
<main id="main">
  <!-- main content -->
</main>
~~~

- Avoid huge text blocks; prefer chunked sections and lists for cognitive accessibility.  

#### Semantics and ARIA

- Prefer **native HTML** elements: `<button>`, `<a>`, `<nav>`, `<main>`, `<header>`, `<footer>`, `<section>`, `<article>`.  
- Use ARIA **only** when native semantics are insufficient.  
- Forms MUST associate labels and inputs:

~~~html
<label for="riverName">River name</label>
<input id="riverName" name="riverName" />
<p id="riverError" aria-live="polite"></p>
~~~

- Errors should be announced to assistive tech (e.g., `aria-live`, `role="alert"`).

#### Media, Images, and Icons

- Content images MUST have meaningful `alt` text.  
- Decorative icons/images SHOULD use `alt=""` and/or `aria-hidden="true"`.  
- Video content MUST provide captions (or be explicitly marked as non-essential and documented).  
- Audio-only content MUST provide transcripts.

---

### Maps, Charts, and 3D Scenes

#### MapLibre Maps

Each map instance SHOULD:

- Wrap the map in a labeled region:

~~~html
<section role="region" aria-label="Kansas hydrology map">
  <div id="mapContainer"></div>
  <p>Hydrology layers for Kansas rivers and floodplains. Use + and - keys to zoom; arrow keys to pan.</p>
</section>
~~~

- Provide:
  - Keyboard shortcuts for zoom and pan.  
  - An accessible legend describing layers and symbology.  
  - A short textual summary explaining what the map shows.

#### Data Visualizations (Charts)

For SVG/Canvas charts:

- Provide `<title>` and `<desc>`:

~~~html
<svg aria-labelledby="chartTitle chartDesc">
  <title id="chartTitle">Kansas River Flow Over Time</title>
  <desc id="chartDesc">
    Line chart showing annual flow of the Kansas River from 1900 to 2020,
    with three highlighted drought periods.
  </desc>
  <!-- chart content -->
</svg>
~~~

- Offer a data table view *or* textual summary accessible to non-visual users.  
- Make legend items keyboard-focusable and labeled.

#### Cesium and Other 3D Views

- Respect `prefers-reduced-motion` via CSS or runtime flags:

~~~css
@media (prefers-reduced-motion: reduce) {
  .cesium-viewer {
    animation: none !important;
    transition: none !important;
  }
}
~~~

- Provide:
  - Textual descriptions of key 3D elements.  
  - Keyboard controls for essential interactions (rotate, zoom, pan).  
  - A way to reset the camera to a known orientation.

---

## 🧠 Story Node & Focus Mode Integration

> This section constrains how Story Nodes and Focus Mode UIs must behave to remain accessible.

### Focus Mode v3

- Focus Mode panels MUST be fully keyboard operable.  
- The main narrative area MUST be clearly labeled and structured.

Example dialog:

~~~html
<aside role="dialog" aria-modal="true"
       aria-labelledby="focusTitle"
       aria-describedby="focusBody">
  <h2 id="focusTitle">Fort Larned — Focus View</h2>
  <div id="focusBody">
    <!-- narrative and metadata -->
  </div>
  <button type="button">Previous</button>
  <button type="button">Next</button>
  <button type="button">Close</button>
</aside>
~~~

- Changes in Story Node content SHOULD:
  - Update headings, OR  
  - Announce via an ARIA live region, to avoid silent content changes.

### Story Node Narratives

Story Node rendering MUST:

- Provide clear titles, summaries, and chunked paragraphs.  
- Use alt text and captions for any embedded media.  
- Respect sovereignty by:
  - Using generalized spatial references (e.g., regions vs. exact coordinates) where required by `sovereignty_policy`.  
  - Avoiding exposure of sensitive sites unless explicitly approved.

Focus Mode transforms on this document and related standards MUST be limited to:

- Summaries, semantic highlighting, and a11y-oriented adaptations,  
- NOT content alteration or re-interpretation of compliance status.

---

## 🧪 Validation & CI/CD

> Accessibility is CI-enforced. Failing critical a11y checks MUST block release.

### Automated Checks

Minimum automated checks per release:

- **Page-level audits** (e.g., axe-core, Pa11y, Lighthouse) on:
  - Main landing pages  
  - Map/3D viewers  
  - Focus Mode and Story Node readers  
  - Major dashboards and data-table UIs  

- **Component-level checks** for shared design system components (buttons, menus, dialogs, tabs, etc.).  

These map to `test_profiles`:

- `markdown-lint` – docs structure (including heading order).  
- `accessibility-check` – HTML/a11y checks across core UIs.  
- `diagram-check` – ensures diagrams use accessible text and ARIA where relevant.  

### Manual & Assisted Testing

Each release SHOULD include:

- Screen reader spot-checks (NVDA, JAWS, VoiceOver or equivalent) of:
  - Core navigation flows  
  - At least one complex interaction (map, 3D, or chart).  

- Keyboard-only walkthroughs of:
  - Primary explore → select → focus → exit flows.

Accessibility issues triaged as **critical** MUST block production deployment until resolved or explicitly waived by governance (with ledger entries).

---

## 📦 Data & Metadata

> Accessibility is also **data**: we track audits, issues, and scores as first-class entities.

### Telemetry & A11y Metrics

A11y telemetry SHOULD include, at minimum:

- Number of UI components audited per release  
- Count and severity (critical/major/minor) of open a11y issues  
- Per-surface or per-route a11y scores (e.g., Lighthouse scores)  
- Whether key flows passed keyboard-only and screen-reader checks  

Example telemetry record:

~~~json
{
  "event": "ui_a11y_audit",
  "version": "v11.2.2",
  "components_audited": 142,
  "critical_issues": 0,
  "major_issues": 3,
  "lighthouse_a11y_score": 0.98,
  "timestamp": "2025-11-27T11:00:00Z"
}
~~~

These events are written into:

- `releases/v11.2.2/focus-telemetry.json`  
- Possibly aggregated into `docs/reports/telemetry/ui_a11y_scorecard.json` (implementation-specific).

### Metadata for UI Components

Design system components SHOULD:

- Carry metadata such as:
  - `kfm:a11yProfile` (e.g., `"button.primary.v2"`),  
  - `kfm:requiresKeyboardSupport` (boolean),  
  - `kfm:ariaPattern` (reference to WAI-ARIA pattern used).  

This metadata is helpful for:

- Automated governance checks,  
- Story Node explanations (e.g., “This component is certified accessible as of v11.2.2.”).

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT / STAC

- This standard is modeled as a **documentation dataset** in DCAT with:
  - `dct:title` = title  
  - `dct:identifier` = `semantic_document_id`  
  - `dct:license` = `license`  
  - `dct:modified` = `last_updated`  

- It can appear as a STAC Item in a `kfm-docs` Collection:
  - `id` = `semantic_document_id`  
  - `properties.datetime` = `last_updated`  
  - `assets.markdown` → `docs/standards/ui_accessibility.md`

A11y telemetry and scorecards may be modeled as:

- Associated DCAT distributions,  
- Additional STAC assets, linked via `rel`-like relationships.

### PROV-O

In PROV terms:

- This document is a `prov:Plan` (`prov:Entity`) governing UI accessibility.  
- Each a11y audit is a `prov:Activity` which:
  - `prov:used` UI code and components,  
  - `prov:generated` telemetry and issue lists,  
  - `prov:wasAssociatedWith` specific Agents (Accessibility Board, engineers, auditors).

This allows lineage queries like:

- “Which audits and agents have validated UI accessibility as of v11.2.2?”

---

## ⚖ FAIR+CARE & Governance

### FAIR+CARE Alignment

- **FAIR**
  - Accessibility metadata and telemetry are:
    - Findable via catalogs and dashboards,  
    - Accessible as open JSON/Markdown,  
    - Interoperable with standard vocabularies,  
    - Reusable thanks to clear licensing and provenance.

- **CARE**
  - Respectful language and narratives are required, especially when:
    - Describing communities,  
    - Presenting cultural or historical context.  
  - Designs MUST avoid:
    - Ableist assumptions,  
    - UIs that systematically disadvantage particular user groups.  

### Governance Hooks

- Governance over UI accessibility ultimately flows from:
  - `governance/ROOT-GOVERNANCE.md` (authority).  
  - `faircare/FAIRCARE-GUIDE.md` (ethical framing).  
  - `sovereignty/INDIGENOUS-DATA-PROTECTION.md` (spatial/cultural constraints).

Accessibility-related governance decisions (e.g., waivers, critical issue overrides) MUST be:

- Logged in `reports/audit/governance-ledger.json`.  
- Linked to this standard’s `semantic_document_id` and the release version.

---

## 🕰️ Version History

| Version  | Date       | Author    | Summary                                                                                                                                    |
|---------:|------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-27 | A. Barta  | Upgraded UI Accessibility Super-Standard to align with KFM-MDP v11.2.4; added full governance metadata, heading registry alignment, and explicit STAC/DCAT/PROV and telemetry hooks. |
| v11.0.0  | 2025-11-20 | A. Barta  | Initial v11 UI Accessibility Super-Standard; defined WCAG 2.1 AA+ baseline, MapLibre/Cesium/Chart requirements, and Focus Mode/Story Node a11y constraints. |

---

<div align="center">

♿ **Kansas Frontier Matrix — UI Accessibility & Inclusion Super-Standard (v11.2.2)**  
Accessibility is infrastructure. Inclusion is part of the architecture.

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Aligned · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[📚 Back to Standards Index](README.md) ·  
[🏛️ Root Governance Charter](governance/ROOT-GOVERNANCE.md) ·  
[⚖ FAIR+CARE Guide](faircare/FAIRCARE-GUIDE.md)

</div>
