---
name: "🧪 Experiment Report"
about: "Plan, run, and log a reproducible experiment (MCP-grade)"
title: "[EXP] <concise title>"
labels: ["mcp", "reproducibility", "experiment"]
assignees: []
---

> Use this template when **planning and completing** an experiment.  
> Keep everything **deterministic** and **copy–paste runnable**.

---

## 0) Metadata

- **Experiment ID**: `EXP-YYYYMMDD-<slug>`
- **Owner(s)**: @you
- **Status**: ☐ Planned ☐ Running ☐ Completed ☐ Abandoned
- **Scope areas**: `data` | `stac` | `web` | `src` | `scripts` | `ci` | `docker`
- **Related issues/PRs**: Fixes #…, Closes #…, Relates #…
- **Milestone**: `m1-data` | `m2-analytics` | `m3-story` | `m4-tech` | `m5-mcp`

---

## 1) Objective / Hypothesis

- **Question** — What are we trying to learn/compare?  
- **Hypothesis** — What outcome do you expect and why?  
- **Success criteria** — Metrics/thresholds/visuals that define “good”.

---

## 2) Datasets & Catalog

- **Inputs (IDs / paths)**  
  - STAC: `stac/items/<file>.json`, `stac/collections/<file>.json`  
  - Source descriptors: `data/sources/<file>.json|yml`
- **Spatial/temporal bounds** — bbox, date range
- **Licenses / provenance** — cite sources; note restrictions

**Sanity checks**
```bash
make stac-validate     # validate STAC items/collections
make config-validate   # optional: validate web/config/*.json
````

---

## 3) Methods / Protocol (SOP)

* **Design** — controls, treatments, parameter sweeps
* **SOP links** — `mcp/sops/<doc>.md`
* **Randomness** — seeds, sampling rules
* **Assumptions / constraints** — note explicitly

**Commands to reproduce (canonical)**

```bash
make fetch           # fetch new sources (if needed)
make cogs            # build COGs
make terrain         # terrain derivatives (hillshade/slope/aspect)
make stac            # regenerate STAC catalog artifacts
make site            # fallback layers.json + small vector mirrors
make site-config     # render web/config/app.config.json (from STAC)
```

---

## 4) Environment

* **Host** — local / CI / container
* **Image / Python** — `python -V` = …, Docker image = …
* **Hardware** — CPU/GPU, RAM
* **Key tools** — `rasterio`, `gdal`, `jinja2`, `jsonschema`, `kgt`

```bash
python -V
pip freeze > env.txt   # attach file in PR
```

---

## 5) Variables & Configuration

* **Parameters** — list knobs (e.g., hillshade azimuth, Z-factor, resampling)
* **Config files edited** — paths + diffs
* **Hash snapshot(s)**

```bash
git rev-parse HEAD > build/git_sha.txt
(sha256sum data/cogs/**/* 2>/dev/null || true) | sort > build/artifact_hashes.txt
```

---

## 6) Results

* **Metrics** — tables / JSON snippets
* **Visuals** — screenshots, Pages preview link
* **Qualitative notes** — anomalies, CRS alignment issues

---

## 7) Analysis & Interpretation

* Did results meet success criteria? Why / why not?
* Threats to validity — sampling bias, CRS mismatch, georef error
* Error bars / uncertainty — how shown in outputs/UI

---

## 8) Artifacts

* **Generated files**

  * COGs: `data/cogs/**/<file>.tif`
  * Metadata: `*.meta.json` with `checksum:sha256`, `file:size`
  * Reports: `build/stac_report.json`, `build/metrics.json`

* **Experiment folder** (commit optional)

  ```
  mcp/experiments/EXP-YYYYMMDD-<slug>/
    README.md
    commands.sh
    env.txt
    figures/
    artifacts.jsonl
  ```

---

## 9) Ethics / Privacy / Legal

* [ ] Sensitive locations generalized or withheld
* [ ] Licenses verified / attribution added
* [ ] Indigenous/community data use reviewed (if applicable)

---

## 10) Roll-forward Plan

* Adopt / discard / iterate?
* **Follow-ups** (convert to issues)

  * [ ] …
  * [ ] …

---

## Checklists

**Before running**

* [ ] Sources & STAC entries exist and validate
* [ ] Make targets documented
* [ ] Seeds/randomness policy set

**Before merging**

* [ ] Results reproducible with commands above
* [ ] STAC assets include `checksum:sha256` and `file:size`
* [ ] Site rebuilt (`make site`, `make site-config`) if visuals changed
* [ ] SOP/docs updated if workflows changed

---

### Attachments

* `build/stac_report.json` (attach or excerpt)
* `env.txt` (pip freeze)
* Figures (PNG/SVG)
* Logs or console output helpful for reproducibility

```
