<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/redaction/flora/readme
name: Flora Redaction Receipts README
path: data/receipts/redaction/flora/README.md
type: data-receipts-redaction-domain-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <redaction-steward>
  - <flora-domain-steward>
  - <geoprivacy-steward>
  - <sensitivity-reviewer>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: flora-redaction-receipts
receipt_scope: flora-redaction-process-memory
domain: flora
path_posture: requested-redaction-domain-receipt-lane; redaction-parent-still-blank; data-receipts-flora-redaction-already-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; redaction-not-release; restricted-geometry-protected; policy-and-review-required; release-blocked
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
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - redaction
  - flora
  - geoprivacy
  - redaction-receipt
  - review-record
  - policy-decision
  - validation-report
  - no-public-path
notes:
  - "This README replaces a blank placeholder at `data/receipts/redaction/flora/README.md`."
  - "Parent `data/receipts/redaction/README.md` is currently blank."
  - "The established Flora redaction lane `data/receipts/flora/redaction/README.md` is confirmed in the current repository."
  - "The exact choice between `data/receipts/redaction/<domain>/` and `data/receipts/<domain>/redaction/` remains NEEDS VERIFICATION until accepted receipt-layout governance or ADR review confirms it."
  - "README presence confirms documentation only; it does not prove emitted RedactionReceipts, validators, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Redaction Receipts

Redaction receipt lane for Flora geoprivacy process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Lane: redaction" src="https://img.shields.io/badge/lane-redaction-blue">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/redaction/flora/` is for Flora redaction receipt process memory only. It is not Flora truth, location authority, sensitivity policy, proof, catalog authority, release authority, public artifact authority, public UI material, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document governed Flora redaction and geoprivacy activity: suppression, generalization, steward review handoff, delayed-publication support, aggregation support, correction support, rollback support, and release-candidate support.

Redaction receipts record what transform happened, which policy and review references governed it, what input and output hashes apply, and which downstream proof or release artifacts may inspect the receipt.

Redaction receipts do **not** define sensitivity policy, prove a Flora occurrence, approve public release, make restricted geometry public, or replace ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, ReleaseManifests, CorrectionNotices, or RollbackCards.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested redaction/domain lane is:

```text
data/receipts/redaction/flora/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/redaction/README.md` is currently blank, while the domain-first Flora redaction lane below is already confirmed:

```text
data/receipts/flora/redaction/
```

The exact choice between `data/receipts/redaction/<domain>/` and `data/receipts/<domain>/redaction/` remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms the pattern.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/redaction/flora/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | redaction / geoprivacy process memory |
| Domain lane | flora |
| Parent root | `data/receipts/redaction/` |
| Related confirmed lane | `data/receipts/flora/redaction/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload authority | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, and `data/processed/flora/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, or `QUARANTINE` when policy refs, reviewer refs, rights state, stewardship state, geometry state, input/output hashes, evidence refs, correction path, rollback target, or release state are insufficient |

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records redaction behavior, not Flora truth, location truth, or release approval. |
| Redaction is not release | A transform receipt can support review, proof, and release; it cannot approve publication. |
| Policy remains separate | Binding sensitivity and geoprivacy rules live in governed policy roots, not this receipt lane. |
| Review remains separate | ReviewRecord and release authority roles must remain visible and must not collapse into this receipt. |
| Protected geometry stays protected | README and local indexes must not expose restricted geometry or re-identifying details. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Flora redaction receipt instances and receipt-local sidecars:

- RedactionReceipt, TransformReceipt, ValidationReport, PolicyDecision reference, ReviewRecord reference, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, object refs, policy refs, reviewer refs, evidence refs, validation refs, input/output hashes, transform refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect redaction receipt state without becoming proof, catalog, policy, release, public output, Flora truth, location authority, sensitivity policy, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora source payloads | `data/raw/flora/` |
| Work/candidate outputs | `data/work/flora/` |
| Quarantined Flora material | `data/quarantine/flora/` |
| Processed Flora payloads | `data/processed/flora/` |
| EvidenceBundle, ProofPack, CatalogMatrix, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, or discovery records | `data/catalog/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, signature, or release changelog | `release/` |
| Sensitivity, geoprivacy, rights, source-role, publication, or release policy | `policy/` and governed policy roots |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| Pipeline code, tests, fixtures, package code, or CI workflows | `pipelines/`, `tests/`, `fixtures/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/redaction/flora/
├── README.md
├── <run_id>/
│   ├── redaction_receipt.json
│   ├── validation_report.json
│   ├── policy_decision_ref.json
│   ├── review_record_ref.json
│   ├── checksums.sha256
│   └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted redaction receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, policy authority, location authority, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Flora domain and redaction/geoprivacy receipt lane.
- [ ] Confirm canonical redaction/domain receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, policy refs, reviewer refs, object refs, input/output hashes, evidence refs, validation refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm restricted geometry and re-identifying details are not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where a public-safe derivative or release-candidate handoff is involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using this redaction receipt in any public Flora claim path.
- [ ] Confirm receipt presence is not treated as Flora truth, location authority, sensitivity policy, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when policy, review, rights, sensitivity, evidence, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, species page, generated answer, or released layer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/redaction/flora/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/redaction/README.md` is currently blank. | **CONFIRMED by GitHub contents API during this edit** |
| The established domain-first Flora redaction lane `data/receipts/flora/redaction/README.md` is confirmed. | **CONFIRMED by GitHub contents API during this edit** |
| Exact choice between `data/receipts/redaction/<domain>/` and `data/receipts/<domain>/redaction/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Flora receipt docs say redaction receipts are process memory and do not prove Flora occurrence, approve release, expose restricted geometry, define sensitivity policy, or replace proof/release artifacts. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Flora redaction receipt payloads exist under this subtree. | **UNKNOWN** |
| Emitted RedactionReceipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is Flora truth, location authority, sensitivity policy, proof, catalog authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

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
- [`../../../../docs/domains/flora/SENSITIVITY.md`](../../../../docs/domains/flora/SENSITIVITY.md)
- [`../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md`](../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/redaction/flora/` is a Flora redaction receipt lane for process memory only. It is not Flora truth, location authority, sensitivity policy, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
