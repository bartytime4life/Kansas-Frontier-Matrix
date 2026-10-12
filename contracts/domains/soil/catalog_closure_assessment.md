# Soil CatalogClosureAssessment

Status: PROPOSED_INACTIVE  
Profile: `kfm.domains.soil.catalog-closure-assessment.v1`

`CatalogClosureAssessment` is a deterministic, no-network assessment of whether one Soil product candidate has enough declared, resolving support to be considered **catalog-ready for review**. It does not catalog, promote, release, deploy, publish, or authorize public use.

## Finite outcomes

- `READY_FOR_REVIEW`: all required closure dimensions are declared satisfied.
- `HOLD`: the assessment is structurally valid but one or more closure dimensions remain unresolved.
- `ERROR`: the candidate is malformed, contradictory, non-canonical, or over-authoritative.

## Required closure dimensions

1. semantic contract reference;
2. schema reference;
3. source descriptor reference;
4. support-type profile reference;
5. deterministic identity reference;
6. EvidenceBundle reference;
7. validation report reference;
8. rights decision reference;
9. sensitivity decision reference;
10. correction target reference;
11. rollback target reference.

Every dimension has one state: `SATISFIED`, `UNRESOLVED`, or `DENIED`. `READY_FOR_REVIEW` requires all eleven to be `SATISFIED`; `DENIED` or `UNRESOLVED` yields `HOLD`.

## Trust boundary

This profile assesses declared closure only. It does not dereference identifiers, authenticate evidence, evaluate policy, approve review, write CATALOG/TRIPLET state, promote, release, deploy, publish, or authorize public use. All effect flags are fixed `false`.
