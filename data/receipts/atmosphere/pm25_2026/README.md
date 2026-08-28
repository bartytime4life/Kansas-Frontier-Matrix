<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/atmosphere/pm25-2026/readme
name: Atmosphere PM2.5 2026 Receipts README
path: data/receipts/atmosphere/pm25_2026/README.md
type: data-receipts-domain-run-lane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <atmosphere-domain-steward>
  - <pm25-steward>
  - <air-quality-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: atmosphere-pm25-2026-receipts
receipt_scope: atmosphere-pm25-2026-process-memory
domain: atmosphere
object_family: PM25Observation
run_or_collection_hint: pm25_2026
path_posture: requested-domain-run-receipt-lane; parent-atmosphere-receipt-root-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; aqi-concentration-boundary-required; low-cost-caveat-required; aod-not-pm25; advisory-not-life-safety; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../raw/atmosphere/README.md
  - ../../../processed/atmosphere/pm25/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../proofs/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../published/layers/atmosphere/README.md
  - ../../../../release/manifests/README.md
  - ../../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../../contracts/domains/atmosphere/AirStation.md
  - ../../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../../contracts/domains/atmosphere/AdvisoryContext.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - atmosphere
  - pm25
  - pm2.5
  - pm25observation
  - 2026
  - run-receipt
  - transform-receipt
  - validation-report
  - policy-decision
  - air-quality
  - aqi-boundary
  - low-cost-sensor
  - no-public-path
  - evidence-first
notes:
  - "This README replaces a blank placeholder at `data/receipts/atmosphere/pm25_2026/README.md`."
  - "Parent `data/receipts/atmosphere/README.md` is currently a greenfield stub."
  - "PM2.5 processed and contract docs confirm PM25Observation boundaries: AQI/report is not raw concentration, AOD is not PM2.5, low-cost sensor use needs caveats/correction/confidence/limitations, and PM2.5 values are not health/safety/advisory authority by themselves."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted PM2.5 2026 receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, evidence closure, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere PM2.5 2026 Receipts

Receipt lane for Atmosphere PM2.5 2026 process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f9eda">
  <img alt="Object: PM25Observation" src="https://img.shields.io/badge/object-PM25Observation-7048e8">
  <img alt="Collection: 2026" src="https://img.shields.io/badge/collection-2026-blue">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [PM2.5 receipt boundary](#pm25-receipt-boundary) · [Receipt families](#receipt-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/atmosphere/pm25_2026/` is for Atmosphere PM2.5 2026 receipt process memory only. It is not PM2.5 truth, air-quality truth, exposure truth, health guidance, regulatory-exceedance proof, advisory authority, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is for receipt records and receipt-local sidecars that document governed PM2.5-related Atmosphere work for the `pm25_2026` collection or run family: source intake, transform, normalization, unit checks, AQI/report role checks, low-cost-sensor caveat checks, validation, policy evaluation, correction support, rollback support, and release-support context.

Receipts record what a process did. They may cite source refs, run IDs, source roles, station refs, input/output hashes, observed/retrieval/report times, units, averaging periods, QA/correction posture, caveats, limitations, policy refs, evidence refs, validator outcomes, correction refs, rollback refs, and release-candidate refs.

Receipts do **not** prove PM2.5 values, authorize public use, create health or life-safety guidance, establish regulatory exceedance, or replace PM25Observation contracts, schemas, SourceDescriptors, EvidenceBundles, ProofPacks, PolicyDecisions, ReleaseManifests, correction paths, or rollback targets.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested Atmosphere PM2.5 2026 lane is:

```text
data/receipts/atmosphere/pm25_2026/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/atmosphere/README.md` is still a greenfield stub, and exact domain/object/year receipt subfolder naming remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/atmosphere/pm25_2026/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | atmosphere |
| Object family | `PM25Observation` |
| Collection/run hint | `pm25_2026` |
| Path posture | requested domain/object/year receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/atmosphere/` |
| Lifecycle payload lanes | `data/raw/atmosphere/`, `data/work/atmosphere/`, `data/processed/atmosphere/pm25/` where applicable |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Contract authority | `contracts/domains/atmosphere/PM25Observation.md`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when source role, units, station context, AQI/report posture, low-cost caveats, AOD/model/advisory boundary, QA state, freshness, evidence refs, policy refs, validation state, correction path, rollback target, or release state is insufficient |

---

## PM2.5 receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records PM2.5 process behavior, not PM2.5 truth or air-quality truth. |
| PM25Observation meaning stays in the contract | This lane can reference `PM25Observation`; it does not define the object family. |
| AQI/report is not concentration | Receipts must preserve whether a value is concentration, AQI/report posture, regulatory/archive posture, low-cost sensor posture, model context, or other admitted role. |
| AOD is not PM2.5 | Remote-sensing context can be referenced but must not be treated as a PM2.5 observation. |
| Low-cost caveats travel | Low-cost sensor material requires caveat, correction, confidence, limitation, and policy context before public use. |
| Advisory and health limits remain | PM2.5 receipts do not create emergency, medical, exposure, regulatory, or life-safety guidance. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, correction notices, rollback cards, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Receipt families

The exact receipt subtype layout is not proven by this README. This lane may hold or reference PM2.5 2026-scoped records such as:

| Receipt family | Purpose | Boundary |
|---|---|---|
| Source/intake receipt | Records source observation, source-head state, retrieval, source role, run identity, and digests. | Does not prove source content is true or publishable. |
| Transform receipt | Records parsing, unit normalization, station join, correction, QA, or PM25Observation materialization. | Does not replace processed-object validation or proof. |
| Validation report | Records validator outcomes for source role, units, freshness, AQI/concentration boundary, low-cost caveats, AOD/model boundary, and release-readiness support. | Passing validation is not release approval. |
| Policy decision receipt/reference | Records finite policy decision state or policy bundle reference. | Policy authority remains in policy roots. |
| Correction receipt/reference | Records correction, supersession, recalibration, or caveat updates. | Correction authority remains in governed correction/release lanes. |
| Rollback-support receipt | Records rollback target support and affected outputs. | Rollback authority remains in release governance. |
| Release-support receipt | Records process support for a release candidate. | Release decision remains in `release/`. |

---

## Accepted material

Accepted content is limited to PM2.5 2026 receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source/intake, transform, validation, policy-decision, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, station refs, source roles, input refs, input hashes, output refs, output hashes, method IDs, policy refs, evidence refs, validator IDs, finite outcomes, reason codes, observed times, retrieval times, report/valid times, units, averaging period, QA/correction posture, freshness, caveat refs, limitation refs, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect PM2.5 receipt state without becoming proof, catalog, policy, release, public output, air-quality truth, health guidance, regulatory proof, or generated-answer authority.

Do not place direct public health instructions, exposure determinations, regulatory-exceedance conclusions, emergency guidance, exact sensitive station details, private-party details, or unsupported AOD/model-as-PM2.5 claims in README/index text.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw PM2.5 source feeds, station payloads, agency snapshots, QA payloads, logs, or source-native records | `data/raw/atmosphere/` |
| Work/scratch transformations | `data/work/atmosphere/` |
| Quarantined PM2.5 material | `data/quarantine/atmosphere/` |
| Normalized PM25Observation payloads | `data/processed/atmosphere/pm25/` |
| PM25Observation object meaning | `contracts/domains/atmosphere/PM25Observation.md` |
| PM25Observation schema | `schemas/contracts/v1/domains/atmosphere/PM25Observation.schema.json` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Air-quality, AQI/concentration, low-cost, AOD/model, advisory, freshness, sensitivity, or release policy | `policy/` and governed policy roots |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Medical, exposure, emergency, regulatory, or life-safety conclusions | Official/governed advisory and release surfaces only, never this receipt lane alone |

---

## Directory map

```text
data/receipts/atmosphere/pm25_2026/
├── README.md
├── <run_id>/
│   ├── run_receipt.json
│   ├── transform_receipt.json
│   ├── validation_report.json
│   ├── policy_decision_ref.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
├── validation/
│   └── <run_id>/
│       └── README.md
├── correction/
│   └── <run_id>/
│       └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, schemas, validators, fixtures, CI checks, signing, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, air-quality truth index, policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, source role, units, time fields, hashes, signatures, evidence refs, policy refs, validation state, or decision scope are incomplete. |
| Quarantine/correct | Receipt contradicts inputs, omits required AQI/concentration or low-cost caveats, violates policy, lacks replay/signature support, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite the receipt as process/validation/correction support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/atmosphere/pm25_2026/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. PM2.5 receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Atmosphere domain and `pm25_2026` PM2.5 receipt lane.
- [ ] Confirm canonical domain/object/year receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, subject/source refs, station refs, input/output hashes, evidence refs, policy refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role distinguishes concentration, AQI/report, regulatory/archive, low-cost sensor, model context, AOD context, and advisory context where applicable.
- [ ] Confirm units, averaging period, observed time, retrieval time, report/valid time, QA state, correction lineage, freshness, caveats, confidence, and limitations are preserved where material.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public PM2.5 claim path.
- [ ] Confirm receipt presence is not treated as PM2.5 truth, air-quality truth, exposure truth, health guidance, regulatory-exceedance proof, policy authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when rights, freshness, units, source role, low-cost caveat, AQI/concentration boundary, AOD/model boundary, advisory boundary, evidence, policy, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, generated answer, exposure statement, regulatory claim, or life-safety guidance uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/atmosphere/pm25_2026/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/atmosphere/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| `data/processed/atmosphere/pm25/README.md` documents the processed PM25Observation lane and PM2.5 guardrails. | **CONFIRMED by GitHub contents API during this edit** |
| `contracts/domains/atmosphere/PM25Observation.md` defines PM25Observation semantics and denies AQI/concentration collapse, AOD-as-PM2.5 collapse, low-cost overclaiming, advisory/life-safety guidance, proof closure, and release approval by contract alone. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/atmosphere/pm25_2026/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual PM2.5 2026 receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, policy enforcement, evidence closure, correction hooks, rollback hooks, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is PM2.5 truth, air-quality truth, exposure truth, health guidance, regulatory-exceedance proof, advisory authority, proof, catalog authority, registry authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../raw/atmosphere/README.md`](../../../raw/atmosphere/README.md)
- [`../../../processed/atmosphere/pm25/README.md`](../../../processed/atmosphere/pm25/README.md)
- [`../../../processed/atmosphere/README.md`](../../../processed/atmosphere/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../catalog/domain/atmosphere/README.md`](../../../catalog/domain/atmosphere/README.md)
- [`../../../published/layers/atmosphere/README.md`](../../../published/layers/atmosphere/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../contracts/domains/atmosphere/PM25Observation.md`](../../../../contracts/domains/atmosphere/PM25Observation.md)
- [`../../../../contracts/domains/atmosphere/AirObservation.md`](../../../../contracts/domains/atmosphere/AirObservation.md)
- [`../../../../contracts/domains/atmosphere/AirStation.md`](../../../../contracts/domains/atmosphere/AirStation.md)
- [`../../../../contracts/domains/atmosphere/AODRaster.md`](../../../../contracts/domains/atmosphere/AODRaster.md)
- [`../../../../contracts/domains/atmosphere/AdvisoryContext.md`](../../../../contracts/domains/atmosphere/AdvisoryContext.md)
- [`../../../../docs/domains/atmosphere/README.md`](../../../../docs/domains/atmosphere/README.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/atmosphere/pm25_2026/` is an Atmosphere PM2.5 2026 receipt lane for process memory only. It is not PM2.5 truth, air-quality truth, exposure truth, health guidance, regulatory-exceedance proof, advisory authority, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
