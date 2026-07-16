<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-agriculture-soil-moisture-readme
title: tests/domains/agriculture/soil_moisture/ — Agriculture Soil-Moisture Context Test Boundary
type: readme; directory-readme; domain-test-sublane; cross-domain-context-enforceability-boundary
version: v0.2
status: draft; repository-grounded; README-only; soil-owned-contract; schema-missing; fixtures-unpopulated; validator-documentation-only; workflows-todo-only; non-authoritative
owners: OWNER_TBD — Agriculture test steward · Agriculture domain steward · Soil domain steward · Hydrology steward · Source steward · Evidence steward · Fixture steward · Contract and schema steward · Validator steward · Policy steward · Release steward · Public-surface steward · Docs steward
created: NEEDS VERIFICATION — empty placeholder was expanded before v0.2
updated: 2026-07-16
supersedes: v0.1 Agriculture soil-moisture context test guide
policy_label: "public-review; tests; agriculture; soil-moisture; cross-domain-context; soil-owned; source-role-preserving; support-type-preserving; depth-aware; unit-aware; qc-aware; time-aware; stale-aware; no-network; synthetic-fixtures; evidence-aware; policy-aware; release-gated; no-public-authority"
current_path: tests/domains/agriculture/soil_moisture/README.md
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; canonical tests root; Agriculture parent test
  README; bounded repository search surfacing no executable test under the soil_moisture child lane;
  Agriculture soil-moisture fixture README with no confirmed payload inventory; Soil-owned
  SoilMoistureObservation semantic contract; missing paired SoilMoistureObservation schema at the
  contract-declared path; Soil moisture validator README explicitly stating no executable is
  confirmed; Agriculture source documentation distinguishing Mesonet, SCAN, USCRN, and SMAP source
  families; SCAN product documentation distinguishing watcher candidate signals from admitted
  observed station readings; SMAP product documentation distinguishing observation-class L3
  products from model-assimilated L4 products, surface from root-zone, and NRT from reprocessed
  products; Soil SMAP pipeline README documenting the same anti-collapse rules while leaving
  executable behavior unverified; and domain-agriculture and domain-soil workflows containing
  TODO-only echo jobs /
  PROPOSED soil-moisture context case contract, support-type matrix, product-profile matrix,
  temporal/depth/unit/QC tests, stale-state tests, source-role and ownership checks, aggregation and
  interpolation guardrails, evidence and policy closure, public-surface anti-overclaim tests,
  deterministic synthetic fixture profile, finite outcomes and reason codes, implementation
  sequence, definition of done, and migration plan /
  CONFLICTED Agriculture fixture guidance that groups SMAP Level-3/4 as modeled context versus the
  SMAP product page's product-specific distinction between observation-class Level-3 and
  model-assimilated Level-4; multiple source-registry path conventions in documentation; and an
  Agriculture-owned test lane depending on Soil-owned semantics and validator posture without an
  accepted integration contract or executable wiring /
  UNKNOWN collected Agriculture soil-moisture tests, fixture payloads, paired machine schema,
  validator executable, accepted support-type enum, source descriptor instances, source/product
  profiles, rights and current source terms, connector and pipeline behavior, EvidenceRef resolver,
  policy evaluator, catalog/release integration, public API/UI behavior, CI enforcement, current
  pass results, coverage, owners, branch-protection significance, and production use /
  NEEDS VERIFICATION canonical fixture identities, source-profile versions, unit and measurement
  vocabularies, depth semantics, QC vocabularies, cadence and stale thresholds, spatial-support
  vocabulary, interpolation and aggregation methods, public precision rules, reason-code vocabulary,
  registry path, CODEOWNERS, release-gate adoption, correction propagation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9ab8009f9dd2a050327b146558afdf65a38d08a4
  prior_blob: d48b0b2bef26b9049084983db7dd640abe7cfce7
  agriculture_tests_parent_blob: 35ebf2a578f2a39b4f4766cc4146aafde8124e67
  agriculture_fixture_readme_blob: 6d957a868d48e6af6dd885d85895b0c25939089c
  soil_moisture_contract_blob: 8d91c3340e886f4fb008a1ae4767fd5c892fba7e
  soil_moisture_validator_readme_blob: 74db3aae2ac4c4ab05d592c9612633441c395c77
  agriculture_sources_blob: a3cab6e8c5c3fca8d2bacfb3908254ec479722eb
  smap_product_page_blob: 702437992971975b5d2678441d1226f61f079fed
  scan_product_page_blob: e9460e920b2f58f154f6c8f1ac0ba38b17cafa15
  smap_pipeline_readme_blob: 3fff7431d342af216dccfececebebfc3121c4f97
  agriculture_no_network_runbook_blob: 15a94c9f7a92f2f258a85200c7d49f01293fd10b
  agriculture_workflow_blob: a9f5f212ef61d72fdc209d9f8b173bbf87fb1803
  soil_workflow_blob: b2cdd2d6b2d178bbe7f0a47507ac26d3f4377268
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
related:
  - ../README.md
  - ../aggregate_only/README.md
  - ../catalog_closure/README.md
  - ../policy_deny/README.md
  - ../rollback_drill/README.md
  - ../schema/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../fixtures/domains/agriculture/soil_moisture/README.md
  - ../../../../contracts/domains/soil/soil_moisture_observation.md
  - ../../../../tools/validators/domains/soil/moisture/README.md
  - ../../../../docs/domains/agriculture/SOURCES.md
  - ../../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../../docs/sources/catalog/nasa/nasa-smap.md
  - ../../../../docs/sources/catalog/nrcs/scan-soil-climate.md
  - ../../../../pipelines/domains/soil/smap_ingest/README.md
  - ../../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/workflows/domain-agriculture.yml
  - ../../../../.github/workflows/domain-soil.yml
tags: [kfm, tests, agriculture, soil-moisture, soil, hydrology, source-role, support-type, mesonet, scan, uscrn, smap, station, grid, depth, unit, qc, cadence, stale-state, evidence, policy, no-network, fail-closed]
notes:
  - "This revision changes only tests/domains/agriculture/soil_moisture/README.md."
  - "The target lane remains README-only in bounded repository evidence; no executable test is created."
  - "The semantic contract and proposed validator responsibility are Soil-owned; Agriculture consumes bounded context only."
  - "No direct soil-moisture fixture payloads were confirmed in the Agriculture fixture lane."
  - "The domain Agriculture and Soil workflows execute TODO echo commands rather than soil-moisture tests."
  - "No test, fixture, contract, schema, source descriptor, validator, pipeline, policy, workflow, receipt, proof, catalog record, release record, data object, or public route is modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/domains/agriculture/soil_moisture/` — Agriculture Soil-Moisture Context Test Boundary

> **One-line purpose.** Define the enforceability boundary for proving that Agriculture can consume Soil-owned moisture context without collapsing station observations, satellite products, modeled estimates, aggregates, depths, time states, uncertainty, or ownership into unsupported agronomic or public truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: soil moisture" src="https://img.shields.io/badge/lane-soil__moisture-success">
  <img alt="Owner: Soil semantics" src="https://img.shields.io/badge/semantics-Soil__owned-orange">
  <img alt="Maturity: README only" src="https://img.shields.io/badge/maturity-README__only-lightgrey">
  <img alt="CI: TODO only" src="https://img.shields.io/badge/CI-TODO__only-critical">
</p>

> [!IMPORTANT]
> **Agriculture consumes context; Soil owns moisture semantics.** A soil-moisture value used in a crop-stress, suitability, drought-context, irrigation-context, or reporting workflow remains bound to its Soil-owned meaning, source role, support type, unit, depth, quality, time, evidence, and limitations.

> [!CAUTION]
> **Current implementation is not established.** The test lane is README-only in bounded repository search. The fixture lane has no confirmed payloads, the paired Soil moisture schema was not found, the Soil validator lane confirms documentation rather than an executable, and both domain workflows run TODO echo commands.

> [!WARNING]
> **A numerically plausible value can still be categorically wrong.** A station reading presented as a grid, an L4 modeled estimate presented as measured truth, a surface value presented as root-zone moisture, an NRT value presented as final, or one point presented as field/county truth is a failed result even when the number is within an expected range.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Model](#soil-moisture-test-model) · [Profiles](#source-and-product-profile-matrix) · [Cases](#required-test-case-matrix) · [Fixtures](#no-network-and-fixture-posture) · [Public surfaces](#public-surface-and-answer-boundary) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Migration](#migration-correction-and-rollback) · [Open](#open-verification-register) · [Done](#definition-of-done) · [Last reviewed](#last-reviewed)

---

## Purpose

`tests/domains/agriculture/soil_moisture/` is the Agriculture test sublane for **bounded consumption of Soil-owned moisture context**.

A complete test family should answer:

1. Which source, product, support type, and role produced the value?
2. Is the input a station reading, satellite-grid product, model-assimilated estimate, derived surface, aggregate summary, candidate signal, or denied private sensor record?
3. Are measurement type, unit, depth or layer, spatial support, quality-control posture, cadence, and uncertainty explicit?
4. Are observed time, source time, valid time, retrieval time, release time, correction time, and stale state kept distinct where material?
5. Does the record preserve the owning Soil semantics and any Hydrology context without Agriculture re-owning them?
6. Does the test preserve product distinctions such as SMAP L3 versus L4, surface versus root-zone, and NRT versus reprocessed?
7. Does a station reading remain a point/depth observation rather than becoming field, county, watershed, or statewide truth without a separately governed method?
8. Do interpolated, downscaled, fused, averaged, or summarized products receive their own modeled or aggregate role and receipts?
9. Do consequential claims resolve adequate evidence and citation support?
10. Do rights, sensitivity, policy, review, release, correction, and rollback gates remain outside schema or numeric validation?
11. Do public API, UI, map, report, export, search, graph, and AI surfaces state the bounded role and uncertainty?
12. Does unsupported or ambiguous context produce a finite safe outcome instead of inferred certainty?
13. Does the default suite remain synthetic, deterministic, bounded, and no-network?
14. Does CI actually collect and execute the Agriculture soil-moisture tests?

Appropriate Agriculture uses include bounded support for:

- crop-stress context;
- drought and vegetation-condition context;
- soil-crop suitability context;
- irrigation and water-demand context;
- seasonal or period summaries;
- comparison between in-situ and satellite/model products when the comparison is explicit and non-merging;
- public-safe aggregate explanations with evidence, caveats, and release support.

This lane does not define moisture truth, certify current field conditions, issue irrigation advice, approve release, or establish production readiness.

[Back to top](#top)

---

## Authority level

**Canonical test responsibility / non-authoritative Agriculture consumer lane.**

`tests/` owns authored enforceability proof. Soil owns `SoilMoistureObservation` meaning and Soil-specific validator semantics. Agriculture may test how its consumers handle moisture context, but it must not create a parallel moisture contract, schema, source registry, validator authority, or public-serving path.

| Concern | Authority home | This lane's role |
|---|---|---|
| Executable Agriculture tests | `tests/` | Owns test modules and assertions. |
| Agriculture test organization | `tests/domains/agriculture/` | Owns the Agriculture test segment. |
| Soil moisture semantic meaning | `contracts/domains/soil/soil_moisture_observation.md` or accepted successor | Tests bounded consumption; does not redefine meaning. |
| Soil moisture machine shape | Accepted Soil schema lane | Tests shape when available; does not invent a missing schema. |
| Soil moisture validation | `tools/validators/domains/soil/moisture/` or accepted Soil validator lane | Tests integration; does not implement or relocate the validator. |
| Agriculture fixture examples | `fixtures/domains/agriculture/soil_moisture/` | Consumes synthetic examples; does not become source truth. |
| Soil fixtures | Accepted Soil fixture lanes | May supply Soil-owned contract examples after review. |
| Source identity and role | Source registry and SourceDescriptor authority | Tests references and anti-collapse; cannot assign production roles. |
| Source/product documentation | `docs/sources/catalog/` | Supplies review context; product pages are not descriptors. |
| Connectors and ingestion | `connectors/` and `pipelines/domains/soil/` | Tested when substantive; not implemented here. |
| Agriculture derived use | Agriculture contracts, packages, pipelines, and policy | Tests consumption behavior; does not implement it here. |
| Evidence and provenance | Evidence contracts and governed proof roots | Tests resolution; cannot create evidence authority. |
| Policy, rights, sensitivity | `policy/` and governed review | Tests outcomes and obligations; cannot invent permission. |
| Catalog and lifecycle state | Governed `data/` lifecycle and catalog roots | Uses synthetic references only. |
| Release, correction, rollback | `release/` | Tests boundaries; cannot approve transitions. |
| Public API/UI/map/AI | Governed application and released-artifact surfaces | Tests safe output; cannot expose a route. |
| CI workflows | `.github/workflows/` | Must invoke substantive checks; workflow presence is not proof. |

### Domain ownership law

The test boundary should preserve this relationship:

```text
Soil owns:
  SoilMoistureObservation meaning
  support-type distinctions
  unit/depth/QC/time/stale semantics
  Soil source and validator posture

Agriculture owns:
  crop-stress, suitability, drought-context, and irrigation-context use
  Agriculture-specific public claims and policy obligations
  tests proving those consumers do not overclaim

Hydrology owns:
  hydrologic and water-resource meaning when moisture context is joined

No lane may silently re-own another lane's canonical meaning.
```

### Anti-collapse rules

This lane must not collapse:

- watcher signal into admitted observation;
- station reading into satellite-grid value;
- satellite-grid value into station reading;
- SMAP L3 observation-class product into SMAP L4 model-assimilated product;
- SMAP L4 product into raw measured truth;
- surface moisture into root-zone moisture;
- NRT product into reprocessed/final product;
- point support into field, county, HUC, or statewide truth;
- one depth into another depth;
- a unit conversion into evidence that the measurement type is equivalent;
- QC-pass into source freshness;
- freshness into suitability or management advice;
- interpolation into observation;
- comparison into silent fusion;
- modeled fusion into observed source role;
- aggregation into source truth;
- schema validity into semantic validity;
- semantic validity into evidence closure;
- evidence closure into policy permission;
- policy permission into release approval;
- test success into production readiness;
- generated explanation into evidence.

[Back to top](#top)

---

## Status

### Confirmed repository evidence

| Evidence | Confirmed observation | Boundary it supports |
|---|---|---|
| Target README | Existing v0.1 guide at the requested path. | A documented test lane exists. |
| Bounded test-lane search | No executable test surfaced under `tests/domains/agriculture/soil_moisture/`. | Lane maturity remains README-only. |
| Agriculture parent test README | Lists `soil_moisture/` as a child lane with implementation unverified. | Parent/child placement is established; execution is not. |
| Agriculture fixture README | Documents soil-moisture fixtures but reports no confirmed payload inventory. | Fixture intent exists; fixture coverage does not. |
| Soil moisture contract | Defines `SoilMoistureObservation` semantics under Soil. | Semantic ownership is Soil. |
| Contract schema check | Contract states the paired Soil moisture schema was not found. | Field-level machine enforcement cannot be claimed. |
| Soil moisture validator README | Defines proposed validator responsibility and explicitly does not confirm an executable. | Validator behavior remains unimplemented or unverified. |
| Agriculture source register | Distinguishes station, satellite, modeled, and aggregate source roles. | Source-role preservation is required. |
| SCAN product page | Distinguishes watcher `candidate` signals from admitted `observed` station readings. | Watcher-as-non-publisher and source-stage separation. |
| SMAP product page | Distinguishes L3/L4, surface/root-zone, and NRT/reprocessed product postures. | Product profile must be explicit. |
| Soil SMAP pipeline README | Documents Soil-owned SMAP anti-collapse requirements and marks execution unverified. | Pipeline intent exists; runtime proof does not. |
| Agriculture no-network runbook | Requires synthetic, deterministic, no-network fixtures before live-source/public tests. | Default suite must be offline. |
| Agriculture and Soil workflows | Both contain TODO-only echo jobs. | Green jobs do not establish substantive coverage. |

### Current maturity

| Surface | Status | Consequence |
|---|---|---|
| Target README | CONFIRMED | Documentation exists. |
| Executable Agriculture soil-moisture tests | UNKNOWN / NOT SURFACED | Do not claim test coverage. |
| Direct Agriculture soil-moisture fixture payloads | UNKNOWN / NOT CONFIRMED | Do not claim positive or negative fixture coverage. |
| SoilMoistureObservation semantic contract | CONFIRMED / draft / PROPOSED | May guide tests; not an accepted production profile by itself. |
| Paired Soil moisture schema | NOT FOUND at checked path | Do not claim schema conformance or exact fields. |
| Soil moisture validator executable | UNKNOWN / NOT CONFIRMED | Do not claim unit/depth/QC checks run. |
| SourceDescriptor instances | UNKNOWN | Do not claim source identity, rights, cadence, or role activation. |
| Soil pipelines/connectors | Documentation surfaced; execution UNKNOWN | Do not claim ingest or normalization works. |
| Agriculture consumer implementation | UNKNOWN | Do not claim crop-stress/suitability integration. |
| CI enforcement | TODO-only domain workflows | A green workflow is non-substantive for this lane. |
| Public API/UI integration | UNKNOWN | Do not claim caveats or stale state are rendered. |
| Production use | UNKNOWN | No operational maturity claim. |

### Conflicts and drift to preserve visibly

1. **SMAP role wording drift.** The Agriculture fixture README groups SMAP Level-3/4 as modeled context, while the SMAP product page distinguishes observation-class Level-3 products from model-assimilated Level-4 products. Tests must bind to an exact product profile rather than applying one role to all SMAP levels.
2. **Registry-path drift.** Agriculture and source documentation reference multiple registry/path conventions. Tests should resolve an accepted SourceDescriptor handle rather than hard-code one unaccepted path.
3. **Ownership integration gap.** Agriculture owns the consumer test lane; Soil owns the semantic contract and proposed validator. The adapter/profile that binds them is not verified.
4. **Contract/schema gap.** A rich semantic contract exists while the paired machine schema is missing at the checked path.
5. **Documentation/implementation gap.** Source, fixture, validator, pipeline, and workflow documentation is extensive, but executable coverage remains unverified.

### Unknown and verification-dependent items

- accepted SoilMoistureObservation field names;
- schema version and `$id`;
- support-type enum and source-role enum binding;
- measurement-type and unit vocabulary;
- depth and layer vocabulary;
- QC and missing-value vocabulary;
- cadence and stale thresholds per source/product;
- rights and current terms;
- station and grid identity conventions;
- public precision and aggregation rules;
- interpolation/downscaling/fusion method contracts;
- evidence requirements by use case;
- policy outcome and obligation vocabulary;
- correction, supersession, and rollback propagation;
- test owners, CI owner, and branch-protection significance.

[Back to top](#top)

---

## What belongs here

This directory may contain:

- this README;
- Agriculture consumer tests for Soil-owned moisture context;
- deterministic no-network test modules;
- tests that bind exact source/product profiles to expected source roles and support types;
- tests for unit, measurement type, depth/layer, QC, cadence, time, uncertainty, stale state, and spatial support;
- tests that station, grid, modeled, derived, aggregate, candidate, and denied/private support classes remain separate;
- tests for SMAP L3/L4, surface/root-zone, and NRT/reprocessed distinctions;
- tests that SCAN/Mesonet/USCRN watcher signals do not become published observations;
- tests that interpolation, downscaling, fusion, and aggregation produce new governed roles and receipts;
- tests that Agriculture consumers cite Soil and Hydrology context rather than re-owning it;
- tests for evidence, policy, release, correction, and rollback prerequisites;
- public-surface anti-overclaim and stale-state tests;
- small lane-local helper assertions when they are truly test-only and not reusable validator implementation;
- indexes pointing to accepted fixtures, contracts, schemas, validators, and workflows.

### Proposed test module families

| Module family | Responsibility |
|---|---|
| `test_inventory.py` | Assert expected test and fixture inventory after adoption. |
| `test_source_role.py` | Preserve candidate, observed, modeled, aggregate, and restricted roles. |
| `test_support_type.py` | Preserve station, satellite grid, derivative, aggregate, and private sensor support. |
| `test_product_profiles.py` | Bind exact product/version/level/layer/cadence profiles. |
| `test_units_depth_qc.py` | Enforce required unit, depth/layer, measurement type, and QC posture. |
| `test_time_and_stale.py` | Separate time kinds, revisions, cadence, and stale state. |
| `test_spatial_support.py` | Prevent point/grid/field/county/HUC support collapse. |
| `test_aggregation_and_fusion.py` | Require method, lineage, role, receipts, and uncertainty for derived outputs. |
| `test_evidence_policy_release.py` | Enforce evidence and governed transition prerequisites. |
| `test_public_surfaces.py` | Prevent unsafe map/API/report/export/AI wording or precision. |
| `test_no_network.py` | Fail when the default suite attempts live network access. |

These filenames are **PROPOSED**. Do not claim they exist until created and collected by CI.

[Back to top](#top)

---

## What does NOT belong here

Do not place these materials in this test lane:

| Excluded material | Correct authority |
|---|---|
| SoilMoistureObservation contract prose | `contracts/domains/soil/` |
| Canonical Soil moisture JSON Schema | Accepted Soil schema lane under `schemas/` |
| Soil moisture validator implementation | `tools/validators/domains/soil/moisture/` |
| Agriculture production consumer code | Agriculture package or pipeline roots |
| Connector or watcher implementation | `connectors/` or accepted source-edge roots |
| SMAP/SCAN/Mesonet/USCRN ingestion logic | Soil pipeline/connector roots |
| SourceDescriptor records and source activation decisions | Source registry and policy roots |
| Real station readings, satellite files, rasters, source dumps, or caches | Governed lifecycle/source storage, not tests |
| General fixture libraries | `fixtures/` or accepted fixture root |
| Real farm/operator/private sensor data | Quarantine/restricted governed handling; never normal test fixtures |
| Policy rules or rights decisions | `policy/` and governed review |
| EvidenceBundles, proofs, and receipts | Governed proof/receipt roots |
| Catalog records and published layers | Governed `data/catalog/` and `data/published/` roots |
| Release manifests, decisions, corrections, or rollback cards | `release/` |
| Public API, UI, map, tile, report, export, or AI implementation | Governed application/runtime roots |
| Network calls in the default test suite | Connector/integration test lanes after explicit admission |
| Generated explanations treated as evidence | Never acceptable |

This directory must not become a second Soil domain, schema home, source registry, validator package, fixture warehouse, lifecycle store, release lane, or public-serving surface.

[Back to top](#top)

---

## Inputs

Tests should consume only bounded, inspectable inputs.

| Input family | Required posture | Failure posture |
|---|---|---|
| Soil moisture semantic contract | Pinned path/version or explicit profile identifier. | `HOLD` or `ERROR` if unresolved. |
| Machine schema | Accepted schema/profile when one exists. | Do not fabricate a schema; mark schema checks unavailable. |
| Source/product profile | Exact source, product, level, version, layer, and cadence class. | `ABSTAIN` or fail if ambiguous. |
| SourceDescriptor handle | Resolvable source identity, role, rights, cadence, and support context. | Fail closed if consequential use depends on it. |
| Synthetic fixture | Obvious mock marker, deterministic identity, public-safe values. | Reject ambiguous or live-like fixture. |
| Support type | Station, satellite grid, derivative, aggregate, candidate, private/restricted, or accepted equivalent. | Fail if missing or incompatible. |
| Source role | Candidate, observed, modeled, aggregate, context, restricted, or accepted equivalent. | Fail if missing or silently upgraded. |
| Measurement profile | Measurement type, unit, depth/layer, QC, uncertainty. | Fail/abstain when required context is missing. |
| Time profile | Observed, source, valid, retrieval, release, correction, product-version, stale state. | Fail when collapsed or contradictory. |
| Spatial support | Station/point, grid cell, generalized area, aggregate unit, hidden/restricted. | Fail when output exceeds support. |
| Method profile | Aggregation, interpolation, downscaling, fusion, comparison, model, or transform method. | Fail when a derived output lacks its own method/role/receipt. |
| Evidence support | EvidenceRef/EvidenceBundle or bounded test equivalent. | Abstain/deny where consequential claims lack support. |
| Policy/release context | Audience, purpose, sensitivity, rights, review, release, correction, rollback. | Hold/deny when required gates are unresolved. |

### Required fixture identity

Every accepted fixture should eventually include or resolve:

```yaml
fixture_id: "mock:agriculture-soil-moisture:<case>"
mock: true
scenario: "<stable-scenario-id>"
source_profile_ref: "<accepted-profile-or-mock-ref>"
expected_outcome: "PASS | DENY | ABSTAIN | HOLD | ERROR"
expected_reason_codes:
  - "<bounded-code>"
```

This shape is **PROPOSED** and must not be mistaken for an accepted schema.

### Forbidden test inputs

The default suite must reject or avoid:

- live HTTP, DNS, socket, cloud, database, station, or model-service access;
- credentials, tokens, cookies, signing material, or secrets;
- real private farm/operator/sensor records;
- exact private operational sensor coordinates;
- full source payloads or large raster products;
- production manifests, catalog records, or published artifacts used as mutable fixtures;
- current operational advice requests;
- fixtures without a clear mock/test marker.

[Back to top](#top)

---

## Outputs

A test run may emit only bounded testing outputs.

| Output | Meaning | Authority limit |
|---|---|---|
| Test assertion result | Whether one bounded expectation passed. | Not source truth or release approval. |
| Validation diagnostic | Safe field/path/reason information. | Must not leak protected input. |
| Finite test outcome | `PASS`, `DENY_EXPECTED`, `ABSTAIN_EXPECTED`, `HOLD_EXPECTED`, `ERROR_EXPECTED`, or `TEST_FAILURE`. | Proposed test vocabulary only. |
| Expected reason codes | Stable bounded reasons for failure or safe refusal. | Must align with accepted policy/validator contracts before adoption. |
| Coverage report | Which declared cases executed. | Does not prove production integration. |
| JUnit or CI artifact | Machine-readable test result. | Not a receipt/proof unless admitted into an accepted family. |
| Proposed test run receipt | Optional future process-memory record. | Requires accepted contract, home, and emission rule. |

Tests must not emit:

- source descriptors;
- canonical observations;
- catalog entries;
- EvidenceBundles or proof authority;
- policy decisions for real operations;
- release decisions;
- published layers;
- operational agronomic recommendations;
- public API responses represented as released truth.

[Back to top](#top)

---

## Soil-moisture test model

### Proof layers

A mature test suite should keep these layers independent:

| Layer | Question | Passing does not prove |
|---|---|---|
| Inventory proof | Are expected tests, fixtures, contracts, profiles, and validators present? | Correctness. |
| Shape proof | Does the payload match an accepted schema/profile? | Semantic truth or source validity. |
| Semantic proof | Does the payload preserve Soil moisture meaning? | Evidence or policy closure. |
| Source-role proof | Is the source/product role correct and preserved? | Numeric accuracy. |
| Support-type proof | Is station/grid/derivative/aggregate/private support explicit? | Public admissibility. |
| Measurement proof | Are type, unit, depth/layer, QC, uncertainty, and missingness valid? | Freshness or spatial representativeness. |
| Temporal proof | Are cadence, product version, time kinds, supersession, and stale state correct? | Release approval. |
| Spatial proof | Does output remain within its support and precision? | Agronomic suitability. |
| Method proof | Are aggregation/interpolation/fusion/downscaling methods explicit and receipted? | Ground truth. |
| Evidence proof | Do consequential claims resolve support? | Policy permission. |
| Policy proof | Is the requested use allowed/restricted/denied? | Release transition. |
| Release proof | Is a governed release state present? | Truth beyond the released evidence. |
| Public-surface proof | Do clients show correct role, time, caveat, uncertainty, and status? | Canonical data ownership. |

### Support-type model

| Support type | Minimum test posture | Forbidden upcast |
|---|---|---|
| Watcher candidate | Event/change signal only; no measurement truth. | Candidate → observed/published. |
| In-situ station reading | Station ID, depth, time, unit, QC, source role, point support. | Station → field/county/grid truth. |
| Satellite observation-class grid | Product/level, grid cell, resolution, QA, time, uncertainty. | Grid → station or field observation. |
| Model-assimilated grid | Model/product identity, layer, method, uncertainty, version, role `modeled`. | Modeled → measured/observed truth. |
| Derived/interpolated surface | Method, inputs, support, uncertainty, lineage, model/derived role. | Derived → source observation. |
| Aggregate summary | Aggregation unit, period, method, receipt, no disaggregation. | Aggregate → individual station/field truth. |
| Comparison product | Inputs remain separate; comparison method and output role explicit. | Comparison → silent fused observation. |
| Private operational sensor | Restricted identity/location, explicit rights and audience. | Private sensor → public exact output. |

### Measurement model

Tests should eventually require profile-bound handling of:

- measurement type;
- numeric value and missing-value posture;
- unit and conversion lineage;
- sensor depth, profile depth, or product layer;
- depth unit;
- QC flags and quality status;
- uncertainty/error fields;
- source revision and product version;
- support geometry/resolution;
- observed/source/valid/retrieval/release/correction time;
- stale-state calculation and caveat;
- source/product citations.

Exact field names remain **NEEDS VERIFICATION** until an accepted schema/profile exists.

### Unit and depth rules

1. Unit conversion must be deterministic, explicit, and tested against a pinned conversion rule.
2. Conversion must not make different measurement types equivalent.
3. Missing depth must fail when the source/product profile says depth is consequential.
4. Surface and root-zone products must remain distinct.
5. Station sensor depths must not be silently averaged.
6. A profile aggregate must state the method and resulting depth support.
7. Public copy must not drop depth/layer caveats when they materially constrain interpretation.

### Time and stale-state rules

Tests should preserve these time kinds where applicable:

```text
observed_time
source_time
valid_time
retrieved_time
product_version_time
release_time
correction_time
stale_as_of
```

A test should fail when:

- one time kind overwrites another;
- an NRT product is treated as reprocessed/final;
- a superseded record remains current without a replacement pointer;
- station cadence and satellite cadence are silently compared as identical;
- stale data is shown as current;
- a period average is presented as an instantaneous reading;
- a future-valid or out-of-window value is used without an explicit rule.

[Back to top](#top)

---

## Source and product profile matrix

The suite should bind each case to an exact profile. The table below records **test intent**, not accepted production configuration.

| Profile family | Expected role/support | Required distinctions | Common unsafe claim |
|---|---|---|---|
| Kansas Mesonet soil-moisture station | `observed`; station/point/depth | Station identity, sensor depth, time, QA, unit, cadence. | “The field/county has this moisture.” |
| NRCS SCAN admitted reading | `observed`; station/point/depth | Watcher candidate vs admitted reading, depth, time, QA, heartbeat/stale state. | “SCAN watcher event is published truth.” |
| NOAA USCRN soil/climate reading | `observed`; station/reference series | Station support, depth/profile, time, QA, cadence, source identity. | “Reference station equals local field condition.” |
| SMAP L3 selected product | Product-specific observation-class gridded role when accepted | Exact product/level, grid, resolution, QA, time, retrieval semantics. | “L3 grid is a station measurement.” |
| SMAP L4 surface | `modeled`; model-assimilated surface grid | L4/LDAS identity, surface layer, uncertainty, version, NRT/reprocessed status. | “Measured root-zone moisture.” |
| SMAP L4 root-zone | `modeled`; model-assimilated root-zone grid | Root-zone layer, uncertainty, version, cadence, no surface substitution. | “Measured surface moisture.” |
| Downscaled/interpolated product | `modeled` or derived profile | Method, input refs, target resolution, uncertainty, validation, lineage. | “Higher resolution means field truth.” |
| Station-period summary | `aggregate` | Station set, period, method, completeness, receipt. | “Aggregate can identify each station/field.” |
| County/HUC/grid summary | `aggregate` or modeled+aggregate | Geography/support, period, method, uncertainty, non-disaggregation. | “Summary is parcel-level truth.” |
| Station-satellite comparison | comparison/context | Inputs kept separate, alignment rules, mismatch explanation, no silent merge. | “Agreement creates a new observed source.” |
| Fused moisture indicator | `modeled` | ModelRunReceipt, inputs, feature roles, uncertainty, validation. | “Fusion output is observed soil moisture.” |

### Profile conflict rule

Because current documentation does not use one role for every SMAP product, tests must not key only on the source family name `SMAP`. They must use a product-level profile containing at least:

```yaml
source_family: nasa_smap
product_level: "L3 | L4 | NRT | other"
product_id: "<pinned-profile-id>"
layer: "surface | root_zone | other"
processing_class: "observation_class | model_assimilated | derived"
cadence_class: "nrt | standard_quality | reprocessed"
support_type: "satellite_grid"
source_role: "<accepted-role>"
```

This is a **PROPOSED test profile**, not an accepted SourceDescriptor schema.

[Back to top](#top)

---

## Required test-case matrix

### Inventory and wiring cases

| Case | Expected result |
|---|---|
| Test lane contains only README | `NEEDS_IMPLEMENTATION`; do not report coverage. |
| Fixture lane contains only README | `FIXTURE_INVENTORY_MISSING`. |
| Soil semantic contract resolves | Contract-reference check passes. |
| Paired Soil moisture schema is absent | Schema-dependent tests hold or fail visibly; no fabricated schema. |
| Validator README resolves but executable does not | `VALIDATOR_NOT_IMPLEMENTED` or `VALIDATOR_NOT_FOUND`. |
| CI does not collect this lane | `CI_COVERAGE_MISSING`. |
| Domain workflow only echoes TODO | Workflow result is non-substantive. |

### Positive controls

A suite with only negative cases can pass while blocking everything. Minimum positive controls should eventually include:

| Case | Expected bounded outcome |
|---|---|
| Synthetic station reading with source, role, support, unit, depth, QC, time, and evidence | Accepted as bounded station context. |
| Synthetic SMAP L4 surface record with modeled role and surface layer | Accepted as modeled surface context. |
| Synthetic SMAP L4 root-zone record with modeled role and root-zone layer | Accepted as modeled root-zone context. |
| Synthetic observation-class L3 profile when accepted | Accepted only under its exact product profile. |
| Station-period aggregate with method and receipt | Accepted as aggregate, not station truth. |
| Explicit station-versus-grid comparison | Accepted as comparison/context with separate inputs. |
| Stale record with stale marker and caveat | Accepted for a stale-aware display or abstaining answer. |
| Public-safe aggregate explanation with evidence and release refs | Accepted only for bounded audience/use. |

### Source-role and support-type failures

| Case | Expected posture |
|---|---|
| Watcher event labeled as observed reading | Fail closed. |
| Station reading labeled as modeled grid | Test failure. |
| SMAP L4 labeled as measured/observed truth | Deny or fail. |
| Modeled fusion labeled as observed | Deny or fail. |
| Aggregate summary labeled as observed station series | Fail. |
| Private sensor record labeled as public observed context | Deny. |
| Source role missing | Fail or abstain according to use. |
| Support type missing | Fail or abstain. |
| Source family used without exact product profile where required | Hold/abstain. |

### Product and layer failures

| Case | Expected posture |
|---|---|
| SMAP L3 and L4 treated as one undifferentiated product | Fail. |
| SMAP surface used as root-zone value | Fail. |
| SMAP root-zone used as surface value | Fail. |
| NRT treated as reprocessed/final | Fail or stale/restricted outcome. |
| Superseded NRT remains current | Fail; replacement/tombstone expected. |
| Product version missing for consequential comparison | Hold/abstain. |
| Resolution missing for grid product | Fail where spatial interpretation depends on it. |
| L4 model/assimilation identity omitted from public copy | Public-surface failure. |

### Measurement, unit, depth, and QC failures

| Case | Expected posture |
|---|---|
| Unit missing | Fail unless accepted profile explicitly permits. |
| Unsupported unit | Fail. |
| Conversion applied without recording source and target units | Fail. |
| Measurement type missing | Fail/abstain. |
| Depth missing from depth-dependent station reading | Fail. |
| Depth unit missing | Fail. |
| Multiple depths averaged silently | Fail. |
| QC-denied value treated as valid | Deny/fail. |
| QC flags omitted from public interpretation where material | Public-surface failure. |
| Missing-value sentinel treated as a measurement | Fail. |
| Uncertainty omitted from modeled product where required | Fail/abstain. |

### Temporal and stale-state failures

| Case | Expected posture |
|---|---|
| Observed time missing | Fail for observation use. |
| Retrieval time substituted for observation time | Fail. |
| Period average presented as instantaneous | Fail. |
| Stale station series labeled current | Fail. |
| Source revision ignored | Fail or hold. |
| Station and satellite values compared outside accepted alignment window | Fail/abstain. |
| Future-valid value used as current | Fail. |
| Correction time overwrites original observation time | Fail. |
| Product cadence class missing | Fail when freshness policy depends on it. |

### Spatial-support and aggregation failures

| Case | Expected posture |
|---|---|
| One station reading presented as field truth | Deny/fail. |
| One station reading presented as county truth | Deny/fail. |
| Grid cell presented as parcel truth | Deny/fail. |
| Coarse grid presented as exact farm condition | Deny/fail. |
| Interpolated surface lacks method and validation | Fail. |
| Downscaled output lacks uncertainty and lineage | Fail. |
| Aggregate lacks aggregation unit or period | Fail. |
| Aggregate lacks receipt/method support where required | Fail. |
| Aggregate is disaggregated to station/farm/operator | Deny. |
| Hidden/restricted sensor location leaks through error output | Security test failure. |

### Cross-domain ownership failures

| Case | Expected posture |
|---|---|
| Agriculture defines a new Soil moisture meaning locally | Test/review failure. |
| Agriculture duplicates the Soil moisture schema | Path/authority failure. |
| Agriculture implements a parallel Soil validator | Path/authority failure. |
| Soil moisture context is treated as Hydrology water-availability truth | Fail unless a Hydrology-owned contract supports it. |
| Moisture context becomes irrigation recommendation without decision support contract | Deny/abstain. |
| Static SSURGO map unit is treated as current moisture observation | Fail. |
| Moisture observation is treated as suitability rating | Fail unless separately derived and governed. |
| Derived crop-stress indicator is presented as moisture observation | Fail. |

### Evidence, policy, and release failures

| Case | Expected posture |
|---|---|
| Consequential claim lacks EvidenceRef/EvidenceBundle support | Abstain/deny. |
| Source citation missing | Abstain/hold. |
| Rights posture unresolved | Hold/deny. |
| Sensitivity posture unresolved | Hold/deny. |
| Public exact private sensor exposure requested | Deny. |
| Schema and validator pass but policy denies | Deny remains controlling. |
| Evidence and policy pass but release state missing | Hold; no public output. |
| Withdrawn/superseded source still powers current answer | Fail/abstain. |
| Correction does not propagate to derived Agriculture output | Fail. |
| Rollback target absent for public-impacting release | Fail/hold. |

### Public-surface failures

| Surface | Required test |
|---|---|
| Map layer | Role, support, layer/depth, time, stale state, uncertainty, and source visible or safely inspectable. |
| Tooltip/popover | No field/county overclaim from point/grid support. |
| Evidence Drawer | Resolves source/product/evidence and presents limitations. |
| API response | Finite outcome, profile/version, support, time, uncertainty, evidence, policy, and release posture. |
| Report/export | Caveats and provenance survive serialization. |
| Search/index | Withdrawn or stale records are not promoted as current. |
| Graph/triplet | Source role and support type remain explicit. |
| AI/Focus Mode | Cite-or-abstain; no agronomic advice or unsupported local truth. |
| Error response | Does not leak private coordinates, identities, tokens, or protected payloads. |

[Back to top](#top)

---

## No-network and fixture posture

### Default rule

The default suite must run without network access and without production services.

```text
synthetic fixtures
  -> local schema/profile checks when available
  -> local semantic assertions
  -> local source-role/support-type assertions
  -> local evidence/policy/release mocks
  -> bounded outputs

No live source, station, Earthdata, AWDB, Mesonet, cloud store, model, API, or database call.
```

### Minimum future fixture families

| Fixture family | Purpose |
|---|---|
| `valid_station_observed` | Complete synthetic station reading. |
| `valid_smap_l3_profile` | Product-specific observation-class grid example, if accepted. |
| `valid_smap_l4_surface` | Modeled surface product. |
| `valid_smap_l4_root_zone` | Modeled root-zone product. |
| `valid_stale_station` | Stale but correctly labeled context. |
| `valid_station_period_aggregate` | Aggregate with method and receipt. |
| `valid_station_grid_comparison` | Explicit comparison with no merge. |
| `invalid_missing_role` | Missing source role. |
| `invalid_support_collapse` | Station/grid/aggregate role collapse. |
| `invalid_surface_root_swap` | Layer semantic collapse. |
| `invalid_nrt_as_final` | Cadence/trust collapse. |
| `invalid_missing_unit_depth_qc` | Measurement context failure. |
| `invalid_spatial_overclaim` | Point/grid to field/county overclaim. |
| `invalid_missing_evidence` | Consequential unsupported claim. |
| `denied_private_sensor` | Public exposure of private operational sensor. |
| `abstain_ambiguous_product` | Source family known but product profile unresolved. |
| `rollback_superseded_product` | Correction/supersession propagation. |

### Fixture rules

Every fixture should be:

- synthetic;
- compact;
- deterministic;
- obviously marked as test data;
- safe for repository review;
- pinned to a scenario and expected outcome;
- free of credentials and live endpoints;
- free of real private sensor/farm/operator data;
- explicit about source role, support type, product profile, time, unit, depth/layer, QC, and uncertainty where relevant;
- paired with expected safe diagnostics for negative cases.

### Network denial test

A mature suite should actively fail when code attempts:

- DNS resolution;
- HTTP/HTTPS requests;
- raw sockets;
- cloud SDK calls;
- database connections;
- Earthdata/AWDB/Mesonet access;
- external model-runtime calls.

Merely intending to avoid network access is not enforceability proof.

[Back to top](#top)

---

## Public-surface and answer boundary

### Bounded language

Safe output language should identify the character of the evidence:

| Context | Acceptable bounded language | Unsafe language |
|---|---|---|
| Station | “Observed at the cited station and depth at the stated time.” | “This field/county is at X moisture.” |
| SMAP L4 | “Model-assimilated surface/root-zone moisture estimate for the cited grid/product.” | “Measured soil moisture.” |
| Aggregate | “Aggregate/period summary for the stated support and method.” | “Each location has this value.” |
| Stale record | “Last available value; stale as of …” | “Current condition.” |
| Comparison | “Station and grid products differ/agree under the stated alignment method.” | “Combined ground truth.” |
| Unsupported request | “Insufficient evidence or product profile to answer at that precision.” | Invented local estimate. |

### Required public response fields

A governed response should eventually carry or expose:

- outcome;
- bounded reason code;
- source/product profile;
- source role;
- support type;
- measurement type and unit;
- depth/layer;
- spatial support/resolution;
- observed/valid/retrieval time;
- cadence class and stale state;
- QC and uncertainty;
- evidence/citation refs;
- policy/release state;
- caveats and prohibited interpretations;
- correction/supersession state where applicable.

Exact response schema remains **NEEDS VERIFICATION**.

### Agronomic-advice guardrail

Soil-moisture context alone must not produce:

- irrigation scheduling instructions;
- pesticide/fertilizer application advice;
- crop-loss determination;
- field-specific suitability certification;
- regulatory or insurance determination;
- emergency or life-safety advice.

Such outputs require separately governed decision-support contracts, evidence, policy, review, and release posture. In their absence, tests should expect `ABSTAIN`, `NARROWED`, `HOLD`, or `DENY` rather than fluent advice.

[Back to top](#top)

---

## Finite outcomes and reason codes

### Proposed test outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The bounded expected behavior was observed. |
| `DENY_EXPECTED` | Unsafe/publicly disallowed use was correctly denied. |
| `ABSTAIN_EXPECTED` | Evidence, profile, or interpretation was insufficient. |
| `HOLD_EXPECTED` | Review, rights, policy, schema, release, or source state was unresolved. |
| `RESTRICT_EXPECTED` | Use was allowed only with aggregation, caveat, redaction, audience, or precision obligations. |
| `ERROR_EXPECTED` | Test intentionally exercised unavailable/malformed machinery and confirmed fail-closed handling. |
| `TEST_FAILURE` | Behavior did not match the governed expectation. |
| `NOT_IMPLEMENTED` | Required executable surface is absent; must not be reported as passing coverage. |

### Proposed safe reason-code families

| Code | Trigger |
|---|---|
| `SOURCE_PROFILE_MISSING` | Exact source/product profile unresolved. |
| `SOURCE_ROLE_MISSING` | Source role absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate/observed/modeled/aggregate role changed improperly. |
| `SUPPORT_TYPE_MISSING` | Station/grid/aggregate/private support absent. |
| `SUPPORT_TYPE_COLLAPSE` | Support classes treated as interchangeable. |
| `PRODUCT_LEVEL_AMBIGUOUS` | SMAP or other family lacks level/product identity. |
| `SURFACE_ROOT_ZONE_COLLAPSE` | Surface and root-zone semantics mixed. |
| `NRT_FINAL_COLLAPSE` | Preliminary/NRT treated as reprocessed/final. |
| `UNIT_MISSING` | Required unit absent. |
| `MEASUREMENT_TYPE_MISSING` | Measurement basis absent. |
| `DEPTH_CONTEXT_MISSING` | Required depth/layer absent. |
| `QC_CONTEXT_MISSING` | Required QC posture absent. |
| `TIME_CONTEXT_MISSING` | Required time kind absent. |
| `STALE_STATE_UNRESOLVED` | Freshness cannot be established. |
| `SPATIAL_SUPPORT_OVERCLAIM` | Output precision exceeds support. |
| `METHOD_RECEIPT_MISSING` | Derived/aggregate method or receipt absent. |
| `EVIDENCE_UNRESOLVED` | Evidence support does not close. |
| `RIGHTS_UNRESOLVED` | Rights/current terms unresolved. |
| `SENSITIVITY_UNRESOLVED` | Exposure posture unresolved. |
| `POLICY_DENIED` | Policy blocks use. |
| `RELEASE_STATE_MISSING` | Public output lacks governed release. |
| `CORRECTION_NOT_PROPAGATED` | Supersession/correction did not reach downstream output. |
| `PRIVATE_SENSOR_EXPOSURE` | Restricted operational sensor detail would leak. |
| `DOMAIN_AUTHORITY_COLLAPSE` | Agriculture redefines Soil/Hydrology meaning. |
| `FIXTURE_INVENTORY_MISSING` | Required fixture payloads absent. |
| `VALIDATOR_NOT_IMPLEMENTED` | Validator documentation exists without executable. |
| `SCHEMA_NOT_AVAILABLE` | Paired machine schema absent. |
| `CI_COVERAGE_MISSING` | Workflow does not collect substantive lane tests. |

These codes are **PROPOSED**. They must be reconciled with accepted validator, policy, runtime, and release vocabularies before implementation.

[Back to top](#top)

---

## Validation

### Documentation validation performed for this revision

- one top-level H1 outside fenced blocks;
- balanced fenced code blocks;
- no trailing whitespace or tabs;
- required folder-README sections present in order;
- high-signal credential-pattern scan;
- one-file diff scope after publication branch creation;
- remote Git blob readback after write.

### Repository inspection commands

These commands inspect current posture; they do not establish substantive test success by themselves.

```bash
find tests/domains/agriculture/soil_moisture -maxdepth 5 -type f | sort
find fixtures/domains/agriculture/soil_moisture -maxdepth 5 -type f | sort
find contracts/domains/soil schemas/contracts/v1/domains/soil \
  tools/validators/domains/soil/moisture -maxdepth 5 -type f 2>/dev/null | sort
```

```bash
git grep -n -E 'SoilMoistureObservation|soil[_ -]moisture|SMAP|SCAN|Mesonet|USCRN' -- \
  tests fixtures contracts schemas tools pipelines policy .github/workflows
```

```bash
git grep -n -E 'echo TODO|NOT_IMPLEMENTED|NotImplementedError' -- \
  .github/workflows/domain-agriculture.yml \
  .github/workflows/domain-soil.yml \
  tools/validators/domains/soil/moisture
```

### Proposed substantive commands after implementation

```bash
pytest -q tests/domains/agriculture/soil_moisture
```

```bash
pytest -q tests/domains/agriculture/soil_moisture \
  --disable-socket
```

```bash
python tools/validators/domains/soil/moisture/<accepted_entrypoint>.py \
  --fixtures fixtures/domains/agriculture/soil_moisture \
  --no-network
```

The entrypoint and flags above are **PROPOSED**.

### Required validation layers

| Layer | Required checks |
|---|---|
| Collection | Tests and fixtures are discovered; zero-test runs fail. |
| JSON/shape | Payload parses and matches accepted schema/profile when available. |
| Contract | Soil-owned semantics and product profiles are preserved. |
| Source role | Candidate/observed/modeled/aggregate/restricted roles do not drift. |
| Support type | Station/grid/derived/aggregate/private classes stay distinct. |
| Measurement | Unit, type, depth/layer, QC, uncertainty, missingness. |
| Temporal | Time kinds, cadence, stale state, revisions, supersession. |
| Spatial | Support/resolution/precision and non-overclaim. |
| Method | Aggregation/interpolation/fusion/downscaling method and lineage. |
| Evidence | Evidence/citation closure for consequential outputs. |
| Policy | Rights, sensitivity, audience, purpose, and obligations. |
| Release | No public path without governed release/correction/rollback support. |
| Public surface | Bounded wording, caveats, trust state, safe errors. |
| Network | Default suite actively blocks live access. |

### CI admission criteria

A workflow may be described as enforcing this lane only when it:

1. invokes a concrete test command for `tests/domains/agriculture/soil_moisture/`;
2. fails when zero tests are collected;
3. consumes verified fixture payloads;
4. blocks network access;
5. runs positive controls and negative cases;
6. publishes machine-readable results;
7. fails on test failure;
8. does not rely on `echo TODO`, unconditional success, or `|| true`;
9. is required by the relevant protected promotion path;
10. records the tested contract/profile versions.

The current Agriculture and Soil domain workflows do not meet these criteria because their inspected jobs only echo TODO messages.

### Acceptance matrix for this README

| Criterion | Required result |
|---|---|
| Soil ownership is explicit | PASS |
| Agriculture consumer scope is explicit | PASS |
| README-only maturity is not overstated | PASS |
| Missing schema, fixtures, validator, and CI are visible | PASS |
| Station/grid/modeled/aggregate/private support stays separate | PASS |
| Product-level SMAP distinctions are visible | PASS |
| Unit/depth/QC/time/stale requirements are explicit | PASS |
| Spatial support and aggregation overclaim are blocked | PASS |
| Evidence, policy, release, correction, and rollback remain separate | PASS |
| No-network and public-safe fixture posture is explicit | PASS |
| Positive controls and negative cases are documented | PASS |
| Executable behavior changed by this revision | NOT APPLICABLE — documentation only |

[Back to top](#top)

---

## Review burden

This lane is trust-significant because moisture context can be converted into apparently precise crop, drought, irrigation, or field claims even when the underlying evidence is a point reading, coarse grid, modeled estimate, stale product, or aggregate.

### Required reviewers for substantive implementation

- Agriculture domain steward;
- Soil domain steward;
- test/QA steward;
- source steward for affected source profiles;
- contract and schema stewards;
- validator steward;
- evidence steward;
- policy, rights, and sensitivity stewards;
- release steward for public-impacting behavior;
- Hydrology steward when water-resource meaning is involved;
- public API/UI or governed-AI owner when output wording changes.

### Review checklist

- [ ] Test consumes Soil-owned meaning rather than duplicating it.
- [ ] Exact source/product profile is pinned.
- [ ] Source role and support type are explicit.
- [ ] L3/L4, surface/root-zone, and NRT/reprocessed distinctions are preserved where applicable.
- [ ] Measurement type, unit, depth/layer, QC, uncertainty, and missingness are handled.
- [ ] Time kinds, cadence, revision, supersession, and stale state are tested.
- [ ] Spatial support does not exceed station/grid/aggregate evidence.
- [ ] Interpolation, aggregation, downscaling, comparison, and fusion produce new governed roles and lineage.
- [ ] Positive controls prove bounded allowed behavior.
- [ ] Negative cases fail for bounded reasons.
- [ ] Fixtures are synthetic, public-safe, and obviously mocked.
- [ ] Network access is actively blocked.
- [ ] Evidence, policy, release, correction, and rollback checks remain separate.
- [ ] Public wording preserves modeled/observed/aggregate character and caveats.
- [ ] Errors do not leak protected data.
- [ ] CI collects the lane and fails on zero tests.
- [ ] Documentation is updated with behavior changes.

### Change significance

Treat changes as elevated when they alter:

- source role or support type;
- accepted product profiles;
- unit/depth/layer semantics;
- QC, missingness, uncertainty, or stale thresholds;
- interpolation/downscaling/aggregation/fusion rules;
- public precision or caveat requirements;
- rights/sensitivity posture;
- evidence requirements;
- policy outcomes;
- release/correction/rollback behavior;
- public API/UI/AI wording.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| `tests/domains/agriculture/` | Parent Agriculture enforceability-proof lane. |
| `tests/domains/agriculture/aggregate_only/` | Aggregate preservation and precision anti-collapse. |
| `tests/domains/agriculture/policy_deny/` | Deny/abstain/fail-closed behavior. |
| `tests/domains/agriculture/schema/` | Agriculture schema and authority-drift checks. |
| `tests/domains/agriculture/catalog_closure/` | Evidence/catalog/release closure. |
| `tests/domains/agriculture/rollback_drill/` | Reversibility and downstream invalidation. |
| `fixtures/domains/agriculture/soil_moisture/` | Agriculture soil-moisture-shaped synthetic examples; payload inventory unconfirmed. |
| `contracts/domains/soil/soil_moisture_observation.md` | Soil-owned semantic contract. |
| `schemas/contracts/v1/domains/soil/` | Candidate Soil schema home; paired moisture schema absent at checked path. |
| `tools/validators/domains/soil/moisture/` | Proposed Soil moisture validator lane; executable unconfirmed. |
| `docs/domains/agriculture/SOURCES.md` | Agriculture source-family and source-role guidance. |
| `docs/sources/catalog/nasa/nasa-smap.md` | SMAP product distinctions and caveats. |
| `docs/sources/catalog/nrcs/scan-soil-climate.md` | SCAN station/watcher/source-role posture. |
| `pipelines/domains/soil/smap_ingest/` | Soil-owned SMAP ingest intent; runtime maturity unverified. |
| `data/registry/` source lanes | SourceDescriptor and source activation authority after path resolution. |
| `data/proofs/` and `data/receipts/` | Evidence and process-memory authority. |
| `data/catalog/` | Governed catalog projections. |
| `release/` | Publication, correction, supersession, withdrawal, and rollback authority. |
| `.github/workflows/domain-agriculture.yml` | Agriculture workflow scaffold; TODO-only. |
| `.github/workflows/domain-soil.yml` | Soil workflow scaffold; TODO-only. |

### Compatibility and path caution

Current docs use multiple source-registry path conventions. This README therefore refers to **accepted source registry and SourceDescriptor authority** rather than selecting a new canonical path. Any path consolidation requires Directory Rules review, migration notes, and an ADR or equivalent accepted decision.

[Back to top](#top)

---

## ADRs

### Existing governing decisions and doctrine

This lane should remain consistent with:

- contracts-versus-schemas separation;
- domain placement law;
- source-role anti-collapse;
- policy-aware and cite-or-abstain behavior;
- governed API trust membrane;
- promotion as a governed state transition;
- receipt/proof/catalog/release separation;
- correction and rollback visibility;
- watcher-as-non-publisher behavior;
- Directory Rules responsibility-root placement.

### ADR decisions still needed

| Decision | Status | Why it matters |
|---|---|---|
| Canonical SoilMoistureObservation schema/profile | NEEDS VERIFICATION | Tests cannot enforce exact fields without machine shape. |
| Agriculture-to-Soil context adapter/profile | PROPOSED | Prevents Agriculture from duplicating Soil semantics. |
| Canonical support-type vocabulary | NEEDS VERIFICATION | Station/grid/derivative/aggregate/private distinctions must be machine-stable. |
| Product-profile registry | NEEDS VERIFICATION | Source family alone is insufficient for SMAP role decisions. |
| Unit/depth/measurement vocabulary | NEEDS VERIFICATION | Prevents silent semantic conversion. |
| QC and stale-state vocabulary | NEEDS VERIFICATION | Enables deterministic bounded diagnostics. |
| Interpolation/downscaling/fusion contract | NEEDS VERIFICATION | Derived products need explicit role, method, uncertainty, and receipts. |
| Public precision and aggregation rules | NEEDS VERIFICATION | Prevents field/county overclaim. |
| Source-registry path consolidation | CONFLICTED | Current docs reference multiple homes. |
| Reason-code ownership | NEEDS VERIFICATION | Test, validator, policy, and runtime codes must align. |
| CI ownership and promotion significance | NEEDS VERIFICATION | Determines whether failures block release. |

### Decision rule

Until these decisions are accepted:

- do not invent field names;
- do not select one registry path as canonical;
- do not label every SMAP product with one role;
- do not define a parallel Agriculture moisture schema or validator;
- do not claim a green workflow proves coverage;
- fail safe or narrow scope when product, support, time, unit, depth, evidence, or policy context is unresolved.

[Back to top](#top)

---

## Implementation sequence

The smallest sound implementation path is:

1. **Accept the ownership split.** Confirm Soil owns semantic meaning and validation; Agriculture owns consumer tests.
2. **Select a machine profile.** Accept or create the paired Soil moisture schema/profile under the correct schema root.
3. **Resolve source/product profiles.** Pin Mesonet, SCAN, USCRN, SMAP L3/L4, layers, cadence classes, units, depth, QC, and rights posture.
4. **Create synthetic fixtures.** Add positive, invalid, denied, abstaining, stale, correction, and rollback examples.
5. **Implement the Soil validator.** Keep reusable moisture validation in the Soil validator lane.
6. **Implement Agriculture adapter assertions.** Test that Agriculture consumers preserve Soil-owned fields and limitations.
7. **Add source-role/support-type tests.** Cover candidate, observed, modeled, aggregate, and restricted cases.
8. **Add measurement/time/spatial tests.** Unit, depth, layer, QC, uncertainty, cadence, stale state, and precision.
9. **Add method tests.** Aggregation, interpolation, downscaling, comparison, and fusion with lineage/receipts.
10. **Add evidence/policy/release tests.** Ensure public output cannot bypass governed gates.
11. **Add public-surface tests.** Map, API, report, export, search, graph, and AI wording/state.
12. **Enforce no-network.** Fail on external access.
13. **Wire CI.** Fail on zero collection, failed cases, missing fixtures, or unresolved profiles.
14. **Record correction and rollback behavior.** Ensure superseded products and derived outputs update safely.
15. **Update documentation and registers.** Keep inventory and maturity aligned with implementation.

Each step should be independently reviewable and reversible.

[Back to top](#top)

---

## Migration, correction, and rollback

### Documentation rollback

This README can be reverted independently because it changes no executable behavior or governed state.

### Future test migration

When executable tests are added:

1. preserve history and stable scenario IDs;
2. move tests only after Directory Rules and CI ownership are confirmed;
3. update imports, fixture paths, workflow collection, and documentation in one governed change;
4. retain compatibility pointers during transition where needed;
5. verify zero orphaned tests or fixtures;
6. record rollback instructions for the migration.

### Contract/schema correction

When the Soil semantic contract or future schema changes:

- version the contract/profile;
- update valid and invalid fixtures;
- preserve prior-version cases where compatibility matters;
- add migration tests;
- update validator and Agriculture consumer tests together;
- record changed interpretation, not just changed fields;
- prevent old and new meanings from sharing one unversioned identity.

### Source/product correction

When a source product is revised or superseded:

- preserve original source/product identity and time;
- record replacement/supersession linkage;
- invalidate or re-evaluate dependent Agriculture outputs;
- update stale/current public state;
- preserve audit history;
- rerun affected evidence, policy, release, and public-surface tests.

### Rollback expectations

A test-suite rollback should restore:

- previous scenario inventory;
- previous expected outcomes and reason codes;
- previous contract/profile pin;
- previous CI collection behavior;
- previous documentation links.

It must not silently restore an unsafe source-role, support-type, product-profile, precision, or public-wording rule.

[Back to top](#top)

---

## Open verification register

| Item | Status | Verification needed |
|---|---|---|
| Executable test inventory | UNKNOWN | Recursive repository inventory and pytest collection. |
| Fixture payload inventory | UNKNOWN | Inspect Agriculture and Soil moisture fixture directories. |
| Paired Soil moisture schema | NOT FOUND at checked path | Decide schema/profile home and implement/review. |
| Soil moisture validator executable | UNKNOWN | Inspect/create accepted entrypoint and tests. |
| Agriculture consumer implementation | UNKNOWN | Inspect packages/pipelines/API/UI integration. |
| SourceDescriptor instances | UNKNOWN | Resolve accepted registry and inspect source profiles. |
| SMAP L3 selected product | NEEDS VERIFICATION | Pin exact product and role. |
| SMAP L4 product profiles | NEEDS VERIFICATION | Pin surface/root-zone, NRT/reprocessed, versions, uncertainty. |
| Mesonet/SCAN/USCRN profiles | NEEDS VERIFICATION | Pin station/depth/QC/cadence/right profiles. |
| Unit vocabulary | NEEDS VERIFICATION | Accept measurement types and conversion rules. |
| Depth/layer vocabulary | NEEDS VERIFICATION | Accept sensor depth and product-layer semantics. |
| QC/missing/stale vocabulary | NEEDS VERIFICATION | Align source, validator, policy, and public states. |
| Spatial support vocabulary | NEEDS VERIFICATION | Station/grid/field/aggregate/restricted rules. |
| Aggregation/interpolation/fusion contracts | UNKNOWN | Define method, uncertainty, receipts, validation. |
| Evidence requirements | NEEDS VERIFICATION | Define by use and consequence. |
| Public precision rules | NEEDS VERIFICATION | Define map/API/report/AI constraints. |
| Rights and current terms | NEEDS VERIFICATION | Verify against current publishers before activation. |
| Policy and release integration | UNKNOWN | Inspect executable bundles and release gates. |
| Correction/rollback propagation | UNKNOWN | Test source/product supersession and downstream invalidation. |
| CI enforcement | NOT ESTABLISHED | Replace TODO workflows with substantive commands. |
| CODEOWNERS and reviewers | NEEDS VERIFICATION | Confirm ownership and separation of duties. |
| Production use | UNKNOWN | Require runtime, logs, releases, and public-surface evidence. |

[Back to top](#top)

---

## Definition of done

This lane is not complete until all applicable conditions are met:

### Placement and ownership

- [ ] Agriculture consumer test ownership is accepted.
- [ ] Soil semantic and validator ownership is accepted.
- [ ] No parallel Agriculture moisture contract/schema/validator authority exists.
- [ ] Source registry and profile homes are resolved.

### Contract and schema

- [ ] SoilMoistureObservation semantic contract is reviewed and versioned.
- [ ] Paired machine schema/profile exists at an accepted path.
- [ ] Support type, source role, unit, depth/layer, QC, time, stale, uncertainty, and spatial support are machine-represented where required.
- [ ] Product-level SMAP distinctions are represented.

### Fixtures

- [ ] Synthetic valid station fixture exists.
- [ ] Synthetic valid L3 profile fixture exists when applicable.
- [ ] Synthetic valid L4 surface and root-zone fixtures exist.
- [ ] Aggregate, comparison, stale, denied, abstain, correction, and rollback fixtures exist.
- [ ] Fixtures are obviously mocked and public-safe.
- [ ] Negative fixtures have bounded expected diagnostics.

### Tests and validators

- [ ] Soil moisture validator executable exists and is fixture-tested.
- [ ] Agriculture test modules exist and are collected.
- [ ] Positive controls pass.
- [ ] Negative source-role/support-type/product/layer/unit/depth/QC/time/spatial cases fail correctly.
- [ ] Aggregation/interpolation/fusion cases require method, role, uncertainty, and receipts.
- [ ] Evidence/policy/release/public-surface boundaries are tested.
- [ ] Network access is actively blocked.
- [ ] Zero-test collection fails.

### CI and governance

- [ ] Agriculture and/or Soil workflow invokes substantive commands.
- [ ] Workflow failure blocks the appropriate promotion path.
- [ ] Machine-readable results are retained under an accepted artifact policy.
- [ ] Owners and reviewers are confirmed.
- [ ] Documentation, inventories, contracts, schemas, fixtures, and validators agree.
- [ ] Correction and rollback paths are tested.

### Publication boundary

- [ ] Public output identifies observed/modeled/aggregate character.
- [ ] Depth/layer, time, stale state, spatial support, QC, and uncertainty survive projection.
- [ ] No station/grid product is presented as unsupported field/county truth.
- [ ] No private operational sensor detail leaks.
- [ ] AI and narrative surfaces cite or abstain.
- [ ] Release state, correction, and supersession are visible.

Until then, the lane remains **draft / README-only / implementation unconfirmed**.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-16 |
| Review status | Repository-grounded v0.2 documentation update |
| Evidence base | `main@9ab8009f9dd2a050327b146558afdf65a38d08a4` plus pinned blobs in the meta block |
| Implementation status | README-only test lane; schema, fixtures, validator executable, CI, and runtime integration unconfirmed |
| Next review trigger | First executable test, first fixture payload, accepted Soil moisture schema/profile, validator implementation, source-profile decision, CI wiring, public-surface integration, contract change, correction, or rollback event |
| Rollback target | Prior blob `d48b0b2bef26b9049084983db7dd640abe7cfce7` |

[Back to top](#top)
