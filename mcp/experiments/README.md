---
title: "🧪 MCP Experiments — Index & Rules (v11 LTS · Diamond⁹ Ω / Crown∞Ω)"
path: "mcp/experiments/README.md"
version: "v11.2.7"
last_updated: "2026-01-20"
status: "active"
doc_kind: "Index"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & MCP Board"
content_stability: "stable"

header_profile: "standard"
footer_profile: "standard"
intent: "mcp-experiment-index"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.7/signature.sig"
attestation_ref: "releases/v11.2.7/slsa-attestation.json"
sbom_ref: "releases/v11.2.7/sbom.spdx.json"
manifest_ref: "releases/v11.2.7/manifest.zip"

telemetry_ref: "releases/v11.2.7/mcp-experiments-telemetry.json"
telemetry_schema: "schemas/telemetry/mcp-experiments-v11.json"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"

semantic_document_id: "kfm-mcp-experiments-index"
event_source_id: "ledger:kfm:mcp:experiments:index:v11.2.7"
doc_uuid: "urn:kfm:mcp:experiments:index:v11.2.7"

machine_extractable: true
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "US-KS"

classification: "open"
sensitivity: "public"
fair_category: "FAIR+CARE"
care_label: "Mixed"

ai_transform_permissions:
  - "summarize"
  - "timeline_generation"
  - "semantic_highlighting"
  - "a11y_adaptations"
  - "metadata_extraction"
  - "layout_normalization"
ai_transform_prohibited:
  - "content_alteration"
  - "speculative_additions"
  - "narrative_fabrication"
  - "governance_override"
  - "provenance_fabrication"

provenance_chain:
  - "urn:kfm:mcp:experiments:index:v11.2.6"
  - "urn:kfm:mcp:experiments:index:v11.2.7"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# 🧪 MCP Experiments — Index & Rules (v11 LTS)

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Doc](https://img.shields.io/badge/doc-v11.2.7-blue)
![MCP--DL](https://img.shields.io/badge/MCP--DL-v6.3-6f42c1)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-governed-informational)
![License](https://img.shields.io/badge/license-CC--BY--4.0-lightgrey)

> 🔒 **This README is the canonical index + rules surface for MCP experiments.**  
> CI and policy gates are expected to treat these rules as **fail-closed** defaults (where feasible).

**Quick jump:** [📘 Overview](#-overview) · [🗂️ Directory Layout](#️-directory-layout) · [📦 Data--Metadata](#-data--metadata) · [🌐 STAC/DCAT/PROV](#-stac-dcat--prov-alignment) · [🧪 CI/CD](#-validation--cicd) · [⚖ Governance](#-faircare--governance)

---

## 📘 Overview

### Purpose
This README is the **canonical index** and **enforcement surface** for all experiment work under **MCP-DL v6.3**.

In KFM, an “experiment” is any bounded, reproducible activity that produces **new evidence artifacts** (datasets, models, metrics, evaluations, simulation outputs, derived layers, OCR corpora, etc.) that may later feed catalogs, graph, APIs, UI, Story Nodes, or Focus Mode. Evidence artifacts are treated as **first-class datasets** that must travel the canonical pipeline before use downstream.[^pipeline][^boundary-artifacts]

### Non‑negotiables (✅ MUST)
- ✅ **Pipeline ordering is absolute**: data cannot skip stages (ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode).[^pipeline]
- ✅ **Boundary artifacts first**: published outputs require STAC/DCAT/PROV records before graph/UI/story consumption.[^boundary-artifacts]
- ✅ **API boundary**: UI must never query Neo4j directly; all access goes through governed APIs.[^api-boundary]
- ✅ **Evidence-first narrative**: Story Nodes / Focus Mode must cite evidence; unsourced narrative is disallowed.[^evidence-first]
- ✅ **No fabrication in Focus Mode**: Focus Mode must cite sources and refuse to invent missing facts.[^focus-mode]
- ✅ **Sandbox ≠ published**: `data/work/**` (including simulation sandbox outputs) is not “official” until promoted to `data/processed/**` with catalogs.[^sandbox]
- ✅ **Contract-first metadata**: datasets are accepted via schemas + metadata contracts; “mystery layers” are not allowed.[^data-contract]

### Scope

| ✅ In Scope | 🚫 Out of Scope |
|---|---|
| Experiment records (IDs, intent, inputs/outputs, configs, seeds), run records/manifests, artifact locations, reproducibility rules, catalog/provenance expectations, governance + sensitivity guardrails, promotion policy. | Domain ETL recipes (live in `src/pipelines/**`), deployment/ops procedures (live in `tools/**`), unsourced narrative (belongs only in Story Nodes with evidence links), UI implementations (live in `web/**`). |

### Audience
- **Primary**: contributors running experiments (data engineering, modeling/AI, QA, pipeline maintainers).
- **Secondary**: governance reviewers, editors, and auditors validating reproducibility and provenance.

### Definitions (link to glossary)
- Glossary: `docs/glossary.md` *(recommended; confirm in repo)*  
- **Experiment**: a bounded investigation whose outputs are replayable + auditable.
- **Run record**: machine-readable execution log + config/environment snapshot stored under `mcp/runs/`.
- **Evidence artifact**: an output treated as **data + metadata** (STAC/DCAT/PROV) before it can appear downstream.[^boundary-artifacts]
- **Boundary artifacts**: STAC/DCAT/PROV bundles that act as the interface between data and downstream systems.[^boundary-artifacts]
- **Promotion**: moving an artifact from sandbox (`data/work/**`) to published (`data/processed/**`) **plus** emitting catalogs and provenance.[^sandbox]
- **Policy gate**: policy-as-code checks (e.g., OPA/Rego) that deny unsafe / noncompliant publication or exposure.[^opa]

### Key artifacts (what this document points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Experiments index (this doc) | `mcp/experiments/README.md` | MCP Board | Rules + index |
| Experiment records | `mcp/experiments/**` | Experiment owners | Folder or single-file mode |
| Run records | `mcp/runs/**` | MCP Board | Repro logs, configs, seeds, env locks |
| Telemetry bundle | `releases/<version>/mcp-experiments-telemetry.json` | MCP Board | Perf + sustainability |
| Policy pack (recommended) | `policy/**` | Governance | Conftest/OPA rules (repo path may vary) |
| STAC outputs | `data/stac/` | Catalog Maintainers | Items/Collections for spatial outputs |
| DCAT outputs | `data/catalog/dcat/` | Catalog Maintainers | Dataset/distribution discovery |
| PROV outputs | `data/prov/` | Catalog Maintainers | Lineage bundles |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (version pinned)
- [ ] **H2 structure matches the governed heading registry** (stable + automation-friendly)[^heading-registry]
- [ ] Rules are explicit (MUST/SHOULD) and CI-checkable
- [ ] Governance + sovereignty guardrails are stated
- [ ] Index table format is stable and automation-friendly
- [ ] Links point to canonical homes (no “mystery paths”)

### 📚 Project files used to update this README (traceability)
> These are the project “source packs” used to align this index with KFM v13+ standards, AI/UI behavior, governance, and experiment ops.

- 📘 Master Guide / pipeline invariants: :contentReference[oaicite:0]{index=0}  
- 🧾 Markdown best practices (Mermaid/Math/Details): :contentReference[oaicite:1]{index=1}  
- 📥 Data intake + promotion model: :contentReference[oaicite:2]{index=2}  
- 🏗️ Architecture + policy gates: :contentReference[oaicite:3]{index=3}  
- 🧭 AI system behavior (Focus Mode, audit panel, governance ledger): :contentReference[oaicite:4]{index=4}  
- 🖥️ UI system overview (Layer Info + provenance surface): :contentReference[oaicite:5]{index=5}  
- 🧱 Comprehensive technical documentation (contracts, licensing, storage): :contentReference[oaicite:6]{index=6}  
- 🌟 Latest ideas / future proposals (WPE + automation patterns): :contentReference[oaicite:7]{index=7}  
- 💓 “Pulse Ideas” (run_manifest pattern, CI gates, promotion policy): :contentReference[oaicite:8]{index=8}  
- 💡 Innovative concepts (cultural protocols + sovereignty patterns; 4D/AR/AI copilot ideas): :contentReference[oaicite:9]{index=9}  
- 🧠 AI reference portfolio (embedded library pack): :contentReference[oaicite:10]{index=10}  
- 🗄️ Data management + CI/CD + Bayesian methods portfolio: :contentReference[oaicite:11]{index=11}  
- 🗺️ Maps/WebGL/virtual worlds portfolio (viz + geospatial UI research): :contentReference[oaicite:12]{index=12}  
- 🧰 Programming languages/resources portfolio (tooling reference pack): :contentReference[oaicite:13]{index=13}  

---

## 🗂️ Directory Layout

### This document
- `path`: `mcp/experiments/README.md` (must match front-matter)

### Related repository paths (canonical homes)
| Area | Path | What lives here |
|---|---|---|
| 🧪 Experiments | `mcp/experiments/` | Experiment records + index |
| 🧾 Run logs | `mcp/runs/` | Replayable run logs + configs + seeds + env locks |
| 🪪 Model cards | `mcp/model_cards/` | Model docs + limitations + eval notes |
| 📥 Raw data | `data/raw/` | Immutable inputs (source snapshots) |
| 🧰 Working data | `data/work/` | Intermediate artifacts + sandbox outputs |
| ✅ Processed outputs | `data/processed/` | Published/derived datasets (cataloged) |
| 🧭 STAC | `data/stac/` | STAC Items/Collections |
| 🗃️ DCAT | `data/catalog/dcat/` | DCAT datasets/distributions |
| 🧬 PROV | `data/prov/` | PROV lineage bundles |
| 🧱 Pipelines | `src/pipelines/**` | ETL + normalization code |
| 🧠 Graph | `src/graph/**` | Neo4j ingestion + ontology ops |
| 🔌 API | `src/server/**` | Governed API boundary (contracts + redaction) |
| 🖥️ UI | `web/**` | React/Map UI (consumes API only) |

### Expected file tree for this sub-area
~~~text
📁 mcp/
├── 📁 experiments/
│   ├── 📄 README.md                               — Canonical index + rules (this file)
│   ├── 📄 YYYY-MM-DD_<DOMAIN>-EXP-###.md           — Experiment record (single-file mode)
│   └── 📁 YYYY/
│       └── 📁 YYYY-MM-DD_<DOMAIN>-EXP-###/
│           ├── 📄 README.md                        — Experiment record (folder mode)
│           ├── 📁 config/                          — Frozen configs (copies)
│           ├── 📁 results/                         — Figures/tables/maps (small, reviewable)
│           ├── 📁 notes/                           — Optional notes (no governance bypass)
│           └── 📁 refs/                            — Links to catalogs / run IDs / PRs
├── 📁 runs/
│   └── 📁 <run-id>/
│       ├── 📄 run_manifest.json                    — Machine manifest (required; see schema below)
│       ├── 📄 config.snapshot.json                 — Frozen config used (or pointer)
│       ├── 📄 env.lock                             — Environment capture (container digest, deps)
│       ├── 📄 stdout.log                           — Execution logs (redacted if needed)
│       ├── 📄 metrics.json                         — Key metrics (machine-readable)
│       ├── 📄 prov_activity.jsonld                 — PROV activity bundle pointer or inline
│       └── 📁 artifacts/                           — Small reviewable artifacts (hash-logged)
└── 📁 model_cards/
    └── 📄 README.md                               — Model cards index
~~~

---

## 🧭 Context

### Background
KFM treats experiments as **governed scientific work**: reproducible by design, provenance-linked by default, and safe for public release under FAIR+CARE and sovereignty constraints.[^pipeline][^boundary-artifacts]

### Constraints / invariants (must not regress)
- **Canonical pipeline ordering is preserved** (no stage may consume data that hasn’t passed the previous stage’s formal outputs + checks).[^pipeline]
- **API boundary rule**: UI never queries Neo4j directly; the API layer enforces redaction + access controls.[^api-boundary]
- **Provenance-first publishing**: data must be registered with provenance (STAC/DCAT/PROV) before graph/UI use.[^boundary-artifacts]
- **Determinism**: transformations should be idempotent + config-driven; randomness must be logged (seeds + params).[^pipeline]
- **Evidence-first narrative**: Story Nodes / Focus Mode must cite evidence; AI text must be identifiable and provenance-linked.[^evidence-first]
- **Policy gates exist at runtime + build time**: automated checks can deny unsafe/invalid outputs (including Focus Mode outputs).[^opa]

### Sandbox vs Published (important!)
- `data/work/**` is the **sandbox** and may include simulation runs and intermediate products.
- Only **promoted** artifacts in `data/processed/**` with STAC/DCAT/PROV boundary artifacts are considered publishable and eligible for graph/UI/story use.[^sandbox][^boundary-artifacts]

### WPE / agent automation context (optional but supported)
KFM includes an automation pattern (Watcher → Planner → Executor) that can propose and stage changes (including experiments) while remaining policy-bound (no policy-violating plans, and PR-based execution rather than “silent writes”).[^wpe]

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize on single-file vs folder-mode (or keep both permanently)? | MCP Board | TBD |
| Should `mcp/experiments/registry.json` be generated in CI as the canonical machine index? | MCP Board | TBD |
| Do we require per-run telemetry capture (in addition to release telemetry bundle)? | MCP Board | TBD |

### Future extensions (non-normative)
These are **allowed experiment tracks** if governed artifacts are produced:
- 🧊 **4D / temporal digital twin** experiments (time-aware simulation layers, scenario replay).[^innov-4d]
- 🥽 **AR / hybrid 3D storytelling** prototypes (UI experiments must remain API-bound + provenance-surfaced).[^innov-4d]
- 🧭 **AI co-pilot for geospatial query** (must be citation-gated + audit logged).[^focus-mode]

---

## 🗺️ Diagrams

### System / dataflow diagram (canonical)
~~~mermaid
flowchart LR
  A["Experiment record (mcp/experiments)"] --> B["Run record (mcp/runs)"]
  B --> C["Artifacts (data/raw|work|processed)"]
  C --> D["Boundary artifacts (STAC/DCAT/PROV)"]
  D --> E["Graph ingest (Neo4j)"]
  E --> F["API boundary (contracts + redaction)"]
  F --> G["UI surfaces (React/Map)"]
  G --> H["Story Nodes (governed narratives)"]
  H --> I["Focus Mode (evidence-linked)"]
~~~

### Experiment lifecycle (recommended)
~~~mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> Active: "Run(s) executed + run records"
  Active --> Validated: "Checks pass (schema + policy + provenance)"
  Validated --> Promoted: "data/processed + STAC/DCAT/PROV"
  Promoted --> Published: "Graph/API/UI/Story eligible"
  Active --> Blocked: "Missing inputs / failed gates"
  Blocked --> Active: "Fix + re-run"
  Published --> Archived: "Superseded / deprecated"
~~~

---

## 📦 Data & Metadata

### What counts as an experiment
An activity **MUST** be recorded as an MCP experiment if it produces any of the following:
- new derived datasets (tables/rasters/vectors/time series),
- trained or fine-tuned models,
- evaluation results (benchmarks, ablations, bias audits),
- transformations that change interpretation-ready outputs (harmonization, masking/generalization, datum conversions),
- AI-assisted artifacts intended to influence Story Nodes or Focus Mode,
- simulation layers intended for analysis or “what-if” exploration.[^boundary-artifacts]

### Experiment ID and naming
**Supported patterns**
- **Single-file mode:** `YYYY-MM-DD_<DOMAIN>-EXP-###.md`
- **Folder mode:** `YYYY/YYYY-MM-DD_<DOMAIN>-EXP-###/README.md`

**Domain codes (non-exhaustive)**
- `CLIMATE`, `HYDRO`, `GEO`, `SOILS`, `AI`, `NLP`, `ARCH`, `HAZARD`, `STORY`, `PIPELINE`, `GRAPH`, `UI`, `SIM`

### Minimum required contents for an experiment record (✅ MUST)
Each experiment record MUST include:
- **Identity:** experiment ID, date, domain, owner/agent(s), status
- **Objective:** hypothesis/question, success criteria
- **Inputs:** dataset IDs/paths + checksums (or references to manifests)
- **Method:** steps + parameters + seed(s) + environment notes
- **Outputs:** artifact paths + intended catalog actions (STAC/DCAT/PROV)
- **Results:** key metrics, plots/tables (or links), uncertainty/limitations
- **Governance:** sensitivity notes, sovereignty handling, CARE notes, license/attribution notes
- **Provenance pointers:** run record ID(s) + lineage bundle reference(s)
- **Promotion plan:** what goes to `data/processed/**` vs what stays sandbox (`data/work/**`)[^sandbox]

### Run records (✅ MUST) — required fields
Run records exist to make experiments replayable and auditable. A run record MUST capture:
- `run_id` (unique, stable)
- `experiment_id` (link back to experiment record)
- `code_ref` (commit SHA + repo state)
- `config_snapshot` + `env_lock` (or stable pointers)
- `inputs[]` with checksums
- `outputs[]` with checksums + intended catalogs
- `seeds[]` and non-default parameters
- `metrics` summary + pointer to full metrics
- `prov_activity` pointer (or inline) linking inputs → activity → outputs

### Recommended `run_manifest.json` (machine contract)
> This is a **recommended** minimum contract shape for MCP runs; it is designed to support promotion, provenance, CI, and later graph ingest.[^runmanifest]

~~~json
{
  "run_id": "run-2026-01-20T120000Z-ai-exp-001",
  "experiment_id": "2026-01-20_AI-EXP-001",
  "code": { "commit": "<sha>", "dirty": false },
  "config": { "snapshot_path": "mcp/runs/<run-id>/config.snapshot.json" },
  "env": { "lock_path": "mcp/runs/<run-id>/env.lock", "container_image": "<digest>" },
  "inputs": [{ "uri": "data/raw/<domain>/...", "checksum": "sha256:..." }],
  "outputs": [{
    "uri": "data/work/<domain>/... or data/processed/<domain>/...",
    "checksum": "sha256:...",
    "catalogs_intended": ["stac","dcat","prov"]
  }],
  "metrics": { "path": "mcp/runs/<run-id>/metrics.json" },
  "provenance": { "prov_path": "data/prov/<bundle>.jsonld" },
  "governance": { "classification": "public|restricted", "sensitivity": "low|med|high" }
}
~~~

### Suggested (optional) experiment record skeleton
~~~yaml
# (Place in the experiment record, not in this README.)
experiment_id: "2026-01-20_AI-EXP-001"
domain: "AI"
status: "draft|active|completed|blocked|archived"
owners:
  - "handle-or-team"
run_records:
  - "mcp/runs/<run-id>/"
inputs:
  - "data/raw/<domain>/... (checksum: sha256:...)"
outputs:
  - "data/work/<domain>/... (sandbox)"
  - "data/processed/<domain>/... (publishable; intended catalogs: stac|dcat|prov)"
seeds:
  - 1337
contracts:
  stac_profile: "KFM-STAC v11.0.0"
  dcat_profile: "KFM-DCAT v11.0.0"
  prov_profile: "KFM-PROV v11.0.0"
promotion:
  planned: true
  gate_summary: "schema + policy + provenance + license + sensitivity"
~~~

### Index of experiments
This table is intended to remain **automation-friendly** (stable columns, minimal formatting).

| Experiment ID | Title | Domain | Start date | Status | Primary outputs |
|---:|---|---|---:|---|---|
| _none_ | — | — | — | — | — |

---

## 🌐 STAC, DCAT & PROV Alignment

### Required policy
Every new dataset or evidence artifact MUST be represented by:
- **STAC** (Items/Collections for geospatial outputs),
- **DCAT** (dataset/distribution discovery),
- **PROV-O** (lineage: inputs → activity → outputs),
before it is used downstream (graph/API/UI/story).[^boundary-artifacts]

### STAC
Experiments that produce spatial assets SHOULD emit STAC Items (and update/attach to an appropriate Collection):
- Spatial datasets: STAC Item with geometry/bbox/time.
- Non-spatial artifacts: STAC Item MAY use `geometry: null` with clear asset metadata.

### DCAT
Experiments producing publishable datasets SHOULD register a DCAT dataset record and distributions (formats, access methods).

### PROV-O
Experiments that transform data MUST produce provenance lineage linking:
- raw inputs (`prov:used` / `prov:wasDerivedFrom`)
- run/activity (`prov:wasGeneratedBy`)
- outputs (with stable IDs + checksums)

> 🧬 **Advanced (allowed):** Treat GitHub PRs as provenance-bearing activities (e.g., PR as `prov:Activity`, reviewers as `prov:Agent`), when PRs are the controlled mechanism for promotion and publication.[^wpe]

### Cross-layer linkage expectations (recommended)
To prevent drift between catalogs, graph, and UI:
- STAC Items should link to DCAT distributions (or vice versa),
- PROV bundles should reference the STAC/DCAT identifiers,
- graph ingestion should store references back to catalog IDs (not re-host “mystery” metadata).[^boundary-artifacts]

### Canonical locations
~~~text
📁 data/
├── 📁 stac/                 — STAC collections + items
├── 📁 catalog/dcat/         — DCAT datasets + distributions
└── 📁 prov/                 — PROV bundles (lineage)
~~~

---

## 🧱 Architecture

### Components touched by experiments
| Component | Responsibility | Interface |
|---|---|---|
| Experiment record | Human-readable + reviewable log | Markdown file(s) in `mcp/experiments/` |
| Run record | Replayable execution record | `mcp/runs/<run-id>/` + `run_manifest.json` |
| Artifact store | Data outputs | `data/{raw,work,processed}/**` |
| Catalogs | Discovery + lineage | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Contracts | Validation schemas | `schemas/**` |
| Policy layer | Deny unsafe publication/exposure | OPA/Rego via CI/runtime (path TBD) |

### Interfaces / contracts (expectations)
- Experiments MUST reference:
  - dataset locations under `data/**`,
  - run logs under `mcp/runs/**`,
  - catalog outputs under `data/{stac,catalog/dcat,prov}/**` where applicable.
- Experiments MUST NOT imply:
  - UI consumption of Neo4j directly (API boundary),
  - narrative publication without evidence and review.

### Large artifacts (storage reality check)
- Large/high-volume outputs should be stored in dedicated stores (e.g., object storage) and **referenced** via catalogs/manifests rather than embedded in markdown or committed as opaque blobs.[^storage]

---

## 🧠 Story Node & Focus Mode Integration

Experiments that generate or modify Story Nodes MUST:
- separate **facts** vs **interpretation** vs **hypotheses**,
- include evidence IDs (STAC/DCAT/PROV/document identifiers),
- apply sovereignty-first handling (generalize/mask sensitive locations by default),
- route final narrative through Story Node review gates (no direct Focus Mode injection).[^evidence-first]

Focus Mode rules (hard gate):
- Focus Mode must include citations and refuse to fabricate missing information.[^focus-mode]
- Focus Mode should surface explainability + governance flags via an audit panel when applicable.[^focus-audit]
- UI should expose provenance context (Layer Info + provenance panel) so users can see “the map behind the map.”[^layer-provenance]

---

## 🧪 Validation & CI/CD

### Minimum CI expectations (v11 LTS baseline)
- ✅ Filename/pattern checks for experiment records.
- ✅ Markdown protocol checks (single H1; stable H2 registry; mermaid fences validate).
- ✅ Required experiment metadata presence (ID, dates, run record refs, inputs/outputs).
- ✅ Provenance expectations where outputs are produced (PROV refs + checksums).
- ✅ Secret/PII scanning + sovereignty checks for sensitive location leakage.
- ✅ Policy-as-code gate (OPA/Rego) for publication/exposure decisions.[^opa]

### Recommended CI “profiles” (practical)
- 🧾 **Doc gates**: markdown lint, heading registry, link integrity, diagram lint.
- 🧬 **Data gates**: schema validation, checksums, STAC/DCAT/PROV completeness.
- 🧠 **Model gates**: eval reproducibility, bias checks, drift checks (where relevant).
- 🕸️ **Graph gates**: constraints + integrity queries (no orphan nodes, required props).
- 🔐 **Security gates**: secret scan, dependency/SBOM scan, policy deny tests.

### Example: domain CI gate pattern (from Pulse)
A domain module may define a dedicated CI check (example: “air fusion CI gate”) to validate ingest outputs before promotion.[^ci-gate]

### Local checklist (author)
- [ ] Experiment record created and filled
- [ ] Config snapshot captured (or referenced) + seed(s) recorded
- [ ] Run record created under `mcp/runs/` (with `run_manifest.json`)
- [ ] Outputs stored under `data/**` (sandbox vs published clearly separated)
- [ ] Catalog updates planned/emitted (STAC/DCAT/PROV) where applicable
- [ ] Governance notes included (sensitivity + sovereignty + license/attribution)
- [ ] Policy gates passed (or exceptions recorded + approved)

---

## ⚖ FAIR+CARE & Governance

### FAIR+CARE notes
- **FAIR profile:** evidence artifacts must be findable + attributable via catalogs (STAC/DCAT) and lineage (PROV).[^boundary-artifacts]
- **CARE label:** this index is `Mixed` because experiments may span multiple sensitivity regimes.

### Sovereignty, cultural protocols, and sensitive locations
- Default posture: **do not publish precise coordinates** for culturally sensitive resources.
- Prefer generalized representations (H3/grid, buffered extents, redacted geometry) when risk exists.
- Support **cultural protocols / TK label** thinking where communities require differentiated access (open → restricted) and evolving permissions.[^cultural-protocols]
- If an experiment touches Tier-A or culturally sensitive datasets, request governance review per policy.

### Licenses and attribution (minimum)
- Experiments MUST record source licenses and respect usage constraints; this is a core trust and collaboration requirement for KFM.[^license]

### Required approvals (when applicable)
- [ ] FAIR+CARE Council review (sensitivity high, Tier-A, cultural/heritage)
- [ ] Security review (secrets, access tokens, restricted endpoints, threat model changes)
- [ ] Editorial review (Story Node publication)

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| v11.2.7 | 2026-01-20 | Aligned MCP experiments with v13 “boundary artifacts” + inviolable pipeline ordering; clarified sandbox→promotion rule; added `run_manifest.json` contract pattern; expanded policy gate + WPE alignment; added traceable project source pack list. |
| v11.2.6 | 2025-12-28 | Re-structured to universal governed-doc layout; normalized canonical paths; strengthened reproducibility + catalog/provenance expectations; removed HTML-only centering in favor of protocol-safe Markdown. |
| v11.2.5 | 2025-12-12 | Prior baseline draft. |

---

[⬅️ MCP Home](../README.md) · [📘 Master Guide](../../docs/MASTER_GUIDE_v13.md) · [🏛️ Governance Charter](../../docs/governance/ROOT_GOVERNANCE.md)

© 2026 Kansas Frontier Matrix — CC-BY-4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

---

### Footnotes (evidence links)
[^pipeline]: Canonical pipeline ordering + inviolable staging constraints are explicitly specified in the v13 Master Guide draft. :contentReference[oaicite:14]{index=14}
[^api-boundary]: API boundary rule (UI never queries Neo4j directly; governed API layer enforces access controls/redaction). :contentReference[oaicite:15]{index=15}
[^boundary-artifacts]: STAC/DCAT/PROV “boundary artifacts” are required before data is considered fully published and usable downstream. :contentReference[oaicite:16]{index=16}
[^evidence-first]: Evidence-first narrative requirement (no unsourced narrative; claims cite evidence; AI text identified + provenance-linked). :contentReference[oaicite:17]{index=17}
[^focus-mode]: Focus Mode must cite sources and refuses to fabricate missing facts. :contentReference[oaicite:18]{index=18}
[^focus-audit]: Explainable AI / audit panel concept (factor attribution + governance flags). :contentReference[oaicite:19]{index=19}
[^sandbox]: Simulation outputs in `data/work/sims` are sandbox-only and must be promoted (with validation/provenance) before being considered official. 
[^opa]: Policy gate concept using OPA (including runtime gating of Focus Mode outputs). :contentReference[oaicite:21]{index=21}
[^runmanifest]: Example run manifest structure for runs/artifacts/metrics/provenance. 
[^heading-registry]: Approved H2 heading registry pattern used for governed docs. 
[^ci-gate]: Example of defining domain-specific CI gates (pattern). 
[^data-contract]: Data contract requirement for ingest/outputs via metadata JSON (schema-first; no black-box layers). :contentReference[oaicite:25]{index=25}
[^layer-provenance]: UI provenance surfaces (Layer Info + provenance panel / active layers). :contentReference[oaicite:26]{index=26}
[^storage]: Guidance on storing high-volume artifacts in dedicated stores and referencing via catalogs/metadata. :contentReference[oaicite:27]{index=27}
[^wpe]: WPE agent pattern is policy-bound (planner avoids policy violations; executor stages changes via PRs). :contentReference[oaicite:28]{index=28}:contentReference[oaicite:29]{index=29}
[^cultural-protocols]: Cultural protocols/TK labels and differentiated access concepts for sovereignty-aware governance. :contentReference[oaicite:30]{index=30}
[^license]: Licensing care as a core design/operational concern for safe adoption and collaboration. :contentReference[oaicite:31]{index=31}
[^innov-4d]: 4D digital twin + AR/hybrid storytelling concepts as optional experiment tracks (non-normative). :contentReference[oaicite:32]{index=32}
