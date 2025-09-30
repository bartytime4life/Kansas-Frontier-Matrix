<div align="center">

# 📝 Kansas-Frontier-Matrix — Issue Templates (`.github/ISSUE_TEMPLATE/`)

**Mission:** Provide **guided templates** for issues that enforce  
**reproducibility, provenance, and MCP-style rigor**.  

Templates auto-label and guide contributors so triage is fast,  
and artifacts always tie back to STAC, schemas, or Make targets.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../../.github/workflows/stac-badges.yml)

</div>

---

## 📦 Templates Provided

- **[`bug_report.md`](./bug_report.md)** — broken site, pipeline, AI reasoning, or docs  
  _Labels:_ `bug`, `needs-triage` · _Includes:_ env/logs, STAC refs, reproducible steps  

- **[`data_addition.md`](./data_addition.md)** — propose new dataset (map/layer/docs)  
  _Labels:_ `data`, `enhancement`, `stac`, `catalog` · _Includes:_ license, CRS/extent/time, source stub, LFS plan  

- **[`experiment_report.md`](./experiment_report.md)** — deterministic MCP experiment log  
  _Labels:_ `mcp`, `experiment`, `reproducibility` · _Includes:_ hypothesis, SOP/commands, env freeze, artifacts  

> Configured by [`config.yml`](./config.yml). If none fit, open a minimal **bug** or **data** issue.

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
  E --> F["Verification\n(STAC refs, repro steps, CI links)"]
  F --> G["Closure\nonly after validation passes"]

<!-- END OF MERMAID -->



⸻

🔖 Label Lifecycle

flowchart LR
  L0["Template labels\n(bug, data, mcp, …)"] --> L1["Roadmap sync\n(labels.yml / roadmap.yaml)"]
  L1 --> L2["Triage labeling\n(domain, priority:p1–p3)"]
  L2 --> L3["Milestone\n(roadmap stage)"]
  L3 --> L4["Automation\n(badges, reports)"]
  L4 --> L5["Resolution\n(close)"]
  L5 --> L6["Metrics\n(review coverage & velocity)"]

<!-- END OF MERMAID -->



⸻

📑 Example: labels.yml

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

This file allows automation or scripts (scripts/sync-labels.js) to create/sync labels consistently.

⸻

📑 Example: roadmap.yaml

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

This roadmap drives milestone auto-assignment and helps organize project phases.

⸻

♻️ Reproducibility Expectations

Always include:

# Env block
python -V
gdalinfo --version || true
node -v || true; npm -v || true

	•	Provenance: link STAC items/collections or data/sources/*.json
	•	Checks (best effort):

# STAC validation
kgt validate-stac stac/items --no-strict || true

# JSON quick check
jq -e 'type=="object"' path/to/*.json


⸻

✅ Good Practice
	•	Concise title + outcome-oriented summary
	•	Bugs → minimal, reliable, reproducible steps
	•	Data → license first, then CRS/extent/time + STAC stub
	•	Experiments → define success criteria up front

⸻

✅ Summary:
.github/ISSUE_TEMPLATE/ ensures all issues are MCP-grade — reproducible, provenance-linked, and triage-ready.
Labels and milestones are synchronized via labels.yml + roadmap.yaml, closing the loop between templates, automation, and roadmap governance.