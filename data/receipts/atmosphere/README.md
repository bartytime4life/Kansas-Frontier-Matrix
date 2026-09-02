<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/atmosphere/readme
name: Atmosphere Receipts README
path: data/receipts/atmosphere/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <atmosphere-domain-steward>
  - <air-quality-steward>
  - <normalization-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: atmosphere-receipts
receipt_scope: atmosphere-domain-process-memory
domain: atmosphere
path_posture: domain-receipt-parent-lane; child-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-role-preserving; unit-conversion-not-silent-edit; aqi-concentration-boundary-required; aod-not-pm25; advisory-not-life-safety; release-blocked
related:
  - pm25_2026/README.md
  - unit_conversion/README.md
  - ../README.md
  - ../../README.md
  - ../../raw/atmosphere/README.md
  - ../../work/atmosphere/README.md
  - ../../processed/atmosphere/README.md
  - ../../processed/atmosphere/pm25/README.md
  - ../../proofs/README.md
  - ../../catalog/domain/atmosphere/README.md
  - ../../published/layers/atmosphere/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../pipelines/domains/atmosphere/normalize/README.md
  - ../../../pipelines/domains/atmosphere/validate/README.md
  - ../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../contracts/domains/atmosphere/OzoneObservation.md
  - ../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - atmosphere
  - air-quality
  - process-memory
  - pm25
  - unit-conversion
  - transform-receipt
  - validation-report
  - policy-decision
  - source-role
  - aqi-boundary
  - aod-boundary
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/atmosphere/README.md`."
  - "Confirmed child receipt README lanes during this edit: `pm25_2026/` and `unit_conversion/`."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "RunReceipt doctrine says receipts are emitted by governed runs, live under `data/receipts/`, and require fail-closed verification before promotion."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Receipts

Domain parent receipt lane for Atmosphere process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f9eda">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/atmosphere/` is for Atmosphere receipt process memory only. It is not air-quality truth, weather truth, climate truth, exposure truth, health guidance, advisory authority, regulatory-exceedance proof, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is the Atmosphere-domain parent lane for receipts that document governed process memory: source intake support, normalization, unit conversion, PM2.5-specific run support, validation, policy evaluation, correction support, rollback support, and release-support context.

Atmosphere receipts record what a process did, what references it inspected, what outcome or decision class it produced, what evidence, policy, source-role, unit, validation, correction, rollback, or release-candidate references should travel downstream, and what conditions block use.

Receipts do **not** prove atmospheric values, authorize publication, define object meaning, issue advisories, create health or life-safety guidance, establish regulatory exceedance, or replace contracts, schemas, SourceDescriptors, EvidenceBundles, ProofPacks, CatalogMatrix records, PolicyDecisions, ReleaseManifests, correction paths, rollback targets, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This domain parent lane is:

```text
data/receipts/atmosphere/
```

The child lanes `pm25_2026/` and `unit_conversion/` are confirmed as substantive README files in the current repository. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/atmosphere/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | atmosphere |
| Scope | Atmosphere process memory across source intake support, normalization, PM2.5 2026, unit conversion, validation, correction, rollback, and release-support steps |
| Path posture | domain receipt parent lane; exact subtype layout needs verification |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload lanes | `data/raw/atmosphere/`, `data/work/atmosphere/`, `data/processed/atmosphere/` where applicable |
| Pipeline logic authority | `pipelines/domains/atmosphere/`, not this lane |
| Contract authority | `contracts/domains/atmosphere/`, not this lane |
| Schema authority | `schemas/contracts/v1/domains/atmosphere/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when source role, rights, units, station context, AQI/report posture, low-cost caveats, AOD/model/advisory boundary, QA state, freshness, evidence refs, policy refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

The child lanes below are confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted receipts, schemas, validators, fixtures, CI checks, signing, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`pm25_2026/`](pm25_2026/README.md) | **CONFIRMED README** | PM2.5 2026 process memory for source intake, transform, normalization, unit checks, AQI/report role checks, low-cost caveat checks, validation, policy evaluation, correction support, rollback support, and release-support context. | Not PM2.5 truth, exposure truth, health guidance, regulatory-exceedance proof, advisory authority, proof, catalog, policy, release, or public artifact authority. |
| [`unit_conversion/`](unit_conversion/README.md) | **CONFIRMED README** | Unit-conversion process memory preserving source units, target units, conversion factors, method refs, parameter semantics, caveats, validation outcomes, policy refs, and correction/rollback support. | Not accepted value truth, unit-definition authority, semantic contract authority, schema authority, proof, policy, release, or public artifact authority. |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed Atmosphere processes did; it is not the truth source. |
| Source roles remain explicit | Observed sensor, public AQI/report, low-cost sensor, regulatory/archive, model, AOD/proxy, advisory, and derived contexts must not collapse. |
| Unit conversion is auditable | Original units, normalized units, conversion factors, method refs, and TransformReceipts must remain inspectable. |
| AQI/report is not concentration | Receipts cannot turn an index/report posture into raw observed concentration. |
| AOD is not PM2.5 | Receipts cannot turn AOD or remote-sensing proxy context into ground PM2.5 observations. |
| Model fields are not observations | Receipts cannot turn modeled or forecast fields into observed sensor records. |
| Advisory and health limits remain | Receipts do not create emergency, medical, exposure, regulatory, or life-safety guidance. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Atmosphere receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source/intake, transform, unit-conversion, validation, policy-decision, correction-support, rollback-support, and release-support receipt records;
- `TransformReceipt`, `ValidationReport`, `PolicyDecision`, correction-support receipts, rollback-support receipts, release-support receipts, and related process-memory records where applicable;
- run IDs, source refs, object refs, station/network refs, source roles, input refs, input/output hashes, output refs, method IDs, unit fields, conversion factors, formula/method refs, pollutant/variable identity, averaging periods, time facets, QA/correction posture, caveat refs, limitation refs, evidence refs, policy refs, validator refs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, air-quality truth, weather truth, climate truth, advisory authority, unit-definition authority, or generated-answer authority.

Do not put raw payloads, normalized data payloads, public health instructions, exposure determinations, regulatory-exceedance conclusions, emergency guidance, exact sensitive station details, private-party details, or unsupported AQI/AOD/model-as-observation claims in README/index text.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Atmosphere source feeds, station payloads, agency snapshots, satellite/model downloads, QA payloads, logs, or source-native records | `data/raw/atmosphere/` |
| Work/scratch transformations and candidate payloads | `data/work/atmosphere/` |
| Quarantined, rights-unclear, source-role-unclear, stale, malformed, unit-unclear, unsupported, disputed, or unsafe Atmosphere material | `data/quarantine/atmosphere/` |
| Normalized processed Atmosphere payloads | `data/processed/atmosphere/` and child lanes |
| Pipeline logic | `pipelines/domains/atmosphere/` |
| Semantic contracts | `contracts/domains/atmosphere/` |
| Machine schemas | `schemas/contracts/v1/domains/atmosphere/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Air-quality, unit, AQI/concentration, low-cost, AOD/model, advisory, freshness, sensitivity, validation, or release policy | `policy/` and governed policy roots |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Medical, exposure, emergency, regulatory, or life-safety conclusions | Official/governed advisory and release surfaces only, never this receipt lane alone |

---

## Directory map

```text
data/receipts/atmosphere/
├── README.md
├── pm25_2026/
│   └── README.md
├── unit_conversion/
│   └── README.md
└── index.local.json
```

This map confirms the README child lanes currently documented. It does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, air-quality truth index, unit-definition authority, policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, source roles, unit fields, hashes, signatures, evidence refs, policy refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Quarantine/correct | Receipt contradicts inputs, omits required units/method/caveats, violates source-role policy, lacks replay/signature support, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite a receipt as process/transform/validation/correction support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/atmosphere/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Atmosphere receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Atmosphere domain and a documented child receipt lane.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, subject/source refs, station/network refs, input/output hashes, evidence refs, policy refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role distinguishes observed concentration, AQI/report, regulatory/archive, low-cost sensor, model context, AOD context, advisory context, and derived context where applicable.
- [ ] Confirm unit conversion preserves original units, normalized units, conversion factors, method refs, pollutant/variable identity, averaging period, time facets, QA state, correction lineage, freshness, caveats, confidence, and limitations where material.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public Atmosphere claim path.
- [ ] Confirm receipt presence is not treated as accepted value truth, air-quality truth, exposure truth, health guidance, regulatory-exceedance proof, policy authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when rights, units, source role, low-cost caveat, AQI/concentration boundary, AOD/model boundary, advisory boundary, evidence, policy, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, generated answer, exposure statement, regulatory claim, or life-safety guidance uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/atmosphere/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lanes during this edit: `pm25_2026/` and `unit_conversion/`. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere receipt child README presence proves emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/atmosphere/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Atmosphere receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is air-quality truth, weather truth, climate truth, exposure truth, health guidance, advisory authority, regulatory-exceedance proof, proof, catalog authority, registry authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`pm25_2026/README.md`](pm25_2026/README.md)
- [`unit_conversion/README.md`](unit_conversion/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/atmosphere/README.md`](../../raw/atmosphere/README.md)
- [`../../work/atmosphere/README.md`](../../work/atmosphere/README.md)
- [`../../processed/atmosphere/README.md`](../../processed/atmosphere/README.md)
- [`../../processed/atmosphere/pm25/README.md`](../../processed/atmosphere/pm25/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/domain/atmosphere/README.md`](../../catalog/domain/atmosphere/README.md)
- [`../../published/layers/atmosphere/README.md`](../../published/layers/atmosphere/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/domains/atmosphere/README.md`](../../../docs/domains/atmosphere/README.md)
- [`../../../docs/domains/atmosphere/DATA_LIFECYCLE.md`](../../../docs/domains/atmosphere/DATA_LIFECYCLE.md)
- [`../../../pipelines/domains/atmosphere/normalize/README.md`](../../../pipelines/domains/atmosphere/normalize/README.md)
- [`../../../pipelines/domains/atmosphere/validate/README.md`](../../../pipelines/domains/atmosphere/validate/README.md)
- [`../../../contracts/domains/atmosphere/PM25Observation.md`](../../../contracts/domains/atmosphere/PM25Observation.md)
- [`../../../contracts/domains/atmosphere/AirObservation.md`](../../../contracts/domains/atmosphere/AirObservation.md)
- [`../../../contracts/domains/atmosphere/OzoneObservation.md`](../../../contracts/domains/atmosphere/OzoneObservation.md)
- [`../../../contracts/domains/atmosphere/AODRaster.md`](../../../contracts/domains/atmosphere/AODRaster.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/atmosphere/` is an Atmosphere receipt parent lane for process memory only. It is not air-quality truth, weather truth, climate truth, exposure truth, health guidance, advisory authority, regulatory-exceedance proof, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
