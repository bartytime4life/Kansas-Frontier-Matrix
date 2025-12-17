---
title: "Air Quality — API Lifecycle Tracking"
path: "data/air-quality/governance/api-lifecycle-tracking.md"
version: "v1.0.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:data:air-quality:governance:api-lifecycle-tracking:v1.0.0"
semantic_document_id: "kfm-air-quality-api-lifecycle-tracking-v1.0.0"
event_source_id: "ledger:kfm:doc:data:air-quality:governance:api-lifecycle-tracking:v1.0.0"
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

# Air Quality — API Lifecycle Tracking

## 📘 Overview

### Purpose
This document is a **governed registry** for tracking the **lifecycle status** of Air Quality API surfaces (REST + GraphQL), including:
- Contract versions and change history
- Deprecation and retirement timelines
- Ownership and review cadence
- Links to dataset/catalog/provenance identifiers as applicable

This document is **not** the API contract itself; it is the **index + governance log** that points to contract artifacts and approvals.

### Scope
| In Scope | Out of Scope |
|---|---|
| Lifecycle states, gates, and tracking tables for Air Quality API endpoints/queries | Implementing endpoint code (tracked elsewhere) |
| Contract change references (OpenAPI/GraphQL) and required validations | Detailed dataset ETL design (tracked in domain ETL docs/configs) |
| Deprecation / retirement scheduling + migration notes | UI changes not tied to an API lifecycle event |
| Governance and sensitivity notes for API exposure | Security policy authoring (governed in `docs/security/` / `SECURITY.md`) |

### Audience
- Primary: API maintainers, data engineers, QA/CI maintainers
- Secondary: UI engineers, Story Node authors, governance reviewers, security/sovereignty reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **API surface**: A REST endpoint or GraphQL query/mutation/type that clients depend on.
  - **Contract**: Documented and test-validated shape of a request/response (OpenAPI + JSON schema; GraphQL schema + resolver behavior).
  - **Lifecycle state**: One of the states defined in “Lifecycle taxonomy.”
  - **Breaking change**: A change that can break existing clients without changes on their side.
  - **Deprecation**: A time-bounded warning period before retirement.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This registry | `data/air-quality/governance/api-lifecycle-tracking.md` | TBD | Update on every API change release |
| API contract change doc template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | KFM governance | Use for each contract change proposal |
| API implementation | `src/server/` | TBD | REST/GraphQL implementation (not confirmed in repo: exact layout per subsystem) |
| API docs | `docs/` | TBD | Location varies; link contract docs from here |
| Schemas | `schemas/` | TBD | JSON schema profiles, telemetry schemas, etc. |
| Tests | `tests/` | TBD | Contract + integration tests |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Every listed API surface includes: owner, lifecycle state, and contract reference
- [ ] Deprecations include: replacement pointer + timeline + migration note
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No secrets, credentials, or sensitive locations are included

## 🗂️ Directory Layout

### This document
- `path`: `data/air-quality/governance/api-lifecycle-tracking.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Air Quality domain | `data/air-quality/` | Domain data + governance artifacts |
| Data lifecycle staging | `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` | Canonical staging (confirm exact domain scoping in repo) |
| APIs | `src/server/` + docs | Contracted access layer (REST/GraphQL) |
| Schemas | `schemas/` | JSON schema artifacts + validation targets |
| Tests | `tests/` | Unit/integration/contract tests |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Governance observability signals |

### Expected file tree (for this sub-area)
~~~text
📁 data/
└── 📁 air-quality/
    └── 📁 governance/
        └── 📄 api-lifecycle-tracking.md
~~~

## 🧭 Context

### Background
KFM enforces a non-negotiable pipeline order:
ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode.

This registry exists to ensure Air Quality APIs:
- remain contract-driven,
- are versioned and test-validated, and
- do not expose sensitive details by accident.

### Assumptions
- Air Quality data products are discoverable via STAC/DCAT and have PROV lineage records.
- Air Quality API surfaces will be consumed by UI and/or Focus Mode experiences.
- “How the API is versioned” (path prefix, header, semver tags, GraphQL schema versioning) is **not confirmed in repo**; this registry tracks whichever mechanism is used.

### Constraints / invariants
- The frontend must consume data via the API layer (no direct graph access).
- API changes must be either backward compatible or require an explicit version bump + migration notes (**not confirmed in repo**: exact versioning mechanism; confirmed: “do not break” contract rule applies).
- Sensitive or restricted content (including sensitive locations) must be generalized or omitted per governance.
- This registry must stay current: update as part of the same PR that changes the API contract.

### Open questions
- What is the authoritative contract location for REST (OpenAPI JSON/YAML path) and GraphQL schema snapshots? (**not confirmed in repo**)
- What is the default deprecation window for client migration? (**not confirmed in repo**)
- Which Air Quality entities are “focusable” in Focus Mode? (**not confirmed in repo**)

### Future extensions (tracked here; details in subsystem docs)
- Add a machine-readable lifecycle registry (YAML/JSON) for CI enforcement (optional).
- Add automated checks: “no deprecated endpoint is undocumented,” “no retired endpoint remains reachable.”
- Integrate STAC API discovery endpoints if adopted for Air Quality datasets (optional; not confirmed in repo).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  subgraph Data
    A["Air Quality Raw Sources"] --> B["ETL + Normalization"]
    B --> C["STAC Items + Collections"]
    C --> D["DCAT Dataset Views"]
    C --> E["PROV Lineage Bundles"]
  end

  C --> G["Neo4j Graph"]
  G --> H["Air Quality API Layer"]
  H --> I["Map UI / Clients"]
  I --> J["Story Nodes"]
  J --> K["Focus Mode"]
~~~

### API lifecycle state machine (registry semantics)
~~~mermaid
stateDiagram-v2
  [*] --> Proposed

  Proposed --> Draft: intake approved
  Draft --> Alpha: contract stub + initial impl
  Alpha --> Beta: contract tests + integration tests
  Beta --> Stable: docs + telemetry + governance gates
  Stable --> Deprecated: deprecation notice issued
  Deprecated --> Retired: retirement window complete

  Draft --> Proposed: rejected / deferred
  Beta --> Draft: rollback to redesign
  Stable --> Beta: regression / breaking issue
~~~

### Optional: sequence diagram (Focus Mode context query)
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id, time_window)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Contract change proposal | Markdown | PR description + contract doc | Review + template compliance |
| REST contract snapshot | OpenAPI (YAML/JSON) | `src/server/` + docs | Contract tests required |
| GraphQL schema snapshot | SDL / docs | `src/server/` + docs | Schema lint + resolver tests |
| Integration test results | CI logs | `tests/` | Pass/fail gating |
| Deprecation notice | Markdown | `docs/` or release notes | Required fields present |
| Telemetry metrics | JSON/logs | API observability | Schema versioned |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Lifecycle tracking registry | Markdown | `data/air-quality/governance/api-lifecycle-tracking.md` | Markdown protocol checks |
| Deprecation + migration notes | Markdown | `docs/` (location TBD) | Required fields present |
| Optional lifecycle registry | YAML/JSON | TBD | Schema-validated (future) |

### Sensitivity & redaction
- This document should not include secrets (keys, tokens), private URLs, or internal-only endpoints.
- If an API surface can return sensitive locations (e.g., exact sensor placements on sensitive sites), the lifecycle registry **must** flag it as “restricted” and note the redaction/generalization approach.

### Quality signals
- Contract coverage: every public endpoint/query listed here and in OpenAPI/GraphQL docs
- Test coverage: contract tests + integration tests present for each stable API surface
- Deprecation hygiene: deprecated surfaces have replacement + dates; retired surfaces removed
- Governance hygiene: restricted/sensitive surfaces have an explicit handling note

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: **not confirmed in repo** (list Air Quality collection IDs once established)
- Items involved: **not confirmed in repo**
- Extension(s): **not confirmed in repo**
- Registry rule: each API surface should reference the STAC Collection(s)/Item types it exposes.

### DCAT
- Dataset identifiers: **not confirmed in repo**
- License mapping: TBD
- Contact / publisher mapping: TBD

### PROV-O
- `prov:wasDerivedFrom`: identify upstream datasets (STAC item/collection IDs where possible)
- `prov:wasGeneratedBy`: identify ETL/transforms that produced derived/aggregated outputs
- Activity / Agent identities: record run IDs and tool IDs where applicable
- Registry rule: stable API surfaces should allow clients to trace outputs back to provenance identifiers.

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.
- API versioning mechanism is **not confirmed in repo**; track the mechanism used (endpoint version, header, schema version tag, etc.) per surface.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize Air Quality sources | Config + run logs |
| Catalogs | STAC/DCAT/PROV entries for Air Quality datasets | JSON + validator |
| Graph | Neo4j semantic layer for air-quality entities | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative clients | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/cesium/layers/regions.json` | Schema-validated |

### Lifecycle taxonomy (Air Quality API surfaces)
| State | Meaning | Minimum requirements (gate) |
|---|---|---|
| Proposed | Idea captured, not implemented | Tracking row exists + owner assigned |
| Draft | Intended behavior drafted | Contract change doc started (template) |
| Alpha | Implemented for internal use | Contract stub + basic tests (not confirmed: exact thresholds) |
| Beta | Feature complete, stabilizing | Contract tests + integration tests passing |
| Stable | Supported for external clients | Docs published + telemetry + governance review |
| Deprecated | Replacement exists | Deprecation notice + retirement date recorded |
| Retired | Removed from service | Endpoint/query removed + docs updated |

### Lifecycle registry (current Air Quality API surfaces)
> Fill this table as endpoints/queries are implemented. If unknown, keep as `TBD`.

| Surface | Route / Query | Contract ref (operationId / schema) | Introduced | Current version | State | STAC/DCAT refs | Sensitivity | Owner | Last reviewed | Deprecates | Retires | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REST | TBD | TBD | TBD | TBD | Proposed | TBD | public | TBD | TBD | TBD | TBD | not confirmed in repo |
| GraphQL | TBD | TBD | TBD | TBD | Proposed | TBD | public | TBD | TBD | TBD | TBD | not confirmed in repo |

### Lifecycle events log (changes, releases, deprecations)
| Date | Change ID (link) | Type | Affected surfaces | Version action | Migration note | Approver(s) |
|---|---|---|---|---|---|---|
| 2025-12-17 | TBD | Initial | TBD | n/a | n/a | TBD |

### Deprecation checklist (when moving to Deprecated)
- [ ] Replacement identified (new route/query or alternative workflow)
- [ ] Deprecation notice authored (what/why/when/how to migrate)
- [ ] Retirement date assigned
- [ ] Client comms plan recorded (**not confirmed in repo**: where comms are tracked)
- [ ] Runtime warnings/headers added if applicable (**not confirmed in repo**)
- [ ] Metrics added for deprecated surface usage (telemetry)

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- What entities become focusable?
  - Example candidates (not confirmed in repo): station/sensor entities, observations, time-window aggregates, region summaries.
- What evidence must be shown?
  - Provenance references to STAC items + PROV activities used to produce values returned by APIs.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "air_quality_observations"
focus_time: "YYYY-MM-DD/YYYY-MM-DD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)
- [ ] Lifecycle registry updated in same change as contract update (gate)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run contract tests (OpenAPI/GraphQL)
# 4) run doc lint / markdown protocol checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| air_quality_api_contract_version | CI + API build | `docs/telemetry/` + `schemas/telemetry/` |
| air_quality_api_deprecation_warnings | API runtime | `docs/telemetry/` + `schemas/telemetry/` |
| air_quality_api_redaction_applied_count | API runtime | `docs/telemetry/` + `schemas/telemetry/` |
| air_quality_api_error_rate | API runtime | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Who approves changes?
  - **not confirmed in repo** — follow `docs/governance/ROOT_GOVERNANCE.md` roles/process.
- What requires council/board sign-off?
  - Any change that expands access to sensitive/restricted information.

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- If Air Quality sources or sensors relate to sovereignty-controlled areas, ensure:
  - appropriate aggregation/generalization, and
  - access rules aligned to `docs/governance/SOVEREIGNTY.md`.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.
- Do not use AI outputs to infer sensitive locations or generate new policy beyond governed standards.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial Air Quality API lifecycle tracking registry | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
