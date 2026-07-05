# `src/kfm/` — Root `kfm` Package Marker

Minimal Python package marker for Kansas Frontier Matrix import compatibility. This package currently has no confirmed implementation beyond `__init__.py`.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/src-kfm-readme
title: src/kfm/README.md — Root kfm Package Marker
type: readme; package-readme; source-layout-guardrail; compatibility-index
version: v0.1
status: draft; minimal-package-marker; no-implementation-confirmed; NEEDS VERIFICATION
owners: OWNER_TBD — Architecture steward · Package steward · Developer tooling steward · Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; source-layout; python-package; import-compatibility; no-parallel-authority
tags: [kfm, src, python, package, import, compatibility, guardrail]
related:
  - ../README.md
  - ../../packages/README.md
  - ../../apps/README.md
  - ../../tools/README.md
  - ../../scripts/README.md
  - ../../tests/
  - ../../schemas/
  - ../../contracts/
  - ../../policy/
  - ../../data/
  - ../../release/
notes:
  - "Expanded from an empty src/kfm/README.md."
  - "Current-session search found only src/kfm/__init__.py under src/kfm/."
  - "src/kfm/__init__.py currently contains only the docstring: Kansas Frontier Matrix root package."
  - "This README does not prove import stability, package metadata, tests, CI wiring, runtime behavior, public API behavior, or implementation maturity."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Package: kfm" src="https://img.shields.io/badge/package-kfm-blue">
  <img alt="Authority: marker only" src="https://img.shields.io/badge/authority-marker__only-purple">
  <img alt="Maturity: minimal" src="https://img.shields.io/badge/maturity-minimal-orange">
  <img alt="Boundary: no implementation authority" src="https://img.shields.io/badge/boundary-no__implementation__authority-critical">
</p>

**Status:** draft / package-marker compatibility lane  
**Path:** `src/kfm/`  
**Current file:** `src/kfm/__init__.py`  
**Truth posture:** CONFIRMED this README path existed as an empty file; CONFIRMED `__init__.py` exists with only a package docstring; NEEDS VERIFICATION for packaging metadata, imports, tests, CI behavior, release use, and long-term package role.

## Quick jumps

[Purpose](#purpose) · [Boundary](#boundary) · [Current inventory](#current-inventory) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Promotion rules](#promotion-rules) · [Validation](#validation) · [Open questions](#open-questions)

---

## Purpose

`src/kfm/` currently provides a minimal root Python package marker for KFM.

It may be useful for import compatibility, future package bootstrapping, or migration shims, but current evidence does not show implementation beyond the package docstring.

Use this directory cautiously. The documented home for shared reusable implementation is `packages/`; deployable apps belong in `apps/`; validators, generators, builders, proof-pack helpers, release helpers, and QA tooling belong in `tools/`.

## Boundary

This package is not a domain package, deployable application, validator, generator, pipeline, script, fixture lane, schema authority, contract authority, policy engine, lifecycle data root, proof root, receipt root, release root, public API, UI renderer, map payload, or model-runtime adapter.

It must not become a shortcut around KFM governed interfaces, lifecycle gates, EvidenceBundle resolution, policy checks, rights and sensitivity review, release state, correction lineage, or rollback controls.

> [!IMPORTANT]
> `src/kfm/` is currently a marker, not an implementation proof. Do not import it as evidence that KFM runtime, API, domain packages, validators, or public surfaces are implemented.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `src/kfm/README.md` | present | Empty file expanded by this README. |
| `src/kfm/__init__.py` | present | Contains only `"""Kansas Frontier Matrix root package."""`. |
| `src/kfm/*` | no other files found in current search | Full tree audit NOT RUN. |

## Repo fit

```text
src/
└── kfm/
    ├── README.md                     # this file
    └── __init__.py                   # minimal package marker

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
- `__init__.py` package marker.
- Thin import-compatibility shims only when the authoritative implementation home is documented elsewhere.
- Migration notes if imports move from `src/kfm/` to `packages/`, `apps/`, `tools/`, or another accepted root.
- Boundary notes that prevent `src/kfm/` from becoming a hidden parallel package root.

## What does not belong here

| Do not put this in `src/kfm/` | Correct home |
|---|---|
| Shared reusable implementation libraries | `packages/` |
| Domain packages | `packages/domains/` or accepted package lane |
| Deployable services, CLIs, workers, or UI shells | `apps/` |
| Repo-wide validators, generators, builders, proof-pack tools, release tools, or QA tools | `tools/` |
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

Move or redesign code under `src/kfm/` when any of the following become true:

| Signal | Required action |
|---|---|
| Code becomes reusable implementation logic | Move to `packages/` with package README, tests, and ownership. |
| Code becomes domain-owned implementation | Move to `packages/domains/<domain>/` or accepted domain package lane. |
| Code becomes a deployable app, worker, CLI, or service | Move to `apps/` with app boundary documentation. |
| Code becomes a validator, generator, builder, proof-pack helper, release helper, or QA tool | Move to `tools/` with tests and command contract. |
| Code becomes pipeline orchestration | Move to `pipelines/` or accepted pipeline root. |
| Code is only local operational glue | Move to `scripts/` unless it is trust-bearing. |
| Code accesses lifecycle, evidence, policy, or release state | Add governed access boundaries, tests, steward review, and correct-root placement. |

## Validation

```bash
find src/kfm -maxdepth 4 -type f | sort
python -m py_compile src/kfm/__init__.py
python - <<'PY'
import pathlib
print(pathlib.Path('src/kfm/__init__.py').read_text())
PY
```

When this package gains real code, add import tests, packaging metadata checks, type checks, and boundary tests before treating it as implementation-ready.

## Open questions

| Question | Status |
|---|---|
| Should `src/kfm/` remain as a package marker, become an import shim, or be retired? | NEEDS VERIFICATION |
| Which packaging configuration, if any, includes `src/kfm` today? | NEEDS VERIFICATION |
| Should the root `kfm` package re-export selected package APIs, or remain empty? | NEEDS VERIFICATION |
| Which tests or CI workflows import `kfm` from `src/kfm` today? | NEEDS VERIFICATION |
| Who owns decisions about keeping, retiring, or promoting this package marker? | NEEDS VERIFICATION |
