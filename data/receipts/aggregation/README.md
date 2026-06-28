<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/aggregation/readme
name: Aggregation Receipts README
path: data/receipts/aggregation/README.md
type: data-receipts-subroot-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <data-steward>
  - <domain-stewards>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: aggregation-receipts
receipt_family: aggregation
path_posture: requested-subroot; needs-ADR-S-03-or-receipt-layout-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; aggregation-does-not-launder-rights-or-sensitivity; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../published/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../contracts/domains/agriculture/aggregation-receipt.md
  - ../../../policy/domains/agriculture/aggregation_thresholds/README.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - aggregation
  - aggregation-receipt
  - process-memory
  - provenance
  - threshold-profile
  - evidence-refs
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/receipts/aggregation/README.md`."
  - "Parent `data/receipts/README.md` is currently a greenfield stub."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "ADR-0011 names `data/receipts/` as the canonical process-memory family, but the exact aggregation subroot remains NEEDS VERIFICATION pending receipt-layout/ADR review."
  - "The Agriculture AggregationReceipt contract is a draft semantic contract and does not prove validators, fixtures, schemas, emitted receipts, or release integration are wired."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Aggregation Receipts

Requested receipt-family lane for aggregation process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Receipt: aggregation" src="https://img.shields.io/badge/receipt-aggregation-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/aggregation/` is for aggregation receipt process memory only. It is not proof, EvidenceBundle authority, catalog authority, release authority, source registry authority, policy authority, public artifact authority, published-layer authority, aggregation-policy authority, or generated-answer authority.

---

## Scope

This directory is for aggregation receipts: compact records that document that a governed aggregation step ran, what inputs it considered, what method or recipe it used, what threshold/profile context applied, what output references it affected, and what review, policy, correction, or rollback references must be inspected downstream.

Aggregation receipts support audit, replay, review, correction, rollback, and promotion checks. They do **not** prove that an aggregate claim is true by themselves, do not replace EvidenceBundle support, do not authorize publication, and do not make sensitive or weakly supported data safe.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested subroot is:

```text
data/receipts/aggregation/
```

This README documents the requested lane without claiming final receipt-layout authority. ADR-0011 lists canonical receipt homes under `data/receipts/{ingest,validation,pipeline,ai,release,migration}/`, while the RunReceipt standard names `AggregationReceipt` as a receipt subclass. Until receipt-layout ADR review resolves subroot naming, this lane is **NEEDS VERIFICATION** for canonical placement but usable as a bounded README for aggregation receipt discipline.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/aggregation/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt type | aggregation receipts |
| Path posture | requested subroot; canonical subroot naming needs verification |
| Parent root | `data/receipts/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `HOLD`, `DENY`, `QUARANTINE`, or `ABSTAIN` when input lineage, threshold profile, method identity, rights, sensitivity, evidence references, review state, correction path, rollback target, or release state is insufficient |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what an aggregation step did, not whether the resulting claim is true. |
| Aggregation does not erase provenance | Input references, input digests, and evidence references must stay inspectable. |
| Threshold/profile context travels | Suppression, k-threshold, privacy, generalization, and aggregation-profile choices must be named where applicable. |
| Sensitivity is not laundered | Aggregation does not automatically remove rights, privacy, cultural, ecological, infrastructure, living-person, or location-sensitivity obligations. |
| Proof remains separate | EvidenceBundle, ProofPack, catalog closure, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, correction notices, rollback cards, and signatures belong in `release/`. |
| Catalog remains separate | STAC/DCAT/PROV discovery records belong in `data/catalog/`. |
| Public clients never read receipts directly | Receipts can support governed review, but public outputs consume released artifacts and governed APIs, not raw receipt lanes. |

---

## Accepted material

Accepted content is limited to aggregation receipt instances and receipt-local sidecars:

- aggregation receipt JSON or JSONL records;
- run, method, recipe, threshold-profile, aggregation-unit, suppression/generalization, and policy-decision references;
- input references, input digests, evidence references, source-version references, and affected-output references;
- review-state, correction, supersession, rollback-target, and release-candidate references;
- receipt manifests, checksums, signatures, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect aggregation receipt state without becoming proof, catalog, policy, release, or public output authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Full source rows or source payloads | `data/raw/`, `data/work/`, `data/processed/` as applicable |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Aggregation threshold policy | `policy/` and domain policy roots |
| Receipt schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Generated answer text | governed API / answer layer only after evidence and release checks |

---

## Directory map

```text
data/receipts/aggregation/
├── README.md
├── <domain>/
│   └── <run_id>/
│       ├── aggregation_receipt.json
│       ├── checksums.sha256
│       ├── signature.bundle
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream review. |
| Hold | Method identity, input digest, threshold profile, evidence references, review state, or policy context is incomplete. |
| Quarantine/correct | Receipt contradicts inputs, omits required lineage, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when a proof object cites this receipt as process support and supplies independent evidence support. |
| Reference from release | Only when a ReleaseManifest/promotion decision cites the proof chain, receipt lineage, correction path, and rollback target. |

---

## Forbidden shortcut

```text
data/receipts/aggregation/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. A receipt can be cited by proof and release artifacts, but it does not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs in the aggregation receipt family and not another receipt lane.
- [ ] Confirm canonical subroot naming against ADR-S-03 or the accepted receipt-layout ADR before relying on this path as final authority.
- [ ] Confirm receipt ID, run ID, method identity, aggregation unit, threshold/profile, input refs, input digests, output refs, and timestamps are present where applicable.
- [ ] Confirm evidence references resolve to proof-side support before using the receipt in a public claim path.
- [ ] Confirm aggregation did not erase rights, sensitivity, provenance, or source-role obligations.
- [ ] Confirm receipt payloads are immutable or hash-bound and do not overwrite prior receipt records in place.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, or generated answer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/receipts/aggregation/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, and publication are separate artifact families. | **CONFIRMED doctrine / ADR status proposed** |
| ADR-0011 places receipts under `data/receipts/` as process memory and says receipts must not be cited as release-grade proof by themselves. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard names `AggregationReceipt` as a receipt subclass. | **CONFIRMED by GitHub contents API during this edit** |
| Agriculture AggregationReceipt contract says AggregationReceipt records aggregation process, method, thresholds, input digests/evidence refs, and review trail, but does not prove truth or replace proof/release artifacts. | **CONFIRMED draft contract** |
| The exact canonical subroot `data/receipts/aggregation/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual aggregation receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, catalog authority, registry authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/README.md`](../../catalog/README.md)
- [`../../published/README.md`](../../published/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../contracts/domains/agriculture/aggregation-receipt.md`](../../../contracts/domains/agriculture/aggregation-receipt.md)
- [`../../../policy/domains/agriculture/aggregation_thresholds/README.md`](../../../policy/domains/agriculture/aggregation_thresholds/README.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/aggregation/` is a receipt lane for aggregation process memory only. It is not proof, catalog, registry, policy, release, publication, public artifact, graph, vector-index, or generated-answer truth.

[Back to top](#top)
