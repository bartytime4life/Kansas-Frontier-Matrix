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
- **Related issues/PRs**: Fixes #…, Relates #…

---

## 1) Objective / Hypothesis

**Question** — What are we trying to learn/compare?  
**Hypothesis** — What outcome do you expect and why?  
**Success criteria** — Decide up-front what “good” looks like (metrics, visuals, thresholds).

---

## 2) Datasets & Catalog

- **Inputs** (IDs / paths):  
  - STAC items/collections: `stac/items/<file>.json`, `stac/collections/<file>.json`  
  - Source descriptors: `data/sources/<file>.json`
- **Spatial/temporal bounds**: bbox, date range  
- **Licenses / provenance**: cite sources; note any restrictions

**Sanity checks**
```bash
# JSON & STAC validation (best-effort)
kgt validate-stac stac/items --report-json build/stac_report.json || true
````

---

## 3) Methods / Protocol (SOP)

* **Design** — controls, treatments, parameters to sweep
* **SOP links** — `mcp/sops/<doc>.md` (add/update if new)
* **Randomness** — seeds, sampling rules
* **Assumptions / constraints** — keep explicit

**Commands to reproduce (canonical)**

```bash
# minimal deterministic sequence; prefer Make targets
make <target>            # e.g., make fetch cogs terrain
make stac                # (re)generate catalog artifacts
make site                # update static viewer
```

---

## 4) Environment

* **Host**: local / CI / container
* **Image / Python**: `python -V` = …, Docker image = …
* **Hardware**: CPU/GPU, RAM
* **Key tool versions**: `rasterio`, `gdal`, `jinja2`, `jsonschema`, CLI `kgt --version`

```bash
python -V
pip freeze | sed -n '1,120p'   # capture top of env (attach full file below)
```

---

## 5) Variables & Configuration

* **Parameters** — list knobs/values (e.g., hillshade azimuth, Z-factor, resampling)
* **Config files edited** — paths + diffs if relevant
* **Hash snapshot(s)** (optional):

```bash
git rev-parse HEAD > build/git_sha.txt
sha256sum data/cogs/**/* 2>/dev/null | sort > build/artifact_hashes.txt
```

---

## 6) Results

**Metrics / counts** — summarize key numbers, tables, or JSON snippets.

**Visuals** — screenshots or link to Pages preview for layers/timeline.

**Qualitative observations** — artifacts, anomalies, alignment notes, uncertainty.

---

## 7) Analysis & Interpretation

* Did results meet success criteria? Why / why not?
* Threats to validity — sampling bias, georeferencing error, CRS mismatch, etc.
* Error bars / uncertainty — confidence & how shown in UI.

---

## 8) Artifacts

* **Generated files** (paths):

  * COGs / derivatives: `data/cogs/**/<file>.tif`
  * Metadata: `*.meta.json`, `checksum:sha256` filled in STAC assets
  * Reports: `build/stac_report.json`, `build/metrics.json`
* **Experiment folder** (optional; attach in PR):

  * `mcp/experiments/EXP-YYYYMMDD-<slug>/`

    * `README.md` (this report)
    * `commands.sh` (exact commands run)
    * `env.txt` (freeze)
    * `figures/` (PNGs)
    * `artifacts.jsonl` (paths, sizes, hashes)

---

## 9) Ethics / Privacy / Legal

* Sensitive locations generalized or withheld? ☐
* Licenses verified and attributions added? ☐
* Community/Indigenous data use reviewed if applicable? ☐

---

## 10) Roll-forward Plan

* Adopt / discard / iterate?
* **Follow-ups** (open issues to track):

  * [ ] …
  * [ ] …

---

## Checklists

**Before running**

* [ ] Sources & STAC entries exist and validate
* [ ] Make targets documented
* [ ] Seed(s) / randomness policy set (if applicable)

**Before merging**

* [ ] Results reproducible with the commands above
* [ ] STAC assets include `checksum:sha256` (COGs, derivatives)
* [ ] Pages/site updated if visuals changed
* [ ] SOP / docs updated (if workflow changed)

---

### Attachments

* `build/stac_report.json` (first 100 lines or attach file)
* `env.txt` (pip freeze)
* Screens / figures (PNG/SVG)
* Any logs useful for reproducing

```
```
