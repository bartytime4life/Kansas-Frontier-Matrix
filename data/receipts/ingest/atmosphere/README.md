<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/ingest/atmosphere/readme
name: Atmosphere Ingest Receipts README
path: data/receipts/ingest/atmosphere/README.md
type: data-receipts-ingest-domain-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <ingest-steward>
  - <atmosphere-domain-steward>
  - <source-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: atmosphere-ingest-receipts
receipt_scope: atmosphere-source-intake-process-memory
domain: atmosphere
path_posture: requested-ingest-domain-receipt-lane; ingest-parent-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-role-preserving; source-intake-not-raw-payload; aqi-concentration-boundary-required; aod-not-pm25; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../atmosphere/README.md
  - ../../../raw/atmosphere/README.md
  - ../../../work/atmosphere/README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../processed/atmosphere/pm25/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../published/layers/atmosphere/README.md
  - ../../../proofs/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../pipelines/domains/atmosphere/README.md
  - ../../../../pipelines/domains/atmosphere/normalize/README.md
  - ../../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - ingest
  - atmosphere
  - source-intake
  - source-role
  - run-receipt
  - source-descriptor
  - transform-receipt
  - validation-report
  - policy-decision
  - no-public-path
  - evidence-first
notes:
  - "This README replaces a blank placeholder at `data/receipts/ingest/atmosphere/README.md`."
  - "Parent `data/receipts/ingest/README.md` is currently a greenfield stub."
  - "Atmosphere receipt docs confirm Atmosphere receipts are process memory and do not prove atmospheric values, authorize publication, define object meaning, issue advisories, create health/life-safety guidance, or replace proof/release artifacts."
  - "Atmosphere RAW docs confirm RAW captures source material while `data/receipts/` owns receipt authority."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted ingest receipts, source descriptors, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Ingest Receipts

Ingest receipt lane for Atmosphere source-intake process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f9eda">
  <img alt="Lane: ingest" src="https://img.shields.io/badge/lane-ingest-blue">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Ingest receipt boundary](#ingest-receipt-boundary) · [Receipt families](#receipt-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/ingest/atmosphere/` is for Atmosphere ingest receipt process memory only. It is not raw source data, atmospheric truth, air-quality truth, source registry authority, contract authority, schema authority, proof, EvidenceBundle authority, catalog authority, policy authority, release authority, public artifact authority, advisory authority, health/life-safety guidance, or generated-answer authority.

---

## Scope

This directory is for receipt records and receipt-local sidecars that document governed Atmosphere source-intake activity: source check, source descriptor reference, retrieval attempt, source head state, source-role assignment, rights/citation posture, timestamp handling, digest capture, basic admission decision, quarantine routing, and downstream handoff context.

Ingest receipts record what the intake process did and what evidence, source, policy, validation, correction, rollback, or release-candidate references need to travel downstream. They can support proof and release review later, but they do **not** prove atmospheric values, admit source payloads by themselves, authorize publication, or replace SourceDescriptors, RAW payloads, contracts, schemas, EvidenceBundles, ProofPacks, CatalogMatrix records, PolicyDecisions, ReleaseManifests, CorrectionNotices, or RollbackCards.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested ingest/domain receipt lane is:

```text
data/receipts/ingest/atmosphere/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/ingest/README.md` is still a greenfield stub, and the exact choice between `data/receipts/ingest/<domain>/` and `data/receipts/<domain>/ingest/` remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/ingest/atmosphere/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | ingest / source-intake process memory |
| Domain lane | atmosphere |
| Path posture | requested ingest/domain receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/ingest/` |
| Related domain receipt parent | `data/receipts/atmosphere/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| RAW payload authority | `data/raw/atmosphere/`, not this lane |
| Source registry authority | `data/registry/sources/`, not this lane |
| Contract authority | `contracts/domains/atmosphere/`, not this lane |
| Schema authority | `schemas/contracts/v1/domains/atmosphere/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when source identity, source role, rights, citation, cadence, timestamp, digest, station/context, AQI/report posture, low-cost caveats, AOD/model/advisory boundary, evidence refs, policy refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Ingest receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what the intake process did; it is not the truth source. |
| Ingest receipt is not RAW payload | Payloads or payload references belong in RAW lanes; receipts record intake process state and references. |
| SourceDescriptor remains separate | Source identity, rights, cadence, and role authority belong in governed source registry/source descriptor records. |
| Source roles remain explicit | Observed sensor, public AQI/report, low-cost sensor, regulatory/archive, model, AOD/proxy, advisory, aggregate, candidate, and derived contexts must not collapse. |
| AQI/report is not concentration | Intake cannot turn an index/report posture into raw observed concentration. |
| AOD is not PM2.5 | Intake cannot turn AOD or remote-sensing proxy context into ground PM2.5 observations. |
| Model fields are not observations | Intake cannot turn model or forecast products into observed sensor records. |
| Advisory and health limits remain | Ingest receipts do not create emergency, medical, exposure, regulatory, or life-safety guidance. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Receipt families

The exact receipt subtype layout is not proven by this README. This lane may hold or reference Atmosphere ingest records such as:

| Receipt family | Purpose | Boundary |
|---|---|---|
| RunReceipt | Records governed intake run identity, spec hash, inputs, outputs, policy gates, and verification context. | Does not define Atmosphere object meaning by itself. |
| Ingest receipt / source-intake receipt | Records source head, retrieval, source-role, source descriptor ref, digest, admission decision, and handoff state. | Does not replace RAW payloads or SourceDescriptors. |
| ValidationReport | Records admission-time checks for source role, rights, timestamps, digest, schema sniffing, and basic boundary conditions. | Passing intake validation is not proof or release approval. |
| PolicyDecision reference | Records finite policy state for hold, deny, quarantine, allow-to-RAW, or allow-to-WORK handoff. | Policy authority remains in policy roots. |
| Correction / rollback support reference | Records intake correction, re-fetch, supersession, stale-source, or rollback support. | Correction and rollback authority remain in release governance. |

---

## Accepted material

Accepted content is limited to Atmosphere ingest receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source-intake, retrieval, source-head, admission, validation, policy-decision, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, SourceDescriptor refs, source-role refs, endpoint refs, request metadata summaries, retrieval times, source times, observed/valid/issue/expiry times where material, input refs, input hashes, output refs, output hashes, row/object counts, digest refs, evidence refs, policy refs, validator refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect ingest receipt state without becoming RAW payloads, source registry authority, proof, catalog, policy, release, public output, air-quality truth, advisory authority, or generated-answer authority.

Do not put raw source payloads, credentials, secrets, private tokens, full API responses, exact restricted station/private details, public health instructions, exposure determinations, regulatory-exceedance conclusions, emergency guidance, or unsupported source-as-authority claims into README/index text.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Atmosphere source feeds, station payloads, agency snapshots, QA payloads, logs, source-native records, or full API responses | `data/raw/atmosphere/` or governed restricted storage as applicable |
| Work/scratch transformations and normalized candidates | `data/work/atmosphere/` |
| Quarantined source material | `data/quarantine/atmosphere/` |
| Normalized Atmosphere payloads | `data/processed/atmosphere/` and child lanes |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| Pipeline executable logic | `pipelines/domains/atmosphere/` |
| Semantic contracts | `contracts/domains/atmosphere/` |
| Machine schemas | `schemas/contracts/v1/domains/atmosphere/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Source-role, rights, sensitivity, AQI/concentration, low-cost, AOD/model, advisory, freshness, publication, or release policy | `policy/` and governed policy roots |
| Validator code, fixtures, tests, package code, or CI workflows | `tools/`, `fixtures/`, `tests/`, `packages/`, `.github/workflows/` |
| Medical, exposure, emergency, regulatory, or life-safety conclusions | Official/governed advisory and release surfaces only, never this receipt lane alone |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/ingest/atmosphere/
├── README.md
├── <run_id>/
│   ├── run_receipt.json
│   ├── ingest_receipt.json
│   ├── validation_report.json
│   ├── policy_decision_ref.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted ingest receipts, source descriptors, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, source registry, policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records ingest process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, source role, rights, timestamps, hashes, source descriptor refs, evidence refs, policy refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Quarantine/correct | Intake contradicts source metadata, omits required role/time/citation/digest state, violates policy, lacks replay/signature support, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite this receipt as intake/validation/correction support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/ingest/atmosphere/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Atmosphere ingest receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Atmosphere domain and ingest/source-intake receipt lane.
- [ ] Confirm canonical ingest/domain receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, SourceDescriptor refs, source-role refs, input/output hashes, evidence refs, policy refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role distinguishes observed sensor, AQI/report, regulatory/archive, low-cost sensor, model context, AOD/proxy context, advisory context, aggregate, candidate, and derived context where applicable.
- [ ] Confirm source time, observed time, valid time, issue/expiry time, retrieval time, processing time, correction time, rights, citation, cadence, QA state, caveats, confidence, and limitations are preserved where material.
- [ ] Confirm EvidenceBundle/proof references resolve before using this ingest receipt in any public Atmosphere claim path.
- [ ] Confirm receipt presence is not treated as source truth, air-quality truth, accepted value truth, health guidance, regulatory-exceedance proof, policy authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when rights, source role, unit/AQI/AOD/model/advisory boundary, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, generated answer, exposure statement, regulatory claim, or life-safety guidance uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/ingest/atmosphere/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/ingest/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere parent receipt README defines Atmosphere receipts as process memory and not proof, catalog, release, public output, advisory authority, or health/life-safety guidance. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere RAW README says RAW captures source material and that receipt authority belongs to `data/receipts/`, not RAW. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/ingest/atmosphere/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Atmosphere ingest receipt payloads exist under this subtree. | **UNKNOWN** |
| Source descriptors, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, correction hooks, rollback hooks, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is raw source data, source registry authority, atmospheric truth, air-quality truth, proof, catalog authority, policy authority, release authority, public artifact authority, advisory authority, health/life-safety guidance, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../atmosphere/README.md`](../../atmosphere/README.md)
- [`../../../raw/atmosphere/README.md`](../../../raw/atmosphere/README.md)
- [`../../../work/atmosphere/README.md`](../../../work/atmosphere/README.md)
- [`../../../quarantine/atmosphere/README.md`](../../../quarantine/atmosphere/README.md)
- [`../../../processed/atmosphere/README.md`](../../../processed/atmosphere/README.md)
- [`../../../processed/atmosphere/pm25/README.md`](../../../processed/atmosphere/pm25/README.md)
- [`../../../catalog/domain/atmosphere/README.md`](../../../catalog/domain/atmosphere/README.md)
- [`../../../published/layers/atmosphere/README.md`](../../../published/layers/atmosphere/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/domains/atmosphere/README.md`](../../../../docs/domains/atmosphere/README.md)
- [`../../../../pipelines/domains/atmosphere/README.md`](../../../../pipelines/domains/atmosphere/README.md)
- [`../../../../pipelines/domains/atmosphere/normalize/README.md`](../../../../pipelines/domains/atmosphere/normalize/README.md)
- [`../../../../contracts/domains/atmosphere/PM25Observation.md`](../../../../contracts/domains/atmosphere/PM25Observation.md)
- [`../../../../contracts/domains/atmosphere/AirObservation.md`](../../../../contracts/domains/atmosphere/AirObservation.md)
- [`../../../../contracts/domains/atmosphere/AODRaster.md`](../../../../contracts/domains/atmosphere/AODRaster.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/ingest/atmosphere/` is an Atmosphere ingest receipt lane for process memory only. It is not raw source data, source registry authority, atmospheric truth, air-quality truth, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, advisory authority, health/life-safety guidance, or generated-answer truth.

[Back to top](#top)
