<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-proofs-atmosphere-readme
title: data/proofs/atmosphere/README.md — Atmosphere Proof Support
version: v0.2.0
type: README; domain-proof-lane; authority-boundary; evidence-support-index
status: repository-grounded draft; payload/runtime enforcement unverified
owners: NEEDS VERIFICATION — Atmosphere, evidence, proof, validation, policy, release, and documentation stewards
updated: 2026-07-25
policy_label: restricted-review; no-direct-public-path; release-gated; cite-or-abstain
current_path: data/proofs/atmosphere/README.md
truth_posture: >
  CONFIRMED exact path, canonical parent proofs contract, existing PM2.5 2026 child
  README, and Atmosphere source-role boundaries / PROPOSED normalized domain proof
  contract / UNKNOWN recursive payloads, writers, consumers, routes, caches, runtime,
  and release state / NEEDS VERIFICATION owners, accepted proof profiles, schemas,
  validators, fixtures, CI, emitted packets, correction propagation, invalidation,
  and rollback drills
related:
  - ../README.md
  - pm25_2026/README.md
  - ../../processed/atmosphere/README.md
  - ../../catalog/domain/atmosphere/README.md
  - ../../receipts/README.md
  - ../../registry/sources/atmosphere/
  - ../../published/README.md
  - ../../triplets/README.md
  - ../../../contracts/domains/atmosphere/
  - ../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../policy/domains/atmosphere/
  - ../../../release/
notes:
  - "This README aligns the Atmosphere domain proof lane with the canonical data/proofs responsibility contract."
  - "Proof support does not create factual truth, policy permission, release approval, publication, regulatory determination, medical advice, emergency alerting, or life-safety guidance."
  - "Observed sensor readings, public AQI/report posture, low-cost sensor records, regulatory/archive posture, AOD/smoke proxies, modeled fields, forecasts, and advisory context remain distinct source roles."
  - "Rollback target is prior blob 2a0331e803ba50fd6d9bb3771bdd02a4060678eb."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/proofs/atmosphere/` — Atmosphere Proof Support

> **One-line purpose.** Hold Atmosphere-domain proof packets, EvidenceBundle support, citation and integrity closure, limitations, and proof indexes used to evaluate whether Atmosphere claims have sufficient governed support.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: domain proof](https://img.shields.io/badge/authority-domain%20proof-0969da?style=flat-square)](#authority-level)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#validation)
[![Exposure: not public](https://img.shields.io/badge/exposure-not%20public-b42318?style=flat-square)](#outputs)

> [!IMPORTANT]
> A proof file, successful validator, pull request, or merge does **not** make an Atmosphere claim true, rights-cleared, policy-admitted, reviewed, released, public, regulatory, medical, or safe for emergency use.

> [!WARNING]
> Proof packets must not expose harmful-precision station details, private access information, secrets, restricted source terms, calibration internals that enable misuse, or protected operational material in ordinary public-repository paths.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Operating contract](#operating-contract) · [Children](#current-bounded-child-lane-index) · [Verification](#open-verification-register) · [Correction](#correction-withdrawal-and-rollback) · [No-loss](#no-loss-ledger)

## Purpose

`data/proofs/atmosphere/` is the Atmosphere/Air domain proof-support lane under the canonical `data/proofs/` responsibility root.

It may hold or index:

- EvidenceBundle instances or accepted proof packets for Atmosphere claims;
- EvidenceRef resolution maps and claim-scope manifests;
- citation-validation, agreement, integrity, digest, and limitation summaries;
- proof indexes for air observations, stations, PM2.5, ozone, AOD, smoke, weather, wind, climate, forecast/model, and advisory-context claims;
- correction, withdrawal, supersession, invalidation, and rollback dependencies;
- local README, inventory, migration, or disposition sidecars that explain proof boundaries without creating parallel authority.

This lane supports inspectability. It does not replace source records, processed objects, catalogs, triplets, receipts, source registries, contracts, schemas, policy decisions, release records, published products, or governed interfaces.

## Authority level

**Canonical child of the PROOFS responsibility; domain-scoped proof support only.**

This path may support evidence closure for Atmosphere claims. It does not own:

- factual or regulatory truth;
- semantic object meaning;
- machine field shape;
- source admission or source role;
- policy or sensitivity decisions;
- release, promotion, correction, withdrawal, or rollback authority;
- public APIs, tiles, maps, alerts, health guidance, or emergency instructions.

Those authorities remain in their governed responsibility roots.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/proofs/atmosphere/` |
| Version | `v0.2.0` |
| Prior blob | `2a0331e803ba50fd6d9bb3771bdd02a4060678eb` |
| Parent proof contract | **CONFIRMED** at `data/proofs/README.md` |
| Confirmed child README | `pm25_2026/README.md` |
| Recursive proof payload inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Route, cache, hosting, and runtime behavior | `UNKNOWN` |
| Complete domain-wide validator | `NOT VERIFIED` |
| Public readiness | `DENY BY DEFAULT` |

## What belongs here

Atmosphere proof support may include:

- claim-scoped EvidenceBundle or proof-pack instances under accepted profiles;
- stable mappings from EvidenceRef to EvidenceBundle or a finite unresolved outcome;
- proof manifests that identify claim, object family, source role, geography, time, variable, units, uncertainty, caveats, validation profile, policy/review dependencies, and release dependency;
- digest closure linking admitted sources, processed artifacts, catalog/triplet projections, receipts, proof packets, and release candidates;
- citation-validation and source-agreement summaries;
- limitations and reality-boundary notes that prevent observation, model, proxy, AQI/report, forecast, advisory, exposure, impact, and regulatory-role collapse;
- proof indexes for correction, withdrawal, supersession, invalidation, and rollback analysis.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| RAW source captures, feeds, station payloads, source-native files, or logs | `data/raw/atmosphere/` |
| WORK transforms, calibration experiments, joins, notebooks, or scratch outputs | `data/work/atmosphere/` |
| Rights-, role-, freshness-, sensitivity-, or evidence-unclear material | `data/quarantine/atmosphere/` until resolved |
| Canonical processed Atmosphere objects | `data/processed/atmosphere/` |
| Catalog, STAC, DCAT, PROV, or triplet records | Their catalog/triplet lanes |
| Process, validation, redaction, aggregation, model-run, review, or publication receipts | `data/receipts/` |
| SourceDescriptor or source-registry authority | `data/registry/sources/atmosphere/` |
| PolicyDecision, release manifest, promotion decision, correction notice, withdrawal notice, or rollback card | `policy/` or `release/` as applicable |
| Contracts, schemas, validators, fixtures, tests, pipelines, APIs, UI code, or map styles | Their responsibility roots |
| Public AQI reports, maps, tiles, alerts, medical advice, or emergency guidance | Governed released interfaces only |
| Claims presented as true because a proof file exists | Resolve the complete governed evidence and release state or abstain |

## Inputs

Proof packets may reference admitted Atmosphere sources, processed objects, catalog/triplet projections, validation and citation reports, receipts, policy decisions, review records, corrections, and release dependencies.

As applicable, every packet should resolve or explicitly mark unresolved:

- stable claim and object identity;
- source descriptor and immutable source role;
- geography, geometry support, station/network context, and precision posture;
- observation, source, retrieval, model-run, valid, correction, and expiry times;
- variable, pollutant, units, averaging window, conversion, and method;
- QA, calibration, provisional/final state, uncertainty, freshness, and limitations;
- contract/schema profile and validator scope;
- EvidenceRef, EvidenceBundle, receipts, policy, review, release, correction, withdrawal, and rollback dependencies.

## Outputs

Outputs are proof support for review, release evaluation, governed APIs, Evidence Drawer surfaces, correction propagation, withdrawal, and rollback analysis.

An output must be bounded to one or more explicit claims or artifacts. It must not become a direct data service, internal-store public route, AQI advisory engine, regulatory-exceedance authority, health guidance system, or emergency-alert surface.

When evidence is insufficient, the output should yield a finite posture such as `HOLD`, `ABSTAIN`, `RESTRICT`, `DENY`, or `ERROR` rather than fluent completion.

## Validation

Validate at least the following within the declared profile:

- path and responsibility placement;
- stable identity, digest, version, and duplicate detection;
- EvidenceRef resolution or explicit unresolved state;
- source role and anti-collapse boundaries;
- pollutant/variable, units, averaging window, method, and time semantics;
- station/network and harmful-precision handling;
- QA, calibration, uncertainty, freshness, caveats, and provisional/final state;
- receipt, policy, review, catalog/triplet, release, correction, withdrawal, and rollback references;
- links, anchors, metadata, protected-content exposure, and stale dependencies.

No complete Atmosphere proof-lane validator was verified. A passing check proves only its documented scope.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**.

Changes should include Atmosphere, air-quality or weather, proof/evidence, validation, policy/sensitivity, release, and documentation stewards as applicable. Independent review is warranted for:

- source activation or source-role changes;
- low-cost-sensor, regulatory/archive, model, forecast, AOD/smoke, or advisory interpretations;
- exact or sensitive station/location handling;
- health, exposure, regulatory, impact, or life-safety-adjacent claims;
- proof-profile changes, migrations, corrections, withdrawals, public serving, or rollback.

CODEOWNERS routing or reviewer assignment is not approval evidence.

## Related folders

- Parent proof contract: [`../README.md`](../README.md)
- Confirmed child: [`pm25_2026/README.md`](pm25_2026/README.md)
- Processed Atmosphere: [`../../processed/atmosphere/README.md`](../../processed/atmosphere/README.md)
- Atmosphere catalog: [`../../catalog/domain/atmosphere/README.md`](../../catalog/domain/atmosphere/README.md)
- Receipts: [`../../receipts/README.md`](../../receipts/README.md)
- Published carriers: [`../../published/README.md`](../../published/README.md)
- Contracts: [`../../../contracts/domains/atmosphere/`](../../../contracts/domains/atmosphere/)
- Schemas: [`../../../schemas/contracts/v1/domains/atmosphere/`](../../../schemas/contracts/v1/domains/atmosphere/)
- Policy: [`../../../policy/domains/atmosphere/`](../../../policy/domains/atmosphere/)
- Release: [`../../../release/`](../../../release/)

## ADRs

Relevant proposed decisions include receipt/proof/catalog/release separation, connector-output boundaries, public-client trust-membrane rules, and correction/rollback handling. This README accepts no unverified ADR by implication.

Changing the canonical proof responsibility, introducing a parallel proof home, or allowing direct public reads requires an accepted ADR, migration plan, validation, correction plan, and rollback target.

## Last reviewed

- **Date:** 2026-07-25
- **Evidence basis:** exact target README, canonical `data/proofs/README.md`, and confirmed `pm25_2026/README.md`
- **Recursive payload/runtime inspection:** not performed
- **Owners, accepted proof profiles, enforcement, public consumers, and operational rollback:** need verification

Re-review on source-role, object-family, writer, policy, release, public-consumer, correction, withdrawal, or rollback changes—or within six months.

## Operating contract

An Atmosphere proof packet should state:

1. the claim or artifact it supports;
2. the object family and immutable source role;
3. geographic, temporal, variable, units, averaging, and method scope;
4. evidence references, digests, validation profile, uncertainty, freshness, caveats, and limitations;
5. policy, review, release, correction, withdrawal, invalidation, and rollback dependencies.

Role-specific boundaries must remain explicit:

| Role or family | Required boundary |
|---|---|
| Observed sensor | Not model, proxy, AQI/report, advisory, exposure, or impact proof |
| Public AQI/report | Not raw concentration unless separately supported and clearly labeled |
| Low-cost sensor | Calibration, caveat, QA, and confidence posture must remain visible |
| Regulatory/archive | Issuing authority, vintage, role, and legal limitations must remain visible |
| AOD/smoke proxy | Not PM2.5 concentration, exposure, or ground observation |
| Model/forecast/reanalysis | Never promoted to observed sensor truth |
| Advisory context | Referral/context only; KFM does not issue life-safety instructions |

## Current bounded child-lane index

| Child lane | Bounded posture |
|---|---|
| [`pm25_2026/`](pm25_2026/README.md) | README confirmed and recently modernized; payloads, accepted profiles, validators, receipts, release linkage, and runtime remain unverified. |
| `air_observations/` | **PROPOSED** until path, README, payloads, and enforcement are verified. |
| `air_stations/` | **PROPOSED** until path, README, payloads, sensitivity controls, and enforcement are verified. |
| `ozone/` | **PROPOSED** until path, README, payloads, pollutant-specific proof profile, and enforcement are verified. |
| `aod/` | **PROPOSED** until path, README, proxy-proof profile, and enforcement are verified. |
| `smoke_context/` | **PROPOSED** until path, README, model/proxy boundaries, and enforcement are verified. |
| `forecast_context/` | **PROPOSED** until path, README, model-run/uncertainty support, and enforcement are verified. |
| `climate/` | **PROPOSED** until path, README, baseline/anomaly proof profile, and enforcement are verified. |

Omission is not retirement. New child lanes require a verified responsibility need and must not create parallel proof authority.

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive subtree and payload inventory | `NEEDS VERIFICATION` | Pinned tree, payload families, external/LFS storage, rights, sensitivity, owners |
| Writers and consumers | `UNKNOWN` | Connector, pipeline, validator, workflow, API/UI, Evidence Drawer, and deployed-consumer inventory |
| Accepted proof profiles and enforcement | `UNKNOWN` | Contracts/schemas, fixtures, validators, CI, positive/negative cases, version pins |
| EvidenceRef/EvidenceBundle closure | `UNKNOWN` | Emitted packets, resolvers, unresolved outcomes, digest agreement, citation checks |
| Receipt/catalog/triplet/release agreement | `UNKNOWN` | Stable identities, receipt references, policy/review, release and rollback links |
| Correction, withdrawal, invalidation, and serving | `UNKNOWN` | Propagation rules, cache behavior, stale handling, drills, governed route evidence |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## Correction, withdrawal, and rollback

A correction or withdrawal affecting an Atmosphere claim should identify:

- the affected claim, EvidenceRef, EvidenceBundle, proof packet, catalog/triplet projection, and release dependency;
- whether source role, units, averaging window, station context, QA, calibration, freshness, model run, uncertainty, or policy changed;
- downstream products, routes, caches, indexes, and answers requiring invalidation;
- replacement, supersession, withdrawal, and rollback targets.

This README does not execute those actions. Release and operational systems remain authoritative.

Documentation rollback: revert the modernization commit or restore prior blob `2a0331e803ba50fd6d9bb3771bdd02a4060678eb`.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| Atmosphere proof-support purpose | Preserved and clarified |
| EvidenceBundle / EvidenceRef closure | Preserved and strengthened |
| Source-role anti-collapse | Preserved and expanded |
| PM2.5 2026 confirmed child lane | Preserved |
| Proposed child-lane index | Preserved with bounded status labels |
| Receipt, registry, catalog, policy, release, and public-surface separation | Preserved |
| Rights, sensitivity, correction, withdrawal, invalidation, and rollback controls | Preserved and strengthened |
| Payload, source, schema, policy, route, runtime, release, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- reconciled the lane with the canonical parent proofs contract;
- corrected the stale claim that the parent proof README was a greenfield stub;
- normalized proof scope, authority, validation, review, correction, and no-loss sections;
- preserved Atmosphere source-role boundaries and the PM2.5 2026 child lane;
- changed Markdown only.

[Back to top](#top)
