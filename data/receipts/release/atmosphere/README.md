<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/release/atmosphere/readme
name: Atmosphere Release Receipts README
path: data/receipts/release/atmosphere/README.md
type: data-receipts-release-domain-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <release-steward>
  - <atmosphere-domain-steward>
  - <proof-steward>
  - <catalog-steward>
  - <policy-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: atmosphere-release-support-receipts
receipt_scope: atmosphere-release-support-process-memory
domain: atmosphere
path_posture: requested-release-domain-receipt-lane; release-receipts-parent-still-stub; release-manifests-root-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; release-support-not-release-authority; release-manifest-separate; publication-separate
related:
  - ../README.md
  - ../../README.md
  - ../../atmosphere/README.md
  - ../../atmosphere/pm25_2026/README.md
  - ../../atmosphere/unit_conversion/README.md
  - ../../../published/layers/atmosphere/README.md
  - ../../../proofs/README.md
  - ../../../catalog/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - release
  - atmosphere
  - release-support
  - process-memory
  - run-receipt
  - validation-report
  - policy-decision
  - correction
  - rollback
  - no-public-path
notes:
  - "This README replaces a blank placeholder at `data/receipts/release/atmosphere/README.md`."
  - "Parent `data/receipts/release/README.md` is currently a greenfield stub."
  - "ReleaseManifest authority remains in `release/manifests/`; that root is also currently a greenfield stub."
  - "Atmosphere receipt docs define Atmosphere receipts as process memory and not proof, release, policy, catalog, or public artifact authority."
  - "README presence confirms documentation only; it does not prove emitted release-support receipts, ReleaseManifests, validators, CI checks, signing, policy enforcement, proof closure, correction hooks, rollback hooks, or publication integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Release Receipts

Release-support receipt lane for Atmosphere process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Lane: release support" src="https://img.shields.io/badge/lane-release%20support-blue">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f9eda">
  <img alt="Boundary: not ReleaseManifest" src="https://img.shields.io/badge/boundary-not%20ReleaseManifest-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/release/atmosphere/` is for Atmosphere release-support receipt process memory only. It is not a ReleaseManifest, release decision, proof, catalog authority, policy authority, published artifact, public API/UI material, advisory authority, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document governed Atmosphere release-support activity: release-candidate checks, proof-reference checks, catalog-reference checks, policy-state checks, validation handoff, correction support, rollback support, and publication-handoff memory.

Release-support receipts record what a release-support process inspected and what finite outcome it produced. They may reference proof, catalog, policy, validation, correction, rollback, and publication-candidate records.

Release-support receipts do **not** approve release, create a ReleaseManifest, publish artifacts, prove Atmosphere claims, define schemas, decide policy, or replace EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, RollbackCards, or released public artifacts.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested release/domain receipt lane is:

```text
data/receipts/release/atmosphere/
```

This README documents the requested lane without claiming final receipt-layout authority. Parent `data/receipts/release/README.md` is still a greenfield stub. `release/manifests/README.md` is also still a greenfield stub, so no live ReleaseManifest maturity is claimed here.

The exact choice between `data/receipts/release/<domain>/` and `data/receipts/<domain>/release/` remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms the pattern.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/release/atmosphere/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | release-support process memory |
| Domain lane | atmosphere |
| Parent root | `data/receipts/release/` |
| Related domain receipt parent | `data/receipts/atmosphere/` |
| ReleaseManifest authority | `release/manifests/`, not this lane |
| Release-decision authority | `release/`, not this lane |
| Published artifact authority | `data/published/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Public access posture | No direct public path; no normal UI; no governed-public API exposure |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when proof refs, catalog refs, validation refs, policy refs, correction path, rollback target, integrity state, release decision, or publication target is insufficient |

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what a release-support process did; it is not release authority. |
| ReleaseManifest stays separate | ReleaseManifest authority belongs in `release/manifests/`, not this receipt lane. |
| Publication stays separate | Released public artifacts belong in `data/published/` only after governed release gates close. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Policy remains separate | Policy decisions and policy bundles stay in governed policy roots and release decision artifacts. |
| Atmosphere roles stay explicit | Atmosphere source-role, unit, time, caveat, and freshness boundaries must remain visible. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Atmosphere release-support receipt instances and receipt-local sidecars:

- RunReceipt, ValidationReport, PolicyDecision reference, proof-closure reference, catalog-reference check, correction-support, rollback-support, and publication-handoff receipt records;
- run IDs, source refs, proof refs, catalog refs, policy refs, validation refs, release-candidate refs, publication-target refs, correction refs, rollback refs, input/output hashes, finite outcomes, reason codes, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect release-support receipt state without becoming proof, catalog, policy, release, publication, public output, Atmosphere truth, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| ReleaseManifest files | `release/manifests/` |
| Release decisions, correction notices, rollback cards, withdrawal notices, release signatures, or release changelog | `release/` |
| Released map layers, PMTiles, reports, or public downloads | `data/published/` |
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
data/receipts/release/atmosphere/
├── README.md
├── <run_id>/
│   ├── run_receipt.json
│   ├── release_support_receipt.json
│   ├── validation_report_ref.json
│   ├── policy_decision_ref.json
│   ├── proof_closure_ref.json
│   ├── checksums.sha256
│   └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted release-support receipts, ReleaseManifests, validators, fixtures, CI checks, signing, proof closure, correction hooks, rollback hooks, or publication integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, release authority, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Atmosphere domain and release-support receipt lane.
- [ ] Confirm canonical release/domain receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, proof refs, catalog refs, validation refs, policy refs, release-candidate refs, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm the actual ReleaseManifest, when present, lives under `release/manifests/` and is not stored in this lane.
- [ ] Confirm proof closure resolves before any public Atmosphere claim path uses a release-support receipt.
- [ ] Confirm receipt presence is not treated as proof, catalog closure, release approval, publication, public artifact authority, or Atmosphere truth.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when proof, catalog, policy, validation, correction, rollback, release, or publication state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, generated answer, or released layer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/release/atmosphere/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/release/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| `release/manifests/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says `release/manifests/` is the sole canonical home for ReleaseManifest and `release/` owns release-decision artifacts. | **CONFIRMED doctrine / ADR status proposed** |
| Atmosphere receipt docs say Atmosphere receipts are process memory and not proof, release, catalog, policy, or public artifact authority. | **CONFIRMED by GitHub contents API during this edit** |
| Exact choice between `data/receipts/release/<domain>/` and `data/receipts/<domain>/release/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Atmosphere release-support receipt payloads exist under this subtree. | **UNKNOWN** |
| Emitted release-support receipts, ReleaseManifests, validators, CI checks, signing, proof closure, correction hooks, rollback hooks, and publication integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is a ReleaseManifest, release decision, proof, catalog authority, policy authority, published artifact, public API/UI material, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../atmosphere/README.md`](../../atmosphere/README.md)
- [`../../atmosphere/pm25_2026/README.md`](../../atmosphere/pm25_2026/README.md)
- [`../../atmosphere/unit_conversion/README.md`](../../atmosphere/unit_conversion/README.md)
- [`../../../published/layers/atmosphere/README.md`](../../../published/layers/atmosphere/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../catalog/README.md`](../../../catalog/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/release/atmosphere/` is an Atmosphere release-support receipt lane for process memory only. It is not a ReleaseManifest, release decision, proof, catalog, registry, policy, publication, public artifact authority, graph authority, vector-index authority, public API/UI authority, or generated-answer truth.

[Back to top](#top)
