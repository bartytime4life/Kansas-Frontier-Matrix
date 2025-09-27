---
name: "🧪 Experiment Report"
about: "Plan, run, and log a reproducible experiment (MCP-grade)"
title: "[EXP] <concise title>"
labels: ["MCP", "reproducibility"]
assignees: []
---

> Fill this out when proposing **and** after completing an experiment. Keep it copy-paste runnable and deterministic.

## 0) Metadata

- **Experiment ID**: `EXP-YYYYMMDD-<slug>`
- **Owner(s)**: @you
- **Status**: ☐ Planned ☐ Running ☐ Completed ☐ Abandoned
- **Scope areas**: `data` | `stac` | `web` | `src` | `scripts` | `ci` | `docker`
- **Related issues/PRs**: Fixes #…, Closes #…, Relates #…
- **Milestone**: `m1-data` | `m2-analytics` | `m3-story` | `m4-tech` | `m5-mcp` (if applicable)

---

## 1) Objective / Hypothesis

**Question** — What are we trying to learn/compare?  
**Hypothesis** — What outcome do you expect and why?  
**Success criteria** — Define “good” up-front (metrics, visuals, thresholds).

---

## 2) Datasets & Catalog

- **Inputs (IDs / paths)**  
  - STAC: `stac/items/<file>.json`, `stac/collections/<file>.json`  
  - Source descriptors: `data/sources/<file>.json|yml`
- **Spatial/temporal bounds** — bbox, date range
- **Licenses / provenance** — cite sources; note restrictions

**Sanity checks**
```bash
# JSON & STAC validation (best-effort)
make stac-validate || true

# Optional: config pack validation for web UI
make config-validate || true
````

---

## 3) Methods / Protocol (SOP)

* **Design** — controls, treatments, parameters to sweep
* **SOP links** — `mcp/sops/<doc>.md` (add/update if new)
* **Randomness** — seeds, sampling rules
* **Assumptions / constraints** — be explicit

**Commands to reproduce (canonical)**

```bash
# Prefer Make targets for determinism
make fetch           # if new sources are referenced
make cogs            # build COGs
make terrain         # hillshade/slope/aspect (COGs)
make stac            # (re)generate STAC catalog artifacts
make site            # write fallback web/layers.json and mirror small vectors
make site-config     # render web/app.config.json from STAC (requires kgt)
```

---

## 4) Environment

* **Host** — local / CI / container
* **Image / Python** — `python -V` = …, Docker image = …
* **Hardware** — CPU/GPU, RAM
* **Key tools** — `rasterio`, `gdal`, `jinja2`, `jsonschema`, `kgt --version`

```bash
python -V
pip freeze | sed -n '1,120p'   # attach full freeze as file if long
```

---

## 5) Variables & Configuration

* **Parameters** — knobs/values (e.g., hillshade azimuth, Z-factor, resampling)
* **Config files edited** — paths + diffs if relevant
* **Hash snapshot(s)** (optional)

```bash
mkdir -p build
git rev-parse HEAD > build/git_sha.txt
# If large trees: guard errors to keep report generation flowing
(sha256sum data/cogs/**/* 2>/dev/null || true) | sort > build/artifact_hashes.txt
```

---

## 6) Results

* **Metrics / counts** — summarize key numbers, tables, or JSON snippets
* **Visuals** — screenshots or Pages preview link for layers/timeline
* **Qualitative observations** — artifacts, anomalies, alignment/CRS notes, uncertainty

---

## 7) Analysis & Interpretation

* Did results meet success criteria? Why / why not?
* Threats to validity — sampling bias, georeferencing error, CRS mismatch, etc.
* Error bars / uncertainty — confidence & how it’s shown in UI

---

## 8) Artifacts

* **Generated files (paths)**

  * COGs / derivatives: `data/cogs/**/<file>.tif`
  * Metadata: `*.meta.json` with `checksum:sha256` / `file:size` in STAC assets
  * Reports: `build/stac_report.json`, `build/metrics.json`

* **Experiment folder** (optional; commit in PR)

  ```
  mcp/experiments/EXP-YYYYMMDD-<slug>/
    README.md          # this report
    commands.sh        # exact commands run
    env.txt            # freeze
    figures/           # PNG/SVG
    artifacts.jsonl    # paths, sizes, hashes
  ```

---

## 9) Ethics / Privacy / Legal

* Sensitive locations generalized or withheld? ☐
* Licenses verified and attributions added? ☐
* Community/Indigenous data use reviewed if applicable? ☐

---

## 10) Roll-forward Plan

* Adopt / discard / iterate?
* **Follow-ups** (open issues to track)

  * [ ] …
  * [ ] …

---

## Checklists

**Before running**

* [ ] Sources & STAC entries exist and validate
* [ ] Make targets documented
* [ ] Seeds / randomness policy set (if applicable)

**Before merging**

* [ ] Results reproducible with the commands above
* [ ] STAC assets include `checksum:sha256` and `file:size` where applicable
* [ ] Pages/site updated if visuals changed (`make site` / `make site-config`)
* [ ] SOP / docs updated (if workflow changed)

---

### Attachments

* `build/stac_report.json` (attach file or first 100 lines)
* `env.txt` (pip freeze)
* Screens / figures (PNG/SVG)
* Logs helpful for reproducing

```
```
