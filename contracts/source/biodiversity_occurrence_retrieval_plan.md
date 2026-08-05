<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/biodiversity-occurrence-retrieval-plan
title: BiodiversityOccurrenceRetrievalPlanCandidate Contract
type: semantic-contract; source-retrieval; biodiversity; fixture-first
version: v0.1.0
status: draft; PROPOSED; no-network; no-source-or-release-authority
owners: OWNER_TBD — Source steward · Fauna/Flora stewards · Contracts steward · Schema steward · Validation steward · Rights and sensitivity reviewers
created: 2026-08-05
updated: 2026-08-05
policy_label: public; source; retrieval-plan; query-snapshot; sampling-support; transfer-state; non-authoritative
related:
  - ./README.md
  - ./source_adapter.md
  - ../../schemas/contracts/v1/source/biodiversity_occurrence_retrieval_plan.schema.json
  - ../../fixtures/contracts/v1/source/biodiversity_occurrence_retrieval_plan/
  - ../../tools/validators/validate_biodiversity_occurrence_retrieval_plan.py
  - ../../tests/validators/test_validate_biodiversity_occurrence_retrieval_plan.py
  - ../../docs/intake/exploratory/new-ideas-4-30-source-map.md
  - ../../docs/sources/catalog/gbif/async-download.md
  - ../../docs/sources/catalog/ebird/ebird-basic-dataset.md
  - ../../docs/sources/catalog/ebird/sampling-event-data.md
tags: [kfm, biodiversity, retrieval-intent, query-snapshot, sampling-support, async-transfer, ebird, gbif, no-network]
notes:
  - "Closes the bounded source-map gap: define retrieval intent, query snapshot, sampling support, and asynchronous-transfer state before source-specific live code."
  - "The source-specific GBIF and eBird fetch modules remain placeholders and are not activated by this contract."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BiodiversityOccurrenceRetrievalPlanCandidate

> A `BiodiversityOccurrenceRetrievalPlanCandidate` is a deterministic, reviewable description of what a proposed eBird or GBIF retrieval would ask for, what sampling claims the source can support, and what finite transfer state has actually been observed. It is planning and process memory, not source admission, evidence, policy, release, or publication authority.

## Goal

The New Ideas 4-30 packet repeatedly couples eBird and GBIF ingestion to four concerns that should be fixed before source-specific network code:

1. a bounded retrieval intent;
2. a canonical query snapshot that excludes credentials and notification addresses;
3. explicit sampling support, especially the EBD × SED and complete-checklist boundary; and
4. an asynchronous or manually approved bulk-transfer state that cannot be mistaken for successful retrieval.

Current repository source pages already describe GBIF's submit/poll/terminal workflow and the eBird EBD/SED pairing rule, while both source-specific fetch modules remain placeholders. This contract closes that common semantic seam without activating either source.

## Directory Rules basis

| Responsibility | Existing home used by this slice |
|---|---|
| Source-retrieval semantic meaning | `contracts/source/` |
| Machine-checkable shape | `schemas/contracts/v1/source/` |
| Synthetic examples | `fixtures/contracts/v1/source/` |
| Executable validation | `tools/validators/` |
| Enforceability | `tests/validators/` |
| Read-only hosted orchestration | `.github/workflows/` |
| AI authoring provenance | `data/receipts/generated/` |

The singular `source/` schema lane has known naming/placement drift documented by its README. This slice uses the existing lane and does not resolve, duplicate, or migrate that authority question. No new root or parallel source, schema, policy, registry, receipt, proof, release, or publication home is created.

## Object boundary

The candidate owns only:

- deterministic plan identity and local fixture `spec_hash`;
- source family/product/profile references;
- geography, time window, requested result granularity, and candidate claim role;
- a sanitized, digest-bound query snapshot;
- source-appropriate sampling-support declarations;
- finite transfer state and ordered state history;
- local provenance; and
- fixed non-authority declarations.

It does not own:

- source admission, activation, credentials, access approval, or terms acceptance;
- source bytes or RAW lifecycle records;
- an occurrence, checklist, sampling event, absence claim, or specimen identity;
- rights or sensitivity clearance;
- EvidenceRef/EvidenceBundle resolution;
- policy or human review;
- lifecycle promotion, release, deployment, publication, or public-use permission.

## Source profiles

### eBird EBD + SED

The eBird profile preserves the paired-product and effort boundary:

- product is `EBIRD_EBD_SED`;
- query language is `EBIRD_FILTER_PROFILE`;
- transfer mode is `MANUAL_APPROVED_BULK_FILE`;
- sampling mode is `CHECKLIST_EFFORT`;
- SED is required as the paired product;
- complete checklists and reviewed effort fields are required before zero fill or non-detection inference;
- non-detection remains distinct from absence; and
- eBird observations are never treated as specimen-equivalent evidence.

A missing SED pair, incomplete checklist posture, or missing effort field makes the sampling-support declaration invalid. Even a complete checklist cannot authorize an absence claim.

### GBIF occurrence download

The GBIF profiles preserve the predicate/SQL and asynchronous-job boundary:

- product is either `GBIF_OCCURRENCE_PREDICATE` or `GBIF_OCCURRENCE_SQL`;
- query language must match the product;
- transfer mode is `ASYNCHRONOUS_JOB`;
- sampling support is occurrence-only or aggregate-only;
- complete-checklist, zero-fill, and non-detection support are false; and
- a successful transfer requires an artifact reference, artifact digest, and citation reference.

A submitted download key, running job, failed job, cancelled job, expired job, or unknown status is not source bytes and cannot be treated as success.

## Retrieval intent

`retrieval_intent` keeps these questions explicit:

- Why is the retrieval proposed?
- Which candidate claim role could its outputs support later?
- What Kansas geography and time window are in scope?
- Is the requested result a record, checklist, or aggregate?
- Is non-detection inference requested?
- Are absence, public output, or exact-coordinate output requested? Those three remain fixed false in this profile.

The candidate may describe a future internal retrieval. It cannot request or authorize a public result.

## Query snapshot

The query snapshot binds:

- source-appropriate query language and version;
- canonical query text;
- sorted, unique parameters;
- a deterministic query digest; and
- fixed declarations that credentials, notification addresses, and volatile values are excluded.

The validator rejects password/token/secret-like fields, authorization headers, and email-address patterns in query text or parameter values. A query snapshot records the reviewed retrieval predicate, not the credential-bearing request envelope.

## Sampling support

The contract separates three modes:

| Mode | Permitted interpretation |
|---|---|
| `PRESENCE_ONLY` | Individual occurrence records may support later candidate occurrence statements; no zero fill or non-detection inference. |
| `CHECKLIST_EFFORT` | Paired EBD/SED complete-checklist support may enable later effort-aware non-detection analysis; non-detection is not absence. |
| `AGGREGATE_ONLY` | Server-side/source-provided grouped results may support later candidate aggregate statements; no record-level or absence inference. |

Every mode fixes `absence_claim_allowed = false`, preserves the source role, denies specimen equivalence, and states that missing rows and non-detections are not absences.

## Transfer state

The finite state vocabulary is:

```text
PLANNED -> SUBMITTED -> RUNNING -> SUCCEEDED
                     -> FAILED | CANCELLED | UNKNOWN
PLANNED -> SUCCEEDED | FAILED | CANCELLED | UNKNOWN
terminal historical state may later become EXPIRED
```

The state history must be chronological and the top-level state must equal its last entry. `SUCCEEDED` requires bytes, a digest-bound artifact reference, and a citation reference. Failed, cancelled, expired, unknown, submitted, running, and planned states cannot carry artifact bytes or a success claim.

## Deterministic identity

The fixture profile is `kfm-fixture-json-v1`:

1. remove top-level `spec_hash`;
2. serialize UTF-8 JSON with sorted keys, no insignificant whitespace, JSON array order preserved, and finite numbers only;
3. compute SHA-256 and prefix it with `sha256:`.

`query_digest` uses the same local profile over the `query_snapshot` object after removing only `query_digest`.

These profiles support deterministic fixtures and replay. They do not settle a repository-wide canonicalization or hash-policy decision.

## Validator behavior

The no-network validator:

- rejects symbolic links, missing/non-regular/oversized files, duplicate keys, non-finite numbers, malformed JSON, and non-object roots;
- validates the closed Draft 2020-12 shape;
- recomputes `spec_hash` and `query_digest`;
- checks source/product/query/transfer compatibility;
- checks geography and temporal bounds;
- rejects credential, token, authorization, and email leakage;
- enforces source-specific sampling support and non-detection/absence separation;
- enforces ordered finite transfer state and success/failure payload rules;
- rejects RAW/WORK/QUARANTINE references; and
- keeps all rights, sensitivity, evidence, policy, review, promotion, release, publication, and public-use authority false or held.

Findings contain stable codes and JSON pointers only. Candidate values are not echoed.

## Fixture profile

Valid fixtures cover:

- a planned, paired eBird EBD/SED effort-aware retrieval;
- a submitted GBIF predicate download;
- a successful GBIF SQL aggregate download; and
- a failed GBIF predicate job that remains a valid fail-closed process record.

Exact-negative fixtures cover query/spec-hash drift, secret/PII leakage, source-profile mismatch, eBird without SED support, GBIF absence overclaim, success without an artifact, failed transfer with an artifact, unknown status treated as success, invalid transfer history, noncanonical references, internal lifecycle references, and governance overclaim.

Every semantic-negative fixture also contains an undeclared schema canary. This keeps repository-wide schema-invalid fixture polarity and the dedicated semantic-negative lane independently non-vacuous.

## Validation

```bash
python -m unittest discover   --start-directory tests/validators   --pattern 'test_validate_biodiversity_occurrence_retrieval_plan.py'   --verbose

python tools/validators/validate_biodiversity_occurrence_retrieval_plan.py --fixtures
```

A green result proves only the proposed local shape, sanitized-query binding, source-profile compatibility, sampling-support declarations, finite transfer-state consistency, and synthetic fixture polarity.

It does not prove current eBird or GBIF endpoint behavior, access, terms, rights, sensitivity, query correctness, download completeness, source bytes, occurrence truth, evidence closure, policy approval, review, promotion, release, deployment, publication, or public use.

## Rollback

Before merge, close the draft pull request and abandon the feature branch. After an authorized merge, revert the dependency-closed contract/schema/fixture/validator/test/workflow/receipt commit. No connector, source capture, registry record, lifecycle state, release, deployment, cache, or published artifact requires restoration.

<p align="right"><a href="#top">Back to top</a></p>
