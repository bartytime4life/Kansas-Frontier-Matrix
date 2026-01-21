# 🧪 MCP Experiment Templates (KFM)

![MCP](https://img.shields.io/badge/MCP-Experiment%20Templates-blue)
![Docs](https://img.shields.io/badge/docs-documentation--first-success)
![Evidence](https://img.shields.io/badge/ethos-provenance--first-informational)

> [!NOTE]
> This folder is the **canonical copy/paste kit** for documenting **reproducible** experiments in the Kansas Frontier Matrix (KFM) ecosystem — spanning **data intake**, **geospatial processing**, **AI/Focus Mode**, **UI/Story Nodes**, **simulations**, and **governance/policy**.

---

## 🎯 Why this exists

KFM treats experiments as **first-class, reviewable artifacts**:
- **Evidence-first**: every claim can be traced to sources / inputs / provenance.
- **Reproducible**: same inputs + same config + same code = same outputs.
- **Governed**: policy gates & ethical constraints are part of the experiment, not “after the fact”.
- **Human-in-the-loop**: automation can propose, but humans approve (especially for publication).

These templates are aligned with:
- provenance-first intake & metadata standards (STAC/DCAT/PROV),
- KFM’s Focus Mode requirements (citations + refusal when unsourced),
- policy-as-code & CI checks,
- Story Nodes + interactive narrative UX,
- longer-term ideas like OCI artifact publishing, federation, AR, and 4D digital twins.

---

## ⚡ Quick start (copy → fill → run → publish)

1. **Create a new experiment folder** (usually under `mcp/experiments/`):
   - ✅ recommended naming: `EXP-YYYYMMDD--short-slug`  
   - examples: `EXP-20260121--pmtiles-vs-mvt-perf`, `EXP-20260121--focusmode-citations-gate`

2. **Copy the templates** from this folder into your experiment folder.

3. **Fill in the experiment docs** (especially the report + metadata + evidence manifest).

4. **Run the experiment** (pipeline, notebook, script, UI prototype, policy test, etc.).

5. **Record results**:
   - metrics (`metrics.json` or `metrics.csv`)
   - artifacts (plots, tiles, reports, trained weights)
   - provenance (PROV JSON-LD, run manifest)

6. **Open a PR** and link:
   - the experiment report
   - evidence manifest
   - outputs (or OCI references)

> [!TIP]
> If you’re not sure which template to use: start with the **Core** set (Report + Metadata + Evidence + Metrics + Provenance). Everything else is optional add-ons.

---

## 🗂️ Expected folder layout (templates vs actual runs)

```text
📁 mcp/
  📁 templates/
    📁 experiments/
      📄 README.md                      👈 you are here
      📄 TEMPLATE__EXPERIMENT_REPORT.md
      📄 TEMPLATE__EXPERIMENT_META.yaml
      📄 TEMPLATE__EVIDENCE_MANIFEST.yaml
      📄 TEMPLATE__METRICS.json
      📄 TEMPLATE__PROV.prov.jsonld
      📄 TEMPLATE__RUN_MANIFEST.json
      📄 TEMPLATE__MODEL_CARD.md
      📄 TEMPLATE__DATASET_DATASHEET.md
      📄 TEMPLATE__UI_TEST_PLAN.md
      📄 TEMPLATE__SIM_RUN.md
      📄 TEMPLATE__DECISION_RECORD.md

  📁 experiments/
    📁 EXP-20260121--example/
      📄 README.md                      (filled experiment report)
      📄 experiment.yaml
      📁 evidence/
      📁 results/
      📁 artifacts/
      📁 logs/
```

And remember: **data belongs in KFM’s standard data areas** (not ad-hoc folders):
- `data/raw/` → immutable “as received” evidence
- `data/work/` → deterministic transforms / staging
- `data/processed/` → publish-ready derivatives

---

## 🧩 Template pack: what each file is for

### ✅ Core (use for almost every experiment)
- **`TEMPLATE__EXPERIMENT_REPORT.md`**  
  Narrative write-up: question → hypothesis → method → results → decision → next steps.
- **`TEMPLATE__EXPERIMENT_META.yaml`**  
  Machine-readable metadata: scope, datasets, regions, timeframe, owners, risk tags.
- **`TEMPLATE__EVIDENCE_MANIFEST.yaml`**  
  “What evidence supports this?” inputs, citations, hashes, licenses, constraints.
- **`TEMPLATE__METRICS.json`**  
  Results in a consistent format (perf, quality, UX, accuracy, coverage).
- **`TEMPLATE__PROV.prov.jsonld`**  
  Formal lineage: used entities → activity → generated entities.

### ➕ Add-ons (pick what matches your experiment type)
- **`TEMPLATE__RUN_MANIFEST.json`**  
  Reproducibility contract (env, seeds, commit SHA, hardware, parameters).
- **`TEMPLATE__MODEL_CARD.md`**  
  Required for ML/GeoAI outputs (training data, eval, limits, bias/risks).
- **`TEMPLATE__DATASET_DATASHEET.md`**  
  Required when introducing a new dataset or materially changing one.
- **`TEMPLATE__UI_TEST_PLAN.md`**  
  For UI/UX changes (timeline, story nodes, map layers, accessibility, perf).
- **`TEMPLATE__SIM_RUN.md`**  
  For simulations + scenario runs (inputs, calibration, uncertainty, outputs).
- **`TEMPLATE__DECISION_RECORD.md`**  
  When an experiment drives a platform decision (adopt/reject/iterate).

---

## 🧬 Experiment types (and what “good” looks like)

> [!IMPORTANT]
> Different experiments have different success criteria — but **all** must meet the provenance, reproducibility, and governance baseline.

### 1) 📥 Data intake & metadata experiments
Use when testing:
- STAC/DCAT/PROV coverage & correctness
- deterministic ingestion patterns
- W-P-E agents in CI
- schema validation & link checks

**Key metrics**
- schema pass rate
- missing required fields count
- provenance completeness score
- policy gate violations (by rule)

### 2) 🗺️ Geospatial processing & tiling experiments
Use when testing:
- PMTiles vs vector tiles vs raster tiles
- GeoParquet vs GeoJSON vs Shapefile transforms
- PostGIS query performance & indexing strategy

**Key metrics**
- tile generation time
- artifact size (per zoom / per region)
- map FPS / render latency
- query latency (bbox/time/window)

### 3) 🤖 AI / Focus Mode experiments
Use when testing:
- retrieval quality (graph + text + spatial)
- citation enforcement (“refuse if unsourced”)
- explainability surfaces (audit panels, factors, flags)
- entity extraction + graph linking

**Key metrics**
- citation coverage (% answers with valid sources)
- refusal correctness (refuse when should)
- hallucination rate (should be near-zero)
- latency (P50/P95)
- user task success (when paired with UI tests)

### 4) 🧭 UI / Story Node / narrative experiments
Use when testing:
- Story Nodes + guided tours
- timeline navigation and temporal layering
- “map behind the map” provenance UI
- offline packs & field usability
- AR prototypes (early stage)

**Key metrics**
- task completion time
- accessibility checks (keyboard nav, contrast, ARIA)
- performance (load time, frame rate)
- provenance visibility (can users find source + license?)

### 5) 🧊 Simulation & scenario experiments
Use when testing:
- kfm-sim-run style workflows
- calibration/bias correction steps
- uncertainty capture
- scenario comparisons & visualization

**Key metrics**
- reproducibility (bitwise or tolerance bounds)
- calibration error vs reference
- sensitivity analysis outputs
- provenance completeness of model inputs/params/outputs

### 6) 🛡️ Governance / policy / safety experiments
Use when testing:
- OPA / Conftest policy pack behavior
- sensitivity tagging + obfuscation methods
- cultural protocol enforcement
- licensing compliance automation

**Key metrics**
- policy failures by severity
- false positive / false negative rate for gates
- sensitivity leakage tests
- license coverage & conflicts

---

## ✅ “Definition of Done” for an experiment (MCP baseline)

Before an experiment can be considered “done” (and merged), it should have:

- ✅ clear question & hypothesis  
- ✅ explicit scope (region, timeframe, dataset IDs)  
- ✅ deterministic method (code/config, not manual edits)  
- ✅ **evidence manifest** with sources + licenses + hashes  
- ✅ provenance artifact (PROV) or equivalent run lineage  
- ✅ metrics captured in a consistent machine-readable way  
- ✅ policy checks run (or explicitly waived with rationale)  
- ✅ decision recorded (adopt / reject / iterate)  
- ✅ follow-up tasks filed (if needed)

> [!WARNING]
> Experiments that introduce data *without licenses*, *without provenance*, or *without sensitivity classification* should be treated as **fail-closed**.

---

## 🤖 Agent-assisted experiments (W–P–E friendly)

KFM’s Watcher–Planner–Executor approach is designed so that automation can:
- detect issues (Watcher),
- propose a deterministic plan (Planner),
- open a PR (Executor),
- **never silently merge** unless policy explicitly allows it.

When your experiment uses W-P-E or similar automation, ensure your docs include:
- idempotency key / commit seed
- kill-switch behavior (how to disable safely)
- provenance links to watcher alerts & planner reasoning
- explicit statement of what was automated vs human-reviewed

---

## 📦 Publishing outputs (files, registries, catalogs)

Depending on experiment type, outputs may be published as:
- **repo artifacts** (small, diffable results)
- **data area artifacts** (large datasets, tiles, rasters)
- **OCI artifacts** (for larger, signed, versioned outputs)

**Preferred pattern (KFM-style)**
1. generate output
2. attach provenance (PROV)
3. publish distribution pointers in metadata (DCAT distributions + STAC links)
4. optionally sign artifacts (supply-chain integrity)

---

## 🧠 Using the project’s “Research Library” PDFs in experiments

Some project files are **PDF portfolios** (collections). They are meant to be referenced in experiment docs for:
- background research & known-good methods
- statistical validation and evaluation design
- geospatial rendering, projections, and WebGL pipelines
- AI/ML best practices and model evaluation

> [!TIP]
> In your experiment report, add a “Background” section that explicitly links to the relevant portfolio(s) and the specific embedded docs you relied on.

---

## 📚 Reference docs used to shape these templates

### 🧱 Core KFM architecture & rules
- 🧠 KFM – AI System Overview 🧭🤖 :contentReference[oaicite:0]{index=0}  
- 🏗️ KFM – Comprehensive Architecture, Features, and Design :contentReference[oaicite:1]{index=1}  
- 🧩 KFM – Comprehensive Technical Documentation :contentReference[oaicite:2]{index=2}  
- 🎛️ KFM – Comprehensive UI System Overview :contentReference[oaicite:3]{index=3}  
- 📥 KFM – Data Intake (Technical & Design Guide) :contentReference[oaicite:4]{index=4}  
- 🌟 KFM – Latest Ideas & Future Proposals :contentReference[oaicite:5]{index=5}  
- 💡 Innovative Concepts to Evolve KFM :contentReference[oaicite:6]{index=6}  
- 🧠 Additional Project Ideas (incl. refinement proposals) :contentReference[oaicite:7]{index=7}  

### 🧾 MCP / documentation standards
- 🧪 Scientific Method / Research / MCP Documentation :contentReference[oaicite:8]{index=8}  
- 📝 MARKDOWN_GUIDE_v13 (repo structure, templates, DoD) :contentReference[oaicite:9]{index=9}  
- 🗺️ Open-Source Geospatial Historical Mapping Hub Design :contentReference[oaicite:10]{index=10}  

### 📦 Research library portfolios (open in Acrobat for embedded docs)
- 🤖 AI Concepts & more (portfolio) :contentReference[oaicite:11]{index=11}  
- 🧭 Maps / Google Maps / Virtual Worlds / WebGL (portfolio) :contentReference[oaicite:12]{index=12}  
- 🗄️ Data Management / Data Science / Bayesian Methods (portfolio) :contentReference[oaicite:13]{index=13}  
- 🧰 Various programming languages & resources (portfolio placeholder) :contentReference[oaicite:14]{index=14}  

---

## 🧷 Notes for maintainers

- Keep templates **small + composable**: most experiments shouldn’t need every file.
- If KFM adds a new gate (policy, schema, sensitivity), update templates first.
- Prefer **machine-readable** artifacts (`*.json`, `*.yaml`) alongside narrative (`*.md`).
- When new domains appear (e.g., archaeology, hydrology, education), add a template add-on rather than bloating the core.

---

## ✅ Next recommended additions (optional)

<details>
<summary>📌 Suggested template improvements</summary>

- `TEMPLATE__POLICY_REPORT.md` (auto-generated conftest/OPA summary)
- `TEMPLATE__PERF_BENCHMARK.md` (tile/query/UI perf harness notes)
- `TEMPLATE__DATA_QUALITY_CHECKLIST.md` (crowdsourcing + consensus workflows)
- `TEMPLATE__SENSITIVITY_REVIEW.md` (CARE/cultural protocol + obfuscation plan)

</details>

