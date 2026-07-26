<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-proofs-citation-validation-atmosphere-readme
title: data/proofs/citation_validation/atmosphere/README.md — Atmosphere Citation Validation Proofs README
version: v0.2
status: repository-grounded draft; payload/runtime enforcement unverified
type: README; proof-lane-contract; citation-validation-lane; atmosphere-domain-proof-support; authority-boundary
owners: NEEDS VERIFICATION — Atmosphere, evidence, citation-validation, proof, policy, release, UI/Evidence Drawer, and docs stewards
updated: 2026-07-25
policy_label: restricted-review; no-direct-public-path; release-gated; cite-or-abstain
current_path: data/proofs/citation_validation/atmosphere/README.md
truth_posture: >
  CONFIRMED exact path, prior substantive boundary material, canonical parent proofs contract,
  Atmosphere proof-lane README, and PM2.5 2026 child proof README / PROPOSED normalized
  citation-validation lane contract / UNKNOWN recursive payloads, active writers/consumers,
  validator wiring, governed resolver behavior, runtime routes, caches, release state, and public effects /
  NEEDS VERIFICATION accountable owners, accepted profiles, schemas, fixtures, CI, emitted records,
  correction propagation, invalidation, retention, and rollback drills
related:
  - ../../README.md
  - ../../atmosphere/README.md
  - ../../atmosphere/pm25_2026/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../catalog/domain/atmosphere/pm25_2026/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../receipts/README.md
  - ../../../registry/README.md
  - ../../../published/README.md
  - ../../../../contracts/domains/atmosphere/
  - ../../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - ../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../../policy/domains/atmosphere/
  - ../../../../release/
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/trust-membrane.md
notes:
  - "Citation validation checks whether a claim's citations and EvidenceRefs resolve under governed rules; it does not create truth, evidence, policy approval, release approval, or publication."
  - "Atmosphere source roles remain non-interchangeable: observed sensor, AQI/report, low-cost sensor, regulatory/archive, AOD/smoke proxy, modeled field, forecast, and advisory context."
  - "Public clients must use governed resolvers and released projections; this lane is not a direct data service."
  - "Rollback target is prior blob d8f3f954a6628f5261a406798dfe73192cffcb77."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/proofs/citation_validation/atmosphere/` — Atmosphere Citation Validation

> Validate that Atmosphere claims, citations, and `EvidenceRef` values resolve to the correct governed evidence, source-role, caveat, policy, release, correction, and rollback context before use.

<p>
  <img alt="Status: grounded draft" src="https://img.shields.io/badge/status-grounded__draft-yellow">
  <img alt="Authority: proof support" src="https://img.shields.io/badge/authority-proof__support-blue">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-1f8fff">
  <img alt="Posture: cite or abstain" src="https://img.shields.io/badge/posture-cite--or--abstain-green">
  <img alt="Exposure: no direct public path" src="https://img.shields.io/badge/exposure-no__direct__public__path-critical">
</p>

> [!IMPORTANT]
> A citation-validation pass proves only the checks declared by its validation profile. It does not prove that a claim is true, rights-cleared, policy-admitted, reviewed, released, current, or safe for public use.

> [!CAUTION]
> Missing, stale, conflicting, role-collapsed, restricted, unreleased, withdrawn, or unresolvable support must yield a finite fail-closed result such as `ABSTAIN`, `HOLD`, `RESTRICT`, `DENY`, or `ERROR`.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Atmosphere guardrails](#atmosphere-citation-guardrails) · [Review](#review-burden) · [Related](#related-folders) · [Operating contract](#operating-contract) · [Correction](#correction-withdrawal-and-rollback) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This lane holds or indexes citation-validation proof support for Atmosphere/Air claims. Its job is to determine whether a claim's references resolve coherently across evidence, source, catalog, triplet, receipt, policy, review, release, correction, and rollback state.

It may support governed answers, Evidence Drawer payloads, catalog review, triplet review, release review, correction review, or audit. It must not become the canonical evidence store, a public API, an advisory service, or a substitute for the underlying proof packet.

## Authority level

**Canonical within the existing `data/proofs/citation_validation/atmosphere/` responsibility; citation-validation proof support only.**

This path does not own:

- factual truth or source authority;
- semantic contracts or machine schemas;
- policy or sensitivity decisions;
- release, correction, withdrawal, or rollback decisions;
- public API/UI rendering or Evidence Drawer behavior;
- AQI, medical, emergency, regulatory, exposure, or life-safety guidance.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/proofs/citation_validation/atmosphere/` |
| Prior blob | `d8f3f954a6628f5261a406798dfe73192cffcb77` |
| Parent proof authority | `data/proofs/README.md` — confirmed canonical parent contract |
| Atmosphere proof parent | `data/proofs/atmosphere/README.md` — confirmed present |
| PM2.5 2026 child proof lane | `data/proofs/atmosphere/pm25_2026/README.md` — confirmed present |
| Recursive validation-record inventory | `UNKNOWN` |
| Active validators and consumers | `UNKNOWN` |
| Governed resolver/runtime behavior | `UNKNOWN` |
| Public readiness | `DENY BY DEFAULT` |

## What belongs here

- citation-closure manifests for bounded Atmosphere claims;
- `EvidenceRef` resolution check outputs that point to, but do not duplicate, an `EvidenceBundle` or accepted proof packet;
- claim-to-citation maps for catalog, triplet, release, governed-answer, and Evidence Drawer review;
- integrity and identity agreement summaries across claim, proof, catalog, receipt, and release references;
- negative-result records explaining finite `ABSTAIN`, `HOLD`, `RESTRICT`, `DENY`, or `ERROR` outcomes;
- stale, correction, supersession, withdrawal, and invalidation closure summaries;
- local README, inventory, digest, migration, or disposition sidecars that do not create parallel authority.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | Corresponding lifecycle lane |
| Canonical `EvidenceBundle` or proof-packet instances | Accepted proof/evidence home under `data/proofs/` |
| Process receipts or validation execution receipts | `data/receipts/` |
| Source descriptors and source-admission state | `data/registry/sources/atmosphere/` |
| Policy, sensitivity, or admissibility decisions | `policy/` and referenced decision records |
| Release approval, correction notices, withdrawals, or rollback cards | `release/` |
| Contracts, schemas, validators, tests, fixtures, pipelines, or runtime code | Their responsibility roots |
| Public AQI payloads, maps, tiles, popups, reports, alerts, or AI answers | Released governed delivery surfaces |
| Exact sensitive station details, credentials, private endpoints, secrets, or unsafe logs | Approved restricted systems; never ordinary public proof paths |

## Inputs

A citation-validation record should identify the bounded claim or artifact being checked and, where applicable, resolve:

- claim ID, object family, and claim text or machine field;
- geography, spatial precision, and time scope;
- pollutant or variable identity, units, averaging window, and method;
- source identity, source role, source version, and source rights posture;
- `EvidenceRef` and expected `EvidenceBundle` or proof-packet identity;
- processed, catalog, triplet, receipt, policy, review, release, correction, and rollback references;
- digests, versions, timestamps, stale state, caveats, limitations, and conflict markers;
- validation profile, validator version, run identity, and declared check scope.

Inputs that are incomplete or mutually inconsistent narrow the allowed outcome; they do not invite inferred completion.

## Outputs

A bounded citation-validation result should include:

- stable validation-record identity and digest;
- claim and citation scope;
- resolved and unresolved references;
- source-role compatibility result;
- units, time, freshness, QA, caveat, and limitation result;
- policy/review/release dependency state;
- correction, supersession, withdrawal, and rollback dependency state;
- finite outcome: `PASS`, `ABSTAIN`, `HOLD`, `RESTRICT`, `DENY`, or `ERROR`;
- machine-readable findings suitable for review and a human-readable summary that does not exceed the evidence.

`PASS` means only that the declared citation-validation profile passed. It is not release approval or proof of truth.

## Validation

Validate, as applicable:

- deterministic identity, digest, version, and duplicate handling;
- `EvidenceRef` resolution to the intended `EvidenceBundle` or proof packet;
- claim-to-evidence scope agreement for object, geography, time, variable, units, and method;
- source identity, source role, rights, sensitivity, and lineage;
- catalog, triplet, receipt, policy, review, release, correction, and rollback reference integrity;
- stale, conflict, supersession, withdrawal, and invalidation state;
- link, anchor, metadata, and sensitive-content exposure;
- finite negative outcomes and stable finding identifiers.

No complete lane-wide validator, accepted profile, fixture suite, CI gate, or deployed resolver was verified in this task.

## Atmosphere citation guardrails

| Boundary | Required citation behavior |
|---|---|
| Observed sensor vs. AQI/report | A public AQI/report citation must not be accepted as a raw concentration citation. |
| Low-cost sensor | Calibration, caveat, QA, and role limitations must remain visible. |
| Regulatory/archive | Issuing authority, vintage, role, and applicability must be explicit. |
| PM2.5 vs. ozone | Pollutant-specific claims and units must not collapse into generic air-quality citations. |
| AOD/smoke proxy vs. ground observation | Proxy evidence cannot satisfy a ground-concentration claim without separately governed support. |
| Model/forecast vs. observation | Modeled or forecast evidence must remain labeled and cannot validate an observed-sensor claim. |
| Station context vs. observation value | Station identity or geometry does not prove the attached measurement. |
| Advisory context vs. KFM instruction | Official-source referral may be cited; KFM must not synthesize an advisory or life-safety instruction from proof placement. |
| Exposure/health/impact | Air-quality evidence alone does not prove individual exposure, health effect, damage, or causation. |
| Current vs. stale | Retrieval time, observed/valid time, correction state, and source freshness must be checked before use. |

## Review burden

Accountable owners remain **NEEDS VERIFICATION**. Changes should include Atmosphere, evidence, citation-validation, proof, policy, release, and UI/Evidence Drawer stewards as applicable.

Independent specialist review is required when a change affects source activation, rights, sensitivity, source roles, pollutant semantics, station precision, public serving, correction propagation, withdrawal, or rollback. CODEOWNERS routing or a successful check is not approval evidence.

## Related folders

- Parent proof authority: [`../../README.md`](../../README.md)
- Atmosphere proof lane: [`../../atmosphere/README.md`](../../atmosphere/README.md)
- PM2.5 2026 proof lane: [`../../atmosphere/pm25_2026/README.md`](../../atmosphere/pm25_2026/README.md)
- Atmosphere processed lane: [`../../../processed/atmosphere/README.md`](../../../processed/atmosphere/README.md)
- Atmosphere catalog lane: [`../../../catalog/domain/atmosphere/README.md`](../../../catalog/domain/atmosphere/README.md)
- Receipts: [`../../../receipts/README.md`](../../../receipts/README.md)
- Registry: [`../../../registry/README.md`](../../../registry/README.md)
- Published: [`../../../published/README.md`](../../../published/README.md)
- Contracts: [`../../../../contracts/domains/atmosphere/`](../../../../contracts/domains/atmosphere/)
- Schemas: [`../../../../schemas/contracts/v1/domains/atmosphere/`](../../../../schemas/contracts/v1/domains/atmosphere/)
- Policy: [`../../../../policy/domains/atmosphere/`](../../../../policy/domains/atmosphere/)
- Release: [`../../../../release/`](../../../../release/)

## Operating contract

For each bounded claim, the validator should evaluate this chain without silently filling gaps:

```text
claim
  -> citation / EvidenceRef
  -> EvidenceBundle or accepted proof packet
  -> source identity + source role + rights
  -> space/time/units/method/QA/caveats
  -> catalog/triplet/receipt agreement
  -> policy/review/release state
  -> correction/withdrawal/rollback state
  -> finite result
```

A result is invalid if it changes a source role, treats a proxy as an observation, converts an index/report into concentration truth, hides caveats, ignores stale or withdrawn state, or relies on a non-governed direct path.

## Correction, withdrawal, and rollback

Citation validation must be recomputed or invalidated when any referenced source, evidence bundle, proof packet, catalog record, triplet, receipt, policy decision, review, release, correction, or withdrawal changes materially.

A correction workflow should preserve:

1. prior validation-record identity and digest;
2. superseding validation-record identity;
3. affected claims and consumers;
4. stale or withdrawn references;
5. correction and invalidation reason;
6. cache or projection invalidation evidence where applicable;
7. rollback target and drill result.

This README does not verify that automated propagation or cache invalidation exists.

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive validation-record inventory | `NEEDS VERIFICATION` | Pinned tree, payload families, digests, owners, retention, rights/sensitivity |
| Accepted citation-validation profile | `UNKNOWN` | Contract/schema/profile version and decision record |
| Validators, fixtures, and CI | `UNKNOWN` | Implemented validator, positive/negative fixtures, stable findings, workflow evidence |
| Governed EvidenceRef resolver | `UNKNOWN` | Resolver contract, authorization, logs, failure behavior, tests |
| Writers and consumers | `UNKNOWN` | Pipeline, tool, release, API/UI, Evidence Drawer, Focus Mode, cache inventory |
| Correction and withdrawal propagation | `UNKNOWN` | Emitted records, dependency map, invalidation receipts, drills |
| Public-serving boundary | `UNKNOWN` | Governed route, release resolution, access control, no-direct-path tests |

Unknowns block higher-risk transitions and narrow claims. They do not justify plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path, document identity, and top anchor | Preserved |
| Citation-validation specialization | Preserved and clarified |
| `EvidenceRef` to `EvidenceBundle` closure | Preserved and strengthened |
| Atmosphere source-role and caveat boundaries | Preserved and strengthened |
| Negative-state outcomes | Preserved and normalized |
| Separation from evidence, receipts, policy, release, and public surfaces | Preserved |
| Correction and rollback posture | Preserved and expanded |
| Prior blob and documentation rollback target | Recorded |
| Payload, route, release, runtime, migration, or public-state change | None |

### Change history

#### v0.2 — 2026-07-25

- reconciled the lane with the canonical parent proofs authority;
- normalized citation identity, resolution, validation, review, correction, and rollback controls;
- preserved source-role anti-collapse and no-direct-public-path boundaries;
- changed Markdown only.

[Back to top](#top)
