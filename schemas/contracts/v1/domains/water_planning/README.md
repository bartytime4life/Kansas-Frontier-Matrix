<a id="top"></a>

# `schemas/contracts/v1/domains/water_planning/` — Kansas Water-Planning Domain Schemas

[![Status: PROPOSED](https://img.shields.io/badge/status-PROPOSED-d29922?style=flat-square)](#status)
[![Authority: machine shape](https://img.shields.io/badge/authority-machine%20shape-1f6feb?style=flat-square)](#authority-boundary)
[![Water-planning checks](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml/badge.svg?branch=main)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml)

> **Purpose.** This lane defines JSON Schema Draft 2020-12 shapes for Kansas water-planning, Regional Advisory Committee (RAC), grant-program, funding, project-delivery, correction, and bounded RAC-registry records.

> [!IMPORTANT]
> Every schema in this directory is **PROPOSED**. Schema validity is bounded machine-shape evidence only; it does not admit a source, establish claim truth, resolve rights or sensitivity, approve policy, prove payment or project outcomes, create a release, or authorize publication.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-boundary) · [Status](#status) · [Schema index](#schemas) · [Invariants](#contract-and-schema-invariants) · [RAC authority](#slice-4-authority-boundary) · [Inputs and outputs](#inputs-and-outputs) · [Validation](#validation) · [Public-safe use](#public-safe-projection) · [Correction and rollback](#versioning-correction-and-rollback) · [Maintenance](#review-burden-and-maintenance) · [Open verification](#open-verification-items) · [Related authority](#related)

## Purpose

This directory is the machine-shape lane for the water-planning bounded context. It keeps distinct records for public participation, program and scoring versions, application intake, eligibility, recommendations, awards, agreements, projects, construction, completion, corrections, RAC identities, RAC geometry datasets, and RAC/county crosswalks.

The lane supports:

- explicit identity, reference, amount, time, and lineage fields;
- fail-closed unresolved states instead of guessed applicant, recipient, regional, or geometry facts;
- distinct schemas for events and decisions that must not collapse;
- source-grounded RAC identity and registry references;
- deterministic local fixtures, validators, and tests;
- correction and supersession without rewriting prior identity.

It does not model authenticated grant-portal payloads, activate a live connector, construct proof, or publish a public water-planning layer.

[Back to top](#top)

## Authority boundary

The accepted [Directory Rules](../../../../../docs/doctrine/directory-rules.md) place machine-checkable shape under `schemas/`, semantic meaning under `contracts/`, decision rules under `policy/`, executable checks under `tests/` and `tools/`, governed instances under `data/`, and release decisions under `release/`. [ADR-0029](../../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) makes those Directory Rules the repository's writable human placement authority.

This existing same-path lane is retained under the Directory Rules' domain-schema pattern and `BOUNDARY_COMPACT` README profile. The relevant rules include `DIR-AUTHROOT-001`, `DIR-AUTHROOT-002`, `DIR-SCOPELANE-001`, `DIR-SCOPELANE-003`, and `DIR-README-001` through `DIR-README-004`.

> [!NOTE]
> The proposed [`domain_lane_register.yaml`](../../../../../control_plane/domain_lane_register.yaml) currently has no entries. This README does not use its existing `water_planning` path spelling to claim that domain registration or alias policy is complete, and it does not authorize a rename or parallel lane.

| Concern | Owning surface | This directory's role |
|---|---|---|
| Water-planning object meaning and anti-collapse law | [`contracts/domains/water_planning/`](../../../../../contracts/domains/water_planning/README.md) | Encodes contract-backed structure; does not redefine meaning. |
| Machine-checkable fields, requiredness, enums, references, and closure | This directory | Owns the 18 proposed JSON Schema files indexed below. |
| Rights, access, sensitivity, and public-use decisions | Governed policy and review surfaces | Exposes decision-relevant fields; does not grant permission. |
| Source identity and registry instances | `data/registry/` | Shapes two bounded registry records; does not activate or refresh a source. |
| Valid, invalid, and authority fixtures | `fixtures/domains/water_planning/` | References synthetic/public-safe inputs; does not own fixture bytes. |
| Validator and regression behavior | `tools/validators/` and `tests/` | Supplies schemas consumed by checks; does not make a passing check authoritative. |
| Release, correction, withdrawal, and rollback decisions | `release/` and applicable record families | Shapes correction lineage; does not approve or execute a transition. |
| Public API, map, UI, search, export, or AI behavior | Governed delivery surfaces | No direct public-client authority. |

### What belongs here

- Proposed JSON Schema Draft 2020-12 files for the bounded water-planning object families.
- Stable schema `$id` values, local field constraints, conditional reference coherence, and closed-object posture.
- This schema-family README and links to paired semantic contracts.
- Shape-level correction, supersession, compatibility, validation, and public-safe-use guidance.

### What does not belong here

- Semantic contract authority, policy rules, source activation, source payloads, or connector code.
- Real applicants, recipients, projects, addresses, authenticated portal records, or inferred geometry.
- Fixture payloads, validator implementation, tests, receipts, proofs, release decisions, or published carriers.
- Inline RAC/project geometry used as a substitute for a governed authority reference.
- Claims that a meeting is an approval, an application or recommendation is an award, an award is payment, or a project is complete.

[Back to top](#top)

## Status

| Surface | Pinned evidence | Current conclusion |
|---|---|---|
| Schema inventory | 17 readable `*.schema.json` files were pinned at `main@ab8fbd9147f085f35a89b88e14ba954e84d25801`; this proposed revision adds one scenario schema | **CONFIRMED on this revision:** 16 entity schemas and 2 RAC registry schemas. |
| Dialect and object closure | Every indexed schema declares JSON Schema Draft 2020-12 and `additionalProperties: false` | **CONFIRMED:** bounded closed-object shapes at the top level. |
| Schema status | Every indexed schema declares `x-kfm.status: PROPOSED` | **CONFIRMED:** no schema is promoted, released, or published by this lane. |
| Semantic pairing | All 16 entity schemas link to individual contracts; both registry schemas link to the RAC registry contract | **CONFIRMED:** contract links exist; contract status remains draft/PROPOSED. |
| Entity fixtures | One valid and one invalid fixture exists for each of the 15 core entities and the scenario pilot | **CONFIRMED:** 32 bounded fixture files are present; observed test execution remains revision-specific. |
| Schema tests | [`test_water_planning_contracts.py`](../../../../../tests/schemas/test_water_planning_contracts.py) | **CONFIRMED definition:** checks file presence, valid/invalid polarity, distinct titles, time, identity, amount, and unresolved-state constraints. |
| Semantic anti-collapse | [`validate_status_collapse.py`](../../../../../tools/validators/domains/water_planning/validate_status_collapse.py) plus tests | **CONFIRMED implementation:** deterministic fixture-only checks with stable non-echoing findings. |
| Region and project authority | `PlanningRegion` and `Project` conditional references plus [`validate_geometry_authority.py`](../../../../../tools/validators/domains/water_planning/validate_geometry_authority.py) | **CONFIRMED implementation:** exact RAC identity and reference-state checks; schemas remain PROPOSED. |
| RAC registry | Two registry schemas plus [`validate_rac_registry.py`](../../../../../tools/validators/domains/water_planning/validate_rac_registry.py) | **CONFIRMED implementation:** pinned local records and geometry/crosswalk consistency checks; source refresh and rights closure are not performed. |
| Workflow definition | [`briefing-integration.yml`](../../../../../.github/workflows/briefing-integration.yml) | **CONFIRMED definition:** this path triggers a read-only, no-persisted-credentials water-planning job on pull requests and `main`. A branch-current result is observed separately. |
| Release posture | Registry schemas require `release_status: not-released` | **CONFIRMED machine constraint:** this is not proof of source freshness, rights clearance, review completion, or public-release eligibility. |
| Review routing | [`.github/CODEOWNERS`](../../../../../.github/CODEOWNERS) routes `/schemas/` to `@bartytime4life` | **CONFIRMED routing only:** independent stewardship, required-review enforcement, and approval remain separate controls. |

Issue [#1841](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1841) is closed as the bounded region/project-geometry authority slice. Parent epic [#1647](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1647) and document-pinning slice [#1844](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1844) remain open; neither issue state promotes these schemas or authorizes release.

[Back to top](#top)

## Schemas

All schema links below resolve to current files in this existing directory. Contract links point to semantic meaning; the short descriptions state only the schema's bounded structural role.

### Planning and public participation

| Schema | Semantic contract | Structural boundary |
|---|---|---|
| [`planning_scenario_manifest.schema.json`](./planning_scenario_manifest.schema.json) | [`planning_scenario_manifest.md`](../../../../../contracts/domains/water_planning/planning_scenario_manifest.md) | Synthetic generalized scenario shape with visible assumptions, horizon, equity, participation, public-summary candidate, drawer payload, and false authority flags. |
| [`planning_region.schema.json`](./planning_region.schema.json) | [`planning_region.md`](../../../../../contracts/domains/water_planning/planning_region.md) | Exact `kwo-rac-01` through `kwo-rac-14` identity shape plus explicit geometry and county-crosswalk resolution states. |
| [`public_meeting.schema.json`](./public_meeting.schema.json) | [`public_meeting.md`](../../../../../contracts/domains/water_planning/public_meeting.md) | KWO public-meeting event shape; a meeting is not a decision or approval. |
| [`advisory_committee_meeting.schema.json`](./advisory_committee_meeting.schema.json) | [`advisory_committee_meeting.md`](../../../../../contracts/domains/water_planning/advisory_committee_meeting.md) | RAC advisory-meeting event shape; attendance or discussion is not an award. |

### Program, scoring, and intake

| Schema | Semantic contract | Structural boundary |
|---|---|---|
| [`program_version.schema.json`](./program_version.schema.json) | [`program_version.md`](../../../../../contracts/domains/water_planning/program_version.md) | Versioned program identity and supersession; later statutes do not overwrite prior program history. |
| [`scoring_matrix_version.schema.json`](./scoring_matrix_version.schema.json) | [`scoring_matrix_version.md`](../../../../../contracts/domains/water_planning/scoring_matrix_version.md) | Digest-linked scoring-matrix version; not a program version or project outcome. |
| [`application_window.schema.json`](./application_window.schema.json) | [`application_window.md`](../../../../../contracts/domains/water_planning/application_window.md) | Open/close interval with explicit source timezone; FY2027 closes at `2026-09-15T23:59:00-05:00` in the current fixture. |
| [`application.schema.json`](./application.schema.json) | [`application.md`](../../../../../contracts/domains/water_planning/application.md) | Application and requested-amount shape with explicit unresolved applicant identity. |
| [`eligibility_decision.schema.json`](./eligibility_decision.schema.json) | [`eligibility_decision.md`](../../../../../contracts/domains/water_planning/eligibility_decision.md) | Finite eligibility state distinct from recommendation, award, and payment. |

### Recommendation, funding, delivery, and correction

| Schema | Semantic contract | Structural boundary |
|---|---|---|
| [`recommendation.schema.json`](./recommendation.schema.json) | [`recommendation.md`](../../../../../contracts/domains/water_planning/recommendation.md) | Advisory recommendation and recommended amount; not an award. |
| [`award.schema.json`](./award.schema.json) | [`award.md`](../../../../../contracts/domains/water_planning/award.md) | Award decision and awarded amount; not payment, construction, completion, or benefit. |
| [`funding_agreement.schema.json`](./funding_agreement.schema.json) | [`funding_agreement.md`](../../../../../contracts/domains/water_planning/funding_agreement.md) | Agreement and paid-amount field kept distinct from award and project state. |
| [`project.schema.json`](./project.schema.json) | [`project.md`](../../../../../contracts/domains/water_planning/project.md) | Award-linked project with independent recipient, RAC-membership, and project-location resolution states. |
| [`construction_milestone.schema.json`](./construction_milestone.schema.json) | [`construction_milestone.md`](../../../../../contracts/domains/water_planning/construction_milestone.md) | Construction milestone distinct from project creation and completion. |
| [`completion.schema.json`](./completion.schema.json) | [`completion.md`](../../../../../contracts/domains/water_planning/completion.md) | Completion state distinct from award, payment, construction, and operational benefit. |
| [`correction_or_withdrawal.schema.json`](./correction_or_withdrawal.schema.json) | [`correction_or_withdrawal.md`](../../../../../contracts/domains/water_planning/correction_or_withdrawal.md) | Digest-linked correction or withdrawal without rewriting the prior subject record. |

### RAC geometry and county-crosswalk registries

| Schema | Semantic contract | Structural boundary |
|---|---|---|
| [`rac_geometry_dataset_registry.schema.json`](./rac_geometry_dataset_registry.schema.json) | [`rac_geometry_registry.md`](../../../../../contracts/domains/water_planning/rac_geometry_registry.md) | One source-grounded KWO RAC geometry dataset version, processed payload digest, rights-review posture, and `not-released` hold. |
| [`rac_county_crosswalk_registry.schema.json`](./rac_county_crosswalk_registry.schema.json) | [`rac_geometry_registry.md`](../../../../../contracts/domains/water_planning/rac_geometry_registry.md) | Deterministic positive-area KWO RAC/Census 2025 county intersection mappings; geometry overlap is not governance membership. |

[Back to top](#top)

## Contract and schema invariants

### Status and amount anti-collapse

| Boundary | Required interpretation |
|---|---|
| Meeting != decision | `PublicMeeting` and `AdvisoryCommitteeMeeting` do not establish eligibility, recommendation, or award. |
| Application != recommendation != award | Intake, advisory recommendation, and award remain separate records with separate source support. |
| Award != payment | `awarded_amount` belongs to `Award`; `paid_amount` belongs to `FundingAgreement`. Neither field alone proves disbursement or expenditure. |
| Award != project | `Project` references an award; it is not created merely because an award record exists. |
| Project != construction != completion | Project identity, milestone evidence, and completion state remain separate. |
| Completion != operational benefit | A completed record does not prove service, impact, or benefit without separate evidence. |
| Program version != scoring matrix | Statutory/program lineage and scoring-document lineage remain distinct. |
| Correction != new event | `CorrectionOrWithdrawal` preserves the subject reference and prior digest rather than silently replacing history. |

### Identity, time, and evidence posture

- Missing applicant and recipient identities remain explicit `unresolved` or `pending` states; they are never guessed.
- Source publication, retrieval, correction, and effective times remain distinct where the applicable schema carries them.
- Application-window time retains its source timezone and UTC offset.
- Requested, recommended, awarded, paid, and any later expenditure facts must not share an ambiguous generic amount field.
- A `source_ref`, URL, digest, or document link is a reference, not proof that every claim attributed to it is supported.
- Evidence, policy, review, release, correction, and rollback references remain separate object families.

[Back to top](#top)

## Slice 4 authority boundary

- `PlanningRegion.region_id` and `Project.planning_region_ref` admit only `kwo-rac-01` through `kwo-rac-14`.
- `rac_number` is a KFM stable ordinal pinned by the identity inventory; it is not represented as a KWO-native number.
- RAC, groundwater-management-district, county, municipality, venue, recipient, and project-location identities remain distinct.
- Unresolved geometry requires a null reference. `approximate` or `confirmed` geometry requires a non-null reference to a declared authority.
- County-crosswalk and project-region resolution states must agree with their nullable references.
- Project RAC membership and project-location geometry are independent facts; neither may be inferred from the other.
- Inline geometry, coordinates, polygons, centroids, addresses-as-geometry, and inferred containment are outside these entity schemas.
- Canonical RAC geometry bytes live under [`data/processed/water_planning/rac_regions/`](../../../../../data/processed/water_planning/rac_regions/), not inside `PlanningRegion` or a registry record.
- County rows are measured positive-area polygon intersections. `dominant`, `material-partial`, and `boundary-sliver` describe overlap, not political, administrative, advisory, funding, or governance membership.
- Referential integrity, exact names, authority version/digest/correction metadata, GMD/RAC separation, deterministic ordering, and non-echoing findings are enforced by the bounded validators rather than JSON Schema alone.
- Registry records and paired source descriptors remain internal and `not-released`. No schema or validator result changes that state.

[Back to top](#top)

## Inputs and outputs

### Inputs

Schema maintenance may use:

- paired semantic contracts in [`contracts/domains/water_planning/`](../../../../../contracts/domains/water_planning/README.md);
- synthetic valid and invalid fixtures under `fixtures/domains/water_planning/`;
- source and identity constraints recorded by the [KWO catalog entry](../../../../../docs/sources/catalog/kansas/kwo.md);
- deterministic validator and test behavior;
- governed registry records and processed RAC geometry referenced by the two registry schemas;
- accepted Directory Rules, ADRs, correction lineage, and verified consumer requirements.

### Outputs

This lane emits only:

- JSON Schema documents;
- schema-family navigation and machine-shape guidance;
- structural validation results when external tools consume the schemas.

It does not emit a SourceDescriptor activation, EvidenceBundle, receipt, proof, PolicyDecision, PromotionDecision, ReleaseManifest, published payload, map layer, public API response, or authoritative generated answer.

[Back to top](#top)

## Validation

Run commands from the repository root. The first command exercises the 15 core entity schemas. The remaining commands cover the scenario, semantic, authority-reference, and concrete RAC-registry boundaries.

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py

python tools/validators/domains/water_planning/validate_status_collapse.py \
  fixtures/domains/water_planning/status_collapse/valid/valid_1.json

python tools/validators/domains/water_planning/validate_geometry_authority.py \
  fixtures/domains/water_planning/geometry_authority/valid/valid_1.json

python tools/validators/domains/water_planning/validate_rac_registry.py

python tools/validators/domains/water_planning/validate_planning_scenario_manifest.py --fixtures

python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_*.py' \
  --verbose
```

### Validation surfaces

| Surface | What it checks | Success signal | What success does not prove |
|---|---|---|---|
| [`test_water_planning_contracts.py`](../../../../../tests/schemas/test_water_planning_contracts.py) | 15 schema files, distinct titles, valid/invalid fixtures, explicit time, identity, amount, and resolution constraints | Pytest exits `0` | Semantic truth, source freshness, policy, rights, release, or publication. |
| [`validate_planning_scenario_manifest.py`](../../../../../tools/validators/domains/water_planning/validate_planning_scenario_manifest.py) | Synthetic scenario schema polarity, content identity, horizon order, canonical references, surface parity, and authority boundary | `PLANNING_SCENARIO_MANIFEST_FIXTURES_VALID` | Prediction, evidence resolution, participation approval, policy, review, release, rendering, or publication. |
| [`validate_status_collapse.py`](../../../../../tools/validators/domains/water_planning/validate_status_collapse.py) | Synthetic status, amount, lineage, portal, personal-data, proof, release, and publication anti-collapse rules | One JSON object per file with `"outcome":"PASS"`; exit `0` | Validation of live applications, recipients, projects, or grant outcomes. |
| [`validate_geometry_authority.py`](../../../../../tools/validators/domains/water_planning/validate_geometry_authority.py) | Exact RAC inventory, authority digests, region/project reference coherence, namespace separation, inline-geometry denial | `{"files":N,"outcome":"VALIDATOR_PASS"}`; exit `0` | Construction or refresh of production geometry or county intersections. |
| [`validate_rac_registry.py`](../../../../../tools/validators/domains/water_planning/validate_rac_registry.py) | Pinned KWO payload digest, 14 RAC features, 105 Kansas county GEOIDs, ordered 209-row mapping digest, source and release posture | `RAC_REGISTRY_OK regions=14 counties=105 mappings=209`; exit `0` | Independent source refetch, spatial recomputation, rights clearance, or governance membership. |
| [`briefing-integration.yml`](../../../../../.github/workflows/briefing-integration.yml) | The domain regression suite and canonical RAC registry validator for affected pull requests and `main` | Branch-current GitHub job succeeds | Repository authorization, evidence closure, release, deployment, or publication. |

Malformed, missing, oversized, mismatched, authority-collapsed, value-echoing, or release-overclaiming inputs fail closed within each validator's documented scope. Do not reinterpret a nonzero exit as a warning or use a green workflow badge as release evidence.

[Back to top](#top)

## Public-safe projection

These schemas are internal machine-shape authorities, not ordinary public-client inputs.

Public APIs, maps, dashboards, search, exports, Focus Mode, and AI surfaces must consume governed interfaces or release-approved public-safe carriers. Before any water-planning record reaches such a surface, the applicable process must separately resolve evidence, source role, identity, rights, sensitivity, policy, review, release, correction, and rollback.

Authenticated grant-portal data, applicant/recipient personal information, inferred project locations, and source material without verified access authority remain denied or held. A public source page or recipient table does not by itself prove application, recommendation, award, payment, construction, completion, or benefit.

[Back to top](#top)

## Versioning, correction, and rollback

Treat these as compatibility-significant changes:

- changing a schema `$id`, required field, enum, reference target, identity pattern, or conditional resolution rule;
- changing the exact RAC ID inventory, KFM ordinal mapping, dataset version, source version, digest, geometry path, county vintage, mapping thresholds, or overlap classes;
- widening a schema so guessed, inline, unauthoritative, or release-overclaiming data becomes valid;
- narrowing a schema in a way that invalidates retained records or known consumers.

A material change should update the paired contract, schema, fixtures, validators, tests, consumer expectations, correction lineage, and rollback target together within an authorized review boundary. A source refresh creates a new observation and digest or an explicit correction; it must not mutate prior source identity silently.

Before merge, rollback is to close the draft pull request and abandon the scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. Never rewrite shared history, remove prior digest lineage, or restore guessed geometry to make validation pass.

[Back to top](#top)

## Review burden and maintenance

| Item | Requirement |
|---|---|
| Review route | [`.github/CODEOWNERS`](../../../../../.github/CODEOWNERS) routes this lane to `@bartytime4life`; routing is not independent approval or proof of review. |
| Local stewardship | **NEEDS VERIFICATION:** no separate water-planning schema steward is established by this directory. |
| Evidence review | Reviewed on 2026-07-30 against `main@ab8fbd9147f085f35a89b88e14ba954e84d25801`. |
| Schema/contract parity | Keep each schema's `x-kfm.contract_doc`, field semantics, and status synchronized with its paired contract. |
| Fixture parity | Maintain at least one meaningful valid and invalid entity fixture; add targeted negative cases for every new fail-closed rule. |
| Determinism | Preserve stable ordering, finite findings, no-network behavior where declared, non-echoing diagnostics, and explicit exit semantics. |
| Source and registry changes | Version and digest source observations; preserve correction/supersession lineage and `not-released` state unless separately authorized. |
| Documentation | Update this index when a schema is added, removed, renamed, superseded, reclassified, or wired into a different validator/workflow. |

Re-review when issue #1647 or #1844 changes the modeled source/document set, an ADR changes the schema home or domain identity, a schema status changes, a validator or workflow changes scope, a registry baseline changes, a public consumer appears, or release/correction policy is accepted.

[Back to top](#top)

## Open verification items

| ID | Item | Required evidence |
|---|---|---|
| `WP-SCHEMA-01` | Register the water-planning domain ID and path/code aliases | Populated, adopted domain-lane register entry plus migration decision if the existing underscore path changes. |
| `WP-SCHEMA-02` | Close source-document identity gaps for program/scoring fixtures | Authorized public-document observation, immutable digests, manifests/receipts, and deterministic tests under issue #1844. |
| `WP-SCHEMA-03` | Verify schema `$id` namespace and external resolution posture | Accepted schema-identity decision, registry behavior, consumer inventory, and compatibility plan. |
| `WP-SCHEMA-04` | Establish source rights, freshness, and correction cadence | Current source observations, rights review, immutable lineage, and bounded refresh procedure. |
| `WP-SCHEMA-05` | Establish independent stewardship and required-review behavior | Verified collaborator/team, responsibility assignment, ruleset evidence, and review policy. |
| `WP-SCHEMA-06` | Inventory governed consumers | Commit-pinned API, package, pipeline, map/UI, export, search, and AI consumer evidence. |
| `WP-SCHEMA-07` | Bind any future public projection to release and rollback | EvidenceBundle, policy decision, review record, release manifest, correction route, and tested rollback. |

[Back to top](#top)

## Related

| Surface | Role |
|---|---|
| [`contracts/domains/water_planning/`](../../../../../contracts/domains/water_planning/README.md) | Semantic object meaning and anti-collapse boundaries. |
| [`fixtures/domains/water_planning/`](../../../../../fixtures/domains/water_planning/) | Synthetic/public-safe valid, invalid, status-collapse, and authority-reference inputs. |
| [`tools/validators/domains/water_planning/README.md`](../../../../../tools/validators/domains/water_planning/README.md) | Validator contracts, commands, finite outcomes, limitations, and recovery. |
| [`tests/schemas/test_water_planning_contracts.py`](../../../../../tests/schemas/test_water_planning_contracts.py) | Entity-schema and fixture regression tests. |
| [`tests/domains/water_planning/test_status_collapse.py`](../../../../../tests/domains/water_planning/test_status_collapse.py) | Semantic anti-collapse regression tests. |
| [`tests/domains/water_planning/test_geometry_authority.py`](../../../../../tests/domains/water_planning/test_geometry_authority.py) | RAC identity and reference-authority regression tests. |
| [`tests/domains/water_planning/test_rac_registry.py`](../../../../../tests/domains/water_planning/test_rac_registry.py) | Pinned registry, geometry, county, mapping, source, and release-posture tests. |
| [`docs/sources/catalog/kansas/kwo.md`](../../../../../docs/sources/catalog/kansas/kwo.md) | Human KWO source catalog entry and authority limitations. |
| [`rac_geometry_registry.md`](../../../../../contracts/domains/water_planning/rac_geometry_registry.md) | Concrete RAC geometry and county-crosswalk semantic contract. |
| [Directory Rules](../../../../../docs/doctrine/directory-rules.md) | Responsibility-root, domain-lane, schema-placement, and README authority. |
| [ADR-0029](../../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for the canonical Directory Rules. |
| [`briefing-integration.yml`](../../../../../.github/workflows/briefing-integration.yml) | Read-only path-triggered water-planning validation definition. |
| [Issue #1647](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1647) | Open parent modeling epic; not release authority. |
| [Issue #1844](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1844) | Open public-document pinning slice; not implementation authority by itself. |

[Back to top](#top)
