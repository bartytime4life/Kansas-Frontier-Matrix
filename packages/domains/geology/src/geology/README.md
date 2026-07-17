<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-geology-src-geology-readme
title: Geology Python Source Namespace
type: readme
version: v0.1
status: draft; repository-grounded; greenfield-scaffold
owners:
  - OWNER_TBD — Geology package/domain steward
  - OWNER_TBD — Validation and sensitivity reviewer
created: 2026-07-17
updated: 2026-07-17
policy_label: public; packages; geology; implementation; non-authoritative; sensitive-location-aware
path: packages/domains/geology/src/geology/README.md
truth_posture: CONFIRMED package name and version, bounded namespace inventory, empty __init__.py, one-line placeholder modules, sibling README pattern, adjacent authority roots, and placeholder tests / UNKNOWN installed-package behavior, public API, consumers, dependencies, build backend, CI wiring, production behavior, evidence closure, policy enforcement, and release behavior / PROPOSED future helper behavior only
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1cadc7ebc81e29b863ea29fd78f4a1c7d2d23a16
related:
  - ../README.md
  - ../../README.md
  - ../../pyproject.toml
  - ../../../../../docs/domains/geology/README.md
  - ../../../../../contracts/domains/geology/README.md
  - ../../../../../schemas/contracts/v1/domains/geology/README.md
  - ../../../../../policy/domains/geology/README.md
  - ../../../../../tests/domains/geology/README.md
  - ../../../../../fixtures/domains/geology/README.md
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, geology, natural-resources, python, package, source-namespace, greenfield, public-safe-geometry]
notes:
  - "This README records the namespace as found; it does not claim that placeholder modules implement behavior."
  - "Only importable Geology helper code belongs here; authority-bearing records remain in their governing roots."
  - "Exact borehole, well-log, resource, sample, extraction, and other sensitive locations remain restricted until evidence, rights, policy, review, and release gates permit a public-safe representation."
[/KFM_META_BLOCK_V2] -->

# Geology Python Source Namespace

`packages/domains/geology/src/geology/` is the importable-code boundary for the `kfm-domain-geology` package. The current package is a `0.0.0` greenfield scaffold, not an implemented geology library.

## Purpose

This folder owns future reusable Python helpers for the Geology and Natural Resources domain. Helpers may normalize or validate caller-supplied candidates, preserve source roles, and prepare bounded candidate metadata, but they must not become an authority for geology truth, source admission, rights, sensitivity, evidence, lifecycle state, or release.

## Authority level

**Implementation-bearing boundary; currently a non-functional greenfield scaffold.**

The namespace may implement accepted contracts and schemas. It does not define them, admit sources, make policy decisions, close evidence, authorize exact-location exposure, or approve publication.

## Status

**CONFIRMED scaffold / UNKNOWN runtime behavior.** The bounded inventory at `main@1cadc7ebc81e29b863ea29fd78f4a1c7d2d23a16` is:

| File | Repository evidence | Implemented behavior |
|---|---|---|
| `__init__.py` | Empty file | None; no exports or public API are declared. |
| `identity.py` | One line identifying a greenfield identity-normalization placeholder | None. |
| `layers.py` | One line identifying a greenfield layer-descriptor placeholder | None. |
| `observations.py` | One line identifying a greenfield observation-parsing placeholder | None. |

`packages/domains/geology/pyproject.toml` declares package name `kfm-domain-geology` and version `0.0.0`; it does not declare dependencies or a build backend. The repository also contains Geology contracts, schemas, policy scaffolds, fixtures, and tests in their own roots, but their presence does not prove this namespace consumes or enforces them.

Installed-package behavior, supported imports outside an explicit source-path check, consumers, packaging, CI wiring, and production behavior remain **UNKNOWN**. The current Geology test modules are placeholders and do not prove helper behavior.

## What belongs here

- small, deterministic, importable Geology helper modules;
- identity helpers that preserve source-native identifiers, ambiguity, version, spatial support, and temporal scope;
- candidate observation parsing that keeps measurements, interpretations, administrative context, models, and generated material distinguishable;
- candidate layer-description helpers that retain evidence, policy, release, correction, and rollback references supplied by callers;
- public-safe geometry helper implementations only after accepted interfaces and policy inputs exist;
- explicit result types and reason codes needed by reviewed package interfaces;
- package-local documentation for behavior that is actually implemented.

Future code must preserve source values and caveats, avoid hidden I/O, and return explicit failures rather than inventing missing evidence, rights, sensitivity, geometry, or authority.

## What does NOT belong here

- semantic contracts or JSON Schemas;
- executable policy, sensitivity rules, source-admission decisions, or release decisions;
- source descriptors, credentials, live fetchers, scrapers, or endpoint activation;
- raw, work, quarantine, processed, catalog, triplet, or published data;
- receipts, proofs, EvidenceBundles, release manifests, correction notices, or rollback records;
- pipeline orchestration, public API routes, UI components, map styles, or generated answers;
- exact sensitive borehole, well-log, core, sample, mineral occurrence, extraction, or resource geometry in code, logs, examples, or errors;
- code that claims a candidate is true, admissible, evidence-closed, reviewed, public-safe, or released merely because a helper returned it.

Those concerns remain in their responsibility roots under `contracts/`, `schemas/`, `policy/`, `data/`, `connectors/`, `pipelines/`, `release/`, and `apps/`.

## Inputs

Future functions may accept explicit, caller-supplied values from governed pipelines, validators, tests, and synthetic fixtures. Inputs should carry the source identity and role, source-native identifiers, observation or interpretation character, spatial and temporal support, units, quality and uncertainty context, evidence references, rights and sensitivity context, policy references, and release references required by an accepted interface.

This namespace must not silently fetch a missing value, infer stronger authority from a filename or map style, or treat administrative, modeled, generated, or public-display material as observed geology.

## Outputs

Future modules may return normalized **candidates**, parsed values, candidate layer descriptors, public-safe transformation candidates, or structured validation findings for downstream gates.

An output from this namespace is not, by itself, a canonical geology object, source admission, policy decision, proof, receipt, lifecycle promotion, released artifact, exact-location permission, or public claim. No implemented output contract exists today because all three named modules are placeholders and `__init__.py` is empty.

## Validation

The following bounded commands verify the current scaffold without claiming package behavior:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=packages/domains/geology/src \
  python -c "import geology, geology.identity, geology.layers, geology.observations"

PYTHONPYCACHEPREFIX=/tmp/kfm-geology-pycache \
  python -m compileall -q packages/domains/geology/src/geology

make validate
git diff --check
```

When behavior is implemented, reviewers should add deterministic no-network tests for malformed and ambiguous inputs, source-role collapse, missing evidence, unresolved rights, sensitive or exact geometry, unsupported temporal or spatial scope, import-time side effects, and attempts to bypass contract, policy, review, or release authority.

## Review burden

Changes require the Geology package/domain steward. Add contract/schema review for typed interfaces, evidence review for claim-bearing outputs, policy and sensitivity review for borehole/resource/location behavior, and release review for public-delivery candidates.

`.github/CODEOWNERS` currently provides only the repository-wide `@kfm/maintainers` fallback for this path; a Geology-specific package owner is not declared. Placeholder owner labels above do not replace repository review policy.

Reviewers must verify that code remains inside the importable-helper boundary, any public export is intentional, exact and public-safe geometry stay distinct, and tests demonstrate behavior without promoting placeholder intent to fact.

## Related folders

- [`packages/domains/geology/`](../..): package overview and `pyproject.toml`.
- [`packages/domains/geology/src/`](..): source-root boundary and explicit reference to this README.
- [`docs/domains/geology/`](../../../../../docs/domains/geology/): human-facing Geology domain documentation.
- [`contracts/domains/geology/`](../../../../../contracts/domains/geology/): semantic-contract authority.
- [`schemas/contracts/v1/domains/geology/`](../../../../../schemas/contracts/v1/domains/geology/): machine-shape authority.
- [`policy/domains/geology/`](../../../../../policy/domains/geology/): Geology policy and sensitivity responsibility.
- [`tests/domains/geology/`](../../../../../tests/domains/geology/): current Geology-domain test scaffolds.
- [`fixtures/domains/geology/`](../../../../../fixtures/domains/geology/): current synthetic and placeholder Geology fixtures.
- [`docs/doctrine/directory-rules.md`](../../../../../docs/doctrine/directory-rules.md): placement and directory-README contract; parallel Directory Rules copies remain a repository conflict.

## ADRs

- [`ADR-0001 — schema home`](../../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) is **proposed** and identifies `schemas/contracts/v1/` as the candidate canonical schema home.

No accepted ADR inspected for this change establishes a Geology-specific Python API or transfers source, contract, schema, policy, evidence, receipt, proof, release, or public authority into this namespace.

## Rollback

This documentation-only addition is reversible by removing this README. If future code changes break callers or governance boundaries, preserve evidence and release records, revert or supersede the code change through normal review, restore the last reviewed interface, and record any required correction in the governing release lane. Do not rewrite contracts, receipts, proofs, or published history to make an implementation rollback appear clean.

## Last reviewed

2026-07-17 — repository inventory and namespace boundary reviewed at `main@1cadc7ebc81e29b863ea29fd78f4a1c7d2d23a16`; implemented helper behavior remains unverified.
