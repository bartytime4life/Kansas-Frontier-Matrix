---
title: "KFM Drift — Baselines (README)"
path: "tools/ai/drift/baselines/README.md"
version: "v0.1.0"
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

doc_uuid: "urn:kfm:doc:tools:ai:drift:baselines-readme:v0.1.0"
semantic_document_id: "kfm-tools-ai-drift-baselines-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:tools:ai:drift:baselines-readme:v0.1.0"
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

# KFM Drift — Baselines

## 📘 Overview

### Purpose
This directory documents **how KFM drift baselines are stored and referenced** for drift monitoring.
A “baseline” is a **reference snapshot** (typically summary statistics, distributions, or embeddings) used to compare a “current window” and quantify drift.

### Scope
| In Scope | Out of Scope |
|---|---|
| Baseline storage conventions | Full drift algorithm implementation details |
| Baseline metadata expectations (manifest fields, IDs) | Alert routing / notification policies |
| Validation expectations (schema + safety) | UI dashboards and visualization design |
| Guidance on what *not* to commit | Production deployment / ops runbooks |

### Audience
- Primary: KFM maintainers implementing/operating drift monitoring in pipelines and AI runs
- Secondary: Data governance reviewers, CI maintainers, contributors adding new telemetry signals

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Baseline**: reference snapshot of statistics/distributions for a defined scope.
  - **Reference window**: time/range used to build the baseline.
  - **Current window**: time/range used for drift evaluation.
  - **Drift target**: what we are monitoring (input features, embeddings, model outputs, graph metrics).
  - **Manifest**: metadata that points to baseline artifacts and their provenance.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Drift tool root README | `tools/ai/drift/README.md` | TBD | Overall drift tool usage and concepts |
| Baseline manifests | `tools/ai/drift/baselines/**` | TBD | Recommended: lightweight pointers + checksums |
| Baseline schemas | `schemas/telemetry/**` | Contracts owners | Expected location for telemetry contracts (may be placeholder) |
| Run artifacts | `mcp/runs/**` | AI/Tooling | Recommended home for large, run-scoped artifacts |
| Derived datasets | `data/<domain>/processed/**` | Data engineering | Canonical home for derived data products |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory intent clearly documented (“what belongs here” vs “what doesn’t”)
- [ ] Baseline manifest + artifact expectations described (even if formats are TBD)
- [ ] Sensitivity rules included (no secrets/PII; redaction expectations)
- [ ] Validation steps listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `tools/ai/drift/baselines/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Tools | `tools/` | Ops/dev utilities, scripts, docs (not large derived datasets) |
| Drift tooling | `tools/ai/drift/` | Drift detectors, docs, configs (tooling layer) |
| Telemetry contracts | `schemas/telemetry/` | JSON Schemas for telemetry signals (baseline + drift reports) |
| Derived data outputs | `data/<domain>/processed/` | Derived datasets (canonical; not under `src/`) |
| Run artifacts | `mcp/runs/` | Experiment/run logs + artifacts (preferred for large outputs) |

### Expected file tree for this sub-area
~~~text
📁 tools/
└── 📁 ai/
    └── 📁 drift/
        ├── 📄 README.md
        └── 📁 baselines/
            └── 📄 README.md   # (this file)

# Recommended (optional) structure if/when baselines are stored in-repo:
# (Only keep small, non-sensitive artifacts here; large artifacts belong in mcp/ or data/processed/)
#
# 📁 tools/ai/drift/baselines/
# ├── 📄 README.md
# ├── 📁 manifests/                 # baseline metadata (JSON/YAML)
# ├── 📁 stats/                     # summary stats (JSON)
# └── 📁 fixtures/                  # tiny test baselines only (optional)
~~~

## 🧭 Context

### Background
Drift monitoring compares a “current” dataset/model behavior against a known-good baseline.
Without stable baselines, drift metrics become difficult to interpret, audit, or reproduce across runs.

### Assumptions
- Baselines are created as part of a repeatable workflow (pipeline run or tooling command).
- Baseline artifacts are **versioned** and **traceable** to inputs (dataset IDs, run IDs, model IDs).
- This directory may contain **manifests and small fixtures**; it should not become a dumping ground for large outputs.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- **Data outputs are not code**: large derived artifacts should live under `data/<domain>/processed/` or `mcp/runs/`, not in `tools/` or `src/`.
- Baseline artifacts must not leak secrets, PII, or sensitive locations; store aggregated statistics and redacted forms only.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize a baseline manifest schema under `schemas/telemetry/`? | Contracts owners | TBD |
| Should baselines be represented as STAC Items (“evidence artifacts”)? | Catalog + governance | TBD |
| What is the baseline refresh cadence (monthly, per release, per source change)? | AI/Tooling | TBD |
| Where should large baseline artifacts be stored and referenced from manifests? | AI/Tooling + Data Eng | TBD |

### Future extensions
- Baseline registry exposed via API for discovery (read-only; contract-validated).
- CI gates that fail a PR if baseline schemas break compatibility.
- Drift signal surfacing in UI as **provenance-linked quality indicators** (not narrative claims).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  R[Reference window<br/>data/processed or mcp/runs] --> B[Baseline builder]
  B --> M[Baseline manifest<br/>(metadata + checksums)]
  B --> S[Baseline stats artifact<br/>(aggregates only)]

  C[Current window<br/>runtime/pipeline] --> D[Drift evaluator]
  M --> D
  S --> D
  D --> T[Telemetry drift report]
  T --> A[API surface / dashboards]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Pipeline as Pipeline/Run
  participant Baselines as Baseline Store
  participant Drift as Drift Evaluator
  participant Telemetry as Telemetry Sink

  Pipeline->>Baselines: Load baseline manifest + stats
  Pipeline->>Drift: Provide current-window features/outputs
  Drift->>Telemetry: Emit drift report (schema-validated)
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Reference window data | Parquet/CSV/JSON (TBD) | `data/<domain>/processed/` or `mcp/runs/` | Deterministic snapshot + checksums |
| Baseline configuration | YAML/JSON (TBD) | `tools/ai/drift/` | Schema-validated config (recommended) |
| Model reference (if applicable) | ID + version | Model registry or run metadata (TBD) | Must be explicit and stable |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Baseline manifest | JSON/YAML (recommended) | `tools/ai/drift/baselines/**` | `schemas/telemetry/**` (expected) |
| Baseline stats | JSON (recommended) | `tools/ai/drift/baselines/**` or external | Baseline schema (expected) |
| Drift report | JSON | `mcp/runs/**` or telemetry store | Drift-report schema (expected) |

### Sensitivity & redaction
- Prefer **aggregated** summaries: counts, histograms, quantiles, embedding centroids/dispersion, feature missingness rates.
- Avoid storing raw records or unredacted examples.
- If a sample is required for debugging, it must be:
  - very small,
  - de-identified/redacted,
  - reviewed under governance gates,
  - never used as a public artifact.

### Quality signals
- Manifest includes:
  - baseline ID, scope (domain/source/model), and time window
  - input dataset references (IDs/paths)
  - artifact checksums and schema versions
- Artifacts validate against telemetry schemas (recommended).
- Outputs are deterministic and diffable.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: (TBD — only if baselines are treated as evidence artifacts)
- Items involved: (TBD)
- Extension(s): (TBD)

### DCAT
- Dataset identifiers: baseline artifact may be a distribution of an existing DCAT dataset (TBD)
- License mapping: CC-BY-4.0 unless otherwise restricted by source constraints
- Contact / publisher mapping: (TBD)

### PROV-O
- `prov:wasDerivedFrom`: reference dataset snapshot / run artifact
- `prov:wasGeneratedBy`: baseline-build activity (run ID / pipeline activity)
- Activity / Agent identities: pipeline runner + reviewer identity (TBD)

### Versioning
- Baselines should be additive: prefer creating a new baseline version rather than overwriting.
- If overwriting is unavoidable, the manifest must record predecessor/successor linkage (TBD: exact mechanism).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Baseline builder | Create baseline stats from reference window | CLI/script (TBD) + schema output |
| Baseline store | Store manifests + small artifacts; point to large artifacts | Filesystem paths + checksums |
| Drift evaluator | Compare current window to baseline | Library API (TBD) |
| Telemetry sink | Persist drift reports for audit/CI | `mcp/runs/**` + telemetry schemas |
| API surface (optional) | Serve drift status to UI | `src/server/` contracts (TBD) |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Baseline manifest schema | `schemas/telemetry/` | Semver + changelog |
| Drift report schema | `schemas/telemetry/` | Semver + changelog |
| API contracts (if exposed) | `src/server/contracts/` | Contract tests required |

### Extension points checklist (for future work)
- [ ] Telemetry: baseline + drift report schemas under `schemas/telemetry/`
- [ ] Pipelines: baseline build step emits PROV activity metadata
- [ ] APIs: read-only drift status endpoint with contract tests
- [ ] UI: optional drift quality indicators (no unsourced narrative)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Baselines themselves are **internal quality infrastructure**.
- If surfaced at all, it should be as provenance-linked **quality/health signals**, not narrative claims.

### Provenance-linked narrative rule
- Any displayed claim about drift must trace to a drift report artifact + its provenance references.

### Optional structured controls
~~~yaml
# N/A by default for baselines. If drift signals are surfaced in Focus Mode later,
# this can be used to scope “quality overlays” or filters.
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter present; path matches)
- [ ] Schema validation (telemetry schemas if present)
- [ ] Baseline artifacts checksummed and referenced by manifest
- [ ] No secrets/PII checks (as applicable)
- [ ] Reproducibility note (reference window + run IDs recorded)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas (when present)
# <cmd> validate schemas/telemetry/

# 2) validate baseline manifests/artifacts
# <cmd> validate tools/ai/drift/baselines/

# 3) run tool/unit tests
# <cmd> test
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| baseline_build | Pipeline/tool run | `mcp/runs/**` (+ optional PROV) |
| drift_report | Drift evaluator | `mcp/runs/**` or telemetry store |
| baseline_registry (optional) | API layer | `src/server/` + contracts |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that add or modify **baseline artifacts** should be reviewed by:
  - AI/Tooling maintainers (correctness + reproducibility)
  - Governance reviewers when sensitive sources are involved

### CARE / sovereignty considerations
- Baselines can still leak sensitive patterns if derived from restricted data.
- When in doubt:
  - keep only aggregates,
  - generalize location/time,
  - store artifacts outside the repo under controlled access,
  - document restrictions in the manifest.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-22 | Initial baselines README (conventions + governance notes). | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`