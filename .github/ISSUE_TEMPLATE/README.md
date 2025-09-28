# Issue Templates — Kansas-Frontier-Matrix

This folder contains **guided templates** for filing issues with strong
**reproducibility** and **data provenance** signals (MCP style).  
Templates ship with sensible defaults and auto-labels to speed up triage.

> Template visibility is configured in [`config.yml`](./config.yml).

---

## 📦 Available templates

- **[`bug_report.md`](./bug_report.md)** — Something broke in the site, data pipeline, AI reasoning, or docs.  
  **Auto-labels:** `bug`, `needs-triage`  
  **Includes:** env block, logs, STAC/DVC/LFS pointers, geospatial context.

- **[`data_addition.md`](./data_addition.md)** — Propose a new dataset (map/layer/catalog/docs).  
  **Auto-labels:** `data`, `enhancement`, `stac`, `catalog`  
  **Includes:** license/provenance, CRS/extent/time, STAC/Source stub, storage plan (DVC/LFS).

- **[`experiment_report.md`](./experiment_report.md)** — Plan and log a deterministic experiment (MCP).  
  **Auto-labels:** `mcp`, `reproducibility`, `experiment`  
  **Includes:** hypothesis, SOP/commands, env freeze, artifacts, success criteria.

> If you don’t see a fit, open a minimal **bug** or **data** issue and we’ll retag.

---

## 🏷️ Label taxonomy (quick reference)

Roadmap-managed labels live in **[`.github/roadmap/roadmap.yaml`](../roadmap/roadmap.yaml)**.  
Common areas:

`data`, `hydrology`, `paleoclimate`, `ai`, `uncertainty`, `ontology`,  
`storytelling`, `crowdsourcing`, `3d`, `api`, `architecture`, `reproducibility`, `mcp`, `education`

GitHub defaults like `bug`, `enhancement` are used by templates.  
If your repo does not have a label referenced by a template, add it to
[`labels.yml`](../labels.yml) (and sync) or create it once in the UI.

---

## 🔎 Triage workflow

1. **Intake** — new issues get auto-labels from the template.  
2. **Classify** — add **area** labels (e.g., `data`, `ai`, `architecture`) and **priority** (e.g., `priority:p1`).  
3. **Assign** — use [`CODEOWNERS`](../CODEOWNERS) or @-mention specialists.  
4. **Link** — set a milestone (Roadmap-managed) and reference PRs/issues (`Fixes #123`, `Relates #456`).  
5. **Verify** —  
   - Bugs: confirm **Steps to Reproduce**, attach logs, link site/CI runs.  
   - Data: verify **license/provenance**, **CRS/extent/time**, and a STAC draft.  
6. **Close** — only after reproduction & validation (**Make targets** or **CI**) are green.

---

## ♻️ Reproducibility expectations (all issues)

Please include whenever applicable:

- **Commands** you ran (prefer `make` targets), and a short **env** block:

```bash
python -V
gdalinfo --version || true
node -v || true; npm -v || true
````

* **Data provenance:** link **STAC items/collections** or **data/sources** descriptors.
* **Checks** (best-effort):

```bash
# STAC sanity
kgt validate-stac stac/items --no-strict || true

# JSON quick check
jq -e 'type=="object"' path/to/*.json
```

---

## ➕ Adding a new template

1. Create a file in this folder, e.g. `feature_request.md`.
2. Start with **YAML front-matter** (GitHub requires it):

```markdown
---
name: "✨ Feature Request"
about: "Propose a new capability for the KFM stack"
title: "[FEAT] <concise title>"
labels: ["enhancement"]
assignees: []
---
```

3. Keep prompts **actionable** and include:

   * Motivation / user story
   * Acceptance criteria
   * Risks / rollbacks
   * Repro commands or integration points (web config, STAC, Make targets)

> After adding labels referenced by a new template, update
> [`labels.yml`](../labels.yml) (and optionally [`roadmap.yaml`](../roadmap/roadmap.yaml))
> so automation can create/sync them consistently.

---

## 🤖 Automation cues

* **Roadmap sync** workflow may add/normalize labels & milestones.
* **CI runs**:

  * `site.yml` — build & deploy Pages
  * `stac-badges.yml` — catalog integrity/badges
  * `codeql.yml` — CodeQL security scans
  * *(optional)* `tests.yml` — pytest/docs when enabled

Keep issues aligned with these jobs for faster reviews.

---

## ✅ Tips for great issues

* **Concise title** + outcome-oriented summary.
* Bugs: **minimal, reliable, reproducible** steps.
* Data: **license first**, then CRS/extent/time; attach a **STAC or source stub**.
* Experiments: define **success criteria** up front.

```
```
