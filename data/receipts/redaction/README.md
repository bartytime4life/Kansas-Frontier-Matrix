<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/redaction/readme
name: Redaction Receipts README
path: data/receipts/redaction/README.md
type: data-receipts-redaction-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <redaction-steward>
  - <policy-steward>
  - <review-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: redaction-receipts
receipt_scope: redaction-process-memory
path_posture: redaction-receipt-parent-lane; flora-child-lane-confirmed; domain-first-flora-redaction-lane-also-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; redaction-not-release; policy-and-review-required; release-blocked
related:
  - flora/README.md
  - ../README.md
  - ../../README.md
  - ../flora/README.md
  - ../flora/redaction/README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - redaction
  - geoprivacy
  - process-memory
  - redaction-receipt
  - review-record
  - policy-decision
  - validation-report
  - release-gated
  - no-public-path
notes:
  - "This README replaces the blank placeholder at `data/receipts/redaction/README.md`."
  - "Confirmed child receipt README lane during this edit: `flora/`."
  - "The established domain-first Flora redaction lane `data/receipts/flora/redaction/README.md` is also confirmed."
  - "The exact choice between `data/receipts/redaction/<domain>/` and `data/receipts/<domain>/redaction/` remains NEEDS VERIFICATION until accepted receipt-layout governance or ADR review confirms it."
  - "README presence confirms documentation only; it does not prove emitted RedactionReceipts, validators, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Redaction Receipts

Parent lane for redaction receipt process memory.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Lane: redaction" src="https://img.shields.io/badge/lane-redaction-blue">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/redaction/` is for redaction receipt process memory only. It is not source truth, domain truth, sensitivity policy, proof, catalog authority, release authority, published artifact authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory is the parent lane for receipts that document governed redaction and geoprivacy activity: transform support, review handoff, policy-decision reference, validation support, correction support, rollback support, and release-candidate support.

Redaction receipts record what a governed transform did, what policy and review references governed it, what input/output hashes apply, and which downstream proof or release artifacts may inspect the receipt.

Redaction receipts do **not** define policy, prove domain claims, approve release, publish artifacts, or replace ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, ReleaseManifests, CorrectionNotices, or RollbackCards.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This requested redaction parent lane is:

```text
data/receipts/redaction/
```

The child lane `flora/` is confirmed as a substantive README file. The domain-first Flora redaction lane is also confirmed:

```text
data/receipts/flora/redaction/
```

The exact choice between `data/receipts/redaction/<domain>/` and `data/receipts/<domain>/redaction/` remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms the pattern.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/redaction/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | redaction / geoprivacy process memory |
| Confirmed child receipt lanes | `flora/` |
| Related confirmed lane | `data/receipts/flora/redaction/` |
| Lifecycle payload authority | `data/raw/`, `data/work/`, `data/quarantine/`, and `data/processed/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, or `QUARANTINE` when policy refs, reviewer refs, input/output hashes, evidence refs, correction path, rollback target, or release state are insufficient |

---

## Confirmed child lanes

The child lane below is confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted redaction receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`flora/`](flora/README.md) | **CONFIRMED README** | Flora redaction/geoprivacy process memory for transform, review, validation, correction, rollback, and release-candidate support. | Not Flora truth, location authority, sensitivity policy, proof, release approval, or public artifact authority. |

Other domain redaction receipt lanes are **UNKNOWN** until verified by repository evidence.

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records redaction behavior; it is not the truth source. |
| Redaction is not release | A receipt can support review, proof, and release; it cannot approve publication. |
| Policy remains separate | Binding rules live in governed policy roots, not this receipt lane. |
| Review remains separate | ReviewRecord and release authority roles must remain visible and must not collapse into this receipt. |
| Protected detail stays protected | README and local indexes must not expose restricted or re-identifying detail. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to redaction receipt instances and receipt-local sidecars:

- RedactionReceipt, TransformReceipt, ValidationReport, PolicyDecision reference, ReviewRecord reference, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, object refs, policy refs, reviewer refs, evidence refs, validation refs, input/output hashes, transform refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect redaction receipt state without becoming proof, catalog, policy, release, public output, domain truth, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source payloads | `data/raw/` |
| Work/candidate outputs | `data/work/` |
| Quarantined material | `data/quarantine/` |
| Processed payloads | `data/processed/` |
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
data/receipts/redaction/
├── README.md
├── flora/
│   └── README.md
└── index.local.json
```

This map confirms the README child lane currently documented. It does not prove emitted redaction receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, policy authority, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the redaction/geoprivacy receipt family and a documented domain child lane.
- [ ] Confirm canonical redaction/domain receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, policy refs, reviewer refs, object refs, input/output hashes, evidence refs, validation refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm protected or re-identifying detail is not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where a public-safe derivative or release-candidate handoff is involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using redaction receipts in any public claim path.
- [ ] Confirm receipt presence is not treated as domain truth, location authority, sensitivity policy, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when policy, review, rights, sensitivity, evidence, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, generated answer, or released layer uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the blank placeholder at `data/receipts/redaction/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lane during this edit: `flora/`. | **CONFIRMED by GitHub contents API during this edit** |
| The established domain-first Flora redaction lane `data/receipts/flora/redaction/README.md` is confirmed. | **CONFIRMED by GitHub contents API during this edit** |
| Exact choice between `data/receipts/redaction/<domain>/` and `data/receipts/<domain>/redaction/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Flora receipt docs say redaction receipts are process memory and do not prove occurrence, approve release, expose restricted geometry, define sensitivity policy, or replace proof/release artifacts. | **CONFIRMED by GitHub contents API during this edit** |
| Redaction child README presence proves emitted redaction receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration. | **DENY** |
| Actual redaction receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is domain truth, location authority, sensitivity policy, proof, catalog authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`flora/README.md`](flora/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../flora/README.md`](../flora/README.md)
- [`../flora/redaction/README.md`](../flora/redaction/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/README.md`](../../catalog/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/redaction/` is a redaction receipt parent lane for process memory only. It is not domain truth, location authority, sensitivity policy, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
