---
title: "web/src/utils/contracts — UI Contract Utilities (README)"
path: "web/src/utils/contracts/README.md"
version: "v0.1.0-draft"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:web:contracts:readme:v0.1.0-draft"
semantic_document_id: "kfm-web-contracts-readme-v0.1.0-draft"
event_source_id: "ledger:kfm:doc:web:contracts:readme:v0.1.0-draft"
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

# web/src/utils/contracts/ — UI Contract Utilities

## 📘 Overview

### Purpose

- Provide a single, UI-local home for **contract consumption**:
  - typed request/response interfaces for API calls,
  - runtime validation/decoding at the UI boundary (recommended),
  - adapters that map contracted payloads into UI view-models.
- Make “no UI direct-to-graph reads” easy to uphold by ensuring **all graph-shaped data enters the UI via API contracts**, not via Neo4j drivers.

### Scope

| In Scope | Out of Scope |
|---|---|
| UI-side *consumption* of contracted payloads (API + catalog responses) | Defining canonical API contracts (belongs in `src/server/contracts/**`) |
| Runtime decoding/validation helpers (recommended) | Implementing server endpoints or Neo4j queries |
| Small, pure mapping functions to UI view-models | Storing dataset outputs or catalog artifacts (belongs under `data/**`) |

### Audience

- Primary: `web/` contributors consuming API + catalog data in React views.
- Secondary: API/contract owners verifying UI contract compliance.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: contract-first, API boundary, STAC, DCAT, PROV, Focus Mode, redaction, generalization.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline invariants) | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline ordering and non-negotiables |
| API contracts (canonical) | `src/server/contracts/**` | API owners | OpenAPI / GraphQL schemas; semver + contract tests |
| Validation schemas (canonical) | `schemas/**` | Contracts owners | Includes `schemas/ui/**`, `schemas/stac/**`, `schemas/dcat/**`, `schemas/prov/**` *(schema families may vary; not confirmed in repo)* |
| Story Nodes (canonical) | `docs/reports/story_nodes/` | Curators | Narrative artifacts that must be provenance-linked |
| This README | `web/src/utils/contracts/README.md` | Web maintainers | UI-side contract consumption rules + layout |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] `path` matches file location
- [ ] Placement rules reflect the canonical pipeline (ETL → catalogs → graph → API → UI → Story Nodes → Focus Mode)
- [ ] Clear rules for handling contract violations + sensitive fields
- [ ] Validation steps listed and repeatable (even if placeholder commands)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/utils/contracts/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| ETL / pipelines | `src/pipelines/` | Deterministic ingest + transforms |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts (evidence + lineage) |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings, graph build, import fixtures |
| API boundary | `src/server/` | REST/GraphQL services + redaction/generalization enforcement |
| API contracts | `src/server/contracts/` | OpenAPI / GraphQL schemas used by API and tests |
| Schemas | `schemas/` | JSON Schemas and constraint bundles used by CI + validators |
| UI | `web/` | React map/narrative UI (must not query Neo4j directly) |

### Expected file tree for this sub-area

> Note: Subfolders/files below are a **recommended** structure to keep contract usage consistent.  
> If they do not exist yet, treat them as extension points (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    └── 📁 utils/
        └── 📁 contracts/
            ├── 📄 README.md
            ├── 📄 index.ts                      (barrel exports) *(not confirmed in repo)*
            ├── 📁 api/                          (API payload types + decoders) *(not confirmed in repo)*
            ├── 📁 catalogs/                     (STAC/DCAT/PROV helpers) *(not confirmed in repo)*
            ├── 📁 story_nodes/                  (Story Node front-matter parsing) *(not confirmed in repo)*
            └── 📁 ui/                           (UI registry validation) *(not confirmed in repo)*
~~~

## 🧭 Context

### Background

KFM is intentionally staged to preserve auditability:

**ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**

The UI is a React-based map + narrative client that **must not connect to Neo4j directly**; all graph access happens through the API boundary.

### Constraints / invariants

- **No UI direct-to-graph reads:** `web/` must never import Neo4j drivers, embed Cypher, or use Neo4j credentials.
- **Contracts are canonical:** schemas/specs live in `schemas/`; API contracts live in `src/server/contracts/` and should validate in CI.
- **Focus Mode is provenance-linked only:** narrative views must show evidence IDs and respect redaction/generalization flags.
- **Do not unmask generalized locations:** if a payload includes generalization metadata (e.g., `kfm:locationGeneralization`), UI must not reconstruct precise locations.

### Open questions (**not confirmed in repo**)

| Question | Why it matters | Owner |
|---|---|---|
| Do we generate TypeScript types from OpenAPI/GraphQL in CI? | Prevents drift between API and UI | TBD |
| What is the preferred runtime validator (e.g., JSON Schema validator vs Zod/io-ts)? | Determines how strict UI validation can be | TBD |
| Where do UI telemetry events live / how are they emitted? | Needed to report contract violations safely | TBD |

## 🗺️ Diagrams

### Where UI contract utilities sit in the canonical pipeline

~~~mermaid
flowchart LR
  P[ETL<br/>src/pipelines] --> C[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  C --> G[Graph<br/>src/graph + data/graph]
  G --> A[API Boundary<br/>src/server]
  A --> U[UI<br/>web]
  U --> S[Story Nodes<br/>docs/reports/story_nodes]
  S --> F[Focus Mode<br/>provenance-linked only]

  U --> CU[Contract utilities<br/>web/src/utils/contracts]
  CU -. validates/decodes .-> A
  CU -. validates/decodes .-> C
~~~

### Request → validate → render

~~~mermaid
sequenceDiagram
  participant UI as UI Component
  participant CU as contracts/*
  participant API as API (src/server)

  UI->>API: fetch(...)
  API-->>UI: JSON payload
  UI->>CU: decode(payload)
  alt Valid
    CU-->>UI: typed + normalized view-model
    UI-->>UI: render
  else Invalid / unexpected
    CU-->>UI: typed error (contract violation)
    UI-->>UI: show safe fallback + log telemetry (no PII)
  end
~~~

## 🧠 Story Node & Focus Mode Integration

### How this folder supports Focus Mode

- Ensure Focus Mode inputs are **evidence-first**:
  - surface STAC IDs, PROV run/activity IDs, and dataset identifiers whenever present.
- Ensure Focus Mode outputs are **safe**:
  - respect location generalization/redaction flags,
  - avoid rendering interactive UI affordances that could reveal restricted locations by zoom/hover.

### Provenance-linked narrative rule

- If the UI renders Story Nodes or Focus Mode narratives, every factual claim must be traceable to an evidence identifier or API-provided citation bundle. *(Narrative authoring rules live with Story Node templates and validation.)*

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Typecheck/lint the `web/` app (tooling **not confirmed in repo**)
- [ ] Ensure **no Neo4j client usage** in `web/` (static scan for imports/URLs like `neo4j://`)
- [ ] Ensure API contract versions are compatible with UI consumption (contract tests belong to API; UI should pin + update)
- [ ] Validate UI registry JSON against `schemas/ui/**` where applicable
- [ ] Validate any consumed STAC/DCAT/PROV payload shapes against canonical schema families (if the UI loads them directly)

### Reproduction (placeholders — replace with repo commands)

~~~bash
# Example placeholders — replace with repo-specific commands

# UI
# npm run lint
# npm run typecheck
# npm test

# Optional: scan for forbidden graph access in UI bundle/source
# rg -n "neo4j://|neo4j-driver|cypher" web/
~~~

## 📦 Data & Metadata

### Inputs

| Input | Typical source | Contract authority | Notes |
|---|---|---|---|
| API JSON responses | `src/server/` endpoints | `src/server/contracts/**` | Canonical |
| UI registry JSON | `web/**` | `schemas/ui/**` | Should validate |
| STAC/DCAT/PROV artifacts (if UI reads them) | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | `schemas/stac/**`, `schemas/dcat/**`, `schemas/prov/**` | Prefer serving via API when possible |

### Outputs

| Output | Who uses it | Notes |
|---|---|---|
| Typed view-models | React components | Prefer pure functions |
| Contract violation errors | Error boundary / telemetry | Must not include secrets/PII |
| “Generalized location” notices | Focus Mode + map UI | Required when precision is reduced |

### Sensitivity & redaction

- Treat redaction/generalization as **authoritative** when it comes from the API boundary.
- Do not attempt to reconstruct restricted values from nearby public data.
- Avoid UI behaviors that can inadvertently reveal restricted locations (e.g., high-precision hover tooltips, deep-linking to exact coordinates) unless explicitly permitted by governance docs.

## 🌐 STAC, DCAT & PROV Alignment

- Prefer that the API boundary provides catalog-derived content in UI-friendly contracts.
- When the UI must consume STAC/DCAT/PROV payloads directly:
  - validate shape and required fields,
  - preserve and surface stable identifiers (STAC item IDs, DCAT dataset IDs, PROV activity IDs),
  - avoid rewriting identifiers in ways that break provenance links.

## 🧱 Architecture

### What belongs here

- “Edge” helpers that make contracted payload consumption safe and consistent:
  - request/response types (generated or handwritten),
  - runtime decoding/validation,
  - mapping functions from contract payload → UI view state.

### What does not belong here

- Neo4j access code, Cypher strings, graph credentials.
- Server-side contract definitions (canonical home: `src/server/contracts/**`).
- Domain data outputs or catalog artifacts (canonical home: `data/**`).

### Example pattern (library-agnostic)

~~~ts
// PSEUDO-CODE ONLY — choose the repo's preferred validator (not confirmed in repo)

export type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: { code: "CONTRACT_VIOLATION"; message: string; details?: unknown } };

export function decodeExamplePayload(input: unknown): Result<{ id: string }> {
  if (!input || typeof input !== "object") {
    return { ok: false, error: { code: "CONTRACT_VIOLATION", message: "Expected object" } };
  }
  const obj = input as Record<string, unknown>;
  if (typeof obj.id !== "string") {
    return { ok: false, error: { code: "CONTRACT_VIOLATION", message: "Expected id: string" } };
  }
  return { ok: true, value: { id: obj.id } };
}
~~~

### Extension points checklist (UI-side)

- [ ] API change consumed in UI: update decoders/types in this folder
- [ ] New UI registry schema: update validators + ensure `schemas/ui/**` exists/updated
- [ ] New Focus Mode field: ensure provenance IDs are displayed and redaction respected
- [ ] New domain layer: ensure UI can access via API (no dark data) and validation passes

## ⚖ FAIR+CARE & Governance

### Review gates

- Governance review recommended when:
  - introducing UI features that could reveal sensitive locations by interaction/zoom,
  - changing how generalized/redacted fields are displayed,
  - emitting new telemetry fields that might include sensitive data.

### CARE / sovereignty considerations

- If a dataset intersects with sovereignty-controlled areas or culturally sensitive sites:
  - prefer coarse/aggregate representation,
  - ensure UI respects API-provided generalization/redaction flags,
  - document decisions in governance docs referenced above.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy text; inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author | PR / Issue |
|---|---:|---|---|---|
| v0.1.0-draft | 2025-12-26 | Initial README scaffold for UI contract utilities | TBD | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Next stages blueprint (if adopted): `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` *(path not confirmed in repo)*
- v13 blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(path not confirmed in repo)*
- API Contract Extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`

---

