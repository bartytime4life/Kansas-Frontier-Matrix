---
title: "♿ Kansas Frontier Matrix — UI Accessibility & Inclusion Super-Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/ui_accessibility.md"

version: "v11.2.7"
last_updated: "2026-01-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Accessibility Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<sha256:v11.2.6>"

signature_ref: "../../releases/v11.2.7/signature.sig"
attestation_ref: "../../releases/v11.2.7/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.7/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.7/manifest.zip"
telemetry_ref: "../../releases/v11.2.7/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-ui-accessibility-v11.2.7.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"

license: "CC-BY-4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

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
    - "dashboards"
    - "story-node-authoring"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Sensitivity"
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
  - "docs/standards/ui_accessibility.md@v11.2.6"
  - "docs/standards/ui_accessibility.md@v11.2.2"
  - "docs/standards/ui_accessibility.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../schemas/json/kfm-ui-accessibility-superstandard-v11.2.7.schema.json"
shape_schema_ref: "../../schemas/shacl/kfm-ui-accessibility-superstandard-v11.2.7-shape.ttl"

story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:docs:standards:ui-accessibility-superstandard:v11.2.7"
semantic_document_id: "kfm-ui-accessibility-superstandard"
event_source_id: "ledger:kfm:doc:standards:ui-accessibility-superstandard:v11.2.7"
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
Define the **binding accessibility & inclusion requirements** for all KFM user interfaces (web, maps, 3D, Story Nodes, Focus Mode, explainability views, dashboards, and documentation rendering) so they remain usable, understandable, and equitable for the widest possible range of people—aligned with **WCAG 2.1 AA+**, **FAIR+CARE**, and **MCP‑DL v6.3**.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA%2B-2b6cb0" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

### Scope (normative)

This standard applies to **all KFM user-facing surfaces**, including (but not limited to):

- 🌐 Web application UI (React + map clients)
- 🧭 Focus Mode panels, drawers, overlays, timeline playback, and reader flows
- 📰 Story Node rendering (Markdown → UI), including citations/evidence blocks
- ✍️ Story Node authoring/editor experiences (if present)
- 🗺️ 2D maps (MapLibre or equivalent)
- 🧊 3D scenes and time-based visualizations (Cesium/WebGL or equivalent)
- 📊 Charts and data visualization layers (SVG / Canvas / WebGL)
- 🧠 Explainability dashboards + model health + uncertainty views (if present)
- 📄 Rendered documentation (Markdown → HTML in-app)

All covered surfaces MUST meet:

- ✅ **WCAG 2.1 AA+** *(KFM baseline)*  
- ✅ **WAI-ARIA** authoring practices *(only when native semantics are insufficient)*  
- ✅ **FAIR+CARE** framing and equity expectations *(inclusive language + transparent tradeoffs)*  
- ✅ **Sovereignty policy constraints** *(no sensitive location leaks; redactions must be explained safely)*  

> [!NOTE]
> KFM treats accessibility as **infrastructure**, not polish. If the UI “works” but excludes users, it is **broken**.

### Principles (POUR + KFM extensions)

KFM uses WCAG’s POUR principles and extends them with KFM governance constraints:

| Principle      | Defined By     | What it means in KFM |
|----------------|----------------|----------------------|
| Perceivable    | WCAG           | Multiple modalities: visual + text + captions + summaries |
| Operable       | WCAG           | Keyboard + AT control without traps; alternatives to gestures |
| Understandable | WCAG           | Predictable UI, consistent affordances, plain language |
| Robust         | WCAG           | Works across AT, browsers, and future tech changes |
| Respectful     | KFM / FAIR+CARE | Language and presentation respect identity, dignity, and context |
| Equitable      | KFM            | Design supports diverse sensory, cognitive, motor, bandwidth, and device realities |
| Sovereignty-safe | KFM governance | Redaction/classification applies to *all* UI channels (visual + alt + captions + exports) |

### Non‑negotiables (KFM posture)

- 🚦 **Release-blocking:** accessibility failures block merges/releases unless a governed waiver exists.
- 🧾 **Evidence-first UI:** whenever the UI asserts facts (especially in Focus Mode), it must surface **citable provenance**.
- 🧱 **Boundary-safe:** UI consumes data through **API contracts**; it must not query the graph directly.
- 🪶 **Sovereignty-aware:** accessibility features MUST NOT become a “side channel” that reveals restricted data.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
├── 📄 README.md
├── 📁 governance/
│   ├── 📄 ROOT_GOVERNANCE.md
│   ├── 📄 ETHICS.md
│   └── 📄 SOVEREIGNTY.md
└── 📁 standards/
    ├── 📄 README.md
    ├── 📄 ui_accessibility.md                 ← this standard ♿
    └── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md       ← doc authoring rules (Markdown → UI assumptions)

📁 .github/
└── 📁 workflows/
    ├── 📄 kfm-ci.yml                          ← primary CI gates
    └── 📄 docs-lint.yml                        ← docs structure/link checks (if present)

📁 reports/                                    ← recommended evidence output surface (optional)
└── 📁 self-validation/
    └── 📁 a11y/
        ├── 📄 a11y_summary.json               ← machine-readable a11y results (per run)
        └── 📄 summary.md                      ← human-readable summary (PR-friendly)

📁 web/ or 📁 src/web/                          ← UI app (repo-dependent)
└── 📁 ui/                                      ← shared UI components + patterns (repo-dependent)
~~~

**Author rules (normative)**

- Component-level docs MUST link back to this standard.
- Any “exception” MUST be documented, time-bounded, and governed (see **⚖ FAIR+CARE & Governance**).
- Directory layout examples are **targets**; repos may vary, but the *intent boundaries* must not.

---

## 🧭 Context

### Accessibility as governed infrastructure

KFM is a meaning-making system (maps + narrative + evidence). Accessibility failures are not “UX bugs”—they are:

- 🧯 **public trust failures** (users cannot verify what the system claims),
- 🧭 **governance failures** (meaning is withheld from parts of the public),
- 🧱 **system integrity failures** (alternatives and summaries are where side-channels happen).

### Relationship to other KFM standards (expected)

- 📜 Doc protocol / rendering assumptions: `./KFM_MARKDOWN_WORK_PROTOCOL.md`
- 🏛️ Governance authority: `../governance/ROOT_GOVERNANCE.md`
- ⚖ Ethical framing: `../governance/ETHICS.md`
- 🪶 Sovereignty constraints: `../governance/SOVEREIGNTY.md`

### 📚 Project reference library lens (influence → this standard)

<details>
<summary><strong>📦 Expand: Which project files shape this accessibility standard (and how)</strong></summary>

#### 🧭 Core KFM system + governance docs
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx` → Focus Mode UX surfaces, provenance-first UI expectations, contract boundaries.
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx` → Offline/low-bandwidth realities, story authoring/editor surfaces, dashboards, mobile-first constraints.
- `Audit of the Kansas Frontier Matrix (KFM) Repository.pdf` → Missing gates/runbooks/templates: reinforces “release-blocking” a11y posture + evidence outputs.

#### 🌐 Web + UI engineering
- `responsive-web-design-with-html5-and-css3.pdf` → responsive reflow, semantic HTML, WCAG/ARIA discipline, “offline-first” considerations.
- `O-R programming Books.pdf` + `F-H programming Books.pdf` → semantic HTML + “don’t use roles for semantic elements” rule; ARIA used only where necessary.
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` → asset hygiene: readable compression, alt text, avoid repo bloat, preserve legibility.

#### 🗺️ Geospatial + cartography + mapping UX
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf` → legend clarity, symbology choices as meaning decisions, classification/aggregation transparency.
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` → field constraints, small screens, unstable networks, offline affordances.
- `python-geospatial-analysis-cookbook.pdf` + `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` → raster/time-series layers: require accessible legends, summaries, and non-visual alternatives.

#### 🧪 Modeling, uncertainty, and inference hygiene (UI implications)
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` → communicate V&V + uncertainty; UI must not present simulations as certainty.
- `think-bayes-bayesian-statistics-in-python.pdf` + regression/statistics PDFs → credible intervals/uncertainty visuals require accessible explanations and tables.

#### 🗄️ Data systems + interoperability (UI implications)
- `Data Spaces.pdf` → trust via metadata interfaces; encourages discoverable, machine-readable accessibility evidence artifacts.
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` + `Scalable Data Management for Future Hardware.pdf` → latency/streaming: accessibility includes predictable loading + progressive disclosure.

#### 🛡️ Security & hostile inputs (UI implications)
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` + `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` → defensive posture: do not leak sensitive info via tooltips, alt text, hidden DOM, exports, logs, or telemetry.
- `Data Mining Concepts & applictions.pdf` → inference control mindset: telemetry and query outputs must not enable sensitive inference.

#### 📚 Programming shelves (general craft)
- `A programming Books.pdf` … `U-X programming Books.pdf` → keeps implementation patterns pragmatic; encourages testable, maintainable accessibility fixes.

</details>

---

## 🗺️ Diagrams

### Accessibility gate in the CI/CD pipeline (release-blocking)

~~~mermaid
flowchart LR
  A["PR / Push"] --> B["Build UI + render docs"]
  B --> C["A11y checks: axe / pa11y / Lighthouse + lint"]
  C --> D{"Pass policy?"}
  D -->|Yes| E["Upload reports + emit telemetry"]
  D -->|No| F["Block merge / release"]
  E --> G["Governance ledger + dashboards"]
~~~

### Accessibility in the KFM pipeline boundary (no side channels)

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV]
  B --> C[Graph]
  C --> D[APIs]
  D --> E[UI / Focus Mode]
  E --> F[Exports / Reports]

  subgraph Guardrails
    G1[Redaction + Classification] --> E
    G1 --> F
    G2[Evidence Links + Provenance] --> E
  end
~~~

---

## 🧱 Architecture

### 1) Baseline requirements for all UIs (MUST)

#### Keyboard interaction (MUST)

All interactive elements MUST:

- be reachable via `Tab` / `Shift+Tab`,
- support activation via `Enter` and/or `Space` (as appropriate),
- provide a visible focus indicator (not removed),
- avoid keyboard traps (user must always be able to escape),
- preserve logical focus order (DOM order reflects reading/interaction order).

Minimum focus-ring pattern (example):

~~~css
:focus-visible {
  outline: 3px solid var(--kfm-focus-ring-color);
  outline-offset: 3px;
}
~~~

Constraint: `--kfm-focus-ring-color` MUST meet ≥ **3:1** contrast against adjacent colors.

#### Landmarks + skip navigation (MUST)

- Every app shell MUST provide landmarks: `header`, `nav`, `main`, `footer`.
- A “Skip to main content” link MUST be present and visible on focus.

~~~html
<a class="skip-link" href="#main">Skip to main content</a>
<main id="main">
  <!-- app content -->
</main>
~~~

#### Color, contrast, and themes (MUST)

- Text contrast ratio MUST be:
  - ≥ **4.5:1** for normal text,
  - ≥ **3:1** for large text.
- Focus indicators and key icons MUST be ≥ **3:1**.
- Light and dark themes MUST both pass.
- State MUST NOT rely on color alone (add icons, patterns, labels, or text).

#### Text scaling and reflow (MUST)

- UI MUST remain usable at **200% zoom** without horizontal scrolling for primary content flows.
- Layout MUST support responsive reflow:
  - content wraps,
  - controls remain reachable,
  - dialogs remain operable without hidden close controls.

#### Touch targets + pointer alternatives (MUST)

- Touch targets SHOULD be ≥ **44×44 CSS px** wherever feasible.
- Any gesture-based control MUST have a non-gesture alternative:
  - drag → buttons, keyboard steps, or numeric input
  - pinch → zoom controls + keyboard shortcuts
  - hover-only → click/focus alternative

#### Semantics and ARIA discipline (MUST)

- Prefer native HTML semantics (`button`, `a`, `nav`, `main`, `header`, `footer`, `section`, `article`).
- Use ARIA only when native semantics are insufficient.
- **Do not set ARIA roles that duplicate native semantics** (avoid “role=button” on `<button>` etc).

Example input labeling:

~~~html
<label for="riverName">River name</label>
<input id="riverName" name="riverName" autocomplete="off" />
<p id="riverError" aria-live="polite"></p>
~~~

**Accessibility rule of thumb:** “If you only remember one thing—use the correct elements.” ✅

#### Errors, validation, and status (MUST)

- Errors MUST be:
  - visually visible,
  - announced to assistive tech (`aria-live` or `role="alert"`),
  - tied to relevant fields when possible (`aria-describedby`).
- Avoid “only red border” validation states.
- Loading states MUST be announced (polite) and MUST NOT trap focus.

#### Motion, animation, and sensory load (MUST)

- Respect `prefers-reduced-motion`.
- Avoid auto-play animations and auto-flying map/3D camera moves by default.
- If animation is meaningful, provide:
  - pause/stop controls,
  - step-by-step mode,
  - reduced-motion alternative.

~~~css
@media (prefers-reduced-motion: reduce) {
  * { scroll-behavior: auto; transition: none !important; animation: none !important; }
}
~~~

#### Timeouts, long tasks, and resilience (MUST)

- Long operations MUST show progress and allow cancellation when feasible.
- Timeouts MUST be avoidable or extendable (especially in Focus Mode reading/authoring).
- Background refresh MUST not steal focus or reset user context.

---

### 2) Maps, charts, timelines, and 3D scenes (MUST)

#### Map UIs (MapLibre, etc.) (MUST)

Each map experience MUST provide:

- an accessible label for the map region,
- keyboard interaction for essential actions *or* an equivalent non-map pathway,
- an accessible legend + layer list,
- a non-visual summary of what the map conveys (and what it does **not** convey).

Example wrapper:

~~~html
<section role="region" aria-label="Kansas hydrology map">
  <div id="mapContainer"></div>
  <p id="mapHelp">
    Hydrology layers for Kansas rivers and floodplains. Use the layer list and the data table below to explore features.
  </p>
</section>
~~~

**If full keyboard panning is not feasible**, the UI MUST provide an equivalent pathway:
- searchable feature list
- filters
- data table view
- “jump to location” via named places (not raw coordinates for sensitive contexts)

#### Legends and symbology as meaning (MUST)

- Legends MUST be accessible and descriptive (not only colored squares).
- Where color ramps are used, provide:
  - textual ranges,
  - patterns or line styles where possible,
  - explicit “classification method” notes (e.g., quantile, equal interval) when it changes meaning.

#### Timeline controls (Focus Mode + maps) (MUST)

Any time slider / playback control MUST:

- be keyboard operable,
- expose the current time window as text,
- provide discrete step controls (prev/next),
- provide pause/play (and respect reduced motion).

Example (minimum viable):

~~~html
<div role="group" aria-label="Timeline controls">
  <button type="button">Previous</button>
  <button type="button">Play</button>
  <button type="button">Next</button>

  <label for="timeRange">Time</label>
  <input id="timeRange" type="range" min="0" max="100" value="0" />
  <output aria-live="polite">1854</output>
</div>
~~~

#### Charts and visualizations (SVG/Canvas/WebGL) (MUST)

For charts, the UI MUST provide:

- a clear title and description accessible to AT,
- a text summary and/or tabular view,
- keyboard-accessible legend toggles and key controls,
- uncertainty cues when relevant (e.g., confidence bands), plus a textual explanation.

Example (SVG semantics):

~~~html
<svg aria-labelledby="chartTitle chartDesc" role="img">
  <title id="chartTitle">Kansas River flow over time</title>
  <desc id="chartDesc">
    Line chart showing annual flow from 1900 to 2020, with drought periods highlighted.
  </desc>
</svg>
~~~

#### 3D scenes (Cesium/WebGL) (MUST)

- Respect motion preferences (`prefers-reduced-motion`) where possible.
- Provide:
  - a reset view (camera home),
  - keyboard access for essential actions,
  - non-visual summaries of key scene meaning and state,
  - a 2D or list/table fallback for critical workflows.

---

### 3) Language, inclusivity, and cognitive accessibility (MUST/SHOULD)

#### Plain language (SHOULD)

- Prefer clear, plain language for UI copy.
- Avoid jargon unless defined (tooltips, glossary links, “learn more”).
- Provide “quick summary” blocks for dense panels (especially Focus Mode).

#### Respectful framing (MUST)

- Avoid ableist language and assumptions.
- When presenting historical content:
  - avoid sensationalism,
  - present context clearly,
  - align framing with governance notes and sovereignty constraints.

#### User autonomy (MUST)

- Users MUST be able to control information density:
  - collapse/expand sections,
  - “simple” vs “detailed” mode where appropriate,
  - persistent preferences (without collecting PII).

---

### 4) Documentation rendering (Markdown → UI) (MUST)

If KFM renders Markdown inside the UI:

- Headings MUST map to semantic heading levels.
- Tables MUST have accessible headers, or provide table alternatives.
- Code blocks MUST be scrollable *and* copyable without trapping focus.
- Images MUST have alt text (or be marked decorative).

**Critical governance note:** redaction rules apply to:
- images,
- captions,
- alt text,
- footnotes,
- hidden DOM,
- downloadable exports.

---

### 5) Performance & “inclusive latency” (MUST)

Performance is accessibility:

- The UI MUST avoid long main-thread blocks that prevent keyboard/AT interaction.
- Use:
  - pagination,
  - virtualization for long lists,
  - progressive loading (skeletons that don’t mislead),
  - server-side filtering (don’t ship millions of features).

**Energy/carbon note (recommended):** heavy WebGL/3D layers SHOULD expose a “low-power mode” and emit performance/energy telemetry (aggregated, non-PII).

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode UI (MUST)

- Focus Mode containers MUST be keyboard operable end-to-end.
- Content changes MUST be perceivable:
  - update headings, and/or
  - announce significant changes via a live region.
- Provide a consistent “next/previous” navigation model (no focus loss).

Example dialog skeleton:

~~~html
<aside role="dialog" aria-modal="true"
       aria-labelledby="focusTitle"
       aria-describedby="focusBody">
  <h2 id="focusTitle">Focus View</h2>
  <div id="focusBody">
    <!-- narrative, evidence links, and governance notices -->
  </div>

  <nav aria-label="Focus navigation">
    <button type="button">Previous</button>
    <button type="button">Next</button>
    <button type="button">Close</button>
  </nav>
</aside>
~~~

### Story Node rendering (MUST)

Story Node content MUST render with:

- semantic headings and lists,
- alt text for content images and diagrams,
- captions/transcripts for media where applicable,
- citations/evidence blocks that are keyboard navigable and screen-reader friendly.

### AI assistance in Focus Mode (Allowed with restrictions)

If AI-generated or AI-assisted content appears in Focus Mode:

- MUST be **opt-in** (user-controlled toggle)
- MUST be labeled (what is AI vs sourced)
- MUST provide citations for factual claims (system-native pointers preferred)
- MUST include uncertainty framing (confidence, caveats, or “unknown”)
- MUST NOT infer sensitive locations or re-identify people from partial context
- MUST NOT bypass redactions (including via alt text, summaries, tooltips, or exports)

### Sovereignty constraints MUST be enforced in UI (no side channels)

- Sensitive coordinates and site details MUST be generalized or withheld according to policy.
- When redaction occurs, the UI MUST present a governance-safe explanation (“why”), without revealing the withheld details.

---

## 🧪 Validation & CI/CD

### 1) Automated checks (MUST)

A release (or protected-branch merge) MUST include automated a11y checks for:

- primary navigation surfaces,
- Story Node reader surfaces,
- Focus Mode surfaces,
- at least one map surface (2D) and one “heavy viz” surface (chart or 3D) when present.

Recommended automation types:

- Browser-based audits: `axe-core` / `pa11y`
- Lighthouse accessibility scoring (where stable)
- Component linting: `eslint-plugin-jsx-a11y` (or equivalent)
- Markdown rendering checks for Story Nodes (headings/links/alt text)

### 2) Manual checks (SHOULD)

At minimum per release candidate:

- keyboard-only walkthrough of core flows,
- screen reader spot-check (NVDA/VoiceOver) of:
  - navigation,
  - Focus Mode,
  - at least one map layer list + legend + “feature details” flow.

### 3) Gating policy (normative)

The pipeline MUST fail if:

- critical accessibility errors are detected (as defined by policy config),
- required reports are missing,
- telemetry emission fails *(no evidence = not shippable)*.

Any temporary waiver MUST:

- be explicitly approved via governance,
- be time-bounded,
- include mitigation notes and a remediation plan,
- be referenced in release notes (where applicable).

---

## 📦 Data & Metadata

### Reports (recommended evidence artifacts)

Per CI run, emit:

- `reports/self-validation/a11y/a11y_summary.json`
- `reports/self-validation/a11y/summary.md`

Suggested JSON fields (schematic):

~~~json
{
  "workflow": "accessibility-check",
  "run_id": "<run-id>",
  "routes_scanned": 0,
  "surfaces_scanned": ["focus-mode", "story-node-reader", "map-2d"],
  "critical": 0,
  "major": 0,
  "minor": 0,
  "lighthouse_a11y_score": null,
  "timestamp": "<utc-iso8601>",
  "commit_sha": "<git-sha>",
  "policy_version": "v11.2.7",
  "waivers": []
}
~~~

### Telemetry (recommended; aggregated, non-PII)

A11y-related telemetry events SHOULD be appended into:

- `../../releases/v11.2.7/focus-telemetry.json`

Minimum signals:

- severity counts (critical/major/minor),
- routes/components scanned,
- pass/fail,
- runtime, energy, carbon (when available).

**Privacy / inference safety note (normative):**
- Telemetry MUST avoid collecting user content, user identifiers, or precise sensitive locations.
- Aggregate metrics only; do not store raw interaction traces that enable re-identification.

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

### FAIR (applied to accessibility work)

- **Findable:** stable doc IDs + predictable paths + release manifests
- **Accessible:** standards and reports discoverable in docs and telemetry artifacts
- **Interoperable:** JSON summaries + PROV/DCAT mappings
- **Reusable:** versioned standard + governance evidence trail

### CARE (applied to UI and narrative meaning)

- **Collective benefit:** the UI must not exclude users by default design choices
- **Authority to control:** sovereignty constraints respected in disclosure and display
- **Responsibility:** accessibility failures block releases; waivers are governed
- **Ethics:** respectful framing, no exploitative/dehumanizing presentation

### Governance hooks (normative)

- 🏛️ Governance authority: `../governance/ROOT_GOVERNANCE.md`
- ⚖ Ethical framing: `../governance/ETHICS.md`
- 🪶 Sovereignty constraints: `../governance/SOVEREIGNTY.md`

---

## 🕰️ Version History

| Version  | Date       | Author        | Summary |
|---------:|------------|---------------|---------|
| v11.2.7  | 2026-01-12 | `@kfm-a11y`   | Corrected governance path alignment (docs/governance/*); expanded scope to dashboards + authoring surfaces; strengthened “no side-channel” sovereignty rule (alt text/summaries/exports); added timeline accessibility requirements; added inclusive-latency/performance guidance + telemetry privacy constraints; refreshed directory layout to v13-aligned docs structure. |
| v11.2.6  | 2025-12-12 | `@kfm-a11y`   | Updated to KFM‑MDP v11.2.6 formatting; corrected repo-relative references; standardized directory layout tree; added CI gating diagram; expanded Focus Mode/Story Node constraints and telemetry/report expectations. |
| v11.2.2  | 2025-11-27 | `@kfm-a11y`   | Established governed UI Accessibility Super-Standard with WCAG 2.1 AA+ baseline and KFM inclusion principles. |
| v11.0.0  | 2025-11-20 | `@kfm-a11y`   | Initial v11 draft and baseline requirements. |

---

<div align="center">

♿ **Kansas Frontier Matrix — UI Accessibility & Inclusion Super-Standard (v11.2.7)**  
Accessibility is infrastructure · Inclusion is architecture · Governance is enforcement

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/WCAG-2.1_AA%2B-2b6cb0" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />

[⬅ Standards Index](./README.md) ·
[📘 Docs Root](../README.md) ·
[🧾 Markdown Work Protocol](./KFM_MARKDOWN_WORK_PROTOCOL.md) ·
[🧭 CI Workflow](../../.github/workflows/kfm-ci.yml) ·
[🏛️ Governance Charter](../governance/ROOT_GOVERNANCE.md) ·
[⚖ Ethics](../governance/ETHICS.md) ·
[🪶 Sovereignty Policy](../governance/SOVEREIGNTY.md)

© 2026 Kansas Frontier Matrix — CC‑BY‑4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
