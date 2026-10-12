<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/pipeline/atmosphere/readme
name: Atmosphere Pipeline Receipts README
path: data/receipts/pipeline/atmosphere/README.md
type: data-receipts-pipeline-domain-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <pipeline-steward>
  - <atmosphere-domain-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: atmosphere-pipeline-receipts
receipt_scope: atmosphere-pipeline-process-memory
domain: atmosphere
path_posture: requested-pipeline-domain-receipt-lane; pipeline-parent-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; pipeline-run-not-release; executable-logic-separate; source-role-preserving; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../atmosphere/README.md
  - ../../atmosphere/unit_conversion/README.md
  - ../../atmosphere/pm25_2026/README.md
  - ../../../raw/atmosphere/README.md
  - ../../../work/atmosphere/README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../proofs/README.md
  - ../../../../release/manifests/README.md
  - ../../../../pipelines/domains/atmosphere/README.md
  - ../../../../pipelines/domains/atmosphere/normalize/README.md
  - ../../../../pipeline_specs/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/PM25Observation.md
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
  - pipeline
  - atmosphere
  - transform-receipt
  - validation-report
  - model-run-receipt
  - unit-conversion
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces a blank placeholder at `data/receipts/pipeline/atmosphere/README.md`."
  - "Parent `data/receipts/pipeline/README.md` is currently a greenfield stub."
  - "Atmosphere pipeline docs say pipeline logic is implementation support only and does not own object meaning, schemas, source descriptors, policy, lifecycle data, catalog truth, or release decisions."
  - "Atmosphere normalize docs say normalization preserves source roles, units, time facets, caveats, freshness, and receipts, and prevents pipeline-run-to-release collapse."
  - "README presence confirms documentation only; it does not prove emitted pipeline receipts, executable behavior, validators, CI checks, signing, evidence closure, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Pipeline Receipts

Pipeline receipt lane for Atmosphere pipeline-run process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Lane: pipeline" src="https://img.shields.io/badge/lane-pipeline-blue">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f9eda">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/pipeline/atmosphere/` is for Atmosphere pipeline-run receipt process memory only. It is not pipeline code, pipeline specification authority, raw source data, processed Atmosphere truth, proof, catalog authority, policy authority, release authority, public artifact authority, public UI material, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document governed Atmosphere pipeline activity: normalization runs, transform runs, validation handoffs, unit-conversion support, model-materialization support, caveat and freshness preservation, quarantine routing, correction support, rollback support, and release-candidate support.

Pipeline receipts record what a pipeline run did, what specification or executable context it used, what inputs and outputs were referenced, what hashes and policy or validation outcomes apply, and what downstream proof or release artifacts may inspect the receipt.

Pipeline receipts do **not** prove atmospheric values, approve release, publish public artifacts, define object meaning, define schemas, fetch source data, admit sources, decide policy, or replace contracts, schemas, SourceDescriptors, EvidenceBundles, ProofPacks, CatalogMatrix records, PolicyDecisions, ReleaseManifests, CorrectionNotices, or RollbackCards.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested pipeline/domain receipt lane is:

```text
data/receipts/pipeline/atmosphere/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/pipeline/README.md` is still a greenfield stub. The exact choice between `data/receipts/pipeline/<domain>/` and `data/receipts/<domain>/pipeline/` remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/pipeline/atmosphere/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | pipeline / executable-run process memory |
| Domain lane | atmosphere |
| Parent root | `data/receipts/pipeline/` |
| Related domain receipt parent | `data/receipts/atmosphere/` |
| Pipeline logic authority | `pipelines/domains/atmosphere/`, not this lane |
| Pipeline spec authority | `pipeline_specs/atmosphere/` or accepted spec home, not this lane |
| Lifecycle payload authority | `data/raw/`, `data/work/`, `data/quarantine/`, and `data/processed/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when executable refs, spec refs, source role, units, time facets, caveats, input/output hashes, evidence refs, policy refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what the pipeline run did; it is not the truth source. |
| Pipeline run is not release | A successful run can create candidates, receipts, and handoffs; it cannot publish or approve release. |
| Executable logic stays separate | Code belongs under `pipelines/`; receipts under `data/receipts/` record run memory and references. |
| Specs stay separate | Declarative run specs belong under accepted `pipeline_specs/` homes, not this receipt lane. |
| Source roles remain explicit | Observed, modeled, report, archive, aggregate, candidate, and derived contexts must not collapse. |
| Units and conversions stay auditable | Original units, normalized units, conversion factors, method refs, and TransformReceipts remain inspectable. |
| Time facets stay distinct | Observed, valid, issue, expiry, model-run, retrieval, processing, release, and correction times remain separate where material. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Atmosphere pipeline receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- transform, normalization, unit-conversion, validation, model-materialization, policy-decision, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, pipeline refs, spec refs, executable refs, input refs, input hashes, output refs, output hashes, evidence refs, policy refs, validator refs, source-role refs, unit refs, time-facet refs, caveat refs, freshness refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect pipeline receipt state without becoming executable code, pipeline spec authority, proof, catalog, policy, release, public output, Atmosphere truth, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Pipeline executable code, adapters, normalizers, validator wrappers, or handoff helpers | `pipelines/domains/atmosphere/` |
| Declarative pipeline specs | `pipeline_specs/atmosphere/` or accepted spec home |
| Raw source captures or source-native records | `data/raw/atmosphere/` |
| Work/candidate outputs | `data/work/atmosphere/` |
| Quarantined source or pipeline outputs | `data/quarantine/atmosphere/` |
| Normalized processed Atmosphere payloads | `data/processed/atmosphere/` and child lanes |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Policy bundles | `policy/` and governed policy roots |
| Tests, fixtures, package code, or CI workflows | `tests/`, `fixtures/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/pipeline/atmosphere/
├── README.md
├── <run_id>/
│   ├── run_receipt.json
│   ├── transform_receipt.json
│   ├── validation_report.json
│   ├── policy_decision_ref.json
│   ├── checksums.sha256
│   └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted pipeline receipts, executable behavior, validators, fixtures, CI checks, signing, evidence closure, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, pipeline spec, policy authority, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Atmosphere domain and pipeline-run receipt lane.
- [ ] Confirm canonical pipeline/domain receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, pipeline refs, executable refs, spec refs, input/output hashes, evidence refs, policy refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, original units, normalized units, conversion factors, relevant time facets, caveats, freshness, and limitations are preserved where material.
- [ ] Confirm EvidenceBundle/proof references resolve before using this pipeline receipt in any public Atmosphere claim path.
- [ ] Confirm receipt presence is not treated as executable behavior proof, accepted value truth, policy authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when executable/spec identity, source role, units, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, generated answer, or released layer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/pipeline/atmosphere/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/pipeline/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere pipeline docs say executable pipeline logic is implementation support only and cannot own object meaning, schemas, policy, lifecycle data, catalog truth, or release decisions. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere normalize docs say normalization must preserve source roles, units, time facets, caveats, freshness, evidence state, and lifecycle state while preventing pipeline-run-to-release collapse. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere receipt docs define Atmosphere receipts as process memory and not proof, release, or public artifact authority. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/pipeline/atmosphere/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Atmosphere pipeline receipt payloads exist under this subtree. | **UNKNOWN** |
| Executable behavior, validators, fixtures, CI checks, signing, evidence closure, correction hooks, rollback hooks, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is pipeline code, pipeline spec authority, raw source data, processed Atmosphere truth, proof, catalog authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../atmosphere/README.md`](../../atmosphere/README.md)
- [`../../atmosphere/unit_conversion/README.md`](../../atmosphere/unit_conversion/README.md)
- [`../../atmosphere/pm25_2026/README.md`](../../atmosphere/pm25_2026/README.md)
- [`../../../raw/atmosphere/README.md`](../../../raw/atmosphere/README.md)
- [`../../../work/atmosphere/README.md`](../../../work/atmosphere/README.md)
- [`../../../quarantine/atmosphere/README.md`](../../../quarantine/atmosphere/README.md)
- [`../../../processed/atmosphere/README.md`](../../../processed/atmosphere/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../pipelines/domains/atmosphere/README.md`](../../../../pipelines/domains/atmosphere/README.md)
- [`../../../../pipelines/domains/atmosphere/normalize/README.md`](../../../../pipelines/domains/atmosphere/normalize/README.md)
- [`../../../../pipeline_specs/atmosphere/README.md`](../../../../pipeline_specs/atmosphere/README.md)
- [`../../../../contracts/domains/atmosphere/PM25Observation.md`](../../../../contracts/domains/atmosphere/PM25Observation.md)
- [`../../../../contracts/domains/atmosphere/AirObservation.md`](../../../../contracts/domains/atmosphere/AirObservation.md)
- [`../../../../contracts/domains/atmosphere/AODRaster.md`](../../../../contracts/domains/atmosphere/AODRaster.md)
- [`../../../../docs/domains/atmosphere/README.md`](../../../../docs/domains/atmosphere/README.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/pipeline/atmosphere/` is an Atmosphere pipeline receipt lane for process memory only. It is not pipeline code, pipeline spec authority, source data, Atmosphere truth, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
