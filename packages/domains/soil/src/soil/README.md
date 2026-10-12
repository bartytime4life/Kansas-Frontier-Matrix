<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-soil-src-soil-readme
title: Soil Python Source Namespace
type: readme
version: v0.1
status: draft; repository-grounded; greenfield-scaffold
owners:
  - OWNER_TBD — Soil package/domain steward
  - OWNER_TBD — Validation reviewer
created: 2026-07-16
updated: 2026-10-08
policy_label: public; packages; soil; implementation; non-authoritative
path: packages/domains/soil/src/soil/README.md
truth_posture: CONFIRMED README and empty namespace at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; retired placeholder modules are absent; PROPOSED future helper behavior; earlier evidence_snapshot retained for history.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 9741610a833bc7112a1d42a766fae592baf8f1af
related:
  - ../README.md
  - ../../README.md
  - ../../pyproject.toml
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../contracts/domains/soil/README.md
  - ../../../../../schemas/contracts/v1/domains/soil/
  - ../../../../../policy/domains/soil/
  - ../../../../../tests/domains/soil/
  - ../../../../../fixtures/domains/soil/
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, soil, python, package, source-namespace, greenfield]
notes:
  - "This README records the namespace as found; it does not claim that placeholder modules implement behavior."
  - "Only importable Soil helper code belongs here; authority-bearing records remain in their governing roots."
owning_root: packages/
responsibility: Explain the soil Python namespace, current absence of a supported API, and safe implementation handoffs.
[/KFM_META_BLOCK_V2] -->

## Source namespace guide — 2026-10-08

At `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`, this namespace retains its README and empty `__init__.py`. It does not expose a supported domain API. The removed `identity.py`, `layers.py` and `observations.py` files described in the historical text below must not be imported or recreated solely to satisfy an old example.

### Where to work now

Use the [domain guide](../../../../../docs/domains/soil/README.md) for meaning and the [validator lane](../../../../../tools/validators/domains/soil/README.md) for current bounded executable profiles. Follow [domain tests](../../../../../tests/domains/soil/README.md) to the actual assertions before selecting a test command. An empty namespace import cannot validate a source record or prove a working library.

A future reusable helper belongs here only when its inputs, outputs, consumers and dependency contract are clear. Keep acquisition/network side effects in the owning operator or connector; keep schema shape, policy, lifecycle data and release decisions in their existing roots. Begin with a caller-supplied deterministic case and a meaningful rejected case. Document the actual exported API and supported versions when implemented.

### Review and recovery

If a consumer still imports one of the retired modules, identify that consumer and its intended behavior before editing. Fix the caller or introduce a reviewed implementation; do not restore a placeholder that merely makes import succeed. Preserve the historical notes below as an earlier inventory, not current executable capability.

# Soil Python Source Namespace

> [!NOTE]
> **2026-09-29:** the unreferenced placeholder files `src/soil/identity.py`, `src/soil/layers.py` and `src/soil/observations.py` were removed from `packages/domains/soil/` in [#4792](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4792). None was executable or authoritative. Evidence notes and prose below that describe their contents record the earlier snapshot.

`packages/domains/soil/src/soil/` is the importable-code boundary for the `kfm-domain-soil` package. The current package is a `0.0.0` greenfield scaffold, not an implemented library.

## Purpose

This folder owns future reusable Python helpers for the Soil domain. Helpers may transform or validate caller-supplied candidates, but they must not become an authority for soil truth, policy, evidence, lifecycle state, or release.

## Authority level

**Implementation-bearing boundary; currently a non-functional greenfield scaffold.**

The namespace may implement accepted contracts and schemas. It does not define them, approve inputs, make policy decisions, close evidence, or authorize publication.

## Status

**CONFIRMED scaffold / UNKNOWN runtime behavior.** The bounded inventory at `main@9741610a833bc7112a1d42a766fae592baf8f1af` is:

| File | Repository evidence | Implemented behavior |
| --- | --- | --- |
| `__init__.py` | Empty file | None; no exports or public API are declared. |
| `identity.py` (removed 2026-09-29) | One line: greenfield identity-normalization placeholder | None. |
| `layers.py` (removed 2026-09-29) | One line: greenfield layer-descriptor placeholder | None. |
| `observations.py` (removed 2026-09-29) | One line: greenfield observation-parsing placeholder | None. |

`packages/domains/soil/pyproject.toml` declares package name `kfm-domain-soil` and version `0.0.0`; it does not declare dependencies or a build backend. Imports, packaging, consumers, test results, CI wiring, and production behavior remain **UNKNOWN**.

## What belongs here

- importable, deterministic Soil helper modules;
- identity normalization that preserves source-native identifiers and ambiguity;
- candidate observation parsing that preserves source, units, timestamps, depth, and quality context;
- candidate layer-description helpers that preserve evidence and release references supplied by callers;
- small internal value objects and explicit result types needed by those helpers;
- package-local documentation describing implemented interfaces.

Any future code must keep source values and governance references visible, avoid hidden I/O, and return explicit failures instead of inventing missing facts.

## What does NOT belong here

- semantic contracts or JSON Schemas;
- executable policy or sensitivity rules;
- source descriptors, credentials, fetchers, or admission decisions;
- raw, work, quarantine, processed, catalog, triplet, or published data;
- receipts, proofs, EvidenceBundles, release manifests, correction notices, or rollback records;
- pipeline orchestration, public API routes, UI components, or map styles;
- code that claims an observation is true, admissible, evidence-closed, reviewed, or released;
- import-time network access, filesystem/database writes, secret loading, or publication side effects.

Those concerns belong to their responsibility roots under `contracts/`, `schemas/`, `policy/`, `data/`, `pipelines/`, `release/`, and `apps/`.

## Inputs

Future functions may accept explicit, caller-supplied values from governed pipelines, validators, tests, and synthetic fixtures. Inputs should carry the source identity, support type, native identifiers, units, temporal context, quality flags, evidence references, policy context, and release references required by the accepted interface.

This namespace must not silently fetch a missing value or infer authority from a filename, import path, or UI state.

## Outputs

Future modules may return normalized **candidates**, parsed values, candidate layer descriptors, or structured validation findings for downstream gates. An output from this namespace is not, by itself, a canonical soil object, policy decision, proof, receipt, lifecycle promotion, released artifact, or public claim.

No output contract exists today because all three named modules are placeholders and `__init__.py` is empty.

## Validation

The following are review commands, not claims that this README or the current scaffold has passed them:

```bash
python -m compileall packages/domains/soil/src/soil
python -m pytest tests/domains/soil -q
python tools/validators/_common/run_all.py
git diff --check
```

When behavior is implemented, reviewers should also require tests for malformed and ambiguous inputs, preservation of native identifiers and units, no-network operation, import-time side effects, and attempts to bypass contract, policy, evidence, or release authority.

## Review burden

Changes require the Soil package/domain steward and a reviewer for every authority surface the change consumes: contract/schema, policy/sensitivity, evidence, or release. `.github/CODEOWNERS` currently provides only the repository-wide `@kfm/maintainers` fallback for this path; a Soil-specific owner is not declared.

Reviewers must verify that code remains inside the importable-helper boundary, that any public export is intentional, and that tests demonstrate behavior without promoting placeholder intent to fact.

## Related folders

- [`packages/domains/soil/`](../../README.md): package overview and `pyproject.toml`.
- [`packages/domains/soil/src/`](../README.md): source-root boundary.
- [`docs/domains/soil/`](../../../../../docs/domains/soil/): human-facing Soil domain documentation.
- [`contracts/domains/soil/`](../../../../../contracts/domains/soil/): semantic contract authority.
- [`schemas/contracts/v1/domains/soil/`](../../../../../schemas/contracts/v1/domains/soil/): machine-shape authority.
- [`policy/domains/soil/`](../../../../../policy/domains/soil/): Soil policy authority.
- [`tests/domains/soil/`](../../../../../tests/domains/soil/): current Soil-domain tests.
- [`fixtures/domains/soil/`](../../../../../fixtures/domains/soil/): current Soil-domain fixtures.
- [`docs/doctrine/directory-rules.md`](../../../../../docs/doctrine/directory-rules.md): placement and README contract.

## ADRs

- [`ADR-0001 — schema home`](../../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) is **proposed** and identifies `schemas/contracts/v1/` as the candidate canonical schema home.

No accepted ADR inspected for this change establishes a Soil-specific Python API or transfers contract, schema, policy, evidence, or release authority into this namespace.

## Rollback

This documentation-only addition is reversible by removing this README. If future code changes break callers, preserve evidence and release records, revert or supersede the code change through normal review, restore the last reviewed interface, and record any required correction in the governing release lane. Do not rewrite contracts, receipts, proofs, or published history to make an implementation rollback appear clean.

## Last reviewed

2026-07-16 — repository inventory and boundary reviewed; implementation and validation results remain unverified.
