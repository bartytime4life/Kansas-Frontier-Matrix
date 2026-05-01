# GBIF Publication Operations

## KFM Meta Block v2
- doc_id: kfm://doc/fauna/gbif-publication-operations
- status: PROPOSED
- domain: fauna

Purpose: governed, fixture-backed publication operations for GBIF public occurrence answers.

Lifecycle: UI/API DTO -> Publication Package -> Audit Ledger -> Replay Verification -> Correction/Withdrawal/Rollback.

Chain: EvidenceBundle -> Public Aggregate -> Geoprivacy Receipt -> Catalog Entry -> Triplet Claim -> Runtime Answer -> UI DTO/Map -> Answer Receipt -> Publication Package -> Audit Ledger.

Includes contracts for package, status, audit ledger, replay verification, correction receipt, withdrawal receipt; validator and policy gates; CLI examples; promotion checklist; rollback/correction notes.

Forbidden fields: decimalLatitude/decimalLongitude and related exact-coordinate keys.
Forbidden language: confirmed present/verified present/known population/exact location phrases.

Limitations:
- GBIF occurrence aggregates are reported occurrence evidence, not confirmed species presence.
- Public output is generalized and does not expose exact coordinates.

NEEDS_VERIFICATION:
- Final schema-home convention between `schemas/<lane>` vs `schemas/contracts/v1/<lane>`.
- Whether fauna policy test harness expects `policy/fauna` or bundle-only registration.
