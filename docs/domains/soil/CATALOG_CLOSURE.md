<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/catalog-closure
title: Soil catalog closure review
type: domain-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Soil catalog closure review; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/soil/README.md
  - contracts/domains/soil/catalog_closure_assessment.md
  - tools/validators/domains/soil/validate_catalog_closure_assessment.py
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Soil catalog closure

Use this guide to prepare one Soil candidate for catalog review. At the pinned
repository snapshot, `release/candidates/soil/` and `data/proofs/soil/` contain
README material only. No completed Soil catalog or proof-bearing release is
established by those lanes.

## Current bounded implementation

The [assessment contract](../../../contracts/domains/soil/catalog_closure_assessment.md)
and [validator](../../../tools/validators/domains/soil/validate_catalog_closure_assessment.py)
implement a deterministic, fixture-only declaration check. The validator does
not dereference or authenticate the supplied references. A reviewer must inspect
the actual supporting artifacts independently.

## Closure dimensions

| Required dimension | What the reviewer must establish outside the fixture assessment |
|---|---|
| Semantic contract | Exact object family and meaning apply to this candidate |
| Schema | Versioned shape and validator agree; negative cases are rejected |
| Source descriptor | Source identity, product, edition and support role match |
| Support-type profile | Survey, grid, station, profile and interpretation remain distinct |
| Deterministic identity | Digest and native-key lineage bind this candidate |
| EvidenceBundle | References resolve to the claimed evidence under permitted access |
| Validation report | Exact candidate and validator version are identified |
| Rights decision | Intended access, reuse and attribution are reviewed |
| Sensitivity decision | Precision and downstream joins are reviewed |
| Correction target | A later correction can reach affected dependents |
| Rollback target | A verified prior state or explicit empty state is available |

The machine profile requires the eleven dimensions in its declared order. Each
has `SATISFIED`, `UNRESOLVED`, or `DENIED` state. A `SATISFIED` reference is only
a declaration at this layer; its existence does not prove the underlying claim.

## Review workflow

1. Pin the repository commit, candidate identity and content digest.
2. Compare the candidate to the exact contract, schema and support-type profile.
3. Inventory every required reference and test access through its owning surface.
   Missing evidence stays `UNRESOLVED`; a failed decision stays `DENIED`.
4. Run the bounded fixture checks below before evaluating a changed profile.
5. Record the assessment outcome and independent evidence-review findings as
   separate results. Route unresolved source, rights, sensitivity or rollback
   questions to the appropriate steward role; those assignments remain unbound.
6. Request the separately governed catalog transition only after its requirements
   are established. This document creates no catalog entry or review approval.

## Validation and result interpretation

```bash
python tools/validators/domains/soil/validate_catalog_closure_assessment.py --fixtures
python -m unittest tests.validators.domains.soil.test_soil_cli_fail_closed
```

`READY_FOR_REVIEW` means all eleven declarations are satisfied. `HOLD` means a
valid declaration has unresolved or denied dimensions. `ERROR` means malformed,
contradictory or over-authoritative input. The single-file CLI can exit zero for
`HOLD`; read the emitted outcome, not only the exit status. Fixture mode checks
that each case has its expected outcome.

## Troubleshooting and completion

For `ERROR`, check dimension order, count, reference/state consistency, immutable
assessment identity and all-false effect flags. Do not replace unknown evidence
with a dummy reference to obtain `READY_FOR_REVIEW`. A useful review packet ends
with a dimension-by-dimension evidence record, residual gaps and next owner.
Catalog writes, promotion, release, deployment, publication and public use remain
separate decisions. See [definition of done](DEFINITION_OF_DONE.md).
