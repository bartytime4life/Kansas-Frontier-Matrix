# `scripts/one_off/` — One-Off Script Holding Lane

Temporary, ticket-bound scripts for narrowly scoped repo work; delete after use or promote to the correct governed home if the behavior becomes repeatable or trust-bearing.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-one-off-readme
title: scripts/one_off/README.md — One-Off Script Holding Lane
type: readme; directory-readme; one-off-script-guardrail
version: v0.1
status: draft; greenfield-stub-expanded; no-direct-one-off-scripts-found; NEEDS VERIFICATION
owners: OWNER_TBD — Developer tooling steward · QA steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; one-off-scripts; temporary; no-production-authority
tags: [kfm, scripts, one-off, temporary, cleanup, guardrail, no-production-authority]
related:
  - ../README.md
  - ../dev/README.md
  - ../maintenance/README.md
  - ../../tools/README.md
  - ../../tests/
  - ../../tools/validators/
  - ../../pipelines/
  - ../../packages/
  - ../../data/
  - ../../release/
notes:
  - "Expanded from a greenfield stub at scripts/one_off/README.md."
  - "Current-session search found no direct one-off scripts under this path beyond the README."
  - "This README defines a deletion-first guardrail; it does not prove any one-off workflow, script readiness, CI wiring, or release authority."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: scripts/one_off" src="https://img.shields.io/badge/root-scripts%2Fone__off-blue">
  <img alt="Authority: temporary helpers" src="https://img.shields.io/badge/authority-temporary__helpers-purple">
  <img alt="Maturity: no scripts confirmed" src="https://img.shields.io/badge/maturity-no__scripts__confirmed-orange">
  <img alt="Boundary: delete or promote" src="https://img.shields.io/badge/rule-delete__or__promote-critical">
</p>

**Status:** draft / temporary one-off lane  
**Path:** `scripts/one_off/`  
**Current scripts:** none confirmed in current search  
**Truth posture:** CONFIRMED path and README; CONFIRMED no direct one-off scripts found by current repository search; NEEDS VERIFICATION for future script inventory, owner, ticket linkage, deletion status, and promotion decisions.

## Quick jumps

[Purpose](#purpose) · [Boundary](#boundary) · [Current inventory](#current-inventory) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Use pattern](#use-pattern) · [Delete or promote](#delete-or-promote) · [Validation](#validation) · [Open questions](#open-questions)

---

## Purpose

`scripts/one_off/` is the temporary holding lane for narrowly scoped scripts that exist to perform a specific, reviewed, usually non-recurring repository task.

The parent `scripts/README.md` states that `scripts/` is for small operational scripts and that long-lived trust-bearing scripts graduate to `tools/`, `pipelines/`, or `packages/`. This child lane makes the temporary end of that rule explicit: one-off scripts should have a reason, a scope, a cleanup plan, and a clear non-authority boundary.

## Boundary

This folder is not production tooling, validator authority, pipeline orchestration, package code, fixture authority, policy authority, data lifecycle storage, proof authority, receipt authority, release authority, or CI proof by itself.

A one-off script must not become the normal path for ingest, validation, publication, evidence resolution, release, correction, rollback, or public-client behavior. If it becomes repeatable, important, trust-bearing, CI-invoked, or depended on by maintainers, it should leave this lane.

> [!CAUTION]
> One-off scripts are high drift risk. Any script that mutates data, fixtures, registries, schemas, contracts, policy, release records, or generated outputs needs an explicit dry-run mode, review notes, rollback instructions, and a decision on deletion or promotion.

## Current inventory

| File | Current status | Notes |
|---|---|---|
| `README.md` | present | This directory guardrail. |
| `scripts/one_off/*` | no direct scripts found in current search | Future scripts must be ticket-bound, temporary, and deletion- or promotion-tracked. |

## Repo fit

```text
scripts/
├── README.md                         # parent script-root guidance
├── dev/                              # local developer helpers
├── maintenance/                      # bounded maintenance CLIs and wrappers
└── one_off/
    └── README.md                     # this file; temporary one-off guardrail

tools/                                # long-lived trust-bearing validators/builders/generators
pipelines/                            # executable pipeline orchestration
packages/                             # reusable implementation libraries
fixtures/                             # valid/invalid/golden/negative examples
tests/                                # executable tests and proof of behavior
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted artifacts
release/                              # release, correction, rollback authority
```

## What belongs here

- Temporary scripts tied to a single issue, migration, audit, cleanup, or repo-maintenance task.
- Scripts with explicit scope, owner, expected inputs, expected outputs, and deletion date or promotion trigger.
- Dry-run-first helpers that produce reviewable diffs before writing.
- Non-authoritative scripts that do not become fixture, schema, policy, data, proof, receipt, or release authority.
- Short-lived wrappers around already-accepted commands when a one-time composition is useful.

## What does not belong here

| Do not put this in `scripts/one_off/` | Correct home |
|---|---|
| Long-lived validators, generators, builders, proof-pack tools, release tools, or QA tools | `tools/` |
| Pipeline orchestration or repeatable production flow | `pipelines/` |
| Reusable libraries imported by multiple systems | `packages/` |
| Local setup helpers used repeatedly by developers | `scripts/dev/` |
| Bounded maintenance CLIs used repeatedly by operators or CI | `scripts/maintenance/` or `tools/` after review |
| Fixture payloads or golden outputs | `fixtures/` |
| Executable tests | `tests/` or accepted test root |
| Source records, lifecycle data, emitted artifacts, receipts, proofs, catalogs, or published payloads | `data/` under governed lifecycle roots |
| Release manifests, rollback cards, correction notices, or publication decisions | `release/` |
| Secrets, credentials, signing keys, tokens, or local `.env` contents | not in repo |
| Policy decisions, sensitivity approvals, rights approvals, or release approvals | `policy/`, review, and release roots |

## Use pattern

A one-off script should include a short header or adjacent note with:

```text
Purpose: <one task only>
Owner: OWNER_TBD
Issue/decision: NEEDS VERIFICATION
Inputs: <paths or commands>
Outputs: <paths or stdout only>
Dry run: yes/no
Rollback: <how to undo>
Delete after: <date or condition>
Promote if: <repeat-use or trust-bearing trigger>
```

Prefer scripts that print planned changes before writing. Any write-capable script should make the write path explicit and leave a reviewable `git diff`.

## Delete or promote

| Signal | Required action |
|---|---|
| Script has completed its one task | Delete it in the same PR or a follow-up cleanup PR. |
| Script is useful more than once | Move to `scripts/dev/` or `scripts/maintenance/` if still lightweight. |
| Script gates evidence, policy, validation, release, or publication | Promote to `tools/`, `pipelines/`, or release tooling with tests and review. |
| Script generates fixtures or expected outputs | Move generation logic to an accepted generator/tooling lane and record deterministic inputs/outputs. |
| Script mutates lifecycle, proof, receipt, catalog, or release records | Route through governed lifecycle/release roots and document rollback. |
| Script is called by CI | Document workflow ownership, exit codes, inputs, outputs, and failure behavior. |

## Validation

```bash
find scripts/one_off -maxdepth 2 -type f | sort
find scripts/one_off -name '*.sh' -print0 | xargs -0 -r bash -n
find scripts/one_off -name '*.py' -print0 | xargs -0 -r python -m py_compile
git diff -- scripts/one_off
```

> [!WARNING]
> Before running any future one-off script, inspect it first. Confirm dry-run behavior, target paths, expected outputs, and rollback steps. Do not run write-capable scripts against RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, policy, or release roots without explicit review.

## Open questions

| Question | Status |
|---|---|
| Should this lane remain empty except during active migrations or audits? | NEEDS VERIFICATION |
| Should one-off scripts require issue IDs or decision references in filenames or headers? | NEEDS VERIFICATION |
| What cleanup cadence should remove stale one-off scripts? | NEEDS VERIFICATION |
| Which owner approves promotion from `scripts/one_off/` into `tools/`, `pipelines/`, `packages/`, `scripts/dev/`, or `scripts/maintenance/`? | NEEDS VERIFICATION |
