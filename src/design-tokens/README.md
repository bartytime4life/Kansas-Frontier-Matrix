---
title: "src/design-tokens — README"
path: "src/design-tokens/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:src:design-tokens:readme:v1.0.0"
semantic_document_id: "kfm-src-design-tokens-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:design-tokens:readme:v1.0.0"
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

# src/design-tokens — README

## 📘 Overview

### Purpose
This directory defines **design tokens** for KFM’s UI-facing surfaces (e.g., the map UI, Focus Mode panels, navigation, and shared UI primitives). Tokens provide a **single source of truth** for presentation values (color, typography, spacing, radii, shadows, z-index, etc.) so styling remains consistent and reviewable.

This document is intentionally **contract-oriented**: it describes *what belongs here*, *what outputs are expected*, and *what invariants must hold*, without assuming any specific implementation tooling (not confirmed in repo).

### Scope

| In Scope | Out of Scope |
|---|---|
| Token naming conventions + semantics | React component implementation details |
| Token source format(s) + validation expectations | Map layer registries / dataset catalogs |
| Build/export expectations for UI consumption | Neo4j/graph access (must remain API-mediated) |
| Accessibility constraints (contrast, typography, motion) | Historical narrative content + citations |

### Audience
- Primary: UI engineers, frontend maintainers, and design-system contributors
- Secondary: API engineers (contract awareness), docs maintainers, reviewers (a11y/governance)

### Definitions (link to glossary)
- Link (if present): `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **Token:** A named, versioned value used in UI styling (e.g., `color.text.primary`).
  - **Primitive token:** Raw values (hex colors, px/rem sizes) not tied to meaning.
  - **Semantic token:** Meaningful aliases (e.g., “primary text”) mapped to primitives.
  - **Theme:** A set of token values for a mode (light/dark/high-contrast/print).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Token source(s) | `src/design-tokens/<TBD>` | UI / Design | Source-of-truth format not confirmed in repo |
| Token schema(s) | `schemas/<TBD>` | UI / Platform | Optional but strongly recommended |
| Generated exports | `src/design-tokens/<dist or build output TBD>` | UI | Must be reproducible + deterministic |
| Consumption docs | `web/<TBD>` + `docs/design/<TBD>` | UI / Docs | Not confirmed in repo |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Token taxonomy is defined (primitive vs semantic) and naming is consistent
- [ ] Validation steps are listed and repeatable
- [ ] Accessibility constraints are explicit (contrast, motion, font sizing)
- [ ] No references imply bypassing API contracts or exposing sensitive data

## 🗂️ Directory Layout

### This document
- `path`: `src/design-tokens/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + map clients consume exported tokens |
| Documentation | `docs/` | Design guidelines + governed docs |
| Schemas | `schemas/` | JSON schemas for tokens (recommended) |
| Tooling | `tools/` | Token build/validation scripts (if adopted) |

### Expected file tree for this sub-area
> The structure below is **expected** for maintainability, but is **not confirmed in repo**.

~~~text
📁 src/
└── 📁 design-tokens/
    ├── 📄 README.md
    ├── 📁 tokens/                 # source-of-truth inputs (not confirmed in repo)
    ├── 📁 schemas/                # optional local schemas (not confirmed in repo)
    ├── 📁 build/                  # build scripts / transforms (not confirmed in repo)
    └── 📁 dist/                   # generated outputs; do not hand-edit (not confirmed in repo)
~~~

## 🧭 Context

### Background
KFM’s UI blends maps, timelines, and narrative panels. Without a shared token system, UI styling tends to diverge across components and features (especially when multiple contributors are involved). Tokens ensure changes are:
- centralized,
- reviewable,
- testable (especially for accessibility),
- and easy to propagate across the UI.

### Assumptions
- The canonical system pipeline ordering is preserved (UI is downstream of the API layer).
- UI consumes data through API contracts; styling artifacts must not introduce data coupling.
- Token build/export should be deterministic (same inputs → same outputs).

### Constraints / invariants
- **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode** ordering remains intact.
- **Frontend consumes contracts via APIs (no direct graph dependency).**
- No sensitive locations or restricted content should be inferable from styling tokens.
- Generated artifacts must be reproducible and should not embed timestamps/randomness.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the source-of-truth token format (JSON/YAML/TS/etc.)? | TBD | TBD |
| What are the supported themes (light/dark/high-contrast/print)? | TBD | TBD |
| Where do exported artifacts live (repo vs build output)? | TBD | TBD |
| Do we need a JSON Schema + CI gate for tokens? | TBD | TBD |

### Future extensions
- Theme packs for Focus Mode (e.g., “Archive”, “Prairie”, “High Contrast”).
- Tokenized map styling primitives (only presentation semantics; no dataset IDs).
- A11y automation: contrast checks + reduced-motion gates in CI.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Token source-of-truth] --> B[Validation + build/export]
  B --> C[UI consumable artifacts\n(CSS vars / JSON / TS)]
  C --> D[React/Map UI]
  D --> E[Story Nodes + Focus Mode rendering]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Token source(s) | TBD | `src/design-tokens/<TBD>` | Schema + lint (recommended) |
| Brand/a11y rules | TBD | `docs/design/<TBD>` | Review gate (recommended) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| UI tokens export | TBD | `src/design-tokens/<TBD>` | Schema (recommended) |
| Theme variants | TBD | `src/design-tokens/<TBD>` | Diff-friendly + deterministic |

### Sensitivity & redaction
- Tokens are expected to be **public** and should not include:
  - private URLs,
  - organization-internal codenames,
  - location-specific “hidden meaning” styling that implies restricted sites.
- If any iconography or terminology is culturally sensitive, route through governance review (requires human review).

### Quality signals
- Contrast ratio targets for text on surfaces (a11y gate).
- Reduced-motion compliance (avoid forcing animations).
- Token naming consistency + no unused exports (lint gate).
- Deterministic builds (byte-for-byte stable outputs when inputs unchanged).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable: design tokens are UI presentation contracts, not asset catalogs.

### DCAT
- Not applicable: tokens are not published datasets.

### PROV-O
- Optional: if tokens are generated by a build step, record the build activity/run in CI logs (location **not confirmed in repo**).

### Versioning
- Token changes should follow semantic versioning *if* exported artifacts are treated as contracts (policy **not confirmed in repo**).
- At minimum: changelog notes in PR descriptions, and stable token names (avoid churn).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Token sources | Declare primitives + semantic tokens | Files under `src/design-tokens/` |
| Validator | Ensure schema + naming correctness | CI step (recommended) |
| Exporter | Emit UI-consumable artifacts | Build script/tool (not confirmed) |
| UI consumers | Import tokens to style components | `web/` |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Token schema | `schemas/<TBD>` | Semver recommended (not confirmed in repo) |
| Export format | `src/design-tokens/<TBD>` | Must be backwards compatible or versioned |
| A11y rules | `docs/design/<TBD>` | Review + CI checks recommended |

### Extension points checklist (for future work)
- [ ] Add new token domain (e.g., `motion.*`, `shadow.*`) with schema updates
- [ ] Add theme(s) with explicit surface/text mappings
- [ ] Add contrast checks and reduced-motion checks in CI
- [ ] Add docs + examples for consumption in `web/`

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Tokens govern the **presentation layer** of Focus Mode:
  - readability of narrative text + citations,
  - visual hierarchy of evidence panels,
  - map UI controls (buttons, legends, overlays).
- Tokens must not weaken provenance rendering (e.g., citation links must remain clearly distinguishable).

### Provenance-linked narrative rule
- This directory does not define narrative claims.
- When styling narrative, ensure citations and provenance affordances remain visually explicit.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Token schema validation (if schema exists)
- [ ] Lint: naming conventions + duplicates + unused tokens
- [ ] A11y checks: contrast + focus states + reduced motion
- [ ] Build determinism check (no timestamped outputs)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# validate tokens
# <cmd> tokens:validate

# build exports
# <cmd> tokens:build

# run UI checks (optional)
# <cmd> test:ui
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Token build hash | CI | `mcp/runs/` or CI logs (not confirmed in repo) |
| Contrast compliance | CI | Test output / report artifact |

## ⚖ FAIR+CARE & Governance

### Review gates
- Design/a11y review: recommended for changes affecting typography/colors/motion.
- Governance review: required if iconography or terminology may be sensitive (requires human review).

### CARE / sovereignty considerations
- Avoid UI metaphors, naming, or symbols that could misrepresent or disrespect communities tied to the represented places/events.
- If theme names reference cultures, tribes, or sensitive historical contexts, route through governance review (requires human review).

### AI usage constraints
- Token generation should not introduce policy or infer sensitive information.
- Keep AI permissions/prohibitions aligned with repository governance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README scaffold for design tokens | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`