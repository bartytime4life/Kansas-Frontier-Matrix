<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-funding-agreement
title: FundingAgreement Contract — Water Planning
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
  - ./project.md
  - ./construction_milestone.md
  - ./completion.md
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/funding_agreement.schema.json
  - ../../../schemas/contracts/v1/domains/water_planning/README.md
  - ../../../fixtures/domains/water_planning/funding_agreement/
  - ../../../fixtures/domains/water_planning/status_collapse/
  - ../../../tools/validators/domains/water_planning/validate_status_collapse.py
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../tests/domains/water_planning/test_status_collapse.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FundingAgreement Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/funding_agreement.schema.json)
[![Water-planning checks](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml/badge.svg?branch=main)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml)

Defines the semantic meaning, paid-amount boundary, and fail-closed interpretation of a water-planning funding-agreement record.

> [!IMPORTANT]
> This document and its paired schema are `PROPOSED` scaffolds. They do not prove that an agreement was executed or remains effective, that an award exists, that money was transferred or spent, that a project or construction activity exists, that work was completed, that an operational benefit occurred, or that a record is policy-approved, released, or KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Agreement, payment, and evidence invariants](#agreement-payment-and-evidence-invariants)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Rights, sensitivity, and release](#rights-sensitivity-and-release)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

A `FundingAgreement` represents one source-attributed agreement record associated with an [`Award`](./award.md). The record separates:

- agreement-record identity from award identity;
- a reference-shaped award relationship from proof that the award exists or supports the agreement;
- a fiscal-year label from program-version, appropriation, and agreement-term authority;
- the agreement's optional effective date from award, payment, source-publication, retrieval, and project-event times;
- a source-stated `paid_amount` from requested, recommended, awarded, expended, construction, completion, and benefit facts; and
- a source pointer from field-level evidence, rights, review, policy, release, and publication authority.

The required `award_ref` expresses an intended relationship to an award. Its non-empty string shape does not establish referential integrity, amount consistency, recipient identity, agreement eligibility, or legal effect.

The optional `paid_amount` can carry a non-negative source-stated amount or `null`. A numeric value is not a payment transaction, bank record, receipt, proof of transfer, expenditure, or project outcome. `null` means the amount is not publicly disclosed under the schema description; it must not be converted to zero or interpreted as unpaid. The meaning of an omitted `paid_amount` remains unspecified.

This contract defines record meaning. The paired JSON Schema defines accepted document shape. Source admission, agreement-document identity, award resolution, payment evidence, rights and sensitivity review, policy decisions, correction, release, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
|---|---|---|
| This document | `draft`; `PROPOSED`; v0.1 | Defines semantic meaning and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/funding_agreement.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not source truth, legal effect, payment proof, or policy. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/funding_agreement/) | Synthetic test inputs | Exercise representative schema acceptance and rejection; they are not agreements or payment evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check representative fixture polarity, distinct entity titles, and separation of requested, recommended, awarded, and paid amount fields. |
| [Status-collapse validator](../../../tools/validators/domains/water_planning/validate_status_collapse.py) and [tests](../../../tests/domains/water_planning/test_status_collapse.py) | Deterministic, no-network synthetic-fixture checks | Reject selected award/payment and payment/construction collapses and a generic collapsed amount field; they do not validate a `FundingAgreement` instance. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Separates awarded and paid amounts and excludes unsupported payment, completion, and benefit inferences; it does not activate a connector or authorize release. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; the policy lane is not established | No policy outcome or public-safe projection may be inferred from this contract or schema. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
|---|---:|---|---|
| `agreement_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Funding-agreement record identity. Generation, deduplication, document-version binding, and correction lineage remain unspecified. |
| `award_ref` | Yes | Non-empty string | Reference-shaped relationship to an `Award`; target existence, type, version, and amount consistency are not encoded. |
| `fiscal_year` | Yes | String matching `^FY[0-9]{4}$` | Source-facing fiscal-year label. It does not establish a program version, appropriation period, agreement term, or payment period by itself. |
| `paid_amount` | No | Number greater than or equal to zero, or `null` | Source-stated amount paid under the agreement when disclosed; not an award, transaction ledger, expenditure, construction, completion, or benefit fact. |
| `effective_date` | No | String annotated as `date`, or `null` | Agreement-related effective date when recorded. Execution, signature, amendment, termination, and payment-time semantics are not defined. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not, by itself, an `EvidenceRef`, `EvidenceBundle`, receipt, proof, review, policy decision, or release authorization. |

No additional properties are admitted by the current schema.

[Back to top](#top)

## Agreement, payment, and evidence invariants

The semantic posture is fail closed:

- an agreement record does not prove execution, signatures, legal enforceability, current effect, amendment state, termination state, or remaining obligations;
- `award_ref` remains a reference whose existence, version, and relationship to the agreement require validation beyond string shape;
- `paid_amount` records only the source-stated paid-amount fact and must not absorb requested, recommended, awarded, expended, construction, completion, operational, or benefit meaning;
- `paid_amount: null` preserves nondisclosure and must not be treated as zero, unpaid, unknown award value, or a failed payment;
- an omitted `paid_amount` must remain unresolved until omission semantics are defined;
- a numeric `paid_amount` is non-negative under the schema, but currency, precision, cumulative-versus-transaction scope, payment schedule, amendment handling, and cross-record consistency are not encoded;
- `effective_date` remains distinct from award, signature, payment, source-publication, retrieval, construction, completion, correction, release, and publication times;
- `fiscal_year` remains a label and must not be used as a substitute for program-version, appropriation, agreement-term, or payment-period authority; and
- `source_ref` must remain a pointer whose field-level support, rights, sensitivity, freshness, correction, and provenance are resolved through their owning governance surfaces.

> [!WARNING]
> The paired schema annotates `effective_date` with `format: date`, but the shared validator constructs `Draft202012Validator` without an explicit format checker. Date syntax must not be described as machine-enforced by the current repository test path.

Real agreement documents, award records, payment data, recipient identities, project details, and funding-source facts require independent identity, source, rights, sensitivity, evidence, policy, review, correction, and release decisions. A `public-with-gates` label is not public-release authorization.

[Back to top](#top)

## Anti-collapse boundaries

A funding agreement is an agreement record, not an award, payment transaction, project, construction event, completion record, or outcome claim. Every related fact requires its own identity, source support, evidence, and governed state.

| Boundary | Required interpretation |
|---|---|
| Funding agreement != award | [`Award`](./award.md) records a funding decision and owns `awarded_amount`; an agreement does not create or replace that decision. |
| Award != payment | `awarded_amount` authorizes or records an award fact only; it does not prove that funds were transferred. |
| Paid amount != awarded amount | `paid_amount` and `awarded_amount` are separate facts. Equality, ordering, or a remaining balance is not enforced by this schema. |
| Paid amount != payment transaction | A numeric aggregate or source-stated amount is not a transfer event, receipt, bank record, or payment ledger. |
| Payment != expenditure | A paid amount does not prove how, when, or whether funds were spent for an eligible purpose. |
| Funding agreement != project | [`Project`](./project.md) is a separate award-linked delivery record; an agreement does not prove project identity, location, or activity. |
| Payment != construction | [`ConstructionMilestone`](./construction_milestone.md) requires separate event evidence; disbursement does not prove physical progress. |
| Payment != completion | [`Completion`](./completion.md) has a separate state and schema; payment does not prove completed work. |
| Completion != operational benefit | Agreement, payment, construction, and completion facts do not establish service, impact, effectiveness, or public benefit. |
| Effective date != execution or payment time | A date-shaped value does not prove signatures, legal effect, a transfer event, or source-publication timing. |
| Fiscal year != program or agreement version | A pattern-valid label does not resolve statutory basis, agreement revision, appropriation, or supersession lineage. |
| Source reference != evidence closure | A non-empty `source_ref` does not establish field-level support, rights, sensitivity, freshness, review, or publication. |
| Schema-valid != true or public-safe | Structural acceptance does not establish real-world correctness, policy approval, release, or KFM publication. |

### Amount semantics

| Fact | Owning entity | What it does not prove |
|---|---|---|
| `requested_amount` | [`Application`](./application.md) | Recommendation, award, agreement, or payment |
| `recommended_amount` | [`Recommendation`](./recommendation.md) | Award or disbursement |
| `awarded_amount` | [`Award`](./award.md) | Agreement execution, payment, expenditure, construction, completion, or benefit |
| `paid_amount` | `FundingAgreement` | Payment transaction detail, expenditure, construction, completion, or operational benefit |

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
|---|---|---|
| Canonical machine-shape file | [`funding_agreement.schema.json`](../../../schemas/contracts/v1/domains/water_planning/funding_agreement.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Properties | 6 | The shape is a bounded agreement envelope, not an agreement document, payment ledger, or release record. |
| Required fields | 4 of 6 | `paid_amount` and `effective_date` may be absent; each also admits `null`. |
| Unknown fields | Rejected by `additionalProperties: false` | Adding agreement status, document identity, payment events, currency, evidence, or correction fields requires coordinated review. |
| Award linkage | Non-empty string only | Referenced-record existence, version, type, amount consistency, and lineage are not enforced. |
| Amount constraint | Non-negative number or `null` | Currency, precision, cumulative scope, transaction identity, schedule, and cross-record checks are not encoded. |
| Effective-date assertion | Annotated as `format: date` | The shared validator supplies no explicit format checker, so syntax enforcement remains `NEEDS VERIFICATION`. |
| Cross-field behavior | No conditional or referential rules | The schema does not condition amount or effective date on agreement state, award state, source evidence, or payment events. |
| Evidence and release closure | Not encoded | `source_ref` and schema validity do not establish support, rights, policy, review, release, or publication. |

The contract and schema must remain synchronized: prose cannot loosen or tighten machine behavior without a coordinated schema change.

[Back to top](#top)

## Synthetic example

The checked-in valid fixture is synthetic and test-only. It must not be cited as evidence that an award, agreement, recipient, payment, project, or source record exists.

```json
{
  "agreement_id": "kwo-swigp-fy2027-agr-synthetic-001",
  "award_ref": "kwo-swigp-fy2027-award-synthetic-001",
  "fiscal_year": "FY2027",
  "paid_amount": null,
  "effective_date": null,
  "source_ref": "kwo:grant-programs:swigp:fy2027:agreement:synthetic-001"
}
```

The example preserves nondisclosure with `paid_amount: null` and does not assert an effective date. The paired invalid fixture uses `paid_amount: -1`; the schema test expects that record to be rejected by the non-negative amount constraint.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Run the focused funding-agreement fixture checks

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py -k funding_agreement
```

### Validate the complete water-planning entity schema family

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

### Exercise the synthetic amount and status boundaries

```bash
python tools/validators/domains/water_planning/validate_status_collapse.py \
  fixtures/domains/water_planning/status_collapse/valid/valid_1.json

python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_status_collapse.py' \
  --verbose
```

| Validation surface | What it checks | What success does not prove |
|---|---|---|
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct entity titles, one representative valid/invalid fixture pair, and separate amount fields across application, recommendation, award, and funding agreement | Award resolution, agreement execution, date syntax, payment evidence, currency, rights, policy, or release |
| [`valid_1.json`](../../../fixtures/domains/water_planning/funding_agreement/valid/valid_1.json) | One synthetic shape with required identity, award reference, fiscal year, source reference, and null amount/date | That an award or agreement exists, that no payment occurred, or that the record is source-supported |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/funding_agreement/invalid/invalid_1.json) | Rejection of one negative `paid_amount` | Exhaustive negative coverage for identifiers, references, fiscal year, dates, non-finite values, currency, or payment semantics |
| [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) | A synthetic no-network envelope rejects award-as-payment, payment-as-construction, and a generic collapsed amount field while retaining four distinct amount keys | Validation of a `FundingAgreement`, a real payment, or cross-record amount consistency |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only pull-request and `main` schema inventory, meta-schema, fixture, and repository-owned schema/contract checks | Semantic truth, source admission, payment proof, rights, sensitivity, policy, release, or publication |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Path-triggered, read-only, no-network water-planning semantic and registry checks | Funding-agreement schema exhaustiveness, review approval, evidence closure, release, deployment, or publication |

> [!NOTE]
> A green test or workflow result is validation evidence only within the tested boundary. It is not a payment receipt, EvidenceBundle, legal determination, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Rights, sensitivity, and release

- Do not place credentials, authenticated portal content, bank or payment-account data, private applicant or recipient material, personal signatory details, or restricted infrastructure information in this semantic-contract lane.
- Public KWO pages and document locators remain subject to source-specific rights, attribution, freshness, and correction review.
- Agreement documents, recipient identities, paid amounts, payment dates, schedules, amendments, signatures, and project details require field-level evidence and public-safe projection decisions before exposure.
- A public record of an award or aggregate payment does not authorize release of an agreement document, transaction detail, applicant material, precise infrastructure location, or another linked record.
- Public clients and ordinary UI, map, export, search, graph, and AI surfaces may consume only governed, release-approved public-safe carriers, not this contract lane or internal canonical stores directly.

A commit, pull request, merge, badge, schema pass, validator pass, or agreement-shaped record is not a KFM promotion or publication event.

[Back to top](#top)

## Known limits and verification backlog

| Item | Status | Verification needed |
|---|---|---|
| Agreement identity and versioning | `NEEDS VERIFICATION` | Define `agreement_id` generation, deduplication, document binding, amendment, supersession, termination, and correction-lineage behavior. |
| Award referential integrity | `NEEDS VERIFICATION` | Resolve `award_ref` to the intended governed award and define behavior for missing, withdrawn, corrected, or superseded targets. |
| Agreement state and legal posture | `NEEDS VERIFICATION` | Define proposed, executed, effective, amended, suspended, terminated, expired, and unknown states without turning schema shape into a legal conclusion. |
| Agreement document authority | `NEEDS VERIFICATION` | Define title, version, digest, signatory-role, source-publication, retrieval, and correction references without embedding restricted document content. |
| Paid-amount scope | `NEEDS VERIFICATION` | Decide whether `paid_amount` is cumulative, period-specific, latest-reported, or another source-defined aggregate and how revisions are retained. |
| Payment events and receipts | `NEEDS VERIFICATION` | Determine whether transaction-level disbursement requires a separate event family; do not treat this aggregate field as a ledger or proof of transfer. |
| Currency and precision | `NEEDS VERIFICATION` | Define currency, units, decimal precision, rounding, matching funds, caps, and cross-record amount comparison. |
| Effective-date semantics | `NEEDS VERIFICATION` | Define omission, `null`, and non-null meaning and distinguish execution, signature, effective, amendment, termination, and payment times. |
| Format and negative coverage | `NEEDS VERIFICATION` | Decide whether to enable date format checking and add representative cases for empty or whitespace references, malformed dates, non-finite amounts, missing optionals, and unknown fields. |
| Evidence, rights, and public projection | `NEEDS VERIFICATION` | Define how `source_ref` resolves to field-level evidence and establish finite policy outcomes for agreement, recipient, payment, portal, and infrastructure data. |

Until these items are resolved, preserve nullable and omitted states, narrow claims, and do not infer award validity, agreement execution, payment occurrence, expenditure, construction, completion, operational benefit, or public eligibility.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- field names, requiredness, patterns, nullability, numeric bounds, or `additionalProperties`;
- agreement, award-reference, fiscal-year, paid-amount, effective-date, and source-reference meaning;
- agreement identity, document binding, amendment, supersession, termination, or correction behavior;
- payment-event, currency, precision, cumulative-total, or cross-record consistency rules;
- date-format enforcement, reference resolution, evidence, rights, sensitivity, policy, or public-safe projection; and
- any consumer rule that distinguishes unknown, undisclosed, unpaid, partially paid, fully paid, corrected, or withdrawn state.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, tests, known consumers, and correction lineage within one authorized review boundary. Use [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) or another governed correction surface when applicable; do not silently rewrite a relied-on agreement or payment fact.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository bytes; it does not erase an agreement, payment history, source observation, downstream reliance, release state, or publication history.

[Back to top](#top)

## Related

| Surface | Role |
|---|---|
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`award.md`](./award.md) | Separate award decision and `awarded_amount` fact. |
| [`project.md`](./project.md) | Separate award-linked delivery identity and reference states. |
| [`construction_milestone.md`](./construction_milestone.md) | Separate construction-progress event. |
| [`completion.md`](./completion.md) | Separate completion state; payment does not prove completion or benefit. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | Separate correction and withdrawal lineage envelope. |
| [`funding_agreement.schema.json`](../../../schemas/contracts/v1/domains/water_planning/funding_agreement.schema.json) | Canonical machine shape for this proposed record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic funding-agreement fixtures](../../../fixtures/domains/water_planning/funding_agreement/) | Representative valid and invalid schema inputs. |
| [Synthetic status-collapse fixtures](../../../fixtures/domains/water_planning/status_collapse/) | Cross-entity amount and event-separation envelopes. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family regression tests. |
| [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) | Deterministic synthetic amount and status-collapse validator. |
| [`test_status_collapse.py`](../../../tests/domains/water_planning/test_status_collapse.py) | No-network validator regression tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, amount separation, rights, and admission limitations. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only pull-request schema and contract validation workflow. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only, path-triggered water-planning validation workflow. |

[Back to top](#top)
