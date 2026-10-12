<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/settlements-infrastructure/condition-redaction/readme
name: Settlements Infrastructure Condition Redaction Receipts README
path: data/receipts/settlements-infrastructure/condition_redaction/README.md
type: data-receipts-domain-redaction-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <redaction-steward>
  - <settlements-infrastructure-domain-steward>
  - <infrastructure-sensitivity-reviewer>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: settlements-infrastructure-condition-redaction-receipts
receipt_scope: infrastructure-condition-redaction-process-memory
domain: settlements-infrastructure
path_posture: requested-domain-condition-redaction-receipt-lane; domain-receipt-parent-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; condition-and-dependency-detail-restricted; redaction-not-release; review-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../raw/settlements-infrastructure/README.md
  - ../../../work/settlements-infrastructure/README.md
  - ../../../quarantine/settlements-infrastructure/README.md
  - ../../../processed/settlements-infrastructure/README.md
  - ../../../proofs/settlements-infrastructure/README.md
  - ../../../catalog/domain/settlements-infrastructure/README.md
  - ../../../published/layers/settlements-infrastructure/README.md
  - ../../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md
  - ../../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md
  - ../../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md
  - ../../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md
  - ../../../../docs/runbooks/settlements-infrastructure/PROMOTION_RUNBOOK.md
  - ../../../../docs/runbooks/settlements-infrastructure/ROLLBACK_RUNBOOK.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - settlements-infrastructure
  - condition-redaction
  - infrastructure
  - condition-observation
  - dependency
  - redaction-receipt
  - review-record
  - validation-report
  - policy-decision
  - correction
  - rollback
  - no-public-path
notes:
  - "This README replaces a blank placeholder at `data/receipts/settlements-infrastructure/condition_redaction/README.md`."
  - "Parent `data/receipts/settlements-infrastructure/README.md` is currently a greenfield stub."
  - "Settlements/Infrastructure doctrine says condition observations, dependencies, operator-sensitive details, and exact facility geometry are restricted or review-gated by default."
  - "This lane records redaction process memory only; it does not store condition observations, dependency payloads, policy, proof, ReleaseManifests, or public artifacts."
  - "README presence confirms documentation only; it does not prove emitted RedactionReceipts, validators, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements/Infrastructure Condition Redaction Receipts

Condition-redaction receipt lane for Settlements/Infrastructure process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: settlements-infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-1f6feb">
  <img alt="Lane: condition redaction" src="https://img.shields.io/badge/lane-condition%20redaction-blue">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/settlements-infrastructure/condition_redaction/` is for condition-redaction receipt process memory only. It is not condition truth, infrastructure truth, dependency truth, exact-facility authority, sensitivity policy, proof, catalog authority, release authority, public artifact authority, public UI material, planning guidance, operations guidance, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document governed redaction of Settlements/Infrastructure condition and dependency material: review handoff, redaction/generalization support, aggregation support, validation support, correction support, rollback support, and release-candidate support.

Condition-redaction receipts record what transform happened, which policy and review references governed it, what input and output hashes apply, what finite outcome was recorded, and which downstream proof or release artifacts may inspect the receipt.

Condition-redaction receipts do **not** define sensitivity policy, prove asset condition, prove dependency state, approve release, create a public layer, make restricted infrastructure detail public, or replace ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, or RollbackCards.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested domain condition-redaction receipt lane is:

```text
data/receipts/settlements-infrastructure/condition_redaction/
```

This README documents the requested lane without claiming final receipt-layout authority. Parent `data/receipts/settlements-infrastructure/README.md` is still a greenfield stub. Exact condition-redaction receipt subtype layout remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms the pattern.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/settlements-infrastructure/condition_redaction/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | condition redaction / infrastructure redaction process memory |
| Domain lane | settlements-infrastructure |
| Related domain receipt parent | `data/receipts/settlements-infrastructure/` |
| Lifecycle payload authority | `data/raw/settlements-infrastructure/`, `data/work/settlements-infrastructure/`, `data/quarantine/settlements-infrastructure/`, and `data/processed/settlements-infrastructure/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Public access posture | No direct public path; no normal UI; no governed-public API exposure |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, or `QUARANTINE` when policy refs, reviewer refs, source role, condition/dependency sensitivity, input/output hashes, evidence refs, correction path, rollback target, or release state are insufficient |

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records redaction behavior; it is not the truth source. |
| Redaction is not release | A receipt can support review, proof, and release; it cannot approve publication. |
| Condition observations stay evidence-bound | The receipt does not certify asset condition or turn a source record into released truth. |
| Dependency detail stays protected | Dependency material remains restricted unless governed policy, review, proof, and release gates close. |
| Source roles stay explicit | Observed, administrative, aggregate, candidate, and derived contexts must not collapse. |
| Time facets stay distinct | Source, observed, valid, retrieval, release, and correction times remain separate where material. |
| Policy remains separate | Binding sensitivity, rights, source-role, publication, and release rules live in governed policy roots, not this receipt lane. |
| Review remains separate | ReviewRecord and release authority roles must remain visible and must not collapse into this receipt. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Settlements/Infrastructure condition-redaction receipt instances and receipt-local sidecars:

- RedactionReceipt, AggregationReceipt, ValidationReport, PolicyDecision reference, ReviewRecord reference, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, object refs, policy refs, reviewer refs, evidence refs, validation refs, input/output hashes, transform refs, aggregation refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect redaction receipt state without becoming proof, catalog, policy, release, public output, condition truth, dependency truth, exact-facility authority, operations authority, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw condition, facility, service-area, operator, dependency, or infrastructure source payloads | `data/raw/settlements-infrastructure/` or governed restricted storage |
| Work/candidate outputs | `data/work/settlements-infrastructure/` |
| Quarantined material | `data/quarantine/settlements-infrastructure/` |
| Processed Settlements/Infrastructure payloads | `data/processed/settlements-infrastructure/` |
| EvidenceBundle, ProofPack, CatalogMatrix, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, or discovery records | `data/catalog/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, signature, or release changelog | `release/` |
| Sensitivity, rights, source-role, publication, or release policy | `policy/` and governed policy roots |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| Pipeline code, tests, fixtures, package code, or CI workflows | `pipelines/`, `tests/`, `fixtures/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, planning instructions, operations instructions, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/settlements-infrastructure/condition_redaction/
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

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, policy authority, release authority, operations source, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Settlements/Infrastructure domain and condition-redaction receipt lane.
- [ ] Confirm canonical condition-redaction receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, policy refs, reviewer refs, object refs, input/output hashes, evidence refs, validation refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, condition/dependency sensitivity, review state, public generalization posture, caveats, and limitations are preserved where material.
- [ ] Confirm restricted condition, dependency, operator, service-area, or facility detail is not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where a public-safe derivative or release-candidate handoff is involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using this receipt in any public Settlements/Infrastructure claim path.
- [ ] Confirm receipt presence is not treated as condition truth, dependency truth, infrastructure authority, sensitivity policy, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when policy, review, rights, sensitivity, evidence, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, generated answer, released layer, planning instruction, or operations instruction uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/settlements-infrastructure/condition_redaction/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/settlements-infrastructure/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Settlements/Infrastructure doctrine owns infrastructure assets, networks, facilities, service areas, operators, condition observations, and dependencies. | **CONFIRMED by GitHub contents API during this edit** |
| Settlements/Infrastructure doctrine says condition observations, dependencies, operator-sensitive details, and exact facility geometry are restricted or review-gated by default. | **CONFIRMED by GitHub contents API during this edit** |
| Settlements/Infrastructure lifecycle says RedactionReceipt is load-bearing and public promotion fails closed when rights, source role, evidence, sensitivity, or release state is unresolved. | **CONFIRMED by GitHub contents API during this edit** |
| RunReceipt standard places governed run receipts under `data/receipts/` and includes redaction as a governed run type. | **CONFIRMED by GitHub contents API during this edit** |
| Exact condition-redaction subtype layout under `data/receipts/settlements-infrastructure/condition_redaction/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Settlements/Infrastructure condition-redaction receipt payloads exist under this subtree. | **UNKNOWN** |
| Emitted RedactionReceipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is condition truth, dependency truth, infrastructure authority, exact-facility authority, sensitivity policy, proof, catalog authority, release authority, public artifact authority, operations guidance, planning guidance, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../raw/settlements-infrastructure/README.md`](../../../raw/settlements-infrastructure/README.md)
- [`../../../work/settlements-infrastructure/README.md`](../../../work/settlements-infrastructure/README.md)
- [`../../../quarantine/settlements-infrastructure/README.md`](../../../quarantine/settlements-infrastructure/README.md)
- [`../../../processed/settlements-infrastructure/README.md`](../../../processed/settlements-infrastructure/README.md)
- [`../../../proofs/settlements-infrastructure/README.md`](../../../proofs/settlements-infrastructure/README.md)
- [`../../../catalog/domain/settlements-infrastructure/README.md`](../../../catalog/domain/settlements-infrastructure/README.md)
- [`../../../published/layers/settlements-infrastructure/README.md`](../../../published/layers/settlements-infrastructure/README.md)
- [`../../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md`](../../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md)
- [`../../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md`](../../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md`](../../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md)
- [`../../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md`](../../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md)
- [`../../../../docs/runbooks/settlements-infrastructure/PROMOTION_RUNBOOK.md`](../../../../docs/runbooks/settlements-infrastructure/PROMOTION_RUNBOOK.md)
- [`../../../../docs/runbooks/settlements-infrastructure/ROLLBACK_RUNBOOK.md`](../../../../docs/runbooks/settlements-infrastructure/ROLLBACK_RUNBOOK.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/settlements-infrastructure/condition_redaction/` is a Settlements/Infrastructure condition-redaction receipt lane for process memory only. It is not condition truth, dependency truth, infrastructure authority, exact-facility authority, sensitivity policy, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, operations guidance, planning guidance, or generated-answer truth.

[Back to top](#top)
