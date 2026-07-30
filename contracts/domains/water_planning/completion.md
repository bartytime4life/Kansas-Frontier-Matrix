<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-completion
title: Completion Contract — Water Planning
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
  - ./award.md
  - ./funding_agreement.md
  - ./project.md
  - ./construction_milestone.md
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/completion.schema.json
  - ../../../schemas/contracts/v1/domains/water_planning/README.md
  - ../../../fixtures/domains/water_planning/completion/
  - ../../../fixtures/domains/water_planning/status_collapse/
  - ../../../tools/validators/domains/water_planning/validate_status_collapse.py
  - ../../../tests/domains/water_planning/test_status_collapse.py
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Completion Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/completion.schema.json)

Defines the semantic meaning, explicit-state posture, and anti-collapse boundaries of a water-planning project completion record.

> [!IMPORTANT]
> This document and its paired schema are `PROPOSED` scaffolds. They do not prove that a project exists or is complete, that funds were paid, that construction or inspection occurred, that infrastructure is operational, that benefits were realized, or that a record is policy-approved, released, or KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [State, time, and evidence invariants](#state-time-and-evidence-invariants)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

A `Completion` represents an explicit completion-state record associated with a water-infrastructure [`Project`](./project.md). The record keeps five concerns separate:

- completion-record identity;
- a reference-shaped relationship to a project;
- the recorded completion timestamp;
- an explicit `complete`, `partial`, or `unknown` state; and
- a source pointer.

The required `project_ref` expresses an intended relationship to a project. Its non-empty string shape does not prove that the referenced project exists, that the reference resolves, or that project, region, recipient, location, award, funding, or construction facts are correct.

The required `completed_at` field records a date-time-shaped value, but the current schema does not define whether that value is an occurrence time, source-reported time, determination time, inspection time, or another completion-related instant. It also does not condition the timestamp on `completion_state`. Those semantics remain `NEEDS VERIFICATION`.

The contract describes record meaning. The paired JSON Schema defines accepted document shape. Source admission, field-level evidence resolution, referential integrity, rights and sensitivity review, policy decisions, correction, release, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
| --- | --- | --- |
| This document | `draft`; `PROPOSED`; v0.1 | Defines semantic meaning and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/completion.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not source truth, project resolution, policy, or release. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/completion/) | Synthetic test inputs | Exercise representative schema behavior; they are not project or completion evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check representative acceptance/rejection and preserve the completion-versus-award distinction. |
| [Status-collapse validator](../../../tools/validators/domains/water_planning/validate_status_collapse.py) and [tests](../../../tests/domains/water_planning/test_status_collapse.py) | Deterministic, no-network synthetic-fixture checks | Reject selected application/award, award/payment, payment/construction, and construction/completion collapse claims; they do not validate a `Completion` instance. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Excludes completion or operational-benefit claims inferred beyond source evidence; it does not activate a source or authorize release. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; policy behavior remains `NEEDS VERIFICATION` | No policy outcome or public-safe projection may be inferred from this contract or schema. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
| --- | ---: | --- | --- |
| `completion_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Completion-record identity. Generation, deduplication, versioning, and correction-lineage rules remain unspecified. |
| `project_ref` | Yes | Non-empty string | Reference-shaped relationship to a `Project`; existence and referential integrity are not encoded. |
| `completed_at` | Yes | String annotated as `date-time` | Completion-related time value. Its exact event role and relationship to the state remain unspecified. |
| `completion_state` | Yes | `complete`, `partial`, or `unknown` | Explicit source-evidence posture for completion. It is not an operational-readiness or benefit outcome. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not, by itself, an `EvidenceBundle`, receipt, proof, review, or release authorization. |

All five properties are required, and the current schema admits no additional properties.

[Back to top](#top)

## State, time, and evidence invariants

### Completion-state vocabulary

| State | Bounded meaning | Must not be inferred |
| --- | --- | --- |
| `complete` | The record asserts a complete state according to its source-evidence posture. | Payment, inspection approval, operational readiness, service delivery, effectiveness, or public benefit. |
| `partial` | The record asserts a partial state. | Which components are complete, a percentage, a construction milestone, remaining work, or operational capability. |
| `unknown` | The record preserves an unresolved completion state. | Incomplete, failed, denied, abandoned, not started, or complete. |

The state is explicit and finite, but the schema does not encode transition rules, evidence thresholds, determination authority, component-level detail, or correction lineage.

### Time and reference boundaries

- `completed_at` remains distinct from award, agreement, payment, construction-milestone, source-publication, retrieval, determination, review, correction, release, and publication times;
- all three completion states currently require `completed_at`; the schema does not define or enforce state/time coherence;
- `project_ref` does not establish project existence, identity resolution, location, region membership, construction status, or completion;
- `source_ref` does not prove field-level support, source admission, rights, sensitivity, freshness, review, or correction closure; and
- a completion record contains no completion certificate, inspector identity, component inventory, evidence digest, benefit measure, or operational-readiness determination.

> [!WARNING]
> The shared schema loader constructs `Draft202012Validator` without an explicit format checker. The schema's `date-time` annotation on `completed_at` must not be described as repository-enforced syntax until validation proves otherwise.

Real completion records, project details, payment data, precise infrastructure locations, inspection material, and operational claims require independent identity, source, rights, sensitivity, evidence, policy, review, correction, and release decisions. A `public-with-gates` label is not public-release authorization.

[Back to top](#top)

## Anti-collapse boundaries

A completion is not a payment, award, project, construction milestone, inspection approval, operational-readiness decision, or benefit claim. Every related record requires its own identity, source support, evidence, and governed state.

| Boundary | Required interpretation |
| --- | --- |
| Completion != award | [`Award`](./award.md) records a funding decision; it does not prove project delivery or completion. |
| Completion != payment | Paid-amount meaning belongs to [`FundingAgreement`](./funding_agreement.md); payment does not prove construction, completion, operation, or benefit. |
| Completion != project | [`Project`](./project.md) records award-linked delivery identity; project existence does not prove completion. |
| Completion != construction milestone | [`ConstructionMilestone`](./construction_milestone.md) records bounded progress; a milestone is not a completion event. |
| `complete` != operational benefit | A complete state does not prove that infrastructure operates, serves users, produces outcomes, or delivers public benefit. |
| `partial` != milestone detail | The partial state does not identify completed components, progress percentage, sequence, or remaining work. |
| `unknown` != false | An unresolved state is not evidence of incomplete, failed, denied, or abandoned work. |
| `completed_at` != evidence closure | A date-time-shaped value does not prove the event, source timing, inspection, determination authority, or correction state. |
| Project reference != referential integrity | A non-empty `project_ref` does not establish that the target exists or that project facts are valid. |
| Source reference != EvidenceBundle | A non-empty `source_ref` does not establish field-level support, rights, sensitivity, freshness, review, or publication. |
| Schema-valid != true or public-safe | Structural acceptance does not establish real-world correctness, policy approval, release, or KFM publication. |

### Related event and delivery records

| Record | Bounded fact | What it does not prove |
| --- | --- | --- |
| [`Award`](./award.md) | Formal funding decision and awarded amount | Payment, construction, completion, or benefit |
| [`FundingAgreement`](./funding_agreement.md) | Agreement and paid-amount meaning | Expenditure, construction, completion, or benefit |
| [`Project`](./project.md) | Award-linked delivery identity and reference states | Construction, completion, operation, or benefit |
| [`ConstructionMilestone`](./construction_milestone.md) | Bounded construction-progress event | Project completion or operational benefit |
| `Completion` | Explicit completion-state record | Operational readiness, service, impact, effectiveness, or benefit |

### Executable sequence guardrails

The no-network status-collapse suite preserves the upstream chain that must remain separate before a completion claim can be interpreted:

| Invalid synthetic claim | Stable finding | Contract boundary retained |
|---|---|---|
| [`application_is_award`](../../../fixtures/domains/water_planning/status_collapse/invalid/application_is_award.json) | `APPLICATION_IS_NOT_AWARD` | A submitted request does not become a funding decision. |
| [`award_is_payment`](../../../fixtures/domains/water_planning/status_collapse/invalid/award_is_payment.json) | `AWARD_IS_NOT_PAYMENT` | An award does not prove disbursement. |
| [`payment_is_construction`](../../../fixtures/domains/water_planning/status_collapse/invalid/payment_is_construction.json) | `PAYMENT_IS_NOT_CONSTRUCTION` | Payment does not prove physical progress. |
| [`construction_is_completion`](../../../fixtures/domains/water_planning/status_collapse/invalid/construction_is_completion.json) | `CONSTRUCTION_IS_NOT_COMPLETION` | Construction activity does not become an explicit completion state. |

These findings apply to the synthetic status-collapse candidate only. They do not validate a `Completion` document, establish event order, resolve `project_ref`, or prove any real application, award, payment, milestone, or completion.

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
| --- | --- | --- |
| Canonical machine-shape file | [`completion.schema.json`](../../../schemas/contracts/v1/domains/water_planning/completion.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Required fields | 5 of 5 properties | Every admitted record carries identity, project reference, time, state, and source reference. |
| Completion states | `complete`, `partial`, `unknown` | Other values, including `done`, are rejected by enum validation. |
| Unknown fields | Rejected by `additionalProperties: false` | Widening the record requires coordinated contract, schema, fixture, and test review. |
| Project referential integrity | Not encoded | A non-empty `project_ref` may still be unresolved or incorrect. |
| State/time coherence | Not conditionally enforced | Every state requires `completed_at`, and no rule defines what the time means for `partial` or `unknown`. |
| Date-time assertion | Annotated on `completed_at` | The shared validator supplies no explicit format checker, so syntax enforcement remains `NEEDS VERIFICATION`. |
| Evidence and release closure | Not encoded | `source_ref` and schema validity do not establish support, rights, policy, review, release, or publication. |

The contract and schema must remain synchronized: prose cannot loosen or tighten machine behavior without a coordinated schema change.

[Back to top](#top)

## Synthetic example

The checked-in valid fixture is synthetic and test-only. It must not be cited as evidence that a project exists, construction occurred, completion was determined, or benefits were realized.

```json
{
  "completion_id": "kwo-swigp-fy2027-compl-synthetic-001",
  "project_ref": "kwo-swigp-fy2027-proj-synthetic-001",
  "completed_at": "2027-06-01T00:00:00Z",
  "completion_state": "complete",
  "source_ref": "kwo:grant-programs:swigp:fy2027:completion:synthetic-001"
}
```

The paired invalid fixture uses `completion_state: done`; the schema test expects that record to be rejected because `done` is not an admitted enum value.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Run the focused completion checks

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py -k completion
```

### Validate the complete water-planning schema family

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

### Exercise the accepted synthetic anti-collapse envelope

```bash
python tools/validators/domains/water_planning/validate_status_collapse.py \
  fixtures/domains/water_planning/status_collapse/valid/valid_1.json
```

### Run the no-network cross-record boundary tests

```bash
python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_status_collapse.py' \
  --verbose
```

| Validation surface | What it checks | What success does not prove |
| --- | --- | --- |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct entity titles, representative valid/invalid fixtures, and completion-versus-award separation | Project resolution, state/time coherence, source accuracy, rights, policy, operation, benefit, or release |
| [`valid_1.json`](../../../fixtures/domains/water_planning/completion/valid/valid_1.json) | One representative `complete` record accepted by the paired schema | That the example is real, current, source-supported, operational, or beneficial |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/completion/invalid/invalid_1.json) | An unrecognized `done` state is rejected | Exhaustive negative coverage for identity, references, time, evidence, transitions, or state semantics |
| [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) and [`test_status_collapse.py`](../../../tests/domains/water_planning/test_status_collapse.py) | Stable findings for synthetic application/award, award/payment, payment/construction, and construction/completion collapse; complete invalid-fixture polarity; no-network execution; and protected-value non-echo | Validation of a `Completion` instance, lifecycle chronology, project resolution, or real completion evidence |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Pull-request schema inventory, meta-schema checks, aggregate fixtures, and repository-owned schema/contract tests under read-only permissions | Semantic truth, source admission, policy, rights, sensitivity, release, or publication |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Path-triggered no-network water-planning domain and RAC-registry checks under `contents: read` | Completion-schema exhaustiveness, project resolution, review approval, evidence closure, release, deployment, or publication |

> [!NOTE]
> A green test or workflow result is validation evidence only within the tested boundary. It is not a source receipt, completion certificate, policy decision, review record, release manifest, operational assessment, benefit proof, or publication proof.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
| --- | --- | --- |
| `WP-COMP-01` | `NEEDS VERIFICATION` | Define `completion_id` generation, deduplication, versioning, correction, withdrawal, and supersession behavior. |
| `WP-COMP-02` | `NEEDS VERIFICATION` | Add or identify deterministic referential-integrity validation from `project_ref` to a governed project record. |
| `WP-COMP-03` | `NEEDS VERIFICATION` | Define the exact event role of `completed_at` and its relationship to `complete`, `partial`, and `unknown`. |
| `WP-COMP-04` | `NEEDS VERIFICATION` | Decide whether `date-time` annotations require an explicit format checker in the shared schema runner. |
| `WP-COMP-05` | `NEEDS VERIFICATION` | Define evidence thresholds, determination authority, allowed transitions, and correction rules for each completion state. |
| `WP-COMP-06` | `NEEDS VERIFICATION` | Define partial-completion detail and milestone linkage without collapsing a `ConstructionMilestone` into `Completion`. |
| `WP-COMP-07` | `NEEDS VERIFICATION` | Define how `source_ref` resolves to field-level evidence and how observation, retrieval, determination, correction, and supersession times are retained. |
| `WP-COMP-08` | `NEEDS VERIFICATION` | Define operational-readiness and benefit evidence outside this record; neither may be inferred from completion alone. |
| `WP-COMP-09` | `NEEDS VERIFICATION` | Establish finite policy outcomes and public-safe projection rules for project, completion, infrastructure, payment, inspection, and operational information. |

Until these items are resolved, narrow claims, preserve explicit unknowns, and do not infer project resolution, construction, inspection approval, payment, operational readiness, service, impact, effectiveness, benefit, or public eligibility.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- field names, requiredness, enum values, patterns, date-time handling, or `additionalProperties`;
- completion-state meaning, transition rules, timestamp semantics, or evidence thresholds;
- project-reference or source-reference resolution;
- identity, deduplication, correction, withdrawal, and supersession behavior;
- the boundary between milestone, completion, operation, and benefit; and
- any public-safe projection or policy outcome.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, tests, known consumers, and correction lineage within one authorized review boundary. Use [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) or another governed correction surface when applicable; do not silently rewrite a relied-on historical completion record.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository bytes; it does not erase source history, project or completion records, downstream reliance, operational state, benefit claims, or publication state.

[Back to top](#top)

## Related

| Surface | Role |
| --- | --- |
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`award.md`](./award.md) | Separate award decision and awarded-amount meaning. |
| [`funding_agreement.md`](./funding_agreement.md) | Separate agreement and paid-amount meaning. |
| [`project.md`](./project.md) | Separate award-linked project and authority-reference contract. |
| [`construction_milestone.md`](./construction_milestone.md) | Separate construction-progress event contract. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | Domain correction and withdrawal event contract. |
| [`completion.schema.json`](../../../schemas/contracts/v1/domains/water_planning/completion.schema.json) | Canonical machine shape for this record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic completion fixtures](../../../fixtures/domains/water_planning/completion/) | Representative valid and invalid inputs. |
| [Synthetic status-collapse fixtures](../../../fixtures/domains/water_planning/status_collapse/) | Cross-record application, award, payment, construction, and completion rejection envelopes. |
| [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) | Deterministic synthetic anti-collapse validator. |
| [`test_status_collapse.py`](../../../tests/domains/water_planning/test_status_collapse.py) | No-network regression tests for stable cross-record findings. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family regression tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, rights, freshness, access, and admission limitations. |
| [Directory Rules v2](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only schema and contract validation workflow. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only path-triggered water-planning validation workflow. |

[Back to top](#top)
