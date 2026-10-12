<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-correction-or-withdrawal
title: CorrectionOrWithdrawal Contract — Water Planning
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
  - ./application.md
  - ./award.md
  - ./funding_agreement.md
  - ./project.md
  - ./completion.md
  - ../../../schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json
  - ../../../fixtures/domains/water_planning/correction_or_withdrawal/
  - ../../../fixtures/domains/water_planning/status_collapse/
  - ../../../tools/validators/domains/water_planning/validate_status_collapse.py
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../tests/domains/water_planning/test_status_collapse.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# CorrectionOrWithdrawal Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json)

Defines the semantic meaning, temporal posture, and lineage boundaries of a correction or full-withdrawal record for a water-planning entity.

> [!IMPORTANT]
> This document and its paired schema are `PROPOSED` scaffolds. They do not prove that a source issued a correction or withdrawal, mutate or delete the referenced subject, supply a corrected replacement state, create a new award, decision, payment, project, completion, or benefit record, approve policy or promotion, or make any record KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Action and lineage semantics](#action-and-lineage-semantics)
- [Evidence, rights, and downstream use](#evidence-rights-and-downstream-use)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

A `CorrectionOrWithdrawal` is a distinct record about another water-planning entity identified by `subject_ref`. When supported by admitted evidence:

- `action_type: correction` states that the referenced subject requires correction; and
- `action_type: withdrawal` states that the referenced subject is fully withdrawn as of the modeled effective time.

The action record preserves its own identity, reason, effective time, and source pointer separately from the subject. It does not become the subject, silently overwrite prior bytes, or acquire the subject's event type.

The current shape contains no corrected payload, field-level patch, replacement reference, superseding-subject reference, or policy/release decision. A schema-valid action record therefore cannot, by itself, express the corrected successor state, prove that a consumer applied the action, or establish how a withdrawn subject must be treated by a particular interface.

The contract describes record meaning. The paired JSON Schema defines accepted document shape. Subject resolution, digest verification, evidence resolution, correction application, rights and sensitivity review, policy decisions, release correction, retraction, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
|---|---|---|
| This document | `draft`; `PROPOSED`; v0.1 | Defines correction, withdrawal, time, and lineage meaning. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not subject mutation, source truth, policy, or release behavior. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/correction_or_withdrawal/) | Synthetic test inputs | Exercise one accepted correction shape and one rejected action value; they are not source notices or production records. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check schema presence, title separation, and representative valid/invalid polarity for this entity family. |
| [Status-collapse validator](../../../tools/validators/domains/water_planning/validate_status_collapse.py) and [tests](../../../tests/domains/water_planning/test_status_collapse.py) | Deterministic, no-network synthetic-envelope checks | Require a correction-or-withdrawal lineage slot in the cross-entity fixture envelope; they do not validate or resolve this record type. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Records correction and supersession as required provenance concerns; it does not activate a source or prove a specific notice. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; policy behavior remains `NEEDS VERIFICATION` | No suppression, replacement, denial, release, or public-interface outcome may be inferred from this contract or schema. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
|---|---:|---|---|
| `record_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Identity of the action record. Generation, deduplication, chaining, and version-lineage rules remain unspecified. |
| `subject_ref` | Yes | Non-empty string | Reference-shaped pointer to the water-planning entity being corrected or withdrawn. Target existence, type, version, and referential integrity are not encoded. |
| `action_type` | Yes | `correction` or `withdrawal` | Finite action kind. `withdrawal` represents full withdrawal under the current schema description; partial withdrawal is not modeled. |
| `reason` | Yes | Non-empty string | Source-grounded explanation for the action. Accuracy, sufficiency, controlled vocabulary, redaction, and field-level support are not machine-checked. |
| `effective_at` | Yes | String annotated as `date-time` | When the correction or withdrawal is intended to take effect; distinct from source publication, retrieval, record creation, and release times. |
| `prior_digest` | No | String matching `^sha256:[a-f0-9]{64}$`, or `null` | Optional digest-shaped pointer to a prior representation. Canonicalization, digest scope, recomputation, and subject binding are not defined by the schema. |
| `correction_time` | No | String annotated as `date-time`, or `null` | When the source published the correction, if known. Despite the field name, it may accompany either admitted `action_type`. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not, by itself, an `EvidenceRef`, `EvidenceBundle`, receipt, proof, review, policy decision, or release authorization. |

No additional properties are admitted by the current schema.

[Back to top](#top)

## Action and lineage semantics

### Correction

A correction record identifies a prior subject and records that a source-supported change is required. It does not create a new event in the subject's family and does not carry the corrected value. Applying a correction requires a separately governed subject-state, successor, projection, or consumer behavior that preserves the prior state and cites the correction lineage.

### Withdrawal

A withdrawal record represents full withdrawal of the referenced subject. Withdrawal is not physical deletion, Git-history rewriting, evidence destruction, or automatic retraction from every released carrier. Downstream suppression, replacement, retention, notice, and rollback behavior require the applicable policy and release authorities.

### Digest and time lineage

The semantic posture is fail closed:

- when `prior_digest` is present, it must identify the exact declared prior representation under a defined canonicalization and digest scope before it is treated as verified lineage;
- an absent or `null` `prior_digest` means digest binding is unresolved, not implicitly satisfied;
- `effective_at` and `correction_time` remain distinct even when their values happen to be equal;
- a later `correction_time` does not silently rewrite what was known before that publication time;
- a `subject_ref` or `source_ref` string does not prove that the referenced object exists or is authoritative; and
- correction chains must preserve prior records and detect unresolved, conflicting, duplicate, or cyclic lineage before consequential use.

> [!WARNING]
> The paired schema describes `prior_digest` as preserving historical lineage, but the field is optional and nullable. The current machine shape therefore permits a correction or withdrawal with no digest binding. Documentation and consumers must not claim universal digest-preserved lineage until requiredness, canonicalization, verification, and subject binding are implemented and tested.

[Back to top](#top)

## Evidence, rights, and downstream use

- Resolve `subject_ref` to the intended entity and version before applying an action.
- Resolve `source_ref` through the applicable source and evidence authorities before treating the action as a supported fact.
- Verify field-level support for `action_type`, `reason`, `effective_at`, `correction_time`, and any claimed prior digest.
- Keep `reason` minimal and source-grounded; do not copy private applicant material, authenticated portal content, living-person details, restricted infrastructure information, or other sensitive values into a public-facing explanation.
- Preserve the prior subject, observation, evidence, receipt, review, release, and correction lineage according to their own retention rules.
- Re-evaluate released carriers and governed interfaces through their correction, withdrawal, policy, sensitivity, notice, and rollback procedures; this semantic record does not self-authorize those transitions.
- Public clients and ordinary UI, map, export, search, graph, and AI surfaces may consume only governed, release-approved public-safe carriers, not this contract lane or an internal action record directly.

A `public-with-gates` label is not public-release authorization. Withdrawing a subject also does not authorize destruction of audit evidence or concealment of a prior public claim.

[Back to top](#top)

## Anti-collapse boundaries

| Boundary | Required interpretation |
|---|---|
| Correction record != corrected subject | The action record signals a required change but contains no corrected payload or replacement reference. |
| Withdrawal != deletion | Withdrawal changes modeled status or admissibility only through governing policy and release behavior; it does not erase history. |
| Correction or withdrawal != new event | The action does not become an application, eligibility decision, recommendation, award, agreement, project, milestone, completion, payment, or benefit record. |
| Subject reference != referential proof | A non-empty `subject_ref` does not establish target existence, type, version, or identity. |
| Effective time != source-publication time | `effective_at` describes when the action takes effect; `correction_time` describes when the source published it. |
| Prior digest != verified lineage | Digest syntax does not prove canonicalization, recomputation, subject binding, or preservation of the referenced bytes. |
| Source reference != evidence closure | A non-empty `source_ref` does not establish field-level support, rights, sensitivity, freshness, review, or release. |
| Schema-valid != action applied | Structural acceptance does not prove that any canonical record, catalog, API, UI, map, export, AI answer, or published carrier was corrected or withdrawn. |
| Repository change != KFM correction event | Editing this Markdown, merging a pull request, reverting a commit, or passing CI does not create a domain correction, release notice, rollback decision, or publication transition. |

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
|---|---|---|
| Canonical machine-shape file | [`correction_or_withdrawal.schema.json`](../../../schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Properties | 8 | The shape records an action envelope, not corrected replacement state. |
| Required fields | 6 | `prior_digest` and `correction_time` may be absent; each also admits `null`. |
| Unknown fields | Rejected by `additionalProperties: false` | Adding replacement, patch, review, evidence, or release fields requires coordinated contract, schema, fixture, and test review. |
| Action kinds | `correction`, `withdrawal` | Other actions such as `edit`, partial withdrawal, reinstatement, and cancellation are not admitted. |
| Digest syntax | Lowercase `sha256:` plus 64 lowercase hexadecimal characters | Syntax is checked for string values; digest computation and target binding are not. |
| Date-time assertions | `format: date-time` on `effective_at` and `correction_time` | The shared validator constructs `Draft202012Validator` without an explicit format checker, so syntax enforcement remains `NEEDS VERIFICATION`. |
| Cross-field behavior | No conditional or referential rules | The schema does not require a digest, order the two times, constrain target type, resolve references, or distinguish correction-specific from withdrawal-specific fields. |

The contract and schema must remain synchronized: prose cannot loosen or tighten machine behavior without a coordinated schema change.

[Back to top](#top)

## Synthetic example

The checked-in valid fixture is synthetic and test-only. It must not be cited as evidence that an applicant name, application, source notice, correction, or withdrawal exists.

```json
{
  "record_id": "kwo-swigp-fy2027-corr-synthetic-001",
  "subject_ref": "kwo-swigp-fy2027-app-synthetic-001",
  "action_type": "correction",
  "reason": "Applicant name corrected per official KWO notice.",
  "effective_at": "2026-09-20T00:00:00Z",
  "prior_digest": null,
  "correction_time": "2026-09-20T00:00:00Z",
  "source_ref": "kwo:grant-programs:swigp:fy2027:correction:synthetic-001"
}
```

The example deliberately demonstrates a limitation: it states that a name was corrected but carries neither the prior nor corrected name and has `prior_digest: null`. It is an accepted synthetic action-envelope shape, not proof of corrected state or digest-bound lineage.

The paired invalid fixture uses `action_type: edit`; the schema test expects that record to be rejected because `edit` is not an admitted action.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Validate the paired schema and fixture family

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

### Exercise the cross-entity lineage envelope

```bash
python tools/validators/domains/water_planning/validate_status_collapse.py \
  fixtures/domains/water_planning/status_collapse/valid/valid_1.json
```

### Run the focused no-network lineage-envelope tests

```bash
python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_status_collapse.py' \
  --verbose
```

| Validation surface | What it checks | What success does not prove |
|---|---|---|
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct title, and representative valid/invalid fixture polarity for this entity family | Subject existence, digest validity, time syntax, source truth, correction application, withdrawal handling, rights, policy, or release |
| [`valid_1.json`](../../../fixtures/domains/water_planning/correction_or_withdrawal/valid/valid_1.json) | One representative correction envelope accepted with a nullable prior digest | That the example is real, source-supported, digest-bound, applied, current, or public-safe |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/correction_or_withdrawal/invalid/invalid_1.json) | The unrecognized `edit` action is rejected | Exhaustive negative coverage for identifiers, references, reason content, digest linkage, dates, or action-specific behavior |
| [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) | A synthetic cross-entity envelope contains `correction_or_withdrawal_ref`, `supersedes_ref`, and `superseded_by_ref` as strings or `null` | Resolution of those references or validation of a `CorrectionOrWithdrawal` record |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | A read-only pull-request workflow runs the repository schema and contract test lanes, including `tests/schemas` | Semantic truth, source admission, digest proof, policy, rights, sensitivity, correction application, release, or publication |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | A read-only, no-network workflow is path-triggered for water-planning contract changes and runs domain semantic and registry suites | The paired schema suite, Markdown link integrity, repository authorization, evidence closure, release, deployment, or publication |

> [!NOTE]
> A green test or workflow result is validation evidence only within the tested boundary. It is not a source receipt, digest verification, subject-state transition, policy decision, review record, release correction, rollback decision, or publication proof.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
|---|---|---|
| `WP-CW-01` | `NEEDS VERIFICATION` | Define allowed `subject_ref` families, version semantics, referential-integrity checks, and behavior when the target is missing, ambiguous, already withdrawn, or superseded. |
| `WP-CW-02` | `NEEDS VERIFICATION` | Define how corrected state is represented and applied: same-identity version, successor record, field-level patch, replacement reference, or another governed mechanism. |
| `WP-CW-03` | `NEEDS VERIFICATION` | Decide when `prior_digest` is required; define canonicalization, byte scope, algorithm agility, recomputation, subject binding, and mismatch behavior. |
| `WP-CW-04` | `NEEDS VERIFICATION` | Define correction and withdrawal chains, stable `record_id` generation, deduplication, ordering, conflict handling, cycle detection, and correction of a correction. |
| `WP-CW-05` | `NEEDS VERIFICATION` | Define full-withdrawal effects, reinstatement or reversal behavior, historical retention, public notice obligations, and downstream current-state selection. |
| `WP-CW-06` | `NEEDS VERIFICATION` | Enable or explicitly defer date-time format checking and define coherence among effective, source-publication, retrieval, observation, release, and correction times. |
| `WP-CW-07` | `NEEDS VERIFICATION` | Define how `source_ref` resolves to field-level evidence, receipts, source versions, and freshness without treating a pointer as evidence closure. |
| `WP-CW-08` | `NEEDS VERIFICATION` | Establish finite policy and consumer outcomes for unresolved, conflicting, stale, corrected, withdrawn, superseded, and rollback-required subjects. |
| `WP-CW-09` | `NEEDS VERIFICATION` | Define rights, privacy, sensitivity, redaction, and public-safe projection rules for `reason`, subject identity, prior values, and source material. |
| `WP-CW-10` | `NEEDS VERIFICATION` | Add dedicated positive and negative coverage for absent/null/valid/invalid digests, digest mismatch, empty or whitespace-only reasons, reference resolution, time format/order, both actions, duplicate actions, and withdrawal handling. |

Until these items are resolved, preserve prior state, narrow claims, expose unresolved lineage, and do not infer that a corrected value was supplied, a withdrawal was applied, a digest was verified, or a public carrier is current.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- field names, requiredness, enums, patterns, nullability, or `additionalProperties`;
- action, subject, reason, source, effective-time, publication-time, and prior-digest semantics;
- corrected-state, replacement, supersession, reinstatement, or withdrawal behavior;
- digest canonicalization, verification, mismatch, or algorithm rules;
- reference resolution, evidence, policy, rights, sensitivity, or public-safe projection; and
- consumer rules for selecting current, corrected, withdrawn, or superseded subjects.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, tests, known consumers, and correction lineage within one authorized review boundary. Do not widen or narrow runtime behavior through prose alone, and do not silently rewrite a relied-on historical subject.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository bytes; it does not erase source observations, action records, downstream reliance, released carriers, or publication history.

[Back to top](#top)

## Related

| Surface | Role |
|---|---|
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`application.md`](./application.md) | Example subject family with unresolved identity and explicit correction needs. |
| [`award.md`](./award.md) | Separate award decision and amount fact; a correction is not a new award. |
| [`funding_agreement.md`](./funding_agreement.md) | Separate agreement and paid-amount meaning. |
| [`project.md`](./project.md) | Separate project, recipient, region, and geometry-reference meaning. |
| [`completion.md`](./completion.md) | Separate completion state; correction or withdrawal does not create completion or benefit. |
| [`correction_or_withdrawal.schema.json`](../../../schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json) | Canonical machine shape for this action record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic action fixtures](../../../fixtures/domains/water_planning/correction_or_withdrawal/) | Representative valid and invalid inputs. |
| [Synthetic status-collapse fixtures](../../../fixtures/domains/water_planning/status_collapse/) | Cross-entity lineage and anti-collapse envelopes. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family regression tests. |
| [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) | Deterministic synthetic cross-entity lineage and anti-collapse validator. |
| [`test_status_collapse.py`](../../../tests/domains/water_planning/test_status_collapse.py) | No-network validator regression tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, temporal provenance, correction, supersession, rights, and admission limitations. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only pull-request schema and contract validation workflow. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only path-triggered water-planning validation workflow. |

[Back to top](#top)
