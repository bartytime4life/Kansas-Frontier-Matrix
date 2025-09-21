---
name: "🔀 Pull Request"
about: Submit code/data/doc changes for review (MCP-grade reproducibility)
title: "[PR] <concise summary>"
assignees: ""
---

<!--
Quick tips:
- Keep the title actionable (“Add…”, “Fix…”, “Update…”).
- Reference issues with “Fixes #123” / “Closes #456”.
- Use labels from .github/roadmap/roadmap.yaml when helpful.
-->

## Summary

**What does this change do? Why now?**  
_A short, outcome-oriented description. Include context/links._

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

- **Area(s)**: `web` | `scripts` | `src` | `mcp` | `stac` | `data` | `ci`
- **Breaking change?** yes/no  
  _If yes, describe migration steps and update docs accordingly._
- **User-visible changes?** yes/no  
  _Screenshots / GIF preferred for UI._

---

## Details

### 1) Implementation notes
_Bullets: design choices, trade-offs, alternatives considered._

### 2) Data & Catalog (if adding/updating datasets)
- [ ] Added/updated **STAC** entries under `stac/items/**` and/or `stac/collections/**`
- [ ] Updated source descriptors in `data/sources/*.json` (if applicable)
- [ ] License/provenance verified and cited in collection/item metadata
- [ ] Storage plan chosen: **DVC** / **Git LFS** / small in-repo
- [ ] Checksums (`checksum:sha256`) filled for assets where applicable

**Paths/IDs**  
- STAC item/collection: `stac/items/<id>.json`, `stac/collections/<id>.json`  
- Source entry (if used): `data/sources/<file>.json`  
- DVC files: `*.dvc` (list)  
- LFS files: (list)

### 3) Reproducibility (MCP)
- [ ] Deterministic pipeline (documented commands / Make targets)
- [ ] Updated/added **SOP** in `mcp/sops/` (if new/changed workflow)
- [ ] Experiment log in `mcp/experiments/` (if model/analysis change)
- [ ] Model card updated in `mcp/model_cards/` (if ML involved)

**Commands to reproduce**
```bash
# minimal steps to regenerate outputs / site
make <target>  # e.g., make terrain && make stac && make site
