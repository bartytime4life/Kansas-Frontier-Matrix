<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TBD-CHANGELOG-UUID
title: Changelog
type: standard
version: v1
status: draft
owners: TBD — verify from .github/CODEOWNERS
created: 2026-03-14
updated: 2026-03-14
policy_label: TBD
related: [README.md, CONTRIBUTING.md, SECURITY.md, .github/CODEOWNERS]
tags: [kfm, changelog, release-notes, governance]
notes: [Proposed root changelog draft; verify owner mapping, historical release history, and final policy label before commit.]
[/KFM_META_BLOCK_V2] -->

# Changelog

Repository-level record of notable, behavior-significant changes to Kansas Frontier Matrix.

> [!IMPORTANT]
> This file is intentionally conservative.
> It does **not** backfill historical releases from memory, architecture manuals, or inferred repo state.
> Add older entries only from verified tags, release manifests, proof packs, merged pull requests, correction notices, or equivalent repository evidence.

**Path:** `CHANGELOG.md`  
**Companion docs:** [`README.md`](README.md) · [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`SECURITY.md`](SECURITY.md) · [`.github/CODEOWNERS`](.github/CODEOWNERS)

## Quick jump

[Format](#format) · [Unreleased](#unreleased) · [Historical backfill needed](#historical-backfill-needed)

## Format

This changelog tracks **repository-level** changes that materially affect one or more of the following:

- public behavior
- contracts or schemas
- governed delivery and promotion
- security posture
- data lifecycle or publication rules
- review, verification, or correction workflows
- contributor-facing documentation that changes behavior

Use the newest release first.

| Section | Use for |
|---|---|
| **Added** | New capabilities, lanes, artifacts, or governed workflows |
| **Changed** | Behavior changes, contract updates, workflow shifts, or release-process changes |
| **Fixed** | Corrected defects, regressions, invalid examples, broken links, or repair work |
| **Security** | Vulnerability fixes, hardening, auth/policy changes, or exposure reductions |
| **Docs** | Behavior-significant documentation changes |
| **Governance** | Review gates, rights/sensitivity handling, ownership changes, or policy updates |
| **Data** | New governed datasets, promotion events, corrections, supersessions, or publication-state changes |
| **Verification** | New tests, proof-pack rules, release checks, rollback drills, or restore drills |
| **Deprecated** | Still available, but scheduled for replacement or removal |
| **Removed** | Deleted or retired behavior, interfaces, artifacts, or flows |

### Entry rules

1. Record only **notable** changes.
2. Prefer entries that point to a verifiable release unit: tag, manifest, proof pack, PR, correction notice, or dataset promotion artifact.
3. Do **not** log speculative roadmap items as released changes.
4. When a change affects trust posture, policy, evidence resolution, or public interpretation, say so explicitly.
5. When a change is domain-specific but user-visible, keep the summary here and link outward to the deeper artifact or document.

<details>
<summary><strong>Entry template</strong></summary>

```md
## YYYY-MM-DD — <release-id>

### Added
- ...

### Changed
- ...

### Fixed
- ...

### Security
- ...

### Docs
- ...

### Governance
- ...

### Data
- ...

### Verification
- ...

### Deprecated
- ...

### Removed
- ...

**Evidence:** <tag / PR / manifest / proof pack / correction notice>
```

</details>

## Unreleased

_No verified unreleased entries recorded yet._

## Historical backfill needed

Historical release entries should be reconstructed only from repository evidence strong enough to survive review.

| Evidence source | What it should prove |
|---|---|
| Git tag or release record | Release identifier and release date |
| Release manifest or proof pack | Exact artifact scope, digests, and promotion state |
| Merged PR or reviewed change set | Human-readable summary of what changed |
| Schema or contract diff | Interface or metadata breaking/non-breaking status |
| Correction notice or supersession record | Whether prior behavior was withdrawn, corrected, generalized, or replaced |
| Dataset promotion artifacts | Publication-ready data changes that belong in the root changelog |

Until that backfill is complete, older releases should remain absent rather than guessed.

## Maintainer note

When a change ships, update this file in the same governed review stream as the code, contracts, workflows, or docs it describes.