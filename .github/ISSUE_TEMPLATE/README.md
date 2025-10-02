<div align="center">

# 📝 Kansas-Frontier-Matrix — Issue Templates (`.github/ISSUE_TEMPLATE/`)

**Mission:** Provide **guided templates** for issues that enforce  
**reproducibility, provenance, and MCP-style rigor**.  

Templates auto-label and guide contributors so triage is fast,  
and artifacts always tie back to STAC, schemas, or Make targets.  

<!-- Core CI/CD -->
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../.github/workflows/tests.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../../.github/workflows/stac-badges.yml)  

<!-- Governance / Roadmap -->
[![Labels Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/labels.yml/badge.svg)](../../.github/workflows/labels.yml)  
[![PR Labeler](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pr-labeler.yml/badge.svg)](../../.github/workflows/pr-labeler.yml)  
[![Roadmap Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/roadmap.yml/badge.svg)](../../.github/workflows/roadmap.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../.github/workflows/automerge.yml)  

<!-- Security / Hygiene -->
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)  
[![Secret Scanning](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/secret-scanning.yml/badge.svg)](../../.github/workflows/secret-scanning.yml)  
[![OpenSSF Scorecard](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ossf-scorecard.yml/badge.svg)](../../.github/workflows/ossf-scorecard.yml)  

<!-- Repo Info -->
![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)  
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  

</div>

---

## 📦 Templates Provided

- **[`bug_report.md`](./bug_report.md)** — broken site, pipeline, AI reasoning, or docs  
  _Labels:_ `bug`, `needs-triage` · _Includes:_ env/logs, STAC refs, reproducible steps  

- **[`data_addition.md`](./data_addition.md)** — propose new dataset (map/layer/docs)  
  _Labels:_ `data`, `enhancement`, `stac`, `catalog` · _Includes:_ license, CRS/extent/time, source stub, LFS plan  

- **[`experiment_report.md`](./experiment_report.md)** — deterministic MCP experiment log  
  _Labels:_ `mcp`, `experiment`, `reproducibility` · _Includes:_ hypothesis, SOP/commands, env freeze, artifacts  

Configured by [`config.yml`](./config.yml). If none fit, open a minimal **bug** or **data** issue.

---

## 🏷️ Labels & Taxonomy

- **Default:** `bug`, `enhancement`, `needs-triage`  
- **Domain labels:** `data`, `hydrology`, `ai`, `ontology`, `uncertainty`, `education`, …  
- **Roadmap-managed:** defined in [`.github/roadmap/roadmap.yaml`](../roadmap/roadmap.yaml)  
- **Sync:** if missing, add to [`labels.yml`](../labels.yml) (or create once in the UI)  

---

## 🔎 Triage Workflow

```mermaid
flowchart TD
  A["New issue\n(template chosen)"] --> B["Auto-label\nfrom template"]
  B --> C["Classification\nadd domain + priority labels"]
  C --> D["Assignment\nCODEOWNERS / @-mentions"]
  D --> E["Linkage\nmilestones + related PRs/issues"]
  E --> F["Verification\nSTAC refs · repro steps · CI links"]
  F --> G["Closure\nonly after validation passes"]
````

<!-- END OF MERMAID -->

---

## 🔖 Label Lifecycle

```mermaid
flowchart LR
  L0["Template labels\n(bug, data, mcp, …)"] --> L1["Roadmap sync\nlabels.yml / roadmap.yaml"]
  L1 --> L2["Triage labeling\n(domain, priority:p1–p3)"]
  L2 --> L3["Milestone\nroadmap stage"]
  L3 --> L4["Automation\nbadges · reports"]
  L4 --> L5["Resolution\nclose"]
  L5 --> L6["Metrics\ncoverage · velocity"]
```

<!-- END OF MERMAID -->

---

## 📑 Example: `labels.yml`

```yaml
# .github/labels.yml
- name: bug
  color: d73a4a
  description: Something isn’t working
- name: data
  color: 1d76db
  description: Data ingestion, sources, or STAC-related
- name: mcp
  color: fbca04
  description: Master Coder Protocol experiment or reproducibility task
- name: reproducibility
  color: 0e8a16
  description: Requires or enforces reproducibility checks
- name: hydrology
  color: 5319e7
  description: Hydrology / river / watershed datasets
- name: priority:p1
  color: b60205
  description: Highest priority / blocking
```

Automation (`scripts/sync-labels.js`) ensures labels stay consistent.

---

## 📑 Example: `roadmap.yaml`

```yaml
# .github/roadmap/roadmap.yaml
milestones:
  - title: "M1: Basemaps & DEM"
    description: "Foundational elevation + terrain COGs, STAC wiring, site baseline."
    labels: ["data", "dem", "stac"]
  - title: "M2: Hydrology"
    description: "Kansas River + watersheds, flood history, linked events."
    labels: ["hydrology", "uncertainty"]
  - title: "M3: Treaties & Land"
    description: "Boundary polygons, cessions, reservations, STAC integration."
    labels: ["data", "treaties", "storytelling"]
  - title: "M4: Hazards & Climate"
    description: "Tornadoes, droughts, paleoclimate; linked to settlement events."
    labels: ["hazards", "climate", "mcp"]
```

Roadmap milestones auto-assign issues and structure project phases.

---

## ♻️ Reproducibility Expectations

Always include:

```bash
# Env block
python -V
gdalinfo --version || true
node -v || true; npm -v || true
```

* **Provenance:** link STAC items/collections or `data/sources/*.json`
* **Checks (best effort):**

```bash
# STAC validation
kgt validate-stac stac/items --no-strict || true

# JSON quick check
jq -e 'type=="object"' path/to/*.json
```

---

## ✅ Good Practice

* Concise title + outcome-oriented summary
* **Bugs** → minimal, reliable, reproducible steps
* **Data** → license first, then CRS/extent/time + STAC stub
* **Experiments** → define success criteria up front

---

## ✅ Summary

`.github/ISSUE_TEMPLATE/` ensures all issues are **MCP-grade** — reproducible, provenance-linked, and triage-ready.
Labels and milestones are synchronized via `labels.yml` + `roadmap.yaml`, closing the loop between templates, automation, and roadmap governance.
