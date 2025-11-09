```markdown
---
title: "🎯 Focus Mode AI — Context vs. Environment Heuristic Evaluation (v1)"
path: "src/ai/focus/evaluation/context-vs-environment/README.md"
version: "v9.7.0"
last_updated: "2025-11-09"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/focus-eval-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🎯 **Focus Mode AI — Context vs. Environment Heuristic Evaluation**
`src/ai/focus/evaluation/context-vs-environment/README.md`

**Purpose:** Define a repeatable session to measure how **Focus Mode AI** balances **historical context weighting** vs. **environmental variables** (weather, hydrology, landcover, ownership, fauna, etc.). We will tune heuristics so the model’s interpretive output is **faithful, useful, and auditable** under FAIR+CARE.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)](../../../../docs/standards/fair-care/README.md)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](#)

</div>

---

## 📘 Overview

**Historical context weighting** = how strongly the model prioritizes time-aware, provenance-linked facts (e.g., 1870s plat maps, 1930s drought reports, 1950s aerials).  
**Environmental variables** = contemporaneous or reconstructed signals (e.g., LiDAR hillshade, flood recurrence, soil, microclimate, species presence, ownership parcels).

This evaluation isolates and then blends both to find the **optimal weighting schedule** per task type (discovery, explanation, ranking, mapping).

---

## 🗂️ Directory Layout

```

src/ai/focus/evaluation/context-vs-environment/
├── configs/                               # Experiment configs (YAML/JSON)
│   ├── context_only.yaml                  # Context=1.0, Environment=0.0
│   ├── env_only.yaml                      # Context=0.0, Environment=1.0
│   ├── blended_grid.yaml                  # Grid-search over weights
│   └── ablation.yaml                      # Feature drop/disable tests
├── datasets/                              # Curated eval sets (links or small refs)
│   ├── tasks/                             # Task definitions & gold labels
│   └── splits/                            # train/val/test manifests
├── metrics/                               # Metric calculators & schemas
│   ├── explainability/                    # SHAP/LIME export adapters
│   └── provenance/                        # Lineage completeness checks
├── runs/                                  # Generated artifacts (gitignored)
│   ├── logs/                              # Structured logs/telemetry
│   ├── reports/                           # HTML/MD summaries
│   └── shards/                            # Intermediate caches
├── scripts/                               # CLI entrypoints
│   ├── run_grid_search.py                 # Weight grid search
│   ├── run_ablation.py                    # Feature ablations
│   ├── summarize_reports.py               # Compile eval dashboards
│   └── export_explanations.py             # SHAP/LIME packs
└── README.md

````

---

## 🧩 Evaluation Design

### Tasks (representative KFM use-cases)

| Task ID | Description | Primary Signal | Gold/Label Source |
|---|---|---|---|
| T1 | Rank candidate “lost homestead” sites | Historical context | Cross-checked plats + registry |
| T2 | Explain why a site likely had human activity in year-range | Context → Env | Curated expert rationales |
| T3 | Prioritize survey tiles for field validation | Environmental | Hydrology + access + risk |
| T4 | Suggest interpretive panel copy (public history) | Context (time-aware) | Editor-reviewed text set |

### Weighting Schedule

We define scalar weights **w_c** (context) and **w_e** (environment) such that **w_c + w_e = 1.0**. The fusion layer accepts normalized feature groups and computes:
- **score = w_c · f_context + w_e · f_environment**

We sweep **w_c ∈ {1.0, 0.8, 0.6, 0.4, 0.2, 0.0}** (complement for **w_e**).

---

## 🧾 Metrics

| Category | Metric | Why it matters | Notes |
|---|---|---|---|
| Discovery | nDCG@k, MAP | Ranking quality | On T1, T3 |
| Faithfulness | Attributed Fact Precision | Cites correct time/place | Requires provenance anchors |
| Explanation | Rationale Helpfulness (Likert), Token Evidence Overlap | Human eval + text-to-evidence | Blind annotators |
| Robustness | Performance Drop under Ablation | Sensitivity to signal loss | Compare to baseline |
| Governance | Provenance Completeness %, License Pass | FAIR+CARE alignment | From lineage graph |
| Energy | J/Inference, gCO₂e/Run | Sustainability | From telemetry_ref schema |

---

## ⚙️ Heuristics Under Test

| Heuristic | Description | Control Range | Default |
|---|---|---|---|
| H1: Time-Proximity Boost | Prefer sources closer to target year-range | 0.0–2.0 | 1.0 |
| H2: Provenance Depth Bonus | Reward multi-hop, corroborated sources | 0.0–1.5 | 0.8 |
| H3: Spatial Concordance | Penalize mismatched footprints | 0–100 m tolerance | 25 m |
| H4: Env Variability Gate | Downweight volatile env layers | 0.0–1.0 | 0.5 |
| H5: Narrative Coherence | Encourage consistent, non-contradictory chains | 0.0–1.0 | 0.6 |

---

## 🧪 Procedure (One-Command Session)

**Goal:** run grid search over weights + ablations, export reports, and produce explainability packs.

```bash
# From repo root
python src/ai/focus/evaluation/context-vs-environment/scripts/run_grid_search.py \
  --config src/ai/focus/evaluation/context-vs-environment/configs/blended_grid.yaml \
  --tasks  T1 T2 T3 T4 \
  --outdir src/ai/focus/evaluation/context-vs-environment/runs

python src/ai/focus/evaluation/context-vs-environment/scripts/run_ablation.py \
  --config src/ai/focus/evaluation/context-vs-environment/configs/ablation.yaml \
  --outdir src/ai/focus/evaluation/context-vs-environment/runs

python src/ai/focus/evaluation/context-vs-environment/scripts/export_explanations.py \
  --runs  src/ai/focus/evaluation/context-vs-environment/runs \
  --outdir src/ai/focus/evaluation/context-vs-environment/runs/reports/explainability
````

---

## 🧩 Components Flow

```mermaid
flowchart TD
  A["Start Session"] --> B["Load Tasks & Splits"]
  B --> C["Load Context Features (plats, archives, reports)"]
  B --> D["Load Environment Features (LiDAR, hydro, soil, landcover)"]
  C --> E["Normalize Context Features"]
  D --> F["Normalize Env Features"]
  E --> G["Fusion: score = w_c * f_context + w_e * f_env"]
  F --> G
  G --> H["Apply Heuristics H1–H5"]
  H --> I["Rank / Generate / Explain"]
  I --> J["Compute Metrics + Telemetry"]
  J --> K["Reports + SHAP/LIME Exports"]
```

---

## 🧾 Reporting & Acceptance

**Minimum acceptance per task (default thresholds):**

| Task | nDCG@10 | Attributed Fact Precision | Provenance Completeness | Energy Δ vs. baseline |
| ---- | ------: | ------------------------: | ----------------------: | --------------------: |
| T1   |  ≥ 0.78 |                         — |                  ≥ 0.90 |                 ≤ +5% |
| T2   |       — |                    ≥ 0.85 |                  ≥ 0.90 |                 ≤ +7% |
| T3   |  ≥ 0.75 |                         — |                  ≥ 0.85 |                 ≤ +5% |
| T4   |       — |                    ≥ 0.80 |                  ≥ 0.90 |                 ≤ +5% |

A run is **accepted** if all task-specific bars are met; else **flagged** for retune.

---

## 🧪 Quick Start Datasets (placeholders / link-outs)

* `datasets/tasks/`:

  * `lost_homestead_rank.jsonl` — T1 pairs with labels.
  * `site_explanations.jsonl` — T2 rationales with evidence IDs.
  * `survey_prioritization.jsonl` — T3 tiles with priorities.
  * `panel_copy_eval.jsonl` — T4 target blurbs + editor scores.

* `datasets/splits/`:

  * `train.json`, `val.json`, `test.json`

> Note: Store only small manifests here; large rasters and graphs referenced via URIs in the repo’s data catalog.

---

## ♿ Accessibility & FAIR+CARE Notes

* Cite sources with **time and place**; include community-sensitive tags where applicable.
* Avoid deterministic claims on culturally sensitive sites; prefer **probabilistic language** and **consent-aware** metadata.

---

## 🕰️ Version History

| Version | Date       | Author    | Summary                                                    |
| ------- | ---------- | --------- | ---------------------------------------------------------- |
| v9.7.0  | 2025-11-09 | Core Team | Initial evaluation design, metrics, CLI, reporting layout. |

---

<div align="center">

© Kansas Frontier Matrix — Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
[Back to docs/] · [Governance Charter]

</div>
```
