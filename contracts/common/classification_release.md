<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/classification-release/v1
title: ClassificationRelease Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-only
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; no-public-authority
owning_root: contracts/
responsibility: Define the shared semantic boundary for a broad-scale classification product without collapsing it into an observation, forecast, model, policy decision, release, or public claim.
truth_posture: "CONFIRMED source/repository boundary; PROPOSED candidate semantics; NEEDS VERIFICATION steward review and any operational adoption"
related:
  - ../../schemas/contracts/v1/common/classification_release.schema.json
  - ../../fixtures/contracts/v1/common/classification_release/
  - ../../tools/validators/validate_classification_release.py
  - ../../tests/validators/test_validate_classification_release.py
  - ../../tests/cross_domain/test_classification_observation_boundary.py
  - ./condition_relation.md
  - ./temporal_authority_envelope.md
  - ../source/official_source_snapshot_candidate.md
  - ../source/official_source_snapshot_lineage_assessment.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, common, classification, source-role, temporal, lineage, deterministic, fixture-only, no-network]
notes:
  - "Implements only the ClassificationRelease half of the briefing architecture's ClassificationRelease/ObservationRecord pair."
  - "Current repository evidence already contains domain-specific DomainObservation profiles, including a closed soil/Mesonet candidate, so this slice does not create a competing shared ObservationRecord."
  - "A validator PASS proves bounded local shape and invariants only; it creates no source, evidence, policy, review, release, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

# ClassificationRelease

## Purpose

`ClassificationRelease` is a shared, release-neutral candidate for a broad-scale classification product such as a weekly drought class surface. It records **what an issuing source classified**, the source data cutoff, validity interval, retrieval time, spatial support, class vocabulary, source snapshots, evidence references, and correction or supersession lineage.

It is deliberately not:

- a station or sensor observation;
- a forecast;
- a modeled estimate;
- a parcel-level condition;
- a policy decision;
- a KFM release manifest;
- an EvidenceBundle;
- a public map or API authorization.

The briefing-to-system architecture describes a conditions lane in which classifications, observations, forecasts, modeled grids, survey products, and aggregates must remain distinct. This contract realizes only the classification carrier and proves its boundary against the repository's existing soil station-observation candidate.

## Status and authority boundary

| Field | Value |
|---|---|
| Profile | `kfm.common.classification-release.v1` |
| Adoption state | `PROPOSED_INACTIVE` |
| Execution | Fixture-only, deterministic, no-network |
| Machine schema | `schemas/contracts/v1/common/classification_release.schema.json` |
| Validator | `tools/validators/validate_classification_release.py` |
| Public use | Always `false` in this profile |
| Release state | Always semantically `UNRELEASED` |
| Reference resolution | Not performed |
| Policy/review execution | Not performed |
| Lifecycle writes | None |

A `PASS` means the local candidate is internally coherent for the tested profile. It does not prove that a referenced source, source snapshot, evidence object, geography, statistic, narrative, legend, or artifact exists or is authoritative.

## Bounded-context and anti-collapse rule

The shared classification context uses one published language:

| Concept | Required source role | Required support type |
|---|---|---|
| Classification release | `CLASSIFICATION` | `DERIVED_CLASSIFICATION` |
| Existing soil station candidate | Domain-native observation role | Domain-native station support type |

The repository already has domain-owned observation profiles. The soil profile includes a synthetic Kansas Mesonet-style station observation with `station_soil_moisture` support. This packet therefore adds a cross-domain boundary test rather than a second shared `ObservationRecord` authority.

A classification candidate must be denied when it claims `OBSERVATION`, `FORECAST`, or `MODEL` source role, when it claims direct-measurement support, or when it uses point scale as if one station represented a broad classification surface.

## Required semantic content

### Identity

- `classification_release_id` is content-derived.
- `spec_hash` uses the repository RFC 8785 JCS plus SHA-256 hashing package.
- The identity subject excludes only `classification_release_id` and `spec_hash`.
- Equivalent semantic input replays to the same identity.

### Source and authority

The candidate names:

- the product;
- the source and source-native release identity;
- the issuing authority;
- one or more immutable `OfficialSourceSnapshotCandidate` references;
- the required classification source role and support type.

Source capture is still pre-evidence. A source snapshot reference does not establish rights, truth, citation closure, or release permission.

### Time

The candidate keeps distinct:

- source data cutoff;
- source-valid start and end;
- source release;
- KFM retrieval;
- correction;
- supersession;
- source-native timezone.

The validator denies cutoff after source release, inverted validity, release after retrieval, and incoherent correction or supersession times.

### Space and scale

The candidate records:

- a governed geography reference or an explicit unresolved state;
- scale;
- geometry role;
- geometry digest;
- geometry confidence.

A point-scale candidate is denied. Unresolved geometry cannot carry a digest or resolved confidence. Resolved geometry requires a reference, digest, and non-unresolved confidence.

### Classification support

The candidate binds:

- spatial artifact references;
- aggregate-statistic references;
- legend and narrative references;
- content digests;
- evidence references;
- canonical class codes;
- explicit limitations.

These references remain unresolved in this fixture profile. The candidate does not upgrade them into evidence or release state.

### Lineage

Finite source-lineage states are:

| State | Required closure |
|---|---|
| `CURRENT` | No correction, supersession, or conflict edges |
| `CORRECTED` | `corrects` reference plus `corrected_at` |
| `SUPERSEDED` | `superseded_by` reference plus `superseded_at` |
| `CONFLICTED` | At least two conflict references and an unresolved-safe posture |

Lineage state is not KFM lifecycle or release state. Historical candidates remain addressable; the profile never deletes corrected or superseded history.

## Authority flags

Every candidate carries all-false effects:

```json
{
  "source_activated": false,
  "evidence_resolved": false,
  "policy_evaluated": false,
  "promoted": false,
  "released": false,
  "published": false
}
```

`public_use_allowed` is also `false`. Any release reference, released state, public-use claim, or true effect is denied.

## Deterministic validation

The no-network validator checks:

- closed Draft 2020-12 shape;
- duplicate-free, finite JSON;
- classification role/support;
- canonical arrays;
- non-placeholder content digests;
- temporal order;
- geography/scale coherence;
- correction, supersession, and conflict closure;
- release/public/effect non-authority;
- RFC 8785 JCS plus SHA-256 identity.

Finite validator outcomes are:

- `PASS` — bounded candidate accepted;
- `DENY` — semantic or authority boundary violated;
- `ERROR` — unsafe input, unavailable dependency, or identity corruption.

Diagnostics contain stable code/path pairs and do not echo source values.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. This packet reuses established responsibility roots:

| Responsibility | Path family |
|---|---|
| Meaning | `contracts/common/` |
| Machine shape | `schemas/contracts/v1/common/` |
| Synthetic proof inputs | `fixtures/contracts/v1/common/` |
| Executable validation | `tools/validators/` |
| Behavioral proof | `tests/validators/` and `tests/cross_domain/` |
| Read-only CI | `.github/workflows/` |
| Exploratory adaptation record | `docs/intake/exploratory/` |
| AI-authoring accountability | `data/receipts/generated/` |

No root, domain root, second observation authority, policy home, source registry, proof home, release home, or publication path is created.

## Non-effects

This profile does not:

- fetch USDM or any live source;
- activate a source or connector;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED data;
- resolve `EvidenceRef` to `EvidenceBundle`;
- evaluate rights, sensitivity, policy, or human review;
- construct a map layer, API response, alert, dashboard, or AI answer;
- approve a correction or release;
- deploy or publish.

## Compatibility and next seams

The packet is additive. Existing domain observation profiles remain authoritative for their domain candidate shapes. `ConditionRelation` remains the contextual relation carrier; it may relate a released classification and observation later, but it cannot turn one into the other or claim causality.

The next dependency-ordered conditions-lane candidates are a fixture-first `ForecastProduct`, field-level `ClaimFieldBinding`, and—only after release controls mature—a `ReleaseEvidenceIndex` and public conditions projection.

## Rollback

Before merge, abandon the patch or close its draft pull request. After an authorized merge, revert the additive packet. No live source, lifecycle object, evidence bundle, release, cache, deployment, or public artifact requires restoration.
