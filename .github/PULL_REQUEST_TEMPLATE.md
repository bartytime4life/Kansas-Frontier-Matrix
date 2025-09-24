<!--
Title: [PR] <concise summary>
Tips: Keep it actionable (“Add…”, “Fix…”, “Update…”). Reference issues: Fixes #123 / Closes #456.
Labels: Use ones defined in .github/roadmap/roadmap.yaml when helpful.
-->

## Summary
**What does this change do, and why now?**  
_Context + links. Keep it outcome-oriented._

---

## Type of change
- [ ] Feature (new capability)
- [ ] Fix (bug / regression)
- [ ] Data (new layer/catalog entry, data update)
- [ ] Docs (README, SOPs, model cards, glossary)
- [ ] Build/CI (workflows, tooling, pre-commit)
- [ ] Refactor (no functional change)
- [ ] Performance
- [ ] Chore / housekeeping

---

## Scope & Impact
- **Area(s)**: `web` | `scripts` | `src` | `stac` | `data` | `ci` | `docs`  
- **Breaking change?** yes/no  
  _If **yes**: describe migration steps & update docs._
- **User-visible?** yes/no  
  _Attach screenshots/GIFs for UI changes._

---

## Validation (what you ran)
- [ ] `pytest -q` green locally
- [ ] Web config schemas pass (`web/app.config.json`, `web/layers.json`)
- [ ] STAC validation green (items/collections)
- [ ] Site builds locally (`make site` or web build)
- [ ] Link check (lychee) no critical failures
- [ ] JSON/YAML parse clean for `stac/**` and `data/sources/**`
- [ ] (optional) Docker image builds locally
- [ ] Docs render (MkDocs) if changed

**Commands to reproduce**
```bash
# minimal steps to regenerate outputs / site
make prebuild        # if present
make stac-validate   # optional but recommended
make tiles           # optional: terrain tiles (hillshade/slope/aspect)
make site
````

---

## Data & Catalog (if adding/updating datasets)

* [ ] Added/updated **STAC** under `stac/items/**` and/or `stac/collections/**`
* [ ] Updated source descriptors in `data/sources/*.json|yml` (if applicable)
* [ ] License/provenance verified and cited in collection/item metadata
* [ ] Storage plan chosen: **DVC** / **Git LFS** / small in-repo
* [ ] Checksums (`checksum:multihash` or `file:size`) present where applicable

**Paths/IDs**

* STAC: `stac/items/<id>.json`, `stac/collections/<id>.json`
* Sources: `data/sources/<file>.json|yml`
* DVC/LFS: list any tracked files

---

## Reproducibility (MCP)

* [ ] Deterministic pipeline (documented commands / Make targets)
* [ ] Updated/added **SOP** in `mcp/sops/` (if workflow changed)
* [ ] Experiment log in `mcp/experiments/` (if model/analysis)
* [ ] Model card in `mcp/model_cards/` (if ML involved)

---

## Risks & Rollback

* **Risks:** *briefly list*
* **Rollback:** *how to revert/disable if needed (e.g., `git revert`, toggle layer in config)*

---

## Reviewer Notes

*Context for reviewers: areas to focus on, known trade-offs, follow-ups slated for a next PR.*

```

**What changed**
- Removed unsupported YAML front-matter (prevents it from showing up in PR body).
- Added explicit **Validation** & **Schema/STAC** checklists to match your CI (tests, web-config-validate, stac-validate, site).
- Included **repro commands**, **risk/rollback**, and **MCP** reproducibility hooks.
```
