<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-hazards-readme
title: data/processed/hazards/README.md — Hazards Processed Data README
version: v0.2.0
type: readme; data-lifecycle-domain-lane; processed-stage-guide; hazards-domain-root; not-for-life-safety-lane-index
status: repository-grounded draft; PROPOSED lane contract; runtime and payload enforcement unverified
owners: NEEDS VERIFICATION — Hazards steward · Source-role steward · Freshness steward · Sensitivity reviewer · Rights steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; not-for-life-safety; no-direct-public-path; source-role-preserved; freshness-aware; release-gated
tags: [kfm, data, processed, hazards, hazard-event, warning-context, advisory-context, freshness, expiry, stale-state, source-role, evidence, correction, rollback]
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/PRESERVATION_MATRIX.md
  - ../../../docs/domains/hazards/MISSING_OR_PLANNED_FILES.md
  - ../../../policy/domains/hazards/
  - ../../../policy/release/hazards/
  - ../../../policy/sensitivity/hazards/
  - ../../../contracts/domains/hazards/
  - ../../../schemas/contracts/v1/domains/hazards/
  - ../../raw/hazards/
  - ../../work/hazards/
  - ../../quarantine/hazards/
  - ../../catalog/domain/hazards/
  - ../../triplets/
  - ../../published/
  - ../../proofs/
  - ../../receipts/
  - ../../registry/sources/hazards/
  - ../../../release/candidates/hazards/
notes:
  - "This file preserves the existing path and document identity while aligning the lane to the current data/processed authority contract."
  - "This lane owns normalized hazard candidates and context, not source captures, catalog records, proof closure, policy decisions, release authority, public serving, emergency alerting, or life-safety guidance."
  - "Warning, watch, and advisory records are contextual only and must preserve issue, effective, expiry, retrieval, correction, supersession, freshness, and official-source referral state."
  - "Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic source roles are not interchangeable."
  - "Prior blob and rollback target: dbb3bd830d004f1d2df3db7d4902c3419823804c."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/hazards/` — Hazard Context Candidates

> **One-line purpose.** Own normalized, source-traced, time-aware hazard candidates that have passed applicable WORK checks but have not thereby become cataloged, released, public, current operational guidance, or life-safety authority.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Boundary: not for life safety](https://img.shields.io/badge/boundary-NOT%20FOR%20LIFE%20SAFETY-d1242f?style=flat-square)](#not-for-life-safety-boundary)
[![Freshness: explicit](https://img.shields.io/badge/freshness-explicit-1a7f37?style=flat-square)](#freshness-and-time-state)

> [!IMPORTANT]
> Directory placement, a successful transform, a validated timestamp, a rendered map, a pull request, or a merge does not create truth, evidence closure, policy permission, catalog admission, release approval, current-warning status, or KFM publication.

> [!CAUTION]
> KFM is not an emergency alert system. Warning, watch, and advisory records may be preserved only as contextual evidence with explicit time state and official-source referral. This lane must never issue emergency instructions, evacuation guidance, driving-safety direction, operational response orders, or life-safety advice.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Source roles](#source-role-contract) · [Freshness](#freshness-and-time-state) · [Life-safety boundary](#not-for-life-safety-boundary) · [Sensitivity](#sensitivity-and-cross-domain-joins) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Children](#current-bounded-child-lane-index) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This is the canonical Hazards segment under the `data/processed/` responsibility root. It owns normalized hazard-event, observation, warning-context, advisory-context, declaration, flood, wildfire, smoke, drought, earthquake, heat/cold, exposure, resilience, timeline, and impact-area candidates that have passed applicable processing checks.

The lane exists to preserve inspectable hazard context while keeping every artifact upstream of catalog closure, proof closure, policy admission, release approval, public serving, and operational alerting.

## Authority level

**Canonical PROCESSED responsibility; non-public and not-for-life-safety by default.**

This path may own normalized tables, vectors, rasters, timelines, context records, uncertainty sidecars, freshness state, and lane-local explanatory manifests. It does not own:

- source-native captures or original alert payloads;
- object meaning or machine shape;
- source-registry authority;
- policy, sensitivity, or release decisions;
- EvidenceBundle or proof authority;
- catalog, triplet, release, or publication decisions;
- public API, UI, map, tile, AI, export, or notification behavior;
- emergency alerting, life-safety advice, or official warning issuance.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/hazards/README.md` |
| Version | `v0.2.0` |
| Prior blob | `dbb3bd830d004f1d2df3db7d4902c3419823804c` |
| Parent authority | `data/processed/README.md` |
| Recursive payload inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Current alerting behavior | `DENIED BY DOCTRINE` |
| Public readiness | `DENY BY DEFAULT` |

**CONFIRMED:** the target exists; the parent processed lane is non-public; Hazards doctrine forbids KFM-as-alert-authority; source-role and freshness boundaries are required.

**PROPOSED:** the lane-specific input, output, validation, child-lane, review, correction, and rollback expectations below.

**NEEDS VERIFICATION:** recursive payloads, owners, accepted schemas and contracts, validators, fixtures, workflows, source descriptors, receipts, EvidenceBundles, policy decisions, access controls, release links, governed routes, cache invalidation, and rollback drills.

## What belongs here

- normalized `HazardEvent` and `HazardObservation` candidates with stable identity and source trace;
- warning, watch, and advisory context with issue, effective, expiry, retrieval, correction, supersession, and freshness state;
- disaster declarations preserved as administrative or regulatory context rather than observed-event proof;
- flood, wildfire, smoke, drought, earthquake, heat/cold, severe-weather, exposure, resilience, timeline, and impact-area candidates with explicit source role;
- processed-local digests, uncertainty, limitations, freshness, identity, and derivation sidecars;
- generalized or restricted public-candidate derivatives that remain catalog- and release-gated;
- local README, inventory, migration, disposition, and correction notes that explain this lane without becoming policy, proof, or release authority.

## What does NOT belong here

| Do not place or do here | Correct home or action |
|---|---|
| Source-native feeds, CAP/XML/JSON payloads, agency messages, original rasters/vectors, logs, and raw identifiers | `data/raw/hazards/` |
| Mutable transforms, source-role experiments, freshness tests, geometry repair, temporal joins, model tuning, notebooks, and scratch outputs | `data/work/hazards/` |
| Expired-as-current records, unknown source role, unresolved rights, ambiguous identity, harmful precision, unsafe infrastructure detail, or disputed hazard material | `data/quarantine/hazards/` |
| Catalog records and graph projections | `data/catalog/` and `data/triplets/` |
| Proofs, receipts, source registry, policy, schemas, validators, and release records | Their canonical responsibility roots |
| Released public-safe bytes | `data/published/` after governed release |
| Emergency alerts, evacuation or shelter instructions, driving guidance, dispatch decisions, incident command, engineering certification, medical advice, or operational directives | Official authorities and governed operational systems; never this lane |
| Direct public API, UI, tile, map, export, notification, or Focus Mode output | Governed published and delivery interfaces only |

## Inputs

Governed WORK products or structured quarantine exits with, as applicable:

- stable artifact and source identity;
- source role and source lineage;
- source, observed/event, issue, effective, valid, expiry, retrieval, release, correction, and supersession times;
- rights, sensitivity, precision, and public-safety posture;
- contract/schema version references;
- transform, model-run, validation, freshness, redaction/generalization, and policy receipts;
- uncertainty, limitations, stale-state, and fitness-for-use disclosures;
- correction and rollback references.

An input that cannot establish required role, time state, rights, sensitivity, or identity fails closed to WORK or QUARANTINE.

## Outputs

Bounded outputs are candidates for:

- domain catalog and STAC/DCAT/PROV projection;
- EvidenceBundle assembly and triplet projection;
- policy and release-candidate review;
- public-safe derivative preparation after generalization or redaction;
- correction, supersession, historical-state, or withdrawal workflows.

PROCESSED output is not a current alert, public warning, release approval, or public-serving artifact. Public clients must not read this lane directly.

## Source-role contract

Every artifact must preserve the role assigned at admission. Promotion does not upgrade or blur source role.

| Source role | What it may represent | Must not be presented as |
|---|---|---|
| `observed` | measured or detected event/condition evidence | regulatory designation, forecast, or administrative decision |
| `regulatory` | official mapped or declared regulatory context | direct observation or modeled prediction |
| `modeled` | simulation, forecast, trajectory, probability, or estimated field | observed fact or official warning issuance |
| `aggregate` | summarized or rolled-up context | per-place or per-person truth without support |
| `administrative` | declaration, jurisdictional, program, or response-status context | observed hazard proof by itself |
| `candidate` | unconfirmed detection, inferred transition, or review candidate | confirmed event or authoritative state |
| `synthetic` | test, demonstration, or generated material | real hazard evidence or public operational state |

Hazard terms such as event, observation, detection, forecast, warning, advisory, declaration, exposure, impact, and resilience are not interchangeable.

## Freshness and time state

Time-sensitive hazard context must make temporal meaning explicit. At minimum, distinguish the times that materially apply:

- source publication or source update time;
- observed or event time;
- issue time;
- effective or valid-from time;
- expiry or valid-through time;
- retrieval time;
- processing time;
- release time;
- correction, supersession, withdrawal, or cancellation time.

| Time-state condition | Required posture |
|---|---|
| Before effective time | Mark pending or not-yet-effective; never current by implication |
| Within a verified validity window | Context may be described as source-current only when policy and source checks allow |
| Expired | Historical/expired context or deny as current state |
| Superseded or corrected | Resolve successor/correction and prevent stale-current presentation |
| Withdrawn or cancelled | Mark withdrawn/cancelled and block current-state use |
| Missing or ambiguous validity | Fail closed; do not infer current status |
| Source unavailable or freshness unverified | Narrow the claim, mark freshness unknown, and redirect to official sources |

A warning or advisory that has passed expiry must never remain visible as a live warning state because it still exists in storage or cache.

## Not-for-life-safety boundary

The following invariant is permanent:

> **KFM may explain hazard context; it must not become the alert authority.**

Any downstream public candidate requires all applicable controls, including:

- explicit not-for-life-safety language;
- official-source referral suitable to the hazard type;
- source role and current freshness state;
- issue, effective, expiry, supersession, and correction state;
- evidence and policy support;
- public-safe geometry and sensitivity controls;
- release state, correction path, cache/invalidation plan, and rollback target.

AI-generated summaries must be evidence-bounded and must abstain or redirect when current operational status cannot be verified. They must not transform contextual records into personal action instructions.

## Sensitivity and cross-domain joins

Hazards may join to Hydrology, Atmosphere, Settlements/Infrastructure, Roads/Rail/Trade, Agriculture, Geology, Habitat, Fauna, Flora, People/Land, and other lanes. A join does not transfer ownership or create new truth.

Fail closed, restrict, generalize, or deny when a join could expose:

- sensitive infrastructure or operational vulnerabilities;
- exact private residences, facilities, shelters, access routes, or responder locations;
- rare-species, rare-plant, archaeological, or other protected locations;
- person-level exposure or health information;
- parcel, ownership, operator, or private-well detail;
- harmful combinations of otherwise public datasets.

Hydrology owns canonical gauge and water-network truth; Atmosphere owns canonical air and weather observations; Infrastructure owns canonical asset identity; Roads/Rail/Trade owns network and closure truth. Hazards may reference those facts only through governed relationships.

## Validation

Validate at least the following when applicable:

1. path placement and lifecycle state;
2. stable identity, digest, version, and predecessor/successor links;
3. source identity, source role, and source lineage;
4. object-family distinction and anti-collapse rules;
5. spatial scope, geometry validity, precision, and sensitivity;
6. all material time fields and freshness/expiry logic;
7. rights, terms, and reuse posture;
8. schema/contract references and validator scope;
9. transform, model-run, freshness, redaction, validation, and policy receipts;
10. evidence references and downstream EvidenceBundle resolvability;
11. catalog/triplet identity parity;
12. not-for-life-safety disclaimer and official-source redirect dependencies;
13. correction, supersession, withdrawal, cache invalidation, and rollback dependencies;
14. negative cases for expired-as-current, modeled-as-observed, declaration-as-event-proof, candidate-as-confirmed, and restricted-precision exposure.

No complete lane-wide validator was verified. A successful check proves only its declared scope.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Review should include Hazards, data, evidence, validation, policy, sensitivity, freshness, and release expertise as applicable.

Independent specialist review is required before changes involving:

- current warning/advisory/watch presentation;
- expiry, freshness, correction, supersession, or withdrawal behavior;
- sensitive infrastructure or person-level exposure joins;
- source activation or rights posture;
- public geometry, API/UI behavior, notifications, or caching;
- release, correction, or rollback state.

CODEOWNERS routing, CI success, or documentation approval is not evidence of operational or release approval.

## Correction and rollback

Corrections must identify the affected artifact, claim, time window, source, downstream derivatives, catalog/triplet entries, public releases, caches, and AI/search indexes where applicable.

A correction should preserve:

- predecessor and successor identity;
- reason and evidence for the correction;
- corrected issue/expiry/freshness state;
- invalidation targets;
- review and release disposition;
- rollback target.

Rollback for this documentation change is the prior blob `dbb3bd830d004f1d2df3db7d4902c3419823804c`. Operational rollback behavior remains **NEEDS VERIFICATION** and must not be inferred from this README.

## Related folders

- Parent processed contract: [`../README.md`](../README.md)
- Data root: [`../../README.md`](../../README.md)
- Domain doctrine: [`../../../docs/domains/hazards/README.md`](../../../docs/domains/hazards/README.md)
- Publication boundary: [`../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`](../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md)
- Preservation matrix: [`../../../docs/domains/hazards/PRESERVATION_MATRIX.md`](../../../docs/domains/hazards/PRESERVATION_MATRIX.md)
- Lifecycle siblings: [`../../raw/hazards/`](../../raw/hazards/) · [`../../work/hazards/`](../../work/hazards/) · [`../../quarantine/hazards/`](../../quarantine/hazards/)
- Downstream: [`../../catalog/domain/hazards/`](../../catalog/domain/hazards/) · [`../../triplets/`](../../triplets/) · [`../../published/`](../../published/)
- Trust support: [`../../proofs/`](../../proofs/) · [`../../receipts/`](../../receipts/) · [`../../registry/sources/hazards/`](../../registry/sources/hazards/)
- Authority: [`../../../contracts/domains/hazards/`](../../../contracts/domains/hazards/) · [`../../../schemas/contracts/v1/domains/hazards/`](../../../schemas/contracts/v1/domains/hazards/) · [`../../../policy/domains/hazards/`](../../../policy/domains/hazards/) · [`../../../release/candidates/hazards/`](../../../release/candidates/hazards/)

## Current bounded child-lane index

The prior README listed the following child lanes. Their presence, payloads, writers, validators, and release state remain **NEEDS VERIFICATION**; omission is not retirement.

| Lane | Object or context family | Non-negotiable boundary |
|---|---|---|
| `events/` | `HazardEvent` | Historical/observed context, not emergency instruction |
| `observations/` | `HazardObservation` | Observation is not regulatory/model/administrative state |
| `warnings/` | `WarningContext` | Context only; issue/expiry/freshness and official-source referral required |
| `advisories/` | `AdvisoryContext` | Not life-safety guidance or official issuance by KFM |
| `declarations/` | `DisasterDeclaration` | Administrative context is not event proof by itself |
| `flood/` | `FloodContext` | Hydrology retains canonical gauge and network truth |
| `wildfire/` | `WildfireDetection` | Detection is not confirmed ignition or operational status by itself |
| `smoke/` | `SmokeContext` | Atmosphere retains canonical air and weather truth |
| `drought/` | `DroughtIndicator` | Aggregate indicator is not automatic per-place truth |
| `earthquake/` | `EarthquakeEvent` | Catalog context is not emergency response guidance |
| `heat_cold/` | `HeatColdEvent` | Not personal health or emergency guidance |
| `exposure/` | `ExposureSummary` | Aggregated planning context; protect people and infrastructure precision |
| `resilience/` | `ResilienceSummary` | Planning context, not certification or guarantee |
| `timelines/` | `HazardTimeline` | Preserve role, source, time, and correction distinctions |
| `impact_areas/` | `ImpactArea` | Candidate/derived extent is not verified damage or legal determination |

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive subtree and payload inventory | `NEEDS VERIFICATION` | Pinned tree, object families, formats, LFS/external stores, rights, sensitivity, owners |
| Writers and consumers | `UNKNOWN` | Connector, pipeline, tool, runtime, API/UI, workflow, deployed-consumer inventory |
| Schema/contract/policy enforcement | `UNKNOWN` | Accepted versions, fixtures, validators, decisions, CI and negative cases |
| Freshness and expiry enforcement | `UNKNOWN` | Deterministic clock handling, stale-state tests, supersession/correction cases, cache behavior |
| Receipt/proof/catalog/release closure | `UNKNOWN` | Emitted instances, identity agreement, EvidenceBundles, review, release, rollback links |
| Public serving and official-source referral | `UNKNOWN` | Governed routes, UI/API envelopes, disclaimer placement, redirects, access, caches, drills |
| Operational rollback and correction propagation | `NEEDS VERIFICATION` | RollbackCards, CorrectionNotices, invalidation lists, rehearsed recovery evidence |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED lifecycle role | Preserved and aligned to current parent contract |
| Not-for-life-safety boundary | Preserved and strengthened |
| Source-role and freshness rules | Preserved and expanded |
| Child-lane index | Preserved as bounded, unverified documentation |
| Rights, sensitivity, evidence, policy, release, correction, and rollback controls | Preserved and strengthened |
| Prior blob and rollback target | Recorded |
| Payload, move, deletion, migration, source, schema, policy, runtime, release, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the Hazards lane with the normalized parent `data/processed/` contract;
- strengthened not-for-life-safety, official-source-referral, freshness, expiry, and source-role boundaries;
- added bounded inputs, outputs, validation, review, correction, rollback, verification, and no-loss controls;
- preserved the child-lane index without claiming recursive implementation maturity;
- changed Markdown only.

[Back to top](#top)
