<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/0c122f14-7b08-4303-be70-b2e9594f59f4
title: KFM Changelog
type: standard
version: v1
status: draft
owners: TBD
created: 2026-03-04
updated: 2026-03-04
policy_label: public
related: []
tags: [kfm, changelog]
notes:
  - "Bootstrapped changelog scaffold. Populate entries from PRs/commits and release tags."
[/KFM_META_BLOCK_V2] -->

# Changelog
Track notable changes to the Kansas Frontier Matrix (KFM) repository.

> **Evidence discipline**: Every meaningful bullet is tagged **CONFIRMED**, **PROPOSED**, or **UNKNOWN**.
> - **Released sections MUST be CONFIRMED** (and include a PR/commit reference).
> - **Unreleased may include PROPOSED/UNKNOWN** while work is in-flight.

## How to use this file

### When to add an entry
Add a bullet under **[Unreleased]** when a change is merged (or when a change is planned but not yet merged).

### When to cut a release
1. Pick a release identifier (tag) and a release date.
2. Move applicable **CONFIRMED** bullets from **[Unreleased]** into a new dated release section.
3. Ensure each bullet has *at minimum*:
   - **Area** (one of: `governance`, `policy`, `data`, `catalog`, `pipeline`, `graph`, `api`, `ui`, `focus`, `infra`, `docs`)
   - **Evidence** (PR number and/or commit hash)
   - **Risk** (`low|medium|high`) and (if `medium|high`) a short rollback note

### Recommended bullet format

```
- [CONFIRMED][area] <what changed> (PR #123) (risk: low)
- [CONFIRMED][data] Promoted dataset <dataset_id> RAW→WORK (run: <run_id>) (PR #123) (risk: medium; rollback: revert catalog + invalidate promotion)
- [PROPOSED][policy] <policy intent> (owner: @handle) (target: 2026-03-XX)
- [UNKNOWN][api] <suspected change> (needs: link to PR/commit + test evidence)
```

### Notes
- This changelog is **not** a substitute for dataset-level provenance.
  - Dataset promotions must be evidenced via catalogs (e.g., DCAT/STAC/PROV) and run records.
- Prefer small, additive entries. If a change is large, break it into multiple bullets with clear scope.

---

## [Unreleased]

### Added
- [PROPOSED][docs] Add `docs/CHANGELOG.md` scaffold with evidence-tag conventions (this file). (risk: low)

### Changed

### Deprecated

### Removed

### Fixed

### Security

### Governance / Policy

---

## Release history

> Add new release sections **above** this line. Keep newest releases at the top.
