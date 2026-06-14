<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-settlement-readme
title: Settlement Pipeline Specs Alias README
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
path: pipeline_specs/settlement/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipeline_specs/settlements-infrastructure/
  - pipelines/README.md
  - pipelines/domains/settlement/README.md
  - pipelines/domains/settlements-infrastructure/README.md
  - docs/domains/settlements-infrastructure/README.md
  - docs/domains/settlements-infrastructure/ARCHITECTURE.md
  - docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md
  - data/registry/sources/settlements-infrastructure/
  - data/receipts/pipeline/settlements-infrastructure/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/settlement/
  - fixtures/pipeline_specs/settlement/
tags: [kfm, pipeline-specs, settlement, settlements-infrastructure, compatibility-alias, municipality, census-place, townsite, ghost-town, facility-context, service-area-context, declarative-config, receipts, governance]
notes:
  - "This README replaces the one-character pipeline_specs/settlement stub with a governed declarative-spec alias contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "The governing bounded context remains Settlements / Infrastructure unless an ADR resolves the settlement vs settlements-infrastructure segment naming differently."
  - "Do not create parallel schemas, contracts, source registries, policies, lifecycle data, catalog truth, or release decisions under both settlement and settlements-infrastructure without ADR/path-map/migration/rollback notes."
  - "Restricted facility, operator, condition, dependency, private-property, living-person, and culturally sensitive context fail closed by default."
  - "Concrete spec filenames, schema validation, CI coverage, source activation, and release wiring remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlement Pipeline Specs Alias

> Compatibility README for the requested `pipeline_specs/settlement/` path. This path must not become a parallel authority beside `pipeline_specs/settlements-infrastructure/`. Until an ADR resolves segment naming, use this path only for carefully bounded Settlement-sublane declarative profiles or compatibility documentation that preserves Settlements / Infrastructure governance.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-compatibility%20alias-d62728)
![canonical](https://img.shields.io/badge/governing%20context-settlements--infrastructure-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/settlement/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Bounded-context posture:** `settlement` is a compatibility/alias segment for the Settlements / Infrastructure bounded context  
**Companion implementation posture:** `pipelines/domains/settlement/` is also alias-gated; whole-context execution should resolve through `pipelines/domains/settlements-infrastructure/` unless ADR says otherwise.  
**Placement posture:** `CONFLICTED / NEEDS VERIFICATION` until the `settlement` vs `settlements-infrastructure` segment naming decision is resolved by ADR, path map, migration note, and rollback note.  
**Public posture:** no public release, data storage, source admission, legal-status decision, operational-status decision, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Alias and authority posture](#2-alias-and-authority-posture)
- [3. Sensitivity boundary](#3-sensitivity-boundary)
- [4. Spec anti-collapse rules](#4-spec-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Settlement spec scope](#7-settlement-spec-scope)
- [8. Lifecycle posture](#8-lifecycle-posture)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Spec profile families](#11-spec-profile-families)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal spec profile shape](#13-minimal-spec-profile-shape)
- [14. Tests, fixtures, and validation](#14-tests-fixtures-and-validation)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipeline_specs/settlement/` is a compatibility/alias lane for declarative Settlement-sublane pipeline profiles.

It may describe:

- which settlement-only profile should run;
- which source descriptor ids are in scope;
- which settlement candidate, municipality candidate, census-place candidate, townsite, ghost-town, fort, mission, community, or public-safe derivative profile is intended;
- which source-role, temporal, sensitivity, public-safe geometry, legal-status, and release-readiness gates apply;
- which lifecycle gates are required;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** establish `settlement` as a new canonical bounded context. The governing semantics, sensitivity posture, source-role posture, lifecycle posture, and release posture are inherited from Settlements / Infrastructure.

[⬆ Back to top](#top)

---

## 2. Alias and authority posture

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `settlement/`? | User requested this path, and it is represented as a shorter Settlement-sublane alias candidate. | PROPOSED / NEEDS VERIFICATION |
| Is `settlement` canonical? | Not proven. The visible domain docs and executable lane identify `settlements-infrastructure` as the broader governing lane. | NEEDS VERIFICATION / likely alias |
| What is canonical today? | Treat `settlements-infrastructure` as the governing bounded-context lane for docs and controls until ADR resolution. | CONFIRMED documentation posture; implementation NEEDS VERIFICATION |
| Can this path create parallel authority? | No. It must not create duplicate schemas, contracts, policies, registries, data lanes, release lanes, or public surfaces. | CONFIRMED governance posture |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Can this approve release? | No. Specs can require gates only; release authority remains separate. | CONFIRMED release separation |

> [!IMPORTANT]
> The alias must not weaken the controls of the parent bounded context. A shorter path is not permission to publish restricted facility, operator, private-land, living-person, condition, dependency, exact-location, or culturally sensitive details.

[⬆ Back to top](#top)

---

## 3. Sensitivity boundary

Settlement-sublane specs inherit the Settlements / Infrastructure sensitivity posture.

A spec must fail closed when it cannot prove safe handling for:

- restricted facility or operator-sensitive details;
- condition observations and dependencies;
- exact facility geometry where public exposure is not release-approved;
- service-area or network-dependency context that requires review;
- private-property or living-person joins;
- historic settlement, mission, fort, community, burial-adjacent, or culturally sensitive context that requires review;
- generated summaries that could be mistaken for source evidence, legal status, or operational status.

[⬆ Back to top](#top)

---

## 4. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
settlement candidate -> official municipal status
census place -> municipality truth
townsite candidate -> active community truth
fort / mission context -> public sensitive-location release
facility context -> public restricted detail
condition observation -> current operational status
service area -> guaranteed service truth
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
- settlement candidate, municipality, census place, townsite, ghost town, fort, mission, community context, infrastructure facility, operator, condition, dependency, service area, and public derivative states remain separately labeled;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include declarative Settlement-sublane specs for:

- settlement candidate profiles;
- municipality candidate profiles;
- census-place context profiles;
- townsite, ghost-town, fort, mission, and community-context profiles;
- settlement identity and source-vintage profiles;
- public-safe settlement-context derivative profiles;
- watcher, validation, catalog, triplet, publish-readiness, rollback-readiness, and dry-run profiles that preserve Settlements / Infrastructure controls.

A good placement test:

> If the file answers “what Settlement-sublane profile should run, with what scope, source-role gates, sensitivity gates, legal-status boundaries, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable settlement pipeline code | `pipelines/domains/settlement/` only as ADR-safe alias, or canonical `pipelines/domains/settlements-infrastructure/` |
| Whole-domain infrastructure pipeline logic | `pipelines/domains/settlements-infrastructure/` |
| Source connectors | `connectors/<source>` |
| Source descriptors | `data/registry/sources/settlements-infrastructure/` or accepted registry home |
| Object meaning | `contracts/domains/settlements-infrastructure/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` or accepted schema home |
| Policy and review decisions | `policy/domains/settlements-infrastructure/`, sensitivity/review roots |
| Tests | `tests/pipeline_specs/settlement/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/settlement/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 7. Settlement spec scope

Settlement-sublane specs may configure profiles for object families and candidate products such as:

- Settlement Candidate;
- Municipality Candidate;
- Census Place context;
- Townsite and ghost-town candidates;
- fort, mission, reservation-community, and historic-community context;
- settlement identity candidates and source-vintage warnings;
- public-safe, release-reviewed settlement-context derivatives.

Infrastructure assets, network nodes, network segments, facilities, service areas, operators, condition observations, and dependencies remain governed by the broader Settlements / Infrastructure lane and must not be smuggled through this alias path.

[⬆ Back to top](#top)

---

## 8. Lifecycle posture

Specs may target lifecycle stages, but do not create lifecycle transitions themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare input lifecycle state, expected output lifecycle state, source descriptor refs, source-role labels, time and source-vintage checks, legal-status posture, public-safe geometry posture, EvidenceBundle requirements, receipt requirements, release blockers, rollback support, and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Settlement-sublane spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, bounded context, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Lifecycle gate** — allowed input and output lifecycle states.
5. **Alias gate** — `settlement` remains subordinate to `settlements-infrastructure` unless ADR resolves otherwise.
6. **Legal-status gate** — settlement candidate, census place, municipality, and administrative status remain distinct.
7. **Sensitivity gate** — private-property, living-person, cultural, restricted-facility, and exact-location exposure fail closed where unresolved.
8. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
9. **Receipt gate** — required run, transform, validation, source-vintage, representation, redaction, or release-readiness receipts.
10. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended alias-safe shape:

```text
pipeline_specs/settlement/
├── README.md
├── settlement_candidates.yaml       # PROPOSED
├── municipalities.yaml              # PROPOSED
├── census_places.yaml               # PROPOSED
├── townsites_ghost_towns.yaml       # PROPOSED
├── forts_missions_communities.yaml  # PROPOSED
├── source_vintage.yaml              # PROPOSED
├── validate.yaml                    # PROPOSED
├── public_derivatives.yaml          # PROPOSED
├── publish_readiness.yaml           # PROPOSED
├── rollback.yaml                    # PROPOSED
└── watchers.yaml                    # PROPOSED
```

These filenames are proposed placeholders until actual spec files, schema validation, CI coverage, and ADR/path resolution are implemented.

[⬆ Back to top](#top)

---

## 11. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `settlement_candidates` | Declare candidate settlement intake and evidence requirements. | settlement alias or settlements-infrastructure implementation lane |
| `municipalities` | Declare municipal-status context without becoming legal authority. | settlements-infrastructure implementation lane |
| `census_places` | Declare census-place context without becoming municipality truth. | settlements-infrastructure implementation lane |
| `townsites_ghost_towns` | Declare historic settlement profile and temporal gates. | settlements-infrastructure implementation lane |
| `forts_missions_communities` | Declare sensitive historical/community context profile and review gates. | settlements-infrastructure implementation lane |
| `source_vintage` | Declare source-vintage and identity drift profile. | watcher or validation lane |
| `public_derivatives` | Declare release-reviewed public-safe derivatives only. | publish support lane |
| `watchers` | Declare source-change observation profiles. | watcher implementation lane |

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/settlement/` | Alias-gated declarative config only. |
| Canonical spec lane | `pipeline_specs/settlements-infrastructure/` | Preferred whole-domain spec lane until ADR resolution. |
| Executable target | `pipelines/domains/settlement/` as alias, or canonical `pipelines/domains/settlements-infrastructure/` | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/settlements-infrastructure/` | Stable source ref; path needs ADR confirmation where conflicted. |
| Fixture | `fixtures/pipeline_specs/settlement/` or accepted fixture home | Must avoid restricted facility/private/cultural exposure. |
| Spec validation test | `tests/pipeline_specs/settlement/` | Verifies shape, alias boundaries, and fail-closed gates. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/settlements-infrastructure/` or accepted receipt home | Emitted by execution, not by spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/settlements-infrastructure/`, `release/manifests/settlements-infrastructure/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 13. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.settlement.v1
spec_id: settlement.<profile>
version: 0.1.0
status: draft
bounded_context: settlements-infrastructure
lane: settlement
owner: <settlements-infrastructure-domain-steward>
implementation:
  target_pipeline: pipelines/domains/settlement/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  source_role_required: true
  alias_boundary_required: true
  legal_status_overclaim_blocked: true
  sensitive_context_review_required: true
  public_safe_geometry_required: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  settlement_candidate_is_municipality_truth: false
  census_place_is_municipality_truth: false
  condition_context_is_operational_status: false
  service_area_is_guaranteed_service_truth: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 14. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/settlement/
├── test_spec_shape.py                       # PROPOSED
├── test_no_runtime_outputs.py               # PROPOSED
├── test_alias_boundary.py                   # PROPOSED
├── test_implementation_refs.py              # PROPOSED
├── test_source_descriptor_refs.py           # PROPOSED
├── test_settlement_municipality_boundary.py # PROPOSED
├── test_sensitivity_boundary.py             # PROPOSED
├── test_required_receipts.py                # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, alias-boundary checks, legal-status checks, sensitivity gates, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the one-character `pipeline_specs/settlement/README.md` stub;
- marks this path as a Settlement-sublane compatibility/alias spec lane;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, legal-status decisions, operational-status decisions, restricted-facility exposure, release approval, or public API/UI authority;
- defines expected Settlement profile families, lifecycle gates, alias gates, legal-status gates, sensitivity gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/source-role/sensitivity/anti-collapse posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-SETTLE-001` | Should `pipeline_specs/settlement/` remain an alias or be migrated into `pipeline_specs/settlements-infrastructure/`? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-SETTLE-002` | Which Settlement spec schema is canonical for this alias path? | NEEDS VERIFICATION |
| `PIPE-SPEC-SETTLE-003` | Which first-wave source descriptors should be activated without restricted facility, private-property, living-person, or cultural-location leakage? | NEEDS VERIFICATION |
| `PIPE-SPEC-SETTLE-004` | Which CI workflow validates Settlement specs and alias boundaries? | UNKNOWN |
| `PIPE-SPEC-SETTLE-005` | Which source-vintage, legal-status, sensitivity, representation, and release-readiness receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-SETTLE-006` | Should Settlement specs be split by settlement type, source family, temporal period, sensitivity tier, or release tier? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative and alias-safe. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, legal-status decisions, operational-status decisions, restricted-facility details, private-property joins, culturally sensitive exact locations, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
