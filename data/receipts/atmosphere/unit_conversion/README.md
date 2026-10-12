<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/atmosphere/unit-conversion/readme
name: Atmosphere Unit Conversion Receipts README
path: data/receipts/atmosphere/unit_conversion/README.md
type: data-receipts-domain-transform-lane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <atmosphere-domain-steward>
  - <normalization-steward>
  - <unit-conversion-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: atmosphere-unit-conversion-receipts
receipt_scope: atmosphere-unit-conversion-process-memory
domain: atmosphere
path_posture: requested-domain-transform-receipt-lane; parent-atmosphere-receipt-root-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; unit-conversion-not-silent-edit; aqi-concentration-boundary-required; aod-not-pm25; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../raw/atmosphere/README.md
  - ../../../work/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../processed/atmosphere/pm25/README.md
  - ../../../processed/atmosphere/ozone/README.md
  - ../../../processed/atmosphere/air_observations/README.md
  - ../../../proofs/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../published/layers/atmosphere/README.md
  - ../../../../release/manifests/README.md
  - ../../../../pipelines/domains/atmosphere/normalize/README.md
  - ../../../../pipelines/domains/atmosphere/validate/README.md
  - ../../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../../contracts/domains/atmosphere/OzoneObservation.md
  - ../../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - atmosphere
  - unit-conversion
  - transform-receipt
  - normalization
  - units
  - conversion-factor
  - method-ref
  - pm25
  - ozone
  - aqi-boundary
  - aod-boundary
  - no-public-path
  - evidence-first
notes:
  - "This README replaces a blank placeholder at `data/receipts/atmosphere/unit_conversion/README.md`."
  - "Parent `data/receipts/atmosphere/README.md` is currently a greenfield stub."
  - "Atmosphere normalize doctrine says unit conversion must not be a silent edit and original source units, normalized units, conversion factors, method refs, and TransformReceipts remain auditable."
  - "PM2.5 processed and contract docs require units, averaging period, source role, AQI/report posture, low-cost caveats, AOD boundaries, evidence, policy, and release posture to remain explicit."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted unit conversion receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, evidence closure, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Unit Conversion Receipts

Receipt lane for Atmosphere unit-conversion process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f9eda">
  <img alt="Lane: unit conversion" src="https://img.shields.io/badge/lane-unit__conversion-7048e8">
  <img alt="Posture: auditable" src="https://img.shields.io/badge/posture-auditable-blue">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Unit-conversion receipt boundary](#unit-conversion-receipt-boundary) · [Receipt families](#receipt-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/atmosphere/unit_conversion/` is for Atmosphere unit-conversion receipt process memory only. It is not normalized data, air-quality truth, unit-definition authority, semantic contract authority, schema authority, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document Atmosphere unit-conversion work: preserving source units, target units, conversion factors, methods, formulas, parameter semantics, averaging-period context, timestamp context, station/network context, source-role posture, caveats, validation outcomes, policy references, and downstream correction or rollback support.

Unit-conversion receipts record what conversion or normalization step happened. They can support review, validation, proof, catalog, and release paths, but they do **not** prove an atmospheric value, define object meaning, authorize public use, or replace contracts, schemas, policy, EvidenceBundles, ProofPacks, ReleaseManifests, correction paths, or rollback targets.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested Atmosphere unit-conversion lane is:

```text
data/receipts/atmosphere/unit_conversion/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/atmosphere/README.md` is still a greenfield stub, and exact domain/transform receipt subfolder naming remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/atmosphere/unit_conversion/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | atmosphere |
| Transform scope | Unit conversion / unit normalization process memory |
| Path posture | requested domain/transform receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/atmosphere/` |
| Lifecycle payload lanes | `data/raw/atmosphere/`, `data/work/atmosphere/`, `data/processed/atmosphere/` where applicable |
| Pipeline logic authority | `pipelines/domains/atmosphere/normalize/`, not this lane |
| Contract authority | `contracts/domains/atmosphere/`, not this lane |
| Schema authority | `schemas/contracts/v1/domains/atmosphere/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when original units, target units, conversion factor, method reference, parameter semantics, source role, averaging period, caveats, validation state, evidence refs, policy refs, correction path, rollback target, or release state are insufficient |

---

## Unit-conversion receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records conversion behavior, not atmospheric truth or accepted public truth. |
| Conversion is not a silent edit | Original source units, normalized units, conversion factors, method refs, and TransformReceipts must remain auditable. |
| Object meaning stays in contracts | PM2.5, ozone, temperature, precipitation, wind, AOD, smoke, model, and advisory object semantics live in contracts/docs. |
| AQI/report is not concentration | Unit conversion cannot turn an AQI/report posture into observed concentration. |
| AOD is not PM2.5 | Unit conversion cannot turn remote-sensing AOD/proxy values into ground PM2.5 observations. |
| Model fields are not observations | Unit conversion cannot turn model/forecast values into observed sensor records. |
| Low-cost caveats travel | Unit conversion cannot remove caveat, correction, confidence, limitation, QA, freshness, or policy requirements. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, correction notices, rollback cards, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Receipt families

The exact receipt subtype layout is not proven by this README. This lane may hold or reference Atmosphere unit-conversion records such as:

| Receipt family | Purpose | Boundary |
|---|---|---|
| TransformReceipt | Records conversion from source-unit fields to normalized-unit fields, with input/output hashes and method refs. | Does not prove converted value is correct or publishable by itself. |
| ValidationReport | Records unit validation, impossible-value checks, range checks, averaging-period checks, and source-role boundary checks. | Passing validation is not proof or release approval. |
| PolicyDecision reference | Records finite policy state where unit ambiguity, low-cost caveats, freshness, or source-role boundary affects use. | Policy authority remains in policy roots. |
| Correction receipt/reference | Records correction, recalibration, unit-fix, supersession, or caveat update. | Correction authority remains in governed correction/release lanes. |
| Rollback-support receipt | Records prior value state, affected outputs, and rollback target support. | Rollback authority remains in release governance. |
| Release-support receipt | Records process support for a release candidate. | Release decision remains in `release/`. |

---

## Accepted material

Accepted content is limited to unit-conversion receipt instances and receipt-local sidecars:

- TransformReceipt JSON or JSONL records for Atmosphere unit conversions;
- validation, policy-decision, correction-support, rollback-support, and release-support receipt records tied to conversion work;
- run IDs, source refs, object refs, station/network refs, source roles, input refs, input hashes, output refs, output hashes, source unit, target unit, conversion factor, method ID, method version, formula ID, parameter code, pollutant/variable identity, averaging period, observed/valid/retrieval/processing times, QA state, caveat refs, limitation refs, evidence refs, policy refs, validator refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect unit-conversion receipt state without becoming proof, catalog, policy, release, public output, air-quality truth, unit-definition authority, or generated-answer authority.

Do not put raw payloads, normalized data payloads, public health instructions, exposure determinations, regulatory-exceedance conclusions, emergency guidance, exact sensitive station details, private-party details, or unsupported AQI/AOD/model-as-observation claims in README/index text.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Atmosphere source feeds, station payloads, agency snapshots, QA payloads, logs, or source-native records | `data/raw/atmosphere/` |
| Work/scratch transformations and converted candidate payloads | `data/work/atmosphere/` |
| Quarantined unit-unclear or source-role-unclear material | `data/quarantine/atmosphere/` |
| Normalized processed Atmosphere payloads | `data/processed/atmosphere/` and child lanes |
| Unit-conversion pipeline logic | `pipelines/domains/atmosphere/normalize/` |
| Semantic contracts | `contracts/domains/atmosphere/` |
| Machine schemas | `schemas/contracts/v1/domains/atmosphere/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Air-quality, unit, AQI/concentration, low-cost, AOD/model, advisory, freshness, sensitivity, or release policy | `policy/` and governed policy roots |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Medical, exposure, emergency, regulatory, or life-safety conclusions | Official/governed advisory and release surfaces only, never this receipt lane alone |

---

## Directory map

```text
data/receipts/atmosphere/unit_conversion/
├── README.md
├── <run_id>/
│   ├── transform_receipt.json
│   ├── validation_report.json
│   ├── policy_decision_ref.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
├── corrections/
│   └── <run_id>/
│       └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, schemas, validators, fixtures, CI checks, signing, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, air-quality truth index, unit-definition authority, policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records unit-conversion process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, source units, target units, conversion factor, method reference, hashes, signatures, evidence refs, policy refs, validation state, or decision scope are incomplete. |
| Quarantine/correct | Receipt contradicts inputs, omits required units/method/caveats, violates source-role policy, lacks replay/signature support, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite the receipt as transform/validation/correction support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/atmosphere/unit_conversion/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Unit-conversion receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Atmosphere domain and unit-conversion receipt lane.
- [ ] Confirm canonical domain/transform receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, subject/source refs, station/network refs, input/output hashes, original units, normalized units, conversion factor, method refs, evidence refs, policy refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role distinguishes observed concentration, AQI/report, regulatory/archive, low-cost sensor, model context, AOD context, and advisory context where applicable.
- [ ] Confirm unit conversion preserves pollutant/variable identity, averaging period, time facets, QA state, correction lineage, freshness, caveats, confidence, and limitations where material.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public Atmosphere claim path.
- [ ] Confirm receipt presence is not treated as accepted value truth, air-quality truth, exposure truth, health guidance, regulatory-exceedance proof, policy authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when units, source role, low-cost caveat, AQI/concentration boundary, AOD/model boundary, advisory boundary, evidence, policy, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, generated answer, exposure statement, regulatory claim, or life-safety guidance uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/atmosphere/unit_conversion/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/atmosphere/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere normalize pipeline docs say unit conversion must not be a silent edit and original units, normalized units, conversion factors, method refs, and TransformReceipts remain auditable. | **CONFIRMED by GitHub contents API during this edit** |
| PM2.5 processed docs require pollutant identity, source role, units, averaging period, observed/retrieval/source time, QA, caveats, confidence, limitations, evidence, and release posture to remain explicit. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/atmosphere/unit_conversion/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual unit-conversion receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, policy enforcement, evidence closure, correction hooks, rollback hooks, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is accepted value truth, air-quality truth, exposure truth, unit-definition authority, health guidance, regulatory-exceedance proof, proof, catalog authority, registry authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../raw/atmosphere/README.md`](../../../raw/atmosphere/README.md)
- [`../../../work/atmosphere/README.md`](../../../work/atmosphere/README.md)
- [`../../../processed/atmosphere/README.md`](../../../processed/atmosphere/README.md)
- [`../../../processed/atmosphere/pm25/README.md`](../../../processed/atmosphere/pm25/README.md)
- [`../../../processed/atmosphere/ozone/README.md`](../../../processed/atmosphere/ozone/README.md)
- [`../../../processed/atmosphere/air_observations/README.md`](../../../processed/atmosphere/air_observations/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../catalog/domain/atmosphere/README.md`](../../../catalog/domain/atmosphere/README.md)
- [`../../../published/layers/atmosphere/README.md`](../../../published/layers/atmosphere/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../pipelines/domains/atmosphere/normalize/README.md`](../../../../pipelines/domains/atmosphere/normalize/README.md)
- [`../../../../pipelines/domains/atmosphere/validate/README.md`](../../../../pipelines/domains/atmosphere/validate/README.md)
- [`../../../../contracts/domains/atmosphere/PM25Observation.md`](../../../../contracts/domains/atmosphere/PM25Observation.md)
- [`../../../../contracts/domains/atmosphere/OzoneObservation.md`](../../../../contracts/domains/atmosphere/OzoneObservation.md)
- [`../../../../contracts/domains/atmosphere/AirObservation.md`](../../../../contracts/domains/atmosphere/AirObservation.md)
- [`../../../../contracts/domains/atmosphere/AODRaster.md`](../../../../contracts/domains/atmosphere/AODRaster.md)
- [`../../../../docs/domains/atmosphere/README.md`](../../../../docs/domains/atmosphere/README.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/atmosphere/unit_conversion/` is an Atmosphere unit-conversion receipt lane for process memory only. It is not accepted value truth, air-quality truth, exposure truth, unit-definition authority, health guidance, regulatory-exceedance proof, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
