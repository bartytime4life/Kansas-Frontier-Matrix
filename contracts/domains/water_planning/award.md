<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-award
title: Award Contract — Water Planning
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
  - ./recommendation.md
  - ./funding_agreement.md
  - ./project.md
  - ./construction_milestone.md
  - ./completion.md
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/award.schema.json
  - ../../../fixtures/domains/water_planning/award/
  - ../../../fixtures/domains/water_planning/status_collapse/
  - ../../../tools/validators/domains/water_planning/validate_status_collapse.py
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../tests/domains/water_planning/test_status_collapse.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Award Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/award.schema.json)
[![Water-planning checks](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml/badge.svg?branch=main)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml)

Defines the semantic meaning, amount boundary, and fail-closed interpretation of a water-planning grant award record.

> [!IMPORTANT]
> This document and its paired schema are `PROPOSED` scaffolds. They do not prove that an award was made, admit a source, establish recipient identity, authorize payment, prove a project or benefit, approve policy or promotion, or make a record KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Award and evidence invariants](#award-and-evidence-invariants)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Rights, sensitivity, and release](#rights-sensitivity-and-release)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

An `Award` represents one grant award event associated with an [`Application`](./application.md). The record separates:

- award identity from application and recommendation identity;
- a required application reference from an optional recommendation reference;
- fiscal-year and funding-source labels from program-version authority;
- the awarded amount from requested, recommended, paid, expended, or benefit amounts;
- award-event time from source-publication time; and
- a source pointer from evidence, rights, review, policy, release, and publication authority.

The required `application_ref` expresses an intended relationship to an application. Its non-empty string shape does not prove that the referenced application exists, was eligible, was recommended, or supports the award. A `null` or absent `recommendation_ref` means only that this record does not carry that reference; it does not prove that no recommendation existed.

The contract describes record meaning. The paired JSON Schema defines accepted document shape. Source admission, field-level evidence resolution, recipient identity, rights and sensitivity review, policy decisions, payment, correction, release, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
|---|---|---|
| This document | `draft`; `PROPOSED`; v0.1 | Defines semantic meaning and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/award.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not source truth, funding authority, or policy. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/award/) | Synthetic test inputs | Exercise representative schema behavior; they are not award records or funding evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check representative fixture polarity, distinct entity titles, amount separation, and award/completion separation. |
| [Status-collapse validator](../../../tools/validators/domains/water_planning/validate_status_collapse.py) and [tests](../../../tests/domains/water_planning/test_status_collapse.py) | Deterministic, no-network synthetic-fixture checks | Reject selected application/award, award/payment, payment/construction, construction/completion, and amount collapses; they do not validate a live award record. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Excludes unsupported funding and benefit inferences; it does not activate a connector or authorize release. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; policy behavior remains `NEEDS VERIFICATION` | No policy outcome may be inferred from this contract or schema. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
|---|---:|---|---|
| `award_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Award-record identity. Generation, deduplication, and version-lineage rules remain unspecified. |
| `application_ref` | Yes | Non-empty string | Reference-shaped relationship to an `Application`; referential integrity and application-to-award eligibility are not encoded. |
| `recommendation_ref` | No | String or `null` | Reference to a recommendation when recorded. Absence or `null` does not prove that no recommendation existed. |
| `fiscal_year` | Yes | String matching `^FY[0-9]{4}$` | Source-facing fiscal-year label. It does not establish a program version, appropriation, or effective period by itself. |
| `funding_source` | No | String or `null` | Funding-source label when stated. It is not a controlled identity, rights decision, appropriation record, or proof of available funds. |
| `awarded_amount` | No | Number greater than or equal to zero, or `null` | Amount awarded as stated by the source when disclosed; not a request, recommendation, payment, expenditure, or benefit. Currency and precision semantics remain unspecified. |
| `awarded_at` | Yes | String annotated as `date-time` | Award-event timestamp as recorded; distinct from source publication, retrieval, payment, construction, and completion times. |
| `source_publication_time` | No | `date-time` string or `null` | When the source published the award information, if recorded; distinct from award-event and retrieval time. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not, by itself, an `EvidenceBundle`, receipt, proof, review, or release authorization. |

No additional properties are admitted by the current schema.

[Back to top](#top)

## Award and evidence invariants

The semantic posture is fail closed:

- `awarded_amount` records only the awarded fact and must not absorb requested, recommended, agreed, paid, expended, construction, completion, or benefit meaning;
- `awarded_amount: null` preserves nondisclosure or absence in the record and must not be converted to zero;
- a numeric `awarded_amount` is non-negative under the schema, but the schema does not define currency, scale, rounding, matching-fund treatment, or amendment semantics;
- `application_ref` and `recommendation_ref` remain references whose existence and relationships require validation beyond string shape;
- `awarded_at` and `source_publication_time` remain separate temporal facts and must not be substituted for one another;
- `funding_source` is descriptive text in the current shape and must not be treated as a resolved program, appropriation, or fund identity without separate authority; and
- `source_ref` must remain a pointer whose evidence, rights, sensitivity, freshness, and field-level support are resolved through their owning governance surfaces.

> [!WARNING]
> The paired schema annotates its timestamp fields with `format: date-time`, but the shared validator constructs `Draft202012Validator` without an explicit format checker. Date-time syntax must not be described as machine-enforced by the current test path.

The existence of an `Award` record does not authorize payment or establish a recipient, project, construction milestone, completion event, operational result, or public benefit.

[Back to top](#top)

## Anti-collapse boundaries

An award is a funding decision event. Each upstream request, downstream agreement, delivery record, and claimed outcome requires its own identity, source support, evidence, and governed state.

| Boundary | Required interpretation |
|---|---|
| Award != application | [`Application`](./application.md) is a request; a submitted or eligible application does not prove an award. |
| Award != recommendation | [`Recommendation`](./recommendation.md) is advisory and owns `recommended_amount`; it does not establish a formal award. |
| Award != payment | Paid-amount meaning belongs to [`FundingAgreement`](./funding_agreement.md); `awarded_amount` does not prove disbursement. |
| Award != project | [`Project`](./project.md) is an award-linked delivery record; an award does not prove project creation, location, construction, or delivery. |
| Award != construction | [`ConstructionMilestone`](./construction_milestone.md) requires separate event evidence; funding authorization is not construction evidence. |
| Award != completion | [`Completion`](./completion.md) has a separate schema and state; an award does not prove completed work. |
| Award != operational benefit | Award, payment, construction, and completion facts do not establish service, impact, effectiveness, or public benefit. |
| Fiscal year != program version | A pattern-valid `fiscal_year` does not resolve statutory basis, scoring rules, or supersession lineage. |
| Source reference != evidence closure | A non-empty `source_ref` does not establish field-level support, rights, sensitivity, freshness, review, or publication. |
| Schema-valid != true or public-safe | Structural acceptance does not establish real-world correctness, policy approval, release, or KFM publication. |

### Amount semantics

| Fact | Owning entity | What it does not prove |
|---|---|---|
| `requested_amount` | [`Application`](./application.md) | Recommendation, award, agreement, or payment |
| `recommended_amount` | [`Recommendation`](./recommendation.md) | Award or disbursement |
| `awarded_amount` | `Award` | Payment, expenditure, construction, completion, or benefit |
| `paid_amount` | [`FundingAgreement`](./funding_agreement.md) | Expenditure, completion, or operational benefit |

### Executable sequence guardrails

The no-network status-collapse suite carries a separate synthetic envelope for cross-record claims. It does not validate an `Award` instance, but it makes the application-to-delivery separation executable:

| Invalid synthetic claim | Stable finding | Contract boundary retained |
|---|---|---|
| [`application_is_award`](../../../fixtures/domains/water_planning/status_collapse/invalid/application_is_award.json) | `APPLICATION_IS_NOT_AWARD` | A submitted request does not become a funding decision. |
| [`award_is_payment`](../../../fixtures/domains/water_planning/status_collapse/invalid/award_is_payment.json) | `AWARD_IS_NOT_PAYMENT` | A funding decision does not become a disbursement. |
| [`payment_is_construction`](../../../fixtures/domains/water_planning/status_collapse/invalid/payment_is_construction.json) | `PAYMENT_IS_NOT_CONSTRUCTION` | A payment does not prove physical progress or a milestone. |
| [`construction_is_completion`](../../../fixtures/domains/water_planning/status_collapse/invalid/construction_is_completion.json) | `CONSTRUCTION_IS_NOT_COMPLETION` | Construction activity does not become an explicit completion state. |
| [collapsed `amount` field](../../../fixtures/domains/water_planning/status_collapse/invalid/collapsed_amount_facts.json) | `COLLAPSED_AMOUNT_FIELD_FORBIDDEN` | Requested, recommended, awarded, and paid amounts keep distinct owning fields. |

These findings enforce rejection only within the synthetic status-collapse candidate shape. They do not resolve entity references, prove event order, or establish that any application, award, payment, milestone, or completion exists.

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
|---|---|---|
| Canonical machine-shape file | [`award.schema.json`](../../../schemas/contracts/v1/domains/water_planning/award.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Required fields | 5 of 9 properties | Optional fields may be absent; nullable fields may explicitly carry `null`. |
| Unknown fields | Rejected by `additionalProperties: false` | Widening the record requires coordinated contract, schema, fixture, and test review. |
| Application linkage | Non-empty string only | Referenced-record existence, type, eligibility, and lineage are not enforced. |
| Recommendation linkage | Optional string or `null` | Referential integrity and recommendation-to-award consistency are not enforced. |
| Amount constraint | Non-negative number or `null` | Currency, precision, amendment, and cross-record amount consistency are not encoded. |
| Date-time assertion | Annotated on `awarded_at` and `source_publication_time` | The shared validator has no explicit format checker, so syntax enforcement is absent from that test path. |

The contract and schema must remain synchronized: prose cannot loosen or tighten machine behavior without a coordinated schema change.

[Back to top](#top)

## Synthetic example

The checked-in valid fixture is synthetic and test-only. It must not be cited as evidence that an application, recommendation, award, amount, funding source, or publication exists.

```json
{
  "award_id": "kwo-swigp-fy2027-award-synthetic-001",
  "application_ref": "kwo-swigp-fy2027-app-synthetic-001",
  "recommendation_ref": "kwo-swigp-fy2027-rec-synthetic-001",
  "fiscal_year": "FY2027",
  "funding_source": "State Water Infrastructure Grant Program",
  "awarded_amount": null,
  "awarded_at": "2026-11-01T00:00:00Z",
  "source_publication_time": null,
  "source_ref": "kwo:grant-programs:swigp:fy2027:award:synthetic-001"
}
```

The paired invalid fixture uses `fiscal_year: "2027"`; the schema test expects that record to be rejected because it does not match `^FY[0-9]{4}$`.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Validate the paired schema and fixture family

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

### Exercise the synthetic anti-collapse boundary

```bash
python tools/validators/domains/water_planning/validate_status_collapse.py \
  fixtures/domains/water_planning/status_collapse/valid/valid_1.json
```

### Run the focused no-network validator tests

```bash
python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_status_collapse.py' \
  --verbose
```

| Validation surface | What it checks | What success does not prove |
|---|---|---|
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct entity titles, representative valid/invalid fixtures, amount-field separation, and completion/award separation | Referential integrity, currency semantics, source accuracy, funding authority, rights, policy, payment, or release |
| [`valid_1.json`](../../../fixtures/domains/water_planning/award/valid/valid_1.json) | One representative award shape accepted by the paired schema | That the example is real, current, complete, source-supported, or publicly releasable |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/award/invalid/invalid_1.json) | A fiscal-year value without the required `FY` prefix is rejected | Exhaustive negative coverage for references, timestamps, amounts, funding source, or evidence |
| [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) and [`test_status_collapse.py`](../../../tests/domains/water_planning/test_status_collapse.py) | Stable findings for synthetic application/award, award/payment, payment/construction, construction/completion, and amount-field collapse; blocked live behavior; no-network execution; and protected-value non-echo | Validation of an `Award` instance, lifecycle ordering, or evidence for a real application, award, payment, milestone, completion, or benefit |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Pull-request schema inventory, meta-schema checks, aggregate fixtures, and repository-owned schema/contract tests under read-only permissions | Semantic truth, source admission, policy, rights, sensitivity, release, or publication |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Path-triggered no-network water-planning domain and RAC-registry checks under `contents: read` | Award-schema exhaustiveness, evidence closure, review approval, release, deployment, or publication |

> [!NOTE]
> A green test, check, or badge is validation evidence only within the tested boundary. It is not a source receipt, funding decision, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Rights, sensitivity, and release

The [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) records a fail-closed source posture:

- authenticated grant-portal data is excluded unless separately authorized;
- unpublished application content, scores, review notes, and adjudication records are excluded;
- applicant or organization data not published on official public pages is not treated as public;
- funding, approval, completion, or operational-benefit claims must not be inferred beyond source evidence;
- published recipient-list rights remain `NEEDS VERIFICATION`; and
- no source record, contract, schema, fixture, test, workflow, commit, pull request, or merge creates release or publication authority.

An award record may be eligible for a later public-safe projection only after source identity, field-level evidence, rights, sensitivity, applicant or recipient exposure, policy, validation, review, release, correction, and rollback requirements are satisfied by their owning surfaces.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
|---|---|---|
| `WP-AWARD-01` | `NEEDS VERIFICATION` | Define deterministic `award_id` generation, deduplication, amendment, and supersession behavior. |
| `WP-AWARD-02` | `NEEDS VERIFICATION` | Add or identify referential-integrity checks for `application_ref` and `recommendation_ref`, including type and lineage compatibility. |
| `WP-AWARD-03` | `NEEDS VERIFICATION` | Define currency, scale, precision, rounding, matching-fund, partial-award, and amended-award semantics for `awarded_amount`. |
| `WP-AWARD-04` | `NEEDS VERIFICATION` | Define the authoritative meaning of `awarded_at` and add date-time format enforcement where required. |
| `WP-AWARD-05` | `NEEDS VERIFICATION` | Replace or pair free-text `funding_source` with a governed program or fund reference without overwriting source-native wording. |
| `WP-AWARD-06` | `NEEDS VERIFICATION` | Define field-level evidence requirements and the resolution path from `source_ref` to an admitted `EvidenceBundle`. |
| `WP-AWARD-07` | `NEEDS VERIFICATION` | Model conditional, amended, rescinded, declined, or no-award outcomes without using an `Award` record as a generic decision envelope. |
| `WP-AWARD-08` | `NEEDS VERIFICATION` | Complete rights, sensitivity, recipient-exposure, and public-safe release review for any real award source family. |

Until these items close, consumers must not infer missing references, currencies, timestamps, identities, payment state, project state, completion, benefit, or release eligibility.

[Back to top](#top)

## Compatibility, correction, and rollback

- Preserve `doc_id: kfm://doc/contracts-domains-water-planning-award`, the v0.1 identity, and existing property names while this contract remains in force.
- Treat the Markdown contract as semantic authority and the paired schema as machine-shape authority; change both with fixtures and tests when behavior changes.
- Do not silently reinterpret `null`, omission, a string reference, or a schema-valid value as resolved evidence.
- Additive fields require coordinated review because `additionalProperties: false` rejects unknown properties.
- Represent a later correction or withdrawal through the governed [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) family and preserved lineage; do not erase the prior record silently.
- Before merge, rollback is closing the unmerged draft pull request or reverting its branch commit through the authorized review path.
- After merge, restore the prior document bytes with a transparent revert or forward correction; do not alter the schema or fixtures merely to make prose appear consistent.

Rollback changes repository documentation only. It does not reverse an external award, payment, project, release, or publication state.

[Back to top](#top)

## Related

- [`README.md`](./README.md) — Domain contract index and cross-entity boundaries
- [`application.md`](./application.md) — Upstream application meaning
- [`recommendation.md`](./recommendation.md) — Advisory recommendation and `recommended_amount`
- [`funding_agreement.md`](./funding_agreement.md) — Agreement and `paid_amount`
- [`project.md`](./project.md) — Award-linked project record
- [`construction_milestone.md`](./construction_milestone.md) — Construction event boundary
- [`completion.md`](./completion.md) — Completion-state boundary
- [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) — Correction and withdrawal lineage
- [`award.schema.json`](../../../schemas/contracts/v1/domains/water_planning/award.schema.json) — Canonical machine shape
- [`award` fixtures](../../../fixtures/domains/water_planning/award/) — Synthetic valid and invalid examples
- [Status-collapse fixtures](../../../fixtures/domains/water_planning/status_collapse/) — Synthetic cross-record and amount-boundary envelopes
- [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) — Synthetic anti-collapse validator
- [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) — Paired schema and fixture tests
- [`test_status_collapse.py`](../../../tests/domains/water_planning/test_status_collapse.py) — No-network semantic boundary tests
- [`kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source role, exclusions, rights posture, and verification backlog
- [`directory-rules.md`](../../../docs/doctrine/directory-rules.md) and [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) — Responsibility-root placement authority
- [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) and [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) — Relevant read-only validation workflows

[Back to top](#top)
