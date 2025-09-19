---
name: "🔀 Pull Request"
about: Submit code/data/doc changes for review (MCP-grade reproducibility)
title: "[PR] <concise summary>"
assignees: ""
---

## Summary

**What does this change do? Why now?**  
_A short, outcome-oriented description. Reference issues with `Fixes #123` / `Closes #456` when applicable._

---

## Type of change

- [ ] Feature (new capability)
- [ ] Fix (bug fix / regression)
- [ ] Data (new layer/catalog entry, data update)
- [ ] Docs (README, SOPs, model cards, glossary)
- [ ] Build/CI (workflows, tooling, pre-commit)
- [ ] Refactor (no functional change)
- [ ] Performance
- [ ] Chore / housekeeping

---

## Scope & Impact

- **Area(s)**: `web` | `scripts` | `src` | `mcp` | `data` | `ci`
- **Breaking change?** yes/no  
  _If yes, describe migration steps and update docs accordingly._
- **User-visible changes?** yes/no  
  _Screenshots / GIF preferred for UI._

---

## Details

### 1) Implementation notes
_Bullets: design choices, tradeoffs, alternatives considered._

### 2) Data & Catalog (if adding/updating datasets)
- [ ] Added/updated STAC or `data/sources/*.json` entries
- [ ] License/provenance verified and cited
- [ ] Storage plan: `DVC` / `Git LFS` / small in-repo
- [ ] Checksums (md5/sha256) recorded (if applicable)

**Paths/IDs**  
- STAC item/collection: `data/stac/<id>.json`  
- Source entry: `data/sources/<file>.json`  
- DVC files: `*.dvc` (list)  
- LFS files: (list)

### 3) Reproducibility (MCP)
- [ ] Deterministic pipeline (documented commands / Make targets)
- [ ] Updated or added **SOP** in `mcp/sops/` (if new/changed workflow)
- [ ] Experiment log in `mcp/experiments/` (if model/analysis change)
- [ ] Model card updated in `mcp/model_cards/` (if ML involved)

**Commands to reproduce**  
```bash
# minimal steps to regenerate outputs / site
make <target>  # e.g., make terrain && make site
````

### 4) Validation / QA

* [ ] JSON (catalog) passes `jq` validation
* [ ] CRS/extent/attrs validated for geodata
* [ ] Visual spot-check (QGIS / Pages preview)
* [ ] Unit/integration tests (if present) pass

**Evidence**

* Screenshots / links to Pages preview or QGIS snapshots
* Notable diffs (e.g., layer opacity/style, timeline placement)

### 5) Security / Privacy / Ethics

* [ ] No secrets / tokens committed
* [ ] Sensitive locations (protected/sacred) generalized or withheld
* [ ] Licenses respected, attributions added where required

---

## CI

Link to runs (if applicable):

* Pages/site: …
* Lint/format: …
* Tests: …

---

## Checklist (maintainer & author)

* [ ] Code formatted & linted (pre-commit clean)
* [ ] `.editorconfig` / `.gitattributes` / `.gitignore` respected
* [ ] Large binaries are DVC/LFS (not plain Git)
* [ ] Docs updated (README, architecture, or usage notes)
* [ ] Attribution text surfaced in UI (layer legend/metadata)
* [ ] Reviewers added with relevant domain expertise

---

## Additional notes

*Anything else reviewers should know (rollout plan, follow-ups, tech debt tickets, deprecation notices).*

```
