# `scripts/dev/` — Development Helper Scripts

Local developer convenience scripts for KFM; short-lived helpers live here before trust-bearing logic graduates to `tools/`, `pipelines/`, or `packages/`.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-dev-readme
title: scripts/dev/README.md — Development Helper Scripts
type: readme; directory-readme; dev-script-guardrail
version: v0.1
status: draft; greenfield-placeholders-present; NEEDS VERIFICATION
owners: OWNER_TBD — Developer tooling steward · QA steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; dev-scripts; local-only; no-production-authority
tags: [kfm, scripts, dev, bootstrap, fixtures, tooling, guardrail]
related:
  - ../README.md
  - ../../tools/README.md
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
  - ../../pipelines/
  - ../../packages/
notes:
  - "Expanded from a greenfield stub at scripts/dev/README.md."
  - "Current-session search confirms bootstrap.sh and regen_fixtures.sh under this folder."
  - "Both inspected scripts are placeholders and do not currently install dependencies or regenerate fixtures."
  - "This README documents boundaries and review rules; it does not prove script readiness, CI wiring, dependency installation, fixture regeneration, or validator behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: scripts/dev" src="https://img.shields.io/badge/root-scripts%2Fdev-blue">
  <img alt="Authority: local convenience" src="https://img.shields.io/badge/authority-local__convenience-purple">
  <img alt="Maturity: placeholder scripts" src="https://img.shields.io/badge/maturity-placeholders-orange">
  <img alt="Boundary: not production tooling" src="https://img.shields.io/badge/boundary-not__production__tooling-critical">
</p>

**Status:** draft / local development helper lane  
**Path:** `scripts/dev/`  
**Current scripts:** `bootstrap.sh`, `regen_fixtures.sh`  
**Truth posture:** CONFIRMED path and two placeholder scripts; NEEDS VERIFICATION for dependency setup, fixture regeneration behavior, test coverage, CI use, and promotion path.

## Quick jumps

[Purpose](#purpose) · [Boundary](#boundary) · [Current scripts](#current-scripts) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Usage](#usage) · [Promotion rules](#promotion-rules) · [Validation](#validation) · [Open questions](#open-questions)

---

## Purpose

`scripts/dev/` is the holding lane for small local development helpers.

Use it for developer convenience scripts that help set up a workstation, scaffold repeatable local checks, or run bounded local maintenance while behavior is still too small, local, or immature for `tools/`, `pipelines/`, or `packages/`.

The parent `scripts/README.md` states that `scripts/` is for small operational scripts, and that long-lived trust-bearing scripts graduate to `tools/`, `pipelines/`, or `packages/`.

## Boundary

This folder is not production tooling, validator authority, pipeline orchestration, package code, data lifecycle storage, fixture authority, policy authority, release authority, or CI proof by itself.

A dev script may help a maintainer run a local task. It must not become the normal public path, bypass KFM lifecycle gates, write directly into release authority, silently mutate canonical records, or claim validation/release success without receipts, tests, and review.

> [!IMPORTANT]
> Developer convenience is not governance. If a script starts enforcing trust-bearing behavior, generating governed artifacts, mutating fixture families, or gating promotion, it should be reviewed for graduation into `tools/`, `pipelines/`, `packages/`, or an accepted test root.

## Current scripts

| Script | Confirmed behavior | Status | Notes |
|---|---|---|---|
| `bootstrap.sh` | Uses Bash with `set -euo pipefail` and currently echoes `TODO: install Python and Node deps, set up pre-commit`. | placeholder | It does not currently install dependencies. |
| `regen_fixtures.sh` | Uses Bash with `set -euo pipefail` and currently echoes `TODO`. | placeholder | It does not currently regenerate fixtures. |

## Repo fit

```text
scripts/
├── README.md                         # parent script-root guidance
└── dev/
    ├── README.md                     # this file
    ├── bootstrap.sh                  # placeholder local setup helper
    └── regen_fixtures.sh             # placeholder fixture-regeneration helper

tools/                                # long-lived trust-bearing validators/builders/generators
pipelines/                            # executable pipeline orchestration
packages/                             # reusable implementation libraries
fixtures/                             # valid/invalid/golden/negative examples
tests/                                # executable tests and proof of behavior
data/                                 # lifecycle records and emitted artifacts
release/                              # release, correction, rollback authority
```

## What belongs here

- Local developer bootstrap helpers.
- Small repeatable shell scripts used during development.
- Temporary developer convenience wrappers around already-accepted commands.
- Non-authoritative setup checks that print instructions or run safe local validation.
- Scripts that are clearly labeled as placeholders or local-only until tested and promoted.

## What does not belong here

| Do not put this in `scripts/dev/` | Correct home |
|---|---|
| Long-lived validators, generators, builders, proof-pack tools, release tools, or QA tools | `tools/` |
| Pipeline orchestration | `pipelines/` |
| Reusable libraries imported by multiple systems | `packages/` |
| Fixture payloads or golden outputs | `fixtures/` |
| Executable tests | `tests/` or accepted test root |
| Source records, lifecycle data, emitted artifacts, receipts, proofs, catalogs, or published payloads | `data/` under governed lifecycle roots |
| Release manifests, rollback cards, correction notices, or publication decisions | `release/` |
| Secrets, credentials, signing keys, tokens, or local `.env` contents | not in repo |
| Policy decisions, sensitivity approvals, or rights approvals | `policy/` and governed review/release roots |

## Usage

Current scripts are placeholders. They are safe to inspect, but they should not be treated as complete setup or regeneration commands.

```bash
bash scripts/dev/bootstrap.sh
bash scripts/dev/regen_fixtures.sh
```

Expected current behavior:

```text
bootstrap.sh       -> prints a dependency-setup TODO
regen_fixtures.sh  -> prints TODO
```

## Promotion rules

Move or redesign a script when any of the following become true:

| Signal | Required action |
|---|---|
| The script gates promotion, release, evidence, policy, or publication | Move to `tools/`, `pipelines/`, or accepted release/tooling lane with tests. |
| The script generates or mutates fixtures | Add deterministic inputs/outputs, fixture README updates, tests, and review notes. |
| The script writes lifecycle, proof, receipt, catalog, or release artifacts | Route through governed lifecycle/release roots and add receipts/rollback notes. |
| The script is used by CI | Document the workflow, inputs, outputs, exit codes, and failure behavior. |
| The script is reused by multiple packages or apps | Promote reusable logic to `packages/`; keep this script as a thin local wrapper only if useful. |

## Validation

```bash
find scripts/dev -maxdepth 2 -type f | sort
bash -n scripts/dev/bootstrap.sh
bash -n scripts/dev/regen_fixtures.sh
bash scripts/dev/bootstrap.sh
bash scripts/dev/regen_fixtures.sh
```

When these scripts gain real behavior, add deterministic tests and replace placeholder output with explicit success/failure contracts.

## Open questions

| Question | Status |
|---|---|
| Which dependency manager and setup commands should `bootstrap.sh` use? | NEEDS VERIFICATION |
| Should `bootstrap.sh` install Python dependencies, Node dependencies, pre-commit hooks, or only print instructions? | NEEDS VERIFICATION |
| Which fixture families, if any, should `regen_fixtures.sh` regenerate? | NEEDS VERIFICATION |
| Should fixture regeneration live in `tools/generators/` instead of `scripts/dev/` once implemented? | NEEDS VERIFICATION |
| Should these scripts be called by CI or remain local-only? | NEEDS VERIFICATION |
