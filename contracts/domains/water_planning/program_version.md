<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-program-version
title: ProgramVersion Contract — Water Planning
type: semantic-contract
version: v0.2
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
  - ./scoring_matrix_version.md
  - ./application_window.md
  - ./application.md
  - ./eligibility_decision.md
  - ./award.md
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/program_version.schema.json
  - ../../../schemas/contracts/v1/domains/water_planning/README.md
  - ../../../fixtures/domains/water_planning/program_version/
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../tools/validators/_common/jsonschema_runner.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ProgramVersion Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/program_version.schema.json)
[![Schema validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/schema-validation.yml/badge.svg?branch=main)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/schema-validation.yml)

Defines the identity, lineage, source-document, and anti-overwrite semantics of a versioned Kansas water-planning program record.

> [!IMPORTANT]
> This document and its paired schema are `draft` / `PROPOSED` scaffolds. They do not independently prove that a statute or policy changed, establish the change's effective date or scope, encode the changed eligibility or scoring rules, resolve a prior version or source, clear rights or sensitivity, approve policy, authorize release, or make any record KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Versioning, lineage, and evidence invariants](#versioning-lineage-and-evidence-invariants)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Rights, sensitivity, and release](#rights-sensitivity-and-release)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

A `ProgramVersion` represents one source-attributed version of a water-planning program definition. It gives a version its own identity and preserves an explicit link to the immediately prior version when one is known. A statutory, policy, or administrative change that materially changes tracked program meaning should create a new record instead of rewriting the record previously used for that program.

The contract separates:

- a version identity from a program name or fiscal-year label;
- a statutory or policy citation from proof of enactment, applicability, or effective date;
- a required `effective_date` value from source-publication, retrieval, correction, release, and publication times;
- a `supersedes_ref` string from proof that the referenced version exists, precedes the new version, or forms a valid lineage chain;
- a governing-document title and digest from the document bytes, rights posture, review state, and policy effect;
- a source pointer from field-level evidence, provenance, source admission, and release authority; and
- program-definition lineage from scoring-matrix, application-window, application, decision, award, project, and outcome records.

The current machine shape records the version envelope. It does **not** encode the eligibility criteria, scoring categories, administrative rules, funding terms, or a machine-readable diff between versions. Those details require governed document evidence and, where KFM later models them, separately reviewed contracts and schemas.

The paired JSON Schema defines accepted document shape. This semantic contract defines how accepted fields must and must not be interpreted. Source admission, reference resolution, evidence closure, policy, review, release, correction, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
|---|---|---|
| This document | `draft`; `PROPOSED`; v0.2 | Defines semantic meaning, lineage intent, and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/program_version.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable field shape. It does not verify source facts, resolve references, or decide when a change requires a new version. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/program_version/) | Synthetic test inputs | Exercise representative schema and lineage expectations; they are not program, statute, policy, or document authority. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check fixture polarity, one HB 2462-shaped synthetic lineage case, schema-title separation, and the program/scoring-matrix distinction. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source-grounded candidate; rights and selected facts remain `NEEDS VERIFICATION` | Records the public source family and proposed modeling rule without activating a connector or authorizing release. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; implementation is not established | No policy outcome, public-safe projection, or release decision may be inferred from this contract or schema. |
| [Schema validation workflow](../../../.github/workflows/schema-validation.yml) | Read-only pull-request and `main` validation | Produces bounded test evidence only; it does not create source, policy, review, release, or publication authority. |

Directory placement follows the accepted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, `tests/` and `fixtures/` own executable examples and checks, and `policy/` and `release/` own their respective decisions. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority surface.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
|---|---:|---|---|
| `version_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Stable identity for this program-version record. Issuance, uniqueness, deduplication, aliasing, and correction behavior are not encoded. |
| `program_name` | Yes | Non-empty string | Source-attributed program name. Shape validity does not verify that the value is official, current, or uniquely identifying. |
| `statutory_basis` | No | String or `null` | Statutory or policy basis when available. The schema description says it is required when legislation drives the change, but the current machine shape does not enforce that condition. |
| `fiscal_year` | Yes | String matching `^FY[0-9]{4}$` | Source-facing fiscal-year label. It does not establish a calendar interval, appropriation, application window, program state, or release version by itself. |
| `effective_date` | Yes | String annotated as `date` | Intended program-version effective date. The current shared validator does not install a format checker, so date syntax is not machine-enforced by the inspected test path. |
| `supersedes_ref` | Yes | String or `null` | Reference to the prior `ProgramVersion`, or `null` for a first version. The schema does not resolve the target, prevent cycles, require chronology, or condition nullability on version history. |
| `document_title` | No | String or `null` | Title of a governing program document when known. A title is not document identity, byte provenance, or evidence closure. |
| `document_digest` | No | String matching `^sha256:[a-f0-9]{64}$`, or `null` | Content digest when the governing bytes are available and scoped. `null` means no digest is carried; it must not be treated as a verified document. |
| `source_publication_time` | No | String annotated as `date-time`, or `null` | Source-stated publication time when known. It remains distinct from retrieval, effective, correction, review, release, and KFM publication times. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not by itself an `EvidenceRef`, `EvidenceBundle`, source-admission decision, receipt, proof, or release authorization. |

All ten fields are declared by the current schema, six are required, and unknown fields are rejected with `additionalProperties: false`.

[Back to top](#top)

## Versioning, lineage, and evidence invariants

The semantic posture is append-history-first and fail closed:

- a material program-definition change creates a new `version_id`; it does not mutate the prior record in place;
- `supersedes_ref` expresses intended lineage only after the target's identity, type, version, and existence are resolved;
- a non-null reference does not prove chronology, direct succession, source support, or an acyclic lineage;
- `supersedes_ref: null` is reserved semantically for the first known version, but the current schema cannot prove that no predecessor exists;
- a statute or policy citation does not prove enactment, applicability, effective date, program implementation, or the exact content of a change;
- `fiscal_year` is a label, not a substitute for version identity, effective dates, application windows, appropriations, or source-document lineage;
- `effective_date` remains separate from source-publication, retrieval, observation, correction, supersession, release, and KFM publication times;
- `document_title` without a verified digest and source relationship does not pin governing bytes;
- `document_digest: null` preserves the unresolved state and must not be represented as verified document integrity;
- a digest proves byte identity within its declared scope, not source authority, legal effect, semantic correctness, rights, policy approval, or release;
- `source_ref` must remain a pointer whose target, field-level support, freshness, rights, sensitivity, and correction state are resolved through their owning governance surfaces; and
- a `ProgramVersion` does not contain the changed eligibility, scoring, or administrative rules and must not be used as though it did.

> [!WARNING]
> The checked-in synthetic HB 2462 fixture has a non-null `supersedes_ref`, and a test asserts that example. The schema itself still admits `null` for any record and does not encode the rule “legislation-driven version changes must have a predecessor.” Do not describe that rule as machine-enforced.

Real program documents and legislative claims require authoritative source evidence, document identity and digest where available, rights review, field-level support, correction lineage, and a governed release decision before public reliance.

[Back to top](#top)

## Anti-collapse boundaries

| Boundary | Required interpretation |
|---|---|
| Program != program version | A program family may have many historical versions; a name alone does not select one. |
| Program version != statutory authority | A record citing a statute or policy does not prove enactment, legal effect, applicability, or complete scope. |
| Program version != governing document | The version envelope may identify a document, but it is not the document bytes or their evidence. |
| Program version != scoring matrix | [`ScoringMatrixVersion`](./scoring_matrix_version.md) owns scoring-artifact lineage; a new program version does not identify or validate a matrix. |
| Program version != application window | [`ApplicationWindow`](./application_window.md) owns intake timing; a fiscal year or effective date does not establish an open or close time. |
| Program version != application | [`Application`](./application.md) represents a submitted request; program eligibility does not prove that an application exists. |
| Program version != eligibility decision | [`EligibilityDecision`](./eligibility_decision.md) owns a determination for an application; program criteria do not decide a particular case by themselves. |
| Program version != award | [`Award`](./award.md) owns a funding decision; a program version does not establish recipient, amount, payment, project, or benefit facts. |
| Supersession != correction or withdrawal | Version succession preserves program-definition history; [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) owns explicit correction or withdrawal lineage for affected records. |
| Fiscal year != effective interval | A pattern-valid `FYnnnn` label does not prove start, end, appropriation, application-window, or administrative dates. |
| Document digest != evidence closure | A valid digest shape identifies bytes only when actual bytes and digest scope are resolved; it is not proof, policy, review, or release. |
| Source reference != source resolution | A non-empty string does not prove target existence, authority, freshness, rights, or field-level support. |
| Schema-valid != true or public-safe | Structural acceptance does not establish real-world correctness, admissibility, release, or KFM publication. |

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
|---|---|---|
| Canonical machine-shape file | [`program_version.schema.json`](../../../schemas/contracts/v1/domains/water_planning/program_version.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Properties | 10 | The shape is a version and source-document envelope, not a complete program-rule model. |
| Required fields | 6 of 10 | `statutory_basis`, `document_title`, `document_digest`, and `source_publication_time` may be absent; each also admits `null`. |
| Unknown fields | Rejected by `additionalProperties: false` | Adding program-rule, evidence, correction, status, or policy fields requires coordinated review. |
| Identity constraint | Lowercase-leading pattern only | Uniqueness, namespace ownership, aliasing, and deduplication are not enforced. |
| Lineage constraint | Required string-or-null field | Target resolution, direct succession, cycle detection, chronology, and first-version proof are not enforced. |
| Digest constraint | `sha256:` plus 64 lowercase hexadecimal characters, or `null` | The schema checks string shape only; it does not retrieve bytes or recompute the digest. |
| Date/time assertions | `format: date` and `format: date-time` annotations | The inspected shared validator supplies no explicit format checker, so syntax enforcement remains `NEEDS VERIFICATION`. |
| Cross-field behavior | No conditional or referential rules | Statutory basis, predecessor, fiscal year, dates, source, and document fields are not checked for coherence. |
| Evidence and release closure | Not encoded | Schema conformance does not establish evidence, rights, policy, review, release, or publication. |

The contract and schema must remain synchronized: prose cannot silently loosen or tighten machine behavior.

[Back to top](#top)

## Synthetic example

The checked-in valid fixture is synthetic and test-only. Its source-shaped values must not be cited as independent evidence that a statute changed, that the stated date is legally effective, that the prior version exists, or that the named document has been retrieved and verified.

```json
{
  "version_id": "kwo-swigp-fy2027-hb2462",
  "program_name": "State Water Infrastructure Grant Program",
  "statutory_basis": "2026 HB 2462",
  "fiscal_year": "FY2027",
  "effective_date": "2026-07-01",
  "supersedes_ref": "kwo-swigp-fy2026",
  "document_title": "FY2027 State Water Infrastructure Grant Program Guidelines",
  "document_digest": null,
  "source_publication_time": "2026-07-01T00:00:00Z",
  "source_ref": "kwo:grant-programs:swigp:fy2027"
}
```

The paired invalid fixture uses `fiscal_year: "2027"` and is rejected by the `^FY[0-9]{4}$` pattern. Its `supersedes_ref: null` is **not** independently rejected by the schema. A separate test asserts only that the checked-in HB 2462-shaped valid fixture carries a non-null predecessor.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Run the focused program-version checks

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py -k program_version
```

### Validate the complete water-planning entity schema family

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

| Validation surface | What it checks | What success does not prove |
|---|---|---|
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct titles, representative valid/invalid fixture polarity, one synthetic non-null predecessor assertion, and program/scoring-matrix separation | Source truth, statute scope, effective-date syntax, reference resolution, document integrity, rights, policy, or release |
| [`valid_1.json`](../../../fixtures/domains/water_planning/program_version/valid/valid_1.json) | One synthetic shape with all ten declared fields and a non-null predecessor | That HB 2462 has the represented effect, that the date is authoritative, that the predecessor exists, or that document bytes were verified |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/program_version/invalid/invalid_1.json) | Rejection of one malformed fiscal-year label | Rejection of a null predecessor, malformed date, nonexistent reference, incorrect chronology, digest mismatch, or unsupported statutory claim |
| [`jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) | Draft 2020-12 validation using the repository registry | Date/date-time format checking, referential integrity, evidence resolution, or policy |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only pull-request schema inventory, meta-schema, configured fixture, and repository-owned schema/contract tests | Semantic truth, source admission, rights or sensitivity clearance, release, deployment, or publication |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Path-triggered, read-only water-planning semantic and registry checks | Exhaustive `ProgramVersion` validation, source freshness, evidence closure, policy approval, release, or publication |

> [!NOTE]
> A green test or workflow result is evidence only for the tested boundary. It is not a legislative finding, source-admission decision, `EvidenceBundle`, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Rights, sensitivity, and release

- Do not place credentials, authenticated grant-portal content, private applicant or recipient information, review notes, or restricted infrastructure details in this semantic-contract lane.
- Public KWO pages, legislative materials, program guidance, scoring documents, and recipient records remain subject to source identity, rights, attribution, freshness, and correction review.
- A public statute, program page, or document title does not authorize copying authenticated portal content or exposing linked records.
- Program-definition facts intended for public use require field-level evidence and a public-safe projection decision; unresolved or unsupported claims must narrow, abstain, hold, or be denied according to the applicable governed surface.
- Public clients and ordinary UI, map, search, graph, export, and AI surfaces may consume only governed, release-approved public-safe carriers, not this contract lane or internal canonical stores directly.

A commit, pull request, merge, badge, schema pass, fixture pass, or program-shaped record is not a KFM promotion or publication event.

[Back to top](#top)

## Known limits and verification backlog

| Item | Status | Verification needed |
|---|---|---|
| Version identity | `NEEDS VERIFICATION` | Define `version_id` issuance, namespace ownership, uniqueness, deduplication, aliases, and correction behavior. |
| New-version trigger | `NEEDS VERIFICATION` | Define who decides that a statutory, policy, eligibility, scoring, or administrative change is material enough to create a new version and what evidence supports that decision. |
| HB 2462 basis and scope | `NEEDS VERIFICATION` | Verify enactment, effective date, affected program provisions, and source-document lineage from authoritative legislative and KWO materials. |
| Prior-version resolution | `NEEDS VERIFICATION` | Resolve `supersedes_ref`, require the intended object type, prevent self-reference and cycles, and define missing or corrected target behavior. |
| First-version semantics | `NEEDS VERIFICATION` | Decide how `null` is distinguished from an unknown, missing, or not-yet-resolved predecessor. |
| Program rule content | `NEEDS VERIFICATION` | Define whether eligibility, scoring, administration, funding, and other rule content belongs in referenced documents, separate contracts, or a governed normalized rule family. |
| Document identity and integrity | `NEEDS VERIFICATION` | Define authoritative document selection, title/version identity, byte retrieval, digest scope, correction, and supersession. |
| Time semantics and format validation | `NEEDS VERIFICATION` | Distinguish enactment, effective, source-publication, retrieval, observation, correction, and release times; decide whether to enable format checking. |
| Conditional and cross-field rules | `NEEDS VERIFICATION` | Decide whether legislative basis, predecessor, fiscal year, effective date, source, and document fields require machine-enforced coherence. |
| Evidence and source resolution | `NEEDS VERIFICATION` | Define how `source_ref` resolves to field-level support and how consequential claims resolve through `EvidenceRef` to `EvidenceBundle`. |
| Rights, sensitivity, and public projection | `NEEDS VERIFICATION` | Complete source-specific rights review and finite policy outcomes before release-approved public use. |

Until these items are resolved, preserve unresolved values, narrow claims, and do not infer statutory effect, program-rule content, scoring criteria, application eligibility, award authority, payment, project state, operational benefit, or public eligibility from a `ProgramVersion` record.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- field names, requiredness, patterns, nullability, formats, or `additionalProperties`;
- version identity, material-change triggers, predecessor semantics, chronology, or lineage resolution;
- statutory basis, fiscal year, effective date, source-publication time, or source-reference meaning;
- governing-document identity, digest syntax, digest scope, correction, or supersession behavior;
- any modeled program-rule content or relationship to scoring matrices, windows, applications, decisions, awards, projects, or releases; and
- evidence, rights, sensitivity, policy, public-safe projection, correction, or publication behavior.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, targeted tests, known consumers, and correction lineage within an authorized review boundary. Do not silently rewrite or repoint a relied-on program history record.

This v0.2 documentation revision clarifies the existing v0.1 shape and tested boundaries; it does not change schema fields, fixture bytes, validator behavior, source admission, policy, or release state.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository bytes; it does not erase a statute, program history, source observation, downstream reliance, release state, or publication history.

[Back to top](#top)

## Related

| Surface | Role |
|---|---|
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`scoring_matrix_version.md`](./scoring_matrix_version.md) | Separate scoring-artifact identity and digest lineage. |
| [`application_window.md`](./application_window.md) | Separate application-intake interval and source-timezone semantics. |
| [`application.md`](./application.md) | Separate submitted-request record. |
| [`eligibility_decision.md`](./eligibility_decision.md) | Separate application-specific eligibility determination. |
| [`award.md`](./award.md) | Separate funding decision and awarded-amount fact. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | Separate correction and withdrawal lineage envelope. |
| [`program_version.schema.json`](../../../schemas/contracts/v1/domains/water_planning/program_version.schema.json) | Canonical machine shape for this proposed record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic program-version fixtures](../../../fixtures/domains/water_planning/program_version/) | Representative valid and invalid schema inputs. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family regression tests. |
| [`jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) | Shared Draft 2020-12 validator construction used by the tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, proposed modeling rule, rights posture, and open verification items. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only pull-request schema and contract validation workflow. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only, path-triggered water-planning validation workflow. |

[Back to top](#top)
