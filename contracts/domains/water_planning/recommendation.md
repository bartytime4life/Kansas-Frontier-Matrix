<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-recommendation
title: Recommendation Contract — Water Planning
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
  - ./advisory_committee_meeting.md
  - ./application.md
  - ./eligibility_decision.md
  - ./scoring_matrix_version.md
  - ./award.md
  - ./funding_agreement.md
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/recommendation.schema.json
  - ../../../schemas/contracts/v1/domains/water_planning/README.md
  - ../../../fixtures/domains/water_planning/recommendation/
  - ../../../fixtures/domains/water_planning/status_collapse/
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../tools/validators/domains/water_planning/validate_status_collapse.py
  - ../../../tests/domains/water_planning/test_status_collapse.py
  - ../../../tools/validators/_common/jsonschema_runner.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Recommendation Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/recommendation.schema.json)

Defines the semantic meaning, advisory boundary, amount ownership, and fail-closed interpretation of a water-planning grant-recommendation record.

> [!IMPORTANT]
> This document and its paired schema are `draft` / `PROPOSED` scaffolds. They do not prove that an application was reviewed, establish who made or adopted a recommendation, verify an amount or timestamp, create an eligibility or award decision, authorize payment or project work, clear rights or sensitivity, approve policy or promotion, or make any record KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Recommendation, amount, and evidence invariants](#recommendation-amount-and-evidence-invariants)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Rights, sensitivity, and release](#rights-sensitivity-and-release)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

A `Recommendation` represents one source-attributed advisory or administrative recommendation associated with one application. It may refer to a separate eligibility decision and may carry the amount recommended by the source.

The record is an intermediate grant-process event. It does not create a formal award, agreement, disbursement, project, construction event, completion state, or operational-benefit claim. A later `Award` may refer back to a recommendation, but that relationship does not make the records equivalent and does not guarantee that the awarded amount matches the recommended amount.

The current shape records identity, upstream references, an optional amount, one recommendation timestamp, and a source pointer. It does not identify the recommending body, meeting, reviewer, scoring matrix, score, rank, rationale, vote, conditions, recommendation status, program version, fiscal year, currency, or correction lineage. Consumers must not infer those facts from identifier text, application content, amount equality, chronology, or source naming.

This contract defines semantic meaning. The paired JSON Schema defines accepted machine shape. Source admission, field-level evidence, identity and relationship resolution, policy, review, correction, release, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
|---|---|---|
| This document | `draft`; `PROPOSED`; v0.1 | Defines Recommendation meaning, amount ownership, and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/recommendation.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not source truth, relationship integrity, or policy. |
| [Recommendation fixtures](../../../fixtures/domains/water_planning/recommendation/) | Synthetic test inputs | Exercise one accepted shape and one missing-identity rejection; they are not grant evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check representative fixture polarity, entity-title separation, and amount-field ownership. |
| [Status-collapse fixtures and tests](../../../fixtures/domains/water_planning/status_collapse/) | Synthetic semantic guardrail | Reject collapsing an application into a recommendation or a recommendation into an award; they do not validate real recommendations. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Records source roles, exclusions, and open rights questions; it does not admit grant records or authorize release. |
| `policy/domains/water_planning/` | Schema metadata forward pointer; the KWO catalog records this surface as not yet created | No policy, allow, deny, hold, release, or publication outcome may be inferred here. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, `fixtures/` owns reusable synthetic inputs, `tests/` owns executable conformance evidence, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane within the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
|---|---:|---|---|
| `recommendation_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Recommendation-record identity. Issuance, namespace ownership, uniqueness, deduplication, amendment, and correction rules remain unspecified. |
| `application_ref` | Yes | Non-empty string | Intended reference to the upstream `Application`. The schema does not resolve the target, enforce object type, or prove that the recommendation concerns that application. |
| `eligibility_decision_ref` | No | String or `null`; no minimum length | Intended reference to a separate `EligibilityDecision` when available. Absence, `null`, and an empty string are all shape-admissible states with no fully defined semantic distinction. |
| `recommended_amount` | No | Number or `null`; minimum `0` | Source-stated recommended amount when disclosed. It is distinct from requested, awarded, and paid amounts. Currency, scale, precision, rounding, and amount basis are not encoded. |
| `recommended_at` | Yes | String annotated as `date-time` | Source-attributed time associated with the recommendation. Exact event-time semantics and format enforcement remain unresolved. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not by itself an `EvidenceRef`, `EvidenceBundle`, source-admission decision, receipt, proof, or release authorization. |

No additional properties are admitted by the current schema.

[Back to top](#top)

## Recommendation, amount, and evidence invariants

Interpret a Recommendation fail closed:

- create and preserve a Recommendation as its own event record; do not overwrite the upstream Application or reuse an Award as the recommendation envelope;
- resolve `application_ref` to the intended object, version, and lineage before relying on the relationship;
- treat `eligibility_decision_ref` as an unverified pointer until target existence, type, application compatibility, chronology, and evidence are checked;
- do not infer eligibility from the presence of a recommendation or infer a recommendation from eligibility alone;
- preserve `recommended_amount` as a Recommendation-owned fact, separate from `requested_amount`, `awarded_amount`, and `paid_amount`;
- keep numeric zero, explicit `null`, and field omission distinct; the current schema accepts all three amount states but does not fully define their business meaning;
- do not assume a currency, precision, matching-fund basis, total-project-cost basis, or partial-funding rule from a bare number;
- treat equal requested, recommended, awarded, or paid values as separate facts requiring separate sources and event records;
- keep `recommended_at` separate from application submission, eligibility determination, meeting, source publication, retrieval, award, correction, release, and KFM publication times;
- preserve the source's actual advisory posture; do not convert ranking, scoring, discussion, staff analysis, or a meeting agenda into a recommendation without evidence of the recommending act;
- resolve `source_ref` through the appropriate source, evidence, rights, sensitivity, correction, and review surfaces before making a consequential claim; and
- represent later correction or withdrawal through governed lineage rather than silently replacing the prior recommendation.

> [!WARNING]
> The valid synthetic fixture uses `recommended_amount: null`, which the schema describes as not publicly disclosed. Because the field is optional, the current shape also admits omission; no validator distinguishes unknown, not applicable, not yet observed, withheld, or not publicly disclosed. Consumers must not invent that distinction.

[Back to top](#top)

## Anti-collapse boundaries

| Boundary | Required interpretation |
|---|---|
| Application != recommendation | An application records a request; submission, completeness, or requested amount does not prove that a recommendation exists. |
| Eligibility decision != recommendation | Eligibility is a separate application-specific determination. Eligibility does not establish funding rank, recommended amount, or an advisory act. |
| Meeting or discussion != recommendation | Attendance, agenda placement, deliberation, scoring, or minutes do not establish a recommendation unless the source supports that event. |
| Scoring matrix or score != recommendation | A scoring artifact or computed score does not itself recommend an application or amount. |
| Recommendation != award | A recommendation is advisory or administrative process output; only a separate, supported Award record owns the formal award event. |
| Recommended amount != requested amount | The amount sought by the applicant remains an Application fact even when the values happen to match. |
| Recommended amount != awarded amount | A formal award may differ, be conditional, be absent, or never occur. Equality does not collapse the events. |
| Recommended amount != paid amount | A recommendation does not establish an agreement, disbursement, expenditure, or payment timing. |
| Recommendation != project or delivery state | This record proves no recipient identity, project creation, construction, completion, operation, impact, or public benefit. |
| `null` or omission != zero | Unknown, undisclosed, absent, and explicit zero are not interchangeable amount facts. |
| Reference != resolved relationship | A shape-valid string does not prove target existence, type, version, chronology, or compatibility. |
| Source reference != evidence closure | A non-empty `source_ref` does not prove field-level support, rights, freshness, correction state, or review. |
| Schema-valid != true or public-safe | Structural acceptance does not establish real-world correctness, policy approval, release, or KFM publication. |

The synthetic status-collapse validator separately rejects `application_is_recommendation: true` and `recommendation_is_award: true`. That guardrail is intentionally narrower than real event, evidence, or relationship validation.

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
|---|---|---|
| Canonical machine-shape file | [`recommendation.schema.json`](../../../schemas/contracts/v1/domains/water_planning/recommendation.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Properties | 6 | The shape is a minimal recommendation envelope, not a complete review or adjudication model. |
| Required fields | 4 of 6 | `eligibility_decision_ref` and `recommended_amount` may be absent; each also admits `null`. |
| Unknown fields | Rejected by `additionalProperties: false` | Adding authority, rationale, score, rank, status, currency, evidence, or correction fields requires coordinated review. |
| In-record discriminator | None | Shape recognition depends on the selected schema; the record carries no constant `record_type` or `event_type`. |
| Identity constraint | Lowercase-leading pattern only | Uniqueness, namespace ownership, aliasing, and deduplication are not enforced. |
| Application reference | Required non-empty string | Target existence, type, version, and lineage are not resolved. |
| Eligibility reference | Optional string or `null` | The schema admits an empty string and does not check application compatibility or chronology. |
| Amount constraint | Non-negative number or `null` | Currency, scale, precision, rounding, upper bound, source basis, and relationships to other amount facts are not enforced. |
| Date-time assertion | `format: date-time` annotation | The shared validator constructs `Draft202012Validator` without a format checker, so malformed date-time strings are not rejected by that inspected path. |
| Cross-field behavior | None | References, amount, and time are not checked for coherence with one another or with upstream and downstream records. |
| Evidence and release closure | Not encoded | Schema conformance does not establish evidence, rights, policy, review, release, or publication. |

The contract and schema must remain synchronized: prose cannot silently loosen or tighten machine behavior.

[Back to top](#top)

## Synthetic example

The checked-in valid fixture is synthetic and test-only. Its source-shaped values must not be cited as evidence that an application, eligibility decision, recommendation, amount state, timestamp, or source record exists.

```json
{
  "recommendation_id": "kwo-swigp-fy2027-rec-synthetic-001",
  "application_ref": "kwo-swigp-fy2027-app-synthetic-001",
  "eligibility_decision_ref": "kwo-swigp-fy2027-elig-synthetic-001",
  "recommended_amount": null,
  "recommended_at": "2026-10-01T00:00:00Z",
  "source_ref": "kwo:grant-programs:swigp:fy2027:rec:synthetic-001"
}
```

The paired invalid fixture omits `recommendation_id` and is rejected because that property is required. It does not provide negative coverage for identifier syntax, blank references, malformed timestamps, negative or ambiguous amounts, unresolved relationships, or recommendation-to-award collapse.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Run the focused Recommendation schema checks

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py -k recommendation
```

### Validate the complete water-planning entity schema family

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

### Run the no-network status-collapse suite

```bash
python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_status_collapse.py' \
  --verbose
```

| Validation surface | What it checks | What success does not prove |
|---|---|---|
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct entity titles, representative valid/invalid fixture polarity, and separate requested/recommended/awarded/paid field ownership | Source truth, date-time syntax, relationship resolution, recommending authority, currency, rationale, evidence, rights, policy, or release |
| [`valid_1.json`](../../../fixtures/domains/water_planning/recommendation/valid/valid_1.json) | One synthetic six-field shape accepted by the paired schema | That any referenced record exists or that a recommendation occurred |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/recommendation/invalid/invalid_1.json) | Rejection of one missing `recommendation_id` | Exhaustive rejection of bad identities, references, times, amounts, relationships, or event collapse |
| [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) and [tests](../../../tests/domains/water_planning/test_status_collapse.py) | Synthetic no-network rejection of application/recommendation and recommendation/award collapse, plus distinct amount keys | Validation of Recommendation instances, source support, reference integrity, or amount semantics |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only schema inventory, meta-schema, configured fixture checks, and repository-owned schema/contract tests for every pull request | Semantic truth, source admission, rights or sensitivity clearance, release, deployment, or publication |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Triggers on this contract path and runs no-network water-planning domain tests plus the RAC registry validator | Validation of the Recommendation schema fixture pair; this workflow does not invoke the schema pytest suite |

> [!NOTE]
> A green test, check, or badge is evidence only for the tested revision and boundary. It is not a recommendation record, source receipt, `EvidenceBundle`, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Rights, sensitivity, and release

- Do not place authenticated grant-portal content, unpublished applications, scores, reviewer notes, deliberative material, personal information, restricted infrastructure details, or credentials in this semantic-contract lane.
- A public meeting, agenda, score, ranking, staff document, or recipient list must not be converted into a recommendation without source evidence that supports the specific event and fields.
- Public KWO pages and grant documents remain subject to source identity, rights, attribution, freshness, correction, and field-level evidence review.
- Applicant, reviewer, recipient, amount, project, and location information must be minimized, generalized, quarantined, staged, or denied where authority or sensitivity is unresolved.
- Recommendation facts intended for public use require evidence, rights and sensitivity closure, policy, validation, review, correction, release, and rollback decisions from their owning surfaces.
- Public clients and ordinary UI, map, search, graph, export, and AI surfaces may consume only governed, release-approved public-safe carriers, not this contract lane or internal canonical stores directly.

A commit, pull request, merge, schema pass, fixture pass, or recommendation-shaped record is not a KFM promotion or publication event.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
|---|---|---|
| `WP-REC-01` | `NEEDS VERIFICATION` | Define `recommendation_id` issuance, namespace ownership, uniqueness, deduplication, amendment, supersession, and correction behavior. |
| `WP-REC-02` | `NEEDS VERIFICATION` | Resolve `application_ref` and `eligibility_decision_ref` to governed object types, versions, and lineage; prevent empty, self-incompatible, or cross-application relationships. |
| `WP-REC-03` | `NEEDS VERIFICATION` | Model the recommending authority, body, role, action, quorum or adoption posture, and source-native terminology without converting discussion into a recommendation. |
| `WP-REC-04` | `NEEDS VERIFICATION` | Define recommendation states and outcomes, including no-recommendation, partial, conditional, ranked, amended, withdrawn, superseded, and declined cases. |
| `WP-REC-05` | `NEEDS VERIFICATION` | Define currency, scale, precision, rounding, zero, omission, `null`, matching-fund, total-cost, partial-funding, and maximum-amount semantics. |
| `WP-REC-06` | `NEEDS VERIFICATION` | Define the authoritative meaning of `recommended_at`, preserve source-publication and retrieval times separately, and decide whether date-time format must be machine-enforced. |
| `WP-REC-07` | `NEEDS VERIFICATION` | Define how a recommendation relates to the applicable `ProgramVersion`, `ScoringMatrixVersion`, score, rank, rationale, and eligibility result without collapsing those records. |
| `WP-REC-08` | `NEEDS VERIFICATION` | Define field-level support and the resolution path from `source_ref` through `EvidenceRef` to an admitted `EvidenceBundle`, including freshness and correction state. |
| `WP-REC-09` | `NEEDS VERIFICATION` | Add targeted negative tests for identifier patterns, empty references, malformed timestamps, amount states, relationship coherence, and event-type discrimination. |
| `WP-REC-10` | `NEEDS VERIFICATION` | Complete rights, sensitivity, deliberative-record, applicant-exposure, and public-safe release review for any real recommendation source family. |

Until these items close, preserve unresolved states, narrow claims, and do not infer eligibility, recommending authority, score, rank, currency, formal award, payment, recipient, project state, completion, operational benefit, or public eligibility from a Recommendation record.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- field names, requiredness, patterns, nullability, formats, or `additionalProperties`;
- Recommendation identity, application and eligibility relationship semantics, or event classification;
- recommended-amount currency, scale, precision, zero, omission, `null`, or relationship to other amount facts;
- recommendation time, source-publication time, retrieval time, correction, and supersession semantics;
- recommending authority, rationale, scoring, ranking, condition, status, or outcome behavior;
- source and evidence reference meaning; and
- rights, sensitivity, policy, public-safe projection, correction, release, or publication behavior.

Preserve `doc_id: kfm://doc/contracts-domains-water-planning-recommendation`, the v0.1 identity, and existing property names while this contract remains in force. Because `additionalProperties: false` rejects unknown fields, an additive machine-shape change requires coordinated contract, schema, fixture, test, and consumer review.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, targeted tests, known consumers, and correction lineage within one authorized review boundary. Use [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) or another governed correction surface where applicable; do not silently rewrite a relied-on historical recommendation or repurpose an Award as its replacement.

This documentation revision clarifies the existing v0.1 shape and tested boundaries. It does not change schema fields, fixture bytes, validator behavior, source admission, policy, release state, or publication state.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository documentation bytes; it does not undo an external recommendation, eligibility decision, award, payment, source observation, release state, or publication history.

[Back to top](#top)

## Related

| Surface | Role |
|---|---|
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`advisory_committee_meeting.md`](./advisory_committee_meeting.md) | Separate RAC advisory-meeting event contract; a meeting is not a recommendation. |
| [`application.md`](./application.md) | Separate submitted-request record and owner of `requested_amount`. |
| [`eligibility_decision.md`](./eligibility_decision.md) | Separate application-specific eligibility determination. |
| [`scoring_matrix_version.md`](./scoring_matrix_version.md) | Separate scoring-artifact identity and digest lineage. |
| [`award.md`](./award.md) | Separate formal award event and owner of `awarded_amount`. |
| [`funding_agreement.md`](./funding_agreement.md) | Separate agreement and `paid_amount` semantics. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | Separate correction and withdrawal lineage envelope. |
| [`recommendation.schema.json`](../../../schemas/contracts/v1/domains/water_planning/recommendation.schema.json) | Canonical machine shape for this proposed record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic Recommendation fixtures](../../../fixtures/domains/water_planning/recommendation/) | Representative valid and invalid schema inputs. |
| [Synthetic status-collapse fixtures](../../../fixtures/domains/water_planning/status_collapse/) | Cross-entity and amount-separation guardrail inputs. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family and amount-ownership regression tests. |
| [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) | Deterministic synthetic anti-collapse validator. |
| [`test_status_collapse.py`](../../../tests/domains/water_planning/test_status_collapse.py) | No-network semantic guardrail tests. |
| [`jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) | Shared Draft 2020-12 validator construction used by the schema tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, exclusions, rights posture, and open verification items. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only pull-request schema and contract validation workflow. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only, path-triggered water-planning validation workflow. |

[Back to top](#top)
