---
title: "KFM Web — API Types"
path: "web/src/api/types/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:api-types:readme:v1.0.0"
semantic_document_id: "kfm-web-api-types-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:api-types:readme:v1.0.0"
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

# KFM Web API Types

This folder defines the **TypeScript type surface** for data flowing between the **KFM web UI** and the **KFM API boundary**.

> The UI is contract-first: types in this folder must represent **contracted API payloads**, not database/graph internals.

---

## 📘 Overview

### Purpose

- Provide stable, readable TypeScript types for API requests and responses used by the web app.
- Make contract drift visible: when the API contract changes, the types here change (preferably generated).
- Preserve **provenance and evidence identifiers** so Focus Mode remains evidence-linked.

### Scope

| In Scope | Out of Scope |
|---|---|
| API request/response DTO types consumed by `web/**` | Neo4j/Cypher schemas, driver types, or graph-internal models |
| Shared primitives (IDs, timestamps, paging, error envelopes) | ETL, catalogs, graph ingest, or backend services |
| Generated types derived from API contracts | “Fixing” backend contract drift by hand-editing generated types |
| Types that carry evidence/provenance IDs and redaction flags | Storing secrets, tokens, or environment config in repo |

### Audience

- Primary: Web UI contributors working under `web/`.
- Secondary: API contributors validating payloads match contracts and maintain backward compatibility.

### Key artifacts

| Artifact | Path | Notes |
|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline ordering + invariants |
| Next stages blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Contract-first roadmap + rules |
| Redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Canonical roots + subsystem contracts |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL schemas and contract tests |
| API contract change template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Governed way to specify endpoint/query changes |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative artifacts consumed by Focus Mode |

### Definition of done

- [ ] Front-matter complete and `path` matches file location.
- [ ] Responsibilities and update workflow are documented.
- [ ] Contract-first and “no direct graph reads” invariants are stated.
- [ ] Approved H2 headings are used consistently.
- [ ] Maintainer review.

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/api/types/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| API boundary | `src/server/` | Endpoints + resolvers + redaction/generalization |
| API contracts | `src/server/contracts/` | Contract-first source of truth |
| Schemas | `schemas/` | JSON Schemas for catalogs, UI registries, telemetry |
| UI | `web/` | React + map client, Focus Mode UX |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative artifacts and assets |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Canonical evidence + provenance bundles |

### Fencing rule for this README

When adding code blocks inside this README, use triple tildes `~~~` to avoid conflicts with “outer backticks / inner tildes” fencing conventions used across KFM docs.

### Expected file tree for this sub-area

Emoji-enriched, CI-safe layout (recommended targets may be **not confirmed in repo**):

~~~text
web/
└── 📁 src/
    └── 📁 api/
        ├── 📁 types/
        │   ├── 📄 README.md                         # this file
        │   ├── 📄 index.ts                          # barrel exports (recommended; not confirmed in repo)
        │   │
        │   ├── 📁 core/                             # shared primitives
        │   │   ├── 📄 ids.ts                        # entity + evidence id aliases
        │   │   ├── 📄 datetime.ts                   # ISO datetime/date helpers
        │   │   ├── 📄 pagination.ts                 # paging cursors, limits, envelopes
        │   │   └── 📄 errors.ts                     # standard error envelopes
        │   │
        │   ├── 📁 contracts/                        # generated types from API contracts
        │   │   ├── 📁 openapi/                      # generated from REST OpenAPI (not confirmed in repo)
        │   │   └── 📁 graphql/                      # generated from GraphQL SDL (not confirmed in repo)
        │   │
        │   ├── 📁 focus_mode/                       # Focus Mode request/response types
        │   │   ├── 📄 context_bundle.ts             # provenance-linked response shape
        │   │   └── 📄 story_node_refs.ts            # Story Node references + citation handles
        │   │
        │   └── 📁 domains/                          # optional: domain-oriented DTOs
        │       ├── 📄 air_quality.ts                # example domain (not confirmed in repo)
        │       ├── 📄 soils.ts                      # example domain (not confirmed in repo)
        │       └── 📄 land_treaties.ts              # example domain (not confirmed in repo)
        │
        └── ...                                      # api client, endpoints, hooks, etc.
~~~

---

## 🧭 Context

### Pipeline placement

This folder sits at the **UI stage** of the canonical pipeline, consuming data at the **API boundary**.

- Upstream stages: ETL → STAC/DCAT/PROV → Graph → API
- Downstream surfaces: UI → Story Nodes → Focus Mode

### Contract-first boundary

- Types in this folder describe **API payloads** only.
- The UI must not query Neo4j directly.
- If the API payload shape changes, the contract and server must change first, then these types update.

### Versioning alignment

If the API is versioned (for example `v1`, `v2`), keep types aligned:

- Prefer versioned contract output directories under `types/contracts/**`.
- Breaking changes should be handled via version bumps and documented migrations, not silent type edits.

---

## 🗺️ Diagrams

### Contracts to UI types

~~~mermaid
flowchart LR
  CONTRACTS["API Contracts\nsrc/server/contracts"] --> GEN["Generated Types\nweb/src/api/types/contracts"]
  GEN --> CLIENT["API client layer\nweb/src/api"]
  CLIENT --> UI["UI components\nweb/"]
~~~

### Canonical pipeline context

~~~mermaid
flowchart LR
  ETL["ETL\nsrc/pipelines"] --> CAT["STAC/DCAT/PROV\n(data/stac · data/catalog/dcat · data/prov)"]
  CAT --> GRAPH["Graph\n(src/graph + Neo4j)"]
  GRAPH --> API["API boundary\n(src/server + contracts)"]
  API --> UI["UI types + UI app\n(web/src/api/types + web/)"]
  UI --> STORY["Story Nodes\ndocs/reports/story_nodes"]
  STORY --> FOCUS["Focus Mode\n(provenance-linked only)"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

If an endpoint feeds Focus Mode, types should support:

- **Evidence references**: stable IDs that map to STAC Items, DCAT datasets, and PROV activities.
- **Citations**: renderable citation handles and links suitable for UI display.
- **Redaction signals**: flags/notes indicating that a value was generalized or withheld.

Recommended approach:

- Model Focus Mode payloads as a **single response envelope** that bundles:
  - focused entity + related entities,
  - evidence/provenance references,
  - citations,
  - audit and redaction metadata.

The exact field names and shapes must match the API contract.

---

## 🧪 Validation & CI/CD

At minimum, changes under `web/src/api/types/` should be validated by:

- [ ] Web project type-check and build.
- [ ] Contract drift checks ensuring generated types match `src/server/contracts/`.
- [ ] Focus Mode payload types still include provenance identifiers where required.
- [ ] Security and sovereignty scans do not flag introduced content.

---

## 📦 Data & Metadata

Even though this folder is “types-only,” most KFM API payloads should carry consistent metadata patterns that the UI can rely on:

- Stable identifiers: entity IDs, dataset IDs, artifact IDs.
- Temporal metadata: `as_of`, `observed_at`, `valid_from`, `valid_to` as ISO 8601 strings.
- Spatial metadata: `bbox`, `centroid`, or geometry summaries when safe.
- Provenance: references to the generating run/activity and source assets.
- Error envelopes: machine-readable error codes + human-readable messages.

Example envelope pattern:

~~~ts
export interface ApiEnvelope<T> {
  data: T;
  as_of?: string;              // ISO 8601
  warnings?: string[];         // non-fatal warnings for UX + audit panel
  provenance?: {
    stac_item_ids?: string[];
    dcat_dataset_ids?: string[];
    prov_activity_ids?: string[];
  };
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

When API responses reference catalog/provenance artifacts, model those identifiers explicitly.

~~~ts
export type EntityId = string;

export type StacItemId = string;
export type StacCollectionId = string;

export type DcatDatasetId = string;

export type ProvActivityId = string;

export type IsoDateTime = string; // e.g., "2025-12-25T00:00:00Z"
~~~

Guideline:

- Prefer IDs and links over duplicating catalog metadata in API payloads.
- Keep payloads minimal and evidence-linked rather than “re-explaining” catalogs in the UI layer.

---

## 🧱 Architecture

### Non-negotiables

1. **No direct graph dependency**
   - Types here must not describe Cypher results or Neo4j internals.
   - The UI must consume graph-derived data only via the API boundary.

2. **Contracts are the source of truth**
   - If a payload changes, update `src/server/contracts/` and regenerate types.
   - Do not patch drift by hand-editing generated output.

3. **Generated vs hand-authored must be explicit**
   - Generated: `types/contracts/**`
   - Hand-authored: `types/core/**`, `types/focus_mode/**`, `types/domains/**`

### Type design rules

- Prefer explicit aliases over raw `string` when identifiers have semantics.
- Keep date/time values as ISO 8601 strings at the transport boundary.
- Avoid `any`. If a field is unknown, type it as `unknown` and add a TODO.
- Reflect optionality accurately: if the API can omit a field, the type must allow it.

### Updating types

#### When adding or changing an API field

1. Update the API contract and implementation at the API boundary:
   - contract artifacts live under `src/server/contracts/`
   - document the change using `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

2. Regenerate or update web types from the contract:
   - generated output should land under `web/src/api/types/contracts/**` (or equivalent)
   - do not manually edit generated files

3. Update any hand-authored DTOs or helpers in `core/`, `focus_mode/`, or `domains/` as needed.

#### Placeholder generation commands

Tooling is repo-specific. If your repo has scripts, list the actual commands here.

~~~bash
# Placeholders only — replace with repo-approved tooling.
# npm run gen:api-types
# pnpm gen:api-types
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates

- Schema or contract changes that affect public-facing payloads, provenance fields, or any sensitive data fields require governance review.
- Any change that could reveal restricted locations through interaction/zoom must be reviewed against sovereignty rules.

### CARE and sovereignty considerations

- Do not assume the UI will receive exact locations or raw sensitive attributes.
- Redaction and generalization are enforced at the API boundary.
- Types should allow fields to be omitted or generalized, and should support safe UI rendering when restricted.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial README for `web/src/api/types/` | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

