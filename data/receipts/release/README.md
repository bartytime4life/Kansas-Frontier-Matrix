<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/release/readme
name: Release Receipts README
path: data/receipts/release/README.md
type: data-receipts-release-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <release-steward>
  - <proof-steward>
  - <catalog-steward>
  - <policy-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: release-support-receipts
receipt_scope: release-support-process-memory
path_posture: release-support-receipt-parent-lane; atmosphere-and-flora-child-lanes-confirmed; release-manifests-root-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; release-support-not-release-authority; release-manifest-separate; publication-separate
related:
  - atmosphere/README.md
  - flora/README.md
  - ../README.md
  - ../../README.md
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
  - release
  - release-support
  - process-memory
  - run-receipt
  - validation-report
  - policy-decision
  - correction
  - rollback
  - release-gated
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/receipts/release/README.md`."
  - "Confirmed child receipt README lanes during this edit: `atmosphere/` and `flora/`."
  - "ReleaseManifest authority remains in `release/manifests/`; that root is currently a greenfield stub."
  - "Exact release-support receipt layout remains NEEDS VERIFICATION until accepted receipt-layout governance or ADR review confirms it."
  - "README presence confirms documentation only; it does not prove emitted release-support receipts, ReleaseManifests, validators, CI checks, signing, proof closure, correction hooks, rollback hooks, or publication integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Release Receipts

Parent lane for release-support receipt process memory.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Lane: release support" src="https://img.shields.io/badge/lane-release%20support-blue">
  <img alt="Boundary: not ReleaseManifest" src="https://img.shields.io/badge/boundary-not%20ReleaseManifest-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/release/` is for release-support receipt process memory only. It is not a `ReleaseManifest`, release decision, proof, catalog authority, policy authority, published artifact, public API/UI material, or generated-answer authority.

---

## Scope

This directory is the parent lane for receipts that document governed release-support activity: release-candidate checks, proof-reference checks, catalog-reference checks, policy-state checks, validation handoff, review handoff where applicable, correction support, rollback support, and publication-handoff memory.

Release-support receipts record what a release-support process inspected and what finite outcome it produced. They may reference proof, catalog, policy, validation, review, correction, rollback, and publication-candidate records.

Release-support receipts do **not** approve release, create a `ReleaseManifest`, publish artifacts, prove domain claims, decide policy, define schemas, or replace EvidenceBundles, ProofPacks, CatalogMatrix records, PolicyDecisions, ReviewRecords, ReleaseManifests, CorrectionNotices, RollbackCards, or released public artifacts.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This requested release-support parent lane is:

```text
data/receipts/release/
```

The child lanes `atmosphere/` and `flora/` are confirmed as substantive README files in the current repository. `release/manifests/README.md` is still a greenfield stub, so this README does not claim live ReleaseManifest maturity.

Exact release-support receipt layout remains **NEEDS VERIFICATION** because the child files preserve uncertainty between `data/receipts/release/<domain>/` and `data/receipts/<domain>/release/` until accepted receipt-layout governance or ADR review confirms the pattern.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/release/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | release-support process memory |
| Confirmed child receipt lanes | `atmosphere/`, `flora/` |
| ReleaseManifest authority | `release/manifests/`, not this lane |
| Release-decision authority | `release/`, not this lane |
| Published artifact authority | `data/published/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Public access posture | No direct public path; no normal UI; no governed-public API exposure |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when proof refs, catalog refs, validation refs, policy refs, review refs, correction path, rollback target, release decision, or publication target is insufficient |

---

## Confirmed child lanes

The child lanes below are confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted release-support receipts, ReleaseManifests, validators, CI checks, signing, proof closure, review closure, correction hooks, rollback hooks, or publication integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`atmosphere/`](atmosphere/README.md) | **CONFIRMED README** | Atmosphere release-support process memory for release-candidate checks, proof-reference checks, catalog-reference checks, policy-state checks, validation handoff, correction, rollback, and publication-handoff memory. | Not a ReleaseManifest, release decision, proof, catalog authority, policy authority, published artifact, public API/UI material, or generated-answer authority. |
| [`flora/`](flora/README.md) | **CONFIRMED README** | Flora release-support process memory for release-candidate checks, proof-reference checks, catalog-reference checks, policy-state checks, review-state checks, validation handoff, correction, rollback, and publication-handoff memory. | Not a ReleaseManifest, release decision, proof, catalog authority, policy authority, sensitivity authority, published artifact, public API/UI material, or generated-answer authority. |

Other domain release-support receipt lanes are **UNKNOWN** until verified by repository evidence.

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what a release-support process did; it is not release authority. |
| ReleaseManifest stays separate | ReleaseManifest authority belongs in `release/manifests/`, not this receipt lane. |
| Release decisions stay separate | Promotion decisions, correction notices, rollback cards, withdrawals, signatures, and release changelogs belong in `release/`. |
| Publication stays separate | Released public artifacts belong in `data/published/` only after governed release gates close. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Policy remains separate | Policy decisions and policy bundles stay in governed policy roots and release decision artifacts. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to release-support receipt instances and receipt-local sidecars:

- RunReceipt, ValidationReport, PolicyDecision reference, ReviewRecord reference where applicable, proof-closure reference, catalog-reference check, correction-support, rollback-support, and publication-handoff receipt records;
- run IDs, source refs, proof refs, catalog refs, policy refs, validation refs, review refs, release-candidate refs, publication-target refs, correction refs, rollback refs, input/output hashes, finite outcomes, reason codes, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect release-support receipt state without becoming proof, catalog, policy, release, publication, public output, domain truth, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| ReleaseManifest files | `release/manifests/` |
| Release decisions, correction notices, rollback cards, withdrawal notices, release signatures, or release changelog | `release/` |
| Released map layers, reports, PMTiles, or public downloads | `data/published/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or discovery records | `data/catalog/` |
| Source, work, quarantine, or processed payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/` |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| Policy bundles | `policy/` and governed policy roots |
| Pipeline code, tests, fixtures, package code, or CI workflows | `pipelines/`, `tests/`, `fixtures/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/release/
├── README.md
├── atmosphere/
│   └── README.md
├── flora/
│   └── README.md
└── index.local.json
```

This map confirms the README child lanes currently documented. It does not prove emitted release-support receipts, ReleaseManifests, validators, fixtures, CI checks, signing, proof closure, review closure, correction hooks, rollback hooks, or publication integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, release authority, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the release-support receipt family and a documented domain child lane.
- [ ] Confirm canonical release/domain receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, proof refs, catalog refs, validation refs, policy refs, review refs, release-candidate refs, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm the actual ReleaseManifest, when present, lives under `release/manifests/` and is not stored in this lane.
- [ ] Confirm proof closure and required review closure resolve before any public claim path uses a release-support receipt.
- [ ] Confirm receipt presence is not treated as proof, catalog closure, release approval, publication, public artifact authority, domain truth, or policy authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when proof, catalog, policy, review, validation, correction, rollback, release, or publication state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, generated answer, or released layer uses this parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/release/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lanes during this edit: `atmosphere/` and `flora/`. | **CONFIRMED by GitHub contents API during this edit** |
| `release/manifests/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says `release/manifests/` is the sole canonical home for ReleaseManifest and `release/` owns release-decision artifacts. | **CONFIRMED doctrine / ADR status proposed** |
| Exact release-support receipt layout under `data/receipts/release/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual release-support receipt payloads exist under this subtree. | **UNKNOWN** |
| Release-support child README presence proves emitted release-support receipts, ReleaseManifests, validators, CI checks, signing, proof closure, review closure, correction hooks, rollback hooks, or publication integration. | **DENY** |
| This README is a ReleaseManifest, release decision, proof, catalog authority, policy authority, published artifact, public API/UI material, or generated-answer authority. | **DENY** |

---

## Related files

- [`atmosphere/README.md`](atmosphere/README.md)
- [`flora/README.md`](flora/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/README.md`](../../catalog/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/release/` is a release-support receipt parent lane for process memory only. It is not a ReleaseManifest, release decision, proof, catalog, registry, policy, publication, public artifact authority, graph authority, vector-index authority, public API/UI authority, or generated-answer truth.

[Back to top](#top)
