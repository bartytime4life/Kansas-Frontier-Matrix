<!--
🧪 TEMPLATE__EXPERIMENT_LOG.md
📍 Copy this file into: mcp/experiments/EXP-###--<slug>/README.md
✅ Then: fill 🔴 REQUIRED sections + commit alongside your code/config/artifacts.

Hard gates (KFM invariants):
- 🚫 No “mystery layers” / unsourced outputs.
- 🧾 Anything that reaches Graph/API/UI/Story/Focus must be provenance-linked (STAC + DCAT + PROV).
- 🧱 UI must not query Neo4j directly — always via governed API (redaction + classification).
-->

---
doc_id: "EXP-000"
title: "🧪 EXP-000 — <Short, specific experiment title>"
path: "mcp/experiments/EXP-000--<slug>/README.md"
status: "draft" # draft | running | paused | complete | shipped | abandoned
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
owners:
  - "<name_or_handle>"
reviewers:
  - "<optional>"
tags:
  - "mcp"
  - "experiment"
  - "<domain_tag>"        # e.g., air-quality | land-treaties | soils | ui | ai | ingest
risk: "low"               # low | medium | high
kfm:
  target_version: "v13"
  pipeline_stage:
    - "<etl|catalogs|graph|api|ui|story|focus|wpe_agents>"
  components_touched:
    - "<FastAPI|Neo4j|PostGIS|MapLibre|Cesium|STAC|DCAT|PROV|PolicyPack|WPE>"
related:
  issues: ["<issue_link_or_id>"]
  prs: ["<pr_link_or_id>"]
  adrs: ["<optional ADR path>"]
  story_nodes: ["<SN-### if relevant>"]
  pulse_threads: ["<PT-### if relevant>"]
artifacts:
  run_manifest: "data/audits/<run_id>/run_manifest.json"
  evidence_manifest: "data/evidence/EM-<id>.yml"
  prov_bundle: "data/prov/<run_id>.jsonld"
  stac:
    collections: ["data/stac/collections/<collection>.json"]
    items: ["data/stac/items/<item>.json"]
  dcat: ["data/catalog/dcat/<dataset>.jsonld"]
  oci:
    - "oci://<registry>/<repo>:<tag>@sha256:<digest>"
repro:
  git_commit: "<sha>"
  git_branch: "<branch>"
  container_image: "<image>@sha256:<digest>"
  seeds:
    python: 0
    numpy: 0
    torch: 0
    other: {}
  hardware:
    cpu: "<model>"
    ram_gb: <int>
    gpu: "<model|none>"
policy:
  pack_ref: "<tag_or_commit>"
  conftest_report: "mcp/experiments/EXP-000--<slug>/policy/conftest.json"
  waivers: "mcp/experiments/EXP-000--<slug>/policy/waivers.yml"
---

# 🧪 Experiment Log — EXP-000: <Short title>

[![KFM](https://img.shields.io/badge/KFM-v13-blue)](#)
[![Status](https://img.shields.io/badge/status-draft-lightgrey)](#)
[![Risk](https://img.shields.io/badge/risk-low-brightgreen)](#)
[![Reproducible](https://img.shields.io/badge/reproducible-yes-brightgreen)](#)
[![Policy%20Pack](https://img.shields.io/badge/policy_pack-pending-lightgrey)](#)

> 🔴 **Hard Gate:** If it shows up in **UI** or **Focus Mode**, it must be traceable to **cataloged sources** with **STAC/DCAT/PROV** (and pass Policy Pack). No exceptions.  
> 🧭 **Pipeline reminder:** ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode

---

## 🧭 Quick Start

- [ ] Copy template → `mcp/experiments/EXP-###--<slug>/README.md`
- [ ] Fill **Snapshot** + **Hypothesis & Goals** + **Inputs/Evidence** + **Design** + **Results**
- [ ] Add (or link) **Run Manifest**, **Evidence Manifest**, **PROV bundle**, and policy outputs
- [ ] Record **Decision** + **Next steps**
- [ ] Ensure a second person can reproduce from this log ✅

---

## 🗂️ Suggested Experiment Folder Layout

```text
mcp/experiments/EXP-000--<slug>/
├─ 📄 README.md                 # 👈 this log 📌 Experiment overview + timeline + links to key artifacts/results
├─ 📓 notebooks/                # (optional) Exploratory notebooks (keep runnable; reference pinned env/manifests)
├─ 🛠️ src/                      # Scripts used for runs (deterministic entrypoints; prefer CLI-friendly)
├─ ⚙️ config/                   # Configs/prompts/detector settings (versioned; no secrets)
├─ 🧪 data_samples/             # Small fixtures only (no restricted/PII; include license notes)
├─ 📦 outputs/                  # Outputs for review (plots, tables, exports, screenshots; promote “final” elsewhere if needed)
├─ 🛡️ policy/                   # Policy evidence (conftest reports, waivers, gate summaries)
└─ 📝 notes/                    # Meeting notes, reviewer comments, decisions-in-progress (human collaboration)
```

---

## 📌 Snapshot (Fill First) 🔴

| Field | Value |
|---|---|
| Experiment ID | `EXP-000` |
| One-liner | `<What are we testing, in one sentence?>` |
| Stage | `<etl|catalogs|graph|api|ui|story|focus|wpe_agents>` |
| Baseline | `<what exists today?>` |
| Variant(s) | `<what changes?>` |
| Success threshold | `<explicit go/no-go threshold>` |
| Primary metric(s) | `<e.g., F1, RMS error, latency, citation coverage>` |
| Data sensitivity | `<public|internal|restricted>` |
| Decision target date | `YYYY-MM-DD` |
| Final decision | `<go|no-go|go-with-conditions|tbd>` |

---

## 🧠 1) Executive Summary 🔴

### What we did
<2–5 sentences>

### What we found
<2–5 sentences>

### Why it matters to KFM
<connect to: evidence-first + provenance-first + UX + governance>

---

## 🎯 2) Hypothesis, Goals, and Non-Goals 🔴

### Hypothesis
- **If** `<change>`  
- **then** `<measurable outcome>`  
- **because** `<mechanism / reasoning>`  

### Goals (measurable)
- [ ] G1: `<metric + threshold>`
- [ ] G2: `<metric + threshold>`

### Non-goals (explicitly out of scope)
- [ ] NG1: `<what we are not trying to prove>`
- [ ] NG2: `<what we are not changing>`

---

## 🧩 3) System Context (Where this plugs into KFM) 🔴

### KFM subsystems touched
Check all that apply:

- [ ] 🧱 ETL / pipelines (`data/raw → data/work → data/processed`)
- [ ] 🌐 Catalogs (STAC / DCAT / PROV “evidence triplet”)
- [ ] 🕸️ Graph (Neo4j nodes/edges; ontology constraints)
- [ ] 🔌 API (FastAPI / GraphQL contracts, redaction enforcement)
- [ ] 🗺️ UI (React + MapLibre (+ optional Cesium), timeline, layer panels)
- [ ] 🧾 Story Nodes (governed narrative artifacts)
- [ ] 🧠 Focus Mode (provenance-linked context bundle + citations hard gate)
- [ ] 🤖 W‑P‑E agents (Watcher–Planner–Executor automation)
- [ ] ⚖️ Policy Pack (OPA/Rego + Conftest in CI)
- [ ] 📡 Telemetry (OpenTelemetry traces, energy/carbon metrics)

### User personas impacted
- [ ] Researchers / analysts
- [ ] Educators / students
- [ ] Maintainers / curators
- [ ] Contributors (data/code)
- [ ] Public viewers

### Compatibility + invariants checklist (must not break)
- [ ] UI does **not** query Neo4j directly (API boundary preserved)
- [ ] Outputs shown to users have STAC/DCAT/PROV + license
- [ ] Any AI-generated artifact is flagged + has provenance + confidence metadata
- [ ] No policy downgrades (classification cannot silently become “more public”)

---

## 📚 4) Project Reference Docs Used (check what you relied on) 🟡

> ✅ The point: make it easy to audit “what informed this experiment” and to replicate reasoning.

KFM core docs:
- [ ] Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation
- [ ] Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design
- [ ] Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖
- [ ] Kansas Frontier Matrix – Comprehensive UI System Overview
- [ ] 📚 KFM Data Intake – Technical & Design Guide
- [ ] 🌟 KFM – Latest Ideas & Future Proposals
- [ ] Innovative Concepts to Evolve KFM
- [ ] Additional Project Ideas
- [ ] MARKDOWN_GUIDE_v13 / Master Guide (pipeline invariants + doc protocol)

Reference libraries / cookbooks (as needed):
- [ ] AI Concepts & more (portfolio)
- [ ] Maps / Google Maps / Virtual Worlds / Archaeological / WebGL (portfolio)
- [ ] Data Management / Data Science / Bayesian Methods (portfolio)
- [ ] Data Mining Concepts & Applications
- [ ] Python Geospatial Analysis Cookbook (PostGIS/topology/routing/WebGIS)

External references (papers, standards, specs, URLs):
- <add here>

---

## 🧾 5) Inputs, Data, and Evidence 🔴

### 5.1 Data sources
List **every** input (raw + intermediate + external APIs) with identifiers.

| Input | Type | Location / ID | License | Sensitivity | Notes |
|---|---|---|---|---|---|
| `<source_1>` | `<raster|vector|table|text|api>` | `<path or URL or dataset_id>` | `<license>` | `<public/internal/restricted>` | `<notes>` |

### 5.2 Catalog + provenance IDs (the “evidence triplet”)
- **STAC Collection(s):** `<collection IDs / file paths>`
- **STAC Item(s):** `<item IDs / file paths>`
- **DCAT Dataset(s):** `<dataset IDs / file paths>`
- **PROV bundle(s):** `<prov IDs / file paths>`

### 5.3 Data sensitivity & governance
- **Classification:** `<public/internal/restricted>`
- **Sovereignty/CARE flags:** `<yes/no + details>`
- **PII / sensitive locations present?:** `<yes/no>`
- **Redaction/generalization plan:** `<how + where enforced (API/pipeline)>`

> ✅ Include any required council review triggers, domain steward sign-off, or required SOP references.

---

## 🧪 6) Experimental Design 🔴

### 6.1 Baseline vs Variant(s)
- **Baseline:** `<control system behavior>`
- **Variant A:** `<what changes>`
- **Variant B:** `<optional>`

### 6.2 Variables and controls
- **Independent variable(s):** `<what you vary>`
- **Dependent variable(s):** `<what you measure>`
- **Controls:** `<what must be held constant>`

### 6.3 Sampling plan
- Spatial scope: `<Kansas statewide|county|bbox>`
- Temporal scope: `<YYYY-MM-DD..YYYY-MM-DD>`
- Stratification: `<county strata, era strata, sensor type, etc.>`
- Sample size rationale: `<why this size is enough>`

### 6.4 Metrics (define precisely)
> 🔴 Define metrics so someone else computes them the same way.

| Metric | Definition | Computation | Threshold | Notes |
|---|---|---|---|---|
| `<metric>` | `<what it means>` | `<formula / procedure>` | `<pass/fail>` | `<notes>` |

Common metric starters (use as relevant):
- 🧠 ML/AI: accuracy, precision/recall/F1, citation coverage, refusal rate, hallucination rate
- 🗺️ Geospatial: RMS georeferencing error, topology validity, CRS consistency, bbox correctness
- ⚡ Performance: API latency p50/p95, tile load time, UI FPS, memory, build time
- 🧾 Governance: % outputs with license + provenance, policy violations, waiver count
- ♻️ Sustainability: runtime, energy usage, carbon estimate, trace coverage %

### 6.5 Statistical analysis plan (optional but recommended) 🟡
- Approach: `<frequentist|bayesian|mixed>`
- Confidence/credible intervals: `<what you’ll report>`
- Multiple comparisons handling: `<if any>`
- Stopping rule / early exit: `<if any>`

---

## 🧱 7) Implementation Details & Run Configuration 🔴

### 7.1 Code + config references
- Commit: `<sha>`
- Branch: `<branch>`
- Key files changed: `<paths>`
- Config files used: `<paths>`
- Seeds: `<list seeds + rationale>`

### 7.2 Environment / reproducibility
- Runtime: `<python/node/docker/k8s>`
- Dependencies: `<requirements.txt / lockfile / image digest>`
- Hardware: `<CPU/GPU/RAM>`
- OS: `<os + version>`

### 7.3 Run Manifest + idempotency (required for governed runs)
- `run_id`: `<RUN-YYYYMMDD-#### or similar>`
- `run_manifest.json` path: `data/audits/<run_id>/run_manifest.json`
- Canonical digest (idempotency key): `<sha256:...>`
- Logs: `<path to NDJSON logs / traces>`
- OCI artifact refs (if used): `oci://...@sha256:...`
- Signatures (Cosign): `<yes/no + where>`

### 7.4 Policy Pack results
- Conftest report: `<path>`
- Waivers: `<path>`
- Notes: `<what rules fired + why>`

### 7.5 If W‑P‑E agents are involved (Watcher–Planner–Executor) 🟡
- Watcher: `<what it watches + polling strategy (ETag/Last-Modified/etc.)>`
- Planner: `<plan output + constraints>`
- Executor: `<actions performed + safety rails + approvals required>`
- Human approval points: `<what required review gates exist>`

### 7.6 If Focus Mode / AI is involved 🟡
- Model(s): `<name + version>`
- Retrieval config: `<vector store/graph queries/filters>`
- Prompt templates: `<path>`
- Citation strategy: `<how sources are attached>`
- Guardrails: `<prompt security, tool allowlist, refusals>`
- Drift monitoring hooks: `<what is monitored + thresholds>`

---

## 🧾 8) Execution Log (What actually happened) 🔴

> ✅ Keep this chronological and boring. Boring = reproducible.

### Timeline
| Time (local/UTC) | Step | Operator | Result |
|---|---|---|---|
| `YYYY-MM-DD HH:MM` | `<step>` | `<name|bot>` | `<ok|warn|fail>` |

### Commands / procedures
```bash
# Example:
# make exp-run EXP=EXP-000
# python -m src.run --config config/exp.yaml --run-id RUN-...
```

### Deviations from plan (and why)
- `<deviation + rationale>`

### Errors, warnings, and mitigations
- `<error>` → `<fix>`

---

## 📈 9) Results 🔴

### 9.1 Outcome vs success thresholds
| Goal | Metric | Threshold | Observed | Pass? |
|---|---|---:|---:|---|
| G1 | `<metric>` | `<x>` | `<y>` | ✅/❌ |
| G2 | `<metric>` | `<x>` | `<y>` | ✅/❌ |

### 9.2 Quantitative results
- Tables: `<link to outputs/>`
- Charts: `<link to outputs/>`
- Benchmarks: `<p50/p95, fps, etc.>`

### 9.3 Qualitative findings (what surprised us)
- `<bullets>`

### 9.4 Artifacts produced (must be traceable)
| Artifact | Type | Path / ID | Cataloged? | Notes |
|---|---|---|---|---|
| `<artifact>` | `<layer/report/model>` | `<path>` | ✅/❌ | `<notes>` |

### 9.5 Evidence integrity checks
- [ ] Outputs hash recorded
- [ ] STAC/DCAT/PROV generated or updated
- [ ] Licenses present and correct
- [ ] Any AI-generated output marked as AI-generated
- [ ] API/UI exposure respects classification + redaction

---

## ✅ 10) Validation, QA, and Peer Review 🔴

### 10.1 Reproduction attempt(s)
| Reproducer | Date | Environment | Match? | Notes |
|---|---|---|---|---|
| `<name>` | `YYYY-MM-DD` | `<env>` | ✅/❌ | `<notes>` |

### 10.2 Review notes
- Reviewer: `<name>` — `<summary>`
- Reviewer: `<name>` — `<summary>`

### 10.3 CI / QA gates executed
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Link checks (docs + catalogs + story references)
- [ ] Graph integrity tests (constraints, orphan nodes, ontology)
- [ ] API contract tests (OpenAPI/GraphQL)
- [ ] Security scans (secrets, PII, sensitive locations)
- [ ] Policy Pack (Conftest) pass or waivers filed
- [ ] Telemetry present (traces + energy/carbon, if required)

---

## ⚖️ 11) Governance, Ethics, and Security Review 🔴

### FAIR checklist (Findable/Accessible/Interoperable/Reusable)
- [ ] Findable: catalog entries are complete + discoverable
- [ ] Accessible: distributions available with proper access controls
- [ ] Interoperable: open formats + standards alignment
- [ ] Reusable: license + provenance + context are explicit

### CARE checklist (Collective Benefit / Authority to Control / Responsibility / Ethics)
- [ ] Collective Benefit considered
- [ ] Authority to Control honored (community/indigenous/sensitive constraints)
- [ ] Responsibility (stewardship, accountability, escalation path)
- [ ] Ethics (harm analysis, mitigation, opt-outs)

### Privacy / sensitive data (if relevant)
- Data types present: `<identifiers/quasi-identifiers/sensitive attributes>`
- Controls: `<anonymization/generalization/access gating>`
- Risk of inference/leakage: `<assessment>`

### Security notes
- Threat model notes: `<brief>`
- Prompt security tests (if AI): `<jailbreak attempts, tool misuse, data exfil tests>`
- Waivers used?: `<yes/no + IDs + expiry>`

---

## 🧭 12) Impact Assessment (Downstream effects) 🔴

### 12.1 Data + catalogs impact
- New/changed datasets: `<list>`
- Catalog changes: `<STAC/DCAT/PROV files updated>`
- Versioning notes: `<semantic versioning, dataset version bumps>`

### 12.2 Graph + ontology impact
- New node labels / relationship types: `<list>`
- Migrations required?: `<yes/no + link>`
- Constraint changes: `<list>`
- “No mystery nodes” preserved?: ✅/❌

### 12.3 API impact
- New endpoints / contract changes: `<list>`
- Backwards compatible?: ✅/❌
- Version bump needed?: `<yes/no>`

### 12.4 UI impact (MapLibre / Cesium / Timeline / Story)
- Layer behavior changes: `<list>`
- Performance (FPS, tile load time): `<numbers>`
- Accessibility checks: `<keyboard nav, contrast, focus order>`

### 12.5 Observability + sustainability
- OpenTelemetry trace coverage: `<%>`
- Energy usage: `<kWh or estimate>`
- Carbon estimate: `<kgCO2e or estimate>`
- Any SLO regressions?: `<yes/no>`

### 12.6 Rollback plan
- Trigger for rollback: `<conditions>`
- Rollback steps: `<commands / PR revert>`
- Data rollback: `<how catalogs/graph are reverted safely>`

---

## 🟢 13) Decision & Next Steps 🔴

### Decision
- **Decision:** `<go|no-go|go-with-conditions|abandoned>`
- **Rationale:** `<tight explanation>`
- **Decision owner:** `<name>`
- **Date:** `YYYY-MM-DD`

### Conditions (if “go-with-conditions”)
- [ ] C1: `<condition>`
- [ ] C2: `<condition>`

### Next steps / TODOs
- [ ] `<task>` → owner `<name>` → due `YYYY-MM-DD`
- [ ] `<task>` → owner `<name>` → due `YYYY-MM-DD`

---

## 📎 Appendices (Optional but 🔥 useful)

<details>
<summary>📦 Appendix A — Run Manifest Skeleton (JSON)</summary>

```json
{
  "run_id": "RUN-YYYYMMDD-0001",
  "experiment_id": "EXP-000",
  "git": {
    "commit": "<sha>",
    "branch": "<branch>",
    "repo": "<repo>"
  },
  "inputs": [
    {
      "id": "<dataset_id or URL>",
      "sha256": "<hash>",
      "license": "<license>",
      "sensitivity": "<public|internal|restricted>"
    }
  ],
  "config": {
    "files": ["config/exp.yaml"],
    "params": {"key": "value"},
    "seeds": {"python": 0}
  },
  "outputs": [
    {
      "path": "outputs/<file>",
      "sha256": "<hash>",
      "stac_item": "data/stac/items/<item>.json",
      "dcat_dataset": "data/catalog/dcat/<dataset>.jsonld",
      "prov_bundle": "data/prov/<run_id>.jsonld"
    }
  ],
  "policy": {
    "pack_ref": "<tag_or_commit>",
    "conftest_report": "policy/conftest.json",
    "waivers": "policy/waivers.yml"
  },
  "telemetry": {
    "trace_id": "<optional>",
    "energy_kwh_est": "<optional>",
    "carbon_kgco2e_est": "<optional>"
  }
}
```

</details>

<details>
<summary>🧾 Appendix B — Evidence Manifest Skeleton (YAML)</summary>

```yaml
evidence_id: "EM-000"
experiment_id: "EXP-000"
created: "YYYY-MM-DD"
claims:
  - claim_id: "C-001"
    text: "<claim statement>"
    supported_by:
      - type: "dataset"
        dcat: "data/catalog/dcat/<dataset>.jsonld"
        stac_item: "data/stac/items/<item>.json"
        prov: "data/prov/<run_id>.jsonld"
      - type: "analysis_output"
        path: "outputs/<plot_or_table>"
        sha256: "<hash>"
confidence:
  method: "<human_review|model_score|bayesian>"
  value: "<0..1 or description>"
notes: "<anything relevant>"
```

</details>

<details>
<summary>🧬 Appendix C — PROV Bundle Starter (JSON-LD)</summary>

```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "@graph": [
    {
      "@id": "urn:kfm:entity:input-1",
      "@type": "prov:Entity",
      "prov:label": "Input dataset"
    },
    {
      "@id": "urn:kfm:activity:run-RUN-YYYYMMDD-0001",
      "@type": "prov:Activity",
      "prov:used": ["urn:kfm:entity:input-1"],
      "prov:generated": ["urn:kfm:entity:output-1"]
    },
    {
      "@id": "urn:kfm:agent:<name_or_bot>",
      "@type": "prov:Agent",
      "prov:label": "Executor"
    }
  ]
}
```

</details>

<details>
<summary>📏 Appendix D — Metric Definitions Cheatsheet</summary>

- **Precision / Recall / F1 (classification):** define macro vs micro, class weighting, and the exact split strategy.
- **RMS error (georeferencing):** specify control points, CRS, and tolerance.
- **Tile/UI performance:** define test device + browser + dataset + viewport + measurement method.
- **Citation coverage (AI/Focus Mode):** define “citation present” and “citation correct” separately.

</details>

---

## ✅ Definition of Done (DoD) 🔴

- [ ] Front-matter complete and accurate
- [ ] Hypothesis + success thresholds are explicit
- [ ] Inputs are fully enumerated (license + sensitivity included)
- [ ] STAC/DCAT/PROV produced/linked for any publishable outputs
- [ ] Validation steps listed and repeatable
- [ ] Policy Pack results recorded (waivers documented w/ expiry)
- [ ] Peer reproduction attempt recorded (or scheduled with owner)
- [ ] Decision logged + next steps created

🧠 If it isn’t reproducible, it isn’t done.
