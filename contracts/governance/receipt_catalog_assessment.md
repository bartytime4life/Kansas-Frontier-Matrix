<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/receipt-catalog-assessment
title: Receipt Catalog Assessment Candidate
type: semantic-contract
version: v0.1.0
status: proposed; inactive; review-pending; non-authoritative
owners: OWNER_TBD — Governance steward · Receipt-family stewards · Release steward · Contracts steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; governance; receipts; lifecycle; fixture-only
owning_root: contracts/
responsibility: Define a bounded assessment of receipt-family catalog and lifecycle declarations without creating receipt schema authority or reclassifying manifests, proofs, records, or release objects.
truth_posture: PROPOSED source-grounded adaptation / CONFIRMED deterministic fixture validation / CONFLICTED receipt-family inventory remains review-required
related:
  - ../../docs/atlases/receipt-catalog.md
  - ../../docs/adr/INDEX.md
  - ../../schemas/contracts/v1/governance/receipt_catalog_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/receipt_catalog_assessment/cases.json
  - ../../tools/validators/governance/validate_receipt_catalog_assessment.py
  - ../../tests/validators/governance/test_receipt_catalog_assessment.py
  - ../../docs/intake/exploratory/receipt-catalog-assessment-source-map.md
tags: [kfm, governance, receipt, manifest, lifecycle, assessment, fixture-only]
notes:
  - "Implements a bounded assessment slice of the Full Atlas Master Receipt Catalog and Lifecycle Mapping proposal."
  - "The packet records the existing Atlas-versus-adjacent-doctrine conflict and does not settle ADR-S-03, define receipt instances, or write a canonical catalog."
[/KFM_META_BLOCK_V2] -->

# Receipt Catalog Assessment Candidate

> A deterministic, fixture-only assessment for keeping receipt families,
> record families, manifest families, lifecycle declarations, and unresolved
> schema authority visible without silently collapsing them.

## Status and purpose

| Field | Value |
|---|---|
| Profile | `kfm.receipt-catalog-assessment-candidate.v1` |
| State | `PROPOSED` / inactive / review-pending |
| Positive result | `PASS` with `assessment_state: REVIEW_REQUIRED` |
| Canonical receipt catalog or schema effect | None |
| Release, deployment, publication, or public-use effect | None |

The human `docs/atlases/receipt-catalog.md` carrier identifies a doctrinal
catalog and a second adjacent inventory that includes additional records,
manifests, and bundles. It marks reconciliation as unresolved. This contract
turns that conflict into a closed candidate shape so maintainers can inspect:

- which source inventory reports a family;
- whether the family is a receipt, record, report, decision, manifest, bundle,
  notice, or source anchor;
- the lifecycle phases declared for the family;
- whether an existing semantic-contract path is known; and
- whether schema authority remains unresolved.

The assessment does **not** decide whether a family should be called a receipt.
It cannot create or amend a receipt schema, alter a lifecycle gate, write a
control-plane register, or authorize an operation.

## Deterministic validation

The validator requires canonical lexical ordering, unique family IDs, ordered
and non-duplicated lifecycle phases, existing local semantic-contract paths
when declared, internally consistent summary counts, and JCS plus SHA-256
identity. It rejects:

- duplicate or unsorted family rows;
- unsorted, duplicate, or unknown lifecycle phases;
- a source-basis/authority-state mismatch;
- direct references to RAW, WORK, QUARANTINE, URLs, databases, or query text;
- missing or unsafe semantic-contract references;
- stale summary, digest, or assessment identifier fields; and
- any schema-authority, reclassification, catalog-write, release, publication,
  or public-use claim.

## Finite outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | The synthetic catalog assessment is internally consistent. | Still `REVIEW_REQUIRED`; no family classification is adopted. |
| `DENY` | Shape, ordering, identity, reference, or authority invariants fail. | No fallback reclassification or register write. |
| `ERROR` | Input, schema, or bounded repository reference cannot be read safely. | No partial assessment is trusted. |

## Directory Rules basis

| Responsibility | Home |
|---|---|
| Candidate assessment meaning | `contracts/governance/` |
| Machine shape | `schemas/contracts/v1/governance/` |
| Synthetic cases | `fixtures/contracts/v1/governance/` |
| Deterministic validation | `tools/validators/governance/` |
| Executable conformance evidence | `tests/validators/governance/` |
| Hosted read-only orchestration | `.github/workflows/` |
| Source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No receipt schema home, canonical catalog, control-plane register, release
surface, or new root is created.

## Non-effects

A green result does not:

- decide ADR-S-03 or any successor receipt-layout decision;
- define fields for a receipt instance;
- reclassify a manifest, bundle, report, record, notice, or decision as a receipt;
- prove that every receipt family is implemented or emitted;
- write or replace `docs/atlases/receipt-catalog.md`;
- resolve evidence, evaluate policy, approve review, promote, release, deploy,
  publish, or authorize public use.

## Rollback

Before merge, close the draft pull request and remove its branch. After an
authorized merge, revert this additive packet and rerun its dedicated workflow.
No receipt, registry, policy, data, release, deployment, or public state requires
restoration.
