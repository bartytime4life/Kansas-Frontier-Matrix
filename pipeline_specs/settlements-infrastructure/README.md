<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-settlements-infrastructure-readme
title: Settlements Infrastructure Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <settlements-infrastructure-domain-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/settlements-infrastructure/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipeline_specs/settlement/README.md
  - pipelines/README.md
  - pipelines/domains/settlements-infrastructure/README.md
  - pipelines/domains/settlement/README.md
  - docs/domains/settlements-infrastructure/README.md
  - docs/domains/settlements-infrastructure/ARCHITECTURE.md
  - docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md
  - contracts/domains/settlements-infrastructure/
  - schemas/contracts/v1/domains/settlements-infrastructure/
  - data/registry/sources/settlements-infrastructure/
  - data/receipts/pipeline/settlements-infrastructure/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/settlements-infrastructure/
  - fixtures/pipeline_specs/settlements-infrastructure/
tags: [kfm, pipeline-specs, settlements-infrastructure, settlement, infrastructure, municipalities, census-places, townsites, ghost-towns, facilities, service-areas, operators, condition-observations, dependencies, declarative-config, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/settlements-infrastructure stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Settlements/Infrastructure specs configure pipeline intent, source scope, lifecycle gates, temporal/source-vintage checks, sensitivity gates, evidence gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "The shorter settlement path is an alias/compatibility lane unless an ADR resolves the segment differently."
  - "Restricted facility, operator, condition, dependency, private-property, living-person, and culturally sensitive context fail closed by default."
  - "Concrete spec filenames, schema validation, CI coverage, source activation, and release wiring remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements / Infrastructure Pipeline Specs

> Declarative configuration lane for Settlements / Infrastructure pipeline profiles, source scopes, schedules, lifecycle gates, temporal/source-vintage checks, sensitivity and public-safe representation requirements, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable Settlements / Infrastructure pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fsettlements--infrastructure%2F-d62728)
![alias](https://img.shields.io/badge/settlement%20alias-subordinate-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/settlements-infrastructure/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/settlements-infrastructure/` — executable pipeline logic, the **how**  
**Alias posture:** `pipeline_specs/settlement/` is an alias/compatibility path and must not become a parallel authority lane.  
**Placement posture:** Settlements / Infrastructure declarative specs belong here unless an ADR resolves segment naming differently.  
**Public posture:** no public release, data storage, legal-status decision, operational-status decision, restricted-facility exposure, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Settlement alias posture](#3-settlement-alias-posture)
- [4. Sensitivity boundary](#4-sensitivity-boundary)
- [5. Spec anti-collapse rules](#5-spec-anti-collapse-rules)
- [6. What belongs here](#6-what-belongs-here)
- [7. What does not belong here](#7-what-does-not-belong-here)
- [8. Spec scope](#8-spec-scope)
- [9. Lifecycle posture](#9-lifecycle-posture)
- [10. Required gates](#10-required-gates)
- [11. Directory contract](#11-directory-contract)
- [12. Spec profile families](#12-spec-profile-families)
- [13. Inputs and outputs](#13-inputs-and-outputs)
- [14. Minimal spec profile shape](#14-minimal-spec-profile-shape)
- [15. Tests, fixtures, and validation](#15-tests-fixtures-and-validation)
- [16. Definition of done](#16-definition-of-done)
- [17. Open questions](#17-open-questions)

---

## 1. Purpose

`pipeline_specs/settlements-infrastructure/` owns declarative Settlements / Infrastructure pipeline configuration.

It may describe:

- which Settlements / Infrastructure pipeline profile should run;
- which source descriptor ids are in scope;
- which settlement, municipality, census place, townsite, ghost town, fort, mission, reservation community, facility, network, service area, operator, condition, or dependency profile is intended;
- which source-role, temporal, source-vintage, sensitivity, public-safe geometry, legal-status, operational-status, and release-readiness gates apply;
- which lifecycle gates are required;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Settlements / Infrastructure implementation belongs under `pipelines/domains/settlements-infrastructure/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `settlements-infrastructure/`? | Domain docs and executable lane identify this as the broader governing lane. | CONFIRMED documentation posture / NEEDS VERIFICATION for active specs |
| What about `settlement/`? | `settlement` is a shorter alias/compatibility lane and must not create duplicate authority. | CONFIRMED current README posture / ADR still needed |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define object meaning? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Can this approve legal status, operational status, facility exposure, or release? | No. Specs can require gates only; legal/operational/release authority remains separate. | CONFIRMED boundary posture |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not legal status, not operational status, not catalog truth, and not release approval.

[⬆ Back to top](#top)

---

## 3. Settlement alias posture

`pipeline_specs/settlement/` exists as a shorter compatibility path. It must remain subordinate to this whole-domain lane unless an ADR says otherwise.

Rules:

- keep whole-domain declarative specs here;
- do not create duplicate schemas, contracts, policies, source registries, data lanes, release lanes, or public surfaces under both `settlement` and `settlements-infrastructure`;
- if a narrow settlement-only spec is placed under the alias lane, record alias status in receipts and tests;
- migration requires an ADR, path map, compatibility note, tests, and rollback note;
- a shorter path must not weaken evidence, source-role, sensitivity, legal-status, operational-status, or release controls.

[⬆ Back to top](#top)

---

## 4. Sensitivity boundary

Settlements / Infrastructure specs must fail closed when they cannot prove safe handling for:

- restricted facility or operator-sensitive details;
- condition observations and dependencies;
- exact facility geometry where public exposure is not release-approved;
- service-area or network-dependency context that requires review;
- private-property or living-person joins;
- historic settlement, mission, fort, reservation-community, burial-adjacent, or culturally sensitive context that requires review;
- generated summaries that could be mistaken for source evidence, legal status, or operational status.

Sensitive outputs require review state, EvidenceBundle closure, policy result, release decision, correction path, rollback target, and public-safe representation receipts before publication.

[⬆ Back to top](#top)

---

## 5. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
settlement candidate -> official municipal status
census place -> municipality truth
townsite candidate -> active community truth
facility context -> public restricted detail
condition observation -> current operational status
service area -> guaranteed service truth
dependency edge -> infrastructure exposure surface
generated summary -> evidence
settlement alias path -> canonical domain authority
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- settlement candidate, municipality, census place, townsite, ghost town, fort, mission, reservation community, infrastructure asset, network node, network segment, facility, service area, operator, condition observation, dependency, and public derivative states remain separately labeled;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 6. What belongs here

Appropriate contents include declarative specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- proof or dry-run profiles;
- settlement, municipality, census-place, townsite, ghost-town, fort, mission, reservation-community, infrastructure asset, network node, network segment, facility, service-area, operator, condition-observation, dependency, and public-safe map-product variants.

A good placement test:

> If the file answers “what Settlements / Infrastructure pipeline should run, with what source scope, source-role gates, sensitivity gates, legal/operational-status boundaries, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 7. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Settlements / Infrastructure pipeline code | `pipelines/domains/settlements-infrastructure/` |
| Settlement alias executable code | `pipelines/domains/settlement/` only as ADR-safe alias |
| Source connectors | `connectors/<source>` |
| Source descriptors | `data/registry/sources/settlements-infrastructure/` or accepted registry home |
| Object meaning | `contracts/domains/settlements-infrastructure/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` or accepted schema home |
| Policy and review decisions | `policy/domains/settlements-infrastructure/`, sensitivity/review roots |
| Tests | `tests/pipeline_specs/settlements-infrastructure/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/settlements-infrastructure/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 8. Spec scope

Settlements / Infrastructure specs may configure profiles for object families and candidate products such as:

- Settlement, Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, and ReservationCommunity;
- Infrastructure Asset, Network Node, Network Segment, Facility, Service Area, Operator, Condition Observation, and Dependency;
- source-vintage-aware settlement and facility identity candidates;
- public-safe settlement and infrastructure map products after evidence, policy, and release review;
- catalog, graph, Evidence Drawer, Focus Mode, correction, and rollback handoff packages.

This lane may cite other domains for context, including Roads/Rail/Trade, Hydrology, Hazards, People/DNA/Land, Agriculture, Archaeology, Habitat, and Spatial Foundation, but those contexts must not weaken source-role, sensitivity, private-property, living-person, restricted-facility, or release controls.

[⬆ Back to top](#top)

---

## 9. Lifecycle posture

Specs may target lifecycle stages, but do not create lifecycle transitions themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare input lifecycle state, expected output lifecycle state, source descriptor refs, source-role labels, source-time and valid-time handling, source-vintage checks, legal/operational-status posture, public-safe geometry posture, EvidenceBundle requirements, receipt requirements, release blockers, rollback support, and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 10. Required gates

Every Settlements / Infrastructure spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Lifecycle gate** — allowed input and output lifecycle states.
5. **Alias gate** — `settlement` remains subordinate to `settlements-infrastructure` unless ADR resolves otherwise.
6. **Legal-status gate** — settlement candidate, census place, municipality, administrative status, and official status remain distinct.
7. **Operational-status gate** — facility condition, service area, dependency, and operator-status context are not current operational truth without source-role/review closure.
8. **Sensitivity gate** — private-property, living-person, cultural, restricted-facility, dependency, and exact-location exposure fail closed where unresolved.
9. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
10. **Receipt gate** — required run, transform, validation, source-vintage, representation, redaction, dependency, or release-readiness receipts.
11. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 11. Directory contract

Recommended shape:

```text
pipeline_specs/settlements-infrastructure/
├── README.md
├── ingest.yaml                    # PROPOSED
├── normalize.yaml                 # PROPOSED
├── validate.yaml                  # PROPOSED
├── catalog.yaml                   # PROPOSED
├── triplets.yaml                  # PROPOSED
├── publish.yaml                   # PROPOSED
├── rollback.yaml                  # PROPOSED
├── watchers.yaml                  # PROPOSED
├── settlements.yaml               # PROPOSED
├── municipalities.yaml            # PROPOSED
├── census_places.yaml             # PROPOSED
├── townsites_ghost_towns.yaml     # PROPOSED
├── historic_communities.yaml      # PROPOSED
├── facilities_assets.yaml         # PROPOSED
├── networks_dependencies.yaml     # PROPOSED
└── service_areas_operators.yaml   # PROPOSED
```

These filenames are proposed placeholders until actual spec files, schema validation, CI coverage, and ADR/path resolution are implemented.

[⬆ Back to top](#top)

---

## 12. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/settlements-infrastructure/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Settlements / Infrastructure normalize implementation |
| `validate` | Declare source-role, temporal, alias, legal-status, operational-status, and sensitivity checks. | Settlements / Infrastructure validate implementation |
| `catalog` | Declare catalog closure requirements. | Settlements / Infrastructure catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Settlements / Infrastructure triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Settlements / Infrastructure publish support |
| `rollback` | Declare rollback-readiness check profile. | Settlements / Infrastructure rollback support |
| `watchers` | Declare source-change observation profiles. | Settlements / Infrastructure watcher support |
| `settlements` | Declare settlement, municipality, census-place, townsite, ghost-town, fort, mission, and community profile variants. | Domain sublane implementations |
| `infrastructure` | Declare assets, networks, facilities, service areas, operators, conditions, and dependencies. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 13. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/settlements-infrastructure/` | Declarative config only. |
| Alias spec | `pipeline_specs/settlement/` | Compatibility only; no parallel authority. |
| Executable target | `pipelines/domains/settlements-infrastructure/` or accepted pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/settlements-infrastructure/` | Stable source ref. |
| Fixture | `fixtures/pipeline_specs/settlements-infrastructure/` or accepted fixture home | Must avoid restricted facility/private/cultural exposure. |
| Spec validation test | `tests/pipeline_specs/settlements-infrastructure/` | Verifies shape, boundaries, and fail-closed gates. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/settlements-infrastructure/` or accepted receipt home | Emitted by execution, not by spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/settlements-infrastructure/`, `release/manifests/settlements-infrastructure/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 14. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.settlements_infrastructure.v1
spec_id: settlements-infrastructure.<profile>
version: 0.1.0
status: draft
domain: settlements-infrastructure
owner: <settlements-infrastructure-domain-steward>
implementation:
  target_pipeline: pipelines/domains/settlements-infrastructure/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  source_role_required: true
  temporal_fields_required: true
  legal_status_overclaim_blocked: true
  operational_status_overclaim_blocked: true
  sensitive_context_review_required: true
  public_safe_geometry_required: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  settlement_candidate_is_municipality_truth: false
  census_place_is_municipality_truth: false
  condition_observation_is_operational_status: false
  service_area_is_guaranteed_service_truth: false
  dependency_edge_is_public_exposure_surface: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 15. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/settlements-infrastructure/
├── test_spec_shape.py                       # PROPOSED
├── test_no_runtime_outputs.py               # PROPOSED
├── test_alias_boundary.py                   # PROPOSED
├── test_implementation_refs.py              # PROPOSED
├── test_source_descriptor_refs.py           # PROPOSED
├── test_settlement_municipality_boundary.py # PROPOSED
├── test_operational_status_boundary.py      # PROPOSED
├── test_sensitivity_boundary.py             # PROPOSED
├── test_required_receipts.py                # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, alias-boundary checks, legal/operational-status checks, sensitivity gates, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 16. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/settlements-infrastructure/README.md` stub;
- identifies this path as Settlements / Infrastructure declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- keeps `pipeline_specs/settlement/` subordinate as an alias path;
- blocks specs from becoming executable logic, data storage, proof storage, legal-status decisions, operational-status decisions, restricted-facility exposure, release approval, or public API/UI authority;
- defines expected profile families, lifecycle gates, alias gates, legal/operational-status gates, sensitivity gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/source-role/sensitivity/anti-collapse posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 17. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-SI-001` | Which Settlements / Infrastructure spec schema is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-SI-002` | Should `pipeline_specs/settlement/` remain an alias or be migrated fully into this path? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-SI-003` | Which first-wave source descriptors should be activated without restricted facility, private-property, living-person, or cultural-location leakage? | NEEDS VERIFICATION |
| `PIPE-SPEC-SI-004` | Which CI workflow validates Settlements / Infrastructure specs and alias boundaries? | UNKNOWN |
| `PIPE-SPEC-SI-005` | Which source-vintage, legal-status, operational-status, sensitivity, dependency, representation, and release-readiness receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-SI-006` | Should specs be split by lifecycle stage, source family, object family, settlement/infrastructure sublane, sensitivity tier, or release tier? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative and authority-safe. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, legal-status decisions, operational-status decisions, restricted-facility details, private-property joins, culturally sensitive exact locations, dependency exposure packages, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
