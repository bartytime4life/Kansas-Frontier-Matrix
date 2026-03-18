<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TBD-CHANGELOG-UUID
title: Changelog
type: standard
version: v1
status: draft
owners: TBD — verify from .github/CODEOWNERS
created: 2026-03-14
updated: 2026-03-18
policy_label: TBD — verify
related: [README.md, CONTRIBUTING.md, SECURITY.md, .github/CODEOWNERS]
tags: [kfm, changelog, release-notes, governance]
notes: [Revised from the user-supplied root changelog baseline; owner mapping, related paths, policy label, and historical release inventory remain unverified in the current-session PDF-only workspace.]
[/KFM_META_BLOCK_V2] -->

# Changelog

Repository-level record of notable, behavior-significant changes to Kansas Frontier Matrix.

> [!IMPORTANT]
> This file is intentionally conservative.
> It does **not** backfill historical releases from memory, architecture manuals, or inferred repo state.
> Add older entries only from verified tags, release manifests, proof packs, merged pull requests, correction notices, or equivalent repository evidence.

| Field | Value |
|---|---|
| **Target path** | `CHANGELOG.md` |
| **Status** | Draft |
| **Owners** | `TBD — verify from .github/CODEOWNERS` |
| **Current evidence posture** | Current-session revision work was constrained by a PDF-only mounted workspace; repository history, tags, CODEOWNERS, workflows, and release artifacts were **not** directly inspected here. |
| **Related repo docs** | Expected, not current-session verified: `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `.github/CODEOWNERS` |

## Quick jump

[Scope](#scope) · [Format](#format) · [Unreleased](#unreleased) · [Historical backfill needed](#historical-backfill-needed) · [Entry authoring gate](#entry-authoring-gate)

## Scope

This changelog records **repository-level** changes that materially affect KFM behavior, trust posture, contract surface, governed delivery, correction behavior, or contributor-facing operating truth.

### Include here

- public or maintainer-visible behavior changes
- contract, schema, API, envelope, or policy changes
- governed delivery, promotion, rollback, correction, or verification changes
- security changes that alter exposure, auth, release integrity, or runtime trust behavior
- dataset or publication changes that materially affect visible scope, freshness, drill-through, or correction state
- documentation or runbook changes that change behavior, review posture, release obligations, or operator procedure

### Keep elsewhere

- speculative roadmap items
- unverified implementation guesses
- local scratch notes and temporary investigation detail
- domain-deep technical analysis that belongs in a lane-specific document, proof pack, ADR, runbook, or correction memo
- historical release entries reconstructed without auditable evidence

## Format

Use the **newest release first**.

Each entry should describe the smallest useful release unit or correction unit that a reviewer can verify later: tag, release manifest, proof pack, merged PR, correction notice, dataset promotion artifact, or equivalent governed record.

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

### Per-entry minimum

| Field | Expectation |
|---|---|
| **Heading** | `YYYY-MM-DD — <release-id>` or another unambiguous, reviewable identifier |
| **Summary** | One or two lines that say what changed and why it matters |
| **Sections used** | Only the sections that actually apply |
| **Evidence line** | Tag, manifest, proof pack, PR, correction notice, release artifact, or equivalent |
| **Trust note** | Required when the change affects policy, evidence resolution, rights/sensitivity, runtime outcomes, or public interpretation |

### Entry rules

1. Record only **notable** changes.
2. Prefer entries that point to a verifiable release unit: tag, manifest, proof pack, PR, correction notice, or dataset promotion artifact.
3. Do **not** log speculative roadmap items as released changes.
4. When a change affects trust posture, policy, evidence resolution, public interpretation, or correction behavior, say so explicitly.
5. When a change is domain-specific but user-visible, keep the summary here and link outward to the deeper artifact or document.
6. If the evidence is incomplete, leave the entry out rather than smoothing uncertainty into history.

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

**Evidence:** <tag / release manifest / proof pack / PR / correction notice / promotion artifact>
```

</details>

## Unreleased

_No verified unreleased entries recorded yet._

## Historical backfill needed

Historical release entries should be reconstructed only from repository evidence strong enough to survive review.

| Evidence source | What it should prove |
|---|---|
| Git tag or release record | Release identifier and release date |
| Release manifest or proof pack | Exact artifact scope, digests, promotion state, and release truth |
| Merged PR or reviewed change set | Human-readable summary of what changed |
| Schema or contract diff | Interface or metadata breaking/non-breaking status |
| Correction notice or supersession record | Whether prior behavior was withdrawn, corrected, generalized, superseded, or replaced |
| Dataset promotion artifacts | Publication-ready data changes that belong in the root changelog |
| Runbook / operational correction record | Whether rollback, restore, or correction materially changed operator truth |

Until that backfill is complete, older releases should remain absent rather than guessed.

## Entry authoring gate

Before merging a new entry, confirm the following:

- [ ] The entry is tied to a reviewable evidence unit.
- [ ] The change is behavior-significant at repository level.
- [ ] Trust, policy, release, or correction impact is named where relevant.
- [ ] Contracts, examples, diagrams, runbooks, and related docs were updated or intentionally left unchanged with explanation.
- [ ] The entry does not imply repo state or release history that has not been verified.
- [ ] Older history was added only from auditable repository evidence.

## Maintainer note

Update this file in the same governed review stream as the code, contracts, workflows, policies, schemas, or docs it describes.

A release is not fully documented until the changelog, supporting release evidence, and any required correction or rollback notes agree with one another.
