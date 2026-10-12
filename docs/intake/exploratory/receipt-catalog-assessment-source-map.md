<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/receipt-catalog-assessment-source-map
title: Receipt Catalog Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · Governance steward · Receipt-family stewards · Release steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded adaptation of the master receipt catalog proposal into a bounded conflict-preserving assessment without defining receipt schemas or writing a canonical catalog
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/governance/receipt_catalog_assessment.md
  - ../../atlases/receipt-catalog.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../adr/INDEX.md
tags: [kfm, atlas, governance, receipt, lifecycle, source-map]
[/KFM_META_BLOCK_V2] -->

# Receipt Catalog Assessment Source Map

## Source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| Google Drive `KFM_Full_Atlas_seed_cards`, document `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho` | The "Master Receipt Catalog and Lifecycle Mapping" pattern proposes a uniform receipt taxonomy, lifecycle coverage, and a receipt-by-phase validator. | Proposal register, not schema or implementation authority. |
| `docs/atlases/receipt-catalog.md` | Existing carrier enumerates the Atlas 24.2 catalog, lifecycle mapping, and a `CONFLICTED` adjacent inventory. | Navigation and doctrine carrier; it explicitly does not settle receipt-schema layout. |
| `docs/adr/INDEX.md` | Current decision inventory shows receipt/proof/manifest/catalog separation remains proposed rather than accepted. | Inventory only; it cannot accept a classification. |
| Current semantic contracts | The checked repository already has independent `AIReceipt`, `RunReceipt`, `PromotionReceipt`, `RedactionReceipt`, `ReleaseManifest`, and `SourceDescriptor` contracts. | Presence proves independent meanings exist; it does not unify or reclassify them. |

## Repository reconciliation

GitHub `main@c4cb046829f72afd07e39d167c781fb7435a9ac4` already contained the
human receipt catalog and several receipt or adjacent object-family contracts,
but repository search found no `ReceiptCatalogAssessmentCandidate`, matching
schema, validator, fixtures, tests, workflow, or generated authoring receipt.
The existing carrier also records one unresolved family in this synthetic set:
`EventRunReceipt` has source/schema surfaces but no single semantic contract
path selected by the carrier.

The implementation therefore adds an assessment only. It does not create
`schemas/contracts/v1/receipts/`, extend the Atlas, or decide ADR-S-03.

## Bounded adaptation

| Source pressure | Retained behavior | Deferred authority |
|---|---|---|
| Uniform taxonomy | Families carry an explicit object class and source basis. | Receipt-versus-manifest reclassification. |
| Lifecycle map | Phases are finite, unique, and ordered. | Gate requirements and operational emission. |
| Contract closure | Existing semantic contract paths are checked when declared. | Choosing a canonical schema family or inventing missing contracts. |
| Conflict visibility | Adjacent-only families remain `CONFLICTED_ADJACENT`. | Acceptance, supersession, or catalog rewrite. |

## Path decision

~~~yaml
path_decision:
  artifact: ReceiptCatalogAssessmentCandidate
  proposed_path: contracts/governance/receipt_catalog_assessment.md
  artifact_kind: semantic contract
  authority_owner: receipt-catalog conflict assessment meaning
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: object_family
  scope_id: receipt-catalog-assessment
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/atlases/receipt-catalog.md
    - docs/adr/INDEX.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
~~~

The governance contract lane owns the meaning of a conflict-preserving
assessment. Receipt instance contracts remain in their existing responsibility
lanes; schemas remain under `schemas/contracts/v1/`; no parallel catalog or
schema home is created.

## Non-effects

This packet does not define receipt instance fields, reclassify manifests or
records, accept an ADR, write a canonical catalog, resolve evidence, evaluate
policy, approve review, promote, release, deploy, publish, or authorize public
use.
