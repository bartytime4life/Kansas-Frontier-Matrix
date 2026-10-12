<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-application
title: Application Contract — Water Planning
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
  - ./application_window.md
  - ./recommendation.md
  - ./award.md
  - ./funding_agreement.md
  - ./project.md
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/application.schema.json
  - ../../../fixtures/domains/water_planning/application/
  - ../../../fixtures/domains/water_planning/status_collapse/
  - ../../../tools/validators/domains/water_planning/validate_status_collapse.py
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../tests/domains/water_planning/test_status_collapse.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Application Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/application.schema.json)

Defines the semantic meaning, unresolved-state posture, and anti-collapse boundaries of a water-planning grant application record.

> [!IMPORTANT]
> This document and its paired schema are `PROPOSED` scaffolds. They do not prove that an application was submitted, admit a source, authorize access to an applicant portal, establish an applicant's identity, recommend or award funding, approve policy or promotion, or make a record KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Resolution and evidence invariants](#resolution-and-evidence-invariants)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

An `Application` represents one grant request associated with an [`ApplicationWindow`](./application_window.md). The record separates:

- application identity from applicant identity;
- the application-window reference from submission or source-publication time;
- the requested amount from recommended, awarded, and paid amounts;
- applicant-resolution state from an applicant reference;
- project-location reference from geometry confidence; and
- a source pointer from evidence, review, policy, release, and publication authority.

The required `window_ref` expresses an intended relationship to an application window. Its non-empty string shape does not prove that the referenced window exists, that submission occurred inside the window, or that a submission timestamp was captured.

The contract describes record meaning. The paired JSON Schema defines accepted document shape. Source admission, field-level evidence resolution, identity resolution, rights and sensitivity review, policy decisions, correction, release, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
|---|---|---|
| This document | `draft`; `PROPOSED`; v0.1 | Defines semantic meaning and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/application.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not source truth, identity resolution, or policy. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/application/) | Synthetic test inputs | Exercise representative schema behavior; they are not applications or applicant evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check representative acceptance, rejection, explicit unresolved applicant identity, and amount separation. |
| [Status-collapse validator](../../../tools/validators/domains/water_planning/validate_status_collapse.py) and [tests](../../../tests/domains/water_planning/test_status_collapse.py) | Deterministic, no-network synthetic-fixture checks | Reject selected application/recommendation/award collapses and guessed states; they do not validate live application records. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Excludes authenticated portal content and non-public application data; it does not activate a connector or authorize release. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; policy behavior remains `NEEDS VERIFICATION` | No policy outcome may be inferred from this contract or schema. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
|---|---:|---|---|
| `application_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Application-record identity. Generation, deduplication, and version-lineage rules remain unspecified. |
| `window_ref` | Yes | Non-empty string | Reference-shaped relationship to an `ApplicationWindow`; referential integrity and submission-within-window checks are not encoded. |
| `applicant_ref` | Yes | String or `null` | Applicant-identity reference when resolved; `null` preserves an explicit missing identity. |
| `applicant_resolution_status` | Yes | `resolved`, `unresolved`, or `pending` | Identity-resolution state. The current schema does not condition this value on `applicant_ref`. |
| `requested_amount` | No | Number greater than or equal to zero, or `null` | Amount requested as stated by the source when disclosed; not a recommendation, award, or payment. Currency semantics remain unspecified. |
| `project_location_ref` | No | String or `null` | Reference-shaped project-location pointer when available; inline geometry is not part of this record shape. |
| `geometry_confidence` | Yes | `unresolved`, `approximate`, or `confirmed` | Geometry-resolution confidence. The current schema does not condition this value on `project_location_ref`. |
| `source_publication_time` | No | `date-time` string or `null` | Source-publication time when recorded; not the application submission time or retrieval time. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not, by itself, an `EvidenceBundle`, receipt, proof, review, or release authorization. |

No additional properties are admitted by the current schema.

[Back to top](#top)

## Resolution and evidence invariants

The semantic posture is fail closed:

- missing applicant identity remains `applicant_ref: null` with `applicant_resolution_status: unresolved`; it is never guessed from names, addresses, project prose, or another record;
- missing or unverified project geometry remains `geometry_confidence: unresolved`; it is never inferred from an applicant address, county, recipient, planning region, venue, centroid, containment, or proximity;
- `requested_amount` records only the requested fact and must not absorb recommended, awarded, agreed, paid, expended, construction, completion, or benefit meaning;
- `source_publication_time`, when present, remains distinct from submission, retrieval, effective, decision, award, and payment times; and
- `source_ref` must remain a pointer whose evidence, rights, sensitivity, freshness, and field-level support are resolved through their owning governance surfaces.

> [!WARNING]
> The paired schema currently enumerates applicant and geometry states but does not enforce reference/state coherence with conditional rules. Semantic requirements must not be described as machine-enforced until the schema, fixtures, and tests prove that behavior.

Real applicant identities, application materials, review notes, scores, authenticated portal content, and unpublished organization data require independent access, rights, privacy, sensitivity, and release decisions. A `public-with-gates` label is not public-release authorization.

[Back to top](#top)

## Anti-collapse boundaries

An application is not a recommendation, award, payment, or project. Each downstream event or delivery record requires its own identity, source support, evidence, and governed state.

| Boundary | Required interpretation |
|---|---|
| Application != application window | [`ApplicationWindow`](./application_window.md) defines an intake interval; an `Application` is a request associated with that interval. |
| Application != recommendation | [`Recommendation`](./recommendation.md) is a later advisory fact with its own amount and evidence. |
| Application != award | [`Award`](./award.md) is a formal funding decision; an application does not prove that an award exists. |
| Application != payment | Paid-amount meaning belongs to [`FundingAgreement`](./funding_agreement.md); a request or award does not prove disbursement. |
| Application != project | [`Project`](./project.md) is an award-linked delivery record; an application does not prove project creation, construction, completion, or benefit. |
| Applicant reference != identity proof | A string-shaped `applicant_ref` does not establish referential integrity, correct entity resolution, or public eligibility. |
| Window reference != timely submission | A non-empty `window_ref` does not prove that a submission occurred or fell inside the referenced interval. |
| Location reference != geometry proof | `project_location_ref` and `geometry_confidence` do not replace a declared geometry authority, digest, lineage, or correction posture. |
| Source reference != evidence closure | A non-empty `source_ref` does not establish field-level support, rights, sensitivity, freshness, review, or publication. |
| Schema-valid != true or public-safe | Structural acceptance does not establish real-world correctness, policy approval, release, or KFM publication. |

### Amount semantics

| Fact | Owning entity | What it does not prove |
|---|---|---|
| `requested_amount` | `Application` | Recommendation, award, agreement, or payment |
| `recommended_amount` | [`Recommendation`](./recommendation.md) | Award or disbursement |
| `awarded_amount` | [`Award`](./award.md) | Payment, expenditure, construction, completion, or benefit |
| `paid_amount` | [`FundingAgreement`](./funding_agreement.md) | Expenditure, completion, or operational benefit |

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
|---|---|---|
| Canonical machine-shape file | [`application.schema.json`](../../../schemas/contracts/v1/domains/water_planning/application.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Required fields | 6 of 9 properties | Optional fields may be absent; nullable fields may explicitly carry `null`. |
| Unknown fields | Rejected by `additionalProperties: false` | Widening the record requires coordinated contract, schema, fixture, and test review. |
| Applicant-reference coherence | Not conditionally enforced | `resolved` can currently coexist with `applicant_ref: null`, and `unresolved` can coexist with a string reference. |
| Geometry-reference coherence | Not conditionally enforced | `approximate` or `confirmed` can currently appear without `project_location_ref`; `unresolved` can coexist with a reference. |
| Date-time assertion | Annotated on `source_publication_time` | The shared validator constructs `Draft202012Validator` without an explicit format checker, so syntax enforcement remains `NEEDS VERIFICATION`. |

The contract and schema must remain synchronized: prose cannot loosen or tighten machine behavior without a coordinated schema change.

[Back to top](#top)

## Synthetic example

The checked-in valid fixture is synthetic and test-only. It must not be cited as evidence that an application, applicant, amount, or project exists.

```json
{
  "application_id": "kwo-swigp-fy2027-app-synthetic-001",
  "window_ref": "kwo-swigp-fy2027-window",
  "applicant_ref": null,
  "applicant_resolution_status": "unresolved",
  "requested_amount": null,
  "project_location_ref": null,
  "geometry_confidence": "unresolved",
  "source_publication_time": null,
  "source_ref": "kwo:grant-programs:swigp:fy2027:app:synthetic-001"
}
```

The paired invalid fixture uses `applicant_resolution_status: unknown`; the schema test expects that record to be rejected because `unknown` is not an admitted enum value.

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
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct entity titles, representative valid/invalid fixtures, explicit unresolved applicant identity, and amount-field separation | Reference/state coherence, submission timing, source accuracy, applicant identity, rights, policy, or release |
| [`valid_1.json`](../../../fixtures/domains/water_planning/application/valid/valid_1.json) | One representative unresolved-state shape accepted by the paired schema | That the example is real, current, complete, or source-supported |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/application/invalid/invalid_1.json) | An unrecognized applicant-resolution enum is rejected | Exhaustive negative coverage for identity, geometry, time, references, or amount semantics |
| [`test_status_collapse.py`](../../../tests/domains/water_planning/test_status_collapse.py) | Stable findings for synthetic application/recommendation/award collapse, guessed resolution, blocked live behavior, no-network execution, and protected-value non-echo | Validation of an `Application` instance or evidence for a real applicant, request, award, project, or payment |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Pull-request schema inventory, meta-schema checks, aggregate fixtures, and repository-owned schema/contract tests under read-only permissions | Semantic truth, source admission, policy, rights, sensitivity, release, or publication |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Path-triggered no-network water-planning domain and RAC-registry checks under `contents: read` | Application-schema exhaustiveness, review approval, evidence closure, release, deployment, or publication |

> [!NOTE]
> A green test or workflow result is validation evidence only within the tested boundary. It is not a source receipt, identity decision, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
|---|---|---|
| `WP-APP-01` | `NEEDS VERIFICATION` | Define submission-time representation and validate that an application falls within the referenced `ApplicationWindow`; `source_publication_time` is not submission time. |
| `WP-APP-02` | `NEEDS VERIFICATION` | Add or identify deterministic referential-integrity validation from `window_ref` to a governed application-window record. |
| `WP-APP-03` | `NEEDS VERIFICATION` | Define and enforce coherence between `applicant_ref` and `applicant_resolution_status`, including the meaning and allowed transitions of `pending`. |
| `WP-APP-04` | `NEEDS VERIFICATION` | Define and enforce coherence between `project_location_ref` and `geometry_confidence` without introducing inline or inferred geometry. |
| `WP-APP-05` | `NEEDS VERIFICATION` | Decide whether `date-time` annotations require an explicit format checker in the shared schema runner. |
| `WP-APP-06` | `NEEDS VERIFICATION` | Define `application_id` generation, deduplication, versioning, correction, withdrawal, and supersession behavior. |
| `WP-APP-07` | `NEEDS VERIFICATION` | Define currency and unit semantics for `requested_amount` without collapsing later amount facts. |
| `WP-APP-08` | `NEEDS VERIFICATION` | Define how `source_ref` resolves to field-level evidence and how retrieval, correction, and supersession times are retained. |
| `WP-APP-09` | `NEEDS VERIFICATION` | Establish finite policy outcomes and public-safe projection rules for applicant identity, application materials, review data, and authenticated portal content. |

Until these items are resolved, narrow claims, preserve explicit unknowns, and do not infer applicant identity, timely submission, geometry, recommendation, award, payment, project delivery, or public eligibility.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- field names, requiredness, enums, patterns, nullable behavior, or `additionalProperties`;
- application, applicant, window, location, source, time, and amount semantics;
- reference/state coherence or referential-integrity rules;
- identity, deduplication, correction, withdrawal, and supersession behavior; and
- any public-safe projection or policy outcome.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, tests, known consumers, and correction lineage within one authorized review boundary. Use [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) or another governed correction surface when applicable; do not silently rewrite a relied-on historical application.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository bytes; it does not erase source history, applicant records, downstream reliance, or publication state.

[Back to top](#top)

## Related

| Surface | Role |
|---|---|
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`application_window.md`](./application_window.md) | Meaning of the referenced application-window entity. |
| [`recommendation.md`](./recommendation.md) | Separate recommendation event and amount fact. |
| [`award.md`](./award.md) | Separate award decision and amount fact. |
| [`funding_agreement.md`](./funding_agreement.md) | Agreement and paid-amount meaning. |
| [`project.md`](./project.md) | Separate award-linked project and geometry-reference contract. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | Domain correction and withdrawal event contract. |
| [`application.schema.json`](../../../schemas/contracts/v1/domains/water_planning/application.schema.json) | Canonical machine shape for this record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic application fixtures](../../../fixtures/domains/water_planning/application/) | Representative valid and invalid inputs. |
| [Synthetic status-collapse fixtures](../../../fixtures/domains/water_planning/status_collapse/) | Cross-entity negative and fail-closed envelopes. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family regression tests. |
| [`validate_status_collapse.py`](../../../tools/validators/domains/water_planning/validate_status_collapse.py) | Deterministic synthetic anti-collapse validator. |
| [`test_status_collapse.py`](../../../tests/domains/water_planning/test_status_collapse.py) | No-network validator regression tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, rights, freshness, access, and admission limitations. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only schema and contract validation workflow. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only path-triggered water-planning validation workflow. |

[Back to top](#top)
