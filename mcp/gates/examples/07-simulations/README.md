# 07 — Simulations Gate 🧪🗺️
![MCP](https://img.shields.io/badge/MCP-Gates-blue)
![Example](https://img.shields.io/badge/Example-07--Simulations-brightgreen)
![Policy](https://img.shields.io/badge/Policy-OPA%2FRego%20%2B%20Conftest-orange)
![Provenance](https://img.shields.io/badge/Provenance-STAC%20%7C%20DCAT%20%7C%20PROV-purple)
![Reproducible](https://img.shields.io/badge/Reproducible-Deterministic%20%2B%20Idempotent-success)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-informational)

> 📍 **Example path:** `mcp/gates/examples/07-simulations/`  
> ✅ **Purpose:** Turn “what-if” modeling runs into **auditable, reproducible, promotable** KFM artifacts (with governance baked in).

---

## 🧭 What this gate protects (in one sentence)
**Simulations must not become “shadow production.”** This gate enforces the rule: **sandbox first → review → promote → catalog → then UI/API.**

---

## 📚 Table of contents
- [Core concepts](#-core-concepts)
- [What the Simulations Gate checks](#-what-the-simulations-gate-checks)
- [Example folder layout](#-example-folder-layout)
- [Examples included](#-examples-included)
- [Run the gate locally](#-run-the-gate-locally)
- [Promotion workflow](#-promotion-workflow)
- [UI wiring expectations](#-ui-wiring-expectations)
- [Extending the gate](#-extending-the-gate)
- [Troubleshooting](#-troubleshooting)
- [References](#-references)

---

## 🧠 Core concepts

### 1) 🧪 “Simulation” = first-class dataset
In KFM, simulation outputs (climate runs, forecasts, agent-based models, statistical models, etc.) are treated like **datasets**: they require **stable IDs**, **lineage**, **metadata**, and **policy compliance**.

### 2) 🧰 `kfm-sim-run` pattern (deterministic + idempotent)
KFM proposes a deterministic simulation runner pattern (`kfm-sim-run`) that:
- takes a structured scenario/change request,
- runs it in a **sandbox pipeline**,
- emits **diff patches**, updated **STAC items**, and **PROV lineage**,
- and can even open a **draft PR** for promotion.

Key behaviors:
- **Fixed seeds** where possible (bitwise reproducibility when feasible; otherwise statistical reproducibility).
- **Pinned environment** (container image digest / lockfiles).
- **Virtual clock** (frozen time; do not depend on “now”). ⏱️

### 3) 🧪 Sandbox vs promotion (non-negotiable)
- Simulation runs start in `data/work/sims/` (workbench).  
- Nothing becomes “real KFM” until promoted to `data/processed/` **and cataloged**.
- **Do not** wire UI/analytics directly to `data/work/sims` outputs. 🚫

### 4) 🧾 Provenance + catalog as default
Every run should be able to answer:
- What inputs (exact versions/hashes) were used?
- What code + parameters?
- What environment?
- What outputs were produced?
- How do we reproduce it?

Expect metadata artifacts:
- **STAC** (items for geospatial outputs)
- **DCAT** (dataset-level catalog view)
- **PROV** (lineage & transformations)

### 5) 🧭 Governance & ethics baked in
Simulation outputs can leak sensitive locations or sensitive inferences. KFM’s stance includes:
- **location generalization / obfuscation** for sensitive points,
- **sensitivity tagging** (and “no downgrade” rules),
- **CARE + cultural protocols** (e.g., Traditional Knowledge labels / community access constraints),
- **review + auditability**.

### 6) 📉 Uncertainty is part of the deliverable
If the model is uncertain, the artifacts should say so:
- sensitivity analysis,
- ensembles,
- distribution summaries,
- calibration/validation notes,
- known limitations.

---

## ✅ What the Simulations Gate checks

> Think of this as a “PR-ready simulation artifact contract.” If you can’t review it, you can’t ship it.

### Required artifacts (minimum)
| Artifact | Why it exists | Typical filename(s) |
|---|---|---|
| Scenario definition | What was requested + intent | `scenario.yaml` |
| Run manifest | Inputs, params, environment, reproducibility | `run_manifest.json` |
| Output catalog | What came out (IDs, formats) | `outputs.json` *(or in manifest)* |
| Provenance | Traceability | `metadata/prov.json` *(or `.ttl`)* |
| STAC item(s) | Spatial discovery / UI layer wiring | `metadata/stac/*.json` |
| DCAT dataset | Dataset-level metadata | `metadata/dcat.json` |
| Review-friendly diff | What changed vs baseline | `diff.patch` / `diff.md` |
| Model card | Assumptions + limits + intended use | `model_card.md` |

### Reproducibility & integrity rules
- ✅ **Inputs pinned:** dataset IDs + content hashes (or immutable references).
- ✅ **Parameters captured:** no “magic defaults.”
- ✅ **Environment pinned:** container digest or lockfile(s).
- ✅ **Seeded randomness:** seed recorded; if nondeterministic, declare expected distribution + tolerances.
- ✅ **Virtual clock:** timestamp is *a parameter*, not a side effect.
- ✅ **Idempotency key:** rerunning the same manifest yields the same run identity (or same digest).

### Manifest digest rule (canonicalized JSON → SHA-256)
To support idempotency and auditing, simulation runs can include a canonical digest:
- Canonicalize JSON (RFC 8785 style).
- Hash with SHA-256.
- Store as `canonical_digest`.
- Optionally derive `idempotency_key` from it.

### Governance rules (FAIR/CARE + safety)
- ✅ **License present** and consistent across metadata.
- ✅ **Sensitivity tags present** and cannot be downgraded during promotion.
- ✅ **Sensitive locations obfuscated** (e.g., rounding, hex bins, bounding areas).
- ✅ **Cultural protocol fields** supported where applicable (access restrictions / TK labels / community constraints).
- ✅ **No secrets** in logs or manifests (tokens, keys, credentials).

### Promotion safety rule (anti-shadow-production)
- ✅ Run outputs must *not* be referenced directly by UI/API until promoted.
- ✅ Promotion requires STAC/DCAT/PROV updated and stable IDs assigned.
- ✅ Promotion creates a reviewable PR with diffs and artifacts.

---

## 🗂 Example folder layout

```text
mcp/
└─ gates/
   └─ examples/
      └─ 07-simulations/
         ├─ README.md
         ├─ scenarios/
         │  ├─ 01_patch_single_run/
         │  │  ├─ scenario.yaml
         │  │  ├─ run_manifest.json
         │  │  ├─ model_card.md
         │  │  ├─ expected/
         │  │  │  ├─ diff.patch
         │  │  │  ├─ metadata/
         │  │  │  │  ├─ stac/
         │  │  │  │  ├─ dcat.json
         │  │  │  │  └─ prov.json
         │  │  │  └─ gate_report.json
         │  ├─ 02_ensemble_uq/
         │  │  ├─ scenario.yaml
         │  │  ├─ run_manifest.json
         │  │  ├─ uq_summary.json
         │  │  └─ expected/...
         │  └─ 03_sensitive_obfuscation/
         │     ├─ scenario.yaml
         │     ├─ run_manifest.json
         │     ├─ governance.json
         │     └─ expected/...
         ├─ policy/
         │  ├─ simulations_gate.rego
         │  └─ simulations_gate_test.rego
         └─ schemas/
            ├─ run_manifest.schema.json
            └─ scenario.schema.json
```

> 🧩 The exact filenames can vary by implementation — the *contract* is what matters.

---

## 🧪 Examples included

### Example 01 — Patch-based, single-run scenario 🔧
A minimal “what-if” run that:
- takes a baseline dataset,
- applies a structured patch (e.g., “+10% crop yield” or “rainfall multiplier = 1.10”),
- produces a reviewable `diff.patch`,
- emits STAC/DCAT/PROV for the derived output,
- passes the gate.

**Conceptual `scenario.yaml` (template):**
```yaml
scenario_id: sim-YYYYMMDD-example-01
title: "Rainfall +10% sensitivity test"
intent:
  question: "How do yield projections change if rainfall increases 10%?"
  domain: agriculture
inputs:
  - id: kfm:datasets/rainfall
    ref: "stac://.../items/rainfall@sha256:..."
  - id: kfm:datasets/crop_yield_model_inputs
    ref: "stac://.../items/inputs@sha256:..."
parameters:
  rainfall_multiplier: 1.10
  seed: 1337
environment:
  container_image: "ghcr.io/org/kfm-sim@sha256:REPLACE_ME"
  virtual_clock_utc: "2026-01-01T00:00:00Z"
outputs:
  - id: kfm:sims/yield_projection_rainfall_plus_10pct
    format: geoparquet
    stac_item: metadata/stac/yield_projection.json
governance:
  sensitivity: public
  license: "CC-BY-4.0"
```

---

### Example 02 — Ensemble + uncertainty quantification 📊
An ensemble run that demonstrates:
- multiple seeds / parameter sweeps,
- aggregated summaries (mean/quantiles),
- declared uncertainty bounds,
- UQ artifacts required for promotion.

**Expected extra artifacts:**
- `uq_summary.json` (quantiles, metrics, assumptions)
- `ensemble_manifest.json` (each member run ↔ seed/params ↔ output ref)
- `model_card.md` describing calibration/validation + limits

---

### Example 03 — Sensitive outputs + obfuscation 🛡️
Demonstrates governance handling where the *results* would be risky if published at full fidelity:
- site-level points become coarse geometry (hex cells / ~10km rounding / bounding areas),
- sensitivity tags are enforced,
- access constraints are explicitly represented.

**Expected extra artifacts:**
- `governance.json` (or embedded governance block in manifests)
- a “public-safe” derived layer plus optional restricted artifacts (if supported)

---

## 🧰 Run the gate locally

> Below is a typical flow using policy-as-code (OPA/Rego) + Conftest. Adjust paths to match your repo.

### 1) Validate schemas (optional but recommended)
```bash
# Example (use your JSON schema tooling of choice)
jsonschema -i scenarios/01_patch_single_run/run_manifest.json schemas/run_manifest.schema.json
jsonschema -i scenarios/01_patch_single_run/scenario.yaml schemas/scenario.schema.json
```

### 2) Run policy gate
```bash
# Conftest example
conftest test scenarios/01_patch_single_run \
  --policy policy \
  --all-namespaces
```

### 3) Expected outputs
- Pass → `gate_report.json` equivalent indicates ✅  
- Fail → actionable messages like:
  - missing `metadata/prov.json`
  - environment not pinned
  - sensitivity downgrade attempt
  - no diff artifact
  - missing license

---

## 🚀 Promotion workflow

### Promotion checklist ✅
Before you promote a sim run to `data/processed/`:

- [ ] Scenario definition included (`scenario.yaml`)
- [ ] Run manifest complete + digested (`run_manifest.json` with `canonical_digest`)
- [ ] Inputs pinned (dataset IDs + hashes/immutable refs)
- [ ] Outputs have stable IDs (not “temp” names)
- [ ] STAC/DCAT/PROV updated and consistent
- [ ] Sensitivity reviewed (no downgrades; obfuscation where needed)
- [ ] Model card written (assumptions, intended use, limits, validation notes)
- [ ] No UI/API references point to `data/work/sims/`
- [ ] Large artifacts tracked appropriately (DVC/LFS/OCI artifacts as applicable)
- [ ] PR includes review-friendly diffs + summary

### W🛰️–P🧠–E⚙️ (Watcher–Planner–Executor) fit
A common automation shape:
1. **Watcher** sees a new scenario request or upstream data change  
2. **Planner** creates a run plan and proposes artifacts  
3. **Executor** runs the sim, generates metadata, opens a draft PR  
4. **Gate** blocks or allows promotion

---

## 🖥️ UI wiring expectations

If a simulation result becomes a visible layer, the UI should be able to show:

- 🌓 **Scenario toggle:** baseline vs scenario
- 🪟 **Compare view:** side-by-side or swipe comparison
- 🎛️ **What-if sliders:** parameter controls (when applicable)
- 📌 **Model details panel:** assumptions + parameterization + provenance links
- 📉 **Uncertainty display:** error bars, confidence bands, ensemble spread

> 🔍 A “cool layer” without provenance is a liability. The UI should never be forced to guess what a layer means.

---

## 🧩 Extending the gate

### Add a new simulation example
1. Create a new folder under `scenarios/NN_name/`
2. Add:
   - `scenario.yaml`
   - `run_manifest.json`
   - `model_card.md`
   - `expected/` outputs (STAC/DCAT/PROV + diff)
3. Add/extend policy rules and tests under `policy/`

### Common extensions
- 🔒 **Signing & supply chain:** package sim artifacts as OCI artifacts + sign (e.g., cosign)
- 🧾 **Deeper PROV graphs:** granular activities per pipeline step
- 🧪 **Stronger V&V:** golden tests, back-to-back comparisons, calibration checks
- 🧠 **Surrogate models:** store both simulator and surrogate metadata + performance

---

## 🧯 Troubleshooting

**Gate fails: “environment not pinned”**  
→ Add container digest or lockfile references (`requirements.lock`, `poetry.lock`, etc.).

**Gate fails: “missing provenance”**  
→ Generate `metadata/prov.json` linking inputs → activity → outputs.

**Gate fails: “sensitivity downgrade”**  
→ Keep or raise sensitivity; add obfuscation; include governance justification.

**Gate fails: “no diff artifact”**  
→ Emit `diff.patch` or `diff.md` comparing to baseline (review is the point).

**Gate passes locally but fails CI**  
→ Check for nondeterminism: seeds, threading, BLAS behavior, GPU nondeterminism, time dependence.

---

## 📎 References

### Core KFM docs (project files)
- **📚 KFM Data Intake – Technical & Design Guide** <!-- :contentReference[oaicite:0]{index=0} -->
- **🧭 KFM – Comprehensive Architecture, Features, and Design** <!-- :contentReference[oaicite:1]{index=1} -->
- **🧰 KFM – Comprehensive Technical Documentation** <!-- :contentReference[oaicite:2]{index=2} -->
- **🧠 KFM – AI System Overview 🧭🤖** <!-- :contentReference[oaicite:3]{index=3} -->
- **🖥️ KFM – Comprehensive UI System Overview** <!-- :contentReference[oaicite:4]{index=4} -->
- **💡 Innovative Concepts to Evolve KFM** <!-- :contentReference[oaicite:5]{index=5} -->
- **🌟 Latest Ideas & Future Proposals** <!-- :contentReference[oaicite:6]{index=6} -->
- **🧱 Additional Project Ideas (manifests, policy, OCI, signing)** <!-- :contentReference[oaicite:7]{index=7} -->
- **🔎 Data Mining Concepts & Applications (privacy, inference, optimization)** <!-- :contentReference[oaicite:8]{index=8} -->

### MCP + documentation standards
- **🧪 Scientific Method + Master Coder Protocol Documentation** <!-- :contentReference[oaicite:9]{index=9} -->
- **🧾 Design Audit (gaps & enhancements)** <!-- :contentReference[oaicite:10]{index=10} -->
- **🧷 Comprehensive Markdown Guide** <!-- :contentReference[oaicite:11]{index=11} -->
- **🧷 MASTER / MARKDOWN guide v13** <!-- :contentReference[oaicite:12]{index=12} -->
- **🗺️ Open-Source Geospatial Historical Mapping Hub Design** <!-- :contentReference[oaicite:13]{index=13} -->

### Reference libraries (PDF portfolios)
<details>
<summary>📦 Maps / WebGL / Virtual Worlds pack (highly relevant for simulation visualization)</summary>

- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `google-maps-javascript-api-cookbook.pdf`
- `DesigningVirtualWorlds.pdf`
- `Archaeological 3D GIS...pdf`
- `geoprocessing-with-python.pdf`
- `python-geospatial-analysis-cookbook...pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`

<!-- :contentReference[oaicite:14]{index=14} -->
</details>

<details>
<summary>📦 Data Management / Bayesian / CI-CD pack (highly relevant for UQ + reproducibility)</summary>

- `Bayesian Methods for Hackers...pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `Comprehensive CI_CD Guide for Software and Data Projects.pdf`
- `The Data Engineering Cookbook.pdf`
- `Database Performance at Scale.pdf`

<!-- :contentReference[oaicite:15]{index=15} -->
</details>

<details>
<summary>📦 AI Concepts pack (agents, ML foundations, model documentation)</summary>

- `AI Foundations of Computational Agents 3rd Ed.pdf`
- `Pattern Recognition and Machine Learning.pdf`
- `Deep Learning with Python.pdf`
- `understanding-machine-learning-theory-algorithms.pdf`

<!-- :contentReference[oaicite:16]{index=16} -->
</details>

<details>
<summary>📦 Programming Languages & Engineering pack (solvers, simulation tooling, dev practices)</summary>

- `Matlab-Modeling, Programming & Simulations.pdf`
- `Solving Ordinary Differential Equations in Python.pdf`
- `Solving PDEs in Python.pdf`
- `Introduction-to-Docker.pdf`
- `Python Notes for Professionals.pdf`
- `PostgreSQL Notes for Professionals.pdf`

<!-- :contentReference[oaicite:17]{index=17} -->
</details>

