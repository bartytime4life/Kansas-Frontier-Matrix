---
title: "KFM Repro Kit — Environment (CI + Local)"
path: ".github/repro-kit/env/README.md"
version: "v1.0.0"
last_updated: "2025-12-30"
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

doc_uuid: "urn:kfm:doc:github:repro-kit:env-readme:v1.0.0"
semantic_document_id: "kfm-github-repro-kit-env-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:repro-kit:env-readme:v1.0.0"
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

# KFM Repro Kit — Environment (CI + Local)

## 📘 Overview

### Purpose

This README defines **how KFM environments are made reproducible** (in GitHub Actions and on developer machines) so that:

- the canonical pipeline can be executed deterministically (as practical),
- the same inputs produce the same governed boundary artifacts (STAC/DCAT/PROV),
- provenance can record **what code + config + environment** produced each output, and
- CI can reliably enforce policy + integrity gates.

This folder is the canonical home for *environment specifications* and *reproducibility helpers* that reduce “works on my machine” drift.

### Scope

| In Scope | Out of Scope |
|---|---|
| Environment specs (container/VM/lockfiles) used by CI and local dev | Production hosting / runtime infrastructure (deployments) |
| Toolchain pinning (Python/Node/JVM/OS) and dependency locking | Domain-specific ETL logic (that lives in `src/pipelines/`) |
| Environment fingerprinting + recording env details into run logs/PROV | Secrets management itself (credentials never stored here) |
| Supply-chain artifacts support (SBOM/SLSA) where applicable | Governance documents content (lives under `docs/governance/`) |

### Audience

- **Maintainers / reviewers**: need to evaluate env changes safely.
- **Contributors**: need a consistent setup path that matches CI.
- **Researchers / auditors**: need to reproduce a historical run from provenance.

### Definitions

- **Environment spec**: a version-pinned definition of runtimes + dependencies (e.g., image digest + lockfiles).
- **Env fingerprint**: a stable hash that summarizes the environment spec inputs (lockfiles + spec files).
- **Repro Kit**: repo-supported tooling/docs for running + validating KFM deterministically.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + invariants |
| Ingestion architecture | `docs/architecture/KFM_INGEST_ARCHITECTURE.md` | Architecture | Defines reproducible governed intake patterns |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Required doc structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Machine-ingestible narrative |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Contract-first API changes |
| Schemas | `schemas/` | Data/Platform | JSON Schemas for boundary artifacts |
| Validators + utilities | `tools/` | Platform | Lints, schema checks, QA scripts |
| CI workflows | `.github/workflows/` | Platform | Policy gates (secret/PII scans, schema validation, etc.) |
| MCP run logs | `mcp/runs/` | AI/Platform | Experiments + reproducible run artifacts |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Uses required governed sections (Overview/Directory/Context/Diagrams/…)
- [ ] Clearly defines what “environment fingerprint” means and where it is recorded
- [ ] Specifies how CI and local environments converge (pinning + lockfiles)
- [ ] Explicitly states **no secrets** may live in env specs
- [ ] Lists CI gates relevant to env reproducibility (schema checks, security scans, etc.)
- [ ] FAIR+CARE implications called out (especially around sensitive-location leakage prevention)

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/env/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows + policy gates |
| Data lifecycle | `data/` | `raw/ → work/ → processed/` plus catalogs `stac/`, `catalog/dcat/`, `prov/` |
| Pipelines | `src/pipelines/` | ETL + catalog generation |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| Schemas | `schemas/` | STAC/DCAT/PROV/story/ui schemas |
| Tools | `tools/` | Validators, utilities, QA scripts |
| MCP | `mcp/` | Experiments, runs, SOPs |
| Tests | `tests/` | Unit + integration tests |

### Expected file tree for this sub-area

The following layout is **recommended** for this folder. Entries marked *not confirmed in repo* are optional conventions this README expects to exist for full reproducibility.

~~~text
📁 .github/
├── 📁 repro-kit/
│   ├── 📁 env/
│   │   ├── 📄 README.md
│   │   ├── 📁 docker/                         # optional; not confirmed in repo
│   │   │   ├── 📄 Dockerfile
│   │   │   └── 📄 docker-bake.hcl
│   │   ├── 📁 compose/                        # optional; not confirmed in repo
│   │   │   └── 📄 docker-compose.yml
│   │   ├── 📁 python/                         # optional; not confirmed in repo
│   │   │   ├── 📄 pyproject.toml
│   │   │   ├── 📄 poetry.lock
│   │   │   └── 📄 requirements.lock.txt
│   │   ├── 📁 node/                           # optional; not confirmed in repo
│   │   │   ├── 📄 package.json
│   │   │   └── 📄 pnpm-lock.yaml
│   │   ├── 📁 neo4j/                          # optional; not confirmed in repo
│   │   │   └── 📄 neo4j.conf
│   │   ├── 📁 scripts/                        # optional; not confirmed in repo
│   │   │   ├── 📄 env-fingerprint.sh
│   │   │   └── 📄 verify-repro.sh
│   │   └── 📄 ENVIRONMENT_MATRIX.md           # optional; not confirmed in repo
│   └── 📄 README.md                           # repro-kit root; not confirmed in repo
└── 📁 workflows/
    └── 📄 <workflow>.yml
~~~

## 🧭 Context

### Background

KFM’s architecture depends on a strict, non-negotiable pipeline ordering:

- **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

To keep this pipeline **traceable and repeatable**, the environment must be reproducible: dependency versions, toolchain versions, and build inputs should be pinned and recorded. KFM further expects deterministic, idempotent transforms with logged inputs/outputs and stable IDs.

### Assumptions

- CI is GitHub Actions-based (because this doc lives in `.github/`) *(not confirmed in repo)*.
- ETL/catalog generation is implemented in `src/pipelines/`, graph build in `src/graph/`, API in `src/server/`, UI in `web/` (per Master Guide expectations).
- Neo4j is used for graph storage and is accessed **only through the API layer** (UI never queries Neo4j directly).

### Constraints / invariants

- **API boundary invariant:** the UI must never read Neo4j (or any DB) directly—only contracted APIs.
- **No secrets in env specs:** credentials, tokens, keys must be supplied via secret stores (GitHub Secrets, local `.env` excluded from git, etc.).
- **Reproducibility-first:** lock dependencies; record tool versions and hashes in run manifests/PROV where possible.
- **FAIR+CARE enforcement:** environment and CI must support scans that prevent sensitive-location leakage and classification downgrades.

### Open questions

| Question | Why it matters | Owner | Target decision date | Status |
|---|---|---:|---:|---|
| What is the canonical Python dependency manager (Poetry vs pip-tools vs Conda)? | Determines lockfile strategy and build reproducibility | TBD | TBD | Open |
| What is the canonical Node package manager (pnpm vs npm vs yarn)? | Impacts lockfile + CI determinism | TBD | TBD | Open |
| Are container images required for all pipeline stages in CI? | Affects parity between CI and local | TBD | TBD | Open |
| Is an env fingerprint mandatory in every PROV run? | Needed for full run reproduction | TBD | TBD | Open |
| Do we support GPU profiles for AI evidence artifacts? | Required for reproducible ML/model runs | TBD | TBD | Open |

### Future extensions

- Add devcontainer support (`.devcontainer/`) *(not confirmed in repo)*.
- Add a Nix flake or similar fully declarative build *(not confirmed in repo)*.
- Add multi-arch builds + cached artifacts for faster CI.
- Add explicit “GPU/Accelerated” profiles for AI evidence artifacts with recorded driver versions.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  subgraph Env["Repro Kit Environment (CI + Local)"]
    E1["Pinned toolchains<br/>OS · Python · Node · JVM"]
    E2["Dependency locks<br/>Lockfiles + image digests"]
    E3["Supply chain artifacts (optional)<br/>SBOM + SLSA provenance"]
    E4["Env fingerprint recorded<br/>in run manifest + PROV"]
  end

  subgraph Pipeline["KFM Canonical Pipeline"]
    A["Raw Sources"] --> B["ETL + Normalization"]
    B --> C["STAC Items + Collections"]
    C --> D["DCAT Dataset Views"]
    C --> P["PROV Lineage Bundles"]
    C --> G["Neo4j Graph (references catalogs)"]
    G --> H["API Layer (contracts + redaction)"]
    H --> I["Map UI — React · MapLibre"]
    I --> J["Story Nodes (governed narratives)"]
    J --> K["Focus Mode (provenance-linked bundle)"]
  end

  Env -.build/run/validate.-> Pipeline
  P <-->|"links to env + run IDs"| Env
~~~

### Optional: sequence diagram (CI parity)

~~~mermaid
sequenceDiagram
  autonumber
  participant Dev as Contributor
  participant CI as GitHub Actions (CI)
  participant Env as Repro Kit Env
  participant Pipe as Pipeline Stages
  participant Cat as STAC/DCAT/PROV Outputs

  Dev->>CI: Push PR (env / pipeline changes)
  CI->>Env: Build pinned environment (lockfiles/image digest)
  CI->>Pipe: Run deterministic steps (ETL → catalogs → tests)
  Pipe-->>Cat: Produce boundary artifacts
  CI->>Pipe: Run schema + integrity checks
  CI-->>Dev: Pass/Fail with actionable logs
~~~

## 📦 Data & Metadata

Even though this folder is “environment,” treat the environment itself as a **first-class artifact**: it has inputs, versioning, and outputs that must be referenced by provenance.

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Container spec | `Dockerfile` / image digest | `.github/repro-kit/env/docker/` *(optional; not confirmed in repo)* | Build must be deterministic and pinned |
| Python dependency lock | `poetry.lock` / `requirements.lock.txt` | `.github/repro-kit/env/python/` *(optional; not confirmed in repo)* | Hash-locked dependency resolution |
| Node dependency lock | `pnpm-lock.yaml` / `package-lock.json` | `.github/repro-kit/env/node/` *(optional; not confirmed in repo)* | Lockfile-based install in CI |
| Neo4j config | `neo4j.conf` | `.github/repro-kit/env/neo4j/` *(optional; not confirmed in repo)* | Minimal settings; no secrets |
| Environment matrix | Markdown/JSON | `.github/repro-kit/env/ENVIRONMENT_MATRIX.md` *(optional; not confirmed in repo)* | Reviewed + versioned |

### Outputs

| Output | Format | Where recorded | Why it exists |
|---|---|---|---|
| Env fingerprint | JSON (`sha256` summary) | `mcp/runs/<run_id>/` *(suggested; not confirmed in repo)* | Reproduce runs exactly |
| Run manifest | JSON | alongside pipeline outputs or `mcp/runs/` | Records commit + params + env |
| SBOM | SPDX/CycloneDX | CI artifacts / releases | Supply-chain transparency |
| SLSA provenance | Attestation | CI artifacts / releases | Tamper-resistant build linkage |

### Environment fingerprinting (recommended contract)

The env fingerprint should be derived from:

- normalized list of env spec inputs (Dockerfile, lockfiles, tool version pins),
- their file hashes (sha256),
- plus declared platform context (OS/arch).

Suggested algorithm:

~~~text
fingerprint_inputs = sorted([
  sha256("docker/Dockerfile"),
  sha256("python/poetry.lock"),
  sha256("node/pnpm-lock.yaml"),
  sha256("ENVIRONMENT_MATRIX.md"),
  ...
])

env_fingerprint = sha256(join("\n", fingerprint_inputs))
~~~

Record `env_fingerprint`, `commit_sha`, toolchain versions, and (if applicable) random seeds in the run manifest and PROV.

### Secrets & sensitive data

- **Never** commit secrets into this folder.
- CI must supply credentials via GitHub Secrets and mask logs.
- Any env files that require tokens must support injection at runtime (e.g., via env vars) and remain safe when printed.

## 🌐 STAC, DCAT & PROV Alignment

### Why env belongs in PROV

Reproducibility requires that provenance captures:

- code version (commit hash),
- parameters/config,
- inputs/outputs (with checksums),
- and the environment details (toolchain + dependency pins).

KFM treats boundary artifacts (STAC/DCAT/PROV) as the interface between pipeline stages; the environment is part of what makes those boundary artifacts reproducible.

### Recommended PROV fields for environment capture

| PROV concept | Recommended capture | Example |
|---|---|---|
| `prov:SoftwareAgent` | container image digest, tool versions | `python=3.12.x`, `node=20.x`, `neo4j=5.x` |
| `prov:Activity` | env fingerprint + run id + commit | `env_fingerprint`, `commit_sha`, `run_id` |
| `prov:Entity` | lockfiles as entities | `poetry.lock`, `pnpm-lock.yaml` |
| `prov:used` | activity uses lockfile entities | ETL activity uses env + deps |
| `prov:generated` | activity generates outputs | STAC/DCAT/PROV files |

### Versioning expectations

- Environment changes that affect reproducibility should be versioned (semantic versioning recommended).
- When env changes, link which modules/runs are affected (at minimum via commit hash references).
- Keep old env definitions available so historical runs can be reproduced.

## 🧱 Architecture

### Subsystem contracts for reproducibility

| Subsystem | Contract artifacts | Environment obligations | “Do not break” rule |
|---|---|---|---|
| ETL | configs + run logs + validation | Python runtime + geospatial deps; deterministic seeds recorded | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | JSON schema validators available in CI/local | machine-validated |
| Graph | ontology + migrations + constraints | Neo4j version pinned; graph fixture tests runnable | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | Node runtime pinned; contract tests runnable | backwards compat or version bump |
| UI | layer registry + a11y + audit affordances | Node toolchain pinned; build reproducible | no hidden data leakage |
| Story/Focus | provenance-linked bundle | doc validators + story schema checks | no hallucinated/unsourced claims |

### Canonical subsystem homes (one home per subsystem)

- Pipelines: `src/pipelines/`
- Graph build: `src/graph/`
- API boundary: `src/server/`
- UI: `web/`
- Data + catalogs: `data/` (including `data/stac/`, `data/catalog/dcat/`, `data/prov/`)
- Docs + templates: `docs/` and `docs/templates/`
- CI: `.github/`

### Interfaces / contracts (why env must be multi-stack)

This environment must support contract validation across layers:

- JSON schema validation for STAC/DCAT/PROV outputs.
- Graph integrity tests (constraints + ontology expectations).
- API contract tests (OpenAPI/GraphQL).
- UI configuration schema checks (layer registry) *(not confirmed in repo)*.
- Documentation protocol validation (front-matter + required sections).

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

Environment reproducibility supports narratives by ensuring:

- Story Nodes are validated against their template/schema.
- Claims remain traceable to cataloged evidence and stable IDs.

### Focus Mode rule

Focus Mode must only consume **provenance-linked** content. The environment (CI + local) must include validators that prevent:

- orphan citations,
- broken provenance links,
- and any workflow that would publish sensitive locations without required generalization/redaction.

Any predictive/suggestive content must be opt-in and carry uncertainty/confidence metadata.

## 🧪 Validation & CI/CD

### Minimum CI gates (env-relevant)

When env specs change, CI should be able to run at least:

- Markdown protocol validation (front-matter + required sections)
- Link/reference checks (no orphan pointers)
- JSON schema validation (STAC/DCAT/PROV; story node schemas; telemetry schemas if present)
- Graph integrity tests (constraints, expected labels/edges)
- API contract tests (OpenAPI/GraphQL schema + resolver tests)
- UI layer registry schema checks (if present)
- Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Reproduction

This folder is successful if it enables a contributor to reproduce a historical run using only:

1) a commit hash, and  
2) a PROV/run manifest reference to environment details.

Recommended reproduction workflow (conceptual):

- Identify the run’s `commit_sha` + `env_fingerprint` (from `mcp/runs/` and/or `data/prov/`).
- Checkout the exact `commit_sha`.
- Rebuild the environment from the lockfiles/container specs referenced by that commit.
- Re-run the pipeline step(s) with the same configs/seeds (as recorded in run manifest).
- Compare output checksums to the recorded manifest.

### Telemetry signals (recommended)

| Signal | Source | Where recorded |
|---|---|---|
| `env_built` | CI/local env build | `mcp/runs/` *(recommended; not confirmed in repo)* |
| `deps_locked` | dependency resolver | `mcp/runs/` / CI artifacts |
| `schema_validated` | schema validators | `mcp/runs/` / CI logs |
| `promotion_blocked` | policy gate | `mcp/runs/` / CI logs |
| `catalog_published` | catalog publish step | `mcp/runs/` / CI logs |

## ⚖ FAIR+CARE & Governance

### Review gates

Environment changes are high-leverage. At minimum:

- require maintainer review for any changes that affect lockfiles/toolchain versions,
- require security review for any changes that affect build provenance/SBOM tooling,
- require governance review if environment changes could impact redaction/generalization behavior.

### CARE / sovereignty considerations

- Ensure scans exist to prevent publishing sensitive locations without redaction/generalization.
- Ensure classification propagation checks prevent downgrading restricted inputs into public outputs.

### AI usage constraints

- Respect `ai_transform_permissions` / `ai_transform_prohibited` in front-matter.
- Never introduce workflows that infer sensitive locations from restricted datasets.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-30 | Initial environment reproducibility README | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Ingestion architecture: `docs/architecture/KFM_INGEST_ARCHITECTURE.md`
- Templates: `docs/templates/` (universal/story/API)
- Schemas: `schemas/`
- Tools/validators: `tools/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

