<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-construction-milestone
title: ConstructionMilestone Contract — Water Planning
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
  - ./project.md
  - ./completion.md
  - ./award.md
  - ./funding_agreement.md
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json
  - ../../../fixtures/domains/water_planning/construction_milestone/
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../tools/validators/_common/jsonschema_runner.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ConstructionMilestone Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json)

Defines the semantic meaning, time posture, and anti-collapse boundaries of a project-linked water-infrastructure construction milestone.

> [!IMPORTANT]
> This document and its paired schema are `PROPOSED` scaffolds. They do not prove that a project exists, construction began, a milestone was achieved, work was inspected or accepted, a project was completed, an operational benefit occurred, or a record is approved for KFM publication.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Milestone, time, and evidence invariants](#milestone-time-and-evidence-invariants)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

A `ConstructionMilestone` represents one source-attributed checkpoint associated with a [`Project`](./project.md). The record separates:

- milestone-record identity from project identity;
- the project reference from proof that the referenced project exists;
- a source-stated milestone type from a governed milestone vocabulary or status;
- the time a milestone was reportedly achieved from source publication, retrieval, verification, correction, and release times; and
- a source pointer from field-level evidence, review, policy, release, and publication authority.

The paired schema admits a non-empty, free-text `milestone_type`. Its examples include `groundbreaking`, `substantial_completion`, and `inspection`, but those examples are not an enum, a controlled vocabulary, or proof that the named activity occurred.

The schema also permits `achieved_at` to be omitted, set to `null`, or set to a date-time-shaped string. Its description assigns `null` the meaning “not yet achieved.” The meaning of an omitted field is not defined. Until that distinction is governed, absence must remain unresolved and must not be silently treated as achieved, not achieved, planned, cancelled, or complete.

This contract defines record meaning. The paired JSON Schema defines accepted document shape. Source admission, project-reference resolution, field-level evidence, rights and sensitivity review, policy decisions, correction, release, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
| --- | --- | --- |
| This document | `draft`; `PROPOSED`; v0.1 | Defines semantic meaning, time posture, and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not source truth, project resolution, policy, or release. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/construction_milestone/) | Synthetic test inputs | Exercise representative schema acceptance and rejection; they are not project or construction evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check schema presence, distinct entity titles, and representative valid/invalid fixture polarity. |
| [Shared schema runner](../../../tools/validators/_common/jsonschema_runner.py) | Draft 2020-12 structural validator | Loads local schemas and reports structural errors; it does not resolve source evidence or enable an explicit format checker. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Excludes authenticated portal content and unsupported construction or benefit inference; it does not activate a connector or authorize release. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; policy behavior remains `NEEDS VERIFICATION` | No policy outcome may be inferred from this contract or schema. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
| --- | ---: | --- | --- |
| `milestone_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Milestone-record identity. Generation, deduplication, versioning, and correction-lineage rules remain unspecified. |
| `project_ref` | Yes | Non-empty string | Reference-shaped relationship to a `Project`; the schema does not establish referential integrity, project existence, or the correct project version. |
| `milestone_type` | Yes | Non-empty string | Type as stated by the source. No enum, normalization profile, vocabulary version, or crosswalk is encoded. |
| `achieved_at` | No | Draft 2020-12 `date-time` string or `null` | Reported achievement time when present; `null` is described as not yet achieved. Omission semantics, source timezone, and precision are not encoded. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not, by itself, an `EvidenceBundle`, receipt, proof, review, or release authorization. |

No additional properties are admitted by the current schema.

[Back to top](#top)

## Milestone, time, and evidence invariants

The semantic posture is fail closed:

- a milestone record must not be created merely because an award, agreement, project, schedule, invoice, photograph, inspection reference, or completion record exists;
- `project_ref` must remain a reference until the intended project record and version resolve through a governed identity surface;
- `milestone_type` preserves source-stated meaning and must not be silently normalized into a completion, approval, inspection result, payment, or benefit state;
- `achieved_at: null` asserts no achieved instant under the paired schema description; an omitted `achieved_at` remains semantically unresolved;
- a non-null `achieved_at` records a reported time but does not independently prove achievement, acceptance, completion, source freshness, or publication;
- source publication, retrieval, verification, correction, supersession, and release times remain distinct from `achieved_at`, even though this schema does not carry those provenance times; and
- `source_ref` must remain a pointer whose field-level support, rights, sensitivity, freshness, and correction posture are resolved through their owning governance surfaces.

> [!WARNING]
> The paired schema neither controls `milestone_type` nor enforces project referential integrity, evidence resolution, or achievement-state coherence. The shared runner also constructs `Draft202012Validator` without an explicit format checker. These behaviors must not be described as machine-enforced until schemas, fixtures, validators, and tests prove them.

Real project schedules, contractor records, inspection documents, photographs, payment materials, authenticated portal content, and precise infrastructure details require independent access, rights, sensitivity, security, evidence, and release decisions. A `public-with-gates` label is not public-release authorization.

[Back to top](#top)

## Anti-collapse boundaries

A construction milestone is not a project, award, payment, completion, inspection approval, or operational-benefit claim. Each related record requires its own identity, source support, evidence, and governed state.

| Boundary | Required interpretation |
| --- | --- |
| Milestone != project | [`Project`](./project.md) owns award-linked project identity and resolution; a milestone does not create or validate that project. |
| Milestone != award | [`Award`](./award.md) records a formal funding decision; an award does not prove construction activity or a milestone. |
| Milestone != payment | [`FundingAgreement`](./funding_agreement.md) owns agreement and paid-amount meaning; payment does not prove physical progress. |
| Milestone != completion | [`Completion`](./completion.md) carries explicit completion state. Even a source-stated `milestone_type` such as `substantial_completion` does not become a `Completion` record by label alone. |
| Milestone != inspection result | A type such as `inspection` identifies a source-stated checkpoint; it does not encode pass, fail, acceptance, deficiency, or approval. |
| Milestone != operational benefit | Construction activity does not prove service, impact, effectiveness, safety, capacity, or public benefit. |
| Milestone type != governed status | A non-empty free-text type is not a controlled state machine, normalized taxonomy, or promotion decision. |
| Achievement time != evidence closure | A date-time-shaped value does not prove the event occurred or that its source is authoritative, current, and rights-cleared. |
| Source reference != evidence closure | A non-empty `source_ref` does not establish field-level support, integrity, review, policy, release, or publication. |
| Schema-valid != true or public-safe | Structural acceptance does not establish real-world correctness, source admission, sensitivity clearance, release, or KFM publication. |

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
| --- | --- | --- |
| Canonical machine-shape file | [`construction_milestone.schema.json`](../../../schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Required fields | 4 of 5 properties | `achieved_at` may be absent; all other defined fields are required. |
| Unknown fields | Rejected by `additionalProperties: false` | Widening the record requires coordinated contract, schema, fixture, and test review. |
| Milestone vocabulary | Non-empty free text | Spelling variants, source vocabularies, normalization, and crosswalk semantics are not governed by this shape. |
| Project linkage | Non-empty string only | Project existence, version, lifecycle state, and referential integrity are not checked. |
| Achievement state | No explicit status field or conditional rules | Null, omission, and non-null time do not form a machine-enforced milestone state model. |
| Date-time assertion | `format: date-time` on `achieved_at` | The shared runner does not install an explicit format checker, so syntax enforcement remains `NEEDS VERIFICATION`. |

The contract and schema must remain synchronized: prose cannot loosen or tighten machine behavior without a coordinated schema change.

[Back to top](#top)

## Synthetic example

The checked-in valid fixture is synthetic and test-only. It must not be cited as evidence that a project, groundbreaking, construction activity, or milestone exists.

```json
{
  "milestone_id": "kwo-swigp-fy2027-ms-synthetic-001",
  "project_ref": "kwo-swigp-fy2027-proj-synthetic-001",
  "milestone_type": "groundbreaking",
  "achieved_at": null,
  "source_ref": "kwo:grant-programs:swigp:fy2027:milestone:synthetic-001"
}
```

The `null` time means the fixture does not assert an achieved instant. The paired invalid fixture omits `milestone_id`; the schema test expects that record to be rejected because the identity field is required.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Validate the water-planning entity schemas and fixture families

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

| Validation surface | What it checks | What success does not prove |
| --- | --- | --- |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | All 15 entity schema files, distinct titles, and one representative valid/invalid fixture pair per entity | Milestone vocabulary, project referential integrity, achieved-time syntax, source truth, rights, policy, or release |
| [`valid_1.json`](../../../fixtures/domains/water_planning/construction_milestone/valid/valid_1.json) | One synthetic shape with a required identity, project reference, source-stated type, null achievement time, and source reference | That a project or milestone exists, is current, or is source-supported |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/construction_milestone/invalid/invalid_1.json) | Rejection of one record missing `milestone_id` | Exhaustive negative coverage for empty references, type vocabulary, time, evidence, or cross-entity collapse |
| [`jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) | Local Draft 2020-12 structural validation and deterministic valid/invalid polarity | Date-time format enforcement, reference resolution, semantic truth, or policy |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Pull-request schema inventory, meta-schema checks, configured aggregate fixtures, and repository-owned schema/contract tests under read-only permissions | Milestone evidence, source admission, rights, sensitivity, policy, release, or publication |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Path-triggered no-network water-planning semantic and RAC-registry checks under `contents: read` | Milestone-schema exhaustiveness, project progress, review approval, evidence closure, release, deployment, or publication |

> [!NOTE]
> A green test or workflow result is validation evidence only within the tested boundary. It is not a construction receipt, inspection result, EvidenceBundle, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
| --- | --- | --- |
| `WP-CM-01` | `NEEDS VERIFICATION` | Define `milestone_id` generation, deduplication, versioning, and identity preservation across source corrections. |
| `WP-CM-02` | `NEEDS VERIFICATION` | Add or identify deterministic referential-integrity validation from `project_ref` to the intended governed `Project` record and version. |
| `WP-CM-03` | `NEEDS VERIFICATION` | Define source-vocabulary preservation, normalization, and versioned crosswalk rules for `milestone_type`. |
| `WP-CM-04` | `NEEDS VERIFICATION` | Prevent terms such as `substantial_completion` and `inspection` from being reinterpreted as completion state or inspection approval without separate records and evidence. |
| `WP-CM-05` | `NEEDS VERIFICATION` | Define distinct semantics for omitted, null, and non-null `achieved_at`, including planned, delayed, cancelled, corrected, and achieved states. |
| `WP-CM-06` | `NEEDS VERIFICATION` | Decide whether date-time annotations require an explicit format checker and how source timezone, precision, and uncertainty are retained. |
| `WP-CM-07` | `NEEDS VERIFICATION` | Define how `source_ref` resolves to field-level evidence and how source publication, retrieval, correction, and supersession times are retained. |
| `WP-CM-08` | `NEEDS VERIFICATION` | Add representative negative tests for empty references, malformed achievement time, status/type collapse, unresolvable project references, and unsupported achievement claims. |
| `WP-CM-09` | `NEEDS VERIFICATION` | Establish finite policy outcomes and public-safe projection rules for construction records, inspections, photographs, schedules, portal content, and precise infrastructure details. |

Until these items are resolved, narrow claims and do not infer project existence, physical progress, milestone achievement, inspection approval, completion, payment, benefit, or public eligibility.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- field names, requiredness, patterns, nullable behavior, `format`, or `additionalProperties`;
- milestone, project-reference, type-vocabulary, achievement-time, and source-reference semantics;
- the distinction between omitted, null, and non-null achievement time;
- project referential integrity, identity, deduplication, correction, withdrawal, and supersession behavior; and
- any public-safe projection or policy outcome.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, tests, known consumers, and correction lineage within one authorized review boundary. Use [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) or another governed correction surface when applicable; do not silently rewrite a relied-on historical milestone.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository bytes; it does not erase source history, project activity, downstream reliance, or publication state.

[Back to top](#top)

## Related

| Surface | Role |
| --- | --- |
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`project.md`](./project.md) | Referenced project identity, recipient, RAC-membership, and location-resolution semantics. |
| [`award.md`](./award.md) | Separate formal funding-decision and awarded-amount meaning. |
| [`funding_agreement.md`](./funding_agreement.md) | Separate agreement and paid-amount meaning. |
| [`completion.md`](./completion.md) | Separate explicit completion-state contract. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | Domain correction and withdrawal event contract. |
| [`construction_milestone.schema.json`](../../../schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json) | Canonical machine shape for this record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic construction-milestone fixtures](../../../fixtures/domains/water_planning/construction_milestone/) | Representative valid and invalid inputs. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family regression tests. |
| [`jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) | Shared local Draft 2020-12 validator construction. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, access, rights, freshness, and inference limitations. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only schema and contract validation workflow. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only water-planning boundary workflow. |

[Back to top](#top)
