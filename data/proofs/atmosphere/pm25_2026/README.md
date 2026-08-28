<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-proofs-atmosphere-pm25-2026-readme
title: data/proofs/atmosphere/pm25_2026/README.md — Atmosphere PM2.5 2026 Proof Support
version: v0.2.0
type: README; proof-lane-guide; dataset-proof-contract; atmosphere-domain-proof-lane
status: repository-grounded draft; payload/runtime enforcement unverified
owners: NEEDS VERIFICATION — Atmosphere steward · Air-quality steward · PM2.5 steward · Evidence steward · Proof steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
policy_label: restricted-review; no-direct-public-path; release-gated
truth_posture: CONFIRMED exact path, prior README, parent Atmosphere proof lane, parent proofs authority, and PM2.5 semantic boundaries / PROPOSED normalized dataset-proof contract / UNKNOWN recursive proof payloads, active writers, consumers, runtime, routes, release state, caches, and public effects / NEEDS VERIFICATION accountable owners, accepted profiles, validators, fixtures, CI, receipt closure, correction propagation, invalidation, and rollback drills
related:
  - ../README.md
  - ../../README.md
  - ../../../catalog/domain/atmosphere/pm25_2026/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../processed/atmosphere/pm25/README.md
  - ../../../processed/atmosphere/air_observations/README.md
  - ../../../processed/atmosphere/air_stations/README.md
  - ../../../receipts/README.md
  - ../../../registry/sources/atmosphere/
  - ../../../published/
  - ../../../triplets/
  - ../../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../../contracts/domains/atmosphere/AirStation.md
  - ../../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../../contracts/domains/atmosphere/SmokeContext.md
  - ../../../../contracts/domains/atmosphere/ForecastContext.md
  - ../../../../contracts/domains/atmosphere/AdvisoryContext.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/PM25Observation.schema.json
  - ../../../../policy/domains/atmosphere/
  - ../../../../release/candidates/atmosphere/
  - ../../../../release/
notes:
  - "This path supports PM2.5 2026 claim evidence; it does not own source data, processed observations, catalog records, receipts, policy, release, public AQI guidance, or life-safety instructions."
  - "Observed concentration, public AQI/report posture, low-cost-sensor records, regulatory/archive posture, AOD/smoke proxy context, modeled fields, forecasts, and advisory context must remain role-separated."
  - "No recursive proof inventory, emitted EvidenceBundle set, validator suite, receipt closure, release manifest, route behavior, or cache invalidation was verified in this task."
  - "Rollback target is prior blob df4cee7c241265b1a426ad30f4dcca4d4e845d69."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/proofs/atmosphere/pm25_2026/`

> Dataset-specific proof-support lane for PM2.5 2026 claims. It may hold or index EvidenceBundle support, claim-scope manifests, citation and digest closure, limitations, and correction lineage. It is not factual truth, receipt authority, policy authority, release authority, public AQI guidance, medical advice, emergency alerting, or a direct data service.

<p>
  <img alt="Status: grounded draft" src="https://img.shields.io/badge/status-grounded__draft-yellow">
  <img alt="Authority: proof support" src="https://img.shields.io/badge/authority-proof__support-blue">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-1f8fff">
  <img alt="Dataset: PM2.5 2026" src="https://img.shields.io/badge/dataset-PM2.5__2026-purple">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-green">
  <img alt="Exposure: no direct public path" src="https://img.shields.io/badge/exposure-no__direct__public__path-critical">
</p>

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Operating contract](#operating-contract) · [PM2.5 boundaries](#pm25-claim-boundaries) · [Correction](#correction-withdrawal-and-rollback) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

> [!IMPORTANT]
> A proof file, resolved citation, passing schema check, successful workflow, pull request, or merge does not make a PM2.5 claim true, current, rights-cleared, policy-admitted, reviewed, released, or safe for public-health guidance.

> [!CAUTION]
> PM2.5 concentration, AQI/report posture, low-cost-sensor output, regulatory/archive status, AOD or smoke proxy context, model output, forecast context, and advisory context are different knowledge characters. Proof support must preserve those distinctions and must never infer one from another without separately governed evidence and method support.

## Purpose

Own dataset-scoped proof support for claims associated with the PM2.5 2026 family. The lane exists so a claim, catalog row, triplet, release candidate, correction, rollback action, or governed answer can resolve evidence, limitations, source role, time scope, and integrity without reading raw or processed stores directly.

This README documents the lane boundary. It does not assert that proof packets, EvidenceBundles, receipts, release records, validators, CI checks, public routes, or deployed consumers currently exist.

## Authority level

**Canonical child lane under `data/proofs/`; proof-support authority only.**

This path may organize or hold accepted PM2.5 2026 proof packets and indexes. It does not own:

- PM2.5 object meaning;
- machine shape;
- source admission or source rights;
- observation, station, catalog, or triplet truth;
- validation or process receipts;
- policy decisions;
- release, correction, withdrawal, or rollback authority;
- public AQI, medical, emergency, or life-safety guidance;
- public API, tile, UI, or AI-answer behavior.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/proofs/atmosphere/pm25_2026/` |
| Version | `v0.2.0` |
| Prior blob | `df4cee7c241265b1a426ad30f4dcca4d4e845d69` |
| Parent proof lane | `data/proofs/atmosphere/` |
| Proof payload inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Accepted EvidenceBundle/profile version | `NEEDS VERIFICATION` |
| Validator and CI enforcement | `NEEDS VERIFICATION` |
| Release/public readiness | `DENY BY DEFAULT` |

## What belongs here

Subject to accepted profiles and policy, this lane may hold or index:

- PM2.5 2026 EvidenceBundle instances or resolvable pointers;
- EvidenceRef resolution maps;
- claim-scope manifests binding proof support to a specific claim, catalog row, triplet, release candidate, correction, or governed answer;
- citation-validation, source-agreement, limitation, uncertainty, and integrity summaries;
- digest manifests binding admitted source evidence, processed artifacts, catalog records, triplets, and proof packets;
- proof support for concentration observations, AQI/report claims, low-cost-sensor records, regulatory/archive records, station/network context, freshness, QA, correction, and caveat claims;
- proof support for comparisons with AOD, smoke, weather, or model context when the compared objects remain separate and individually evidenced;
- lane-local indexes, README files, inventory notes, migration notes, or disposition sidecars that do not become parallel receipt, policy, catalog, or release authority.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Raw sensor feeds, agency downloads, station payloads, QA payloads, or source-native files | `data/raw/atmosphere/` |
| Parsing, calibration, joins, model comparison, QA work, notebooks, or scratch outputs | `data/work/atmosphere/` |
| Rights-unclear, role-unclear, stale, malformed, disputed, unsafe, or caveat-missing material | `data/quarantine/atmosphere/` |
| PM2.5 observations or station records | Accepted `data/processed/atmosphere/` object lanes |
| Catalog, STAC, DCAT, PROV, or triplet records | Their catalog or triplet lanes |
| Run, transform, validation, policy, review, correction, access, release, or publication receipts | `data/receipts/` or accepted receipt authority |
| SourceDescriptor or source activation records | `data/registry/sources/atmosphere/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, WithdrawalNotice, or RollbackCard | `release/` |
| Public AQI payloads, maps, tiles, APIs, UI state, notifications, or AI answers | Released governed delivery surfaces |
| Medical advice, regulatory determination, emergency alerting, or life-safety instructions | Authoritative agencies and separately governed referral surfaces |
| Secrets, private endpoints, unsafe logs, exact protected siting, or access-control details | Approved restricted operational systems |

## Inputs

A proof packet should be constructed only from admitted, identifiable inputs. As applicable, inputs should resolve:

- stable claim, object, dataset, source, station/network, catalog, triplet, release-candidate, and proof identities;
- source role and source rights posture;
- pollutant identity as PM2.5;
- claim type: concentration, AQI/report, regulatory/archive, low-cost-sensor, comparison, correction, or other accepted role;
- source value, normalized value, units, conversion method, and precision posture;
- averaging window, observed time, retrieval time, correction time, and freshness state;
- station/network context and any siting sensitivity;
- QA, calibration, provisional/final state, uncertainty, caveats, limitations, and missingness;
- contract/schema/profile versions;
- source, run, validation, policy, review, correction, release, and rollback references when applicable;
- digests binding evidence inputs and supported artifacts.

Missing or unresolved inputs narrow claim scope and should produce `HOLD`, `ABSTAIN`, `RESTRICT`, `DENY`, or `ERROR`, not plausible completion.

## Outputs

Outputs may include a proof packet, EvidenceBundle, proof index, claim-support manifest, citation/integrity report, or limitations summary under an accepted profile.

Every output should state what it supports and what it does not support. A proof packet for a concentration claim does not automatically support AQI, exposure, health, regulatory exceedance, smoke attribution, forecast, or advisory claims.

Public clients should resolve released claims through governed APIs or release-resolved artifacts. They must not use this internal proof lane as a direct data service.

## Validation

Validation should be deterministic and scoped. At minimum, check:

- path and profile placement;
- stable identity and duplicate prevention;
- claim-to-proof and EvidenceRef-to-EvidenceBundle resolution;
- source role, pollutant identity, units, averaging window, and time scope;
- source/station/network linkage;
- concentration versus AQI/report separation;
- low-cost-sensor caveats and calibration lineage where applicable;
- observed versus model/proxy separation;
- freshness, provisional/final state, correction, supersession, and withdrawal state;
- digest closure and supported-artifact agreement;
- rights, sensitivity, policy, review, release, correction, and rollback dependencies;
- absence of secrets, harmful precision, protected siting details, or direct public-serving instructions;
- Markdown metadata, anchors, links, and rollback notes for documentation changes.

No complete validator or CI-enforced PM2.5 2026 proof profile was verified in this task. A passing check proves only its declared scope.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Review should include the PM2.5/air-quality steward, proof/evidence steward, and policy/release reviewers appropriate to the claim.

Independent specialist review is expected when a change affects:

- concentration-to-AQI/report interpretation;
- low-cost-sensor calibration or caveats;
- station/network identity or siting sensitivity;
- regulatory/archive posture;
- model, AOD, smoke, or forecast comparisons;
- public-health or action-oriented wording;
- release, correction, withdrawal, cache invalidation, or rollback behavior.

CODEOWNERS routing, approvals, or a merge are not evidence closure by themselves.

## Related folders

- Parent: [`../README.md`](../README.md) · [`../../README.md`](../../README.md)
- Catalog: [`../../../catalog/domain/atmosphere/pm25_2026/README.md`](../../../catalog/domain/atmosphere/pm25_2026/README.md)
- Processed: [`../../../processed/atmosphere/pm25/README.md`](../../../processed/atmosphere/pm25/README.md) · [`../../../processed/atmosphere/air_observations/README.md`](../../../processed/atmosphere/air_observations/README.md) · [`../../../processed/atmosphere/air_stations/README.md`](../../../processed/atmosphere/air_stations/README.md)
- Trust support: [`../../../receipts/README.md`](../../../receipts/README.md) · `data/registry/sources/atmosphere/`
- Authority: `contracts/domains/atmosphere/PM25Observation.md` · `schemas/contracts/v1/domains/atmosphere/PM25Observation.schema.json` · `policy/domains/atmosphere/` · `release/`

## ADRs

Relevant decisions may include schema-home, proof/receipt/catalog/release separation, connector-output boundaries, published aliases, and public-client trust-membrane ADRs. Their accepted status and applicability to this dataset remain **NEEDS VERIFICATION**. This README accepts no new ADR and creates no parallel authority.

## Last reviewed

- **Date:** 2026-07-25
- **Review type:** exact target README plus parent Atmosphere and parent proofs contracts
- **Recursive payload/runtime inspection:** not performed
- **Owners, accepted profiles, validators, CI, releases, routes, caches, and operational rollback:** needs verification

Re-review after changes to source roles, PM2.5 contracts/schemas, proof profiles, policy, release, public consumers, correction propagation, or rollback behavior—or within six months.

## Operating contract

Each proof packet must bind to a finite claim scope and preserve the source's knowledge character. The packet should declare:

1. supported claim identity and object family;
2. geography or station/network scope;
3. observed, retrieval, correction, and validity times;
4. value, units, averaging window, and precision;
5. source role and source authority;
6. QA, calibration, uncertainty, caveats, and limitations;
7. citations and evidence digests;
8. applicable receipts, policy, review, release, correction, and rollback dependencies;
9. supported decision outcomes;
10. explicit non-claims.

Missing support yields a finite governed outcome. Fluency, schema validity, directory placement, or historical precedent does not fill evidence gaps.

## PM2.5 claim boundaries

| Boundary | Required posture |
|---|---|
| Concentration vs. AQI/report | An AQI/report value is not raw concentration. Preserve source role, method/version, averaging window, and issuing authority. |
| Regulatory/archive vs. general observation | Regulatory posture requires explicit source role, vintage, method, authority, and evidence. |
| Low-cost sensor vs. reference-grade observation | Preserve device/network role, calibration, collocation or correction context, uncertainty, caveats, and provisional/final status. |
| PM2.5 vs. AOD or smoke | AOD and smoke are proxy/context families; they do not prove ground-level PM2.5 concentration or exposure. |
| Observed vs. modeled/forecast | Model and forecast outputs remain model context and cannot be promoted into observed concentration. |
| Observation vs. exposure/health | Ambient concentration does not prove individual exposure, diagnosis, harm, or medical action. |
| Observation vs. advisory | KFM proof support does not issue public-health advisories or emergency instructions. |
| Proof vs. release | Evidence closure supports review; release authority remains under `release/`. |

## Correction, withdrawal, and rollback

A correction or withdrawal affecting a supported input, station identity, source role, unit conversion, averaging window, QA state, calibration, catalog row, triplet, or release candidate should trigger dependency review.

The governed correction path should:

1. identify affected proof packets and EvidenceRefs;
2. mark stale, superseded, withdrawn, or invalid state without deleting history;
3. preserve the reason and replacement linkage;
4. propagate to catalog, triplet, release, API/UI, caches, and AI-answer surfaces where applicable;
5. retain the prior digest and rollback target;
6. verify that stale public artifacts are no longer served.

Operational correction propagation and rollback drills remain **NEEDS VERIFICATION**.

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive proof inventory | `UNKNOWN` | Pinned tree, payload families, digests, rights/sensitivity, retention, owners |
| Accepted EvidenceBundle/proof profile | `NEEDS VERIFICATION` | Contract/schema/profile versions and compatibility policy |
| Source manifest and roles | `NEEDS VERIFICATION` | SourceDescriptors, admission decisions, terms, station/network lineage |
| Validators, fixtures, and CI | `UNKNOWN` | Positive/negative fixtures, deterministic validators, workflow evidence |
| Receipt and digest closure | `UNKNOWN` | Emitted source/run/validation/policy/review/correction/release records and agreement checks |
| Catalog/triplet/release linkage | `UNKNOWN` | Stable IDs, supported claims, release manifests, rollback cards |
| Public serving and invalidation | `UNKNOWN` | Governed routes, hosting, caches, stale/withdrawal behavior, drills |
| Accountable owners and review separation | `NEEDS VERIFICATION` | Ownership mapping, reviewer independence, escalation path |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| Dataset-specific PM2.5 2026 proof role | Preserved and clarified |
| EvidenceBundle / EvidenceRef closure | Preserved and strengthened |
| Source-role anti-collapse | Preserved and expanded |
| Concentration, AQI/report, low-cost, regulatory, model, proxy, and advisory boundaries | Preserved and strengthened |
| Receipts, registry, policy, catalog, release, and public authority separation | Preserved |
| Correction and rollback posture | Preserved and strengthened |
| Prior blob | Recorded as documentation rollback target |
| Payload, schema, policy, route, release, or runtime change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the child lane with the normalized parent proofs authority model;
- strengthened PM2.5 claim scope, role separation, freshness, correction, withdrawal, and rollback controls;
- added bounded validation, review, verification, and no-loss sections;
- changed Markdown only.

[Back to top](#top)
