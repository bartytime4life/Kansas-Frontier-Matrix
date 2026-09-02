<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/pipeline/flora/readme
name: Flora Pipeline Receipts README
path: data/receipts/pipeline/flora/README.md
type: data-receipts-pipeline-domain-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <pipeline-steward>
  - <flora-domain-steward>
  - <geoprivacy-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: flora-pipeline-receipts
receipt_scope: flora-pipeline-process-memory
domain: flora
path_posture: requested-pipeline-domain-receipt-lane; pipeline-parent-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; pipeline-run-not-release; executable-logic-separate; rare-flora-fail-closed; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../flora/README.md
  - ../../flora/redaction/README.md
  - ../../../raw/flora/README.md
  - ../../../work/flora/README.md
  - ../../../quarantine/flora/README.md
  - ../../../processed/flora/README.md
  - ../../../proofs/README.md
  - ../../../../release/manifests/README.md
  - ../../../../pipelines/domains/flora/README.md
  - ../../../../pipelines/domains/flora/normalize/README.md
  - ../../../../pipelines/domains/flora/redact/README.md
  - ../../../../pipelines/domains/flora/validate/README.md
  - ../../../../pipeline_specs/flora/README.md
  - ../../../../contracts/domains/flora/rare_plant_record.md
  - ../../../../contracts/domains/flora/flora_occurrence.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - pipeline
  - flora
  - normalize
  - transform-receipt
  - redaction-receipt
  - validation-report
  - model-run-receipt
  - source-role
  - geoprivacy
  - rare-flora
  - no-public-path
  - evidence-first
notes:
  - "This README replaces a blank placeholder at `data/receipts/pipeline/flora/README.md`."
  - "Parent `data/receipts/pipeline/README.md` is currently a greenfield stub."
  - "Flora pipeline docs say pipeline logic is implementation support only and does not own object meaning, schemas, source descriptors, policy, lifecycle data, catalog truth, geoprivacy decisions, or release decisions."
  - "Flora normalize docs say normalization preserves source identity, source role, taxonomic uncertainty, geoprivacy state, evidence state, and lifecycle state, and prevents pipeline-run-to-release collapse."
  - "README presence confirms documentation only; it does not prove emitted pipeline receipts, executable behavior, validators, CI checks, signing, evidence closure, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Pipeline Receipts

Pipeline receipt lane for Flora pipeline-run process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Lane: pipeline" src="https://img.shields.io/badge/lane-pipeline-blue">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/pipeline/flora/` is for Flora pipeline-run receipt process memory only. It is not pipeline code, pipeline specification authority, raw source data, accepted Flora truth, exact-location authority, sensitivity policy, proof, catalog authority, policy authority, release authority, public artifact authority, public UI material, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document governed Flora pipeline activity: normalization runs, transform runs, redaction/geoprivacy handoffs, validation handoffs, taxonomic-candidate handling, occurrence/specimen candidate handling, quarantine routing, correction support, rollback support, and release-candidate support.

Pipeline receipts record what a pipeline run did, what specification or executable context it used, what inputs and outputs were referenced, what hashes and policy, review, transform, or validation outcomes apply, and what downstream proof or release artifacts may inspect the receipt.

Pipeline receipts do **not** prove Flora occurrence, approve release, publish public artifacts, define object meaning, define schemas, decide taxonomic truth, decide geoprivacy, fetch source data, admit sources, decide policy, or replace contracts, schemas, SourceDescriptors, ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, or RollbackCards.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested pipeline/domain receipt lane is:

```text
data/receipts/pipeline/flora/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/pipeline/README.md` is still a greenfield stub. The exact choice between `data/receipts/pipeline/<domain>/` and `data/receipts/<domain>/pipeline/` remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/pipeline/flora/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | pipeline / executable-run process memory |
| Domain lane | flora |
| Parent root | `data/receipts/pipeline/` |
| Related domain receipt parent | `data/receipts/flora/` |
| Pipeline logic authority | `pipelines/domains/flora/`, not this lane |
| Pipeline spec authority | `pipeline_specs/flora/` or accepted spec home, not this lane |
| Lifecycle payload authority | `data/raw/`, `data/work/`, `data/quarantine/`, and `data/processed/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when executable refs, spec refs, source role, taxonomy state, sensitivity state, review state, transform state, input/output hashes, evidence refs, policy refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what the pipeline run did; it is not the truth source. |
| Pipeline run is not release | A successful run can create candidates, receipts, and handoffs; it cannot publish or approve release. |
| Executable logic stays separate | Code belongs under `pipelines/`; receipts under `data/receipts/` record run memory and references. |
| Specs stay separate | Declarative run specs belong under accepted `pipeline_specs/` homes, not this receipt lane. |
| Taxonomic uncertainty stays visible | Candidate names, accepted-name refs, synonym refs, and steward-review refs must not collapse into taxonomic truth. |
| Sensitive Flora fails closed | Sensitive or unresolved Flora records require governed transform, review, evidence, policy, correction, and rollback support before public use. |
| Geometry state stays protected | README/index text must not expose sensitive coordinates, transform parameters, or restricted stewardship detail. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Flora pipeline receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- transform, normalization, redaction/geoprivacy, validation, model-materialization, policy-decision, review-reference, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, pipeline refs, spec refs, executable refs, input refs, input hashes, output refs, output hashes, evidence refs, policy refs, reviewer refs, validator refs, source-role refs, taxonomic refs, transform refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect pipeline receipt state without becoming executable code, pipeline spec authority, proof, catalog, policy, release, public output, Flora truth, exact-location authority, sensitivity policy, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Pipeline executable code, adapters, normalizers, validator wrappers, or handoff helpers | `pipelines/domains/flora/` |
| Declarative pipeline specs | `pipeline_specs/flora/` or accepted spec home |
| Raw source captures or source-native records | `data/raw/flora/` |
| Work/candidate outputs | `data/work/flora/` |
| Quarantined source or pipeline outputs | `data/quarantine/flora/` |
| Normalized processed Flora payloads | `data/processed/flora/` and child lanes |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Sensitivity, geoprivacy, rights, source-role, publication, or release policy | `policy/` and governed policy roots |
| Tests, fixtures, package code, or CI workflows | `tests/`, `fixtures/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/pipeline/flora/
├── README.md
├── <run_id>/
│   ├── run_receipt.json
│   ├── transform_receipt.json
│   ├── validation_report.json
│   ├── policy_decision_ref.json
│   ├── review_record_ref.json
│   ├── checksums.sha256
│   └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted pipeline receipts, executable behavior, validators, fixtures, CI checks, signing, evidence closure, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, pipeline spec, policy authority, exact-location authority, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Flora domain and pipeline-run receipt lane.
- [ ] Confirm canonical pipeline/domain receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, pipeline refs, executable refs, spec refs, input/output hashes, evidence refs, policy refs, reviewer refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, taxonomic uncertainty, geometry/geoprivacy posture, review state, caveats, and limitations are preserved where material.
- [ ] Confirm exact sensitive coordinates, transform parameters, and restricted stewardship details are not exposed in README/index text.
- [ ] Confirm EvidenceBundle/proof references resolve before using this pipeline receipt in any public Flora claim path.
- [ ] Confirm receipt presence is not treated as executable behavior proof, accepted botanical truth, exact-location authority, sensitivity policy, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when executable/spec identity, source role, sensitivity, review, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, species page, generated answer, or released layer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/pipeline/flora/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/pipeline/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Flora pipeline docs say executable pipeline logic is implementation support only and cannot own object meaning, schemas, policy, lifecycle data, catalog truth, geoprivacy decisions, or release decisions. | **CONFIRMED by GitHub contents API during this edit** |
| Flora normalize docs say normalization must preserve source identity, source role, taxonomic uncertainty, geoprivacy state, evidence state, and lifecycle state while preventing pipeline-run-to-release collapse. | **CONFIRMED by GitHub contents API during this edit** |
| Flora receipt docs define Flora receipts as process memory and not rare-plant truth, exact-location authority, sensitivity policy, proof, release approval, or public artifact authority. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/pipeline/flora/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Flora pipeline receipt payloads exist under this subtree. | **UNKNOWN** |
| Executable behavior, validators, fixtures, CI checks, signing, evidence closure, correction hooks, rollback hooks, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is pipeline code, pipeline spec authority, raw source data, accepted Flora truth, exact-location authority, sensitivity policy, proof, catalog authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../flora/README.md`](../../flora/README.md)
- [`../../flora/redaction/README.md`](../../flora/redaction/README.md)
- [`../../../raw/flora/README.md`](../../../raw/flora/README.md)
- [`../../../work/flora/README.md`](../../../work/flora/README.md)
- [`../../../quarantine/flora/README.md`](../../../quarantine/flora/README.md)
- [`../../../processed/flora/README.md`](../../../processed/flora/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../pipelines/domains/flora/README.md`](../../../../pipelines/domains/flora/README.md)
- [`../../../../pipelines/domains/flora/normalize/README.md`](../../../../pipelines/domains/flora/normalize/README.md)
- [`../../../../pipelines/domains/flora/redact/README.md`](../../../../pipelines/domains/flora/redact/README.md)
- [`../../../../pipelines/domains/flora/validate/README.md`](../../../../pipelines/domains/flora/validate/README.md)
- [`../../../../pipeline_specs/flora/README.md`](../../../../pipeline_specs/flora/README.md)
- [`../../../../contracts/domains/flora/rare_plant_record.md`](../../../../contracts/domains/flora/rare_plant_record.md)
- [`../../../../contracts/domains/flora/flora_occurrence.md`](../../../../contracts/domains/flora/flora_occurrence.md)
- [`../../../../docs/domains/flora/SENSITIVITY.md`](../../../../docs/domains/flora/SENSITIVITY.md)
- [`../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md`](../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/pipeline/flora/` is a Flora pipeline receipt lane for process memory only. It is not pipeline code, pipeline spec authority, source data, Flora truth, exact-location authority, sensitivity policy, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
