<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/agriculture/readme
name: Agriculture Receipts README
path: data/receipts/agriculture/README.md
type: data-receipts-domain-lane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <agriculture-domain-steward>
  - <data-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
domain: agriculture
artifact_family: agriculture-receipts
path_posture: domain-receipt-lane; needs-receipt-layout-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-role-preserving; private-join-denial-defaults; release-blocked
related:
  - ../README.md
  - ../aggregation/README.md
  - ../../README.md
  - ../../raw/agriculture/README.md
  - ../../processed/agriculture/README.md
  - ../../proofs/README.md
  - ../../catalog/domain/agriculture/README.md
  - ../../published/layers/agriculture/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../docs/domains/agriculture/PIPELINE.md
  - ../../../contracts/domains/agriculture/aggregation-receipt.md
  - ../../../policy/domains/agriculture/aggregation_thresholds/README.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - agriculture
  - aggregation-receipt
  - run-receipt
  - transform-receipt
  - validation-receipt
  - process-memory
  - source-role
  - provenance
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/agriculture/README.md`."
  - "Parent `data/receipts/README.md` is currently a greenfield stub."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "Agriculture canonical-path doctrine places Agriculture material as a domain segment under responsibility roots; this README documents the Agriculture segment under the receipts family root."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Receipts

Domain receipt lane for Agriculture process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-2e7d32">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Receipt families](#receipt-families) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/agriculture/` is for Agriculture receipt process memory only. It is not proof, EvidenceBundle authority, catalog authority, source registry authority, aggregation-threshold policy, release authority, public artifact authority, crop truth, field truth, private-join authority, or generated-answer authority.

---

## Scope

This directory is for Agriculture-domain receipt records emitted by governed Agriculture runs: intake, source refresh, transform, aggregation, validation, policy evaluation, AI assistance, correction, rollback support, migration, and release-support steps.

Receipts help reviewers reconstruct what a process did. They can cite input digests, evidence references, policy states, threshold profiles, output references, and rollback/correction references. They do **not** prove that an Agriculture claim is true by themselves, do not replace EvidenceBundle support, and do not authorize publication.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. Agriculture is the domain segment under that family root:

```text
data/receipts/agriculture/
```

This README documents the domain receipt lane without claiming every receipt subtype or subfolder naming convention is final. ADR-0011 names `data/receipts/` as the canonical process-memory family; Agriculture canonical-path doctrine says Agriculture material appears as a domain segment inside responsibility roots. Exact receipt-layout conventions remain **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms them.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/agriculture/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | agriculture |
| Path posture | domain receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/` |
| Related family lane | `data/receipts/aggregation/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payloads | `data/raw/agriculture/`, `data/work/agriculture/`, `data/processed/agriculture/` |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `HOLD`, `DENY`, `QUARANTINE`, or `ABSTAIN` when source role, input lineage, rights, sensitivity, threshold profile, evidence references, review state, correction path, rollback target, or release state is insufficient |

---

## Receipt families

The exact subtype layout is not verified by this README. The lane may reference or contain Agriculture-scoped receipt instances such as:

| Receipt type | Purpose | Boundary |
|---|---|---|
| Intake / source refresh receipt | Records source observation, source-head state, digests, source role, and admission result. | Does not prove source content is true or publishable. |
| Transform receipt | Records normalization, mapping, crosswalk, or derived-object process memory. | Does not replace processed-object validation or proof. |
| Aggregation receipt | Records aggregation method, input digests, threshold/profile context, and affected outputs. | Does not prove the aggregate claim is true or safe to publish. |
| Validation receipt | Records validation execution and outcome. | Does not replace proof, catalog closure, or release approval. |
| Policy decision receipt/reference | Records or points to finite policy evaluation state. | Policy authority remains in policy roots; release authority remains in `release/`. |
| AI receipt | Records AI assistance or interpretation where used. | AI output is not root truth and cannot replace EvidenceBundle support. |
| Correction / rollback support receipt | Records process memory around correction, supersession, or rollback support. | Correction and rollback authority remains in release/proof governance. |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what a governed Agriculture process did, not whether the resulting claim is true. |
| Domain lane is not lifecycle payload storage | Source rows and transformed data stay in lifecycle roots, not in receipts. |
| Aggregation does not erase provenance | Aggregation receipts must preserve input references, input digests, evidence references, and threshold/profile context. |
| Private joins fail closed | Person, parcel, operator, field-level, or ownership-sensitive joins cannot be made public by receipt presence. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, correction notices, rollback cards, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Agriculture receipt instances and receipt-local sidecars:

- Agriculture run receipt JSON or JSONL records;
- intake, transform, aggregation, validation, AI, policy-evaluation, correction, migration, rollback-support, and release-support receipt records;
- run IDs, source refs, input refs, input digests, output refs, evidence refs, method IDs, threshold profiles, policy-decision refs, review states, correction refs, rollback targets, timestamps, actor/runner identity, and status fields;
- receipt manifests, checksums, signatures, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect Agriculture receipt state without becoming proof, catalog, policy, release, public output, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Full source rows or source payloads | `data/raw/agriculture/`, `data/work/agriculture/`, `data/processed/agriculture/` as applicable |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Aggregation threshold, private-join, sensitivity, or release policy | `policy/` and domain policy roots |
| Receipt schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Generated answer text | governed API / answer layer only after evidence and release checks |

---

## Directory map

```text
data/receipts/agriculture/
├── README.md
├── runs/
│   └── <run_id>/
│       ├── run_receipt.json
│       ├── checksums.sha256
│       ├── signature.bundle
│       └── README.md
├── aggregation/
│   └── <run_id>/
│       ├── aggregation_receipt.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, schemas, validators, fixtures, CI checks, signing, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream review. |
| Hold | Source role, input digest, method identity, threshold profile, evidence references, review state, or policy context is incomplete. |
| Quarantine/correct | Receipt contradicts inputs, omits required lineage, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when a proof object cites this receipt as process support and supplies independent evidence support. |
| Reference from release | Only when a ReleaseManifest/promotion decision cites the proof chain, receipt lineage, correction path, and rollback target. |

---

## Forbidden shortcut

```text
data/receipts/agriculture/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. A receipt can support proof and release artifacts, but it does not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Agriculture domain lane and the receipt family.
- [ ] Confirm canonical receipt subtype naming against ADR-S-03 or the accepted receipt-layout ADR before relying on this path as final authority.
- [ ] Confirm receipt ID, run ID, method identity, source/input refs, input digests, output refs, evidence refs, timestamps, actor/runner identity, and status fields are present where applicable.
- [ ] Confirm aggregation receipts preserve aggregation unit, threshold/profile context, suppression/generalization state, and input lineage.
- [ ] Confirm evidence references resolve to proof-side support before using the receipt in a public claim path.
- [ ] Confirm receipt presence is not treated as crop truth, field truth, operator truth, parcel truth, private-join approval, proof, catalog closure, or release approval.
- [ ] Confirm receipt payloads are immutable or hash-bound and do not overwrite prior receipt records in place.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, or generated answer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/agriculture/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, and publication are separate artifact families. | **CONFIRMED doctrine / ADR status proposed** |
| ADR-0011 places receipts under `data/receipts/` as process memory and says receipts must not be cited as release-grade proof by themselves. | **CONFIRMED doctrine / ADR status proposed** |
| Agriculture canonical-path doctrine places Agriculture material as a domain segment inside responsibility roots. | **CONFIRMED doctrine / path details draft** |
| RunReceipt standard names `AggregationReceipt` as a receipt subclass. | **CONFIRMED by GitHub contents API during this edit** |
| Agriculture AggregationReceipt contract says AggregationReceipt records aggregation process, method, thresholds, input digests/evidence refs, and review trail, but does not prove truth or replace proof/release artifacts. | **CONFIRMED draft contract** |
| Exact subtype layout under `data/receipts/agriculture/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Agriculture receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, catalog authority, registry authority, policy authority, release authority, public artifact authority, crop truth, field truth, private-join approval, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../aggregation/README.md`](../aggregation/README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/agriculture/README.md`](../../raw/agriculture/README.md)
- [`../../processed/agriculture/README.md`](../../processed/agriculture/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/domain/agriculture/README.md`](../../catalog/domain/agriculture/README.md)
- [`../../published/layers/agriculture/README.md`](../../published/layers/agriculture/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/domains/agriculture/CANONICAL_PATHS.md`](../../../docs/domains/agriculture/CANONICAL_PATHS.md)
- [`../../../docs/domains/agriculture/PIPELINE.md`](../../../docs/domains/agriculture/PIPELINE.md)
- [`../../../contracts/domains/agriculture/aggregation-receipt.md`](../../../contracts/domains/agriculture/aggregation-receipt.md)
- [`../../../policy/domains/agriculture/aggregation_thresholds/README.md`](../../../policy/domains/agriculture/aggregation_thresholds/README.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/agriculture/` is an Agriculture receipt lane for process memory only. It is not proof, catalog, registry, policy, release, publication, crop truth, field truth, private-join authority, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
