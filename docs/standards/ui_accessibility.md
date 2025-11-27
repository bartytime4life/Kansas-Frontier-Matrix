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
sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-ui-accessibility-v11.2.2.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "ui-accessibility-superstandard"
semantic_document_id: "kfm-ui-accessibility-superstandard"
doc_uuid: "urn:kfm:docs:standards:ui-accessibility-superstandard:v11.2.2"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Sensitivity"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

provenance_chain:
  - "docs/standards/ui_accessibility.md@v11.0.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "inventing-compliance-status"
  - "overriding-governance-decisions"

jurisdiction: "Kansas / United States"
classification: "Public"
lifecycle_stage: "stable"
ttl_policy: "24 months"
sunset_policy: "Superseded by next major UI accessibility standard"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# ♿ **Kansas Frontier Matrix — UI Accessibility & Inclusion Super-Standard**  
`docs/standards/ui_accessibility.md`

**Purpose**  
Define the **binding accessibility & inclusion requirements** for all KFM user interfaces (web, maps, 3D, Story Nodes, Focus Mode, explainability views, docs) so that they are usable, understandable, and equitable for the widest possible range of people, in alignment with WCAG 2.1 AA+, FAIR+CARE, and MCP-DL v6.3.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]() ·
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-purple)]() ·
[![Accessibility · WCAG 2.1 AA+](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold)]()

</div>

---

## 📘 Overview

### Scope

This standard applies to:

- React + MapLibre frontends (`web/`)  
- Focus Mode v3 UI and overlays  
- Story Node v3 narrative/reader experiences  
- Cesium 3D scenes and time-based visualizations  
- Charts and data visualizations (D3/Canvas/SVG)  
- API-driven explainability dashboards  
- Rendered documentation (Markdown → HTML)

All of these MUST meet:

- **WCAG 2.1 AA+**  
- **WAI-ARIA** best practices  
- **FAIR+CARE** equity and sovereignty expectations  
- **KFM-MDP** documentation and metadata rules  

### Principles

KFM extends WCAG’s POUR with two KFM-specific principles:

| Principle        | Defined By | Focus                                |
|------------------|-----------|--------------------------------------|
| Perceivable      | WCAG      | Content can be perceived in multiple ways |
| Operable         | WCAG      | Interfaces can be operated via keyboard/AT |
| Understandable   | WCAG      | Content and flows are clear and predictable |
| Robust           | WCAG      | Works with current and future AT/tech      |
| Respectful       | KFM/FAIR+CARE | Language and framing respect users’ identities |
| Equitable        | KFM       | Designs support diverse sensory/cognitive realities |

These principles guide all detailed requirements that follow.

---

## 🗂️ Directory Layout

UI accessibility is part of the same canonical repository structure as all other KFM standards:

```text
📁 KansasFrontierMatrix/
│
├── 📁 docs/
│   ├── 📁 standards/                        — Governance, ethics, documentation, a11y
│   │   ├── 📄 README.md                     — Standards index
│   │   ├── 📄 faircare.md                   — FAIR+CARE framework
│   │   ├── 📄 data-contracts.md             — Dataset + metadata contracts
│   │   ├── 📄 licensing.md                  — SPDX licensing rules
│   │   ├── 📄 ui_accessibility.md           — ← THIS FILE (UI Accessibility Super-Standard)
│   │   ├── 📄 telemetry_standards.md        — Sustainability & telemetry standard
│   │   ├── 📄 markdown_rules.md             — Markdown structure rules
│   │   ├── 📄 markdown_guide.md             — Authoring guidance
│   │   ├── 📄 kfm_markdown_protocol_v11.md  — Authoring protocol v11
│   │   ├── 📄 kfm_markdown_output_protocol.md — Output rules for generators/AI
│   │   └── 📁 governance/                  — Governance documents
│   │       └── 📄 ROOT-GOVERNANCE.md        — Root governance charter
│   │
│   ├── 📁 architecture/                     — System + UI architecture docs
│   ├── 📁 guides/                           — Developer & operator guides
│   ├── 📁 data/                             — Data-related documentation
│   ├── 📁 analyses/                         — Analyses and case studies
│   └── 📄 glossary.md                       — Shared vocabulary
│
├── 📁 src/
│   ├── 📁 pipelines/                        — ETL + AI pipelines
│   ├── 📁 graph/                            — Neo4j schema and loaders
│   ├── 📁 api/                              — FastAPI, GraphQL
│   └── 📁 tools/                            — Utility code
│
├── 📁 data/
│   ├── 📁 sources/
│   ├── 📁 raw/
│   ├── 📁 work/
│   ├── 📁 processed/
│   └── 📁 stac/
│
├── 📁 schemas/
│   ├── 📁 json/
│   └── 📁 telemetry/
│
├── 📁 mcp/
│   ├── 📁 experiments/
│   ├── 📁 model_cards/
│   └── 📁 sops/
│
├── 📁 tests/
├── 📁 tools/
└── 📁 .github/
    └── 📁 workflows/
```

---

## 🧱 Core Accessibility Requirements

### Keyboard Interaction

All interactive elements across KFM UIs:

- Are reachable by `Tab` and `Shift+Tab`.  
- Support activation via `Enter` and/or `Space`.  
- Provide visible, high-contrast focus rings.  

Minimum focus style:

```css
:focus-visible {
  outline: 3px solid #2e7dff;
  outline-offset: 3px;
}
```

Composite components (menus, sliders, tablists, treeviews) MUST implement expected keyboard patterns (arrow keys, Home/End, Page Up/Page Down where appropriate).

---

### Color, Contrast, and Theme Support

- Text contrast ratio: ≥ **4.5:1** (normal) and ≥ **3:1** (large text).  
- Focus indicators and key icons: ≥ **3:1** against adjacent colors.  
- Both light and dark themes MUST satisfy WCAG contrast ratios.  
- State (e.g. error vs success vs neutral) MUST have at least one non-color cue (icon shape, text label, or pattern).

---

### Text, Structure, and Layout

- Use headings (`<h1>`–`<h4>`) in logical hierarchy, matching document and page structure.  
- Use lists and tables where appropriate for structured content.  
- Keep paragraph lengths reasonable; prefer chunked, scannable blocks for complex content.  
- Provide a “Skip to main content” link in major UIs.  

Example:

```html
<a class="skip-link" href="#main">Skip to main content</a>
<main id="main">
  <!-- content -->
</main>
```

---

### Semantics and ARIA

- Use **native HTML elements** for semantics: `<button>`, `<a>`, `<nav>`, `<main>`, `<header>`, `<footer>`, `<section>`, `<article>`.  
- Use ARIA roles when no suitable native element exists, and ensure labels/relationships are correctly wired (`aria-label`, `aria-labelledby`, `aria-describedby`).  
- Forms MUST:
  - Associate `<label for="id">` with `<input id="id">`.  
  - Identify errors programmatically.  

Example:

```html
<label for="riverName">River name</label>
<input id="riverName" name="riverName" />
<p id="riverError" aria-live="polite"></p>
```

---

### Media, Images, and Icons

- Content images MUST have meaningful `alt` text.  
- Decorative images/icons SHOULD use empty `alt=""` or `aria-hidden="true"`.  
- Video content MUST provide captions or transcripts.  
- Audio-only content MUST provide transcripts.  

---

## 🗺️ Maps, Charts, and 3D Scenes

### MapLibre Maps

Each map component SHOULD:

- Expose a region container with `role="region"` and `aria-label` describing purpose.  
- Provide keyboard shortcuts for zoom (e.g. `+` and `-`) and panning (arrow keys).  
- Include an accessible legend that explains layers and symbology in text.  
- Offer a textual summary of what the map shows (e.g. “This map shows flood risk levels across Kansas counties over time.”).

Example:

```html
<section role="region" aria-label="Kansas hydrology map">
  <div id="mapContainer"></div>
  <p>Hydrology layers for Kansas rivers and floodplains. Use + and - keys to zoom; arrow keys to pan.</p>
</section>
```

---

### Data Visualizations (Charts)

For charts rendered via SVG/Canvas:

- Provide `<title>` and `<desc>` for SVG charts, linked via `aria-labelledby`.  
- Offer a data table view or textual summary for non-visual access.  
- Ensure legend items are keyboard-focusable and labeled.  

Example:

```html
<svg aria-labelledby="chartTitle chartDesc">
  <title id="chartTitle">Kansas River Flow Over Time</title>
  <desc id="chartDesc">
    Line chart showing annual flow of the Kansas River from 1900 to 2020, with three highlighted drought periods.
  </desc>
</svg>
```

---

### Cesium and 3D Views

- Respect `prefers-reduced-motion` to limit camera fly-throughs and animations.  
- Provide a textual summary of the 3D scene, explaining the key features.  
- Provide keyboard alternatives for rotation/zoom/panning of essential interactions.  

Example reduced-motion snippet:

```css
@media (prefers-reduced-motion: reduce) {
  .cesium-viewer {
    animation: none !important;
    transition: none !important;
  }
}
```

---

## 🧠 Focus Mode & Story Nodes

### Focus Mode v3

- Focus Mode panels MUST be reachable and usable entirely via keyboard.  
- The primary content area MUST have a clear region label and title.  
- Announce Story Node changes via ARIA live regions or updated headings.  

Example dialog container:

```html
<aside role="dialog" aria-modal="true" aria-labelledby="focusTitle" aria-describedby="focusBody">
  <h2 id="focusTitle">Fort Larned — Focus View</h2>
  <div id="focusBody">
    <!-- narrative and metadata -->
  </div>
  <button>Previous</button>
  <button>Next</button>
  <button>Close</button>
</aside>
```

### Story Node Narratives

Story Node implementations MUST:

- Provide clear titles and summaries.  
- Expose structured content blocks that can be read in order.  
- Include alt text and captions for referenced media.  
- Respect sovereignty constraints by using generalized spatial references (e.g. regions rather than exact coordinates) when required.

---

## 🧪 Testing & CI for Accessibility

Accessibility is included in CI/CD as a first-class check.

Minimum tests per release:

- Automated checks (e.g. axe-core, Pa11y, Lighthouse) on key pages and flows:
  - Main map viewer  
  - Focus Mode  
  - Story Node reader  
  - Data tables and chart dashboards  
- Screen reader spot-checks (NVDA, VoiceOver, or equivalent) on:
  - Landing pages  
  - Primary interaction flows (search → select → focus → exit)  

Basic CI pipeline expectations:

- `a11y_html_check`: runs on compiled static HTML  
- `a11y_component_check`: runs on Storybook or component library  
- `docs_a11y_check`: ensures alt attributes on images in docs and correct heading structure  

Accessibility failures classified as critical MUST block production deployment.

---

## 📦 Telemetry for Accessibility & Inclusion

UX and accessibility telemetry SHOULD track:

- Number of components audited per release  
- Automated a11y scores (e.g. from Lighthouse)  
- Count and severity of unresolved a11y issues  
- Screen reader usage indicators (where privacy allows)  
- Focus Mode and Story Node a11y scores  

Example telemetry entry:

```json
{
  "event": "ui_a11y_audit",
  "version": "v11.2.2",
  "components_audited": 142,
  "critical_issues": 0,
  "major_issues": 3,
  "lighthouse_a11y_score": 0.98,
  "timestamp": "2025-11-27T11:00:00Z"
}
```

---

## 🕰️ Version History

| Version  | Date       | Summary                                                                                                         |
|---------:|------------|-----------------------------------------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-27 | Upgraded to v11.2.2; aligned directory layout with project-wide pattern; tightened Focus Mode & Story Node rules; added telemetry guidance. |
| v11.0.0  | 2025-11-20 | Initial v11 UI Accessibility Super-Standard; WCAG 2.1 AA+, MapLibre/Cesium/D3 coverage, FAIR+CARE hooks.      |

---

<div align="center">

♿ **Kansas Frontier Matrix — UI Accessibility & Inclusion Super-Standard (v11.2.2)**  
Accessibility is infrastructure. Inclusion is part of the architecture.

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Aligned · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Standards Index](README.md) ·  
[⚖ Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
