# Soil Watcher Specification

## Status

**PROPOSED, inactive, fixture-only.** This contract implements Pass 31 candidates `KFM-P31-IDEA-0019` and `KFM-P31-PROG-0015` as a reviewable soil-watcher lifecycle specification. It does not activate a source, permit network access, admit RAW data, execute a watcher, promote, release, or publish.

## Purpose

`SoilWatcherSpec` describes a deterministic candidate workflow for two source families that must remain semantically distinct:

| Source family | Required support type | Intended role |
|---|---|---|
| `SSURGO` | `AUTHORITATIVE_STATIC_SOIL_SURVEY` | Static survey and keyed tabular/vector evidence. |
| `GNATSGO` | `GRIDDED_DERIVATIVE_SOIL` | Gridded derivative support; never a silent replacement for SSURGO. |

The specification records source-registry placeholders, fixture-only acquisition modes, ordered pipeline phases, hard-QA rules, provider-specific materiality profiles, WORK/QUARANTINE outputs, required receipt families, and explicit non-authority flags.

## Required lifecycle

```text
LOCAL FIXTURE
  -> SNAPSHOT
  -> NORMALIZE
  -> HARD_QA
  -> MATERIALITY
  -> PACKAGE
  -> RECEIPT
  -> WORK or QUARANTINE only
```

The specification never creates a path to `RAW`, `PROCESSED`, `CATALOG`, `PUBLISHED`, source activation, or public delivery. A future live implementation requires separately reviewed SourceDescriptors, rights and sensitivity decisions, activation records, connector logic, network authorization, evidence closure, promotion controls, release records, and rollback support.

## Determinism and identity

- `watcher_id` is stable and matches the watcher-registry projection.
- `source_scope`, `qa_rules`, `materiality_rules`, `outputs`, and `receipt_expectations` are canonical and duplicate-free.
- `spec_hash` is the RFC 8785 JCS SHA-256 digest of the object with `spec_hash` omitted.
- Source roles cannot collapse: SSURGO and gNATSGO have different support types and materiality profiles.
- Unknown rights, sensitivity, source authority, schema behavior, or materiality outcomes route to `QUARANTINE`.

## Finite findings

The validator emits stable codes including:

- `SOIL_SPEC_HASH_MISMATCH`
- `SOIL_SOURCE_ROLE_INVALID`
- `SOIL_SOURCE_SCOPE_NOT_CANONICAL`
- `SOIL_PHASE_ORDER_INVALID`
- `SOIL_QA_RULES_INCOMPLETE`
- `SOIL_MATERIALITY_PROFILE_MISSING`
- `SOIL_OUTPUT_AUTHORITY_OVERREACH`
- `SOIL_WATCHER_AUTHORITY_OVERREACH`

## Directory Rules basis

Semantic meaning belongs under `contracts/domains/soil/`; machine shape under `schemas/contracts/v1/domains/soil/`; declarative watcher configuration under `pipeline_specs/watchers/`; policy under `policy/domains/soil/`; executable validation under `tools/validators/domains/soil/`; fixtures and tests under their responsibility roots; and the cross-system index remains under `control_plane/`. No new root or parallel authority is created.

## Rollback

Before merge, close the draft PR and delete its branch. After an authorized merge, revert the additive commit. The change has no live source, network schedule, RAW data, release, cache, API, map layer, or public artifact to unwind.
