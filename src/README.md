# `src/` — Root Python Package Compatibility Lane

Compatibility lane for the root `kfm` Python package marker. This path is not the primary home for shared implementation packages, deployable apps, validators, pipelines, data, or release authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/src-readme
title: src/README.md — Root Python Package Compatibility Lane
type: readme; directory-readme; source-layout-guardrail; compatibility-index
version: v0.1
status: draft; minimal-root-package-present; compatibility-lane; NEEDS VERIFICATION
owners: OWNER_TBD — Architecture steward · Package steward · Developer tooling steward · Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; source-layout; python-package; no-parallel-authority
tags: [kfm, src, python, package, source-layout, compatibility, guardrail]
related:
  - ../packages/README.md
  - ../apps/README.md
  - ../tools/README.md
  - ../scripts/README.md
  - ../tests/
  - ../schemas/
  - ../contracts/
  - ../policy/
  - ../data/
  - ../release/
notes:
  - "Expanded from an empty src/README.md."
  - "Current-session search found only src/kfm/__init__.py under src/."
  - "src/kfm/__init__.py currently contains only a root package docstring."
  - "This README is a compatibility guardrail and does not prove package implementation, import stability, packaging metadata, tests, CI wiring, runtime behavior, or public API maturity."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: src" src="https://img.shields.io/badge/root-src%2F-blue">
  <img alt="Authority: compatibility lane" src="https://img.shields.io/badge/authority-compatibility__lane-purple">
  <img alt="Maturity: minimal" src="https://img.shields.io/badge/maturity-minimal-orange">
  <img alt="Boundary: no parallel package root" src="https://img.shields.io/badge/boundary-no__parallel__package__root-critical">
</p>

**Status:** draft / minimal Python source-layout lane  
**Path:** `src/`  
**Current package marker:** `src/kfm/__init__.py`  
**Truth posture:** CONFIRMED `src/README.md` exists and was empty; CONFIRMED `src/kfm/__init__.py` exists as a minimal package marker; NEEDS VERIFICATION for packaging configuration, imports, tests, CI, release usage, and whether this root should remain long-term.

## Quick jumps

[Purpose](#purpose) · [Boundary](#boundary) · [Current inventory](#current-inventory) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Promotion rules](#promotion-rules) · [Validation](#validation) · [Open questions](#open-questions)

---

## Purpose

`src/` currently acts as a minimal Python source-layout compatibility lane for the root `kfm` package marker.

Use this path cautiously. In this repository, `packages/` is the documented home for shared reusable implementation packages, `apps/` is the deployable application root, and `tools/` owns repo-wide validators, generators, builders, and trust-tooling. Do not use `src/` to create a parallel implementation authority without an ADR or migration note.

## Boundary

This directory is not the canonical home for domain packages, deployable applications, validators, generators, pipelines, scripts, fixtures, schemas, semantic contracts, policy rules, lifecycle data, proofs, receipts, release records, public map payloads, or direct model-runtime outputs.

A Python module under `src/` may provide import scaffolding only if it does not bypass KFM governed interfaces, lifecycle gates, policy checks, EvidenceBundle resolution, review state, release state, correction lineage, or rollback controls.

> [!IMPORTANT]
> `src/` must not become a shadow `packages/` root. If code becomes reusable, trust-bearing, domain-owned, deployable, or CI-critical, place it in the appropriate responsibility root and keep this lane as a compatibility shim only if needed.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `src/README.md` | present | Empty file expanded by this README. |
| `src/kfm/__init__.py` | present | Minimal root package marker with docstring: `Kansas Frontier Matrix root package.` |
| `src/*` | no other files found in current search | Full tree audit NOT RUN. |

## Repo fit

```text
src/
├── README.md                         # this file
└── kfm/
    └── __init__.py                   # minimal root package marker

packages/                             # shared reusable implementation packages
apps/                                 # deployable application boundaries
tools/                                # validators, generators, builders, proof/release/QA tooling
scripts/                              # small operational scripts before graduation
tests/                                # executable tests and proof of behavior
schemas/                              # machine-checkable shape
contracts/                            # semantic meaning
policy/                               # admissibility, rights, sensitivity, and release posture
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted data
release/                              # release, correction, rollback authority
```

## What belongs here

- This README.
- Minimal Python package markers required by packaging or import compatibility.
- Thin compatibility shims only when their target authority is documented elsewhere.
- Migration notes if code is moved from `src/` into `packages/`, `apps/`, `tools/`, or another accepted root.
- Import boundary notes that prevent `src/` from becoming a parallel implementation root.

## What does not belong here

| Do not put this in `src/` | Correct home |
|---|---|
| Shared reusable libraries | `packages/` |
| Deployable apps, services, CLIs, workers, or UI shells | `apps/` |
| Repo-wide validators, generators, builders, proof-pack tools, release tools, QA tools | `tools/` |
| Small operational helpers or one-off scripts | `scripts/` |
| Pipeline orchestration | `pipelines/` |
| Source connectors and fetchers | `connectors/` or accepted source-acquisition root |
| Schema definitions | `schemas/` |
| Semantic contracts | `contracts/` |
| Policy rules, sensitivity decisions, rights decisions, release approvals | `policy/`, review, and release roots |
| Fixtures, golden outputs, valid/invalid examples | `fixtures/` |
| Executable tests | `tests/` or accepted package/app test root |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| EvidenceBundles, SourceDescriptors, receipts, proofs, catalogs, or release manifests | accepted `data/`, source-registry, proof, receipt, catalog, or release roots |
| Public map payloads, public tiles, generated summaries, dashboards, screenshots, or direct model-runtime output | governed artifact/UI/publication roots after validation and release |

## Promotion rules

Move or redesign code under `src/` when any of the following become true:

| Signal | Required action |
|---|---|
| Code becomes a reusable implementation library | Move to `packages/` and add package-level README/tests. |
| Code becomes a deployable app, worker, CLI, or service | Move to `apps/` with app boundary documentation. |
| Code becomes a validator, generator, builder, proof-pack helper, release helper, or QA tool | Move to `tools/` with tests and command contract. |
| Code becomes pipeline orchestration | Move to `pipelines/` or accepted pipeline root. |
| Code is used only for local operations | Move to `scripts/` unless it is trust-bearing. |
| Code accesses lifecycle, evidence, policy, or release state | Add governed access boundaries, tests, review notes, and correct-root placement. |

## Validation

```bash
find src -maxdepth 4 -type f | sort
python -m py_compile src/kfm/__init__.py
python - <<'PY'
import pathlib
print(pathlib.Path('src/kfm/__init__.py').read_text())
PY
```

When `src/` gains real code, add packaging metadata, import tests, type checks, and explicit boundary tests before treating it as implementation-ready.

## Open questions

| Question | Status |
|---|---|
| Should `src/` remain as a root Python compatibility lane, or should all implementation move under `packages/`? | NEEDS VERIFICATION |
| Which packaging configuration, if any, includes `src/kfm` today? | NEEDS VERIFICATION |
| Should the root `kfm` package re-export packages, remain empty, or be removed after migration? | NEEDS VERIFICATION |
| Which tests or CI workflows import `kfm` from `src/` today? | NEEDS VERIFICATION |
| Who owns decisions about keeping, retiring, or promoting this source-layout lane? | NEEDS VERIFICATION |
