<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/occurrence-retrieval-snapshot
title: Occurrence Retrieval Snapshot Candidate Contract
type: semantic-contract; fixture-first; no-network
version: v0.1.0
status: proposed; fixture-only; no-live-source
owners: OWNER_TBD — Source steward · Fauna/Flora steward · Contracts steward · Validation steward · Rights/sensitivity steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; source; retrieval; no-publish
related:
  - ./source_adapter.md
  - ./source_artifact.md
  - ../../schemas/contracts/v1/source/occurrence_retrieval_snapshot.schema.json
  - ../../fixtures/contracts/v1/source/occurrence_retrieval_snapshot/
  - ../../tools/validators/validate_occurrence_retrieval_snapshot.py
  - ../../tests/validators/test_validate_occurrence_retrieval_snapshot.py
  - ../../docs/intake/exploratory/new-ideas-4-30-source-map.md
  - ../../docs/sources/catalog/ebird/sampling-event-data.md
  - ../../docs/sources/catalog/gbif/async-download.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, source, retrieval-intent, query-snapshot, sampling-support, async-transfer, ebird, gbif, no-network]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Occurrence Retrieval Snapshot Candidate Contract

> A fixture-first record that binds **why** an eBird or GBIF occurrence subset is requested, **what normalized query was declared**, **what sampling support the result can honestly provide**, and **where the source-native transfer currently stands**. It is process planning and replay metadata, not source admission, evidence, occurrence truth, absence proof, policy approval, or release authority.

## Source-derived gap

The repository's governed source map for *New Ideas 4-30-26* classifies the broad eBird/GBIF adapter recipes as corroborative or partial, while identifying a shared gap: no common artifact bound retrieval intent, query predicates, sampling support, and asynchronous transfer state before source-specific code. This contract closes only that seam.

Existing source pages already carry important source-native distinctions:

- eBird Sampling Event Data is the checklist/effort companion to EBD. The EBD × SED pair enables checklist-event non-detection only when complete-checklist support is present.
- GBIF bulk retrieval is an asynchronous, predicate-defined occurrence transfer. A queued, failed, cancelled, or expired job is not an empty biological result.
- SourceAdapter and SourceArtifact remain separate: the adapter owns transport mechanics; SourceArtifact identifies exact captured bytes; this candidate records a request snapshot and transfer history.

## Bounded context

| Candidate may describe | Candidate must not do |
|---|---|
| Synthetic eBird or GBIF retrieval intent | Activate either source or submit a real request |
| Safe, normalized, credential-free predicates | Embed tokens, usernames, passwords, email addresses, or raw job keys |
| Kansas county/date/taxon selectors | Carry exact coordinates or sensitive occurrence geometry |
| Sampling support and non-detection limits | Upgrade observations into specimen evidence or broad absence claims |
| Append-only transfer-state history | Treat failure, timeout, cancellation, or missing rows as zero records |
| Digest-bound result-artifact references | Resolve EvidenceRefs, approve rights/sensitivity, or publish |

## Object surface

`OccurrenceRetrievalSnapshotCandidate` contains four connected but non-interchangeable parts:

1. **`retrieval_intent`** — purpose, requested claim support, public-output posture, and explicit denial of exact-coordinate and absence requests.
2. **`query_snapshot`** — normalized selectors and predicates, a digest of the source-native request representation, and a deterministic `query_hash`. Credentials and notification addresses are fixed absent.
3. **`sampling_support`** — what the selected source and declared filters can support. This is not a confidence score.
4. **`transfer`** — append-only finite state history, safe native-job-key digest when applicable, result-artifact references, citation references, and result interpretation.

## Sampling-support anti-collapse rules

| Source/profile | Honest support | Required conditions | Explicit non-effects |
|---|---|---|---|
| eBird `COMPLETE_CHECKLIST_EBD_SED` | Checklist-event non-detection | Paired EBD/SED artifacts, same declared release, complete checklists, and declared effort fields | Not county-wide or timeless absence; not specimen evidence |
| eBird presence-only | Source-reported observation | Non-detection disabled; no EBD/SED absence inference | Not evidence of species absence |
| GBIF `PRESENCE_ONLY_OCCURRENCE` | Aggregated source-reported occurrence | Coordinate and geospatial-issue predicates declared; later per-dataset rights review | Not non-detection or absence; not automatic public fitness |

`absence_claim_supported` is false in this v1 profile. A complete eBird checklist can support a non-detection statement for that checklist event; it cannot prove that a species is absent from a county, habitat, season, or historical interval.

The numeric thresholds in synthetic predicates are fixture examples. They are not adopted universal source policy, current source terms, or scientifically validated cutoffs.

## Transfer state and false-empty prevention

Finite states are:

```text
NOT_SUBMITTED -> SUBMITTED -> QUEUED -> RUNNING -> SUCCEEDED
                              |         |          \
                              +---------+---------> FAILED | CANCELLED | EXPIRED
```

The validator also permits direct `SUBMITTED -> SUCCEEDED` for a synthetic bulk-file profile. State history is timestamp ordered and append-only inside each snapshot. The final history state must equal `current_state`.

Rules:

- `SUCCEEDED` requires immutable `SourceArtifact` references and a non-null record count.
- A successful zero-record response is `zero_records_no_claim`, never absence.
- Nonterminal or failed states have no result artifacts, no record count, and `not_evaluated` interpretation.
- `FAILED`, `CANCELLED`, and `EXPIRED` require an explicit safe reason code.
- GBIF success requires a digest-bound citation reference; the validator does not dereference or authenticate it.
- Raw job keys never appear. Only an optional SHA-256 digest may be carried.

## Deterministic identity

```text
query_hash    = SHA-256(canonical query_snapshot excluding query_hash)
retrieval_id  = kfm://candidate/source/occurrence-retrieval/<source_family>/<query_hash-hex>
revision      = number of transfer state-history entries
snapshot_id   = <retrieval_id>/revision/<revision>
spec_hash     = SHA-256(canonical top-level record excluding spec_hash)
```

`previous_snapshot_ref` points to the immediately prior revision when `revision > 1`. These identities make retries and state progression inspectable without treating the candidate as an operational source record.

## Rights, sensitivity, and public boundary

Every v1 fixture remains:

- `rights = NEEDS_VERIFICATION`;
- `sensitivity = NEEDS_VERIFICATION`;
- `release = HOLD`;
- `public_use_allowed = false`;
- `source_activation_allowed = false`; and
- `evidence_resolution_performed = false`.

Exact geometry fields, references into RAW/WORK/QUARANTINE, and secret-bearing fields are denied. Public aggregates, source terms, per-dataset licenses, observer privacy, rare-species handling, evidence resolution, review, and release remain separate later gates.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2 and places this slice by responsibility:

- semantic meaning: `contracts/source/`;
- machine shape: `schemas/contracts/v1/source/`;
- synthetic examples: `fixtures/contracts/v1/source/`;
- executable validation: `tools/validators/`;
- enforceability: `tests/validators/`;
- hosted orchestration: `.github/workflows/`; and
- AI authoring provenance: `data/receipts/generated/`.

The contract creates no new root and no parallel source registry, evidence store, policy home, lifecycle store, receipt authority, proof authority, release authority, or publication path.

## Validation

```bash
python -m pytest -q -p no:cacheprovider \
  tests/validators/test_validate_occurrence_retrieval_snapshot.py

python tools/validators/validate_occurrence_retrieval_snapshot.py --fixtures
```

A green result proves only closed schema shape, deterministic identity, exact synthetic fixture polarity, sampling-support anti-collapse, and transfer-state consistency.

## Rollback

Before merge, close the draft pull request and delete its task branch. After an authorized merge, revert the dependency-closed contract/schema/fixtures/validator/tests/workflow/receipt slice. No live source, request, job, captured artifact, lifecycle data, release, deployment, or published object requires cleanup.

[Back to top](#top)
