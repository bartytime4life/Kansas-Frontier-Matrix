<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-set-operation-provenance-receipt-source-map
title: Pass 18 Set-Operation Provenance Receipt Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Evidence steward · Source-reconciliation steward · Data-quality steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; set-operation; provenance
responsibility: Reconcile one supplied set-operation provenance idea with current repository evidence while withholding private discovery-source identifiers from public provenance.
truth_posture: "CONFIRMED supplied-card and repository gap; PROPOSED inactive implementation profile; UNKNOWN consumer adoption and engine-specific equivalence; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/evidence/set_operation_provenance_receipt.md
  - ../../../contracts/common/reversible_entity_reconciliation.md
  - ../../../contracts/common/measurement_support_reconciliation.md
  - ../../../contracts/evidence/spatial_transform_receipt.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-18, set-operation, provenance, reconciliation]
[/KFM_META_BLOCK_V2] -->

# Pass 18 Set-Operation Provenance Receipt Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-068` | Cross-source set operations should preserve the operator and duplicate policy in provenance because `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT` can produce materially different reconciliation results. | `CONFIRMED` source statement |
| `contracts/common/reversible_entity_reconciliation.md` | The existing profile preserves reversible entity-identity decisions, not the set operator used to combine declared inputs. | `CONFIRMED` adjacent contract |
| `contracts/common/measurement_support_reconciliation.md` | The existing profile checks scientific measurement comparability, not union, intersection, or difference semantics. | `CONFIRMED` adjacent contract |
| `contracts/evidence/spatial_transform_receipt.md` | The existing receipt records a spatial transform and digest-bound artifacts but does not record ordered set inputs or duplicate treatment. | `CONFIRMED` adjacent contract |
| Starting `main@463381703bcd6eada8eea05e95c4a88912ed4b02` search | No exact card ID, set-operation provenance receipt contract, schema, fixture family, validator, workflow, branch, or matching pull request was found before implementation. | `CONFIRMED` bounded gap |
| Connected private research corpus | Used only for candidate discovery and corroboration. Private file identifiers, URLs, and copied prose are intentionally excluded. | `CONFIRMED` provenance boundary |

## Adaptation

The implementation is a closed, synthetic process-memory candidate under the existing evidence family. It records execution family, set operator, duplicate and alignment policies, null-semantics and method references, canonically ordered digest-bound inputs, one digest-bound output, safe row-count bounds, and opaque query-plan and reconciliation-rule references.

The supplied card also proposed a query-plan receipt. Current `main` has no such exact authority object, so this packet carries only a digest-bound, resolvable query-plan reference. It neither creates query-plan authority nor stores query text.

## Directory Rules basis

The packet uses existing responsibility roots: semantic meaning in `contracts/evidence/`, shape in `schemas/contracts/v1/evidence/`, synthetic replay in `fixtures/contracts/v1/evidence/`, repository validation in `tools/validators/evidence/`, conformance evidence in `tests/validators/evidence/`, orchestration in `.github/workflows/`, this reconciliation in `docs/intake/exploratory/`, and authoring accountability in `data/receipts/generated/`.

No query executor, source registry, canonical dataset, entity-identity decision, evidence store, catalog writer, policy rule, lifecycle state, release record, or public surface is created.

## Non-effects and rollback

A local `PASS` authenticates no source, input, output, schema, method, query plan, reconciliation rule, evidence, policy, review, release, publication, or public-use state. Rollback is a single additive revert with no external cleanup.
