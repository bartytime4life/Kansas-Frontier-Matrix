<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/full-atlas-retrieval-intent-query-snapshot-source-map
title: Full Atlas retrieval intent and query snapshot — source map
type: intake/exploratory
version: v1
status: draft
owners: source-steward, contracts-steward, validation-steward
created: 2026-08-11
updated: 2026-08-11
policy_label: public
owning_root: docs/
responsibility: Exploratory source-to-repository adaptation record for a fixture-only declared-versus-executed retrieval query assessment.
truth_posture: Proposed implementation source map; no source, request, evidence, policy, lifecycle, release, publication, or public-use authority.
related:
  - contracts/source/retrieval_intent_query_snapshot_assessment.md
  - contracts/source/occurrence_retrieval_snapshot.md
  - contracts/source/source_artifact.md
  - docs/kfm_full_atlas_seed_cards.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [retrieval, query, provenance, pagination, source, full-atlas, intake, exploratory]
notes: Source-backed, fixture-only adaptation of KFM-TRIAD-043.
[/KFM_META_BLOCK_V2] -->

# Full Atlas retrieval intent and query snapshot — source map

## Source evidence

**CONFIRMED:** Connected Google Drive item `KFM_Full_Atlas_seed_cards` (file ID `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) contains `KFM-TRIAD-043`, “Retrieval Intent and Query Snapshot.” The repository mirror at `docs/kfm_full_atlas_seed_cards.md`, SHA-256 `07c7765576df1997e0be88141bd3cd213930e7281d490a8ae62afd78abe8f445`, records:

- `KFM-CAND-0127`: retrieval intent, normalized predicates, scopes, pagination, sampling, fields, and result selection as versioned provenance;
- `KFM-CAND-0128`: reviewer visibility into descriptor version, query scope, fields, filters, exclusions, boundaries, safe authentication posture, result count, and deviations; and
- `KFM-CAND-0129`: deterministic normalization, secret exclusion, descriptor references, request/response digests, pagination closure, and finite incomplete or changed-query outcomes.

**CONFIRMED:** The atlas explicitly says retrieval intent does not grant source admission, rights, claim authority, evidence closure, or release and that secret values remain outside public receipts.

**UNKNOWN:** The source material does not prove adoption by a runtime query engine, correctness of a real query, completeness of a real response, or fitness for public use.

## Repository gap and collision check

**CONFIRMED:** The implementation base was `main@ded9a9755316fee97827d5d65b8fc26e31c2ae4b`. Repository and pull-request searches were repeated before authoring.

**CONFIRMED:** `OccurrenceRetrievalSnapshotCandidate` already binds retrieval intent, a normalized query, sampling support, and transfer state for eBird and GBIF. It is intentionally source-family-specific and carries biological non-detection rules that must not become a repository-wide query contract.

**CONFIRMED:** Open PR #2592 proposes `SourceRetrievalEpisode`, which records an observed retrieval attempt and preserves failure, conditional, and body-transfer outcomes. This packet does not duplicate transport status, HTTP semantics, retry history, or body identity. Its nullable `retrieval_episode_ref` is a non-resolving future binding only.

**CONFIRMED:** Current main had no repository-wide assessment that deterministically compared declared versus executed fields, filters, exclusions, geographic scope, temporal scope, sampling, pagination mode, result selection, and authentication posture as one finite decision.

## Adaptation

**PROPOSED:** Add one inactive `RetrievalIntentQuerySnapshotAssessmentCandidate` envelope with three nested responsibilities:

1. `retrieval_intent` records the declared normalized plan;
2. `query_snapshot` records the executed normalized query and safe digests; and
3. `retrieval_receipt` records exact deviations, pagination closure, and result interpretation.

The validator emits `PASS` only for a matched, completed, pagination-closed declaration. A coherent partial or failed retrieval yields `ABSTAIN`; a changed query yields `DENY`; malformed or identity-tampered input yields `ERROR`. Zero rows remain a no-claim result.

## Directory placement

**CONFIRMED:** `docs/doctrine/directory-rules.md`, adopted by ADR-0029, requires responsibility-aligned placement and reuse of existing roots. Semantics therefore remain under `contracts/source/`; shape under `schemas/contracts/v1/source/`; fixtures under `fixtures/contracts/v1/source/`; validation under `tools/validators/source/`; tests under `tests/source/`; orchestration under `.github/workflows/`; this adaptation record under `docs/intake/exploratory/`; and generated-work provenance under `data/receipts/generated/`.

## Deliberate limits

This proposal does not store raw query values or secrets, dereference the descriptor or episode reference, contact a source, submit a job, authenticate a response, prove source completeness, create a `SourceArtifact`, resolve evidence, decide rights or policy, mutate lifecycle state, approve review, release, deploy, publish, or authorize public use.

## Follow-up candidates

1. **NEEDS VERIFICATION:** Human stewards should decide whether this generic envelope should remain standalone or become a compatibility profile around a future accepted `RetrievalIntent` / `QuerySnapshot` / `RetrievalReceipt` family.
2. **NEEDS VERIFICATION:** After PR #2592 reaches an independently reviewed disposition, a separate compatibility change may constrain `retrieval_episode_ref` to its accepted identity format.
3. **NEEDS VERIFICATION:** Any runtime adapter must prove secret-handling and normalized-request construction without logging raw credentials or sensitive scope values.
