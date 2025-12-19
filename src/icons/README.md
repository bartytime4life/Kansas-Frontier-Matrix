---
title: "src/icons — Icon Assets"
path: "src/icons/README.md"
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

doc_uuid: "urn:kfm:doc:src:icons:readme:v1.0.0"
semantic_document_id: "kfm-src-icons-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:icons:readme:v1.0.0"
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

# src/icons — Icon Assets

## 📘 Overview

### Purpose
This README governs how **icon assets** are organized, named, licensed, and consumed across KFM—especially in the **map/narrative UI**, Story Nodes, and Focus Mode. The goal is to keep iconography consistent, accessible, and legally clean.

### Scope
| In Scope | Out of Scope |
|---|---|
| SVG/PNG icons used by the UI (buttons, controls, entity badges) | Full illustrations, hero images, marketing art |
| Map symbols (markers, pins, layer glyphs) | Basemaps / tiles / imagery datasets (those belong under `data/`) |
| Entity-type glyphs (e.g., Place/Person/Event) for consistent UI semantics | Third-party icon libraries pulled dynamically at runtime |
| Documentation of conventions (naming, sizing, accessibility) | UI implementation details that belong to `web/` |

### Audience
- Primary: Frontend/UI engineers, designers
- Secondary: API/graph engineers (for aligning entity semantics with UI symbols)

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Icon**: A small visual asset used in UI controls or labels.
  - **Map marker / symbol**: An icon used to represent a feature on the map.
  - **Sprite**: A compiled bundle of multiple icons to reduce requests (if used).
  - **Manifest**: A machine-readable list mapping logical icon IDs → file paths (if used).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Icons directory README | `src/icons/README.md` | UI | This document |
| Icon source files | `src/icons/**` | UI/Design | Prefer SVG for scalability |
| Optional: icon manifest | `src/icons/manifest.*` | UI | Not confirmed in repo; add if needed |
| Optional: generated sprite(s) | `web/**` | UI | Not confirmed in repo; avoid committing generated outputs unless required |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory layout and naming conventions are explicit
- [ ] Licensing and attribution expectations are explicit
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `src/icons/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Icons | `src/icons/` | Canonical icon source assets + conventions |
| Design tokens | `src/design-tokens/` | Color/typography/spacing tokens that icons should align with |
| Frontend | `web/` | React/map clients that render icons |
| Docs | `docs/` | Governed docs, templates, governance policies |
| Schemas | `schemas/` | Any manifest schemas (if introduced) |

### Expected file tree for this sub-area
~~~text
📁 src/
└── 📁 icons/
    ├── 📄 README.md
    ├── 📁 svg/                 # preferred source format (proposed)
    │   ├── 📁 ui/              # buttons, panels, controls
    │   ├── 📁 map/             # markers, pins, layer symbols
    │   └── 📁 entities/        # entity-type glyphs (Place/Person/Event/etc.)
    ├── 📁 png/                 # only if SVG is not viable (legacy/export)
    └── 📁 third_party/         # optional: imported sets + attribution (proposed)
        ├── 📄 LICENSES.md
        └── 📄 SOURCES.md
~~~

## 🧭 Context

### Background
Icon sprawl (duplicated assets, inconsistent naming, unclear licensing) becomes a maintenance and governance risk. This directory centralizes icon assets so the UI can stay consistent across map layers, story panels, and Focus Mode affordances.

### Assumptions
- SVG is the default icon format for UI and map rendering when possible.
- Icons follow a consistent sizing grid (e.g., 16/20/24px) and include a stable `viewBox`.
- Where color is required, icons should be compatible with token-driven theming (e.g., `currentColor` or token-mapped fills).

### Constraints / invariants
- Preserve the KFM pipeline ordering (ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode).
- UI should rely on API contracts for data; icons must not become a “side channel” that encodes hidden or sensitive meaning not present in provenance-linked UI content.
- Licensing must be explicit for any third‑party icon imports (avoid “mystery assets”).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we want an icon **manifest** (icon_id → path) to keep usage consistent? | TBD | TBD |
| Do we need a **sprite** pipeline (build-time bundling) or can we import SVGs directly? | TBD | TBD |
| What entity-type icon mapping is canonical (Place/Person/Event/Organization/Artifact/etc.)? | TBD | TBD |

### Future extensions
- Add a schema-validated icon manifest (with lint rules to prevent breaking renames).
- Add optional build-time optimization (SVGO) and sprite generation (if performance requires it).
- Introduce automated checks for missing attribution files in `third_party/`.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Design + icon sources] --> B[src/icons]
  B --> C[Optional: build optimization]
  C --> D[web/ UI bundles]
  D --> E[React/Map UI renders icons]
  E --> F[Story Nodes + Focus Mode UI]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant Icon as Icon Asset (src/icons)
  UI->>Icon: import/use icon by stable ID/path
  Icon-->>UI: SVG/PNG asset
  UI-->>UI: render icon in map + narrative UI
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| UI icon sources | SVG | `src/icons/svg/**` | Lint/optimize (SVGO) (if enabled) |
| Map symbols | SVG/PNG | `src/icons/svg/map/**` | Size + viewBox + naming checks |
| Third-party sets (optional) | SVG/PNG | `src/icons/third_party/**` | License + attribution required |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Optimized icons (optional) | SVG | build output (TBD) | Not confirmed in repo |
| Sprite bundle (optional) | SVG/JSON | build output (TBD) | Not confirmed in repo |
| Icon manifest (optional) | JSON/YAML | `src/icons/manifest.*` | If added: define schema under `schemas/` |

### Sensitivity & redaction
- Icons are generally **public** assets, but symbolism can be culturally sensitive.
- Avoid sacred/culturally restricted imagery in generic iconography. If a symbol relates to a protected community/context, document review requirements under Governance.

### Quality signals
- Consistent naming (kebab-case) and stable IDs
- File size thresholds (avoid oversized SVG paths)
- SVG hygiene: includes `viewBox`, no embedded raster unless required, no external references
- Accessibility: icons used as controls must have labeled buttons/tooltips at the UI layer

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: N/A (icons are source assets, not datasets)
- Items involved: N/A
- Extension(s): N/A

### DCAT
- Dataset identifiers: N/A
- License mapping: handled at asset level (repo license + any `third_party/` attribution)
- Contact / publisher mapping: N/A

### PROV-O
- `prov:wasDerivedFrom`: only applicable if icons are generated from upstream design sources (not confirmed in repo)
- `prov:wasGeneratedBy`: build step (if sprite/optimization is introduced)
- Activity / Agent identities: N/A until an icon build pipeline exists

### Versioning
- Renaming or removing icons is a breaking change for the UI. Prefer additive changes, and deprecate before removal.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| `src/icons/` | Canonical icon sources | File paths + naming conventions |
| Optional: manifest | Stable logical IDs for icons | JSON/YAML contract (if added) |
| Optional: build optimizer | Reduce size, normalize SVG | Build step + CI gate (if added) |
| `web/` UI | Render icons in map + panels | Import assets / reference IDs |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Naming + directory conventions | `src/icons/README.md` | Additive changes preferred |
| Optional: manifest schema | `schemas/` | Semver + changelog |
| Optional: sprite output contract | build output docs | Versioned by build tooling |

### Extension points checklist (for future work)
- [ ] UI: introduce a single icon registry API for the UI (to prevent drift)
- [ ] Validation: add a CI lint step for icons (sizes, licensing, naming)
- [ ] Governance: add required review for third-party icon imports

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Icons may appear in:
  - Story Node markers/pins on the map
  - Entity-type badges (Place/Person/Event/Organization/Artifact)
  - UI controls in the Focus Mode panel

### Provenance-linked narrative rule
- Icons must not imply facts that aren’t supported by provenance-linked content.
  - Example: use a neutral “event” glyph unless the story node has curated evidence for a more specific symbol.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] (Optional) Icon lint: naming + directory rules + basic SVG hygiene
- [ ] (Optional) License check for `third_party/` additions
- [ ] UI build checks to ensure icon imports resolve

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run doc lint / markdown checks
# 2) (optional) run icon lint (naming, sizes, licenses)
# 3) run UI build/tests to verify imports resolve
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| N/A | N/A | N/A |

## ⚖ FAIR+CARE & Governance

### Review gates
- UI/Design review for icon set changes (consistency + accessibility)
- Governance review trigger if:
  - importing third-party icons without clearly compatible licensing
  - using culturally sensitive symbolism

### CARE / sovereignty considerations
- If iconography references Indigenous Nations, sacred locations, or culturally protected symbols:
  - treat as **requires human review**
  - document constraints and acceptable representations

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.
- Do not use AI to “invent” culturally-specific symbols.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for `src/icons/` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`