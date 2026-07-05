# `scripts/` — Operational Script Root

Small operational scripts for local development, bounded maintenance, one-off work, and promotion-sensitive helper commands that have not graduated to `tools/`, `pipelines/`, or `packages/`.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-readme
title: scripts/README.md — Operational Script Root
type: root-readme; script-root; governance-index; operational-helper-boundary
version: v0.2
status: draft; canonical-root-name; mixed-maturity-script-lanes; promotion-sensitive-helpers-present; NEEDS VERIFICATION
owners: OWNER_TBD — Developer tooling steward · Maintenance tooling steward · QA steward · Release steward · Docs steward
created: NEEDS VERIFICATION — short root stub existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; scripts; operational-helpers; no-production-authority
tags: [kfm, scripts, dev, maintenance, one-off, maplibre, perf, artifacts, guardrail]
related:
  - ./dev/README.md
  - ./maintenance/README.md
  - ./one_off/README.md
  - ../tools/README.md
  - ../pipelines/
  - ../packages/
  - ../fixtures/
  - ../tests/
  - ../artifacts/
  - ../data/
  - ../release/
notes:
  - "Expanded from a short root README that said scripts are small operational scripts and long-lived trust-bearing scripts graduate to tools, pipelines, or packages."
  - "Current-session search confirms child lanes dev, maintenance, and one_off plus several root-level MapLibre perf artifact helper scripts."
  - "Root-level MapLibre scripts are promotion-sensitive helpers because they write artifacts, receipts, manifest-shaped objects, proof-pack-shaped objects, failure bundles, and correction/rollback drafts under artifacts/perf."
  - "This README does not prove CI wiring, runtime deployment, release readiness, validator coverage, dependency availability, or public-client behavior."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: scripts" src="https://img.shields.io/badge/root-scripts%2F-blue">
  <img alt="Authority: operational helpers" src="https://img.shields.io/badge/authority-operational__helpers-purple">
  <img alt="Maturity: mixed" src="https://img.shields.io/badge/maturity-mixed-orange">
  <img alt="Rule: graduate trust logic" src="https://img.shields.io/badge/rule-graduate__trust__logic-critical">
</p>

**Status:** draft / canonical script root / mixed maturity  
**Path:** `scripts/`  
**Root rule:** small operational scripts may live here; long-lived or trust-bearing behavior graduates to `tools/`, `pipelines/`, or `packages/`.  
**Truth posture:** CONFIRMED root path and current child/script inventory from repository search; CONFIRMED selected behavior for inspected MapLibre and doctrine-maintenance scripts; NEEDS VERIFICATION for CI callers, dependency setup, validator integration, release use, and long-term placement.

## Quick jumps

[Purpose](#purpose) · [Boundary](#boundary) · [Current inventory](#current-inventory) · [Root-level MapLibre helpers](#root-level-maplibre-helpers) · [Child lanes](#child-lanes) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Promotion rules](#promotion-rules) · [Validation](#validation) · [Open questions](#open-questions)

---

## Purpose

`scripts/` is the KFM root for small operational scripts.

Use this root for lightweight helpers, local wrappers, bounded maintenance commands, one-off scripts, and short operational compositions whose behavior is not yet a long-lived trust-bearing tool, reusable package, or formal pipeline.

The original rule remains controlling: long-lived trust-bearing scripts graduate to `tools/`, `pipelines/`, or `packages/`.

## Boundary

This root is not schema authority, semantic contract authority, policy authority, validator authority, data lifecycle storage, proof authority, receipt authority, release authority, package implementation, pipeline orchestration, or public-client behavior.

Scripts may help generate, inspect, summarize, or stage artifacts. They must not bypass KFM lifecycle gates, publish data, approve release, silently mutate governed roots, or treat generated artifacts as sovereign truth.

> [!IMPORTANT]
> A script can support governance, but it does not replace governance. Release, policy, evidence, review, correction, rollback, and public display remain governed state transitions backed by accepted roots, receipts, proofs, tests, and review.

## Current inventory

| Path | Current status | Notes |
|---|---|---|
| `README.md` | present | This root index. |
| `dev/README.md` | present | Local developer helper lane. |
| `dev/bootstrap.sh` | placeholder confirmed | Prints dependency/pre-commit setup TODO. |
| `dev/regen_fixtures.sh` | placeholder confirmed | Prints `TODO`; does not regenerate fixtures. |
| `maintenance/README.md` | present | Maintenance script lane for doctrine preflight, registry hygiene, readiness, and related checks. |
| `maintenance/*` | present | Doctrine preflight, sync, readiness, test-suite, and helper scripts confirmed by search. |
| `one_off/README.md` | present | Temporary one-off script holding lane; no direct one-off scripts confirmed by current search. |
| `maplibre-smoke-perf.mjs` | inspected | Runs Playwright/MapLibre smoke scenarios and writes perf results, screenshots, frame-times, and a run receipt under `artifacts/perf`. |
| `build-maplibre-render-diff.mjs` | inspected | Compares screenshots to fixture baselines and writes a render-diff report; exits non-zero on failed diff. |
| `attest-maplibre-perf.mjs` | inspected | Builds an unsigned DSSE-shaped envelope and checksum for the MapLibre perf run receipt. |
| `build-maplibre-perf-release-manifest.mjs` | inspected | Builds a MapLibre perf release-manifest-shaped artifact under `artifacts/perf`; not release authority by itself. |
| `build-maplibre-perf-proof-pack.mjs` | inspected | Builds a MapLibre perf proof-pack-shaped artifact from manifest, receipt, and envelope hashes. |
| `build-maplibre-perf-correction-and-rollback.mjs` | inspected | Emits draft correction and rollback artifacts when the candidate manifest is not acceptable. |
| `build-maplibre-perf-failure-bundle.mjs` | inspected | Captures available MapLibre perf failure artifacts and hashes into a failure bundle. |

## Root-level MapLibre helpers

The root-level MapLibre scripts are operational helpers for performance, render-diff, attestation-shaped output, proof-pack-shaped output, release-manifest-shaped output, correction/rollback drafts, and failure-bundle capture.

They are useful but placement-sensitive because they write trust-adjacent outputs under `artifacts/perf`.

| Script | Writes / checks | Boundary |
|---|---|---|
| `maplibre-smoke-perf.mjs` | perf results, screenshots, frame-time CSV files, run receipt | Produces performance evidence candidates; does not approve release or public display. |
| `build-maplibre-render-diff.mjs` | render-diff report and diff images | Fails when render diffs exceed threshold; does not replace visual review or release gates. |
| `attest-maplibre-perf.mjs` | unsigned envelope and checksum | Produces unsigned attestation-shaped output; signing/release remains governed. |
| `build-maplibre-perf-release-manifest.mjs` | release-manifest-shaped artifact | Builds candidate/rejected metadata; does not publish. |
| `build-maplibre-perf-proof-pack.mjs` | proof-pack-shaped artifact | Proof acceptance requires validator/review evidence. |
| `build-maplibre-perf-correction-and-rollback.mjs` | draft correction notice and rollback plan | Drafts failure-response artifacts; release root remains authoritative. |
| `build-maplibre-perf-failure-bundle.mjs` | failure bundle | Captures failure evidence; does not resolve or approve correction. |

## Child lanes

| Lane | Purpose | Current posture |
|---|---|---|
| `dev/` | Local developer convenience scripts and placeholder setup/regeneration helpers. | Draft; placeholder scripts present. |
| `maintenance/` | Bounded maintenance CLIs and wrappers, especially doctrine-artifact preflight and registry hygiene. | Draft; substantive doctrine tooling present; mixed maturity. |
| `one_off/` | Temporary ticket-bound scripts that should be deleted or promoted. | Draft; README only; no direct one-off scripts found in current search. |

## Repo fit

```text
scripts/
├── README.md
├── dev/
├── maintenance/
├── one_off/
├── maplibre-smoke-perf.mjs
├── build-maplibre-render-diff.mjs
├── attest-maplibre-perf.mjs
├── build-maplibre-perf-release-manifest.mjs
├── build-maplibre-perf-proof-pack.mjs
├── build-maplibre-perf-correction-and-rollback.mjs
└── build-maplibre-perf-failure-bundle.mjs

tools/              # long-lived trust-bearing validators/builders/generators
pipelines/          # executable pipeline orchestration
packages/           # reusable implementation libraries
fixtures/           # examples and golden/negative cases
tests/              # executable tests and proof of behavior
artifacts/          # build/docs/qa/temporary artifacts; not sovereign truth
data/               # lifecycle records, receipts, proofs, catalogs, emitted data
release/            # release, correction, rollback authority
```

## What belongs here

- Small operational scripts.
- Local development helpers.
- Bounded maintenance scripts.
- One-off scripts with deletion or promotion plans.
- Thin wrappers around accepted commands.
- Promotion-sensitive helper scripts while their long-term home is being verified.
- README guardrails that prevent scripts from becoming hidden schema, policy, data, proof, release, or publication authority.

## What does not belong here

| Do not put this in `scripts/` | Correct home |
|---|---|
| Long-lived validators, generators, builders, proof-pack tools, release tools, or QA tools | `tools/` |
| Pipeline orchestration or repeatable production flow | `pipelines/` |
| Reusable libraries imported by multiple systems | `packages/` |
| Schema definitions | `schemas/` |
| Semantic contracts | `contracts/` |
| Policy rules or approval records | `policy/`, review, and release roots |
| Fixture payloads or golden outputs | `fixtures/` |
| Executable tests | `tests/` or accepted test root |
| Lifecycle data, receipts, proofs, source records, catalogs, or published payloads | accepted `data/` lifecycle/proof/receipt/catalog/source/published roots |
| Release manifests, rollback cards, correction notices, or publication decisions | `release/` unless explicitly artifact-only and pending promotion review |

## Promotion rules

Move or redesign a script when any of the following become true:

| Signal | Required action |
|---|---|
| It is used repeatedly by maintainers or CI | Add ownership, tests, command contract, and consider `tools/` or `pipelines/`. |
| It gates evidence, policy, validation, release, or publication | Promote to a governed tooling or pipeline lane with validator coverage and review. |
| It writes receipts, proof packs, release manifests, correction notices, or rollback drafts | Confirm accepted output home, schema, validator, review, and rollback path. |
| It implements reusable logic | Move reusable logic to `packages/`; keep a script only as a thin CLI wrapper. |
| It mutates data, fixtures, registries, schemas, contracts, policy, or release roots | Add dry-run mode, explicit targets, review instructions, and rollback notes before use. |
| It is a one-off task that has completed | Delete it or move lessons into docs/tests/tooling. |

## Validation

```bash
find scripts -maxdepth 2 -type f | sort
find scripts -name '*.sh' -print0 | xargs -0 -r bash -n
find scripts -name '*.py' -print0 | xargs -0 -r python -m py_compile
node --check scripts/maplibre-smoke-perf.mjs
node --check scripts/build-maplibre-render-diff.mjs
node --check scripts/attest-maplibre-perf.mjs
node --check scripts/build-maplibre-perf-release-manifest.mjs
node --check scripts/build-maplibre-perf-proof-pack.mjs
node --check scripts/build-maplibre-perf-correction-and-rollback.mjs
node --check scripts/build-maplibre-perf-failure-bundle.mjs
```

> [!WARNING]
> Some scripts write files under review-sensitive paths such as `artifacts/perf`. Inspect outputs and review `git diff` before committing generated artifacts.

## Review burden

Maintainer review is required for ordinary script changes.

Steward review is required when a script touches evidence, policy, release, correction, rollback, proof, receipt, catalog, publication, source-admission, sensitive-domain flows, or generated artifacts that may be mistaken for governed truth.

## Open questions

| Question | Status |
|---|---|
| Should the root-level MapLibre perf scripts remain under `scripts/` or graduate to `tools/`, `tools/release/`, `tools/proof_pack/`, `tools/validators/`, or `pipelines/`? | NEEDS VERIFICATION |
| Which CI workflows call scripts under this root today? | NEEDS VERIFICATION |
| Should `artifacts/perf` outputs generated by scripts be mirrored into governed receipt/proof/release roots after validation? | NEEDS VERIFICATION |
| Which owner signs off when a script graduates from `scripts/` into `tools/`, `pipelines/`, or `packages/`? | NEEDS VERIFICATION |
| Should root-level scripts move into child folders once their role is clarified? | NEEDS VERIFICATION |
