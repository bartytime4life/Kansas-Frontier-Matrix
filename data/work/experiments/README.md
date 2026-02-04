# 🧪 Experiments Lab — `data/work/experiments/`

![Provenance First](https://img.shields.io/badge/provenance-first-2ea44f)
![Reproducible](https://img.shields.io/badge/reproducible-by%20default-blue)
![Truth Path](https://img.shields.io/badge/pipeline-Raw%E2%86%92Processed%E2%86%92Catalog%E2%86%92DB%E2%86%92API%E2%86%92UI-8a2be2)
![Scope](https://img.shields.io/badge/scope-Kansas%20Frontier%20Matrix%20(KFM)-gold)

Welcome to the KFM **sandbox** 🧰—where we test ideas, validate hypotheses, benchmark performance, prototype GIS workflows, and trial AI models **without breaking the “truth path.”**  

> ✅ Goal: turn experiments into **traceable, shippable** datasets, layers, models, and stories.  
> ❌ Not a dumping ground: if it can’t be reproduced (or cited), it doesn’t belong here.

---

## 🔥 Quick Start (the 60-second ritual)

1) **Create a new experiment folder**
```bash
mkdir -p data/work/experiments/2026-02-03__kansas_river_ndvi__yourname
cd data/work/experiments/2026-02-03__kansas_river_ndvi__yourname
```

2) **Add the three required files**
- `experiment.yml` (what/why/how)
- `run.*` (how to reproduce)
- `RESULTS.md` (what happened)

3) **Run it, record it, package it**
- outputs go into `./artifacts/`
- figures go into `./figures/`
- logs go into `./logs/`

---

## 🗂️ Folder Layout (recommended)

```text
data/work/experiments/
├── README.md  👈 you are here
├── _templates/ 🧩 reusable manifests, scripts, report skeletons
└── 2026-02-03__kansas_river_ndvi__yourname/
    ├── experiment.yml           ✅ required
    ├── run.sh | run.py | run.R  ✅ required (one-click reproduction)
    ├── RESULTS.md               ✅ required (human summary)
    ├── notebooks/               📓 optional (exploration only)
    ├── src/                     🧠 code used by run.*
    ├── configs/                 ⚙️ params, AOIs, style specs
    ├── inputs/                  🔗 pointers only (NEVER raw dumps)
    ├── artifacts/               📦 generated data/products (non-final)
    ├── figures/                 🖼️ charts, maps, screenshots
    ├── logs/                    🧾 stdout/stderr + run metadata
    └── provenance/              🧬 citations + lineage notes
```

### ✅ What goes where?
| Thing | Put it here | Notes |
|---|---|---|
| Hypothesis / design | `experiment.yml` | keep it crisp + testable |
| One-click reproduction | `run.*` | no manual steps |
| Raw external data | **not here** | store in `data/raw/` via ingestion pipeline |
| Generated interim outputs | `artifacts/` | okay to be messy, but reproducible |
| Final shippable datasets | `data/processed/` | after review + metadata |
| Metadata (STAC/DCAT) | `data/catalog/` | required for publish |
| Lineage (W3C PROV style) | `data/provenance/` | required for publish |

---

## 🧭 The Lab Rules (non‑negotiables)

### 1) Don’t bypass the Truth Path 🚦
Experiments may explore freely, but anything that becomes **public-facing** must travel:
**Raw → Processed → Catalog → Database → API → UI/AI**  
No shortcuts. No “temporary” backdoors. No “just this once.”  

### 2) Inputs are **references**, not dumps 🔗
Inside an experiment folder, `inputs/` should contain:
- dataset IDs
- URLs
- query parameters
- bounding boxes / AOIs
- commit hashes
- checksums

### 3) Every chart/map needs a breadcrumb trail 🥾
If a figure lands in `figures/`, it must be traceable back to:
- source dataset(s)
- processing steps
- parameters
- code entrypoint (`run.*`)

### 4) Reproducibility beats cleverness ♻️
If the result can’t be recreated by someone else (or you-in-2-weeks), it’s not a result yet.

---

## 🧾 Experiment Manifest (`experiment.yml`) ✅

Use this as your baseline:

```yaml
id: 2026-02-03__kansas_river_ndvi__yourname
title: "Kansas River NDVI trend (2016–2025)"
owner: "yourname"
status: "draft" # draft | validated | shipped | archived
type:
  - remote_sensing
  - time_series
hypothesis: >
  NDVI along the Kansas River corridor shows distinct seasonal signatures and detectable multi-year change.
questions:
  - "What is the NDVI seasonal profile by county?"
  - "Are there statistically meaningful trends after controlling for seasonality?"

inputs:
  datasets:
    - id: "usgs_landsat_collection2"
      access: "stac"   # stac | api | file
      subset:
        aoi: "aoi/kansas_river_corridor.geojson"
        time: ["2016-01-01", "2025-12-31"]
  notes:
    - "inputs are pointers; no raw dumps in this folder"

methods:
  steps:
    - name: "fetch_scenes"
      tool: "stac-client"
    - name: "cloud_mask"
      tool: "python"
    - name: "compute_ndvi"
      tool: "python"
    - name: "aggregate"
      tool: "postgis/sql"
  parameters:
    cloud_threshold: 0.2
    ndvi_scale: 10000
    spatial_unit: "county"
    temporal_unit: "month"

outputs:
  artifacts:
    - path: "artifacts/ndvi_monthly.parquet"
    - path: "figures/ndvi_trends.png"
  candidate_publish:
    processed_dataset_id: "ks_ndvi_kansas_river_monthly_v1"

evaluation:
  checks:
    - "spot-check 10 scenes visually"
    - "validate AOI coverage"
    - "sanity bounds: NDVI ∈ [-1, 1]"
  metrics:
    - "coverage_pct"
    - "missingness_rate"

reproducibility:
  entrypoint: "run.sh"
  environment:
    python: "3.11"
    containers: true
  randomness:
    seed: 1337

provenance:
  citations_file: "provenance/SOURCES.md"
  lineage_file: "provenance/LINEAGE.md"

notes:
  - "If this ships: add STAC/DCAT + PROV docs and move dataset into the canonical pipeline."
```

---

## 🧬 Provenance Pack (minimum viable)

Create these two files:

### `provenance/SOURCES.md`
- Bullet list of **every** external dataset / document used
- License + attribution notes
- Access date(s)
- IDs, URLs, or catalog references

### `provenance/LINEAGE.md`
A human-readable chain like:
- **Input datasets** → **transforms** → **outputs**
- Include command lines + script names + key parameters

> Pro tip: treat this like “the map behind the map” 🗺️—someone should be able to audit the result.

---

## 🧠 Common Experiment Types (pick your flavor)

### 🗺️ Geospatial / GIS
- topology validation
- overlays / joins
- routing & networks
- tile generation sanity checks

### 🛰️ Remote Sensing
- STAC scene ingest tests
- COG/PMTiles generation experiments
- change detection, classification baselines

### 🤖 ML / AI
- baseline models, ablations, feature studies
- RAG retrieval quality checks
- bias/leakage audits (train/test hygiene)

### ⚡ Performance / Scalability
- API latency under load
- tile serving throughput
- DB query plans & caching behavior

### 🎛️ UI / Map UX
- layer styling trials
- time slider usability tests
- narrative “story node” prototypes

---

## ⚡ Performance Experiments (rules of clean measurements)

If you’re load-testing:
- keep load generators **separate** from the system under test
- write down the workload model (open vs closed, think time, concurrency)
- record response time + throughput + utilization, not just “it felt fast”

Suggested structure:
```text
perf/
├── test_plan.md
├── scenarios/
├── scripts/
├── raw_results/
└── report.md
```

---

## 📦 From Experiment → Shippable Output (the promotion ceremony)

When an experiment proves useful:

1) **Freeze the run**
- tag inputs (dataset IDs / commit hashes)
- lock dependencies
- make `run.*` one-command reproducible

2) **Promote artifacts**
- move cleaned outputs to `data/processed/<dataset_id>/...`
- write catalog metadata in `data/catalog/<dataset_id>.{json,yaml}`
- create lineage docs in `data/provenance/<dataset_id>/...`

3) **Integrate**
- load into DB / index as appropriate
- expose through API
- verify UI renders + citations show up

---

## 🧩 Templates

Use these starter files:
- `data/work/experiments/_templates/experiment.yml`
- `data/work/experiments/_templates/RESULTS.md`
- `data/work/experiments/_templates/SOURCES.md`
- `data/work/experiments/_templates/LINEAGE.md`

---

## ✅ RESULTS.md (recommended format)

```markdown
# Results — <experiment id>

## TL;DR
- ✅ what worked
- ❌ what didn’t
- 🤔 what surprised us

## What changed vs baseline?
- bullet list of deltas

## Artifacts
- `artifacts/...`
- `figures/...`

## Quality checks
- what you validated + outcomes

## Decision
- [ ] Archive
- [ ] Iterate
- [ ] Promote to `data/processed/` (with metadata + provenance)
```

---

## 🧠 Mermaid: experiment lifecycle (bird’s-eye view)

```mermaid
flowchart TD
  A[Idea / Hypothesis] --> B[Experiment Folder]
  B --> C[Run + Log + Artifacts]
  C --> D{Validated?}
  D -- No --> E[Iterate / Archive]
  D -- Yes --> F[Promote to Processed]
  F --> G[Catalog Metadata (STAC/DCAT)]
  G --> H[Provenance (W3C PROV-style)]
  H --> I[DB / Index]
  I --> J[API]
  J --> K[UI / AI Answers]
```

---

## 🧯 When to Archive an Experiment
Archive (don’t delete) if:
- it answered the question
- or the hypothesis was falsified
- or a better approach replaced it

Mark `status: archived` in `experiment.yml` and add a final note in `RESULTS.md`.

---

## 🙌 Philosophy (the vibe)
We’re building an evidence-first geospatial knowledge system—so experiments must be:
**testable ✅, reproducible ♻️, and traceable 🧾**.

Happy hacking. Keep the breadcrumbs. 🥖✨