<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-scoring-matrix-version
title: ScoringMatrixVersion Contract — Water Planning
type: semantic-contract
version: v0.1
status: draft; PROPOSED; schema-scaffold; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Water Planning domain steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
created: 2026-07-28
updated: 2026-07-30
policy_label: public-with-gates; semantic-contract; water-planning; deferred-epic; PROPOSED
related:
  - ./README.md
  - ./program_version.md
  - ./application.md
  - ./recommendation.md
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json
  - ../../../schemas/contracts/v1/domains/water_planning/README.md
  - ../../../fixtures/domains/water_planning/scoring_matrix_version/
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../tools/validators/_common/jsonschema_runner.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ScoringMatrixVersion Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json)

Defines the identity, program relationship, byte-integrity posture, lineage, and anti-collapse semantics of a versioned water-planning scoring-matrix record.

> [!IMPORTANT]
> This document and its paired schema are `draft` / `PROPOSED` scaffolds. They do not prove that a scoring document exists, that its criteria were legally or administratively effective, that its bytes or digest were verified, that it governed a particular application, that a score or recommendation was produced, or that rights, policy, review, release, or KFM publication requirements were satisfied.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Versioning, digest, and evidence invariants](#versioning-digest-and-evidence-invariants)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Rights, sensitivity, and release](#rights-sensitivity-and-release)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

A `ScoringMatrixVersion` represents one source-attributed version of a scoring matrix or scoring-guidance artifact used to evaluate applications under a referenced `ProgramVersion`. It preserves an identity for the matrix version, records when the matrix is intended to take effect, and can carry byte-digest and predecessor references for historical traceability.

The record is a document-lineage envelope. It does not contain the scoring categories, criteria, weights, thresholds, tie-break rules, reviewer instructions, formulas, or normalized change set. It also does not represent an application-specific evaluation, computed score, rank, eligibility decision, recommendation, award, payment, project, completion, or benefit.

The contract separates:

- matrix identity from a source-facing document title or version label;
- the matrix version from the `ProgramVersion` under which it is intended to operate;
- an intended `effective_date` from enactment, source-publication, retrieval, observation, correction, release, and KFM publication times;
- a digest-shaped value from the exact bytes, digest scope, recomputation result, source authority, and evidence closure;
- a `supersedes_ref` string from proof of predecessor existence, direct succession, chronology, and acyclic lineage;
- a source pointer from field-level evidence, rights, source admission, correction state, and release authority; and
- the scoring artifact from any application-specific use or outcome.

A material scoring change should be represented as a new matrix-version record rather than an in-place rewrite of the prior identity. That semantic rule still requires an authorized definition of materiality, a resolved source document, and correction-aware lineage.

The paired JSON Schema defines accepted machine shape. This contract defines how accepted fields must and must not be interpreted. Source admission, document retrieval, digest recomputation, reference resolution, evidence closure, policy, review, correction, release, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
|---|---|---|
| This document | `draft`; `PROPOSED`; v0.1 | Defines `ScoringMatrixVersion` meaning, lineage intent, digest posture, and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable field shape; it does not retrieve documents, recompute digests, resolve references, or establish applicability. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/scoring_matrix_version/) | Synthetic test inputs | Exercise one accepted shape and one malformed-digest rejection; they are not scoring-document or program evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check representative fixture polarity, entity-title separation, and the distinction between program-version and scoring-matrix schemas. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Public source-family documentation; historical scoring-matrix availability remains `NEEDS VERIFICATION` | Records a proposed modeling rule and source boundaries without pinning a scoring document, activating a connector, or authorizing release. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; implementation is not established by this contract | No allow, deny, hold, review, public-safe, release, or publication outcome may be inferred here. |
| [Schema validation workflow](../../../.github/workflows/schema-validation.yml) | Read-only pull-request and `main` validation | Produces bounded shape/test evidence only; it does not create document, source, policy, review, release, or publication authority. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, `fixtures/` and `tests/` own reusable synthetic inputs and executable conformance, and `policy/` and `release/` own their respective decisions. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority surface.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
|---|---:|---|---|
| `matrix_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Identity for this matrix-version record. Issuance, namespace ownership, uniqueness, deduplication, aliasing, and correction behavior are not encoded. |
| `program_version_ref` | Yes | Non-empty string | Intended reference to the governing `ProgramVersion`. The schema does not resolve the target, enforce object type, or prove program/matrix applicability. |
| `document_title` | No | String or `null`; no minimum length | Source-facing title when known. Omission, `null`, and an empty string are shape-admissible but do not have fully defined distinct meanings. |
| `document_version` | No | String or `null`; no minimum length | Source-facing version label when known. It is not matrix identity, byte identity, or proof of chronological order. |
| `effective_date` | Yes | String annotated as `date` | Intended applicability date for this matrix version. The currently shared validator does not install a format checker, so date syntax is not enforced by the inspected path. |
| `digest` | Yes | String matching `^sha256:[a-f0-9]{64}$`, or `null` | Intended SHA-256 digest of exact scoring-document bytes. String shape is checked; bytes, algorithm execution, digest scope, and source relationship are not. |
| `supersedes_ref` | Yes | String or `null`; no minimum length | Intended reference to the prior `ScoringMatrixVersion`, or `null`. The schema also admits an empty string and does not resolve lineage, chronology, or cycles. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not by itself an `EvidenceRef`, `EvidenceBundle`, source-admission decision, receipt, proof, rights decision, or release authorization. |

All eight properties are declared by the current schema, six are required, and unknown properties are rejected with `additionalProperties: false`.

[Back to top](#top)

## Versioning, digest, and evidence invariants

Interpret a `ScoringMatrixVersion` append-history-first and fail closed:

- create a new `matrix_id` for a materially changed scoring artifact; do not silently replace the prior matrix-version record;
- do not infer materiality from a new filename, title, fiscal-year label, upload time, or URL alone;
- resolve `program_version_ref` to the intended object, version, and lineage before relying on the relationship;
- do not assume that a program change automatically created a new matrix or that a matrix change altered the entire program;
- keep `effective_date` separate from source publication, retrieval, observation, correction, supersession, release, and KFM publication times;
- treat `document_title` and `document_version` as source-facing metadata, not deterministic identity or proof that particular bytes were retrieved;
- compute `digest` only from identified immutable bytes with a declared scope and algorithm; never infer it from a title, URL, rendered preview, or metadata record;
- treat `digest: null` as unresolved document integrity, not as evidence that no official document exists;
- never represent an all-zero or other synthetic digest as the checksum of an official document;
- treat a digest match as byte-integrity evidence for the declared bytes only, not as proof of source authority, completeness, legal effect, semantic correctness, rights, policy approval, or release;
- resolve `supersedes_ref` before claiming direct succession, preserve the prior identity, and prevent self-reference, cycles, and chronology inversion in a governed lineage check;
- distinguish `supersedes_ref: null`, field omission, and an empty string semantically even though the current shape admits unresolved combinations;
- retain criteria, weights, thresholds, formulas, and reviewer instructions in the authoritative scoring artifact or a separately governed normalized rule model; do not invent them from this envelope;
- resolve `source_ref` through source, evidence, rights, sensitivity, correction, and review surfaces before making consequential claims; and
- represent a correction or withdrawal through governed lineage rather than rewriting a relied-on matrix record or digest.

> [!WARNING]
> The checked-in valid fixture contains `sha256:` followed by 64 zeroes. That value satisfies the schema pattern but is synthetic test data, not a recomputed digest for an official scoring document. The schema does not recognize placeholder digests or verify that referenced bytes exist.

The schema description says `digest` should be `null` only when no official document has been retrieved. The current machine shape does not condition digest nullability on document retrieval, title, version, source, or any other field. Do not describe that prose rule as machine-enforced.

[Back to top](#top)

## Anti-collapse boundaries

| Boundary | Required interpretation |
|---|---|
| Program version != scoring matrix version | [`ProgramVersion`](./program_version.md) owns program-definition lineage; this record owns scoring-artifact lineage. One does not prove or replace the other. |
| Matrix-version envelope != document bytes | Metadata and a digest-shaped value do not contain or resolve the scoring artifact. |
| Document title or label != matrix identity | Titles and version strings may repeat, drift, or be absent; `matrix_id` remains a separate identity claim. |
| Scoring matrix != scoring execution | Criteria or guidance do not prove that any application was evaluated, who evaluated it, or which version was used. |
| Scoring matrix != score or rank | A matrix version contains no application-specific score, rank, reviewer judgment, or adjudication result. |
| Scoring matrix != application | [`Application`](./application.md) owns a submitted request; a scoring artifact does not prove that an application exists or is complete. |
| Scoring matrix != eligibility decision | Eligibility requires a separate application-specific determination and evidence. |
| Scoring matrix != recommendation | [`Recommendation`](./recommendation.md) owns an advisory or administrative recommendation; criteria alone do not recommend an applicant or amount. |
| Scoring matrix != award or payment | A scoring artifact creates no formal award, agreement, disbursement, expenditure, project, completion, or public benefit. |
| Effective date != publication or retrieval time | A date-shaped value does not prove when source bytes were published, observed, retrieved, corrected, or released. |
| Supersession != correction or withdrawal | Matrix succession preserves version history; [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) owns explicit correction or withdrawal lineage. |
| Digest != evidence closure | A valid digest string identifies bytes only after the bytes and digest scope are resolved; it is not source, rights, policy, review, or release proof. |
| Reference != resolved relationship | A shape-valid string does not prove target existence, type, version, chronology, or compatibility. |
| Schema-valid != true or public-safe | Structural acceptance does not establish real-world correctness, applicability, admissibility, release, or KFM publication. |

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
|---|---|---|
| Canonical machine-shape file | [`scoring_matrix_version.schema.json`](../../../schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Properties | 8 | The shape is a document-lineage envelope, not a scoring-rule or application-evaluation model. |
| Required fields | 6 of 8 | `document_title` and `document_version` may be absent; both also admit `null` and empty strings. |
| Unknown fields | Rejected by `additionalProperties: false` | Adding criteria, weights, score, rank, evidence, correction, status, or policy fields requires coordinated review. |
| In-record discriminator | None | Shape recognition depends on the selected schema; the record carries no constant `record_type` or `event_type`. |
| Identity constraint | Lowercase-leading pattern only | Uniqueness, namespace ownership, aliases, and deduplication are not enforced. |
| Program relationship | Required non-empty string | Target existence, object type, lineage, and effective compatibility are not resolved. |
| Document metadata | Optional string-or-null fields | Blank strings are admitted; title/version coherence and source-native meaning are not checked. |
| Digest constraint | Required `sha256:` string shape or `null` | Bytes are not retrieved, digest scope is not declared, and the digest is not recomputed. |
| Lineage constraint | Required string-or-null field | Empty strings are admitted; predecessor resolution, direct succession, cycle detection, and chronology are not enforced. |
| Date assertion | `format: date` annotation | The inspected shared validator supplies no explicit format checker, so syntax enforcement remains `NEEDS VERIFICATION`. |
| Cross-field behavior | No conditional or referential rules | Program, document, date, digest, predecessor, and source fields are not checked for coherence. |
| Matrix content | Not encoded | Categories, criteria, weights, thresholds, formulas, instructions, and change sets cannot be recovered from this record. |
| Evidence and release closure | Not encoded | Schema conformance does not establish source evidence, rights, policy, review, release, or publication. |

The contract and schema must remain synchronized: prose cannot silently loosen or tighten machine behavior.

[Back to top](#top)

## Synthetic example

The checked-in valid fixture is synthetic and test-only. Its source-shaped values must not be cited as independent evidence that the named matrix exists, governed FY2027 scoring, took effect on the stated date, superseded the referenced record, or has the displayed digest.

```json
{
  "matrix_id": "kwo-swigp-fy2027-scoring-v1",
  "program_version_ref": "kwo-swigp-fy2027-hb2462",
  "document_title": "FY2027 SWIGP Scoring Matrix",
  "document_version": "v1",
  "effective_date": "2026-07-01",
  "digest": "sha256:0000000000000000000000000000000000000000000000000000000000000000",
  "supersedes_ref": "kwo-swigp-fy2026-scoring-v1",
  "source_ref": "kwo:grant-programs:swigp:fy2027:scoring"
}
```

The paired invalid fixture uses `digest: "not-a-valid-digest"` and is rejected by the SHA-256 string pattern. Its omitted `document_title` and `document_version` and its `supersedes_ref: null` are schema-admissible. The fixture does not test missing required digest, digest-to-byte mismatch, a placeholder digest, an empty predecessor, malformed date syntax, unresolved program/source references, chronology, or lineage cycles.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Run the focused scoring-matrix checks

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py -k scoring_matrix
```

### Validate the complete water-planning entity schema family

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

| Validation surface | What it checks | What success does not prove |
|---|---|---|
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct entity titles, representative valid/invalid fixture polarity, and program/scoring-matrix field separation | Source truth, date syntax, document retrieval, digest recomputation, reference resolution, matrix applicability, rights, policy, or release |
| [`valid_1.json`](../../../fixtures/domains/water_planning/scoring_matrix_version/valid/valid_1.json) | One synthetic eight-field shape, including a pattern-valid all-zero digest and non-null predecessor | That any official matrix bytes, program version, prior matrix, effective date, or source record exists |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/scoring_matrix_version/invalid/invalid_1.json) | Rejection of one malformed digest string | Rejection of placeholder digests, missing bytes, malformed dates, empty predecessors, unresolved references, chronology errors, or unsupported scoring claims |
| [`jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) | Draft 2020-12 validation using the repository registry | Date format checking, digest recomputation, referential integrity, evidence resolution, or policy |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only schema inventory, meta-schema, configured fixture, and repository-owned schema/contract tests | Semantic truth, source admission, rights or sensitivity clearance, release, deployment, or publication |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | This contract path triggers read-only water-planning domain tests and RAC-registry validation | Validation of the scoring-matrix schema fixture pair; that workflow does not invoke the schema pytest suite |

> [!NOTE]
> A green test or workflow result is evidence only for the tested revision and boundary. It is not a scoring document, digest receipt, `EvidenceBundle`, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Rights, sensitivity, and release

- Do not place scoring-document bytes, authenticated portal content, applications, applicant identities, application-specific scores, rankings, reviewer notes, deliberative material, credentials, or restricted infrastructure details in this semantic-contract lane.
- Public KWO pages and scoring documents remain subject to authoritative document selection, rights, attribution, freshness, correction, and field-level evidence review.
- The source catalog excludes grant scores, review notes, adjudication records, and application content that have not been released as official public records.
- A public title, URL, version label, or digest-shaped value does not authorize copying restricted content or exposing linked application records.
- Scoring-matrix facts intended for public use require source identity, exact byte resolution, digest verification, rights and sensitivity closure, policy, validation, review, correction, release, and rollback decisions from their owning surfaces.
- Public clients and ordinary UI, map, search, graph, export, and AI surfaces may consume only governed, release-approved public-safe carriers, not this contract lane or internal canonical stores directly.

A commit, pull request, merge, badge, schema pass, fixture pass, or matrix-shaped record is not a KFM promotion or publication event.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
|---|---|---|
| `WP-SMV-01` | `NEEDS VERIFICATION` | Define `matrix_id` issuance, namespace ownership, uniqueness, deduplication, aliasing, amendment, and correction behavior. |
| `WP-SMV-02` | `NEEDS VERIFICATION` | Resolve `program_version_ref` to the intended object and lineage; define compatibility when program and matrix effective dates or histories diverge. |
| `WP-SMV-03` | `NEEDS VERIFICATION` | Define material scoring-change triggers and who may decide that a new matrix version is required. |
| `WP-SMV-04` | `NEEDS VERIFICATION` | Locate authoritative historical and current scoring matrices, define title/version identity, and record source publication, retrieval, observation, and correction times. |
| `WP-SMV-05` | `NEEDS VERIFICATION` | Define exact byte selection, media type, digest scope, recomputation evidence, placeholder rejection, and `null` behavior. |
| `WP-SMV-06` | `NEEDS VERIFICATION` | Define `effective_date` semantics, interval or end-date needs, format enforcement, and applicability to application windows or individual applications. |
| `WP-SMV-07` | `NEEDS VERIFICATION` | Resolve `supersedes_ref`, distinguish first/unknown/unresolved predecessor states, and prevent self-reference, cycles, chronology inversion, and silent overwrite. |
| `WP-SMV-08` | `NEEDS VERIFICATION` | Decide whether categories, criteria, weights, thresholds, formulas, reviewer instructions, and version diffs remain document-only or require a separately governed normalized rule family. |
| `WP-SMV-09` | `NEEDS VERIFICATION` | Define how `source_ref` and document identity resolve to field-level support and how consequential claims resolve through `EvidenceRef` to `EvidenceBundle`. |
| `WP-SMV-10` | `NEEDS VERIFICATION` | Add targeted negative tests for missing/placeholder/mismatched digests, blank metadata and predecessors, malformed dates, unresolved references, program mismatch, and lineage failures. |
| `WP-SMV-11` | `NEEDS VERIFICATION` | Complete source-specific rights, sensitivity, deliberative-record, applicant-exposure, and public-safe release review before public reliance. |

Until these items close, preserve unresolved values, narrow claims, and do not infer scoring criteria, weight, threshold, applicability, evaluation, score, rank, eligibility, recommendation, award, payment, project state, benefit, or public eligibility from a `ScoringMatrixVersion` record.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- field names, requiredness, patterns, nullability, formats, or `additionalProperties`;
- matrix identity, material-change triggers, document title/version semantics, or program-version relationship;
- effective-date, applicability-interval, source-publication, retrieval, observation, correction, and release-time semantics;
- digest algorithm, syntax, byte scope, placeholder handling, nullability, recomputation, or evidence behavior;
- predecessor identity, first-version semantics, chronology, cycle handling, correction, or supersession;
- any normalized criteria, weights, thresholds, formulas, instructions, score, rank, or evaluation relationship; and
- source, evidence, rights, sensitivity, policy, public-safe projection, correction, release, or publication behavior.

Preserve `doc_id: kfm://doc/contracts-domains-water-planning-scoring-matrix-version`, the v0.1 identity, and existing property names while this contract remains in force. Because `additionalProperties: false` rejects unknown fields, an additive machine-shape change requires coordinated contract, schema, fixture, test, and consumer review.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, targeted tests, known consumers, and correction lineage within one authorized review boundary. Do not silently rewrite a relied-on matrix history record, replace a digest without lineage, or repurpose a `ProgramVersion`, score, recommendation, or award as the matrix record.

This documentation revision clarifies the existing v0.1 shape and tested boundaries. It does not change schema fields, fixture bytes, validator behavior, source admission, policy, release state, or publication state.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository documentation bytes; it does not erase a source document, external scoring rule, application evaluation, downstream reliance, release state, or publication history.

[Back to top](#top)

## Related

| Surface | Role |
|---|---|
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`program_version.md`](./program_version.md) | Separate program-definition identity and lineage. |
| [`application.md`](./application.md) | Separate submitted-request record and requested-amount semantics. |
| [`recommendation.md`](./recommendation.md) | Separate advisory recommendation and recommended-amount semantics. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | Separate correction and withdrawal lineage envelope. |
| [`scoring_matrix_version.schema.json`](../../../schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json) | Canonical machine shape for this proposed record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic scoring-matrix fixtures](../../../fixtures/domains/water_planning/scoring_matrix_version/) | Representative valid and invalid schema inputs. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family and program/scoring-matrix separation regression tests. |
| [`jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) | Shared Draft 2020-12 validator construction used by the schema tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, proposed modeling rule, rights posture, exclusions, and historical-matrix verification item. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only pull-request schema and contract validation workflow. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only, path-triggered water-planning validation workflow. |

[Back to top](#top)
