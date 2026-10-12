<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/briefing-integration-source-record-absence-source-map
title: Briefing Integration — Source Record Absence Source Map
type: exploratory-source-map; implementation-assay
version: v0.1.0
status: draft; PROPOSED; current-session-repo-assay
owners: OWNER_TBD — Docs steward · Source steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; exploratory; source-map; false-clear; no-live-source-authority
related:
  - ../../../contracts/source/source_record_absence_assessment.md
  - ../../../schemas/contracts/v1/source/source_record_absence_assessment.schema.json
  - ../../../tools/validators/validate_source_record_absence_assessment.py
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "The attached briefing architecture is design evidence, not implementation authority."
  - "Current main was searched for an equivalent shared contract before this profile was selected."
[/KFM_META_BLOCK_V2] -->

# Briefing Integration — Source Record Absence Source Map

## Evidence checkpoint

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Assayed base | `main@ead1250f2923d1532257ec50cb44729be6f6c751` |
| Design source | `KFM_Briefing_to_System_Integration_Architecture.docx`, especially §§10.4 and 13.3 |
| Supporting exploratory source | `New Ideas 3-16-26.pdf` |
| Directory authority | Accepted `ADR-0029`; canonical rules at `docs/doctrine/directory-rules.md` |
| Selected implementation | Fixture-first `SourceRecordAbsenceAssessment` profile |
| Live source/network activation | None |

## Candidate assay

| Candidate | Disposition | Current-session reason |
|---|---|---|
| Generic missing-record source semantics | **SELECTED** | The briefing architecture gives explicit safe behavior for complete snapshots, incremental feeds, publication pages, and mixed surfaces. No shared contract with this name or equivalent finite profile was found on the assayed base. |
| Immediate source-adapter integration | **DEFERRED** | Adapter-specific completeness, health, parser, rights, and operational semantics require separate evidence and tests. |
| AQS watcher correction | **DEFERRED FOLLOW-UP** | Current code contains a domain-specific prior-present/current-absent `SITE_REMOVED` path, but changing it safely requires source-contract evidence and focused regression fixtures beyond this common profile. |
| Public advisory clearing | **DENIED IN THIS SLICE** | Domain authority, rescission/expiration policy, evidence closure, review, and release remain separate. |
| Live polling, storage, or publication | **OUT OF SCOPE** | The first increment is deterministic, synthetic, no-network, and release-neutral. |

## Source-derived rule

The briefing architecture states that every adapter must declare whether its source is a complete current-state snapshot, change log or incremental event feed, publication page, or mixed surface. A missing row may support a removal candidate only for a healthy, complete authoritative snapshot. Incremental-feed absence retains prior state; publication-page and mixed-surface absence remain ambiguous and fail closed.

The public-safety section applies the same asymmetry: failed retrieval never clears an active event, a missing incremental row cannot clear without explicit source semantics, and an unverified current status is safer as abstention or `STATUS_UNCONFIRMED` than as false clearance.

## Repository gap evidence

Searches at the assayed base found no `SourceRecordAbsenceAssessment` family and no shared source-level contract implementing the complete-snapshot versus incremental-feed table. The repository does contain source contracts, bounded validators, deterministic fixture profiles, and accepted Directory Rules placement. Those current patterns support an additive dependency-closed profile under established roots.

A current domain-specific example exists in `tools/ingest/aqs_watch/aqs_site_delta.py`: a previously present site missing from the current input becomes `SITE_REMOVED`. This source map does not classify that behavior as defective without source-contract evidence; it records it as the first candidate for a later integration test.

## Directory Rules result

`PLACE` under existing responsibility roots:

- semantic meaning → `contracts/source/`;
- machine shape → `schemas/contracts/v1/source/`;
- synthetic examples → `fixtures/contracts/v1/source/`;
- validator → `tools/validators/`;
- tests → `tests/validators/`;
- CI orchestration → `.github/workflows/`;
- source-map documentation → `docs/intake/exploratory/`;
- authoring provenance → `data/receipts/generated/`.

No new root, data lifecycle write, source registry record, policy authority, release object, or public route is created.

## Next governed increment

After review of this profile, select one real adapter whose source contract can establish mode, health, completeness, parser confidence, correction behavior, and rights. Add adapter-specific fixtures proving that source failure, partial parsing, and missing incremental events preserve prior state, while only a verified complete snapshot can emit a removal candidate. Keep the domain transition and public release decisions separate.
