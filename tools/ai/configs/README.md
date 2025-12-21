---
title: "tools/ai/configs — AI Configuration Registry"
path: "tools/ai/configs/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:tools:ai:configs:readme:v1.0.0"
semantic_document_id: "kfm-tools-ai-configs-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:ai:configs:readme:v1.0.0"
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

# tools/ai/configs

## 📘 Overview

### Purpose

This directory contains **version-controlled configuration files** for AI/ML tooling that runs **offline as part of the KFM build pipeline** (e.g., text extraction, classification, embeddings, scoring). These configs make runs deterministic, replayable, and traceable (**config-as-code**).

Configs here must preserve the KFM system invariant: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode** (no direct UI ↔ graph coupling).

### Scope

| In Scope | Out of Scope |
|---|---|
| AI pipeline configs (YAML/JSON), prompt templates, model/pipeline profiles, redaction flags | Secrets/credentials, trained model binaries, run outputs, datasets, experiment logs |

### Audience

- Primary: AI / data pipeline engineers; maintainers of `tools/ai/*`
- Secondary: historians/curators reviewing AI-derived artifacts; API/UI developers consuming AI outputs indirectly via catalogs/graph

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: config, run, profile, provenance, STAC, DCAT, PROV, Focus Mode

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| KFM Master Guide (pipeline invariants, CI gates) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Source of pipeline ordering + “do not break” rules |
| Governance (ethics/sovereignty) | `docs/governance/*` | Governance council | Redaction/generalization expectations |
| AI run logs & experiment capsules | `mcp/runs/` and/or `mcp/experiments/` | AI team | Run outputs do **not** live under `tools/ai/configs/` |
| Schemas for configs (if/when added) | `schemas/ai/configs/*` | Platform | **not confirmed in repo** — recommended future addition |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `tools/ai/configs/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Tooling entrypoints | `tools/ai/` | CLI/scripts that consume configs (varies per tool) |
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 tools/
└── 📁 ai/
    └── 📁 configs/
        ├── 📄 README.md
        ├── 📁 profiles/                # config overlays (dev/prod/local)
        │   ├── 📄 default.yaml         # not confirmed in repo
        │   └── 📄 local.example.yaml   # not confirmed in repo (copy → local.yaml, gitignored)
        ├── 📁 pipelines/               # task-level configs (what to run)
        │   ├── 📄 nlp_extract.yaml      # not confirmed in repo
        │   └── 📄 embeddings.yaml       # not confirmed in repo
        ├── 📁 models/                  # model selection + version pins
        │   └── 📄 <model_id>.yaml       # not confirmed in repo
        └── 📁 prompts/                 # prompt templates (if LLM-assisted extraction is used)
            └── 📄 <prompt_id>.md        # not confirmed in repo
~~~

## 🧭 Context

### Background

KFM’s design assumes heavy AI computations happen **offline** during pipeline runs, producing artifacts that are later surfaced through catalogs/graph/APIs rather than executed in the live web UI.

### Assumptions

- Config files are treated as code and versioned.
- A given run should be reproducible from: (a) config file(s), (b) code commit, (c) dataset version references, and (d) environment spec.

### Config-as-code conventions (recommended)

> These are conventions intended to keep runs reproducible and auditable. If a stricter standard/schema exists elsewhere in the repo, that standard wins (**not confirmed in repo**).

**Naming + versioning**

- Prefer `kebab-case` filenames.
- Include either:
  - a semver in the filename (e.g., `nlp-extract.v1.2.0.yaml`), **or**
  - a `version:` field in the config and keep the filename stable.

**No secrets**

- Do **not** commit credentials, API keys, tokens, user identifiers, or sensitive coordinates.
- Use environment variables or a secret manager. If you must include placeholders, use obvious stubs (e.g., `${LLM_API_KEY}`).

**Provenance hooks**

- Configs should make it easy for runners to emit PROV with: run ID, config ID, input dataset IDs, output artifact IDs.

**Example config header (illustrative — not a schema)**

~~~yaml
config_id: "ai.nlp_extract.v1"
version: "1.0.0"
owner: "TBD"
description: "Extract entities/events from source documents and emit evidence artifacts."

inputs:
  - dataset_id: "dcat:TBD"
    selector: "data/work/TBD"

outputs:
  - dataset_id: "dcat:TBD"
    path: "data/processed/TBD"

model:
  name: "TBD"
  version: "TBD"     # pin exact version/hash

runtime:
  seed: 42
  deterministic: true

safety:
  allow_sensitive: false
  redaction_profile: "public"

provenance:
  prov_activity_type: "kfm:AiExtraction"
  run_id: "<filled-at-runtime>"
~~~

### Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- No secrets in repo (use env vars / secret manager).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical config format (YAML vs JSON) for AI tooling? | TBD | TBD |
| Where is the config schema validated (CI step + schema location)? | TBD | TBD |
| Are prompt templates governed like Story Nodes (citation requirements)? | TBD | TBD |

### Future extensions

- Add JSON Schema validation for configs under `schemas/ai/configs/` (**not confirmed in repo**).
- Add a “config registry” index (machine-readable) to map config IDs → tasks → owners.

## 🗺️ Diagrams

### System / dataflow diagram (AI configs in the KFM pipeline)

~~~mermaid
flowchart LR
  A[tools/ai/configs/*] --> B[tools/ai/* scripts]
  B --> C[data/processed/*]
  C --> D[STAC/DCAT/PROV outputs]
  D --> E[Neo4j Graph]
  E --> F[API Layer]
  F --> G[React/Map UI]
  G --> H[Story Nodes]
  H --> I[Focus Mode]
~~~

### Optional: sequence diagram (config → run → provenance)

~~~mermaid
sequenceDiagram
  participant Runner as Pipeline Runner
  participant Cfg as tools/ai/configs/*
  participant Out as data/processed + catalogs
  Runner->>Cfg: load config (config_id, version)
  Runner->>Out: run task + write outputs
  Runner->>Out: emit STAC/DCAT/PROV (includes run_id + config_id)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| AI config | YAML/JSON | `tools/ai/configs/*` | YAML lint / JSON schema (if adopted) |
| Input datasets | varied | `data/raw/` / `data/work/` | dataset-specific checks + catalog references |
| Model artifacts | varied | model registry / DVC / external | hash/version pins |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| AI-derived features | GeoJSON/CSV/Parquet/etc. | `data/processed/` | dataset schema + validators |
| Evidence artifacts | JSON/MD/assets | `mcp/runs/` and/or `data/reports/` | **not confirmed in repo** |
| Catalog entries | JSON | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC 1.0 / DCAT 3 / PROV-O profiles |

### Sensitivity & redaction

- Configs may include flags to enable redaction/generalization in outputs.
- Do not commit: API keys, tokens, user identifiers, sensitive location coordinates.

### Quality signals

- Deterministic runs: fixed seeds, pinned model versions, stable dataset references.
- Provenance completeness: run ID + config ID + input dataset IDs appear in PROV.

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements

- `prov:wasDerivedFrom`: list source IDs
- `prov:wasGeneratedBy`: pipeline activity/run ID
- Confidence/uncertainty fields (if predictive content is included)

### STAC

If an AI job produces a spatial artifact (e.g., derived features, raster masks), the pipeline should:

- write outputs under `data/processed/` and/or `data/stac/`
- register them as STAC Items/Assets where applicable
- include links between versions (predecessor/successor)

### DCAT

- Ensure derived datasets have a DCAT view (title/description/license/keywords at minimum).

### PROV-O

- Record a `prov:Activity` for each AI run (include run ID + config ID).
- Link `prov:wasDerivedFrom` to input dataset IDs / STAC Item IDs.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| AI configs | Define what to run + how | YAML/JSON files in this directory |
| AI tooling | Execute extraction / inference | scripts under `tools/ai/` (varies) |
| Pipelines | Orchestrate runs | `src/pipelines/` |
| Catalogs | Publish machine-readable artifacts | STAC/DCAT/PROV outputs |
| Graph | Connect artifacts to entities | via graph build + API layer |
| UI / Focus | Render provenance-linked outputs | API calls only |

### Extension points checklist

- [ ] New task config added under `tools/ai/configs/pipelines/`
- [ ] Output schema and catalog registration updated
- [ ] PROV activity emission implemented
- [ ] Graph mapping updated (if new entity types/relations)
- [ ] API contract updated (if new UI-facing surface area)

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

- AI-derived outputs can be used to *assist* story node drafting, but Story Nodes must remain evidence-led and provenance-linked.

### Focus Mode rule

- Focus Mode only consumes provenance-linked content.
- Any predictive content must be opt-in and carry uncertainty / confidence metadata.

## 🧪 Validation & CI/CD

### Minimum CI gates for “v12-ready” contributions

- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests (if changes affect API surfaces)
- UI layer registry schema checks (if changes affect UI layer registry)
- Security + sovereignty scanning gates (where applicable)

### Validation checklist (configs)

- [ ] Configs are linted (YAML/JSON) and schema-validated (if schema exists)
- [ ] Model + dataset versions are pinned (or otherwise reproducible)
- [ ] Run output locations match repo placement rules (`data/processed/`, `data/stac/`, `mcp/runs/`, etc.)
- [ ] Provenance emission includes run_id + config_id + input/output IDs
- [ ] No prohibited AI actions implied; no secrets or sensitive coordinates committed

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### Governance approvals required (if any)

- FAIR+CARE council review: TBD
- Security council review: TBD
- Historian/editor review: TBD

### Sovereignty safety

- Document redaction/generalization rules for any restricted locations.

### AI usage constraints

- Do not hard-code prompts/configs that infer sensitive locations from protected or redacted inputs.
- Prefer extraction pipelines that produce auditable, provenance-linked outputs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for AI configs directory | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
