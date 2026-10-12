<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/time-series-promotion-candidate-manifest
title: TimeSeriesPromotionCandidateManifest Candidate Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD - Data steward; Contracts steward; Validation steward; Release steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/data/time_series_promotion_candidate_manifest.schema.json
  - ../../fixtures/contracts/v1/data/time_series_promotion_candidate_manifest/cases.json
  - ../../tools/validators/data/validate_time_series_promotion_candidate_manifest.py
  - ../../tests/validators/test_validate_time_series_promotion_candidate_manifest.py
  - ../../docs/intake/exploratory/pass-22-time-series-promotion-candidate-manifest-source-map.md
  - ../common/spec_hash.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, data, time-series, station, candidate, manifest, spec-hash, fixture]
notes:
  - "This profile records normalized candidate metadata only; it does not admit source observations or authorize promotion."
  - "All included fixtures are synthetic and perform no network, source, policy, signing, registry, or publication operation."
[/KFM_META_BLOCK_V2] -->

# TimeSeriesPromotionCandidateManifest Candidate Contract

> **Purpose.** Define a deterministic, fixture-only candidate manifest for a station time-series batch so reviewers can inspect its spatial footprint, temporal extent, station identifiers, variables, encoding, and `spec_hash` identity before any governed promotion work begins.

## Status and authority

`PROPOSED_INACTIVE`. The contract gives meaning to one candidate record. The canonical machine shape lives in `schemas/`; executable conformance lives in `tools/` and `tests/`; synthetic examples live in `fixtures/`.

A conforming record is not an `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, publication decision, or released carrier. References to those families preserve dependency boundaries and do not create their authority.

## Responsibility signature

| Axis | Value |
|---|---|
| Artifact kind | Semantic contract for a candidate manifest |
| Authority owner | Data-contract stewardship |
| Lifecycle stage | WORK/CANDIDATE metadata; no lifecycle mutation |
| Execution role | Declarative spec with repository validator |
| Scope | Shared station time-series object family |
| Exposure | Internal, synthetic fixtures only |
| Mutability | Content-addressed candidate replacement |
| Retention | Review-bound until separately governed |
| Physical storage | Git for contract and fixtures; no production payload bytes |

Directory Rules basis: meaning belongs in `contracts/data/`; canonical shape in `schemas/contracts/v1/data/`; reusable synthetic inputs in `fixtures/contracts/v1/data/`; repository-wide validation in `tools/`; executable conformance in `tests/`; read-only CI in `.github/`; and source adaptation in `docs/intake/exploratory/`.

## Required record surfaces

| Surface | Required meaning |
|---|---|
| Identity | `manifest_id`, exact profile/version, and RFC 8785 JCS plus SHA-256 `spec_hash` |
| Dataset | Digest-addressed dataset candidate reference |
| Footprint | Declared `EPSG:4326` bounding box; no geometry authority is inferred |
| Time | Inclusive UTC start and end instants with start not after end |
| Stations | Nonempty, unique, lexicographically sorted stable station identifiers |
| Variables | Nonempty, unique, lexicographically sorted variable identifiers |
| Encoding | Declared media type, storage format, compression, and record count |
| Bindings | SourceDescriptor and RunReceipt references; unresolved evidence and policy stay explicit `null` |
| Governance | Fixed candidate role, promotion required, and all evidence/policy/review/release/publication authority flags false |

## Deterministic identity

1. Remove `manifest_id` and `spec_hash` from the complete record.
2. Canonicalize the remaining JSON with RFC 8785 JCS.
3. Compute SHA-256 and encode it as `sha256:<64 lowercase hex>`.
4. Set `manifest_id` to `kfm:time-series-promotion-candidate:<first 24 digest hex characters>`.

No implicit rounding, station alias resolution, variable crosswalk, coordinate transform, or timestamp coercion occurs before hashing.

## Validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, bounded semantics, and deterministic identity are internally consistent |
| `DENY` | The candidate is shaped or bound inconsistently and must not advance |
| `ERROR` | The local input could not be read or parsed safely |

These outcomes are validator results only. `PASS` does not authorize promotion, review, release, deployment, publication, or public use.

## Explicit non-effects

The slice does not:

- fetch SensorThings, Mesonet, or any station service;
- validate scientific accuracy, station authority, physical ranges, rights, sensitivity, or source currentness;
- resolve an `EvidenceBundle`, evaluate policy, authenticate review, or close a catalog;
- create or mutate RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED state;
- sign, promote, release, deploy, publish, update an alias, or write a production receipt.

## Acceptance boundary

- Draft 2020-12 schema meta-validation passes.
- Exact synthetic case polarity is deterministic and no-network.
- Duplicate keys, non-finite numbers, unsafe links, malformed time order, noncanonical identifier arrays, invalid bounding boxes, and identity drift fail closed.
- The generated authoring receipt binds the final non-receipt artifact bytes.
- Human review remains pending.

## Rollback

Revert the additive contract slice. No runtime state, source checkpoint, release alias, published carrier, or external system requires rollback.

## Source basis

- `KFM-P22-PROG-0020`, retained unchanged in the Pass 23/32 consolidated atlas: a time-series station batch should carry footprint, time, station IDs, variables, encoding, and `spec_hash` identity.
- Accepted ADR-0029 and the adopted Directory Rules v2 establish the responsibility-root placement used by this slice.

