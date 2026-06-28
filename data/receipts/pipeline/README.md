<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/pipeline/readme
name: Pipeline Receipts README
path: data/receipts/pipeline/README.md
type: data-receipts-pipeline-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <pipeline-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: pipeline-receipts
receipt_scope: pipeline-run-process-memory
path_posture: pipeline-receipt-parent-lane; atmosphere-and-flora-child-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; pipeline-run-not-release; executable-logic-separate; release-blocked
related:
  - atmosphere/README.md
  - flora/README.md
  - ../README.md
  - ../../README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../../release/manifests/README.md
  - ../../../pipelines/README.md
  - ../../../pipeline_specs/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - pipeline
  - process-memory
  - run-receipt
  - transform-receipt
  - validation-report
  - policy-decision
  - release-gated
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/receipts/pipeline/README.md`."
  - "Confirmed child receipt README lanes during this edit: `atmosphere/` and `flora/`."
  - "Exact pipeline receipt layout remains NEEDS VERIFICATION until accepted receipt-layout governance or ADR review confirms it."
  - "README presence confirms documentation only; it does not prove emitted pipeline receipts, executable behavior, validators, CI checks, signing, evidence closure, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pipeline Receipts

Parent lane for pipeline-run receipt process memory.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Lane: pipeline" src="https://img.shields.io/badge/lane-pipeline-blue">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/pipeline/` is for pipeline-run receipt process memory only. It is not pipeline code, pipeline specification authority, source data, domain truth, proof, catalog authority, policy authority, release authority, published artifact authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory is the parent lane for receipts that document governed pipeline activity: transform runs, normalization runs, validation handoffs, model materialization support, review handoffs where applicable, correction support, rollback support, and release-candidate support.

Pipeline receipts record what a pipeline run did, what executable or specification context it used, what inputs and outputs were referenced, what hashes and policy or validation outcomes apply, and what downstream proof or release artifacts may inspect the receipt.

Receipts can support proof and release review later, but they do **not** prove domain claims, approve release, publish public artifacts, define object meaning, define schemas, fetch source data, admit sources, decide policy, or replace SourceDescriptors, contracts, schemas, EvidenceBundles, ProofPacks, CatalogMatrix records, PolicyDecisions, ReleaseManifests, CorrectionNotices, or RollbackCards.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This requested pipeline parent lane is:

```text
data/receipts/pipeline/
```

The child lanes `atmosphere/` and `flora/` are confirmed as substantive README files in the current repository. Exact pipeline receipt layout remains **NEEDS VERIFICATION** because the child files preserve uncertainty between `data/receipts/pipeline/<domain>/` and `data/receipts/<domain>/pipeline/` until accepted receipt-layout governance or ADR review confirms the pattern.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/pipeline/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | pipeline / executable-run process memory |
| Confirmed child receipt lanes | `atmosphere/`, `flora/` |
| Pipeline logic authority | `pipelines/`, not this lane |
| Pipeline spec authority | `pipeline_specs/` or accepted spec homes, not this lane |
| Lifecycle payload authority | `data/raw/`, `data/work/`, `data/quarantine/`, and `data/processed/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when executable refs, spec refs, source role, input/output hashes, evidence refs, policy refs, validation state, review state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

The child lanes below are confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted pipeline receipts, executable behavior, validators, fixtures, CI checks, signing, evidence closure, correction hooks, rollback hooks, or release integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`atmosphere/`](atmosphere/README.md) | **CONFIRMED README** | Atmosphere pipeline-run process memory for normalization, transform, validation handoff, unit-conversion support, correction, rollback, and release-candidate support. | Not pipeline code, pipeline spec authority, source data, processed Atmosphere truth, proof, release approval, or public artifact authority. |
| [`flora/`](flora/README.md) | **CONFIRMED README** | Flora pipeline-run process memory for normalization, transform, review handoffs, validation handoffs, correction, rollback, and release-candidate support. | Not pipeline code, pipeline spec authority, source data, accepted Flora truth, exact-location authority, sensitivity policy, proof, release approval, or public artifact authority. |

Other domain pipeline receipt lanes are **UNKNOWN** until verified by repository evidence.

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what the pipeline run did; it is not the truth source. |
| Pipeline run is not release | A successful run can create candidates, receipts, and handoffs; it cannot publish or approve release. |
| Executable logic stays separate | Code belongs under `pipelines/`; receipts under `data/receipts/` record run memory and references. |
| Specs stay separate | Declarative run specs belong under accepted `pipeline_specs/` homes, not this receipt lane. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to pipeline receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- transform, normalization, validation, model-materialization, policy-decision, review-reference, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, pipeline refs, spec refs, executable refs, input refs, input hashes, output refs, output hashes, evidence refs, policy refs, reviewer refs, validator refs, source-role refs, transform refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect pipeline receipt state without becoming executable code, pipeline spec authority, proof, catalog, policy, release, public output, domain truth, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Pipeline executable code, adapters, normalizers, validator wrappers, or handoff helpers | `pipelines/` |
| Declarative pipeline specs | `pipeline_specs/` or accepted spec homes |
| Upstream source fetchers and API clients | `connectors/` or accepted connector homes |
| Raw source captures or source-native records | `data/raw/` |
| Work/candidate outputs | `data/work/` |
| Quarantined source or pipeline outputs | `data/quarantine/` |
| Normalized processed payloads | `data/processed/` |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Policy bundles | `policy/` and governed policy roots |
| Tests, fixtures, package code, or CI workflows | `tests/`, `fixtures/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/pipeline/
├── README.md
├── atmosphere/
│   └── README.md
├── flora/
│   └── README.md
└── index.local.json
```

This map confirms the README child lanes currently documented. It does not prove emitted pipeline receipts, executable behavior, validators, fixtures, CI checks, signing, evidence closure, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, pipeline spec, policy authority, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the pipeline-run receipt family and a documented domain child lane.
- [ ] Confirm canonical pipeline/domain receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, pipeline refs, executable refs, spec refs, input/output hashes, evidence refs, policy refs, reviewer refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, domain-specific limits, transform state, review state, caveats, and limitations are preserved where material.
- [ ] Confirm EvidenceBundle/proof references resolve before using pipeline receipts in any public claim path.
- [ ] Confirm receipt presence is not treated as executable behavior proof, domain truth, policy authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when executable/spec identity, source role, evidence, policy, validation, review, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, generated answer, or released layer uses this pipeline parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/pipeline/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lanes during this edit: `atmosphere/` and `flora/`. | **CONFIRMED by GitHub contents API during this edit** |
| Both child lanes state the exact choice between `data/receipts/pipeline/<domain>/` and `data/receipts/<domain>/pipeline/` remains NEEDS VERIFICATION. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Pipeline child README presence proves emitted pipeline receipts, executable behavior, validators, fixtures, CI checks, signing, evidence closure, correction hooks, rollback hooks, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/pipeline/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual pipeline receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is pipeline code, pipeline spec authority, source data, domain truth, proof, catalog authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`atmosphere/README.md`](atmosphere/README.md)
- [`flora/README.md`](flora/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/README.md`](../../catalog/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../pipelines/README.md`](../../../pipelines/README.md)
- [`../../../pipeline_specs/README.md`](../../../pipeline_specs/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/pipeline/` is a pipeline receipt parent lane for process memory only. It is not pipeline code, pipeline spec authority, source data, domain truth, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
