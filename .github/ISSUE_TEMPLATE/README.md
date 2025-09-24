# Issue Templates — Kansas-Frontier-Matrix

This folder contains **guided templates** for filing issues with strong
**reproducibility** and **data provenance** signals (MCP style).

Templates ship with sensible defaults and auto-labels to speed up triage.

---

## Available templates

- **`bug_report.md`** — Something broke in the site, data pipeline, AI reasoning, or docs.  
  Auto-labels: `bug`  
  Includes: env block, logs, STAC/DVC/LFS pointers, geospatial context.

- **`data_addition.md`** — Propose a new dataset (map/layer/catalog/docs).  
  Auto-labels: `data`, `enhancement`  
  Includes: license/provenance, CRS/extent/time, STAC/Source stub, storage plan (DVC/LFS).

- **`experiment_report.md`** — Plan and log a deterministic experiment (MCP).  
  Auto-labels: `MCP`, `reproducibility`  
  Includes: hypothesis, SOP/commands, env freeze, artifacts, success criteria.

> If you don’t see a fit, open a minimal **bug** or **data** issue and we’ll retag.

---

## Label taxonomy (quick reference)

Roadmap-managed labels live in [`.github/roadmap/roadmap.yaml`](../roadmap/roadmap.yaml).  
Common areas:

`data`, `hydrology`, `paleoclimate`, `ai`, `uncertainty`, `ontology`, `fractals`,  
`storytelling`, `crowdsourcing`, `3d`, `api`, `architecture`, `reproducibility`, `MCP`, `education`

GitHub defaults like `bug`, `enhancement` are used by templates; if your repo
doesn’t have them, add via the roadmap file or create once in the UI.

---

## Triage workflow

1. **Intake**  
   New issues get auto-labels from the template.

2. **Classify**  
   Add **area** labels (e.g., `data`, `ai`, `architecture`) and **priority** if used
   (e.g., `priority:p1` via the roadmap).

3. **Assign**  
   Use [CODEOWNERS](../CODEOWNERS) to find a default owner, or @-mention specialists.

4. **Link**  
   - If the work maps to a milestone, set it (see the Roadmap sync).  
   - Reference related PRs and issues: `Fixes #123`, `Relates #456`.

5. **Verify**  
   For bugs: confirm **Steps to Reproduce**, attach logs, and check site/CI links.  
   For data additions: check **license/provenance**, **CRS/extent/time**, and STAC draft.

6. **Close**  
   Close only after reproduction & validation (**make** commands or CI run) are green.

---

## Reproducibility expectations (all issues)

Please include whenever applicable:

- **Commands** you ran (prefer `make` targets), and a short **env** block:
  ```bash
  python -V
  gdalinfo --version || true
  node -v || true; npm -v || true
````

* **Data provenance**: link **STAC items/collections** or **data/sources** descriptors.
* **Checks** (best-effort):

  ```bash
  # STAC sanity
  kgt validate-stac stac/items --no-strict || true

  # JSON quick check
  jq -e 'type=="object"' path/to/*.json
  ```

---

## Adding a new template

1. Create a file in this folder, e.g. `feature_request.md`.
2. Start with **YAML front-matter** (GitHub requires it):

   ```markdown
   ---
   name: "✨ Feature request"
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

> After adding labels referenced by a new template, consider updating
> [`roadmap.yaml`](../roadmap/roadmap.yaml) so the sync job can create them consistently.

---

## Tips for great issues

* **Concise title** + outcome-oriented summary.
* For bugs: **minimal, reliable, reproducible** steps.
* For data: **license first**, then CRS/extent/time; attach a **STAC or source stub**.
* For experiments: define **success criteria up front**.

---

## Automation cues

* Roadmap sync (`roadmap.yml`) may add or normalize labels/milestones.
* CI runs:

  * `stac-validate.yml` for catalog integrity
  * `tests.yml` for pytest suite (including web config schemas)
  * `site.yml` for Pages deploy after checks pass

Keep issues aligned with these jobs for faster reviews.

---

```
```
