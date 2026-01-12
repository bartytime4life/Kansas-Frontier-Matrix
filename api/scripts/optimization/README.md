# ⚙️ Optimization Scripts (`api/scripts/optimization`) 🧠📈

![Status](https://img.shields.io/badge/status-active--dev-blue)
![Provenance-first](https://img.shields.io/badge/provenance-first-brightgreen)
![Deterministic](https://img.shields.io/badge/runs-deterministic-success)
![Policy-Gated](https://img.shields.io/badge/governance-policy--gated-orange)
![Backend](https://img.shields.io/badge/backend-FastAPI%20%7C%20PostGIS%20%7C%20Neo4j-4c1)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV--O-informational)

> **📌 Purpose:** This folder is the **offline + CI-friendly optimization toolbox** for Kansas Frontier Matrix (KFM).
> We use it to **tune model parameters, pipeline knobs, and performance tradeoffs** without sacrificing KFM’s core principles:
> **determinism, traceability (PROV), validation gates, and human-centered governance**.

[⬅️ Back to repo README](../../../README.md) · [🧭 Docs](../../../docs) · [🧪 Validation tooling](../../../tools/validation)

---

## 🧭 Contents

- [What “optimization” means in KFM](#what-optimization-means-in-kfm)
- [Optimization lifecycle](#optimization-lifecycle)
- [Folder layout & conventions](#folder-layout--conventions)
- [Run configuration contract](#run-configuration-contract)
- [Outputs & artifacts](#outputs--artifacts)
- [Optimization recipes](#optimization-recipes)
- [Quality gates](#quality-gates)
- [Reproducibility & experimental design](#reproducibility--experimental-design)
- [Observability & energy](#observability--energy)
- [Security, ethics, and legal safety rails](#security-ethics-and-legal-safety-rails)
- [Adding a new optimization script](#adding-a-new-optimization-script)
- [Reference shelf](#reference-shelf)

---

## What “optimization” means in KFM

In KFM, “optimization” is **not** just “find the best number.” It’s:

✅ **Calibration** (match model outputs to observed data)  
✅ **Sensitivity analysis** (what matters / what doesn’t)  
✅ **Search under constraints** (performance, memory, governance, fairness)  
✅ **Multi-objective tradeoffs** (accuracy vs latency vs interpretability)  
✅ **Offline performance tuning** (indexes, cache plans, tile strategies)  
✅ **Artifact production** (publish *evidence*, not vibes)

> **Rule of thumb 🧠:** If a script produces something that might influence a map, story, or decision, it must produce **evidence artifacts** (STAC/DCAT/PROV + metrics + config) so it can be inspected, re-run, and audited.

---

## 🧬 Optimization lifecycle

```mermaid
flowchart LR
  A[Inputs\n(datasets + bounds + constraints)] --> B[Plan\n(objective + metrics + budget)]
  B --> C[Search\n(grid / random / bayes / gradient / evo)]
  C --> D[Evaluate\n(simulation / query / pipeline / UI perf)]
  D --> E[Artifacts\nmetrics + plots + prov + stac]
  E --> F{Policy + QA Gate}
  F -- pass ✅ --> G[Publish\nPR / catalog entry / worker job]
  F -- fail ❌ --> H[Quarantine\nreport + no publish]
```

---

## 📁 Folder layout & conventions

> This directory is intentionally “scripts-first”: small, composable executables that can be run locally, in a worker, or in CI.

Recommended structure (adjust to what already exists in the repo):

```text
api/scripts/optimization/
├─ README.md                      👈 you are here
├─ _shared/                        ♻️ common helpers
│  ├─ config.py                    (load/validate config)
│  ├─ provenance.py                (PROV emission helpers)
│  ├─ artifacts.py                 (standard output layout)
│  ├─ metrics.py                   (common metrics + schemas)
│  └─ io.py                        (dataset fetch, caching, hashing)
├─ model_calibration/              🧪 tune scientific models
├─ pipeline_tuning/                🏗️ optimize ETL knobs
├─ db_query_tuning/                🗄️ PostGIS/Neo4j tuning runs
├─ map_delivery_tuning/            🗺️ tiling + compression + LOD
└─ reports/                        📈 plots + summaries
```

### ✅ Script invariants (non-negotiable)

Every optimization script should be:

- **Deterministic**: fixed RNG seeds + explicit config + stable outputs.
- **Idempotent**: same inputs/config → same run_id and same artifacts (or clearly versioned outputs).
- **Contract-first**: config schemas and outputs are versioned, validated, and reviewed.
- **Provenance-emitting**: every run writes a PROV lineage record.
- **Validation-gated**: artifacts don’t get published unless QA/policy checks pass.
- **Atomic-publish**: stage → validate → publish (no partial output promotion).

> **Tip 🧩:** Treat scripts like pipelines. The same discipline that applies to ingestion applies here too.

---

## 🧾 Run configuration contract

All scripts should support **config-driven runs** (YAML or JSON), plus a small set of CLI overrides.

### Minimal config schema (recommended)

```yaml
run:
  name: "example_optimization"
  seed: 1337
  idempotency_key: "example_2026-01-12"
  notes: "Short explanation of intent"
objective:
  direction: "min"         # min|max
  primary_metric: "rmse"   # required
  secondary_metrics:       # optional
    - "mae"
    - "latency_ms"
search:
  algorithm: "random"      # grid|random|bayes|gradient|evo
  budget: 50               # total trials / evals
  early_stop:
    enabled: true
    patience: 10
  bounds:
    param_a: [0.0, 1.0]
    param_b: [10, 200]
data:
  inputs:
    - dataset_id: "kfm.ks.example.1900_2000.v1"
      version: "2026-01-01"
  split:
    method: "time"         # time|space|kfold
    holdout: 0.2
publish:
  mode: "none"             # none|staging|pr
observability:
  otel: true
  energy_report: true
```

### CLI expectations

Each script should implement:

- `--config <path>`
- `--seed <int>` (overrides config)
- `--budget <int>` (overrides config)
- `--output-dir <path>`
- `--dry-run` (no publish / no DB writes)
- `--print-resolved-config` (debugging determinism)

Example pattern:

```bash
python -m api.scripts.optimization.model_calibration.calibrate \
  --config configs/optimization/air_quality.yaml \
  --seed 1337 \
  --budget 80 \
  --output-dir data/work/optimization_runs
```

> **Note 🧾:** If these modules don’t exist yet, keep the interface anyway—this README defines the **contract**, not a specific implementation.

---

## 📦 Outputs & artifacts

Every run should create a **single, self-contained run folder** with:

- **Resolved config** (exact parameters actually used)
- **Trial table** (all attempts, not just “the best”)
- **Metrics** (JSON schema-stable)
- **Plots** (optional but encouraged)
- **PROV lineage**
- **STAC/DCAT records** when artifacts are publishable
- **A small human summary** (markdown)

Recommended layout:

```text
data/work/optimization_runs/<run_id>/
├─ config.resolved.yaml
├─ metrics.json
├─ trials.csv
├─ best.json
├─ summary.md
├─ prov.jsonld
├─ stac_item.json                 (if producing a dataset artifact)
├─ dcat_dataset.json              (if publishing to catalog)
├─ plots/
│  ├─ convergence.png
│  ├─ pareto.png
│  └─ residuals.png
└─ logs/
   ├─ run.log
   └─ otel_trace.json             (optional export)
```

> **Golden rule 🥇:** If someone can’t reproduce your “best params” from your artifacts, it doesn’t count.

---

## 🧪 Optimization recipes

### 1) Scientific model calibration (simulation-first) 🛰️🌾🌊

Use when you have:
- A forward model (deterministic runner)
- Observations (sensors, surveys, remote sensing products)
- A calibration objective (RMSE, NSE, likelihood)

Recommended methods:
- **Grid / factorial** for low-dimensional problems
- **Random search** for broad exploration (seeded!)
- **Bayesian optimization** for expensive evaluations
- **Gradient-based** only when objective is differentiable and stable

Artifacts to include:
- Calibration curves, residual plots, uncertainty ranges
- Sensitivity report (which params matter most)
- Clear “domain validity” bounds (don’t optimize nonsense)

---

### 2) Remote sensing pipeline tuning (cloud-to-catalog) ☁️🛰️🗺️

Use when you’re tuning:
- Cloud masks, compositing windows, classification thresholds
- Spatial/temporal resolution tradeoffs
- Post-processing filters (smoothing, gap fill)

Recommended methods:
- DOE-style exploration (factor ranges + replicates)
- Holdout by **space** (counties/tiles) or **time** (years/seasons)
- Metrics beyond accuracy: coverage %, artifacts, latency

Artifacts to include:
- Confusion matrices or agreement with reference labels (if available)
- Spatial error maps (where it fails matters)
- Runtime + cost estimates (compute-to-data philosophy)

---

### 3) Database / query optimization (offline logs → online speed) 🗄️⚡

Typical tasks:
- Index suggestions (PostGIS/JSONB/graph)
- Query shape constraints (pagination, expensive joins)
- Cache placement for repeated query sequences

Recommended approach:
- Collect query logs → cluster sequences → replay “probe queries”
- Compare plans with `EXPLAIN (ANALYZE, BUFFERS)` in controlled runs
- Publish only after a performance regression test passes

Artifacts to include:
- Before/after latency distributions
- Query plans (sanitized), index DDL proposals
- Impact analysis (write overhead / storage cost)

> **Tip:** Prefer improvements that are **auditable and reversible** (migration scripts, feature flags, config knobs).

---

### 4) Map delivery tuning (tiles, LOD, compression) 🗺️🧊🎛️

Targets:
- Tile generation strategy (pre-tile vs on-demand + cache)
- Vector simplification rules per zoom level
- Raster encoding choices (PNG/JPEG/WebP), COG tiling parameters

Metrics:
- P95 tile latency
- Client FPS / GPU load proxies (when measurable)
- Bandwidth per view and cache hit rate

Artifacts:
- Performance dashboards
- Representative screenshots for “visual correctness” regression
- A/B comparisons with “acceptance thresholds”

---

## 🚦 Quality gates

Before anything leaves `data/work/`:

### ✅ Required checks
- Config schema validation (and version compatibility)
- Dataset bounds checks (Kansas extent, CRS expectations, etc.)
- Provenance emission present (`prov.jsonld`)
- If producing a dataset artifact: STAC/DCAT records exist

### 🧪 Strongly recommended checks
- Catalog QA gate (`tools/validation/catalog_qa`)
- Policy pack evaluation (OPA/Conftest or equivalent)
- Regression test on a small “golden” dataset

> **Warning ⚠️:** If an optimization run changes user-facing outputs (maps, stories, recommendations),
> it must go through **human review** before publish.

---

## 🧠 Reproducibility & experimental design

Optimization can accidentally turn into **p-hacking** if we’re not disciplined. Keep it science-grade:

### Do this ✅
- Predefine objective + metrics + stopping rules (write it in config)
- Log **all trials** (not just the best)
- Use appropriate splits (time/space leakage is real)
- Report uncertainty (confidence/credible intervals where possible)
- Prefer simpler models when performance is comparable (interpretability wins)

### Don’t do this ❌
- “Tune until it looks good” without recording the search
- Change the metric after seeing results without documenting why
- Optimize on the same data you claim as validation

> **Best practice 🧪:** Treat each optimization run like an experiment:
> hypothesis → plan → run → artifacts → review → publish.

---

## 📡 Observability & energy

If optimization is compute-heavy, it must be observable:

- Emit OpenTelemetry spans (trial-level spans are 🔥 for debugging)
- Record runtime, memory, and IO stats
- Track energy usage when feasible (especially for large sweeps)

> **Why?** KFM explicitly values responsible compute + transparent operations—not just “fast.”

---

## 🔒 Security, ethics, and legal safety rails

Optimization scripts often touch:
- Sensitive datasets (restricted layers, private contributors)
- API keys (Earth Engine / cloud resources)
- Derived artifacts that could be misinterpreted

Minimum safety posture:
- Never hardcode secrets; use env + secret managers
- Redact logs by default (no tokens, no PII)
- If an artifact is AI-generated or model-derived, label it clearly and attach provenance
- Ensure outputs remain **advisory** unless explicitly governed otherwise

> **Reminder 🧑‍⚖️:** Responsible, explainable, evidence-backed behavior is a design requirement—not a nice-to-have.

---

## ➕ Adding a new optimization script

### Checklist ✅
- [ ] Add script under the right subfolder (model_calibration / db_query_tuning / …)
- [ ] Implement CLI: `--config --seed --budget --output-dir --dry-run`
- [ ] Validate config schema (versioned)
- [ ] Emit artifacts with standard layout
- [ ] Emit PROV lineage
- [ ] Add a smoke test + a tiny fixture dataset
- [ ] Update this README (or subfolder README) with usage

### Naming conventions 🏷️
- Script names: `opt_<domain>_<target>.py` (predictable + searchable)
- Dataset IDs: `kfm.<region>.<theme>.<time_range>.v<version>` (when applicable)
- Run IDs: deterministic hash from `(idempotency_key + resolved_config + inputs)`

---

## 📚 Reference shelf

<details>
<summary><strong>🧱 Project “source of truth” docs</strong> (click to expand)</summary>

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** — system architecture, governance, pipelines, and contracts.
- **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals** — forward-looking designs (simulation runner, bias correction, policy, telemetry).
- **Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities** — what’s missing + where optimization work creates leverage.
- **Kansas-Frontier-Matrix Open-Source Geospatial Historical Mapping Hub Design** — mapping hub framing & architecture.
- **MARKDOWN_GUIDE_v13 (Kansas Matrix System)** — contract-first, deterministic pipeline, evidence artifact requirements.

</details>

<details>
<summary><strong>🧪 Modeling, simulation, stats, and optimization</strong></summary>

- *Scientific Modeling and Simulation (NASA-grade guide)* — V&V, UQ, sensitivity, scientific rigor.
- *Understanding Statistics & Experimental Design* — DOE discipline, avoiding bias.
- *Regression Analysis with Python* + *Linear Regression slides* — objective functions, optimization tooling, cross-validation patterns.
- *Think Bayes* — Bayesian estimation ideas for calibration and uncertainty.
- *Generalized Topology Optimization for Structural Design* — constraint-driven optimization thinking (great analogy for governed outputs).
- *Spectral Geometry of Graphs* — graph analysis foundations (relevant to knowledge graph optimization).
- *Graphical Data Analysis with R* — diagnostic plots and exploratory validation.

</details>

<details>
<summary><strong>🗄️ Data platforms & performance</strong></summary>

- *Scalable Data Management for Future Hardware* — offline optimization using query logs, compiled pipelines, workload-aware tuning.
- *PostgreSQL Notes for Professionals* — indexing and query tuning reference (esp. JSONB patterns).
- *Data Spaces* — governance and interoperability lenses for federated data systems.
- *Concurrent Real-Time and Distributed Programming in Java* — concurrency patterns (useful when designing workers and schedulers).

</details>

<details>
<summary><strong>🗺️ GIS, remote sensing, cartography, and delivery</strong></summary>

- *Cloud-Based Remote Sensing with Google Earth Engine* — cloud processing patterns & remote sensing workflows.
- *Python Geospatial Analysis Cookbook* — practical PostGIS/GDAL pipeline guidance.
- *Making Maps (GIS map design)* — cartographic clarity (optimization must preserve meaning).
- *Mobile Mapping: Space, Cartography and the Digital* — UX context (performance is user experience).
- *WebGL Programming Guide* — GPU/render constraints (tile + vector payload tuning).
- *Responsive Web Design (HTML5/CSS3)* — responsive UI performance implications.
- *Compressed Image File Formats (JPEG/PNG/GIF/BMP)* — compression tradeoffs for tiles and thumbnails.

</details>

<details>
<summary><strong>🔐 Ethics, human-centered design, and security</strong></summary>

- *Introduction to Digital Humanism* — human-centered constraints and accountability.
- *AI Law’s prophecies / conceptual foundations of ML age* — governance framing for ML-derived artifacts.
- *Ethical Hacking and Countermeasures* — defensive mindset for handling keys, infra, and auditability.
- *Gray Hat Python* — security awareness reference (use responsibly; no offensive use in KFM).
- *Principles of Biological Autonomy* — systems thinking reference (useful for agent-like orchestration patterns).

</details>

<details>
<summary><strong>📦 Programming mega-compilations (language reference library)</strong></summary>

- **A programming Books.pdf**
- **B-C programming Books.pdf**
- **D-E programming Books.pdf**
- **F-H programming Books.pdf**
- **I-L programming Books.pdf**
- **M-N programming Books.pdf**
- **O-R programming Books.pdf**
- **S-T programming Books.pdf**
- **U-X programming Books.pdf**

</details>

---

### 🧩 If you only remember 3 things…

1) **Config + artifacts are the product.**  
2) **Determinism + provenance are mandatory.**  
3) **Nothing publishes without QA + policy gates.** 🚦✅

🌾🗺️🚀

