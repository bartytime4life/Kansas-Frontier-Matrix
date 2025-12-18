---
title: "KFM — tools/ Directory README"
path: "tools/README.md"
version: "v1.0.0"
last_updated: "2025-12-18"
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

doc_uuid: "urn:kfm:doc:tools:readme:v1.0.0"
semantic_document_id: "kfm-tools-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:readme:v1.0.0"
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

# KFM — tools/ directory

## 📘 Overview

### Purpose
- Define what belongs in `tools/`, how tools should be structured, and how tooling interacts with the KFM pipeline **without bypassing governed contracts**.
- Provide a single entry point for contributors (and CI) to discover and run developer utilities.

### Scope
| In Scope | Out of Scope |
|---|---|
| Developer tooling (validators, generators, migration helpers, local dev utilities) that support the pipeline | Production pipeline code (`src/pipelines/`), runtime services (`src/server/`, `web/`), and direct UI → graph access |

### Audience
- Primary: Contributors running or adding tools in this repository.
- Secondary: Reviewers verifying tooling changes comply with KFM contracts/governance.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Tool**: A script/program used to validate, generate, inspect, or migrate artifacts in the repo.
  - **Run log**: A record of tool inputs/params/versions/outputs (PROV-friendly).
  - **Governed contracts**: Schemas + APIs that mediate access between layers (catalogs → graph → APIs → UI).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Governs doc structure & metadata |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Use when tools require API contract changes |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Editorial | Use when tools generate/modify story nodes |
| Security governance | `docs/governance/ROOT_GOVERNANCE.md` | Security/Governance | Policy umbrella for tool behavior |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Tooling rules do not violate pipeline ordering or bypass contracts
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `tools/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Tools | `tools/` | Developer tooling: validators, generators, local utilities |
| Data domains | `data/` | Raw/work/processed domain data + catalogs |
| STAC/DCAT/PROV | `data/stac/` + `docs/data/` | Catalogs + mappings |
| Graph | `src/graph/` + `docs/graph/` | Ontology, labels/relations, migrations |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL/transforms + catalog build steps |
| APIs | `src/server/` + `docs/api/` | REST/GraphQL contracts + docs |
| UI | `web/` | Map UI + Focus Mode UX |
| Schemas | `schemas/` | JSON schema contracts used across layers |
| Tests | `tests/` | Automated checks for code + contracts |
| MCP | `mcp/` | Experiment templates/logs + model cards (if used) |

### Expected file tree for this sub-area
~~~text
📁 tools/
└── 📄 README.md
~~~

Recommended pattern for new tools (add only as needed):
~~~text
📁 tools/
├── 📄 README.md
├── 📁 <tool_name>/
│   ├── 📄 README.md
│   ├── 📄 <tool_name>.py
│   └── 📄 <tool_name>.schema.json   # optional: config/schema contract
└── 📁 _shared/
    └── 📄 <shared_helpers>.py
~~~

## 🧭 Context

### Background
KFM is a pipeline-oriented system. Tooling exists to:
- validate catalogs/schemas and prevent contract drift,
- generate repeatable artifacts (reports, derived indices, etc.),
- support migrations that are reviewed, reversible, and provenance-linked.

### Assumptions
- Tools run from the repository root unless a tool documents otherwise.
- Tools should be reproducible: inputs, parameters, versions, and environment should be capturable in a run log.
- Tools should be safe by default: `--help` available, and destructive actions require explicit flags and/or `--dry-run`.

### Constraints / invariants
- **Canonical ordering (non-negotiable):** ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.
- UI must consume data through **APIs** (no direct graph access from frontend).
- Tools must not introduce secrets, nor emit restricted coordinates/data in public artifacts.

### Open questions
| Question | Why it matters | Owner | Status |
|---|---|---|---|
| Preferred tool runtime (Python, Node, both)? | Packaging, dependency mgmt, CI runners | TBD | Open |
| Standard location for run logs (e.g., `mcp/experiments/`, `mcp/runs/`, tool-local output)? | Provenance + reproducibility | TBD | Open |
| Standard tool config format (YAML/JSON/flags)? | Contract stability + testability | TBD | Open |

### Future extensions
- Standardize a minimal CLI contract for tools (help/dry-run/config/output conventions).
- Add CI jobs that run critical tools against a small fixture dataset.

## 🗺 Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Developer / CI] --> T[tools/]
  T --> S[schemas/]
  T --> C[STAC/DCAT/PROV catalogs]
  C --> G[Neo4j graph]
  G --> API[APIs]
  API --> UI[React/Map UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Developer/CI
  participant Tool as Tool
  participant Catalog as Catalogs
  participant Graph as Graph
  Dev->>Tool: run (config + inputs)
  Tool->>Catalog: validate/generate
  Tool->>Graph: (only via approved loader)
  Tool-->>Dev: report + run log
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Tool config | YAML/JSON/flags (tool-defined) | Contributor/CI | Schema-validated where possible |
| Catalog artifacts | JSON | `data/stac/`, `docs/data/` | STAC/DCAT/PROV validators |
| Source/derived data | Varies | `data/` | Domain schema + range/geometry checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation report | text/JSON | tool-defined | Tool output schema (if defined) |
| Generated artifacts | varies | tool-defined | Must reference governing schema/contract |
| Run log (recommended) | JSON/YAML | tool-defined | PROV-friendly fields (inputs, versions, checksums) |

### Sensitivity & redaction
- If a tool handles sensitive locations or culturally protected sites, outputs must generalize/omit precise coordinates per sovereignty policy.
- Logs should avoid storing PII or restricted raw data.

### Quality signals
- Schema validation (JSON schema; STAC/DCAT/PROV profiles)
- Geospatial validity checks (geometry validity, CRS expectations) when applicable
- Determinism checks (fixed seeds, pinned versions) when applicable

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: TBD (tool-dependent)
- Items involved: TBD (tool-dependent)
- Extension(s): TBD (tool-dependent)

### DCAT
- Dataset identifiers: TBD
- License mapping: TBD
- Contact / publisher mapping: TBD

### PROV-O
- `prov:wasDerivedFrom`: capture upstream dataset IDs / assets
- `prov:wasGeneratedBy`: tool run ID (activity)
- Activity / Agent identities: capture author/runner + environment + tool version

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships as applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Tools | Validate/generate/migrate repo artifacts | CLI + config + run logs |
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| Catalog profiles | `data/stac/` + `docs/data/` | Profile version pinned in CI |
| API schemas | `src/server/` + `docs/api/` | Contract tests required |
| Tool interface | `tools/<tool_name>/README.md` | Document CLI/config changes |

### Extension points checklist (for future work)
- [ ] Tools: `tools/<tool_name>/README.md` exists and documents usage
- [ ] Tools: tool has deterministic mode / fixed seeds (if stochastic)
- [ ] Tools: outputs written to appropriate governed locations (data/catalog/docs)
- [ ] STAC: new/updated collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan (if applicable)
- [ ] APIs: contract version bump + tests (if applicable)
- [ ] UI: layer registry entry + access rules (if applicable)
- [ ] Focus Mode: provenance references enforced (if applicable)
- [ ] Telemetry: new signals + schema version bump (if applicable)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Tools that generate or update Story Nodes must:
  - use the governed Story Node template,
  - attach provenance identifiers for every claim,
  - avoid emitting restricted location precision.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

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
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (if tool touches graph)
- [ ] API contract tests (if tool changes API-facing artifacts)
- [ ] UI schema checks (if tool changes UI registries)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) list available tools
ls tools/

# 2) run a tool help
# python tools/<tool_name>/<tool_name>.py --help

# 3) run schema validation (if a repo command exists)
# make validate
# make test
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Tool run summary | Tool | `docs/telemetry/` + `schemas/telemetry/` |
| Validation failures | CI | CI logs |

## ⚖ FAIR+CARE & Governance

### Review gates
- Tool changes that affect catalogs, graph content, APIs, or Story Nodes require review by the relevant subsystem owners.
- Any change impacting sovereignty/sensitivity rules requires governance review per `docs/governance/`.

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- Ensure any location-bearing outputs respect generalization/redaction requirements.

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial `tools/README.md` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`