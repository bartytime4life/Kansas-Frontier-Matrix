# RetrievalIntentQuerySnapshotAssessment

`RetrievalIntentQuerySnapshotAssessmentCandidate` is an inactive, fixture-only profile for comparing a declared retrieval intent with the normalized query that was actually executed. It preserves geographic and temporal scope, requested fields, filters, exclusions, sampling, pagination, safe authentication posture, request and response digests, result count, and deviations without storing secret values.

The profile implements the repository-wide seam proposed by Full Atlas `KFM-TRIAD-043` (`KFM-CAND-0127` through `KFM-CAND-0129`). It does not replace the occurrence-specific `OccurrenceRetrievalSnapshotCandidate`, which owns eBird/GBIF sampling and transfer semantics. It also does not replace `SourceRetrievalEpisode`, which records observed retrieval-process outcomes. This candidate owns only declared-versus-executed query reconciliation.

## Finite outcomes

| Assessment outcome | Validator outcome | Meaning |
|---|---|---|
| `MATCHED_COMPLETE` | `PASS` | Declared and executed query semantics match, execution completed, and pagination closed. |
| `INCOMPLETE` | `ABSTAIN` | Query semantics match, but a partial execution or open page/job boundary prevents a completeness claim. |
| `FAILED` | `ABSTAIN` | Query semantics match, but the retrieval failed and no result or absence claim is made. |
| `CHANGED_QUERY` | `DENY` | One or more normalized query dimensions differ from the declared intent. |
| malformed, contradictory, or identity-tampered input | `ERROR` or `DENY` | Shape, deterministic identity, or cross-field coherence failed. |

`PASS` means internal fixture coherence and readiness for human review only. It does not prove that a source answered correctly, returned all qualifying records, or is admissible.

## Normalization and secret exclusion

- requested and executed fields are unique and lexicographically ordered;
- filters are unique and ordered by `(field, operator, value_digest)`;
- exclusions are unique and lexicographically ordered;
- geographic values and filter values are represented only by SHA-256 digests;
- the endpoint is an opaque source-interface reference, not a URL;
- authentication is limited to `NONE`, `REFERENCE_ONLY`, or `REDACTED_REFERENCE`; and
- `secrets_embedded` and `secret_values_recorded` are fixed `false`.

The validator derives deviation codes by comparing the normalized intent and snapshot. It never normalizes an unsafe raw request on the caller's behalf.

## Completion and false-empty rules

`COMPLETE` requires a response digest, result count, and closed pagination. `PARTIAL` requires an open page or job boundary. `FAILED` carries neither a response digest nor a result count. A zero result count remains `ZERO_RECORDS_NO_CLAIM`; it is not evidence of absence.

## Deterministic identity

The query hash is SHA-256 over canonical JSON for `query_snapshot` excluding only `query_hash`. The assessment `spec_hash` is SHA-256 over the complete object excluding only `assessment_id` and `spec_hash`. `assessment_id` uses the first 24 digest characters with prefix `retrieval-query-assessment:`.

## Trust and authority boundary

Validation performs no network request, secret resolution, source admission, rights determination, source-response authentication, completeness proof, evidence resolution, policy decision, human approval, lifecycle mutation, release, deployment, publication, or public-use authorization. Every authority-bearing effect is fixed `false`.

## Directory Rules basis

Source-process semantics belong in `contracts/source/`; machine shape in `schemas/contracts/v1/source/`; synthetic cases in `fixtures/contracts/v1/source/`; reusable validation in `tools/validators/source/`; executable proof in `tests/source/`; CI orchestration in `.github/workflows/`; exploratory adaptation in `docs/intake/exploratory/`; and generated-work provenance in `data/receipts/generated/`. This uses existing responsibility roots adopted through ADR-0029 and creates no parallel source, query, receipt, evidence, proof, policy, lifecycle, or release authority.

## Rollback

Before merge, close the draft pull request and remove its task branch. After an authorized merge, revert this additive packet and rerun its focused workflow. No live request, source artifact, lifecycle data, release, deployment, cache, or public surface requires restoration.
