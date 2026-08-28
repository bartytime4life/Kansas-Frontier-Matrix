<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-application-window
title: ApplicationWindow Contract — Water Planning
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
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/application_window.schema.json
  - ../../../fixtures/domains/water_planning/application_window/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/briefing-integration.yml
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ApplicationWindow Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/application_window.schema.json)

Defines the semantic meaning, time boundary, source-timezone handling, and fail-closed interpretation of a water-planning grant application window.

> [!IMPORTANT]
> This document and its paired schema are `PROPOSED` scaffolds. They do not prove that a program is open, that an application was submitted or accepted, that a source is admitted, or that any record is policy-approved, release-authorized, or KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Time and deadline semantics](#time-and-deadline-semantics)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

An `ApplicationWindow` represents one open-to-close intake interval for one version of a grant program and one fiscal year. Every record identifies the window, references the applicable [`ProgramVersion`](./program_version.md), records the closing instant and its source timezone, and retains a non-empty source pointer.

The current schema permits `opens_at: null` when the source does not provide an exact opening instant. A missing opening instant means **unknown**, not always open, retroactively open, or open from the start of the fiscal year.

The contract defines interval meaning. The paired JSON Schema defines accepted document shape. Source admission, evidence resolution, application intake, eligibility, recommendation, award, payment, policy, review, release, correction, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
| --- | --- | --- |
| This document | `draft`; `PROPOSED`; v0.1 | Defines semantic meaning, time interpretation, and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/application_window.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not source truth, temporal freshness, or policy. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/application_window/) | Synthetic test inputs | Exercise representative schema behavior; they are not grant-program evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check representative acceptance, rejection, and the modeled FY2027 deadline; passing does not prove a live application window. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Records source role and limitations; it does not activate a connector or authorize release. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; policy behavior remains `NEEDS VERIFICATION` | No policy outcome may be inferred from this contract or schema. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
| --- | ---: | --- | --- |
| `window_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Stable record identity within the modeled system. Generation, deduplication, and correction identity rules remain unspecified. |
| `program_version_ref` | Yes | Non-empty string | Reference to the applicable program version. Shape validity does not prove that the target exists or is current. |
| `fiscal_year` | Yes | String matching `^FY[0-9]{4}$` | Program fiscal-year label; it is not a calendar-year interval or evidence of appropriation. |
| `opens_at` | No | `date-time` string or `null` | Exact opening instant when supported; `null` means the source opening instant is unresolved. |
| `closes_at` | Yes | String annotated as `date-time` | Closing instant with an explicit numeric UTC offset under this contract's semantic rule. |
| `source_timezone` | Yes | Non-empty string | IANA timezone intended to preserve the source-local interpretation, such as `America/Chicago`. The current schema does not validate the IANA registry. |
| `source_publication_time` | No | `date-time` string or `null` | When the source published the notice, if known; distinct from the application interval. |
| `retrieval_time` | No | `date-time` string or `null` | When the source observation was retrieved, if known; distinct from publication and window times. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not, by itself, an `EvidenceBundle`, receipt, proof, source-admission decision, or release authorization. |

No additional properties are admitted by the current schema.

[Back to top](#top)

## Time and deadline semantics

The repository's FY2027 synthetic fixture models the State Water Infrastructure Grant Program window as:

| Time fact | Modeled value | Interpretation |
| --- | --- | --- |
| Fiscal year | `FY2027` | Program-year label, not the interval itself. |
| Opening instant | `null` | No exact opening timestamp is asserted by the fixture. |
| Closing instant | `2026-09-15T23:59:00-05:00` | One offset-bearing instant. |
| Source timezone | `America/Chicago` | Preserves the intended Kansas local-time rule independently of the numeric offset. |
| Source publication time | `2026-07-01T00:00:00Z` | Fixture value for source-publication lineage; not the opening time. |
| Retrieval time | `null` | No retrieval instant is asserted by the fixture. |

As observed on 2026-07-30, the [official KWO grant-program page](https://www.kwo.ks.gov/events-initiatives/grant-programs/state-water-infrastructure-grant-programs) states that FY2027 applications submitted after 11:59 p.m. on September 15, 2026 will not be accepted. The repository schema description and fixture normalize that local deadline with `America/Chicago` and the `-05:00` offset in effect on that date.

> [!WARNING]
> The visible KWO page text does not name a timezone. The source-to-`America/Chicago` normalization is therefore an explicit repository interpretation that still needs immutable source observation, field-level evidence, and freshness review. Do not silently substitute a machine-local timezone, strip the offset, or treat the modeled fixture as proof that the live deadline has not changed.

Store both the offset-bearing `closes_at` value and the IANA `source_timezone`. The offset identifies the represented instant; the IANA zone preserves the civil-time rule needed to interpret future or corrected records across daylight-saving transitions.

[Back to top](#top)

## Anti-collapse boundaries

| Boundary | Required interpretation |
| --- | --- |
| Application window != application | An intake interval does not prove that an [`Application`](./application.md) exists, was timely, was complete, or was accepted. |
| Deadline != eligibility, recommendation, or award | A closing time has no decision, funding, payment, construction, completion, or benefit authority. |
| Unknown opening time != always open | `opens_at: null` preserves uncertainty; it must not be replaced by a guessed instant or unbounded interval. |
| Local timezone != UTC offset | `America/Chicago` preserves a civil-time rule; `-05:00` identifies the offset for the modeled instant. Neither field may silently replace the other. |
| Window time != source time | `opens_at` and `closes_at` describe intake; `source_publication_time` and `retrieval_time` describe provenance events. |
| Program reference != referential proof | A non-empty `program_version_ref` does not establish target existence, currency, statutory effect, or supersession closure. |
| Source reference != evidence closure | A non-empty `source_ref` does not prove field-level support, rights clearance, freshness, review, or publication. |
| Schema-valid != true or public-safe | Structural acceptance does not establish that the source is current, the interval is operational, or the record is release-approved. |

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
| --- | --- | --- |
| Canonical machine-shape file | [`application_window.schema.json`](../../../schemas/contracts/v1/domains/water_planning/application_window.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Properties | 9 | The current shape is intentionally small and source-oriented. |
| Required fields | 6 | `opens_at`, `source_publication_time`, and `retrieval_time` may be absent or `null`. |
| Unknown fields | Rejected by `additionalProperties: false` | Widening the record requires coordinated contract, schema, fixture, and test review. |
| Time annotations | `format: date-time` on four fields | The shared validator currently does not install a format checker, so annotation alone does not enforce RFC 3339 syntax or an explicit offset. |
| Timezone constraint | Non-empty string | IANA membership and agreement with `closes_at` are semantic requirements not currently enforced by the schema. |

The contract and schema must remain synchronized: prose cannot loosen or tighten machine behavior without a coordinated schema change. Where this contract is stricter than the current schema—especially explicit-offset and IANA-zone requirements—the gap remains `NEEDS VERIFICATION`, not silently implemented.

[Back to top](#top)

## Synthetic example

The repository fixture below is synthetic and test-only. It must not be cited as evidence that the program is currently open or that the deadline remains unchanged.

```json
{
  "window_id": "kwo-swigp-fy2027-window",
  "program_version_ref": "kwo-swigp-fy2027-hb2462",
  "fiscal_year": "FY2027",
  "opens_at": null,
  "closes_at": "2026-09-15T23:59:00-05:00",
  "source_timezone": "America/Chicago",
  "source_publication_time": "2026-07-01T00:00:00Z",
  "retrieval_time": null,
  "source_ref": "kwo:grant-programs:swigp:fy2027:window"
}
```

The paired invalid fixture omits `source_timezone`; the schema test expects that record to be rejected.

[Back to top](#top)

## Validation

Run the schema suite from the repository root:

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

| Validation surface | What it checks | What success does not prove |
| --- | --- | --- |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct entity titles, representative valid/invalid fixtures, the modeled FY2027 date/time values, and required `source_timezone` | Source freshness, exact timezone evidence, format enforcement, rights, policy, release, or publication. |
| [`valid_1.json`](../../../fixtures/domains/water_planning/application_window/valid/valid_1.json) | One representative shape accepted by the paired schema | That the window is live, complete, current, or source-admitted. |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/application_window/invalid/invalid_1.json) | Missing required `source_timezone` is rejected | Exhaustive negative coverage for identifiers, dates, offsets, IANA zones, or temporal ordering. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | A repository-wide, read-only pull-request workflow runs `tests/schemas`, including this schema suite | Source truth, deadline freshness, rights, policy, release, deployment, or publication. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | A read-only, no-network workflow is path-triggered for water-planning contract changes and runs domain semantic and registry checks | The schema suite above, Markdown link integrity, repository authorization, evidence closure, release, deployment, or publication. |

> [!NOTE]
> A green test or workflow result is validation evidence only within the tested boundary. It is not a source receipt, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
| --- | --- | --- |
| `WP-AW-01` | `NEEDS VERIFICATION` | Pin immutable source bytes or an admissible receipt that supports the FY2027 deadline and the `America/Chicago` interpretation; the visible KWO page text does not name a timezone. |
| `WP-AW-02` | `NEEDS VERIFICATION` | Decide whether the shared Draft 2020-12 validator must enable a format checker so invalid date-time strings and missing offsets fail closed. |
| `WP-AW-03` | `NEEDS VERIFICATION` | Enforce or explicitly defer IANA timezone membership and agreement between `source_timezone` and the offset in `closes_at`. |
| `WP-AW-04` | `NEEDS VERIFICATION` | Define and test temporal coherence, including whether a non-null `opens_at` must be at or before `closes_at`. |
| `WP-AW-05` | `NEEDS VERIFICATION` | Define stable identity, deduplication, amendment, cancellation, and supersession rules for `window_id`. |
| `WP-AW-06` | `NEEDS VERIFICATION` | Define referential-integrity checks for `program_version_ref` and resolution of `source_ref` to field-level evidence. |
| `WP-AW-07` | `NEEDS VERIFICATION` | Define how later deadline notices, corrections, withdrawals, and retrieval observations preserve lineage without silently overwriting relied-on history. |
| `WP-AW-08` | `NEEDS VERIFICATION` | Establish source-freshness cadence and a fail-closed stale state before any UI, API, notification, or AI surface presents the window as currently open. |

Until these items are resolved, narrow claims, preserve explicit unknowns, and do not infer a live intake state from fixture or schema conformance.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- required fields, identifier patterns, nullability, or `additionalProperties`;
- the relationship between `window_id`, `program_version_ref`, and fiscal year;
- offset, timezone, opening, closing, publication, or retrieval semantics;
- source/evidence reference meaning; and
- any current-state or public-safe projection.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, tests, known consumers, and correction lineage within one authorized review boundary. When an authoritative deadline changes, preserve the prior observation and use [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) or another governed correction surface as applicable; do not silently rewrite a relied-on interval.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository bytes; it does not erase source history or create publication authority.

[Back to top](#top)

## Related

| Surface | Role |
| --- | --- |
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`program_version.md`](./program_version.md) | Meaning of the referenced `ProgramVersion` entity. |
| [`application.md`](./application.md) | Separate application-submission contract. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | Domain correction and withdrawal event contract. |
| [`application_window.schema.json`](../../../schemas/contracts/v1/domains/water_planning/application_window.schema.json) | Canonical machine shape for this record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic fixtures](../../../fixtures/domains/water_planning/application_window/) | Representative valid and invalid inputs. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family regression tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, rights, freshness, and admission limitations. |
| [Official KWO grant-program page](https://www.kwo.ks.gov/events-initiatives/grant-programs/state-water-infrastructure-grant-programs) | Public source candidate for the FY2027 deadline; not an admission or release decision. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`schema-validation.yml`](../../../.github/workflows/schema-validation.yml) | Read-only pull-request schema and contract validation workflow. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only path-triggered water-planning validation workflow. |

[Back to top](#top)
