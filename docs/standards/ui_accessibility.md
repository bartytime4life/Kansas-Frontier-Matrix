---
title: "♿ Kansas Frontier Matrix — UI Accessibility & Inclusion Super-Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/ui_accessibility.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Accessibility Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-ui-accessibility-v11.2.6.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
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
    - "map-2d"
    - "map-3d"
    - "data-visualization"
    - "story-nodes"
    - "focus-mode"

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
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/standards/ui_accessibility.md@v11.2.2"
  - "docs/standards/ui_accessibility.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../schemas/json/kfm-ui-accessibility-superstandard-v11.2.6.schema.json"
shape_schema_ref: "../../schemas/shacl/kfm-ui-accessibility-superstandard-v11.2.6-shape.ttl"

story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:docs:standards:ui-accessibility-superstandard:v11.2.6"
semantic_document_id: "kfm-ui-accessibility-superstandard"
event_source_id: "ledger:kfm:doc:standards:ui-accessibility-superstandard:v11.2.6"
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
    - "summary"
    - "semantic-highlighting"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "inventing-compliance-status"
    - "overriding-governance-decisions"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

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
Define the **binding accessibility & inclusion requirements** for all KFM user interfaces (web, maps, 3D, Story Nodes, Focus Mode, explainability views, documentation rendering) so they are usable, understandable, and equitable for the widest possible range of people—aligned with **WCAG 2.1 AA+**, **FAIR+CARE**, and **MCP‑DL v6.3**.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA%2B-2b6cb0" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

### Scope

This standard applies to **all KFM user-facing surfaces**, including:

- React + MapLibre frontends
- Focus Mode panels, drawers, overlays, and readers
- Story Node rendering (Markdown → UI)
- Cesium (or other) 3D scenes and time-based visualizations
- Charts and data visualization layers (SVG / Canvas / WebGL)
- Explainability dashboards and model health views
- Rendered documentation (Markdown → HTML)

All covered surfaces MUST meet:

- **WCAG 2.1 AA+** (KFM baseline)
- **WAI-ARIA** authoring practices (when custom widgets are required)
- **FAIR+CARE** framing and equity expectations
- **Sovereignty policy constraints** for sensitive and Indigenous-related content

### Principles

KFM uses WCAG’s POUR principles and extends them with two KFM principles:

| Principle      | Defined By     | What it means in KFM |
|----------------|----------------|----------------------|
| Perceivable    | WCAG           | Multiple modalities (visual, text, captions, summaries) |
| Operable       | WCAG           | Keyboard + assistive tech control without traps |
| Understandable | WCAG           | Predictable UI, consistent affordances, clear language |
| Robust         | WCAG           | Works across AT, browsers, and future tech changes |
| Respectful     | KFM / FAIR+CARE | Language and presentation respects identity and dignity |
| Equitable      | KFM            | Design supports diverse sensory, cognitive, and motor realities |

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 standards/
    ├── 📄 README.md                                — Standards index
    ├── 📄 ui_accessibility.md                      — ← This standard (UI accessibility & inclusion)
    ├── 📄 kfm_markdown_protocol_v11.2.6.md         — KFM Markdown Protocol (docs → UI rendering assumptions)
    ├── 📁 governance/
    │   └── 📄 ROOT-GOVERNANCE.md                   — Governance charter (authority + enforcement)
    ├── 📁 faircare/
    │   └── 📄 FAIRCARE-GUIDE.md                    — FAIR+CARE guide (ethics + equity)
    └── 📁 sovereignty/
        └── 📄 INDIGENOUS-DATA-PROTECTION.md        — Sovereignty & Indigenous data protection

📁 .github/
└── 📁 workflows/
    ├── 📄 kfm-ci.yml                               — Primary CI orchestration (gates)
    ├── 📄 docs-lint.yml                            — Docs structure + link checks
    └── 📄 faircare-validate.yml                    — FAIR+CARE governance validation (docs + data)

📁 reports/
└── 📁 self-validation/
    └── 📁 a11y/
        ├── 📄 a11y_summary.json                    — Machine-readable a11y results (per run)
        └── 📄 summary.md                           — Human-readable a11y summary (PR-friendly)

📁 tools/
└── 📁 a11y/
    ├── 📄 run_axe_audit.mjs                        — Browser-based a11y audit runner (example)
    ├── 📄 run_lighthouse_a11y.mjs                  — Lighthouse a11y runner (example)
    └── 📄 normalize_a11y_results.mjs               — Normalization + gating utilities

📁 src/
├── 📁 web/                                         — UI application surfaces (React, Focus Mode, Story Nodes)
└── 📁 ui/                                          — Shared components + accessibility patterns
~~~

**Author rules (normative)**

- UI/component-specific guidance MUST link back to this standard.
- Any “exception” to these requirements MUST be documented and governed (see **⚖ FAIR+CARE & Governance**).
- Accessibility work MUST be treated as release-blocking infrastructure, not “polish.”

---

## 🧭 Context

### Accessibility as governed infrastructure

KFM treats accessibility as:

- a **non-negotiable quality gate**,
- a **public trust requirement** (especially for civic and historical interfaces),
- a **governance surface** (decisions are logged, reviewed, and auditable).

### Relationship to other standards

- **Governance authority:** `governance/ROOT-GOVERNANCE.md`
- **Ethical framing & equity:** `faircare/FAIRCARE-GUIDE.md`
- **Sovereignty restrictions:** `sovereignty/INDIGENOUS-DATA-PROTECTION.md`
- **Docs/Story Node structure:** `kfm_markdown_protocol_v11.2.6.md`

---

## 🗺️ Diagrams

### Accessibility gate in the CI/CD pipeline

~~~mermaid
flowchart LR
  A["PR / Push"] --> B["Build UI + render docs"]
  B --> C["A11y checks: axe / pa11y / Lighthouse"]
  C --> D{"Pass policy?"}
  D -->|Yes| E["Upload reports + emit telemetry"]
  D -->|No| F["Block merge / release"]
  E --> G["Governance ledger + dashboards"]
~~~

---

## 🧱 Architecture

### 1. Baseline requirements for all UIs

#### Keyboard interaction (MUST)

All interactive elements MUST:

- be reachable via `Tab` / `Shift+Tab`,
- support activation via `Enter` and/or `Space` (as appropriate),
- provide a visible focus indicator (not removed),
- avoid keyboard traps (user must always be able to escape).

Minimum focus-ring pattern (example):

~~~css
:focus-visible {
  outline: 3px solid var(--kfm-focus-ring-color);
  outline-offset: 3px;
}
~~~

Constraint: `--kfm-focus-ring-color` MUST meet ≥ 3:1 contrast against adjacent colors.

#### Color, contrast, and themes (MUST)

- Text contrast ratio MUST be:
  - ≥ **4.5:1** for normal text,
  - ≥ **3:1** for large text.
- Focus indicators and key icons MUST be ≥ **3:1**.
- Light and dark themes MUST both pass.
- State MUST NOT rely on color alone:
  - add icons, patterns, labels, or text.

#### Text scaling and reflow (MUST)

- UI MUST remain usable at **200% zoom** without horizontal scrolling for primary content flows.
- Layout MUST support responsive reflow:
  - content should wrap,
  - controls should remain reachable,
  - dialogs should remain operable without hidden close controls.

#### Semantics and ARIA (MUST)

- Prefer native HTML semantics (`button`, `a`, `nav`, `main`, `header`, `footer`, `section`, `article`).
- Use ARIA only when native semantics are insufficient.
- All inputs MUST have accessible names (label, `aria-label`, or `aria-labelledby`).

Example:

~~~html
<label for="riverName">River name</label>
<input id="riverName" name="riverName" autocomplete="off" />
<p id="riverError" aria-live="polite"></p>
~~~

#### Errors, validation, and status (MUST)

- Errors MUST be:
  - visually visible,
  - announced to assistive tech (e.g., `aria-live` or `role="alert"`),
  - tied to the relevant field when possible (`aria-describedby`).
- Avoid “only red border” validation states.

---

### 2. Maps, charts, and 3D scenes

#### Map UIs (MapLibre, etc.) (MUST)

Each map experience MUST provide:

- an accessible label for the map region,
- keyboard interaction for essential actions (pan/zoom or alternatives),
- an accessible legend and layer list,
- a non-visual summary of what the map conveys.

Example wrapper:

~~~html
<section role="region" aria-label="Kansas hydrology map">
  <div id="mapContainer"></div>
  <p id="mapHelp">
    Hydrology layers for Kansas rivers and floodplains. Use keyboard controls to navigate or use the data table below.
  </p>
</section>
~~~

If full keyboard panning is not feasible, the UI MUST provide an equivalent non-map pathway (table, filters, search, list).

#### Charts and visualizations (SVG/Canvas/WebGL) (MUST)

For charts, the UI MUST provide:

- a clear title and description accessible to AT,
- a text summary and/or tabular view,
- keyboard-accessible legend toggles and key controls.

Example:

~~~html
<svg aria-labelledby="chartTitle chartDesc" role="img">
  <title id="chartTitle">Kansas River flow over time</title>
  <desc id="chartDesc">
    Line chart showing annual flow from 1900 to 2020, with drought periods highlighted.
  </desc>
</svg>
~~~

#### 3D scenes (Cesium, etc.) (MUST)

- Respect motion preferences (`prefers-reduced-motion`) where possible.
- Provide:
  - a way to reset view (camera home),
  - keyboard access for essential actions,
  - non-visual summaries of key scene meaning and state.

---

### 3. Language, inclusivity, and cognitive accessibility

#### Plain language (SHOULD)

- Prefer clear, plain language for UI copy.
- Avoid jargon unless it is defined (tooltips, glossary links, “learn more”).

#### Respectful framing (MUST)

- Avoid ableist language and assumptions.
- When presenting historical content, ensure framing respects affected communities and aligns with governance notes.

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode UI (MUST)

- Focus Mode containers MUST be keyboard operable end-to-end.
- Content changes MUST be perceivable:
  - update headings, and/or
  - announce significant changes via a live region.

Example dialog skeleton:

~~~html
<aside role="dialog" aria-modal="true"
       aria-labelledby="focusTitle"
       aria-describedby="focusBody">
  <h2 id="focusTitle">Focus View</h2>
  <div id="focusBody">
    <!-- narrative and metadata -->
  </div>
  <button type="button">Previous</button>
  <button type="button">Next</button>
  <button type="button">Close</button>
</aside>
~~~

### Story Node rendering (MUST)

Story Node content MUST render with:

- semantic headings and lists,
- alt text for content images and diagrams,
- captions/transcripts for media where applicable.

Sovereignty constraints MUST be enforced in the UI:

- sensitive coordinates and site details MUST be generalized or withheld according to policy,
- the UI MUST present “why” (governance-safe explanation) when redaction occurs.

---

## 🧪 Validation & CI/CD

### 1. Automated checks (MUST)

A release (or protected-branch merge) MUST include automated a11y checks for:

- primary navigation surfaces,
- Story Node reader surfaces,
- Focus Mode surfaces,
- at least one map or 3D surface when present.

Recommended automation types:

- Browser-based audits (axe-core / pa11y)
- Lighthouse accessibility scoring (where stable)
- Component linting (`eslint-plugin-jsx-a11y` or equivalent)

### 2. Manual checks (SHOULD)

At minimum per release candidate:

- keyboard-only walkthrough of core flows,
- screen reader spot-check of at least one complex flow (map, chart, or Focus Mode).

### 3. Gating policy (normative)

The pipeline MUST fail if:

- critical accessibility errors are detected (as defined by the a11y policy config),
- required reports are missing,
- telemetry emission fails (no evidence = not shippable).

Any temporary waiver MUST:

- be explicitly approved via governance,
- be time-bounded,
- include mitigation notes and a remediation plan.

---

## 📦 Data & Metadata

### Reports (recommended)

Per CI run, emit:

- `reports/self-validation/a11y/a11y_summary.json`
- `reports/self-validation/a11y/summary.md`

Suggested JSON fields (schematic):

~~~json
{
  "workflow": "accessibility-check",
  "run_id": "<run-id>",
  "routes_scanned": 0,
  "critical": 0,
  "major": 0,
  "minor": 0,
  "lighthouse_a11y_score": null,
  "timestamp": "<utc-iso8601>",
  "commit_sha": "<git-sha>"
}
~~~

### Telemetry (recommended)

A11y-related telemetry events SHOULD be appended into:

- `../../releases/v11.2.6/focus-telemetry.json`

Minimum signals:

- severity counts (critical/major/minor),
- routes/components scanned,
- pass/fail,
- runtime, energy, carbon (when available).

---

## 🌐 STAC, DCAT & PROV Alignment

- **DCAT**
  - This standard is a documentation dataset; audit results are distributions (JSON/MD reports).
- **STAC**
  - Optionally represent audit runs as non-spatial items in a `kfm-ci` collection (`geometry: null`).
- **PROV-O**
  - This document is a `prov:Plan`.
  - Each audit run is a `prov:Activity` that:
    - `prov:used` UI code + config + target routes,
    - `prov:generated` reports and telemetry,
    - `prov:wasAssociatedWith` runner + maintainers (as agents).

---

## ⚖ FAIR+CARE & Governance

### FAIR

- Findable: stable IDs + predictable paths
- Accessible: reports and standards are discoverable in docs and telemetry
- Interoperable: JSON summaries + PROV/DCAT mappings
- Reusable: versioned standard + governance evidence trail

### CARE

- Collective benefit: the UI must not exclude users by default design choices
- Authority to control: sovereignty constraints are respected in display and disclosure
- Responsibility: accessibility failures block releases; waivers are governed
- Ethics: respectful framing, no exploitative or demeaning presentation

### Governance hooks (normative)

- Governance authority: `governance/ROOT-GOVERNANCE.md`
- Ethical framing: `faircare/FAIRCARE-GUIDE.md`
- Sovereignty constraints: `sovereignty/INDIGENOUS-DATA-PROTECTION.md`

---

## 🕰️ Version History

| Version  | Date       | Author        | Summary |
|---------:|------------|---------------|---------|
| v11.2.6  | 2025-12-12 | `@kfm-a11y`   | Updated to KFM‑MDP v11.2.6 formatting; corrected repo-relative references; standardized directory layout tree; added CI gating diagram; expanded Focus Mode/Story Node constraints and telemetry/report expectations. |
| v11.2.2  | 2025-11-27 | `@kfm-a11y`   | Established governed UI Accessibility Super-Standard with WCAG 2.1 AA+ baseline and KFM inclusion principles. |
| v11.0.0  | 2025-11-20 | `@kfm-a11y`   | Initial v11 draft and baseline requirements. |

---

<div align="center">

♿ **Kansas Frontier Matrix — UI Accessibility & Inclusion Super-Standard (v11.2.6)**  
Accessibility is infrastructure · Inclusion is architecture · Governance is enforcement

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA%2B-2b6cb0" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />

[⬅ Standards Index](./README.md) ·
[📘 Docs Root](../README.md) ·
[🧭 CI/CD Workflows](../workflows/README.md) ·
[🧪 Docs Lint Workflow](../workflows/docs-lint.yml.md) ·
[⚖ FAIR+CARE Validation Workflow](../workflows/faircare-validate.yml.md) ·
[📏 Markdown Protocol (KFM‑MDP v11.2.6)](./kfm_markdown_protocol_v11.2.6.md) ·
[🏛️ Governance Charter](./governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](./faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](./sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>