# 🧪📦 `results/` — Experiment Outputs (MCP • Dev Prov • Template)

Welcome to the **Results** folder for the `10_experiment_report_template` example tree. This directory is where an experiment’s **final, reviewable outputs** live: metrics, artifacts, provenance, and “what changed + why it matters”.

> 🧭 Rule of thumb: **If it influenced a decision, it belongs here** (or is referenced from here).

---

## 🗺️ Reading order (recommended)

1. ✅ **`summary.md`** — the “executive summary” (what you’d paste into a PR)
2. 📊 **`metrics/`** — numbers + comparisons (with confidence & caveats)
3. 🧾 **`provenance/`** — lineage, evidence manifests, and run metadata
4. 🧪 **`artifacts/`** — plots, maps, exports, screenshots, samples
5. 🧰 **`logs/`** — debugging & audit trail (only what’s needed)

---

## 🌲 Suggested results tree (example)

```text
results/
  README.md                # (you are here)
  summary.md               # human-first, 1–2 pages max
  changelog.md             # notable diffs vs baseline / previous runs (optional)

  run/
    run_manifest.json      # run_id, timestamp, git sha, command, params, inputs hash
    env.txt                # python/node versions, platform, key libs
    requirements.txt       # pip freeze (or lockfile reference)
    seeds.json             # all RNG seeds used
    timings.csv            # stage timings (ETL, retrieval, model, validation)
    warnings.md            # known issues, policy waivers, edge cases

  metrics/
    metrics.json           # primary metrics (machine-readable)
    metrics.md             # human-readable highlights + interpretation
    ablation.csv           # optional: ablations table
    confusion_matrix.csv   # optional: classification style tasks
    drift_report.json      # optional: drift/bias checks summary

  artifacts/
    figures/
      *.png
      *.svg
    exports/
      *.geojson
      *.parquet
      *.pmtiles
      *.csv
    samples/
      example_inputs/
      example_outputs/
    notebooks/
      *.ipynb
      *.html

  provenance/
    prov.jsonld            # lineage (W3C PROV)
    evidence_manifest.json # “claims -> sources -> transforms -> outputs”
    catalogs/
      stac/
        collection.json
        item_*.json
      dcat/
        dataset.jsonld
    governance/
      policy_eval.json     # policy-as-code results (allow/deny + reasons)
      approvals.md         # reviewer sign-offs (if needed)
      ledger_ref.json      # pointer/ID into an immutable governance ledger (if used)
```

> 🧠 Tip: keep file names boring + sortable. Prefer:  
> `YYYY-MM-DD__exp-####__short_slug/…` (if you later nest multiple runs under `results/`).

---

## ✅ Minimum “Definition of Done” (DoD) for results

Use this as a checklist before you call a run “real” (template-friendly ✅).

- [ ] **`summary.md`** exists and answers: *What did we test? What changed? What won? What broke?*
- [ ] **`metrics/metrics.json`** exists (machine-readable) and includes:
  - [ ] baseline reference (or “N/A” with reason)
  - [ ] confidence / uncertainty where applicable
  - [ ] dataset/version IDs (not just filenames)
- [ ] **`run/run_manifest.json`** exists and includes:
  - [ ] `run_id`
  - [ ] git commit SHA
  - [ ] command line (or entrypoint) used
  - [ ] key parameters + seeds
  - [ ] input digests / checksums
- [ ] **`provenance/prov.jsonld`** exists (or a clearly documented equivalent)
- [ ] **Policy checks are recorded** (`provenance/governance/policy_eval.json`)
- [ ] **Artifacts are referenced** (not orphaned): `summary.md` links to the important plots/exports
- [ ] **Repro path is stated**: “how to rerun this” in 3–6 lines (even if it’s slow)

---

## 🧷 What goes in `summary.md` (keep it sharp)

A good `summary.md` is a PR-ready narrative:

- 🎯 **Goal** (what hypothesis / decision is this run answering?)
- 🧰 **Method** (what changed: data, model, prompt, pipeline stage?)
- 🧪 **Results** (key numbers + key artifacts)
- 🧠 **Interpretation** (why it happened, tradeoffs, failure modes)
- 🔁 **Next steps** (ship / iterate / rollback)
- ⚠️ **Risk & governance notes** (sensitivity, CARE constraints, policy flags)

---

## 🧾 Provenance expectations (evidence-first, not vibes)

This project favors **traceable outputs**. Treat provenance like a first-class deliverable:

- **Every derived file** should be traceable to:
  - source inputs
  - transforms/configs
  - tool versions + parameters
  - responsible agent/person (human or automated)
- If your experiment produces “answer-like” content (summaries, narratives, classifications), store:
  - **the evidence manifest**
  - **the policy evaluation**
  - **the exact inputs retrieved** (or immutable references/digests)

> If you can’t reproduce it, it’s not a result — it’s a screenshot.

---

## 🛡️ Policy & QA gates (how to think about failures)

Use **gates** to keep bad outputs from becoming “official”:

- Metadata completeness (schemas, required fields)
- License presence (no unknown license)
- Sensitivity classification (and correct handling)
- Provenance completeness (no missing lineage)
- AI outputs: citations/evidence required (or output is rejected)

When a gate fails:
- Put the failure details in `provenance/governance/policy_eval.json`
- Summarize in `summary.md` under **⚠️ Known Issues**
- If you had to override anything, record the **who/why/when** in `approvals.md`

---

## 🧠 Results that feed UI/Storytelling (if applicable)

If your experiment outputs Story Nodes, guided tours, map states, or similar UI content:

- store the **rendered artifacts** (screenshots, exports)
- store the **source content** (Markdown + JSON configs) as part of the experiment artifacts
- store a **preview recipe** (how a reviewer opens/validates it locally)

---

## 📌 Tips for clean diffs & easy review

- ✅ Prefer **small, legible artifacts** (downsampled previews + a link/ref to the full resolution)
- ✅ Use **CSV/JSON** for metrics so CI can diff and chart them
- ✅ Keep logs “thin”: errors + warnings + key stage summaries
- ✅ Always include **baselines** when possible
- ✅ Always include **one “golden example”** input/output pair for sanity checking

---

## 🔧 Quick “How to reproduce” template (paste into `summary.md`)

```bash
# 1) set up env
# (fill in: conda/uv/pip/npm)
<SETUP_COMMANDS>

# 2) run the experiment
<RUN_COMMAND> --config <PATH> --seed <N>

# 3) validate results (schemas + policy)
<VALIDATE_COMMAND>

# 4) regenerate artifacts (optional)
<RENDER_COMMAND>
```

---

## 🧰 Appendix: `run_manifest.json` (starter schema)

```json
{
  "run_id": "2026-01-22__exp-0010__example_slug",
  "timestamp_utc": "2026-01-22T00:00:00Z",
  "git": { "repo": "Kansas-Frontier-Matrix", "commit": "<sha>", "dirty": false },
  "entrypoint": "<command or workflow name>",
  "params": { "key": "value" },
  "seeds": { "python": 0, "numpy": 0, "torch": 0 },
  "inputs": [
    { "name": "dataset_x", "ref": "<stac/dcat id>", "sha256": "<digest>" }
  ],
  "outputs": [
    { "path": "metrics/metrics.json", "sha256": "<digest>" }
  ]
}
```

---

<details>
<summary>📚 Why this structure exists (click to expand)</summary>

This results layout is designed to support:

- 🔁 **Reproducibility** (run manifests + deterministic configs)
- 🧾 **Auditability** (provenance + governance outputs)
- 🧪 **Comparability** (metrics in diff-friendly formats)
- 🧑‍⚖️ **Reviewability** (summaries and curated artifacts, not raw dumps)
- 🗺️ **Geospatial + narrative workflows** (exports + story content + previews)

</details>
