<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/packages-temporal-src-readme
title: Temporal package source README
type: readme
version: v1.1
status: draft
owners: OWNER_TBD - Temporal steward - Package steward - Validation steward
created: NEEDS_VERIFICATION
updated: 2026-07-21
policy_label: internal
related:
  - packages/temporal/README.md
  - packages/temporal/src/temporal/README.md
  - contracts/common/temporal_window.md
  - schemas/contracts/v1/common/temporal_window.schema.json
  - tools/validators/validate_temporal_window.py
  - docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md
  - docs/doctrine/time-aware.md
tags: [kfm, packages, temporal, source, time-aware, validation]
notes:
  - "v1.1 replaces speculative files, imports, outcomes, and runtime claims with repository-grounded status."
  - "The source envelope contains a greenfield Python module placeholder and exposes no confirmed runtime API."
  - "Temporal vocabulary remains PROPOSED / CONFLICTED across the current schema, proposed ADR-0014, and draft doctrine."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Temporal package source

Source-code envelope for the KFM temporal package, currently present as a greenfield Python scaffold.

> [!IMPORTANT]
> - **Document status:** draft
> - **Authority level:** implementation-bearing source envelope
> - **Implementation status:** `CONFIRMED` placeholder; no runtime helper API is implemented
> - **Vocabulary posture:** `PROPOSED / CONFLICTED`
> - **Public path:** none; public clients use governed interfaces and released artifacts

## Purpose

`packages/temporal/src/` holds source files for the reusable temporal package declared by `packages/temporal/pyproject.toml`.

The folder may eventually contain implementation code for accepted temporal contracts. It does not define temporal meaning, schema shape, policy outcomes, evidence authority, lifecycle state, or release state.

## Authority level

**Implementation-bearing source envelope.**

Directory Rules places shared reusable library code under `packages/`. This README preserves the existing path and creates no new responsibility root, lifecycle phase, or parallel contract, schema, policy, receipt, proof, or release authority.

## Status

| Claim | Status | Evidence |
|---|---|---|
| The source envelope and Python namespace exist. | `CONFIRMED` | Direct reads of this README and `src/temporal/`. |
| The project is named `kfm-temporal` at version `0.0.0`. | `CONFIRMED` | [`pyproject.toml`](../pyproject.toml). |
| A public or internal helper API is implemented. | `UNKNOWN` / not established | [`__init__.py`](./temporal/__init__.py) is empty and [`core.py`](./temporal/core.py) is comment-only. |
| The temporal vocabulary is settled. | `PROPOSED / CONFLICTED` | The schema, proposed ADR-0014, and draft doctrine use non-equivalent vocabularies. |
| Package-local tests, fixtures, consumers, and CI coverage exist. | `NEEDS VERIFICATION` | No package-local test command or test configuration is declared by the inspected package metadata. |

This README does not promote the package from scaffold to functional implementation.

## What belongs here

Currently confirmed:

- this source-envelope README;
- the `temporal/` Python namespace;
- module documentation tied to the actual namespace;
- Python implementation files subordinate to accepted contracts and schemas.

Future additions may include reusable temporal value objects, parsers, serializers, interval operations, comparison helpers, and low-level validation support after their vocabulary and behavior are accepted and tested.

## What does NOT belong here

| Excluded responsibility | Correct authority or home |
|---|---|
| Temporal field meaning and semantic invariants | [`contracts/`](../../../contracts/README.md) |
| JSON Schema fields, formats, and enum authority | [`schemas/contracts/v1/`](../../../schemas/contracts/v1/README.md) |
| Allow, deny, restrict, redact, freshness, or publication decisions | [`policy/`](../../../policy/README.md) |
| Repository-wide validator entry points | [`tools/validators/`](../../../tools/validators/README.md) |
| Lifecycle records and artifacts | The correct lane under [`data/`](../../../data/README.md) |
| Evidence bundles, receipts, proofs, or audit records | Their governed lanes under `data/` |
| Release, correction, withdrawal, or rollback authority | [`release/`](../../../release/README.md) |
| Deployable API routes or UI surfaces | The appropriate governed application root |
| Source fetching or admission logic | The appropriate connector or pipeline root |
| AI-generated dates presented as canonical truth | Nowhere; generated interpretations remain evidence-subordinate and review-bound |

Do not place secrets, restricted payloads, precise protected locations, living-person data, or genomic material in examples or fixtures here.

## Inputs

### Current input interface

No runtime input interface is confirmed. The namespace exports no inspected symbols and the only inspected implementation file is a placeholder.

### Future input boundary

If implementation is approved, inputs should be explicit contract-shaped values plus versioned configuration required by the accepted temporal vocabulary. This source tree must not fetch missing facts or infer unknown dates as truth.

Inputs must preserve, when required by the controlling contract:

- temporal kind or dimension;
- original value and precision;
- timezone or calendar context;
- uncertainty, open, unknown, and not-applicable states;
- correction and supersession lineage;
- owning record or evidence identity.

## Outputs

### Current output interface

No runtime output, package export, validator result, receipt, proof, or public response is confirmed.

### Future output boundary

Future outputs may be deterministic values or finite local validation results. They must not be represented as proof of temporal truth, evidence closure, a policy decision, release approval, correction closure, rollback approval, or a public response envelope.

Schema validity proves shape only. Parsing success proves syntax only. Evidence, policy, review, and release checks remain separate.

## Validation

### Current validation state

| Check | Outcome | Evidence boundary |
|---|---|---|
| Package identity | `CONFIRMED` | `kfm-temporal`, version `0.0.0`. |
| Namespace export surface | `CONFIRMED empty` | [`__init__.py`](./temporal/__init__.py). |
| Core implementation | `CONFIRMED placeholder` | [`core.py`](./temporal/core.py) contains one greenfield-placeholder comment. |
| Module boundary documentation | `CONFIRMED` | [`temporal/README.md`](./temporal/README.md). |
| Common temporal schema | `CONFIRMED file; PROPOSED status` | [`temporal_window.schema.json`](../../../schemas/contracts/v1/common/temporal_window.schema.json). |
| Declared temporal validator | `CONFIRMED placeholder` | [`validate_temporal_window.py`](../../../tools/validators/validate_temporal_window.py) raises `NotImplementedError`. |
| Package-local runtime tests | `NOT RUN / not established` | No package-local test command is declared by the inspected metadata. |

Before calling this source tree functional:

- [ ] accept or explicitly version a controlling temporal vocabulary;
- [ ] define package build configuration, supported Python versions, dependencies, and package discovery;
- [ ] implement and document actual exports;
- [ ] add valid and invalid fixtures for supported temporal kinds and boundaries;
- [ ] test ordering, overlap, adjacency, timezone/calendar handling, uncertainty, correction, and supersession;
- [ ] implement the repository validator beyond `NotImplementedError`;
- [ ] prove deterministic behavior and governed public-boundary use.

Do not invent a package test command until repository tooling defines one.

## Review burden

[`CODEOWNERS`](../../../.github/CODEOWNERS) routes `packages/` changes to `@bartytime4life`.

That route is review metadata only. It does not prove temporal stewardship, independent approval, policy review, release approval, or separation of duties. Functional changes need the appropriate contract, schema, validation, policy, security, sensitivity, and release reviewers.

## Related folders

| Path | Relationship | Current posture |
|---|---|---|
| [`packages/README.md`](../../README.md) | Canonical shared-library root guidance. | `CONFIRMED` |
| [`packages/temporal/README.md`](../README.md) | Package-level orientation. | `CONFIRMED` thin scaffold |
| [`packages/temporal/src/temporal/`](./temporal/README.md) | Python namespace and module boundary. | `CONFIRMED` placeholder |
| [`contracts/common/temporal_window.md`](../../../contracts/common/temporal_window.md) | Semantic contract for the common temporal window. | `CONFIRMED` draft |
| [`temporal_window.schema.json`](../../../schemas/contracts/v1/common/temporal_window.schema.json) | Current machine shape and six-value `time_kind` enum. | `CONFIRMED` file; metadata says `PROPOSED` |
| [`validate_temporal_window.py`](../../../tools/validators/validate_temporal_window.py) | Declared repository validator. | `CONFIRMED` placeholder |
| [`time-aware.md`](../../../docs/doctrine/time-aware.md) | Draft time-awareness doctrine. | `CONFIRMED` file; vocabulary not reconciled |
| [`DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) | Repository drift register. | No temporal-specific resolution is claimed here |

## ADRs

- [ADR-0014](../../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md) is `proposed`; its vocabulary is not an accepted package contract.
- [ADR-0001](../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) is `proposed`. Directory Rules independently separates `schemas/` machine-shape authority from `packages/` implementation.
- This documentation-only update adds no root, changes no authority boundary, and triggers no new ADR.

## Last reviewed

- Date: 2026-07-21
- Repository: `bartytime4life/Kansas-Frontier-Matrix`
- Evidence snapshot: `main@eac8668ca9786773fcb015f9ba099e0e1dadeb35`
- Target baseline blob: `24c8a50d79f859ef3d01d4270bfa589c50cdfa29`
- Runtime execution: not performed; repository content was inspected through the GitHub connector
- Human review: pending

## Current implementation inventory

```text
packages/temporal/
|-- pyproject.toml
`-- src/
    |-- README.md
    `-- temporal/
        |-- README.md
        |-- __init__.py
        `-- core.py
```

| File | Confirmed state |
|---|---|
| [`pyproject.toml`](../pyproject.toml) | Project `kfm-temporal`, version `0.0.0`; no build backend, Python requirement, dependencies, entry point, or package-local test configuration is declared. |
| [`temporal/__init__.py`](./temporal/__init__.py) | Empty; no confirmed exports. |
| [`temporal/core.py`](./temporal/core.py) | One comment only; no parser, value object, interval operation, comparison, or validator is implemented. |
| [`temporal/README.md`](./temporal/README.md) | Repository-grounded module boundary and open verification record. |

This is an inventory of directly inspected and indexed files, not proof that a concurrently added or unindexed file cannot exist.

## Temporal vocabulary conflict

| Surface | Vocabulary | Authority state |
|---|---|---|
| [`temporal_window.schema.json`](../../../schemas/contracts/v1/common/temporal_window.schema.json) | `observed`, `published`, `ingested`, `effective`, `corrected`, `superseded` | Checked-in schema with `x-kfm.status: PROPOSED` |
| [ADR-0014](../../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md) | `source_time`, `observed_time`, `ingested_time`, `decision_time`, `published_time`, `retraction_time` | Proposed decision |
| [`time-aware.md`](../../../docs/doctrine/time-aware.md) | Source, observed, valid, retrieval, release, correction, and transaction time | Draft doctrine |

Until an accepted decision reconciles them:

1. Do not hard-code a new canonical enum here.
2. Do not silently translate between vocabularies.
3. Treat crosswalks as explicit, versioned, reviewable data.
4. Keep schema acceptance separate from semantic correctness and policy permission.

The current schema requires `start`, `end`, and `time_kind`, rejects additional top-level properties, and uses JSON Schema `date-time` for both endpoints. It does not establish interval ordering, inclusivity, open intervals, timezone normalization, uncertainty, calendar handling, freshness, or bitemporal behavior.

## Trust boundaries

Future implementation must preserve:

1. Different kinds of time remain semantically distinct.
2. Unknown, approximate, open, and not-applicable states are not replaced with magic dates.
3. Corrections and supersessions add auditable history rather than erasing prior facts.
4. Package helpers do not bypass the lifecycle spine:

   ```text
   RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
   ```

5. Public clients receive temporal claims through governed interfaces and released artifacts.
6. EvidenceBundle support outranks generated language or local helper output.
7. Identical inputs, configuration, vocabulary version, and timezone/calendar rules produce deterministic results.

## Change, correction, and rollback

For behavior changes, update contracts, schemas, fixtures, validators, tests, compatibility, and rollback documentation together as their responsibilities require. Preserve provenance and correction lineage for affected released artifacts.

For this documentation-only update, rollback is a transparent revert of the README commit and its generated receipt. No executable behavior changes.

## Evidence limits and open verification

- **NEEDS VERIFICATION:** controlling vocabulary and any migration or crosswalk;
- **NEEDS VERIFICATION:** interval, timezone, calendar, precision, uncertainty, and bitemporal semantics;
- **NEEDS VERIFICATION:** package build configuration, Python versions, dependencies, exports, tests, CI, and consumers;
- **NEEDS VERIFICATION:** policy behavior for stale, corrected, superseded, embargoed, or evidence-incomplete claims;
- **OWNER_TBD:** temporal, package, schema, validation, and documentation stewardship.

<p align="right"><a href="#top">Back to top</a></p>
