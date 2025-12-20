---
title: "README — Accessibility Icons"
path: "src/icons/accessibility/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
status: "draft"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:src:icons:accessibility:readme:v1.0.0"
semantic_document_id: "kfm-src-icons-accessibility-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:icons:accessibility:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# README — Accessibility Icons

## 📘 Overview

### Purpose
This directory provides a **single, governed place** for icon assets and patterns that are specifically
used to support **accessibility and inclusive UI behaviors** (e.g., indicating an accessibility feature,
showing an a11y status, or pairing an icon with text for assistive tech).

This README defines:
- how accessibility icons should be authored and stored,
- how they should be consumed in UI components safely,
- the minimum a11y rules that must be met before adding/using icons.

### Scope

| In Scope | Out of Scope |
|---|---|
| Authoring/adding accessibility-related icons | General map symbology libraries or cartographic markers |
| Usage rules for SVG icon accessibility | Styling systems, brand guidelines, or full design system docs |
| File naming + organization for this subfolder | API contracts or graph semantics |
| License/attribution expectations for third-party icons | Dataset catalogs (STAC/DCAT/PROV) for data assets |

### Audience
- Primary: frontend engineers, UX/UI implementers, accessibility reviewers
- Secondary: designers contributing SVGs; contributors adding new UI affordances

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **a11y**: accessibility
  - **Decorative icon**: conveys no unique information; should be hidden from assistive tech
  - **Informative icon**: conveys meaning; must expose an accessible name (via label/title)
  - **Accessible name**: what screen readers announce for an element (e.g., via `aria-label`)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `src/icons/accessibility/README.md` | UI / Design Systems | Governed rules for this folder |
| Icon assets | `src/icons/accessibility/*` | UI / Design Systems | SVGs and/or components (repo-specific) |
| Attribution (recommended) | `src/icons/accessibility/ATTRIBUTION.md` | UI / Design Systems | Add when importing third-party icon sets |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Folder purpose + scope clearly defined
- [ ] A11y rules for decorative vs informative icons are explicit
- [ ] Naming conventions defined
- [ ] Validation steps listed (lint/build/a11y checks) and repeatable (or marked TBD)

## 🗂️ Directory Layout

### This document
- `path`: `src/icons/accessibility/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Source code | `src/` | Shared code/modules (including icons) |
| Frontend | `web/` | UI that consumes icons (React/Map UI) |
| Documentation | `docs/` | Canonical governed docs; design/a11y standards |
| Tests | `tests/` | Unit/integration/a11y tests |

### Expected file tree for this sub-area
~~~text
📁 src/
└── 📁 icons/
    └── 📁 accessibility/
        ├── 📄 README.md
        ├── 📄 ATTRIBUTION.md            (recommended if any third‑party icons are used)
        ├── 📄 LICENSE                   (recommended if licenses differ from repo default)
        ├── 📄 index.ts                  (optional: explicit export surface)
        ├── 📁 svg/                      (optional: raw assets)
        │   ├── 📄 <icon-name>.svg
        │   └── 📄 ...
        └── 📁 react/                    (optional: wrapped components)
            ├── 📄 <IconName>.tsx
            └── 📄 ...
~~~

## 🧭 Context

### Background
Icons are a dense, high-frequency UI primitive. Small a11y mistakes (like accidental focus stops,
missing accessible names, or redundant announcements) create outsized UX harm.

This folder exists to make the “right thing” the default by keeping accessibility icon decisions
**documented, reviewable, and consistent**.

### Assumptions
- Icons in this folder may be used in buttons, toggles, map overlays, and Focus Mode UI panels.
- Some consumers may be React components; others may import raw SVG (repo-dependent).

### Constraints / invariants
- **Decorative icons must not be announced** by screen readers.
- **Informative icons must have an accessible name** (via label/title/association).
- Icons should not encode meaning by color alone (pair icons with text or other cues).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical icon build/optimization step documented (if any)? | TBD | TBD |
| Do we store icons as raw SVG, React components, or both? | TBD | TBD |
| What is the repo’s default license for code assets vs docs? | TBD | TBD |

### Future extensions
- Extension point A: add a small icon “registry” (name → import path → semantic usage notes)
- Extension point B: add automated checks to prevent missing/invalid `viewBox` and `aria-*` usage

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Design source SVG] --> B[Icon asset in src/icons/accessibility]
  B --> C[UI component wrapper]
  C --> D[React/Map UI surfaces]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Icon artwork | SVG | Design contribution or third-party library | Must meet SVG + a11y rules below |
| Icon metadata (optional) | TS/JSON | UI code | Must include human label if informative |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Accessibility icon assets | SVG/TSX | `src/icons/accessibility/...` | Must satisfy a11y rules in this README |
| UI usage examples | Markdown/TSX | Inline in this doc | Must be consistent with rules |

### Sensitivity & redaction
- Not applicable: icons should not contain sensitive geospatial details or PII.

### Quality signals
- SVGs have a stable `viewBox` and scale cleanly
- Use `currentColor` for fill/stroke where theming is required
- No hidden text nodes in SVG that could be announced unexpectedly
- No accidental keyboard-focus stops on SVGs

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- N/A — icon assets are UI/code artifacts, not cataloged geospatial datasets.

### DCAT
- N/A — this directory does not publish datasets.

### PROV-O
- N/A — provenance is handled at code review + version control level for these assets.

### Versioning
- Icons and wrappers should follow standard repo version control practices.
- If a breaking change occurs (renaming/removing an icon), ensure call sites are updated atomically.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Icon assets | Visual symbol primitives | Imported into UI code |
| Icon wrappers (optional) | Enforce a11y defaults + props | Component API (e.g., `title`, `aria-hidden`) |
| UI components | Compose icons with labels/tooltips | React component composition |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Icon file naming | This README | Breaking rename requires repo-wide refactor |
| Wrapper prop conventions | Wrapper file/docs | Version bump if exported API changes |

### Authoring rules for accessibility icons

#### 1) Decorative icons (most common)
If the icon provides no unique meaning (e.g., a chevron next to a labeled button),
it must be hidden from assistive tech.

**Requirements**
- `aria-hidden="true"`
- `focusable="false"` (prevents stray keyboard focus in some environments)
- No `role="img"` / no title announcement

~~~tsx
// Decorative icon inside a button that already has text:
<button type="button">
  <span>Open layers</span>
  <ChevronDownIcon aria-hidden="true" focusable="false" />
</button>
~~~

#### 2) Informative icons (must be labeled)
If the icon conveys meaning by itself (e.g., a status badge or an icon-only button),
it must expose an accessible name.

**Requirements**
- Provide a label via one of:
  - `aria-label`, or
  - `aria-labelledby` tied to a `<title>` or external label element
- Ensure the element is not redundantly announced alongside adjacent text

~~~tsx
// Icon-only button: label is required.
<button type="button" aria-label="Enable high contrast">
  <HighContrastIcon aria-hidden="true" focusable="false" />
</button>
~~~

~~~tsx
// Informative standalone icon with internal title (pattern varies by SVG/component implementation).
// Note: exact wiring depends on how SVGs are wrapped in this repo (not confirmed in repo).
<StatusIcon role="img" aria-label="Accessible route available" focusable="false" />
~~~

#### 3) Color/contrast rules
- Do not rely on color alone to communicate status.
- Prefer pairing icons with text labels or tooltips.
- Prefer `currentColor` so theming/high-contrast modes can adjust colors.

#### 4) Geometry rules
- Must include a `viewBox` so icons scale correctly.
- Avoid hardcoding width/height unless a consumer contract requires it.

#### 5) Third-party icons (license + attribution)
If importing icons from external sources:
- record the origin, license, and any required attribution in `ATTRIBUTION.md`
- do not remove embedded metadata that is required for compliance

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Icons may be used to:
  - indicate sensitivity gating states (public/restricted),
  - indicate available accessibility features (captions, transcripts, contrast),
  - improve scanability of narrative panels.

### Provenance-linked narrative rule
- Not applicable for icons; however, do not use icons to imply factual claims that are not sourced elsewhere.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] SVG sanity: `viewBox` present; no embedded raster images (unless explicitly allowed)
- [ ] A11y review: decorative icons hidden; informative icons labeled
- [ ] Lint/build: icon imports resolve; no dead exports
- [ ] UI checks: icon renders in typical sizes and high-contrast mode (manual/automated as available)

### Reproduction
~~~bash
# Not confirmed in repo: replace with actual repo commands once identified.
# 1) run lint
# 2) run unit tests
# 3) run any a11y checks / storybook checks if present
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| A11y regressions | CI checks | `docs/telemetry/` + `schemas/telemetry/` (if configured) |

## ⚖ FAIR+CARE & Governance

### Review gates
- UI/accessibility review is required when:
  - adding new icon-only controls
  - adding any icon that implies a safety/eligibility/access status

### CARE / sovereignty considerations
- Icons should not expose sensitive location markers or culturally sensitive symbols without review.

### AI usage constraints
- Any AI-assisted generation of SVG content must not introduce prohibited symbols or misrepresent meaning.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial accessibility icon README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`