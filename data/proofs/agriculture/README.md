<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-proofs-agriculture-readme
title: data/proofs/agriculture/README.md — Agriculture Evidence and Proof Support
version: v0.2.0
type: README; proof-lane-contract; agriculture-domain-proof-index; EvidenceBundle-support; claim-scope-boundary
status: repository-grounded draft; proof payload and runtime enforcement unverified
owners: NEEDS VERIFICATION — Agriculture steward · Evidence steward · Proof steward · Aggregation reviewer · Privacy/sensitivity reviewer · Validation steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, catalog, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; evidence-first; release-gated
current_path: data/proofs/agriculture/README.md
truth_posture: >
  CONFIRMED exact path, prior blob, parent data/proofs authority contract,
  Agriculture proof-lane content, and Agriculture aggregation/privacy doctrine /
  PROPOSED domain proof-packet contract and validation expectations /
  UNKNOWN recursive payloads, active writers/consumers, runtime, release,
  hosting, and public effects / NEEDS VERIFICATION owners, accepted profiles,
  schemas, validators, fixtures, CI, emitted EvidenceBundles, correction
  propagation, cache invalidation, and rollback drills
related:
  - ../README.md
  - ../../README.md
  - ../../processed/agriculture/
  - ../../catalog/domain/agriculture/README.md
  - ../../triplets/
  - ../../published/
  - ../../receipts/
  - ../../registry/sources/agriculture/
  - ../../../docs/domains/agriculture/README.md
  - ../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../contracts/domains/agriculture/README.md
  - ../../../contracts/domains/agriculture/aggregation-receipt.md
  - ../../../policy/domains/agriculture/
  - ../../../schemas/contracts/v1/domains/agriculture/
  - ../../../release/candidates/agriculture/
  - ../../../release/
notes:
  - "This file preserves the canonical Agriculture proof lane under data/proofs/."
  - "Proof support makes claim scope, source role, integrity, limitations, and dependencies inspectable; it does not create factual truth, policy admission, release approval, or publication."
  - "EvidenceRef should resolve to EvidenceBundle where Agriculture claims depend on evidence. Missing or inconsistent closure yields HOLD, ABSTAIN, RESTRICT, DENY, or ERROR rather than plausible completion."
  - "Agriculture proof support is aggregation-aware and privacy-aware: aggregate evidence must not be promoted into field/operator truth, and protected details must not be embedded in public proof packets."
  - "Prior blob and documentation rollback target: cd1a847ff727969ca968b0963e1d48ad6b81454b."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/proofs/agriculture/` — Agriculture Evidence and Proof Support

> **One-line purpose.** Own Agriculture-domain proof packets, EvidenceBundle support, claim-scope manifests, citation/integrity closure, and limitations needed to evaluate whether Agriculture claims have sufficient governed support.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: proof support](https://img.shields.io/badge/authority-proof%20support-0969da?style=flat-square)](#authority-level)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#validation)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#sensitivity-and-aggregation-boundary)

> [!IMPORTANT]
> A proof file, resolved digest, validation pass, pull request, or merge does not make an Agriculture claim true, rights-cleared, policy-admitted, reviewed, released, or public. Proof support is one governed dependency among source, processed, catalog, triplet, receipt, policy, review, correction, rollback, and release state.

> [!WARNING]
> Field-level, operator-level, private parcel, proprietary yield, pesticide-use, FSA CLU, restricted coordinate, or harmful-threshold detail must not be embedded in ordinary public-repository proof packets. Use approved restricted systems, references, redacted summaries, or abstain.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Claim scope](#claim-scope-contract) · [Evidence closure](#evidenceref-to-evidencebundle-closure) · [Aggregation](#sensitivity-and-aggregation-boundary) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This lane supports inspectable Agriculture claims by recording or indexing the evidence, citation, integrity, validation, review, and limitation context needed to evaluate those claims.

It may support claims about `CropObservation`, `FieldCandidate`, `CropRotation`, `YieldObservation`, `IrrigationLink`, `ConservationPractice`, `SoilCropSuitability`, `AgriculturalEconomyObservation`, `SupplyChainNode`, `DroughtStressIndicator`, `PestStressIndicator`, aggregate public layers, and cross-lane Agriculture relations.

It does not replace the source record, processed artifact, catalog row, triplet, receipt, policy decision, review record, release manifest, correction notice, rollback card, or governed public payload.

## Authority level

**Canonical; Agriculture PROOFS responsibility.**

This lane may own:

- Agriculture EvidenceBundle or proof-pack instances under accepted profiles;
- EvidenceRef resolution indexes;
- claim-scope and claim-to-evidence manifests;
- citation-validation, integrity, digest-agreement, and limitation summaries;
- proof indexes for review, release, correction, rollback, governed API, and Evidence Drawer use.

It does not own object meaning, schema shape, source admission, process receipts, policy decisions, release approval, public serving, or factual truth.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/proofs/agriculture/` |
| Version | `v0.2.0` |
| Prior blob | `cd1a847ff727969ca968b0963e1d48ad6b81454b` |
| Parent contract | `data/proofs/README.md` v0.2.0 |
| Recursive proof inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Accepted EvidenceBundle profile | `NEEDS VERIFICATION` |
| Public readiness | `DENY BY DEFAULT` |

## What belongs here

- Agriculture EvidenceBundle, proof-pack, and claim-support instances conforming to an accepted profile;
- EvidenceRef-to-EvidenceBundle resolution maps;
- claim-scope manifests identifying the precise assertion, geography, time, variable, role, and confidence being supported;
- citation-validation and source-agreement summaries;
- digest-closure manifests binding evidence inputs, processed artifacts, catalog rows, triplets, proof packets, and release dependencies;
- proof limitations, caveats, conflicts, stale-state, and unresolved-evidence summaries;
- aggregate-proof packets that reference aggregation, suppression, and redaction receipts without copying protected details;
- model-proof summaries that reference model-run receipts, input digests, uncertainty, and reality-boundary notes;
- lane-local README, index, inventory, migration, and disposition sidecars.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| RAW source captures, mutable WORK candidates, or quarantined material | Their Agriculture lifecycle lanes |
| Canonical processed Agriculture objects | `data/processed/agriculture/` |
| Catalog records, STAC/DCAT/PROV records, or triplets | `data/catalog/` and `data/triplets/` |
| Process receipts such as run, transform, aggregation, redaction, model-run, validation, review, AI, or publication receipts | `data/receipts/` or the accepted receipt family |
| Release manifests, promotion decisions, correction notices, withdrawal notices, or rollback cards | `release/` |
| Source descriptors and source activation decisions | `data/registry/sources/agriculture/` |
| Contracts, schemas, policies, validators, fixtures, tests, pipelines, applications, or packages | Their responsibility roots |
| Public maps, tiles, APIs, UI payloads, downloads, or Focus Mode answers | Released governed delivery paths |
| Field/operator/private-parcel detail, protected coordinates, proprietary records, secrets, or harmful thresholds | Restricted systems or deny/abstain |

## Inputs

A proof packet may reference admitted source records, processed artifacts, catalog/triplet records, validation and citation reports, receipts, policy decisions, reviews, correction state, and release dependencies.

Inputs must preserve, where applicable:

- stable identity and content digest;
- source role and source authority;
- spatial and temporal scope;
- rights, sensitivity, and consent or restriction posture;
- contract and schema versions;
- code, spec, run, aggregation, redaction, and model lineage;
- validation, policy, review, correction, rollback, and release references.

## Outputs

Outputs are proof support for review, catalog closure, triplet interpretation, release decisions, Evidence Drawer views, governed API responses, corrections, withdrawals, and rollbacks.

An output from this lane must not be interpreted as an approval to publish or as permission for public clients to read the proof store directly.

## Claim-scope contract

Every proof packet should state exactly what it supports.

| Scope dimension | Required posture |
|---|---|
| Claim identity | Stable claim or assertion identifier; no ambiguous prose-only target. |
| Object family | Agriculture family or cross-lane relation being supported. |
| Geography | Public-safe scope plus restricted internal reference when authorized. |
| Time | Source, observed, valid, retrieval, release, correction, and supersession times where material. |
| Variable and units | Declared quantity, method, units, and transformation assumptions. |
| Source role | Observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic. |
| Confidence and limitations | Bounded support, conflicts, missing evidence, uncertainty, and fitness for use. |
| Decision dependency | Catalog, release, public layer, governed answer, correction, or rollback use being evaluated. |

A proof packet that cannot state its claim scope should fail closed.

## EvidenceRef-to-EvidenceBundle closure

Where an Agriculture claim depends on evidence, its `EvidenceRef` should resolve to an `EvidenceBundle` or accepted equivalent.

Closure should demonstrate:

1. the referenced evidence exists and is integrity-bound;
2. the evidence supports the stated claim scope rather than an adjacent or stronger claim;
3. source roles remain distinct;
4. processed, catalog, triplet, and proof identities agree where required;
5. referenced receipts and policy/review records resolve without being copied into this lane as primary authority;
6. stale, corrected, superseded, disputed, or withdrawn evidence is visible;
7. public use remains dependent on release and correction state.

Missing, conflicting, or non-resolving closure yields `HOLD`, `ABSTAIN`, `RESTRICT`, `DENY`, or `ERROR` according to the governing interface—not invented support.

## Sensitivity and aggregation boundary

Agriculture proof packets must preserve the difference between aggregate public claims and field/operator truth.

- Aggregate evidence does not support a field-level claim unless the claim scope, evidence, rights, policy, review, and release explicitly allow it.
- `AggregationReceipt` or accepted equivalent remains in the receipt lane and should be referenced by aggregate proof packets.
- Suppression, generalization, redaction, minimum-cell, and withheld-field decisions should be referenced without exposing protected parameters when those parameters could aid re-identification.
- Operator identity, private person-parcel joins, proprietary yield, pesticide detail, FSA CLU detail, and restricted coordinates remain denied or restricted by default.
- Modeled crop, stress, suitability, or yield context remains modeled evidence and must not be promoted into observed truth.
- Cross-lane claims must preserve ownership: Soil, Hydrology, Atmosphere, Hazards, Habitat, Flora/Fauna, and People/Land evidence remains owned by those lanes.

## Validation

Validation should cover:

- path and responsibility placement;
- proof profile and version;
- claim identity and scope;
- EvidenceRef resolution;
- EvidenceBundle completeness;
- source-role consistency;
- rights, sensitivity, and aggregation boundaries;
- spatial/temporal support;
- digest and identity agreement across evidence, processed, catalog, triplet, and proof artifacts;
- receipt, policy, review, release, correction, and rollback references;
- stale, conflict, withdrawal, and supersession handling;
- links, anchors, metadata, and protected-content exposure.

No complete Agriculture proof-lane validator or CI enforcement was verified. A pass proves only the declared scope of the executed check.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**.

Changes involving proof payloads, evidence-profile shape, aggregation boundaries, protected field/operator details, model-derived claims, source rights, cross-lane ownership, corrections, withdrawals, or release dependencies require the corresponding Agriculture, evidence, validation, privacy/sensitivity, policy, and release reviewers.

CODEOWNERS routing is not review evidence, and the proof author should not be treated as the sole release authority for material claims.

## Correction and rollback

When evidence, source records, processed artifacts, catalog rows, triplets, aggregation logic, or model outputs change:

1. identify affected claims and proof packets;
2. mark stale, disputed, corrected, superseded, or withdrawn evidence explicitly;
3. recompute or invalidate affected digests and agreement summaries;
4. propagate correction references to catalog, triplet, release, governed API, Evidence Drawer, indexes, caches, and published derivatives as applicable;
5. preserve predecessor/successor and correction lineage;
6. retain or reference the rollback target required by the release authority.

Reverting this README does not revert proof payloads, release state, public artifacts, or downstream caches. Those require their own governed correction or rollback procedures.

## Related folders

- Parent proof contract: [`../README.md`](../README.md)
- Processed Agriculture: [`../../processed/agriculture/`](../../processed/agriculture/)
- Agriculture catalog: [`../../catalog/domain/agriculture/README.md`](../../catalog/domain/agriculture/README.md)
- Triplets: [`../../triplets/`](../../triplets/)
- Published outputs: [`../../published/`](../../published/)
- Receipts: [`../../receipts/`](../../receipts/)
- Source registry: [`../../registry/sources/agriculture/`](../../registry/sources/agriculture/)
- Agriculture doctrine: [`../../../docs/domains/agriculture/README.md`](../../../docs/domains/agriculture/README.md)
- Contracts: [`../../../contracts/domains/agriculture/README.md`](../../../contracts/domains/agriculture/README.md)
- Policy: [`../../../policy/domains/agriculture/`](../../../policy/domains/agriculture/)
- Release candidates: [`../../../release/candidates/agriculture/`](../../../release/candidates/agriculture/)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive proof payload inventory | `NEEDS VERIFICATION` | Pinned tree, proof families, storage/LFS references, owners, rights and sensitivity |
| Accepted Agriculture EvidenceBundle/proof profile | `NEEDS VERIFICATION` | Contract/schema versions, examples, compatibility and migration rules |
| Writers and consumers | `UNKNOWN` | Pipeline, validator, catalog, release, governed API, Evidence Drawer, correction tooling |
| Validators, fixtures, and CI | `UNKNOWN` | Deterministic positive/negative cases and workflow enforcement |
| Digest and identity agreement | `UNKNOWN` | Emitted proof, processed, catalog, triplet, and release instances |
| Aggregation/redaction/model receipt linkage | `UNKNOWN` | Resolvable receipt instances without protected-detail leakage |
| Correction and withdrawal propagation | `UNKNOWN` | Dependency map, invalidation, cache/index cleanup, and drills |
| Public serving posture | `UNKNOWN` | Governed route and authorization evidence; no direct proof-store reads |

Unknowns narrow claims and block consequential transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| Agriculture EvidenceBundle and EvidenceRef role | Preserved and clarified |
| Digest closure and claim-support purpose | Preserved and strengthened |
| Receipt/proof/release separation | Preserved |
| Aggregation-aware and source-role-aware controls | Preserved and strengthened |
| Cross-lane ownership boundaries | Preserved |
| Privacy, rights, sensitivity, evidence, correction, and rollback controls | Preserved and strengthened |
| Prior blob and documentation rollback target | Recorded |
| Proof payload, data, catalog, release, route, runtime, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the Agriculture proof lane with the normalized parent `data/proofs/` contract;
- strengthened claim-scope and EvidenceRef-to-EvidenceBundle closure;
- tightened aggregation, privacy, model, source-role, correction, and rollback boundaries;
- replaced speculative directory organization with bounded verification and no-loss controls;
- changed Markdown only.

## Documentation rollback

Revert commit created by this update or restore prior blob `cd1a847ff727969ca968b0963e1d48ad6b81454b`.

[Back to top](#top)
