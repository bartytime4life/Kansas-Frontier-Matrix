# 📊 Tables (Experiment Artifacts)

![Artifact](https://img.shields.io/badge/artifact-tables-2ea44f) ![Format](https://img.shields.io/badge/formats-csv%20%7C%20tsv%20%7C%20parquet%20%7C%20md-blue) ![Goal](https://img.shields.io/badge/goal-reproducible%20%26%20auditable-purple)

> [!NOTE]
> This folder stores **tabular outputs** produced by an experiment run (metrics, comparisons, traceability, audits).  
> Keep tables **portable**, **deterministic**, and **provenance-linked** — “numbers with receipts” 🧾✨

---

## ✅ What belongs here?

Put a table here when it:
- backs a claim in the experiment report (“Model A improved recall by 6%”)
- summarizes results across runs / datasets / configs
- acts as a “ledger” linking artifacts together (traceability, model registry, dataset manifest)
- is something you’d want to plot later (dashboards, regression tracking, drift monitoring)

---

## 🧱 Recommended file layout

```text
📁 artifacts/
  📁 tables/
    📄 README.md
    📄 tables_manifest.yml            # ✅ index of tables + provenance pointers
    📄 TBL-001_traceability_matrix.csv
    📄 TBL-010_metrics_summary.csv
    📄 TBL-020_ablation_study.csv
    📄 TBL-030_error_slices.csv
    📄 TBL-040_model_registry.csv
    📄 TBL-900_governance_redactions.csv
    📁 _snapshots/                    # optional: exact “as-used” exports
```

> [!TIP]
> If the table is **big** or **multi-typed**, prefer **Parquet** (and/or GeoParquet for geospatial).  
> If the table is **human-first**, a Markdown table is fine — but still index it in the manifest.

---

## 🧾 Table manifest (required)

Every table in this folder should be listed in **`tables_manifest.yml`** so the experiment report (and tooling) can discover and validate artifacts.

### Minimal manifest shape

```yaml
tables:
  - table_id: "TBL-010"
    title: "Metrics Summary"
    file: "TBL-010_metrics_summary.csv"
    purpose: "Primary results table for the report"
    produced_by:
      run_id: "RUN-2026-01-22T031500Z"
      code_ref: "git:commit:<sha>"
      pipeline: "mcp/dev_prov/examples/10_experiment_report_template"
    inputs:
      - kind: "dataset"
        ref: "dcat:<dataset-id-or-uri>"
      - kind: "artifact"
        ref: "../figures/FIG-010_roc_curve.png"
    provenance:
      prov_ref: "../prov/PROV-RUN-2026-01-22T031500Z.jsonld"
      evidence_manifest_ref: "../evidence/EM-010.yaml"
    governance:
      sensitivity: "public"
      care_label: "none"
      contains_pii: false
    integrity:
      sha256: "<optional-but-nice>"
```

> [!IMPORTANT]
> Keep the **data table clean** (columns that matter to analysis).  
> Put “meta” in the **manifest** and/or a **PROV/evidence manifest** sidecar.

---

## 🏷️ Naming conventions

### File naming
Use stable, sortable, greppable names:

- `TBL-###_<short_slug>.<ext>`
- Prefer `snake_case` for slugs
- Keep IDs stable once referenced in a report

Examples:
- `TBL-001_traceability_matrix.csv`
- `TBL-010_metrics_summary.csv`
- `TBL-040_model_registry.csv`
- `TBL-900_governance_redactions.csv`

### Column naming
- `snake_case`
- include units in the header when ambiguous: `area_sq_km`, `temp_c`, `lat_deg`
- avoid “magic” abbreviations unless documented

---

## 📦 Preferred formats (pick the lightest tool that works)

| Format | Use when | Pros | Watch-outs |
|---|---|---|---|
| `.csv` | default | universal, diffable-ish | escaping/encoding; no types |
| `.tsv` | many text fields | fewer quoting headaches | still no types |
| `.parquet` | large / typed / repeated | compact, typed, fast | not as human-friendly |
| `.md` | tiny, human-first tables | reads great in GitHub | not ideal for stats/plots |
| `.xlsx` | **avoid** (unless required) | stakeholder convenience | not diff-friendly; always export csv too |

---

## 🧪 “Standard tables” we expect to see

### 1) Traceability matrix (high value)
A birds-eye table that connects **experiment → hypothesis/feature → code → data/model → result references**.

Suggested columns:
- `experiment_id`
- `hypothesis_or_feature`
- `code_version`
- `data_version`
- `model_version`
- `result_refs` (paths/IDs to figures/tables/artifacts)

---

### 2) Metrics summary (primary results)
Suggested columns:
- `run_id`, `model_id`, `dataset_id`, `split`
- `metric_name`, `metric_value`
- `ci_low`, `ci_high` (optional)
- `notes`

---

### 3) Ablation / baseline comparison
Suggested columns:
- `variant_id`, `variant_desc`
- `baseline_metric`, `candidate_metric`, `delta`
- `n`, `stat_test`, `p_value` (optional)

---

### 4) Error slices / fairness / robustness
Suggested columns:
- `slice_key`, `slice_value`
- `count`, `metric_value`
- `risk_notes`, `mitigation_ref`

> [!CAUTION]
> If slices could reveal sensitive attributes or locations, aggregate/blur/redact and document it in `TBL-900_*`.

---

### 5) Model registry (when you train/produce models)
A simple “table of models” so any model can be traced back to the conditions that produced it:
- `model_id`
- `training_data_ref` (+ version)
- `code_ref`
- `params_ref`
- `evaluation_ref`

---

## 🔁 Determinism rules (so diffs don’t lie)

- **Sort rows** by a stable key (e.g., `run_id`, `model_id`, `metric_name`)
- **Round floats** consistently (pick a precision and stick to it)
- **Use UTF-8**
- **No hidden filters** (if exporting from notebooks/spreadsheets, double-check)

---

## 🛡️ Safety, governance, and redaction

If the experiment touches sensitive info (PII, vulnerable locations, restricted sources):
- **do not** store raw sensitive rows here
- store aggregated/blurred outputs + a short explanation table like:
  - `TBL-900_governance_redactions.csv`

Recommended columns:
- `artifact_id`, `risk_type`, `what_was_removed`, `why`, `approved_by`, `policy_ref`

---

## 🧩 How tables get used downstream (UI + reports)

Tables in this folder may be:
- embedded in the experiment report as “results”
- plotted into figures
- promoted into dashboards/time-series monitoring
- indexed for search and future “evidence manifests”

> [!TIP]
> If a table becomes a long-lived product (not just a one-off experiment), consider “promoting” it into the platform’s dataset/catalog patterns (with STAC/DCAT/PROV + policy gates).

---

## 🔗 How to reference tables from the experiment report

In your experiment report Markdown:

```md
See the full metrics breakdown in: [TBL-010 Metrics Summary](./artifacts/tables/TBL-010_metrics_summary.csv)
```

For wide tables:
- link to the file
- add a short top-line summary in the report body

---

## ✅ Definition of Done (DoD) for tables ✅

- [ ] Table is listed in `tables_manifest.yml`
- [ ] Filename follows `TBL-###_<slug>.<ext>`
- [ ] Rows are deterministically sorted
- [ ] Units/definitions are clear (or linked)
- [ ] Provenance pointers exist (run id, code ref, input refs)
- [ ] No sensitive data leaks (or redaction table included)
- [ ] Report links to the table from the relevant section

---

## 🧠 Pro tips (tiny things that save hours)

- Keep an “ID column” even if it feels redundant (future joins will thank you 🙏)
- Prefer “long form” for metrics (`metric_name`, `metric_value`) when you expect new metrics
- When comparing runs, store both:
  - the **raw metrics table**
  - the **comparison/delta table** (so your narrative is directly supported)

---
