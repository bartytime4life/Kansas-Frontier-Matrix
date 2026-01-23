# 🧩 MCP Traceability Dashboards — Scripts

![MCP](https://img.shields.io/badge/MCP-Methods%2C%20Controls%20%26%20Processes-1f6feb?style=for-the-badge)
![Traceability](https://img.shields.io/badge/Traceability-Provenance%20%2B%20Telemetry%20%2B%20Policy-0ea5e9?style=for-the-badge)
![Evidence-First](https://img.shields.io/badge/Evidence--First-No%20Mystery%20Layers-22c55e?style=for-the-badge)
![Fail Closed](https://img.shields.io/badge/Governance-Fail%20Closed-f97316?style=for-the-badge)
![Reproducible](https://img.shields.io/badge/Reproducibility-Run%20Manifest%20%2B%20Canonical%20Digest-9333ea?style=for-the-badge)

> 🧭 **Goal:** Turn KFM’s *evidence chain* (STAC/DCAT/PROV + run manifests + telemetry + policy outcomes) into **dashboards + reports** that are *auditable, reproducible, and boringly dependable*.  
> If a metric can’t point back to evidence… **we don’t graph it.** ✅

---

<details>
<summary>🗂️ Table of Contents</summary>

- [✨ What lives here](#-what-lives-here)
- [🧠 Mental model](#-mental-model)
- [🔗 Inputs and evidence chain](#-inputs-and-evidence-chain)
- [📦 Outputs](#-outputs)
- [🗺️ Folder layout](#️-folder-layout)
- [🚀 Quickstart](#-quickstart)
- [📊 Script catalog](#-script-catalog)
- [🧾 Script standards](#-script-standards)
- [⏱️ Schedules and runbooks](#️-schedules-and-runbooks)
- [🧷 Adding a new dashboard script](#-adding-a-new-dashboard-script)
- [🛡️ Security privacy and redaction](#️-security-privacy-and-redaction)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 Design inputs and reference library](#-design-inputs-and-reference-library)

</details>

---

## ✨ What lives here

This folder contains **dashboards scripts** for the **MCP Traceability** stack.

These scripts generate:
- 📈 **Operational dashboards** (ingestion health, graph health, policy gate status, CI signal)
- ⛓ **Chain-of-custody dashboards** (what changed, who/what changed it, which outputs are affected)
- 🤖 **AI governance dashboards** (citation coverage, drift/bias signals, OPA runtime denies)
- 🌱 **Sustainability dashboards** (resource usage, energy/carbon telemetry if captured)
- 🧵 **Pulse / health-check reports** (short, human-readable summaries + machine-readable metrics)

**Big idea:** The KFM UI can show *a map behind the map* (layer provenance panels, export attributions, etc.).  
These scripts produce the **same truth** but formatted for maintainers, reviewers, and auditors.

---

## 🧠 Mental model

KFM has a strict “evidence-first” pipeline ordering:

> **ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode (AI)**

This folder lives in **MCP** land (Methods, Controls & Processes), so we treat dashboards as:
- 📐 a *control surface* (SLOs, gates, and audits),
- 🧾 a *documentation artifact* (reports that can be reviewed),
- 🔁 a *feedback loop* (what to fix next, with receipts).

---

## 🔗 Inputs and evidence chain

Dashboards must derive from **auditable sources**, typically:

### 🗃️ Metadata backbone
- **DCAT** (dataset-level catalog / discoverability)
- **STAC** (spatiotemporal collections and items)
- **PROV** (lineage: inputs → activities → outputs)

### 🧾 Run-level audit trail
- **Run manifests** (per pipeline run)  
  - includes timestamps, tool versions, inputs/outputs, summary counts
  - includes a **canonical digest** so the manifest “fingerprints itself”

### 📉 Telemetry & logs
- Append-only NDJSON telemetry (pipeline events, governance telemetry, health checks)
- OpenTelemetry (if integrated): traces/spans, latency, error rates, etc.

### ⚖️ Policy outcomes
- **OPA / Conftest** results (CI policy gates)
- Runtime policy denies (e.g., block AI output if citations missing)

### 🧠 Optional stores (read-only)
- Graph DB queries (Neo4j health and integrity)
- PostGIS / time-series stores (for “live layers” metrics)

> [!IMPORTANT]
> Dashboards are **not** an alternate source of truth.  
> They are a **projection** of the evidence chain.

---

## 📦 Outputs

All scripts should produce **both**:
- 🧑‍🔧 **Human outputs** (fast to scan)
- 🤖 **Machine outputs** (dashboards / alerts / automation)

### ✅ Recommended output bundle per run
- `summary.md` — short narrative summary (what changed, what failed, what’s next)
- `metrics.json` — structured metrics for dashboards
- `index.csv` — append-friendly rollup row (for simple trending)
- `run_manifest.json` — reproducibility + custody
- `prov.jsonld` *(optional but encouraged)* — PROV for the dashboard build itself

> [!TIP]
> If a script only emits one format, pick **JSON** and have a follow-up step render Markdown/HTML.

---

## 🗺️ Folder layout

Typical layout (adjust to repo reality):

```text
📦 mcp/
 └── 🧭 traceability/
     └── 📊 dashboards/
         ├── 🧰 scripts/               # 👈 you are here
         │   ├── README.md
         │   ├── python/               # optional: Python CLIs
         │   ├── node/                 # optional: TS/Node CLIs
         │   └── lib/                  # shared helpers (manifest, prov, io)
         ├── 📈 dashboards/            # dashboard definitions (Grafana JSON, etc.)
         ├── 🧾 reports/               # generated summaries (optional)
         └── 📦 out/                   # generated machine artifacts (optional)
```

---

## 🚀 Quickstart

### 1) Pick your runtime 🧪

Most KFM pipeline tooling is **Python-first**, but dashboards can be Python or Node.

- 🐍 Python recommended for: parsing catalogs/PROV, QA scans, CSV/JSON reporting
- 🟦 Node/TS recommended for: dashboard JSON manipulation, static site builds, UI-ish bundling

### 2) Python setup (example)

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

### 3) Run a single script (pattern)

```bash
python python/graph_health_check.py \
  --out ../../reports/graph_health/$(date +%Y-%m-%dT%H%M%SZ)
```

### 4) Run “everything” (pattern)

```bash
./run_all.sh --out ../out/$(date +%Y-%m-%d)
```

> [!NOTE]
> This README defines the **contract**. If your repo uses different entrypoints (Makefile, task runner, Poetry, npm), keep the contract but adapt the commands.

---

## 📊 Script catalog

Below is the **recommended** canonical set of scripts for traceability dashboards.

> 🧭 Naming: `verb_noun_scope` (snake_case), with stable “dashboard IDs” baked into metrics.

### 🧬 1) Catalog + provenance QA

#### `stac_dcat_prov_linkcheck`
**Purpose:** Validate that every dataset has the required cross-links:
- DCAT → STAC distribution
- STAC → asset URLs / tiles
- PROV → inputs + activities + outputs
- Optional: “no mystery layers” checks (UI layers must link to catalogs)

**Emits:** `metrics.json`, `summary.md`  
**Dashboards:** ✅ Metadata Completeness, 🔗 Link Integrity

---

### 🗃️ 2) Ingestion telemetry rollups

#### `telemetry_rollup`
**Purpose:** Aggregate append-only NDJSON telemetry into:
- ingest success/failure rates
- bytes processed
- top error classes
- policy deny counts
- “time to publish” lag

**Emits:** `metrics.json`, `index.csv`  
**Dashboards:** 📥 Intake Health, 🚦 Gate Status

---

### 🧠 3) Focus Mode governance metrics (AI)

#### `focus_citation_coverage`
**Purpose:** Compute metrics such as:
- % of answers with ≥1 citation
- % blocked/denied by policy (missing citations, sensitive content)
- drift indicators (citation coverage drops, accuracy regressions if you have eval sets)
- bias flags (if detectors exist)

**Emits:** `metrics.json`, `summary.md`  
**Dashboards:** 🤖 AI Trust, 🧾 Audit Readiness

---

### 🧷 4) Policy gate reporting (CI + runtime)

#### `policy_gate_report`
**Purpose:** Normalize Conftest/OPA outputs into dashboards:
- which policy IDs fired
- what file paths triggered them
- waivers usage (if supported)
- trend lines per policy ID

**Emits:** `metrics.json`, `summary.md`  
**Dashboards:** ⚖️ Governance, 🔒 Security Posture

---

### 🕸️ 5) Graph integrity (weekly health check)

#### `graph_health_check`
**Purpose:** Run weekly Neo4j integrity checks:
- node/edge counts + deltas
- orphaned nodes
- invalid relationship types
- schema drift signals
- backup verification results (if hooked in)

**Emits:** timestamped folder:
- `summary.md`
- `index.csv`
- optional: `details.json` (top offenders / sample IDs)

**Dashboards:** 🕸️ Graph Health, 🧯 Data Quality

> [!TIP]
> Keep the checks **fast** and the output **actionable**:
> - one “headline” section
> - one “top 5 things to fix”
> - one “what changed since last run”

---

### 📦 6) Artifact registry audit (OCI + signatures)

#### `oci_artifacts_audit`
**Purpose:** Validate “artifact distribution” claims:
- referenced OCI artifacts exist (tilesets, COGs, model files)
- digests match
- Cosign signatures present/valid (if required)
- referrers / attestations present (SLSA/SBOM if enabled)

**Emits:** `metrics.json`, `summary.md`  
**Dashboards:** 📦 Supply Chain, ✅ Reproducibility

---

### 🧵 7) Pulse threads (optional but powerful)

#### `pulse_thread_metrics`
**Purpose:** Roll up “Pulse” health checks into:
- fast “heartbeat” charts
- MTTR / incident counts
- open issues spawned by checks

**Emits:** `metrics.json`, `index.csv`, `summary.md`  
**Dashboards:** 🧵 Pulse, 🚑 Reliability

---

## 🧾 Script standards

Every script in this folder should follow these **non-negotiables**:

### ✅ Inputs
- **Read-only** evidence inputs (catalogs, logs, manifests)
- Explicit `--since` / `--until` (or `--window`) where relevant
- Optional `--strict` mode for CI (fail on warnings)

### ✅ Outputs
- Deterministic output paths (`--out`)
- Machine output (`metrics.json`) + human output (`summary.md`)
- A `run_manifest.json` that captures:
  - run ID
  - tool versions
  - inputs/outputs
  - counts/errors
  - canonical digest

### ✅ Determinism
- No nondeterministic timestamps inside the *content* unless they are captured as fields and included in digest intentionally
- Stable ordering (sorted keys / sorted rows)
- Prefer canonical JSON for hashing

### ✅ Exit codes
- `0` = OK
- `1` = failed checks / policy violations
- `2` = partial success / degraded mode (optional; document it per script)

---

## ⏱️ Schedules and runbooks

Recommended cadence:

| Cadence | What | Why |
|---:|---|---|
| Every 10 minutes ⏱ | Telemetry health check / rollup | detect ingestion outages fast |
| Nightly 🌙 | Metadata QA + linkcheck | prevent rot (broken links, missing fields) |
| Weekly 📅 | Graph health check | catch drift, orphans, schema surprises |
| Per PR ✅ | Policy gate report | fail closed before merge |
| Per release 🚀 | OCI/cosign audit | supply chain + reproducibility proof |

> [!WARNING]
> If a check can’t be performed (missing access, broken dependency), default is **fail closed** for CI gating scripts.

---

## 🧷 Adding a new dashboard script

Use this checklist to keep everything consistent:

- [ ] Create the script under `python/` or `node/`
- [ ] Define a stable **dashboard metric ID** namespace (e.g., `kfm.trace.graph.orphans`)
- [ ] Emit `metrics.json` + `summary.md`
- [ ] Emit / update `run_manifest.json`
- [ ] Add a “how to run” snippet in this README
- [ ] Add to CI schedule if it is a gate or heartbeat
- [ ] Add (or update) a policy rule if this metric is a governance requirement
- [ ] Ensure sensitive data is redacted (no leaking classified IDs/coords into public dashboards)

> [!TIP]
> If you’re unsure whether a new metric belongs here:  
> **If it helps explain “why we trust this output,” it belongs here.** ⛓️

---

## 🛡️ Security privacy and redaction

Dashboards are powerful… and dangerous if they leak sensitive info. Follow these rules:

### 🚫 Don’t leak
- secrets, tokens, internal URLs
- sensitive coordinates or protected site locations
- raw user queries (unless aggregated + policy-approved)

### 🧼 Redact by default
- show counts and rates
- show hashed IDs or sampled IDs only in restricted outputs
- keep “public dashboards” and “internal dashboards” separated

### 🧾 Prefer auditability
- keep raw evidence in controlled stores
- keep dashboards as projections (derived data)

---

## 🧯 Troubleshooting

### “Policy gates failing but I don’t know why” 😵‍💫
- Run `policy_gate_report` locally with `--explain`
- Ensure you have the same policy pack version as CI
- Look for missing required files (PROV/STAC/DCAT)

### “Graph check is slow” 🐌
- Add query timeouts
- Prefer count-based checks + sampled deep checks
- Cache last-run baseline metrics to compute deltas cheaply

### “Telemetry NDJSON is huge” 📚
- Add windowing (`--since` / `--until`)
- Maintain daily partitions
- Roll up to `index.csv` for dashboards and keep raw for audits

---

## 📚 Design inputs and reference library

This README is derived from (and should remain aligned with) the KFM design docs and reference packs:

### 📄 Core KFM docs (project truth)
- 📘 **Comprehensive Technical Documentation**
- 🧱 **Comprehensive Architecture, Features, and Design**
- 🧭 **AI System Overview (Focus Mode + governance)**
- 🖥️ **Comprehensive UI System Overview**
- 📥 **Data Intake – Technical & Design Guide**
- 🌟 **Latest Ideas & Future Proposals**
- 💡 **Additional Project Ideas**
- 🧠 **Innovative Concepts to Evolve KFM**

### 🧰 Reference portfolios (supporting literature)
- 🤖 **AI Concepts & more** *(PDF portfolio — AI/ML reference library)*
- 🗺️ **Maps / Google Maps / Virtual Worlds / WebGL** *(PDF portfolio — geospatial + visualization refs)*
- 🧱 **Data Management / Architectures / Bayesian Methods** *(PDF portfolio — data engineering refs)*
- 🧑‍💻 **Various programming languages & resources** *(PDF portfolio — programming reference library)*

> [!NOTE]
> These portfolios are not “required reading,” but they inform standards and implementation choices (CI/CD, observability, geoprocessing, visualization, governance, etc.).

---

### ✅ Definition of done (for this folder)

When `mcp/traceability/dashboards/scripts` is “done enough”, we should be able to answer:
- “Is the system healthy?” ✅
- “What changed?” ✅
- “Can we reproduce it?” ✅
- “Is it compliant?” ✅
- “If something is wrong, what exactly do we fix next?” ✅

🧭 Onward.
