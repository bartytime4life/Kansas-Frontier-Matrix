<a id="top"></a>

# `contracts/domains/water_planning/` — Kansas Water-Planning Domain Contracts

[![Status: PROPOSED](https://img.shields.io/badge/status-PROPOSED-d29922?style=flat-square)](#status)
[![Authority: semantic contracts](https://img.shields.io/badge/authority-semantic%20contracts-1f6feb?style=flat-square)](#authority-and-placement)
[![briefing-integration](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml/badge.svg?branch=main)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml)
[![Release: not authorized](https://img.shields.io/badge/release-not%20authorized-b42318?style=flat-square)](#rights-sensitivity-and-release)

> **Purpose.** This directory defines the semantic meaning and anti-collapse boundaries of Kansas water-planning, public-participation, grant-program, funding, project-delivery, correction, and Regional Advisory Committee (RAC) registry records.

> [!IMPORTANT]
> Every contract in this lane remains **draft / PROPOSED**. The repository contains bounded schemas, synthetic fixtures, deterministic validators, tests, and internal RAC registry records, but none of those surfaces admits a source, proves a claim, resolves rights or sensitivity, approves policy, authorizes payment, releases data, or creates KFM publication.

## Quick navigation

- [Purpose and scope](#purpose-and-scope)
- [Authority and placement](#authority-and-placement)
- [Status](#status)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Directory map](#directory-map)
- [Entity contracts](#entity-contracts)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Inputs and outputs](#inputs-and-outputs)
- [Validation](#validation)
- [Rights, sensitivity, and release](#rights-sensitivity-and-release)
- [Versioning, correction, and rollback](#versioning-correction-and-rollback)
- [Maintenance and open verification](#maintenance-and-open-verification)
- [Related](#related)

## Purpose and scope

This is the `water_planning` bounded-context lane under the canonical [`contracts/`](../../README.md) responsibility root. It answers **what water-planning objects and interfaces mean**. Machine-readable shape belongs in [`schemas/`](../../../schemas/contracts/v1/domains/water_planning/README.md); decision rules, governed instances, executable validation, and release decisions remain in their own authority surfaces.

The lane currently contains:

- 15 core entity contracts introduced for the bounded modeling work under [issue #1647](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1647);
- one synthetic `PlanningScenarioManifest` pilot for bounded, non-predictive planning support;
- one source-grounded RAC geometry and county-crosswalk registry contract;
- semantic distinctions for identity, time, amount, evidence, geometry, correction, and release posture; and
- links to paired proposed schemas, synthetic fixtures, validators, tests, and internal records.

These contracts do not model authenticated grant-portal payloads, activate a connector, grant access to applicant information, establish payment or benefit facts, or expose an internal store to public clients.

[Back to top](#top)

## Authority and placement

The accepted [Directory Rules v2](../../../docs/doctrine/directory-rules.md) assign semantic and interface meaning to `contracts/`, machine-checkable shape to `schemas/`, normative decisions to `policy/`, validation behavior to `tools/` and `tests/`, governed instances to `data/`, and release decisions to `release/`. [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts that responsibility-root split.

This existing same-path domain lane is a `PLACE` outcome under `DIR-AUTHROOT-002`, `DIR-SCOPELANE-001`, `DIR-SCOPELANE-003`, and the `BOUNDARY_COMPACT` README rules `DIR-README-001` through `DIR-README-004`.

| Concern | Owning surface | This directory's role |
|---|---|---|
| Object and interface meaning | This directory | Defines semantic contracts, invariants, references, and non-equivalence rules. |
| Machine shape | [`schemas/contracts/v1/domains/water_planning/`](../../../schemas/contracts/v1/domains/water_planning/README.md) | Paired proposed schemas encode fields and structural constraints without redefining meaning. |
| Source identity and intake | [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) and [`data/registry/sources/water_planning/`](../../../data/registry/sources/water_planning/README.md) | Supplies source guidance and proposed source records; no connector activation occurs here. |
| Policy and release decisions | `policy/` and `release/` | Outside this lane; a contract cannot approve a transition. |
| Fixtures and executable checks | [`fixtures/domains/water_planning/`](../../../fixtures/domains/water_planning/) and [`tools/validators/domains/water_planning/`](../../../tools/validators/domains/water_planning/README.md) | Exercise bounded behavior; passing results do not create authority. |
| Review routing | [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) | Routes `/contracts/` review to `@bartytime4life`; routing is not independent approval or proof of review. |
| Local stewardship | **NEEDS VERIFICATION** | No independently verified water-planning contract steward is established by this README. |

[Back to top](#top)

## Status

| Surface | Repository-grounded status | Authority limit |
|---|---|---|
| Semantic inventory | **CONFIRMED:** 16 entity contracts, including the synthetic scenario pilot, and one RAC registry contract are indexed below. | Presence is not contract promotion or implementation maturity. |
| Contract lifecycle | **PROPOSED / draft.** Individual entity contracts retain proposed schema-scaffold posture; the RAC registry contract is proposed, source-grounded, and not released. | No contract is KFM-published or release-approved. |
| Paired schemas | **CONFIRMED definition:** 18 proposed JSON Schema files cover 16 entities and two RAC registry records. | Schema conformance proves bounded shape only. |
| Entity fixtures and schema tests | **CONFIRMED definition:** the 15 core entity fixtures are exercised by [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py); the scenario pilot has focused fixture-polarity tests. | Tests do not prove live-source truth, rights, or public eligibility. |
| Domain validators | **CONFIRMED implementation:** status-collapse, geometry-authority, RAC-registry, and planning-scenario validators exist with no-network regression coverage. | Validators do not fetch sources, approve policy, construct proof, or release data. |
| RAC records | **CONFIRMED repository state:** the geometry dataset and county-crosswalk registry records remain internal and `not-released`. | Geometry overlap is not official county membership or governance authority. |
| Epic and slice state | [Issue #1647](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1647) remains open; bounded authority slice [#1841](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1841) is closed; document-pinning slice [#1844](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1844) remains open. | Issue state does not promote contracts or authorize release. |
| Repository control | [Issue #1675](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1675) remains open. | This README does not change settings, review, merge, source, proof, release, deployment, or publication authority. |

[Back to top](#top)

## What belongs here

- semantic definitions for stable water-planning entity and registry families;
- object identity, reference, time, amount, evidence, correction, and supersession meaning;
- explicit finite states and unresolved-state semantics;
- anti-collapse rules that keep meetings, decisions, applications, recommendations, awards, payments, projects, milestones, completion, and benefits distinct;
- region-identity, geometry-reference, and county-crosswalk meaning without embedded geometry;
- contract-to-schema, fixture, validator, test, source, and registry navigation; and
- compatibility, correction, maintenance, and rollback guidance for the semantic surface.

## What does not belong here

| Artifact or action | Correct authority or disposition |
|---|---|
| Canonical JSON Schema | [`schemas/contracts/v1/domains/water_planning/`](../../../schemas/contracts/v1/domains/water_planning/README.md) |
| Source descriptors and source activation state | [`data/registry/sources/water_planning/`](../../../data/registry/sources/water_planning/README.md) and governed source-admission review |
| Real applicant, recipient, portal, project, payment, or benefit records | Governed lifecycle lanes only after identity, rights, sensitivity, and admission closure |
| Inline RAC or project geometry | Governed processed data and reference authorities; never embedded as a semantic shortcut |
| Policy rules or decisions | `policy/` and the applicable decision-record family |
| Validator implementation and tests | [`tools/validators/domains/water_planning/`](../../../tools/validators/domains/water_planning/README.md) and `tests/` |
| EvidenceBundles, receipts, proofs, or release manifests | Their canonical accountability and release families |
| Public API, map, search, graph, export, or AI serving | Governed interfaces consuming release-approved public-safe carriers |

[Back to top](#top)

## Directory map

The current direct children are:

```text
water_planning/
├── README.md
├── advisory_committee_meeting.md
├── application.md
├── application_window.md
├── award.md
├── completion.md
├── construction_milestone.md
├── correction_or_withdrawal.md
├── eligibility_decision.md
├── funding_agreement.md
├── planning_scenario_manifest.md
├── planning_region.md
├── program_version.md
├── project.md
├── public_meeting.md
├── rac_geometry_registry.md
├── recommendation.md
└── scoring_matrix_version.md
```

[Back to top](#top)

## Entity contracts

All schema links below resolve to the paired machine-shape authority. The summaries describe bounded semantic meaning, not verified real-world event or release state.

### Planning and public participation

| Contract | Entity | Paired schema | Semantic boundary |
|---|---|---|---|
| [`planning_scenario_manifest.md`](./planning_scenario_manifest.md) | `PlanningScenarioManifest` | [`planning_scenario_manifest.schema.json`](../../../schemas/contracts/v1/domains/water_planning/planning_scenario_manifest.schema.json) | Synthetic generalized scenario with visible assumptions, horizon, equity, participation, public-summary candidate, and drawer payload; not a prediction, alert, determination, or publication. |
| [`planning_region.md`](./planning_region.md) | `PlanningRegion` | [`planning_region.schema.json`](../../../schemas/contracts/v1/domains/water_planning/planning_region.schema.json) | Stable RAC identity with independent geometry and county-crosswalk resolution states. |
| [`public_meeting.md`](./public_meeting.md) | `PublicMeeting` | [`public_meeting.schema.json`](../../../schemas/contracts/v1/domains/water_planning/public_meeting.schema.json) | Public-participation event; not an approval or award. |
| [`advisory_committee_meeting.md`](./advisory_committee_meeting.md) | `AdvisoryCommitteeMeeting` | [`advisory_committee_meeting.schema.json`](../../../schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json) | RAC advisory event; attendance or discussion is not a decision. |

### Program, scoring, and intake

| Contract | Entity | Paired schema | Semantic boundary |
|---|---|---|---|
| [`program_version.md`](./program_version.md) | `ProgramVersion` | [`program_version.schema.json`](../../../schemas/contracts/v1/domains/water_planning/program_version.schema.json) | Versioned program lineage; later law or guidance does not overwrite history. |
| [`scoring_matrix_version.md`](./scoring_matrix_version.md) | `ScoringMatrixVersion` | [`scoring_matrix_version.schema.json`](../../../schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json) | Digest-linked scoring artifact; not a program version or outcome. |
| [`application_window.md`](./application_window.md) | `ApplicationWindow` | [`application_window.schema.json`](../../../schemas/contracts/v1/domains/water_planning/application_window.schema.json) | Source-timezoned intake interval; not an application or award. |
| [`application.md`](./application.md) | `Application` | [`application.schema.json`](../../../schemas/contracts/v1/domains/water_planning/application.schema.json) | Submitted request with explicit unresolved applicant identity where needed. |
| [`eligibility_decision.md`](./eligibility_decision.md) | `EligibilityDecision` | [`eligibility_decision.schema.json`](../../../schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json) | Finite eligibility determination; not a recommendation or award. |

### Recommendation, funding, delivery, and correction

| Contract | Entity | Paired schema | Semantic boundary |
|---|---|---|---|
| [`recommendation.md`](./recommendation.md) | `Recommendation` | [`recommendation.schema.json`](../../../schemas/contracts/v1/domains/water_planning/recommendation.schema.json) | Advisory recommendation; not a formal award. |
| [`award.md`](./award.md) | `Award` | [`award.schema.json`](../../../schemas/contracts/v1/domains/water_planning/award.schema.json) | Award decision; not payment, construction, completion, or benefit. |
| [`funding_agreement.md`](./funding_agreement.md) | `FundingAgreement` | [`funding_agreement.schema.json`](../../../schemas/contracts/v1/domains/water_planning/funding_agreement.schema.json) | Agreement and paid-amount meaning kept distinct from award and project state. |
| [`project.md`](./project.md) | `Project` | [`project.schema.json`](../../../schemas/contracts/v1/domains/water_planning/project.schema.json) | Award-linked project with independent recipient, region, and location resolution. |
| [`construction_milestone.md`](./construction_milestone.md) | `ConstructionMilestone` | [`construction_milestone.schema.json`](../../../schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json) | Construction evidence distinct from project creation and completion. |
| [`completion.md`](./completion.md) | `Completion` | [`completion.schema.json`](../../../schemas/contracts/v1/domains/water_planning/completion.schema.json) | Explicit completion state; not payment or operational benefit. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | `CorrectionOrWithdrawal` | [`correction_or_withdrawal.schema.json`](../../../schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json) | Digest-linked correction or withdrawal that preserves prior identity and history. |

### RAC geometry and county-crosswalk registries

| Contract | Record family | Paired schemas | Semantic boundary |
|---|---|---|---|
| [`rac_geometry_registry.md`](./rac_geometry_registry.md) | RAC geometry dataset and RAC/county crosswalk registries | [`rac_geometry_dataset_registry.schema.json`](../../../schemas/contracts/v1/domains/water_planning/rac_geometry_dataset_registry.schema.json) and [`rac_county_crosswalk_registry.schema.json`](../../../schemas/contracts/v1/domains/water_planning/rac_county_crosswalk_registry.schema.json) | Source-grounded, digest-pinned internal records; polygon overlap is not official county membership, and registry state is not release. |

[Back to top](#top)

## Anti-collapse boundaries

The domain preserves event, decision, identity, amount, geometry, evidence, and release distinctions. A link or shared identifier may relate records; it does not make them equivalent.

| Boundary | Required interpretation |
|---|---|
| Meeting != decision | `PublicMeeting` and `AdvisoryCommitteeMeeting` do not establish eligibility, recommendation, award, or approval. |
| Application != recommendation != award | Intake, advisory recommendation, and formal award require distinct records and support. |
| Award != payment | `awarded_amount` and `paid_amount` are different facts owned by different entity types. |
| Award != project | An award does not prove that a project record, construction activity, or delivered asset exists. |
| Project != construction != completion | Project identity, milestone evidence, and completion state remain separate. |
| Completion != operational benefit | Completion alone does not prove service, impact, effectiveness, or public benefit. |
| Program version != scoring matrix | Program/statutory lineage and scoring-document lineage remain independent. |
| Region identity != geometry != county overlap | RAC identity, RAC polygon authority, and derived county intersections are separate facts. |
| Project region != project location | Membership in a planning region does not prove project-location geometry, and location does not prove membership. |
| Correction != new event | A correction or withdrawal preserves prior identity and digest lineage rather than rewriting history. |
| Validation != authority | Schema or validator success is not source admission, proof, policy approval, release, deployment, or publication. |

### Amount semantics

| Amount | Owning entity | What it does not prove |
|---|---|---|
| `requested_amount` | `Application` | Recommendation, award, or payment |
| `recommended_amount` | `Recommendation` | Award or disbursement |
| `awarded_amount` | `Award` | Payment, expenditure, construction, or completion |
| `paid_amount` | `FundingAgreement` | Expenditure, completion, or operational benefit |

Missing applicant, recipient, region, county-crosswalk, or geometry authority remains explicitly unresolved or pending according to the applicable contract. It is never filled by guessing from an address, venue, county, recipient name, project prose, centroid, proximity, or containment.

[Back to top](#top)

## Inputs and outputs

### Inputs

Contract maintenance may use:

- accepted KFM doctrine and ADRs that govern semantic authority and placement;
- official public-source guidance recorded in the [KWO catalog entry](../../../docs/sources/catalog/kansas/kwo.md);
- paired proposed schemas and synthetic valid/invalid fixtures;
- deterministic validator and test definitions;
- governed internal registry references and correction lineage; and
- verified compatibility requirements from known consumers.

An input reference is evidence for bounded authoring. It does not automatically become admitted source authority, a proven claim, or permission for public use.

### Outputs

This lane emits:

- human-readable semantic contract documents;
- stable object-family terms and anti-collapse invariants;
- reference and unresolved-state meaning;
- contract-to-schema and validation navigation; and
- versioning, correction, and rollback expectations.

It does not emit source observations, SourceDescriptor activation, data instances, EvidenceBundles, receipts, proofs, policy decisions, PromotionDecisions, ReleaseManifests, published carriers, API responses, map layers, or generated answers.

[Back to top](#top)

## Validation

Run commands from the repository root.

### Validate the 15 core entity schemas and fixtures

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

### Run the complete water-planning domain regression suite

```bash
python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_*.py' \
  --verbose
```

### Exercise the bounded validators

```bash
python tools/validators/domains/water_planning/validate_status_collapse.py \
  fixtures/domains/water_planning/status_collapse/valid/valid_1.json

python tools/validators/domains/water_planning/validate_geometry_authority.py \
  fixtures/domains/water_planning/geometry_authority/valid/valid_1.json

python tools/validators/domains/water_planning/validate_rac_registry.py

python tools/validators/domains/water_planning/validate_planning_scenario_manifest.py --fixtures
```

| Validation layer | Bounded evidence | Does not prove |
|---|---|---|
| Schema tests | File presence, valid/invalid polarity, distinct titles, time, identity, amount, and unresolved-reference constraints for 15 entity schemas | Semantic promotion, source truth, rights, or release |
| Planning-scenario validator | Synthetic schema polarity, RFC 8785 body binding, horizon order, canonical references, summary/drawer parity, and false authority flags | Prediction, evidence resolution, participation approval, policy, review, release, rendering, or publication |
| Status-collapse validator | Synthetic anti-collapse and finite unresolved-state behavior | Live application, award, payment, project, or benefit facts |
| Geometry-authority validator | Synthetic RAC identity and reference-coherence rules | Production geometry, official county membership, or source admission |
| RAC-registry validator | Pinned local geometry, source, digest, identity, mapping, correction, and `not-released` constraints | Source refresh, spatial re-derivation, rights clearance, or publication |
| [`briefing-integration`](../../../.github/workflows/briefing-integration.yml) | Read-only pull-request and `main` job for this path, using no persisted checkout credentials and `KFM_NO_NETWORK=1` | Review approval, evidence closure, release, deployment, or publication |

The workflow declares `contents: read`. Opening a pull request for this README is expected to trigger the water-planning job; the check observes the tested revision and does not write KFM state.

[Back to top](#top)

## Rights, sensitivity, and release

- Do not place credentials, authenticated portal content, private applicant material, or real restricted records in this documentation lane.
- Public KWO pages and document locators remain subject to source-specific rights, attribution, freshness, and correction review.
- The checked-in RAC geometry and county-crosswalk records are internal and `not-released`; a public-administrative-boundary sensitivity label does not bypass rights, evidence, policy, review, or release gates.
- County intersection classes describe measured polygon overlap only. They must not be promoted into political, administrative, advisory, funding, or governance membership without a separately defined and reviewed rule.
- Real applicant, recipient, project-location, living-person, land, infrastructure, or other sensitive information must remain minimized, generalized, quarantined, staged, or denied according to the applicable authority.
- Public clients and ordinary UI surfaces may consume only governed interfaces and release-approved public-safe carriers, never this contract lane or internal canonical stores directly.

A commit, pull request, merge, workflow result, schema pass, validator pass, registry record, or documentation badge is not a KFM promotion or publication event.

[Back to top](#top)

## Versioning, correction, and rollback

A semantic change must preserve or explicitly version:

- stable entity and record-family identity;
- field and enum meaning shared with paired schemas;
- amount, event, geometry, evidence, correction, and release distinctions;
- known consumer compatibility;
- prior digests and supersession links where records depend on the contract; and
- a reviewable migration or correction path when meaning changes.

Update paired schemas, fixtures, validators, tests, and documentation in the same dependency-closed review boundary when their behavior must change. Do not change those surfaces merely to make prose appear current.

For a README-only change:

- before merge, rollback is closing the draft pull request and leaving its branch unmerged;
- after merge, use a focused revert or corrective pull request; and
- reverting documentation must not rewrite source observations, registry records, processed geometry, correction history, proofs, release state, or published carriers.

[Back to top](#top)

## Maintenance and open verification

Re-review this README when a contract is added, removed, promoted, deprecated, or superseded; when field meaning or anti-collapse law changes; when a paired schema, validator, workflow, writer, consumer, rights posture, exposure, or release boundary changes; or when an accepted ADR changes this lane's authority.

| Item | Status | Evidence needed |
|---|---|---|
| Independent water-planning contract steward | **NEEDS VERIFICATION** | Approved responsibility assignment beyond CODEOWNERS routing |
| Contract promotion criteria and version policy | **NEEDS VERIFICATION** | Accepted lifecycle/versioning decision and compatibility plan |
| Public KWO guidance and scoring-document digests | **OPEN / PROPOSED WORK** | Completion of bounded issue [#1844](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1844) with immutable source identity and receipts |
| Source rights and freshness | **NEEDS VERIFICATION** | Source-specific review records and a correction-aware observation process |
| Policy lane and release eligibility | **NOT ESTABLISHED** | Applicable policy decisions, evidence, review, release manifest, correction path, and rollback target |
| Repository-control settings | **NEEDS VERIFICATION** | Closure evidence for issue [#1675](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1675) |
| Parent epic closure | **OPEN** | Reconcile all acceptance criteria and preserved non-goals in issue [#1647](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1647) |

Unknowns narrow permitted use. They do not invite plausible defaults.

[Back to top](#top)

## Related

| Surface | Role |
|---|---|
| [`contracts/`](../../README.md) | Parent semantic-authority boundary |
| [Water-planning schemas](../../../schemas/contracts/v1/domains/water_planning/README.md) | Proposed machine shapes paired to these contracts |
| [Synthetic fixtures](../../../fixtures/domains/water_planning/) | Valid, invalid, status-collapse, and geometry-authority inputs |
| [Water-planning validators](../../../tools/validators/domains/water_planning/README.md) | Deterministic no-network executable checks |
| [Schema contract tests](../../../tests/schemas/test_water_planning_contracts.py) | Fifteen-entity shape and anti-collapse tests |
| [Domain regression tests](../../../tests/domains/water_planning/README.md) | Status, geometry-authority, and RAC-registry test guidance |
| [KWO source catalog](../../../docs/sources/catalog/kansas/kwo.md) | Human source-family guidance and bounded source posture |
| [Water-planning source registry](../../../data/registry/sources/water_planning/README.md) | Proposed, review-gated, connector-disabled source records |
| [Water-planning processed data](../../../data/processed/water_planning/README.md) | Internal normalized RAC geometry boundary |
| [Water-planning crosswalk registry](../../../data/registry/crosswalks/water_planning/README.md) | Derived RAC/county mapping identity and release limits |
| [Directory Rules v2](../../../docs/doctrine/directory-rules.md) | Accepted placement and README authority |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Directory Rules adoption decision |
| [Repository-control incident #1675](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1675) | Platform-control and transition holds |
| [Water-planning epic #1647](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1647) | Parent modeling acceptance and non-goals |

[Back to top](#top)
