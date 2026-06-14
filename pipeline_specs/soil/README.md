<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-soil-readme
title: Soil Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <soil-domain-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/soil/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/domains/soil/README.md
  - docs/domains/soil/README.md
  - docs/domains/soil/ARCHITECTURE.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/runbooks/soil/PROMOTION_RUNBOOK.md
  - docs/sources/catalog/nrcs/ssurgo.md
  - docs/sources/catalog/nrcs/gssurgo.md
  - docs/sources/catalog/nrcs/soil-data-access.md
  - docs/sources/catalog/nrcs/scan-soil-climate.md
  - docs/sources/catalog/isric/README.md
  - contracts/domains/soil/
  - schemas/contracts/v1/domains/soil/
  - policy/domains/soil/
  - policy/sensitivity/soil/
  - data/registry/sources/soil/
  - data/receipts/pipeline/soil/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/soil/
  - fixtures/pipeline_specs/soil/
tags: [kfm, pipeline-specs, soil, ssurgo, gssurgo, gnatsgo, soil-data-access, soilgrids, scan, soil-moisture, pedon, horizon, hydrologic-soil-group, support-type-separation, declarative-config, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/soil stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Soil specs configure pipeline intent, source scope, lifecycle gates, support-type separation, evidence gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Support-type separation is mandatory: static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation cannot masquerade as one surface."
  - "Field-specific, owner-specific, unpublished, proprietary, private-network, cross-lane, or insufficiently evidenced soil products fail closed by default."
  - "Concrete spec filenames, schema validation, CI coverage, source activation, and release wiring remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Pipeline Specs

> Declarative configuration lane for Soil pipeline profiles, source scopes, schedules, lifecycle gates, support-type separation, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable Soil pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fsoil%2F-d62728)
![support](https://img.shields.io/badge/support--type-separation%20required-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/soil/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/soil/` — executable pipeline logic, the **how**  
**Placement posture:** Soil declarative specs belong here unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, interpretation authority, crop/yield truth, hydrology truth, geology truth, habitat truth, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Support-type separation](#3-support-type-separation)
- [4. Spec anti-collapse rules](#4-spec-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Soil spec scope](#7-soil-spec-scope)
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

`pipeline_specs/soil/` owns declarative Soil pipeline configuration.

It may describe:

- which Soil pipeline profile should run;
- which source descriptor ids are in scope;
- which source family, source vintage, support type, horizon/component/pedon scope, and observation-time checks apply;
- which lifecycle gates are required;
- which interpretation, suitability, erosion-context, hydrologic-soil-group, soil-moisture, and public-safe representation requirements apply;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Soil implementation belongs under `pipelines/domains/soil/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `soil/`? | Soil has a domain pipeline lane and needs domain-specific run profiles. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Soil objects? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Can this approve interpretation, suitability, or public release? | No. Specs can require gates only; interpretation/review/release authority remains separate. | CONFIRMED boundary posture |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not interpretation authority, not catalog truth, and not release approval.

[⬆ Back to top](#top)

---

## 3. Support-type separation

Support-type separation is the Soil-specific invariant.

Every Soil spec should preserve distinctions among:

- `authoritative_static_soil` — SSURGO / SDA-style survey evidence;
- `gridded_derivative_soil` — gSSURGO, gNATSGO, SoilGrids, and similar grids;
- `station_soil_moisture` — station observations such as Mesonet, SCAN, or USCRN where admitted;
- `satellite_soil_moisture` — satellite-grid observations such as SMAP where admitted;
- `pedon_evidence` — profile-level observations and descriptions;
- `interpretation` — erosion risk, suitability rating, hydrologic interpretation, and other derived products.

A spec that cannot declare the support type must fail closed or route to review/quarantine.

[⬆ Back to top](#top)

---

## 4. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
survey polygon -> gridded derivative truth
station reading -> countywide surface
satellite grid -> station observation
SoilGrid context -> SSURGO authority
interpretation -> measured property
suitability rating -> crop/yield truth
hydrologic soil group -> streamflow or flood truth
generated summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- map unit, component, horizon, pedon, profile view, soil property, hydrologic soil group, soil-moisture observation, erosion context, suitability rating, soil-time caveat, and public derivative states remain separately labeled;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include declarative Soil specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- proof or dry-run profiles;
- SSURGO/SDA, gSSURGO, gNATSGO, SoilGrids, SCAN, Mesonet, USCRN, SMAP, pedon, horizon, component, hydrologic-soil-group, soil-moisture, erosion-context, suitability, and public-safe map-product variants.

A good placement test:

> If the file answers “what Soil pipeline should run, with what source scope, support type, source vintage, interpretation limits, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Soil pipeline code | `pipelines/domains/soil/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<soil-source>` |
| Source descriptors | `data/registry/sources/soil/` or accepted registry home |
| Soil object meaning | `contracts/domains/soil/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/soil/` or accepted schema home |
| Policy and review decisions | `policy/domains/soil/`, `policy/sensitivity/soil/`, review roots |
| Tests | `tests/pipeline_specs/soil/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/soil/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 7. Soil spec scope

Soil specs may configure profiles for object families and candidate products such as:

- SoilMapUnit, SoilComponent, Horizon, and Component Horizon Join;
- SoilProperty and Hydrologic Soil Group;
- Pedon and SoilProfileView;
- Soil Moisture Observation from station, satellite, or gridded sources;
- ErosionRisk, SuitabilityRating, SoilTimeCaveat, and other interpretive products with explicit caveats;
- source-vintage and time-caveat records;
- public-safe generalized map products and release-reviewed derivatives.

Soil may relate to Agriculture, Hydrology, Geology, Habitat, Hazards, and Spatial Foundation, but those cross-lane relations do not transfer truth authority to Soil or weaken support-type separation.

[⬆ Back to top](#top)

---

## 8. Lifecycle posture

Specs may target lifecycle stages, but do not create lifecycle transitions themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare input lifecycle state, expected output lifecycle state, source descriptor refs, source-vintage checks, support-type labels, time-caveat posture, interpretation caveats, EvidenceBundle requirements, receipt requirements, release blockers, rollback support, and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Soil spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Support-type gate** — static survey, gridded derivative, station, satellite, pedon, or interpretation class.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Temporal/source-vintage gate** — survey date, observation time, retrieval time, processing time, source version, and time caveat.
7. **Interpretation gate** — interpretations cannot become measured properties or crop/yield/hydrology truth.
8. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
9. **Receipt gate** — required run, transform, validation, source-vintage, support-type, interpretation, representation, or release-readiness receipts.
10. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipeline_specs/soil/
├── README.md
├── ingest.yaml                    # PROPOSED
├── normalize.yaml                 # PROPOSED
├── validate.yaml                  # PROPOSED
├── catalog.yaml                   # PROPOSED
├── triplets.yaml                  # PROPOSED
├── publish.yaml                   # PROPOSED
├── rollback.yaml                  # PROPOSED
├── watchers.yaml                  # PROPOSED
├── ssurgo_sda.yaml                # PROPOSED
├── gssurgo_gnatsgo.yaml           # PROPOSED
├── soilgrids.yaml                 # PROPOSED
├── pedons_profiles.yaml           # PROPOSED
├── soil_moisture_station.yaml     # PROPOSED
├── soil_moisture_satellite.yaml   # PROPOSED
├── hydrologic_soil_group.yaml     # PROPOSED
├── erosion_suitability.yaml       # PROPOSED
└── support_type_checks.yaml       # PROPOSED
```

These filenames are proposed placeholders until actual spec files, schema validation, CI coverage, and source activation are implemented.

[⬆ Back to top](#top)

---

## 11. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/soil/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Soil normalize implementation |
| `validate` | Declare support-type, source-vintage, temporal, and interpretation checks. | Soil validate implementation |
| `catalog` | Declare catalog closure requirements. | Soil catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Soil triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Soil publish support |
| `rollback` | Declare rollback-readiness check profile. | Soil rollback support |
| `watchers` | Declare source-change observation profiles. | Soil watcher support |
| `source-family` | Declare SSURGO/SDA, gSSURGO, gNATSGO, SoilGrids, SCAN, Mesonet, USCRN, SMAP, pedon, or other admitted source variants. | Domain sublane implementations |
| `interpretation` | Declare hydrologic-soil-group, erosion, suitability, and time-caveat profiles. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/soil/` | Declarative config only. |
| Executable target | `pipelines/domains/soil/` or accepted pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/soil/` | Stable source ref. |
| Fixture | `fixtures/pipeline_specs/soil/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/soil/` | Verifies shape, support-type boundaries, and anti-collapse gates. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/soil/` or accepted receipt home | Emitted by execution, not by spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/soil/`, `release/manifests/soil/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 13. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.soil.v1
spec_id: soil.<profile>
version: 0.1.0
status: draft
domain: soil
owner: <soil-domain-steward>
implementation:
  target_pipeline: pipelines/domains/soil/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  source_role_required: true
  support_type_required: true
  source_vintage_required: true
  temporal_fields_required: true
  interpretation_caveat_required: true
  public_safe_geometry_required: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  survey_polygon_is_grid_truth: false
  station_reading_is_area_surface: false
  satellite_grid_is_station_observation: false
  interpretation_is_measured_property: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 14. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/soil/
├── test_spec_shape.py                       # PROPOSED
├── test_no_runtime_outputs.py               # PROPOSED
├── test_implementation_refs.py              # PROPOSED
├── test_source_descriptor_refs.py           # PROPOSED
├── test_support_type_required.py            # PROPOSED
├── test_source_vintage_and_temporal_fields.py # PROPOSED
├── test_interpretation_not_measurement.py   # PROPOSED
├── test_cross_lane_truth_boundaries.py      # PROPOSED
├── test_required_receipts.py                # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, support-type checks, source-vintage checks, interpretation caveats, cross-lane truth-boundary checks, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/soil/README.md` stub;
- identifies this path as Soil declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, source authority, data storage, proof storage, interpretation authority, crop/yield truth, hydrology truth, geology truth, habitat truth, release approval, or public API/UI authority;
- defines expected Soil profile families, lifecycle gates, support-type gates, source-vintage gates, interpretation gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/support-type/interpretation/anti-collapse posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-SOIL-001` | Which Soil spec schema is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-SOIL-002` | Which first-wave Soil source descriptors should be activated: SSURGO/SDA, gSSURGO, gNATSGO, SoilGrids, SCAN, Mesonet, USCRN, SMAP, or pedon/profile sources? | NEEDS VERIFICATION |
| `PIPE-SPEC-SOIL-003` | Which profile should be implemented first: SSURGO/SDA, gridded derivatives, pedons, soil moisture, hydrologic soil group, erosion, or suitability? | NEEDS VERIFICATION |
| `PIPE-SPEC-SOIL-004` | Which CI workflow validates Soil specs and support-type boundaries? | UNKNOWN |
| `PIPE-SPEC-SOIL-005` | Which support-type, source-vintage, interpretation, representation, and release-readiness receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-SOIL-006` | Should specs be split by lifecycle stage, source family, object family, support type, or interpretation family? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative and support-type safe. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, gridded or station outputs, interpretation products, crop/yield truth, hydrology truth, geology truth, habitat truth, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
