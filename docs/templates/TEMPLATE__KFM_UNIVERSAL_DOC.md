~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FILE: docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---
title: "TEMPLATE — KFM Universal Governed Doc"
path: "docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "template"
doc_kind: "Template"
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

doc_uuid: "urn:kfm:doc:templates:universal-doc:v1.0.0"
semantic_document_id: "kfm-template-universal-doc-v1.0.0"
event_source_id: "ledger:kfm:doc:templates:universal-doc:v1.0.0"
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

# TEMPLATE — KFM Universal Governed Doc

## 📘 Overview

### Purpose
- What this document is for (1–3 sentences).
- What decisions or contracts it governs.

### Scope
| In Scope | Out of Scope |
|---|---|
| TBD | TBD |

### Audience
- Primary: …
- Secondary: …

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: …

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
<add-tree-here>
~~~

## 🧭 Context

### Background
- What problem exists today?
- Why now?

### Assumptions
- …

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| TBD | TBD | TBD |

### Future extensions
- Extension point A: …
- Extension point B: …

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

### Sensitivity & redaction
- Identify any fields requiring generalization or omission for public outputs.

### Quality signals
- Define quality checks (completeness, ranges, geometry validity, etc.).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: …
- Items involved: …
- Extension(s): …

### DCAT
- Dataset identifiers: …
- License mapping: …
- Contact / publisher mapping: …

### PROV-O
- `prov:wasDerivedFrom`: …
- `prov:wasGeneratedBy`: …
- Activity / Agent identities: …

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
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
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/cesium/layers/regions.json` | Schema-validated |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
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
- What evidence must be shown?

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
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Who approves changes?
- What requires council/board sign-off?

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial template | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FILE: docs/MASTER_GUIDE_v12.md
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---
title: "Kansas Frontier Matrix — Master Guide v12 (Draft)"
path: "docs/MASTER_GUIDE_v12.md"
version: "v12.0.0-draft"
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

doc_uuid: "urn:kfm:doc:master-guide:v12.0.0-draft"
semantic_document_id: "kfm-master-guide-v12.0.0-draft"
event_source_id: "ledger:kfm:doc:master-guide:v12.0.0-draft"
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

# Kansas Frontier Matrix — Master Guide v12 (Draft)

## 📘 Overview

### What KFM is (one paragraph)
- A geospatial + historical knowledge system with governed data, catalogs, graph semantics, APIs, and a map/narrative UI.

### The canonical pipeline (non-negotiable ordering)
- ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

### What “v12 evolution” means
- A documentation + contracts evolution that:
  - Keeps v11 artifacts stable
  - Adds explicit extension points for new data domains, AI evidence products, and narrative UX

### System inventory (index)
| System / Area | Canonical location | What it governs |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac organization per domain |
| STAC/DCAT/PROV | `data/stac/` + `docs/data/` | Catalog generation + mappings |
| Graph | `src/graph/` + `docs/graph/` | Ontology, labels, relationships, migrations |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL, transforms, catalog build, graph build |
| APIs | `src/server/` + docs | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` + `docs/design/` | Map layers, Focus Mode UX, a11y |
| Story Nodes | `docs/reports/.../story_nodes/` + graph | Narrative artifacts with provenance |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Observability, security, governance metrics |
| Security | `.github/SECURITY.md` + `docs/security/` | Policy + technical standards |
| MCP | `mcp/` + `docs/templates/` | Experiments, model cards, SOPs |

### “Extension Matrix” (how new capabilities get added)
| Extension | Data | Catalog | Graph | API | UI | Story/Focus | Telemetry |
|---|---|---|---|---|---|---|---|
| New dataset | ✓ | ✓ | optional | optional | optional | optional | optional |
| New analysis product (e.g., evidence artifacts) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| New narrative node type | optional | optional | ✓ | ✓ | ✓ | ✓ | ✓ |
| New security gate | — | — | — | — | — | — | ✓ |

## 🗂️ Directory Layout

### Repo top-levels (expected)
~~~text
.github/
data/
docs/
mcp/
schemas/
src/
tests/
tools/
web/
releases/
~~~

### Documentation map
- `docs/MASTER_GUIDE_v11.md` (current baseline)
- `docs/MASTER_GUIDE_v12.md` (this draft)
- `docs/standards/` (governed standards, including KFM-MDP)
- `docs/templates/` (document + MCP templates)

## 🧭 Context

### What’s driving the next evolution
- Scaling: more domains, more evidence products, more narrative interactivity.
- Governance: stronger provenance + sovereignty enforcement as content grows.

### Key invariants
- No unsourced narrative in Focus Mode contexts.
- Provenance is first-class (STAC/DCAT/PROV and graph lineage).
- Reproducibility and deterministic pipelines.

### Future extensions (tracked here; details in subsystem docs)
- WDE-style discovery outputs (candidate sites, evidence panels, provenance-linked assets)
- More telemetry governance signals (security posture, energy/carbon for workloads)
- Expanded story node ingestion and versioning

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph Data
    A[Raw Sources] --> B[ETL + Normalization]
    B --> C[STAC Items + Collections]
    C --> D[DCAT Dataset Views]
    C --> E[PROV Lineage Bundles]
  end

  C --> G[Neo4j Graph]
  G --> H[API Layer]
  H --> I[Map UI (React/MapLibre/Cesium)]
  I --> J[Story Nodes]
  J --> K[Focus Mode]
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)
- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ `data/reports/` outputs as needed)

### Domain expansion pattern
- New domains go under `data/<domain>/...`
- New domain docs go under `docs/<domain>/...` or `docs/data/<domain>/...` (choose one canonical location and link)

## 🌐 STAC, DCAT & PROV Alignment

### STAC/DCAT/PROV alignment policy (how to document)
- Every new dataset must have:
  - STAC Collection + Item(s)
  - DCAT mapping (minimum title/description/license/keywords)
  - PROV activity for the transform that generated it

### Versioning expectations
- New versions link predecessor/successor
- Graph mirrors version lineage

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)
| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Next-evolution extension points
- (A) Data: new domain, new STAC extension profiles
- (B) AI evidence: artifacts as STAC assets, linked into Focus Mode
- (C) Graph: new entity types (e.g., candidate sites) with explicit provenance
- (D) API: new endpoints with contract tests and redaction policies
- (E) UI: new layer registry entries with provenance pointers and CARE gating

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”
- Story Nodes must carry provenance annotations and connect to graph entities.

### Focus Mode rule
- Focus Mode only consumes provenance-linked content.
- Any predictive content must be opt-in and carry uncertainty / confidence metadata.

## 🧪 Validation & CI/CD

### Minimum CI gates for “v12-ready” contributions
- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)

## ⚖ FAIR+CARE & Governance

### Governance review triggers
- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### Sovereignty safety
- Document redaction/generalization rules for any restricted locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v12.0.0-draft | 2025-12-17 | Initial scaffolding | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FILE: docs/templates/TEMPLATE__STORY_NODE_V3.md
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---
title: "TEMPLATE — Story Node v3"
path: "docs/templates/TEMPLATE__STORY_NODE_V3.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "template"
doc_kind: "Template"
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

doc_uuid: "urn:kfm:doc:templates:story-node-v3:v1.0.0"
semantic_document_id: "kfm-template-story-node-v3-v1.0.0"
event_source_id: "ledger:kfm:doc:templates:story-node-v3:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
ai_transform_prohibited:
  - "speculative_additions"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# TEMPLATE — Story Node v3

## 📘 Overview

### Title
- (Short, human-readable)

### Narrative (factual + source-linked)
- Write in neutral, evidence-led tone.
- Every factual claim must map to a cited dataset/document ID.

### Key entities (graph linkage)
| Entity type | Canonical name / ID | Relationship |
|---|---|---|
| Place | TBD | ABOUT |
| Event | TBD | ABOUT |
| Person/Org | TBD | RELATED |

## 🗂️ Directory Layout

### Where the story node lives
- Markdown: (path)
- Graph node ID: (if applicable)
- STAC item(s): (IDs)

## 🧭 Context

### Why this story node exists
- What question it helps answer in Focus Mode.

### Sensitivity considerations
- If sensitive: describe generalization/redaction expected.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Primary source item(s)] --> B[Extraction/curation activity]
  B --> C[Story Node v3]
  C --> D[Focus Mode narrative]
~~~

## 📦 Data & Metadata

### Source bundle
| Source | Identifier | Notes |
|---|---|---|
| STAC item | TBD | TBD |
| Document | TBD | TBD |
| Map/layer | TBD | TBD |

### Optional Focus Mode controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements
- `prov:wasDerivedFrom`: list source IDs
- `prov:wasGeneratedBy`: pipeline activity/run ID
- Confidence/uncertainty fields (if predictive content is included)

## 🧱 Architecture

### How this story node is served
- API route(s) that fetch it
- UI component(s) that render it
- Audit panel expectations (warnings, citations, sensitivity notices)

## 🧠 Story Node & Focus Mode Integration

### Focus Mode behavior expectations
- Map/timeline changes
- Layer toggles
- Citation rendering
- “AI explanation” toggle behavior (if present)

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] All referenced entities exist (or have creation tickets)
- [ ] All dataset IDs resolve to catalog entries
- [ ] No prohibited AI actions implied
- [ ] Sensitive information handled correctly

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)
- FAIR+CARE council review: yes/no
- Security council review: yes/no
- Historian/editor review: yes/no

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial template | TBD |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FILE: docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---
title: "TEMPLATE — API Contract Extension (REST/GraphQL)"
path: "docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "template"
doc_kind: "Template"
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

doc_uuid: "urn:kfm:doc:templates:api-contract-extension:v1.0.0"
semantic_document_id: "kfm-template-api-contract-extension-v1.0.0"
event_source_id: "ledger:kfm:doc:templates:api-contract-extension:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions: [ "structure_extract" ]
ai_transform_prohibited: [ "generate_policy" ]

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# TEMPLATE — API Contract Extension (REST/GraphQL)

## 📘 Overview

### Change summary
- What is being added/changed/removed?

### Motivation
- Why is this needed (user story + system need)?

### Backward compatibility
- Compatible / version bump required / deprecations.

## 🗂️ Directory Layout

| Artifact | Path |
|---|---|
| API code | `src/server/` |
| API docs | `docs/` (link) |
| Schemas | `schemas/` |
| Tests | `tests/` |

## 🧭 Context

### Security + sensitivity
- If data can be sensitive, define:
  - authorization behavior
  - generalization behavior
  - audit/log behavior

## 🗺️ Diagrams

~~~mermaid
sequenceDiagram
  participant Client
  participant API
  participant Graph
  Client->>API: Request
  API->>Graph: Query (with redaction rules)
  Graph-->>API: Result + provenance refs
  API-->>Client: Contracted payload
~~~

## 📦 Data & Metadata

### Data returned
| Field | Source | Sensitivity | Notes |
|---|---|---|---|
| TBD | TBD | public/restricted | TBD |

## 🌐 STAC, DCAT & PROV Alignment

- How responses link back to:
  - STAC item IDs
  - PROV activity/run IDs
  - DCAT dataset identifiers

## 🧱 Architecture

### REST contract
~~~json
{ "TBD": "example response" }
~~~

### GraphQL contract
~~~graphql
type TBD { id: ID! }
~~~

### Contract tests required
- REST: OpenAPI schema + integration tests
- GraphQL: schema lint + resolver tests

## 🧠 Story Node & Focus Mode Integration

- If this endpoint feeds Focus Mode, define:
  - required provenance refs
  - includePredictions behavior (if any)
  - uncertainty/confidence fields

## 🧪 Validation & CI/CD

- [ ] Contract schema updated
- [ ] Integration tests added
- [ ] Docs updated
- [ ] Sensitivity rules verified

## ⚖ FAIR+CARE & Governance

- Identify required approvals and reviewers.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial template | TBD |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~