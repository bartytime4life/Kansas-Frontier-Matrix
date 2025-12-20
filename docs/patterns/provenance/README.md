---
title: "🧬 KFM Pattern — Provenance & Lineage"
path: "docs/patterns/provenance/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
status: "proposed"
doc_kind: "Pattern"
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
care_label: "Public · Low-Risk"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:patterns:provenance:readme:v1.0.0"
semantic_document_id: "kfm-patterns-provenance-readme-v1"
event_source_id: "ledger:kfm:doc:patterns:provenance:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "keyword_index"
  - "translate"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"
  - "speculative_additions"
  - "fabricate_provenance"
  - "invent_dataset_relationships"
  - "expose_sensitive_coordinates"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# 🧬 KFM Pattern — Provenance & Lineage

**Path:** `docs/patterns/provenance/README.md`

Define a **repeatable, audit-ready** approach to capturing lineage across the KFM pipeline  
(**ETL → STAC/DCAT/PROV → Neo4j → APIs → React/MapLibre UI → Story Nodes → Focus Mode**).

---

## 📘 Overview

### Purpose
This pattern standardizes **how KFM work products declare provenance** so that lineage is:

- **Deterministic & replayable** (run manifests + pinned inputs/versions)
- **Machine‑queryable** (PROV‑O compatible Entities / Activities / Agents)
- **Catalog‑friendly** (links from STAC + DCAT records)
- **Graph‑ready** (Neo4j lineage edges map cleanly from PROV relations)
- **Focus Mode safe** (summarization allowed; provenance invention prohibited)

### Scope

| In Scope | Out of Scope |
|---|---|
| Run-scoped (execution) provenance capture (`mcp/runs/<run_id>/…`) | Full ontology authoring (use existing KFM ontology + PROV‑O) |
| Dataset/item-scoped provenance links (STAC assets/links; DCAT mappings) | Frontend provenance UI design details (UI remains behind APIs) |
| Minimal provenance model: Entity / Activity / Agent | Defining new governance policy (link to governed docs instead) |
| Version-aware identifiers + predecessor/successor semantics | Secrets management, credential flows, or privileged operational procedures |

### Audience
- Primary: ETL/pipeline engineers, catalog maintainers, graph engineers, API engineers, documentation maintainers
- Secondary: data stewards, Story Node editors, Focus Mode reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc: `prov:Entity`, `prov:Activity`, `prov:Agent`, `run_id`, “immutable per run”, “sidecar provenance”

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Run manifest | `mcp/runs/<run_id>/run_manifest.json` | ETL | Deterministic “what happened” record |
| PROV bundle | `mcp/runs/<run_id>/prov.jsonld` | ETL | PROV‑O lineage (Entity/Activity/Agent) |
| Checksums | `mcp/runs/<run_id>/checksums.sha256` | ETL | Hashes for referenced outputs |
| STAC Items | `data/stac/.../item.json` | Catalogs | Links/assets must resolve to provenance |
| DCAT views | `data/catalog/dcat/...` | Catalogs | Dataset/distribution provenance references |

### Governance metadata (moved from front‑matter for template compliance)

| Field | Value |
|---|---|
| Release stage | Draft / Governed |
| Lifecycle | Living Document |
| Review cycle | Annual · FAIR+CARE Council & Focus Mode Board |
| Content stability | evolving |
| FAIR category (granular) | F1-A1-I1-R1 |
| Public exposure risk | Low |
| TTL policy | 24 months |
| Sunset policy | Review for supersession |
| Indigenous rights flag | true |
| Data steward | KFM FAIR+CARE Council |
| Sensitivity requirement (examples) | Examples must mask/generalize locations |

### Definition of done (for this document)
- [ ] Front-matter matches Universal Governed Doc keys
- [ ] Provenance rules are actionable (run-level + item-level linking)
- [ ] Versioning semantics described (predecessor/successor)
- [ ] Validation steps are listed and repeatable
- [ ] Sensitivity + sovereignty handling is explicit (no precise sensitive coordinates)
- [ ] No UI-to-graph direct access implied (API boundary preserved)

---

## 🗂️ Directory Layout

### This document
- `path`: `docs/patterns/provenance/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Pattern library | `docs/patterns/` | Implementation guidance patterns |
| MCP runs | `mcp/runs/` | Deterministic run artifacts + provenance bundles |
| Data domains | `data/` | Raw/work/processed + catalogs |
| STAC catalogs | `data/stac/` | Collections + items |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset/distribution outputs |
| PROV storage | `data/prov/` | Optional non-run PROV artifacts *(pattern-dependent)* |

### Expected file tree for this sub-area

#### Pattern library layout
~~~text
docs/
└── 📁 patterns/                                        # Pattern library (implementation guidance)
    ├── 📁 provenance/                                  # Provenance & lineage patterns (PROV-O aligned)
    │   ├── 📄 README.md                                # This document
    │   ├── 📁 examples/                                # CI-safe examples (mask/generalize locations)
    │   │   ├── 📄 prov_bundle.example.jsonld           # Minimal PROV bundle (run-level)
    │   │   ├── 📄 stac_item_with_prov.example.json     # STAC Item linking provenance asset
    │   │   └── 📄 dcat_dataset_with_prov.example.ttl   # DCAT dataset/distribution w/ PROV links
    │   └── 📁 templates/                               # Copy/paste templates
    │       ├── 📄 run_manifest.template.yaml           # Run manifest skeleton (inputs/outputs/params)
    │       └── 📄 provenance_note.template.md          # Human note to accompany a run (optional)
    └── 📁 stac/                                        # STAC patterns (see docs/patterns/stac/README.md)
~~~

#### Runtime and data artifact layout
~~~text
mcp/
└── 📁 runs/                                            # Run logs (deterministic, replayable)
    └── 📁 <run_id>/                                    # One pipeline execution (stable run_id)
        ├── 📄 run_manifest.json                        # Machine manifest (params, versions, env)
        ├── 📄 prov.jsonld                              # PROV-O bundle for this run
        ├── 📄 checksums.sha256                         # Hashes for referenced outputs
        └── 📁 outputs/                                 # Optional: output pointers (not primary storage)

data/
├── 📁 raw/                                             # Source snapshots (if stored; immutable)
├── 📁 processed/                                       # Derived datasets (versioned; no code here)
└── 📁 stac/                                            # STAC catalogs/items (data discovery layer)
    └── 📁 <collection>/                                # Collection-scoped grouping
        └── 📁 <item_id>/                               # Item folder (if file-based STAC layout)
            ├── 📄 item.json                            # STAC Item (links/assets include provenance)
            └── 📄 prov.jsonld                          # Optional: item-scoped provenance sidecar
~~~

---

## 🧭 Context

### Background
KFM treats provenance as a **first‑class governance artifact**: each dataset and transformation should be traceable to sources, processes, and responsible agents across the canonical pipeline ordering.

This pattern emphasizes:
- **STAC** for dataset/item discovery and structure
- **DCAT** for catalog interoperability and publishing
- **PROV‑O** for lineage (“what used what”, “what generated what”, and “who/what did it”)
- **Version-aware relationships** (predecessor/successor semantics)

### Assumptions
- Pipelines are **deterministic** and **idempotent** for identical inputs/config.
- `run_id` is stable and unique per execution.
- Outputs can be referenced via stable IDs + checksums.
- Frontend consumes provenance via **APIs** (no direct graph access).

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- UI never reads Neo4j directly; all lineage lookup is via the API layer.
- Examples and public artifacts must **not** expose sensitive coordinates or culturally sensitive site locations.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Canonical `run_id` format (timestamped? hash-based? ULID?) | TBD | TBD |
| When to store item-level `prov.jsonld` next to STAC Items vs linking to run-level only? | TBD | TBD |
| Which STAC link relations are canonical for lineage (`derived_from`, `predecessor`, `successor`)? | TBD | TBD |
| Do we require environment/container digests in every manifest? | TBD | TBD |

### Future extensions
- Add/standardize a provenance extension profile for STAC (if needed).
- Add an “audit panel” contract in APIs for provenance summaries + redaction warnings.
- Automated provenance regression tests: ensure every output entity has generating activity + checksums.

---

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL / Transform Activity] --> B[Output Entity]
  B --> C[STAC Item/Collection]
  B --> D[DCAT Dataset/Distribution]
  B --> E[PROV Bundle]
  C --> G[Graph Ingest]
  E --> G
  G --> API[API Layer]
  API --> UI[React/MapLibre UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant CI as CI Runner
  participant ETL as ETL Job
  participant PROV as PROV Bundle
  participant STAC as STAC Catalog
  CI->>ETL: execute(run_id, pinned_inputs, config)
  ETL->>PROV: write prov.jsonld (Activity + Entities + Agent)
  ETL->>STAC: write/update Item (link provenance asset)
  CI->>CI: validate (front-matter, STAC, provenance, checksums)
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Source entities | files/URLs/datasets | `data/raw/` or external | checksums + license metadata |
| Pipeline config | YAML/JSON | `src/pipelines/...` | schema + lint |
| Code revision | git SHA | repo | `commit_sha` captured in manifest |
| Environment | container/deps | CI/runtime | pinned digest / lockfiles (recommended) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Run manifest | JSON | `mcp/runs/<run_id>/run_manifest.json` | manifest schema *(not confirmed in repo)* |
| Run PROV bundle | JSON-LD | `mcp/runs/<run_id>/prov.jsonld` | PROV‑O JSON‑LD profile |
| Checksums | text | `mcp/runs/<run_id>/checksums.sha256` | sha256 entries |
| STAC Items/Collections | JSON | `data/stac/...` | STAC 1.0 + KFM profile |
| DCAT dataset views | TTL/JSON‑LD | `data/catalog/dcat/...` | DCAT 3 + KFM profile |

### Sensitivity & redaction
- Do not publish sensitive or culturally sensitive coordinates in examples.
- Prefer generalized geometry (aggregation, redaction, or centroids at coarse precision) for public artifacts.
- Where sovereignty applies, ensure publication is gated by governance review.

### Quality signals
- Checksum completeness: every referenced output has sha256.
- Provenance completeness: every output entity has a generating activity + at least one agent.
- Schema validity: STAC/DCAT/PROV artifacts validate and links resolve.

### Minimum run manifest fields
A run manifest should reconstruct “what happened” without guesswork:

- `run_id` (stable; unique)
- `started_at`, `ended_at`
- `commit_sha` (code revision)
- execution environment (container digest / pinned deps)
- inputs: `{id, version, checksum, href}`
- outputs: `{id, version, checksum, href}`
- parameters/config references (paths; never embed secrets)

~~~yaml
run_id: "<run_id>"
started_at: "YYYY-MM-DDTHH:MM:SSZ"
ended_at: "YYYY-MM-DDTHH:MM:SSZ"

code:
  commit_sha: "<latest-commit-hash>"
  pipeline: "<pipeline-name>"
  config_ref: "path/to/config.yaml"

inputs:
  - id: "<source-entity-id>"
    version: "<vX.Y.Z>"
    checksum_sha256: "<sha256>"
    href: "<uri-or-path>"

outputs:
  - id: "<output-entity-id>"
    version: "<vX.Y.Z>"
    checksum_sha256: "<sha256>"
    href: "<uri-or-path>"

agents:
  - id: "<agent-id>"
    type: "software|person|org"
    label: "<display-name>"

notes:
  sensitivity: "public|restricted|sensitive"
  sovereignty_review: "required|not-required|pending"
~~~

### Sidecar provenance artifacts
Recommended default:
- Write a **run-level** `prov.jsonld` under `mcp/runs/<run_id>/`
- Optionally write an **item-level** provenance sidecar in the STAC item folder, or expose it as a STAC asset

Provenance artifacts should be treated as **immutable per run**. If corrected, create a new run/version and link with revision semantics.

### Document provenance chain (pattern doc self-lineage)
- Origin root: this document/version
- Provenance chain:
  - `docs/patterns/provenance/README.md@v1.0.0`
- Ordering: newest-first = true
- Must reference origin root = true

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Attach provenance using **assets** or **links**:
- Add an asset such as `assets.provenance` pointing to a PROV JSON‑LD file.
- Use link relations for lineage (e.g., `derived_from`) as defined by KFM STAC profile/patterns.

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "example-item",
  "properties": {
    "datetime": "2025-12-16T00:00:00Z"
  },
  "geometry": null,
  "links": [
    {
      "rel": "derived_from",
      "href": "stac://source-item-id",
      "type": "application/json",
      "title": "Source STAC Item"
    }
  ],
  "assets": {
    "data": {
      "href": "data/processed/example-item.parquet",
      "type": "application/x-parquet",
      "roles": ["data"]
    },
    "provenance": {
      "href": "mcp/runs/<run_id>/prov.jsonld",
      "type": "application/ld+json",
      "roles": ["metadata"],
      "title": "PROV-O lineage bundle for this output"
    }
  }
}
~~~

### DCAT
In DCAT, datasets/distributions can reference provenance using PROV terms.

~~~turtle
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .

<#dataset> a dcat:Dataset ;
  dct:identifier "example-item" ;
  dct:title "Example Dataset" ;
  prov:wasGeneratedBy <#activity> .

<#dist> a dcat:Distribution ;
  dct:format "Parquet" ;
  dcat:downloadURL <file:data/processed/example-item.parquet> ;
  prov:wasDerivedFrom <#sourceEntity> .
~~~

### PROV-O
Minimum recommended:
- One `prov:Activity` (the run / transform)
- One or more input `prov:Entity`
- One or more output `prov:Entity`
- One `prov:Agent` (software/person/org)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "urn:kfm:prov:bundle:<run_id>",
  "@type": "prov:Bundle",
  "prov:wasGeneratedBy": {
    "@id": "urn:kfm:prov:activity:<run_id>",
    "@type": "prov:Activity"
  }
}
~~~

### Versioning
- Use STAC/graph predecessor–successor semantics for new versions.
- Ensure version chains are queryable:
  - In catalogs (STAC/DCAT)
  - In graph lineage (Entity ↔ Activity ↔ Agent edges)

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize + emit provenance | Config + run logs |
| Catalogs | STAC/DCAT/PROV outputs | JSON/Turtle + validators |
| Graph | Ingest lineage as queryable edges | Cypher behind API layer |
| APIs | Serve provenance lookup | REST/GraphQL contracts |
| UI | Render provenance summaries | API calls only |
| Story Nodes | Evidence-led narrative artifacts | Catalog + graph refs |
| Focus Mode | Context synthesis | Provenance-linked bundle |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Provenance artifacts | `mcp/runs/<run_id>/…` | Immutable per run; new run for corrections |
| STAC profile | `data/stac/…` + docs | Profile version bumps with validation |
| DCAT profile | `data/catalog/dcat/…` + docs | Profile version bumps with validation |
| API provenance endpoints | `src/server/…` + docs | Backward compat or version bump |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: provenance asset/link conventions enforced
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: lineage relations mapped and constrained
- [ ] APIs: provenance query endpoints + contract tests
- [ ] UI: provenance summary panel via API
- [ ] Focus Mode: provenance references required for every claim
- [ ] Telemetry: provenance completeness signals recorded

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Story Nodes should reference underlying **Entities** (datasets / STAC Items / documents) and—where available—the **Activity** that generated derived artifacts.
- Focus Mode may summarize and build navigation aids, but must not fabricate provenance or dataset relationships.

### Provenance-linked narrative rule
For any Story Node derived from analysis (extraction/modeling), ensure references back to:
- Source entity (original dataset/document)
- Generating activity (`run_id`)
- Agent/code revision (`commit_sha`)
- Output entity version + checksums

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (H1/H2 structure; fenced trees use `~~~text`)
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Link integrity (STAC assets/links resolve; provenance hrefs resolve)
- [ ] Provenance completeness checks (entity/activity/agent present)
- [ ] Checksum checks (sha256 present for outputs)
- [ ] Secret/PII scanning (no sensitive coords or restricted locations leaked)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate STAC
# 2) validate DCAT
# 3) validate PROV bundles
# 4) run doc lint
# 5) run contract tests
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Provenance completeness % | Catalog/PROV validators | `docs/telemetry/` + `schemas/telemetry/` *(not confirmed in repo)* |
| Broken provenance links | STAC link checker | `mcp/runs/<run_id>/…` |
| Redaction violations | sensitivity scanner | CI logs / telemetry |

---

## ⚖ FAIR+CARE & Governance

### Review gates
- FAIR+CARE council review: recommended for changes affecting public exposure or sovereignty contexts
- Security review: required if provenance begins revealing operational details beyond policy
- Historian/editor review: recommended when narrative provenance is presented to the public

### CARE / sovereignty considerations
- If a dataset touches Indigenous communities, provenance must not undermine sovereignty controls.
- When in doubt:
  - mark sensitivity appropriately
  - route for governance review before publication

### AI usage constraints
- Allowed: summarization and structure extraction that preserves meaning and does not add new factual claims.
- Prohibited: fabricating provenance edges, inventing dataset relationships, inferring sensitive locations, or exposing sensitive coordinates.
- AI training inclusion: false (policy note; if needed, mirror in governed AI policy docs)

### Governance review triggers
Escalate to human review when a change:
- increases public exposure of provenance detail (e.g., adds location precision)
- introduces new lineage relations for sensitive sources
- changes retention policy for run artifacts or provenance bundles

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial provenance & lineage pattern draft (normalized to Universal Governed Doc structure) | KFM Documentation Team |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
