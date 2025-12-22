---
title: "Web UI Utilities — web/src/utils"
path: "web/src/utils/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:web:utils:readme:v1.0.0"
semantic_document_id: "kfm-web-utils-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:utils:readme:v1.0.0"
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

# Web UI Utilities

## 📘 Overview

### Purpose

`web/src/utils/` is the shared utility layer for the KFM web UI. It exists to:

- centralize small, reusable helper functions used across UI features
- keep transformations deterministic and easy to test
- preserve KFM’s provenance-first UX by preventing “helpful” UI code from silently dropping evidence context

### Scope

In scope:

- pure or side-effect-limited helpers (formatting, parsing, small data transforms)
- small wrappers that standardize browser APIs (only when necessary and safe)
- “glue code” that adapts API responses into UI-ready structures without changing meaning

Out of scope:

- direct graph access (Neo4j) or “hidden” graph querying
- API client modules that own authentication, retries, or caching policies
- React components, hooks, or state management modules (keep utilities as simple leaf dependencies)
- anything that fabricates citations, provenance, or narrative claims

### Audience

- UI engineers working in `web/`
- API engineers verifying UI-boundary invariants and provenance flows
- reviewers assessing whether UI changes preserve governance and redaction guarantees

### Definitions

- Link: `docs/glossary.md`
- Key terms used here: **API boundary**, **provenance**, **evidence**, **Focus Mode**, **Story Node**

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline guide | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline and invariants |
| UI boundary constraints | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture Team | “No UI direct-to-graph reads” and provenance-first UX |
| API contracts | `src/server/contracts/` | API Team | UI consumes graph + catalogs via APIs only |
| UI schemas | `schemas/ui/` | UI + Contracts owners | Layer/registry validation and UI artifact contracts |

### Definition of done

- [ ] Front-matter complete and path matches file location
- [ ] Utilities added here do not violate UI boundary constraints
- [ ] Provenance/evidence fields are preserved when transforming API responses
- [ ] Any new utility has a clear owner and usage examples
- [ ] Sensitive or restricted data is not logged, re-derived, or re-exposed

## 🗂️ Directory Layout

### This document

- `path`: `web/src/utils/README.md`

### Related repository paths

| Area | Path | Notes |
|---|---|---|
| UI app | `web/` | React/map UI lives here |
| API boundary | `src/server/` | All graph access occurs here |
| UI contracts | `schemas/ui/` | UI schema validation lives here |
| Story Nodes | `docs/reports/story_nodes/` | Provenance-linked narrative artifacts |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 src/
    └── 📁 utils/
        └── 📄 README.md
~~~

## 🧭 Context

### Background

KFM is contract-first and evidence-first. The UI sits behind an API boundary and must respect provenance and redaction. Utilities in this folder must make it easier (not easier to bypass) those constraints.

### Assumptions

- The web UI is the canonical front-end under `web/`.
- Graph and catalog data is consumed through API endpoints and catalog endpoints, not through direct DB access.
- The UI must be able to render provenance-linked context for Focus Mode and Story Nodes.

### Constraints / invariants

Non-negotiables for anything in `web/src/utils/`:

1. **No UI direct-to-graph reads**
   - Utilities must not create Neo4j connections, embed Cypher, or call graph endpoints that bypass `src/server/`.
2. **No unsourced narrative**
   - Utilities must not generate narrative claims or citations that are not present in upstream evidence.
3. **Contracts are canonical**
   - If a utility depends on response shapes, prefer contract-driven structures (OpenAPI/GraphQL + schema-validated payloads).
4. **Redaction is respected**
   - Do not attempt to “reconstruct” redacted or generalized content (including sensitive coordinates or identifiers).

### Open questions

- Should this directory be split into topic subfolders (for example: formatting, provenance, geo) once it grows beyond a single screen?
- Do we want a formal “allowed imports” rule to keep `utils/` as leaf dependencies?

### Future extensions

- Add a lightweight “utility checklist” snippet for PRs (purity, tests, provenance preservation, no logging of sensitive data).
- Add schema-aware helpers for rendering evidence and citations consistently in Focus Mode.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  U[web/src/utils] --> UI[Web UI]
  UI --> API[src/server APIs]
  API --> G[Neo4j Graph]
  API --> C[STAC/DCAT/PROV catalogs]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant U as utils
  participant API as API boundary (src/server)
  participant G as Neo4j
  UI->>API: Request (query, filters)
  API->>G: Graph query
  API-->>UI: Response with provenance/evidence
  UI->>U: Transform for rendering (preserve provenance)
  U-->>UI: UI-ready view model
~~~

## 📦 Data & Metadata

### Inputs

Typical utility inputs include:

- API response objects (already redacted/generalized as needed)
- catalog-derived JSON objects (STAC/DCAT/PROV payloads, when exposed via API)
- UI state values (filters, view params) that do not contain restricted data

### Outputs

- formatted strings, computed display values, UI-friendly view models
- safe parsing/normalization results
- stable identifiers for UI rendering keys and UI registry lookups

### Sensitivity & redaction

- Do not log raw payloads that might contain sensitive data.
- If a utility must emit debug output, ensure it is safe-by-default and strips sensitive fields.

### Quality signals

- Prefer deterministic, side-effect-free utilities.
- Prefer small functions with narrow responsibilities.
- If a utility is reused across features, document it in this README with a short example.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Utilities that handle STAC payloads should treat IDs/links as evidence references and avoid rewriting identifiers.

### DCAT

- Utilities that map DCAT metadata into UI views must preserve dataset identifiers and license fields.

### PROV-O

- Utilities must not “invent” provenance. If PROV fields are missing, surface that absence explicitly in UI state rather than fabricating defaults.

### Versioning

- If a utility becomes widely used, treat signature changes as breaking and coordinate with UI/API contracts.

## 🧱 Architecture

### Components

Keep `utils/` as a low-level dependency layer. As a rule of thumb:

- `utils/` should be importable without pulling in the whole app.
- avoid circular dependencies between feature modules and utilities.

### Interfaces / contracts

- Prefer consuming API-contract-shaped objects.
- When a transform is needed, document which contract it expects (OpenAPI schema name, GraphQL type, etc.) in code comments near the transform.

### Extension points checklist

- [ ] Does the utility preserve provenance/evidence references?
- [ ] Does it avoid direct graph access?
- [ ] Does it avoid logging or exposing sensitive information?
- [ ] Is it deterministic and unit-testable?
- [ ] Is its name descriptive and stable?

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

Utilities may be used to:

- format citations and evidence badges
- group or filter provenance-linked entities for display
- normalize UI state in ways that keep provenance visible

### Provenance-linked narrative rule

If a utility touches narrative display, it must ensure:

- every claim shown in Focus Mode is traceable to evidence identifiers provided upstream
- “missing evidence” is displayed as missing, not silently filled in

### Optional structured controls

If Focus Mode controls consume structured metadata (filters, provenance facets), utilities should:

- keep the control state serializable
- preserve stable IDs so UI state can be reproduced and audited

## 🧪 Validation & CI/CD

### Validation steps

- Validate that changes do not introduce forbidden access paths (e.g., direct graph queries).
- Add unit tests for utilities that handle provenance, parsing, or identifiers.

### Reproduction

- Run the web app’s standard lint/test pipeline.
- Ensure a clean build when importing utilities across UI modules.

# Example placeholders — replace with repo-specific commands

~~~sh
# Replace these with the repo's actual web commands
# (commands and package manager are intentionally not specified here).
#
# <web-lint-command>
# <web-test-command>
# <web-build-command>
~~~

### Telemetry signals

If performance or UX telemetry exists, utilities should avoid:

- expensive work on hot render paths
- unbounded loops over large payloads without pagination/virtualization upstream

## ⚖ FAIR+CARE & Governance

### Review gates

Requires human review if a change:

- alters provenance rendering logic
- changes how redaction/generalization is displayed
- introduces new logging of payload fields
- adds new “helper” transforms that could be interpreted as narrative claims

### CARE / sovereignty considerations

- Do not add UI utilities that could increase the risk of re-identification (for example, reverse-mapping generalized coordinates).
- Treat restricted layers and restricted entities as “not for display” unless the UI receives explicit permission via API contracts and governance rules.

### AI usage constraints

- Do not generate policy text in UI utilities.
- Do not infer sensitive locations.
- If AI-derived summaries are displayed, ensure uncertainty and provenance are visible and not buried.

## 🕰️ Version History

- v1.0.0 (2025-12-22): Initial `web/src/utils/` README with UI-boundary and provenance-first constraints.
