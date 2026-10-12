<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-eligibility-decision
title: EligibilityDecision Contract — Water Planning
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
  - ./program_version.md
  - ./scoring_matrix_version.md
  - ./recommendation.md
  - ./award.md
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json
  - ../../../fixtures/domains/water_planning/eligibility_decision/
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../tools/validators/_common/jsonschema_runner.py
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EligibilityDecision Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json)

Defines the semantic meaning, finite outcome posture, evidence boundary, and anti-collapse rules of a water-planning grant eligibility decision.

> [!IMPORTANT]
> This document and its paired schema are `PROPOSED` scaffolds. They do not prove that an application or program version exists, establish legal or policy eligibility, admit adjudication records, authorize access to an authenticated grant portal, recommend or award funding, approve a project, or make a record KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Decision and evidence invariants](#decision-and-evidence-invariants)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Rights, sensitivity, and release](#rights-sensitivity-and-release)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

An `EligibilityDecision` represents one recorded determination about whether a referenced [`Application`](./application.md) satisfies the eligibility basis associated with a referenced [`ProgramVersion`](./program_version.md).

The contract preserves these distinctions:

- decision identity is separate from application and program-version identity;
- `eligible`, `ineligible`, and `pending` are eligibility outcomes only;
- an eligibility outcome is separate from scoring, recommendation, award, payment, project approval, construction, completion, and benefit;
- the recorded decision time is separate from application, source-publication, retrieval, recommendation, and award times;
- a basis pointer is separate from the policy, statute, scoring artifact, or evidence to which it may resolve; and
- a source pointer is separate from an `EvidenceBundle`, review record, policy decision, release decision, or publication proof.

`pending` preserves an outcome that is not represented as `eligible` or `ineligible`. The current schema does not define whether it is provisional, incomplete, under review, appealable, or terminal, and it does not encode allowed outcome transitions.

The contract defines record meaning. The paired JSON Schema defines accepted document shape. Referential integrity, source admission, field-level evidence, legal interpretation, policy execution, rights and sensitivity review, correction, release, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
|---|---|---|
| This document | `draft`; `PROPOSED`; v0.1 | Defines semantic meaning, finite outcomes, and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not source truth, legal eligibility, referential integrity, or policy. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/eligibility_decision/) | Synthetic test inputs | Exercise one accepted shape and one rejected outcome; they are not applications, decisions, or adjudication evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check schema presence, distinct entity titles, representative valid-fixture acceptance, and invalid-fixture rejection. |
| [Shared schema runner](../../../tools/validators/_common/jsonschema_runner.py) | Uses `Draft202012Validator` with the repository registry | Does not install an explicit format checker, so `format: date-time` is not enforced by this path. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Excludes authenticated portal content and unpublished application, scoring, review, and adjudication records; it does not activate a connector or authorize release. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; policy behavior remains `NEEDS VERIFICATION` | No legal, administrative, or release outcome may be inferred from this contract or schema. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
|---|---:|---|---|
| `decision_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Eligibility-decision record identity. Generation, deduplication, versioning, and correction-lineage rules remain unspecified. |
| `application_ref` | Yes | Non-empty string | Reference-shaped relationship to an `Application`; the schema does not prove existence, type, version, or referential integrity. |
| `program_version_ref` | Yes | Non-empty string | Reference-shaped relationship to a `ProgramVersion`; the schema does not prove that its eligibility rules governed the application or decision. |
| `outcome` | Yes | `eligible`, `ineligible`, or `pending` | Eligibility determination only. It is not a recommendation, award, payment, project approval, or release outcome. |
| `basis_ref` | No | String or `null`; no `minLength` | Optional pointer to a policy, statutory, or scoring basis. The current shape also admits an empty string and does not require basis resolution for any outcome. |
| `decided_at` | Yes | String annotated as `date-time` | Recorded decision time. The current runner does not enforce date-time syntax or define timezone, effective-time, or source-time semantics beyond the annotation. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not, by itself, an `EvidenceBundle`, receipt, proof, policy decision, review record, release decision, or publication authorization. |

No additional properties are admitted by the current schema.

[Back to top](#top)

## Decision and evidence invariants

The semantic posture is fail closed:

- `outcome` remains one of exactly `eligible`, `ineligible`, or `pending`; labels such as `approved`, `denied`, `recommended`, `awarded`, or `complete` must not be substituted;
- `pending` must not be silently interpreted as eligible, ineligible, withdrawn, denied, approved, or awarded;
- `eligible` means only the recorded eligibility determination and does not establish ranking, recommendation, funding availability, award, payment, project approval, or public release;
- `ineligible` means only the recorded eligibility determination and does not erase, withdraw, or correct the referenced application;
- `application_ref` and `program_version_ref` remain unresolved pointers until their target identities, versions, and relationships are validated;
- `basis_ref` remains a pointer whose authority, version, applicability, digest, and field-level support require resolution; omission, `null`, or an empty string does not establish an evidence-backed basis;
- `decided_at` remains distinct from application submission, program effective, source publication, retrieval, recommendation, award, correction, and release times; and
- `source_ref` must resolve through the owning evidence and source-governance surfaces before a consequential claim is treated as supported.

> [!WARNING]
> The paired schema does not enforce referenced-record existence, application/program compatibility, outcome-transition rules, a non-empty `basis_ref`, basis/outcome coherence, or date-time syntax in the current shared runner. Documentation and schema conformance must not be described as proof that an eligibility decision is lawful, correct, final, evidence-complete, or publicly releasable.

Real application identities, applicant information, eligibility criteria, scoring material, review notes, adjudication records, and decision explanations require independent source, access, rights, privacy, sensitivity, policy, review, correction, and release decisions.

[Back to top](#top)

## Anti-collapse boundaries

An eligibility decision is a distinct decision event. Each upstream record, downstream decision, and delivery fact requires its own identity, source support, evidence, and governed state.

| Boundary | Required interpretation |
|---|---|
| Eligibility decision != application | [`Application`](./application.md) records a request; submission does not establish an eligibility outcome. |
| Eligibility decision != program version | [`ProgramVersion`](./program_version.md) records program and statutory lineage; it does not prove that a particular application was evaluated correctly. |
| Eligibility decision != scoring matrix | [`ScoringMatrixVersion`](./scoring_matrix_version.md) identifies a scoring artifact; scoring criteria or a score do not substitute for an eligibility record. |
| Eligibility decision != recommendation | [`Recommendation`](./recommendation.md) is an advisory funding fact; eligibility does not establish ranking or a recommended amount. |
| Eligibility decision != award | [`Award`](./award.md) is a formal funding decision; `eligible` does not prove that an award exists. |
| Eligibility decision != payment or project approval | Eligibility does not authorize disbursement, create a funding agreement, establish a project, or approve construction. |
| `pending` != a hidden final outcome | A pending record must not be recast as eligible, ineligible, approved, denied, recommended, or awarded without a separately supported transition or successor record. |
| `ineligible` != correction or withdrawal | An ineligibility outcome does not erase or withdraw an application; correction and withdrawal require their governed lineage. |
| Basis reference != basis authority | A string-shaped `basis_ref` does not establish that the referenced rule existed, applied, was current, or was interpreted correctly. |
| Decision time != source or lifecycle time | `decided_at` does not substitute for submission, publication, retrieval, effective, correction, award, or release time. |
| Source reference != evidence closure | A non-empty `source_ref` does not establish field-level support, rights, sensitivity, freshness, review, or publication. |
| Schema-valid != true or public-safe | Structural acceptance does not establish real-world correctness, legal sufficiency, policy approval, release, or KFM publication. |

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
|---|---|---|
| Canonical machine-shape file | [`eligibility_decision.schema.json`](../../../schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Required fields | 6 of 7 properties | `basis_ref` may be omitted; when present, it may be a string or `null`. |
| Unknown fields | Rejected by `additionalProperties: false` | Widening the record requires coordinated contract, schema, fixture, and test review. |
| Outcome vocabulary | Exactly `eligible`, `ineligible`, or `pending` | `approved` and other adjacent decision labels are rejected. |
| Basis shape | Optional string or `null`, without `minLength` | Empty strings are structurally admitted; basis existence, authority, applicability, and outcome coherence are not enforced. |
| Reference integrity | Non-empty strings only for application and program references | Target existence, target type, version compatibility, and relationship validity are not enforced. |
| Outcome transitions | Not encoded | Finality, appeal, reconsideration, correction, and allowed state changes remain unspecified. |
| Date-time assertion | `format: date-time` on `decided_at` | The shared runner constructs `Draft202012Validator` without an explicit format checker, so syntax enforcement is absent from that test path. |

The contract and schema must remain synchronized: prose cannot loosen or tighten machine behavior without a coordinated schema change.

[Back to top](#top)

## Synthetic example

The checked-in valid fixture is synthetic and test-only. It must not be cited as evidence that an application, program version, eligibility decision, basis, or source record exists.

```json
{
  "decision_id": "kwo-swigp-fy2027-elig-synthetic-001",
  "application_ref": "kwo-swigp-fy2027-app-synthetic-001",
  "program_version_ref": "kwo-swigp-fy2027-hb2462",
  "outcome": "pending",
  "basis_ref": null,
  "decided_at": "2026-09-16T00:00:00Z",
  "source_ref": "kwo:grant-programs:swigp:fy2027:eligibility:synthetic-001"
}
```

The paired invalid fixture uses `outcome: "approved"`; the schema test expects that record to be rejected because `approved` is not an admitted eligibility outcome.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Validate the paired schema and fixture family

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

| Validation surface | What it checks | What success does not prove |
|---|---|---|
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct titles for all 15 entity types, representative valid-fixture acceptance, and invalid-fixture rejection | Referential integrity, basis authority, transition rules, legal eligibility, source accuracy, rights, policy, review, or release |
| [`valid_1.json`](../../../fixtures/domains/water_planning/eligibility_decision/valid/valid_1.json) | One representative `pending` shape accepted by the paired schema | That the example is real, current, complete, correctly decided, source-supported, or publicly releasable |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/eligibility_decision/invalid/invalid_1.json) | The unrecognized `approved` outcome is rejected | Exhaustive negative coverage for references, basis, timestamps, transitions, evidence, or correction |
| [`jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) | Draft 2020-12 structural validation with the local registry | Date-time format enforcement, semantic validity, policy execution, or evidence closure |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Pull-request schema inventory, meta-schema checks, aggregate fixtures, and repository-owned schema/contract tests under read-only permissions | Semantic truth, source admission, legal eligibility, rights, sensitivity, release, or publication |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Path-triggered, read-only water-planning domain and RAC-registry checks | Eligibility-schema exhaustiveness, application/program referential integrity, basis resolution, review approval, release, deployment, or publication |

> [!NOTE]
> A green test, check, workflow, or badge is validation evidence only within its named assertions. It is not a source receipt, eligibility determination, legal opinion, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Rights, sensitivity, and release

The [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) records a fail-closed source posture:

- authenticated grant-portal data is excluded unless separately authorized;
- applicant or organization data not published on official public pages is not treated as public;
- application content, scores, review notes, and adjudication records not released as official public records are excluded;
- approval, funding, completion, or operational-benefit claims must not be inferred beyond source evidence;
- public-web and published-recipient-list rights remain `NEEDS VERIFICATION`; and
- no contract, schema, fixture, test, workflow, commit, pull request, or merge creates release or publication authority.

A real eligibility decision may expose the existence or status of an application and may incorporate non-public adjudication material. Public-safe projection therefore requires source identity, field-level evidence, rights, privacy and sensitivity review, policy, validation, human review, release, correction, and rollback closure through their owning surfaces.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
|---|---|---|
| `WP-ELIG-01` | `NEEDS VERIFICATION` | Define deterministic `decision_id` generation, deduplication, versioning, amendment, correction, and supersession behavior. |
| `WP-ELIG-02` | `NEEDS VERIFICATION` | Add or identify referential-integrity checks for `application_ref` and `program_version_ref`, including target type, version, and temporal applicability. |
| `WP-ELIG-03` | `NEEDS VERIFICATION` | Define the semantics, finality, allowed transitions, reconsideration, and appeal posture of `pending`, `eligible`, and `ineligible`. |
| `WP-ELIG-04` | `NEEDS VERIFICATION` | Decide whether `basis_ref` must be present and non-empty for each outcome, identify admitted basis object families, and preserve basis version and digest. |
| `WP-ELIG-05` | `NEEDS VERIFICATION` | Define outcome/basis coherence, reason-code or obligation semantics, and the boundary between eligibility criteria and scoring. |
| `WP-ELIG-06` | `NEEDS VERIFICATION` | Define the authoritative meaning and timezone requirements of `decided_at` and add explicit date-time format enforcement where required. |
| `WP-ELIG-07` | `NEEDS VERIFICATION` | Define how program-version changes affect new decisions without silently reinterpreting or overwriting historical decisions. |
| `WP-ELIG-08` | `NEEDS VERIFICATION` | Establish the applicable policy decision surface, review burden, and finite fail-closed outcomes without treating the eligibility enum as a universal policy enum. |
| `WP-ELIG-09` | `NEEDS VERIFICATION` | Define how `source_ref` and `basis_ref` resolve to field-level evidence, source versions, retrieval records, and correction lineage. |
| `WP-ELIG-10` | `NEEDS VERIFICATION` | Complete rights, privacy, sensitivity, applicant-exposure, and public-safe release review for any real eligibility-decision source family. |

Until these items close, consumers must not infer missing bases, reference integrity, finality, legal eligibility, recommendation, award, payment, project approval, public eligibility, or release readiness.

[Back to top](#top)

## Compatibility, correction, and rollback

- Preserve `doc_id: kfm://doc/contracts-domains-water-planning-eligibility-decision`, the v0.1 identity, and existing property names while this contract remains in force.
- Treat the Markdown contract as semantic authority and the paired schema as machine-shape authority; change both with representative fixtures and tests when behavior changes.
- Treat outcome labels, requiredness, reference meaning, `basis_ref` nullability, timestamp semantics, and `additionalProperties: false` as compatibility-significant.
- Do not silently reinterpret `pending`, omission, `null`, an empty string, a reference-shaped string, or a schema-valid timestamp as resolved evidence or a final decision.
- Represent a later correction or withdrawal through the governed [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) family and preserved lineage; do not erase or silently recast the prior decision.
- Before merge, rollback is closing the unmerged draft pull request and abandoning its scoped branch.
- After merge, restore the prior document bytes with a transparent revert or forward correction; do not alter the schema or fixtures merely to make prose appear consistent.

Rollback changes repository documentation only. It does not reverse an external eligibility determination, application status, recommendation, award, payment, project decision, release, or publication state.

[Back to top](#top)

## Related

- [`README.md`](./README.md) — Domain contract index and cross-entity boundaries
- [`application.md`](./application.md) — Referenced application meaning
- [`program_version.md`](./program_version.md) — Referenced program-version and statutory lineage
- [`scoring_matrix_version.md`](./scoring_matrix_version.md) — Separate scoring-artifact identity
- [`recommendation.md`](./recommendation.md) — Separate advisory recommendation
- [`award.md`](./award.md) — Separate formal award decision
- [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) — Correction and withdrawal lineage
- [`eligibility_decision.schema.json`](../../../schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json) — Canonical machine shape
- [`eligibility_decision` fixtures](../../../fixtures/domains/water_planning/eligibility_decision/) — Synthetic valid and invalid examples
- [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) — Paired schema and fixture tests
- [`jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) — Shared structural validator path
- [`kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source role, exclusions, rights posture, and verification backlog
- [`directory-rules.md`](../../../docs/doctrine/directory-rules.md) and [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) — Responsibility-root placement authority
- [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) and [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) — Relevant read-only validation workflows

[Back to top](#top)
