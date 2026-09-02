<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-agriculture-ssurgo-lineage-readme
title: tests/domains/agriculture/ssurgo_lineage/ — Agriculture SSURGO Lineage Test Boundary
type: readme; directory-readme; domain-test-sublane; cross-domain-lineage-enforceability-boundary
version: v0.2
status: draft; repository-grounded; README-only; fixture-payloads-unconfirmed; validator-readmes-only; workflow-todo-only; source-role-conflicted; non-authoritative
owners: OWNER_TBD — Agriculture test steward · Agriculture steward · Soil steward · Source steward · Evidence steward · Contract and schema steward · Fixture steward · Validation steward · Policy steward · Catalog steward · Release steward · Public-surface steward · Docs steward
created: NEEDS VERIFICATION — empty placeholder was expanded before v0.2
updated: 2026-07-16
supersedes: v0.1 Agriculture SSURGO-lineage test guide
policy_label: "public-review; tests; agriculture; ssurgo; gssurgo; lineage; soil-owned; source-role-preserving; support-type-preserving; mukey; cokey; chkey; source-vintage; evidence-aware; policy-aware; release-gated; no-network; synthetic-fixtures; no-public-authority"
current_path: tests/domains/agriculture/ssurgo_lineage/README.md
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; canonical tests responsibility root;
  Agriculture parent test lane; bounded search returning no executable test for this child lane;
  Agriculture SSURGO fixture README with no confirmed payload inventory; Soil-owned SSURGO product,
  Soil ingest, Soil lineage-validator, Agriculture-facing Soil-join-validator, and shared join-validator
  documentation; SSURGO, SDA, and gSSURGO separation; MUKEY/COKEY/CHKEY hierarchy; source-vintage,
  spatial/tabular coupling, EvidenceRef consumption, Agriculture-owned derivative boundary, and
  TODO-only Agriculture and Soil workflows / PROPOSED executable test contract, fixture cases,
  finite outcomes, reason codes, public-surface checks, correction cascade, CI admission, implementation
  sequence, and definition of done / CONFLICTED gSSURGO source-role posture across repository docs;
  source-role versus support-type terminology; multiple source-registry path conventions; overlapping
  validator routing lanes; and rich documentation versus absent executable proof / UNKNOWN current
  source descriptor instances, accepted schema/contract profiles, executable validators, fixture payloads,
  pipeline behavior, catalog closure, release integration, public API/UI behavior, current test results,
  owners, branch-protection significance, and production use / NEEDS VERIFICATION canonical SSURGO and
  gSSURGO profiles, join-key vocabularies, source-vintage rules, weighting methods, aggregation receipts,
  source-registry topology, reason-code contract, CODEOWNERS, release-gate adoption, correction propagation,
  and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 1852516d033a6180507c7ad0b4390689a401c988
  prior_blob: fb36559ca559de466329aee190fdeb3000365b2a
  agriculture_fixture_ssurgo_blob: 4a5dd906be70f7cb2e5d4f89d81b51013c7ca22b
  ssurgo_product_page_blob: 02955e076e2b2b621cf1229cd430b7094081b3a1
  gssurgo_product_page_blob: e3a8a053889e31437c6d900cfd7f7ef0a2f08442
  agriculture_sources_blob: a3cab6e8c5c3fca8d2bacfb3908254ec479722eb
  soil_ssurgo_ingest_blob: eb457f55d6546219e0bc898dab85c4b76739a825
  soil_lineage_validator_readme_blob: 8d7c6489113015d13e8000969861a0561b94b017
  agriculture_soil_join_validator_readme_blob: 6374ad7010737bed5c95156348267e04272edfaf
  shared_agriculture_soil_join_readme_blob: d6f3cf61e0e5ac1fc15ae508e9168b4f25c2a3a2
  agriculture_contract_index_blob: 27e6b7648d416e0c01da63c339210f9b072a98c5
  soil_source_registry_readme_blob: 8394245909e6e46d891db29afe31c0af8d1d6574
  agriculture_validator_readme_blob: 40d268b425d9939ab6a8cda7bd197ba758572d3f
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
  - ../soil_moisture/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../fixtures/domains/agriculture/ssurgo/README.md
  - ../../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../../docs/sources/catalog/nrcs/gssurgo.md
  - ../../../../docs/domains/agriculture/SOURCES.md
  - ../../../../pipelines/domains/soil/ssurgo_ingest/README.md
  - ../../../../tools/validators/domains/soil/lineage/README.md
  - ../../../../tools/validators/domains/agriculture/soil-join/README.md
  - ../../../../tools/validators/joins/agriculture-soil/README.md
  - ../../../../contracts/domains/agriculture/README.md
  - ../../../../data/registry/sources/soil/README.md
  - ../../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/workflows/domain-agriculture.yml
  - ../../../../.github/workflows/domain-soil.yml
tags: [kfm, tests, agriculture, soil, ssurgo, gssurgo, sda, lineage, mukey, cokey, chkey, source-vintage, support-type, source-role, evidence, catalog, policy, release, no-network, fail-closed]
notes:
  - "This revision changes only tests/domains/agriculture/ssurgo_lineage/README.md."
  - "The child lane remains README-only in bounded repository evidence; no executable test is created."
  - "The Agriculture SSURGO fixture lane has no confirmed fixture payload inventory."
  - "Relevant Soil and Agriculture validator lanes are documentation-first; no executable is established by this change."
  - "The gSSURGO source-role conflict is recorded, not resolved by assertion."
  - "No test, fixture, source descriptor, contract, schema, validator, connector, pipeline, policy, workflow, receipt, proof, catalog record, release record, data object, or public route is modified."
  - "Main advanced during authoring only through an unrelated runtime-proof domain README merge."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/domains/agriculture/ssurgo_lineage/` — Agriculture SSURGO Lineage Test Boundary

> **One-line purpose.** Define the enforceability boundary for proving that Agriculture can consume Soil-owned SSURGO, SDA, and gSSURGO context without losing source identity, survey vintage, MUKEY/COKEY/CHKEY continuity, spatial and tabular lineage, support type, evidence, policy, correction, rollback, or public precision limits.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: SSURGO lineage" src="https://img.shields.io/badge/lane-SSURGO__lineage-success">
  <img alt="Semantics: Soil owned" src="https://img.shields.io/badge/semantics-Soil__owned-orange">
  <img alt="Maturity: README only" src="https://img.shields.io/badge/maturity-README__only-lightgrey">
  <img alt="CI: TODO only" src="https://img.shields.io/badge/CI-TODO__only-critical">
</p>

> [!IMPORTANT]
> **Agriculture consumes governed Soil evidence; it does not re-own SSURGO truth.** SoilMapUnit, SoilComponent, Horizon, SoilProperty, hydrologic group, survey interpretation, and source-vintage meaning remain Soil-owned. Agriculture may create a separately identified and governed derivative such as crop-suitability context.

> [!CAUTION]
> **Current implementation is not established.** Bounded repository search surfaced only this README under the child test lane. The paired Agriculture fixture lane has no confirmed payloads, relevant validator lanes confirm documentation rather than executables, and the Agriculture and Soil workflows execute TODO commands.

> [!WARNING]
> **A successful join can still be a lineage failure.** A valid MUKEY that links mismatched source vintages, a component rollup that loses COKEY weights, a horizon property promoted without CHKEY/depth lineage, or a gSSURGO cell presented at finer precision than the underlying survey supports must fail even if the final value appears plausible.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Model](#ssurgo-lineage-test-model) · [Profiles](#source-and-support-profile-matrix) · [Keys](#identity-and-join-lineage) · [Cases](#required-test-case-matrix) · [Fixtures](#no-network-and-fixture-posture) · [Public surfaces](#public-surface-and-answer-boundary) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs-and-decisions-needed) · [Migration](#migration-correction-and-rollback) · [Open](#open-verification-register) · [Done](#definition-of-done) · [Last reviewed](#last-reviewed)

---

## Purpose

`tests/domains/agriculture/ssurgo_lineage/` is the Agriculture test sublane for **bounded, traceable consumption of Soil-owned static survey and gridded derivative context**.

A complete test family should answer:

1. Which source family and product form supplied the Soil context: SSURGO package, SDA query result, gSSURGO raster, gNATSGO context, or KFM-derived interpretation?
2. Does the candidate resolve to an admitted source descriptor or accepted source-registry record?
3. Are source version, survey area, retrieval/run identity, effective/source vintage, and correction state explicit?
4. Are polygon and tabular sources from compatible releases or intentionally pinned snapshots?
5. Does every map-unit join preserve MUKEY verbatim rather than infer identity from geometry alone?
6. Are COKEY and component percentage preserved when component data affects a result?
7. Are CHKEY, horizon depth intervals, units, and aggregation method preserved when horizon data affects a result?
8. Does gSSURGO remain a gridded derivative tied back to source-survey precision and MUKEY lineage?
9. Are SSURGO, SDA, and gSSURGO kept distinct rather than silently merged into one source or cadence?
10. Does Agriculture cite Soil-owned objects through EvidenceRef or governed pointers rather than copy them into Agriculture canonical truth?
11. Is any Agriculture output separately identified as modeled, interpreted, or aggregate rather than relabeled as observed Soil truth?
12. Are aggregation, weighting, interpolation, resampling, classification, and suitability methods versioned and receipted?
13. Do evidence, policy, review, release, correction, supersession, withdrawal, and rollback references close for public-bound derivatives?
14. Do public API, UI, map, export, search, graph, report, and AI surfaces preserve source, vintage, scale, uncertainty, and role?
15. Does unsupported or ambiguous lineage return a finite safe outcome instead of fabricated certainty?
16. Does the default suite remain synthetic, deterministic, bounded, and no-network?
17. Does CI actually collect and execute the SSURGO-lineage tests?

Appropriate Agriculture uses include:

- soil-crop suitability context;
- aggregate crop-stress or drought interpretation that cites Soil support;
- county, reporting-district, watershed, or generalized-grid summaries with explicit methodology;
- comparison of Agriculture outputs with Soil map units or properties;
- public-safe explanation of why a released Agriculture derivative references a Soil source.

This lane does not define Soil semantics, certify field conditions, create agronomic advice, approve publication, or establish production readiness.

[Back to top](#top)

---

## Authority level

**Canonical test responsibility / non-authoritative Agriculture consumer lane.**

`tests/` owns enforceability proof. Soil owns SSURGO object meaning, source support, and lineage semantics. Agriculture owns only its derivative meaning and the tests that prove its consumers preserve the Soil boundary.

| Concern | Authority home | This lane's role |
|---|---|---|
| Executable Agriculture tests | `tests/` | Owns test modules and assertions. |
| Agriculture test organization | `tests/domains/agriculture/` | Owns this child test segment. |
| SSURGO, component, horizon, and Soil interpretation meaning | Soil contracts and domain roots | Tests bounded consumption; does not redefine meaning. |
| Source admission and role | Accepted source registry and policy roots | Tests references; cannot activate a source. |
| SSURGO/SDA/gSSURGO product documentation | `docs/sources/catalog/nrcs/` | Supplies review context; product pages are not descriptors. |
| Soil ingest behavior | `pipelines/domains/soil/ssurgo_ingest/` or accepted implementation | Tests integration when substantive; not implemented here. |
| Soil lineage validation | `tools/validators/domains/soil/lineage/` | Tests integration; does not move validator authority. |
| Agriculture-facing Soil join validation | `tools/validators/domains/agriculture/soil-join/` | Tests Agriculture edge behavior; does not define Soil truth. |
| Shared Agriculture × Soil join validation | `tools/validators/joins/agriculture-soil/` | Tests shared invariants; topology remains unresolved. |
| Agriculture semantic derivative | Agriculture contracts, including accepted `SoilCropSuitability` profile | Tests meaning when accepted; current object-level contract is unverified. |
| Machine shape | Accepted Soil, Agriculture, source, and join schema homes | Tests shape; does not author schemas. |
| Fixtures | `fixtures/domains/agriculture/ssurgo/` and accepted Soil fixture lanes | Consumes synthetic examples; does not store source truth. |
| Evidence, receipts, proofs, catalog, release | Their governed roots | Tests closure; cannot create authority. |
| Public clients | Governed APIs and released artifacts | Tests payload boundaries; cannot expose a route. |

### Anti-collapse rules

This lane must not collapse:

- source-document prose into a SourceDescriptor;
- source registration into source truth;
- connector output into an admitted record;
- admitted RAW material into processed truth;
- SSURGO vector survey into SDA query behavior;
- SSURGO static survey into gSSURGO raster behavior;
- gSSURGO cell size into survey precision;
- MUKEY into component or horizon identity;
- geometry overlap into canonical MUKEY identity;
- COKEY component values into map-unit values without weighting;
- CHKEY horizon values into profile or map-unit values without depth-aware derivation;
- source vintage into retrieval, release, or correction time;
- Soil interpretation into Agriculture crop truth;
- Agriculture suitability into raw Soil property;
- schema validity into lineage closure;
- lineage closure into evidence closure;
- evidence closure into policy allow;
- policy allow into release approval;
- release approval into unrestricted public precision;
- a green TODO workflow into executable proof;
- README guidance into implementation evidence.

[Back to top](#top)

---

## Status

### Current evidence and maturity

| Surface | Inspected status | Safe conclusion |
|---|---|---|
| This child lane | **CONFIRMED README-only in bounded search** | Test contract exists; no executable test surfaced. |
| Agriculture SSURGO fixture lane | **CONFIRMED README / payloads unconfirmed** | Fixture guidance exists; no direct payload inventory is established. |
| SSURGO product page | **CONFIRMED draft documentation** | Defines static vector survey context and MUKEY hierarchy; not source registry authority. |
| gSSURGO product page | **CONFIRMED draft documentation** | Defines gridded derivative and precision cautions; role conflicts with Agriculture source register. |
| Agriculture source register | **CONFIRMED draft documentation** | Lists SSURGO/SDA as observed plus aggregate summaries; lists gSSURGO as aggregate. |
| Soil SSURGO ingest lane | **CONFIRMED README / behavior unverified** | Documents required lineage and anti-collapse rules. |
| Soil lineage validator | **CONFIRMED README / no executable confirmed** | Proposed reusable Soil lineage checks exist as documentation. |
| Agriculture Soil-join validator | **CONFIRMED README / no executable confirmed** | Proposed MUKEY/EvidenceRef and derivative checks exist as documentation. |
| Shared join validator | **CONFIRMED README / no executable confirmed** | Overlapping shared routing lane exists. |
| `SoilCropSuitability` contract | **NEEDS VERIFICATION** | Named in Agriculture object-family index; concrete accepted object-level contract not confirmed. |
| Agriculture/Soil workflows | **CONFIRMED TODO-only** | Green status would not prove SSURGO tests or validation. |

### Truth labels for this README

- **CONFIRMED:** paths, files, blobs, documented boundaries, absence of surfaced child test modules, fixture README without confirmed payloads, and TODO workflow definitions.
- **PROPOSED:** test case names, finite outcomes, reason codes, fixture shapes, CI command, derivative profile, and definition of done.
- **CONFLICTED:** gSSURGO source role; source-role versus support-type terminology; registry topology; validator topology.
- **UNKNOWN:** current source records, executable behaviors, current data versions, CI enforcement, release consumers, and production use.
- **NEEDS VERIFICATION:** accepted profiles, methods, thresholds, owners, rights, source terms, correction propagation, and rollback automation.

[Back to top](#top)

---

## What belongs here

- This README.
- Agriculture SSURGO-lineage test modules.
- Tests that resolve SSURGO/SDA/gSSURGO source pointers and preserve product form.
- MUKEY, COKEY, CHKEY, component-weight, horizon-depth, and source-vintage tests.
- Tests for spatial/tabular package compatibility and SDA query pinning.
- Tests that detect geometry-only joins, stale lineage, mixed versions, and broken transform chains.
- Tests that Agriculture derivatives cite Soil-owned EvidenceRefs and remain separately identified.
- Tests for aggregation, resampling, weighting, interpretation, correction cascade, and rollback readiness.
- Tests of public-safe payload language, precision, caveats, and finite outcomes.
- Minimal test-local synthetic inline values when a shared fixture file would add no value.

[Back to top](#top)

---

## What does not belong here

| Material | Correct home |
|---|---|
| SSURGO, gSSURGO, SDA, or NRCS source descriptors | Accepted source-registry roots. |
| RAW downloads or SDA responses | Governed RAW or connector test lanes. |
| Soil contracts and schemas | Soil contract/schema roots. |
| Agriculture contracts and schemas | Agriculture contract/schema roots. |
| Validator implementation | Accepted Soil, Agriculture, or shared validator lanes. |
| Connector or pipeline implementation | `connectors/` and `pipelines/`. |
| Shared fixture collections | `fixtures/` or accepted test-fixture roots. |
| Source rights, sensitivity, or policy rules | Policy and registry roots. |
| Lifecycle data, catalog records, receipts, or proofs | Governed `data/` roots. |
| ReleaseManifest, CorrectionNotice, RollbackCard, or release decisions | `release/`. |
| Public map, API, report, export, search, graph, or AI implementation | Governed application/runtime roots. |
| Live source calls in the default suite | Connector/live integration lanes only. |
| Secrets, credentials, private parcel details, operator identities, or production logs | Prohibited from this lane. |

[Back to top](#top)

---

## Inputs

Tests should consume only bounded, version-pinned inputs.

| Input | Minimum posture |
|---|---|
| Source profile | Stable fixture identifier; source family; product form; role/support posture; source vintage; mock marker. |
| Map-unit record | MUKEY, survey-area identity, geometry reference, source version, evidence pointer. |
| Component record | COKEY, parent MUKEY, component percentage, source version. |
| Horizon record | CHKEY, parent COKEY, top/bottom depth and units, source version. |
| SDA result | Query digest/text reference, endpoint/profile version, retrieval time, source snapshot or reproducibility pin. |
| gSSURGO cell | Grid identity, CRS, cell size, MUKEY value, source-survey vintage, transform/resampling lineage. |
| Agriculture derivative candidate | Stable id/spec hash, Soil EvidenceRefs, transform/method profile, source-role/support declarations, policy/release refs where material. |
| Correction case | Superseded/revoked Soil pointer and downstream Agriculture dependency graph. |

Default inputs must be synthetic, deterministic, public-safe, no-network, and too small to be mistaken for production data.

[Back to top](#top)

---

## Outputs

Test outputs are assertions and bounded diagnostics, not truth artifacts.

A test result should expose:

- case identifier;
- finite outcome;
- stable reason code;
- failing invariant;
- object/source family and safe identifier;
- expected and observed lineage state without leaking sensitive payloads;
- unresolved references;
- whether public-bound behavior is blocked;
- deterministic rerun information.

Tests must not emit source descriptors, EvidenceBundles, release records, production receipts, public artifacts, or authoritative catalog objects unless a separate fixture contract explicitly defines synthetic test copies.

[Back to top](#top)

---

## SSURGO lineage test model

### Required lineage chain

```text
SourceDescriptor / source-admission record
  -> connector candidate or pinned source fixture
  -> RAW fixture identity
  -> WORK / QUARANTINE decision
  -> processed Soil map-unit/component/horizon record
  -> Soil catalog and EvidenceRef
  -> Agriculture join candidate
  -> Agriculture derivative method and receipt refs
  -> policy/review/release decision
  -> governed public projection
```

Each arrow requires explicit identity and version continuity. No stage may be inferred solely from path naming.

### Minimum lineage dimensions

| Dimension | Required preservation |
|---|---|
| Source identity | Stable source record or accepted fixture profile. |
| Product form | SSURGO vector/snapshot, SDA query, gSSURGO grid, or derived product. |
| Source role | Preserve accepted role vocabulary; do not silently upgrade on promotion. |
| Support type | Static survey, API query, gridded derivative, interpretation, Agriculture derivative. |
| Source vintage | Survey/release version and effective/source time. |
| Retrieval/run | Retrieval identity, run reference, transform/code/profile version. |
| Spatial support | Survey area, polygon/map unit, grid cell, aggregate region, denied precision. |
| Tabular support | MUKEY/COKEY/CHKEY hierarchy and table/version compatibility. |
| Derivation | Weighting, depth aggregation, classification, resampling, interpretation, uncertainty. |
| Evidence | EvidenceRef resolution and supporting bundle/proof pointers. |
| Governance | Rights, sensitivity, policy, review, release, correction, rollback. |

### Cite-or-abstain rule

When a consequential derivative cannot resolve its Soil evidence, source version, join lineage, or method profile, the safe outcome is `ABSTAIN`, `HOLD`, `DENY`, or `ERROR`—not a guessed suitability value or geometry-snapped identity.

[Back to top](#top)

---

## Source and support profile matrix

| Profile | Expected posture | Required lineage | Forbidden collapse |
|---|---|---|---|
| SSURGO survey package | Soil-owned static survey source/support. | Survey area, package/version, geometry, MUKEY and tabular version. | Real-time condition, crop truth, gSSURGO cell, SDA live query. |
| SDA query | Query/API projection over admitted soil data. | Query profile/digest, retrieval, source snapshot/version, result lineage. | Unpinned live truth or equivalent to a full SSURGO snapshot. |
| gSSURGO raster | Gridded derivative linked to SSURGO by MUKEY. | Grid/version, CRS, cell size, MUKEY, source-survey vintage, resampling history. | Sub-map-unit observation, station/soil-moisture data, raw suitability truth. |
| Component rollup | Derived map-unit property. | MUKEY, all relevant COKEYs, component percentages, missing-data rules, method version. | Dominant component copied as whole map-unit truth without declaration. |
| Horizon aggregation | Derived component/map-unit property. | CHKEY, COKEY, depth intervals, units, overlap method, weighting/normalization. | Horizon value promoted without depth-aware derivation. |
| Soil interpretation | Soil-owned interpretation or rating. | Soil contract/profile, source lineage, method/version, uncertainty and caveat. | Crop/yield truth or field management advice. |
| Agriculture `SoilCropSuitability` candidate | Agriculture-owned derivative consuming Soil evidence. | Soil EvidenceRefs, crop/use profile, method/version, aggregation/redaction, policy/release refs. | Raw Soil truth, verified field fact, operator-specific recommendation. |

### Source-role conflict register

Repository evidence uses inconsistent role language for gSSURGO:

- the gSSURGO product page proposes `observed` for gridded survey mapping;
- the Agriculture source register assigns `aggregate` and says never relabel it observed;
- the Agriculture fixture README describes gSSURGO as a gridded derivative;
- Soil documentation also uses support/lane labels such as `authoritative_static_soil` and `gridded_derivative_soil`.

Tests must not hard-code one of these as canonical until an accepted SourceDescriptor/profile, schema, policy record, or ADR resolves the vocabulary. Until then, test fixtures should carry separate fields for **source family**, **source role**, **support type**, and **product form**, and treat incompatible combinations as `HOLD` or `NEEDS_REVIEW` rather than inventing a resolution.

[Back to top](#top)

---

## Identity and join lineage

### MUKEY

MUKEY is the load-bearing map-unit join key.

Required tests:

- exact preservation from Soil-owned source support;
- no whitespace/numeric coercion that changes identity;
- resolution against the pinned source/version;
- no fabricated MUKEY from geometry overlap alone;
- no cross-vintage join without an explicit migration/crosswalk;
- duplicate or ambiguous MUKEY handling is deterministic;
- gSSURGO cell MUKEY resolves to compatible tabular support.

### COKEY and component weighting

When component data affects an Agriculture derivative:

- every COKEY resolves to the expected parent MUKEY;
- component percentages are present or missingness is explicit;
- percentages and weighting rules are versioned;
- totals outside accepted tolerance fail or route to review;
- dominant-component shortcuts are labeled and not silently treated as weighted truth;
- excluded components and null handling are recorded;
- method changes invalidate dependent outputs.

### CHKEY and horizon depth

When horizon data affects a result:

- each CHKEY resolves to its COKEY;
- top and bottom depth plus units are present;
- intervals are valid and non-inverted;
- overlaps, gaps, and truncation are handled explicitly;
- depth-weighted aggregation is reproducible;
- unit conversions are deterministic and versioned;
- horizon-to-component and component-to-map-unit transforms remain separate;
- missing depth lineage fails closed for depth-dependent claims.

### Spatial and tabular coupling

Tests must detect:

- polygon package and tabular database from different source vintages;
- survey area mismatch;
- stale or missing attribute tables;
- geometry updated without dependent joins being rebuilt;
- table updates without downstream Agriculture invalidation;
- gSSURGO grid and tabular MUKEY support from incompatible releases;
- CRS or resampling changes without transform receipts;
- topology or geometry repairs that change identity without review.

[Back to top](#top)

---

## Agriculture derivative boundary

Agriculture may create an Agriculture-owned derivative only after the Soil inputs remain governed and inspectable.

A derivative such as `SoilCropSuitability` should carry, at minimum:

```yaml
id: mock-ag-soil-suitability-001
_mock: true
object_family: SoilCropSuitability
owner_domain: agriculture
soil_evidence_refs:
  - kfm://evidence/mock-soil-map-unit-001
soil_join:
  mukey: "MOCK-MUKEY-001"
  source_profile_ref: kfm://source/mock-nrcs-ssurgo
  source_vintage: "mock-2026-a"
method:
  profile_id: mock-suitability-profile-v1
  method_version: "1.0.0"
  code_or_spec_hash: sha256:mock
source_role: modeled
support_type: agriculture_derivative
spatial_scope: aggregate_test_area
policy_state: held_for_fixture_test
release_state: not_released
```

This is an illustrative test contract, not an accepted production schema.

A derivative must fail or abstain when:

- Soil EvidenceRefs do not resolve;
- MUKEY is missing, malformed, fabricated, or unresolved;
- Soil source vintage is missing or incompatible;
- method identity or version is absent;
- component/horizon inputs are used without their lineage;
- public precision exceeds source and method support;
- a field/operator-specific output lacks aggregation/redaction/review support;
- Soil-side correction, withdrawal, or source supersession is not propagated;
- release and rollback support is missing for a public-bound surface.

[Back to top](#top)

---

## Required test-case matrix

### Positive controls

| Case | Expected result |
|---|---|
| P01 — SSURGO map unit resolves through pinned source profile | `PASS`. |
| P02 — MUKEY joins compatible polygon and tabular versions | `PASS`. |
| P03 — Component-weighted property preserves COKEYs and percentages | `PASS`. |
| P04 — Horizon aggregation preserves CHKEY/depth/unit method | `PASS`. |
| P05 — SDA result carries query and source-snapshot pins | `PASS`. |
| P06 — gSSURGO cell resolves MUKEY and survey vintage | `PASS` or `HOLD` if role profile unresolved. |
| P07 — Agriculture derivative cites Soil EvidenceRefs and separate method identity | `PASS`. |
| P08 — Aggregate public output stays within supported precision | `PASS`. |
| P09 — Soil correction invalidates and rebuilds dependent Agriculture candidate | `PASS`. |
| P10 — Re-running the same fixtures produces identical outcomes | `PASS`. |

### Source and product failures

| Case | Expected result |
|---|---|
| N01 — source pointer missing | `FAIL_CLOSED`. |
| N02 — source record exists but is inactive, withdrawn, or rights-unresolved | `DENY` or `HOLD`. |
| N03 — connector candidate treated as admitted or published truth | `FAIL_CLOSED`. |
| N04 — SSURGO snapshot treated as SDA query result | `FAIL_CLOSED`. |
| N05 — SDA result lacks query/version/retrieval pin | `ABSTAIN` or `FAIL_CLOSED`. |
| N06 — gSSURGO treated as vector SSURGO or sub-map-unit observation | `FAIL_CLOSED`. |
| N07 — incompatible gSSURGO role/profile is silently accepted | `HOLD`. |
| N08 — product form or support type is missing | `FAIL_CLOSED`. |

### Identity and hierarchy failures

| Case | Expected result |
|---|---|
| N09 — MUKEY missing | `FAIL_CLOSED`. |
| N10 — MUKEY malformed or changed by coercion | `FAIL_CLOSED`. |
| N11 — MUKEY inferred only from geometry overlap | `DENY`. |
| N12 — MUKEY resolves against wrong source vintage | `FAIL_CLOSED`. |
| N13 — COKEY parent MUKEY mismatch | `FAIL_CLOSED`. |
| N14 — component percentages missing or invalid for weighted rollup | `FAIL_CLOSED` or `HOLD`. |
| N15 — CHKEY parent COKEY mismatch | `FAIL_CLOSED`. |
| N16 — horizon depth missing, inverted, or unitless | `FAIL_CLOSED`. |
| N17 — horizon value promoted directly to map-unit truth | `FAIL_CLOSED`. |
| N18 — hierarchy contains a cycle or duplicate canonical identity | `ERROR` or `FAIL_CLOSED`. |

### Vintage, transform, and method failures

| Case | Expected result |
|---|---|
| N19 — polygon and tabular versions differ without crosswalk | `FAIL_CLOSED`. |
| N20 — source vintage absent | `ABSTAIN` or `FAIL_CLOSED`. |
| N21 — transform/method version absent | `FAIL_CLOSED`. |
| N22 — resampling changes grid support without receipt | `FAIL_CLOSED`. |
| N23 — cell size is reported as source precision | `FAIL_CLOSED`. |
| N24 — weighting or depth method changes without dependent invalidation | `FAIL_CLOSED`. |
| N25 — missing-data behavior is implicit | `HOLD`. |
| N26 — stale cached derivative remains current after Soil update | `FAIL_CLOSED`. |

### Ownership, evidence, and public failures

| Case | Expected result |
|---|---|
| N27 — Soil object copied as Agriculture canonical truth | `DENY`. |
| N28 — Agriculture suitability presented as raw Soil property | `DENY`. |
| N29 — Soil evidence cannot resolve | `ABSTAIN` or `FAIL_CLOSED`. |
| N30 — lineage pointer resolves but supporting evidence bundle does not | `ABSTAIN`. |
| N31 — field/operator-specific output lacks redaction or aggregation support | `DENY`. |
| N32 — map/API language claims verified field condition from SSURGO | `DENY`. |
| N33 — public output omits source vintage or survey caveat | `FAIL_CLOSED` or `RESTRICT`. |
| N34 — release-facing output lacks PolicyDecision/review/release refs | `DENY`. |
| N35 — correction/rollback targets do not cover downstream derivative | `HOLD`. |
| N36 — test requires live NRCS/SDA access by default | `TEST_FAILURE`. |
| N37 — generated explanation is accepted as evidence | `TEST_FAILURE`. |
| N38 — green TODO workflow is counted as SSURGO test coverage | `TEST_FAILURE`. |

### Boundary and robustness failures

| Case | Expected result |
|---|---|
| N39 — unknown reason code or outcome | `ERROR`. |
| N40 — error message leaks fixture payload or sensitive join data | `TEST_FAILURE`. |
| N41 — partial run leaves an apparent PASS | `ERROR` and no success artifact. |
| N42 — test ordering changes results | `TEST_FAILURE`. |
| N43 — time zone or locale changes identity/digest | `TEST_FAILURE`. |
| N44 — duplicate execution creates divergent outputs | `TEST_FAILURE`. |
| N45 — unrelated Soil correction invalidates all Agriculture products | `TEST_FAILURE` for over-broad invalidation. |
| N46 — affected derivative remains valid after upstream revocation | `TEST_FAILURE` for under-invalidation. |

[Back to top](#top)

---

## No-network and fixture posture

### Current fixture evidence

`fixtures/domains/agriculture/ssurgo/README.md` exists, but no direct `valid/`, `invalid/`, input, expected, or snapshot payload inventory is confirmed in bounded evidence.

### Required fixture families

```text
fixtures/domains/agriculture/ssurgo/
├── README.md
├── valid/
│   ├── ssurgo_mapunit_join/
│   ├── component_weighted_rollup/
│   ├── horizon_depth_aggregation/
│   ├── sda_pinned_query/
│   ├── gssurgo_mukey_lineage/
│   └── agriculture_suitability_derivative/
├── invalid/
│   ├── missing_source_pointer/
│   ├── mixed_source_vintage/
│   ├── geometry_only_mukey/
│   ├── broken_cokey_parent/
│   ├── broken_chkey_parent/
│   ├── missing_component_weights/
│   ├── missing_horizon_depth/
│   ├── unreceipted_resampling/
│   ├── role_support_conflict/
│   ├── soil_ownership_collapse/
│   ├── public_precision_overclaim/
│   └── upstream_soil_revoked/
└── expected/
    ├── outcomes/
    └── reason_codes/
```

This layout is **PROPOSED**. Do not create empty directories without executable consumers.

### Fixture rules

Every fixture must:

- include `_mock: true` or an equivalent unmistakable marker;
- use non-routable identifiers and synthetic geometry;
- remain compact and reviewable;
- contain no live credentials, full source dumps, private parcel details, or operator identities;
- pin source profile, version, survey area, and method identity when relevant;
- declare expected outcome and reason code;
- avoid network, DNS, sockets, external services, and live model runtimes;
- produce deterministic results across supported platforms;
- be replaceable without modifying source or release authority.

[Back to top](#top)

---

## Finite outcomes and reason codes

### Proposed outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Configured test expectations passed. |
| `FAIL_CLOSED` | Required lineage or invariant failed. |
| `DENY` | Requested use is not permitted as shaped. |
| `RESTRICT` | Only a narrower/generalized output may proceed. |
| `HOLD` | Review or an unresolved profile/authority decision is required. |
| `ABSTAIN` | Available evidence cannot safely support a result. |
| `ERROR` | Test or validator could not complete safely. |

### Proposed reason codes

- `SOURCE_POINTER_MISSING`
- `SOURCE_STATE_INVALID`
- `PRODUCT_FORM_MISSING`
- `SOURCE_ROLE_CONFLICT`
- `SUPPORT_TYPE_CONFLICT`
- `SOURCE_VINTAGE_MISSING`
- `SOURCE_VINTAGE_MISMATCH`
- `SDA_QUERY_UNPINNED`
- `MUKEY_MISSING`
- `MUKEY_MALFORMED`
- `MUKEY_UNRESOLVED`
- `GEOMETRY_ONLY_JOIN_DENIED`
- `COKEY_PARENT_MISMATCH`
- `COMPONENT_WEIGHT_INVALID`
- `CHKEY_PARENT_MISMATCH`
- `HORIZON_DEPTH_INVALID`
- `TABULAR_SPATIAL_VERSION_MISMATCH`
- `TRANSFORM_PROFILE_MISSING`
- `RESAMPLING_RECEIPT_MISSING`
- `PRECISION_OVERCLAIM`
- `SOIL_OWNERSHIP_COLLAPSE`
- `DERIVATIVE_ROLE_COLLAPSE`
- `EVIDENCE_REF_MISSING`
- `EVIDENCE_UNRESOLVED`
- `POLICY_REFERENCE_MISSING`
- `RELEASE_REFERENCE_MISSING`
- `UPSTREAM_SOIL_REVOKED`
- `CORRECTION_CASCADE_INCOMPLETE`
- `ROLLBACK_TARGET_MISSING`
- `PUBLIC_BOUNDARY_VIOLATION`
- `NETWORK_ACCESS_ATTEMPTED`
- `NONDETERMINISTIC_RESULT`

The accepted vocabulary must be defined by a contract/schema/ADR before implementation treats these strings as canonical.

[Back to top](#top)

---

## Public-surface and answer boundary

Public-facing tests must verify both **what is shown** and **what is withheld**.

### Required public language

Acceptable language distinguishes:

- source: USDA NRCS SSURGO, SDA, or gSSURGO profile;
- support: static survey polygon, pinned query, grid derivative, or Agriculture interpretation;
- vintage: source/survey release and correction status;
- precision: survey/map-unit or aggregate support, not arbitrary point truth;
- method: component weighting, horizon aggregation, resampling, classification, or suitability profile;
- uncertainty/limitations: map-unit heterogeneity, missing components, source age, and interpretation limits;
- ownership: Soil source evidence, Agriculture derivative conclusion;
- governance: evidence, policy, review, and release state.

### Forbidden public implications

Tests must reject language or payloads implying:

- exact soil condition at a point solely from SSURGO/gSSURGO;
- current soil moisture or field condition from static survey data;
- verified crop suitability at an individual field without separately governed support;
- gSSURGO cell resolution equals survey precision;
- dominant component equals the entire map unit;
- a horizon property is a map-unit property without derivation;
- Agriculture owns the underlying Soil object;
- a connector, source page, catalog entry, schema pass, or validator pass equals release approval;
- AI-generated prose is evidence.

### Evidence Drawer / trace view

A public-safe trace should expose, when released and policy-allowed:

- source/product label;
- source vintage and survey area;
- relevant MUKEY and generalized support, subject to policy;
- transformation/method profile;
- evidence and citation references;
- limitations and stale/correction state;
- Agriculture derivative identity;
- release and rollback status.

It must not expose internal stores, private joins, raw payloads, unrestricted exact locations, or secrets.

[Back to top](#top)

---

## Correction, invalidation, and rollback tests

### Upstream Soil change

When Soil source support is corrected, superseded, withdrawn, or invalidated, tests should prove that:

1. affected Agriculture dependencies are discoverable;
2. only affected derivatives are held or invalidated;
3. public caches, indexes, exports, map layers, reports, and AI context become stale or unavailable as required;
4. the old audit trail remains immutable;
5. rebuild uses the new source/version and method pins;
6. a corrected derivative receives new identity/digests where required;
7. release review is re-entered rather than silently restoring publication;
8. rollback can restore a verified prior safe derivative or withdraw without replacement.

### Over-invalidation and under-invalidation

Tests must detect both:

- **under-invalidation:** an affected derivative remains current after upstream correction;
- **over-invalidation:** unrelated Agriculture products are withdrawn because dependency resolution is too broad.

### Idempotence and interruption

A correction or rollback test should prove:

- repeating the same invalidation does not compound side effects;
- interruption cannot leave a stale derivative marked current;
- retry preserves deterministic targets;
- audit and lineage records remain inspectable;
- failed rebuild does not republish the prior unsafe state automatically.

[Back to top](#top)

---

## Workflow and CI admission

The repository's `domain-agriculture` and `domain-soil` workflows currently execute TODO echo commands. Their success does not prove this lane.

Before CI may be described as SSURGO-lineage coverage, it must:

- collect at least one substantive test module from this lane or an accepted shared test path;
- run without network access;
- consume reviewed synthetic fixtures;
- exercise positive and negative cases;
- fail on zero collected tests;
- fail on unknown outcomes or reason codes;
- fail when a required fixture family is missing;
- distinguish test failures from tool errors;
- publish bounded diagnostics without sensitive payloads;
- include the accepted command in the workflow and parent test documentation;
- be required by the relevant promotion/release gate before claims of enforcement.

### Proposed command

```bash
pytest -q tests/domains/agriculture/ssurgo_lineage
```

This command is **PROPOSED**. It becomes authoritative only after executable tests exist, collect successfully, and CI invokes it fail-closed.

[Back to top](#top)

---

## Validation

### Documentation validation performed for v0.2

- one H1 outside fenced blocks;
- balanced Markdown fences;
- required Directory Rules section sequence present;
- no trailing whitespace or tabs;
- no high-signal credential patterns;
- evidence blobs and current base pinned;
- one-file change budget preserved.

### Future executable validation

```bash
find tests/domains/agriculture/ssurgo_lineage -maxdepth 6 -type f | sort
find fixtures/domains/agriculture/ssurgo -maxdepth 6 -type f 2>/dev/null | sort
find tools/validators/domains/soil/lineage \
     tools/validators/domains/agriculture/soil-join \
     tools/validators/joins/agriculture-soil \
     -maxdepth 6 -type f 2>/dev/null | sort
pytest -q tests/domains/agriculture/ssurgo_lineage
```

Do not add `|| true` to the accepted CI command. Zero-test collection, missing fixtures, unresolved profiles, or tool errors must remain visible.

### Minimum acceptance matrix

| Criterion | Required |
|---|---:|
| Soil ownership and Agriculture derivative boundary explicit | Yes |
| SSURGO, SDA, and gSSURGO kept distinct | Yes |
| gSSURGO role conflict visible until governed resolution | Yes |
| MUKEY/COKEY/CHKEY hierarchy preserved | Yes |
| Spatial/tabular/source-vintage compatibility tested | Yes |
| Geometry-only identity denied | Yes |
| Weighting/depth/resampling methods pinned | Yes |
| Soil EvidenceRefs resolve before derivative acceptance | Yes |
| Public precision and language bounded | Yes |
| Correction cascade and rollback tested | Yes |
| Default suite no-network and deterministic | Yes |
| CI collects substantive tests and fails on zero tests | Yes |

[Back to top](#top)

---

## Review burden

Changes in this lane require review proportionate to consequence.

### Required reviewers when implemented

- Agriculture test/domain steward;
- Soil domain steward;
- source/registry steward;
- contract and schema steward;
- fixture and validation steward;
- evidence/catalog steward;
- policy, rights, and sensitivity reviewer;
- release/correction/rollback steward;
- public API/UI steward when payload assertions change.

### Review checklist

- [ ] The test does not define Soil semantics or source authority.
- [ ] Product form and support type remain explicit.
- [ ] Accepted source role comes from a governed profile, not this README.
- [ ] MUKEY identity is not fabricated from geometry.
- [ ] COKEY/CHKEY continuity is preserved where material.
- [ ] Source vintage and spatial/tabular versions are compatible.
- [ ] Weighting, depth, resampling, and suitability methods are deterministic and versioned.
- [ ] Fixtures are synthetic, public-safe, and no-network.
- [ ] Errors do not leak source payloads or sensitive details.
- [ ] Evidence, policy, review, and release remain separate gates.
- [ ] Soil corrections propagate to dependent Agriculture products.
- [ ] Rollback and withdrawal paths are testable and auditable.
- [ ] Public wording does not imply unsupported precision or ownership.
- [ ] CI actually invokes substantive tests.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| `tests/domains/agriculture/` | Parent Agriculture test lane. |
| `fixtures/domains/agriculture/ssurgo/` | Synthetic Agriculture SSURGO fixture lane; payload inventory unconfirmed. |
| `contracts/domains/soil/` | Soil semantic authority for map units, components, horizons, and properties. |
| `contracts/domains/agriculture/` | Agriculture derivative meaning; object-level suitability contract unverified. |
| `docs/sources/catalog/nrcs/ssurgo.md` | SSURGO product orientation; not source registry authority. |
| `docs/sources/catalog/nrcs/gssurgo.md` | gSSURGO product orientation and precision cautions. |
| `docs/domains/agriculture/SOURCES.md` | Agriculture source-role register; contains gSSURGO role conflict. |
| `data/registry/sources/soil/` | Candidate Soil source-registry authority; topology unresolved. |
| `pipelines/domains/soil/ssurgo_ingest/` | Proposed Soil SSURGO normalization lane. |
| `tools/validators/domains/soil/lineage/` | Proposed Soil lineage validator lane. |
| `tools/validators/domains/agriculture/soil-join/` | Proposed Agriculture-facing join validator lane. |
| `tools/validators/joins/agriculture-soil/` | Proposed shared join routing lane. |
| `data/catalog/domain/soil/` | Soil catalog projection, not Agriculture truth. |
| `data/proofs/`, `data/receipts/` | Proof and process-memory roots. |
| `release/` | Promotion, correction, withdrawal, and rollback authority. |

[Back to top](#top)

---

## ADRs and decisions needed

| Decision | Status | Why it matters |
|---|---|---|
| Canonical gSSURGO source-role and support-type profile | **NEEDS VERIFICATION** | Current docs conflict between `observed`, `aggregate`, and derivative/support labels. |
| Canonical Soil source-registry topology | **NEEDS VERIFICATION** | Multiple domain-first and subtype-first paths are documented. |
| Agriculture × Soil validator topology | **NEEDS VERIFICATION** | Soil lineage, Agriculture soil-join, shared join, and suitability lanes overlap. |
| Accepted `SoilCropSuitability` semantic contract and schema | **NEEDS VERIFICATION** | Object family is named, but concrete accepted contract/profile is unconfirmed. |
| SSURGO/SDA/gSSURGO profile identity and versioning | **NEEDS VERIFICATION** | Tests need stable product and source-vintage pins. |
| MUKEY/COKEY/CHKEY validation vocabulary | **NEEDS VERIFICATION** | Exact type, formatting, null, and crosswalk rules must be machine-checkable. |
| Component/horizon aggregation method contracts | **NEEDS VERIFICATION** | Weighting and depth transforms control derivative meaning. |
| Source-vintage compatibility and correction policy | **NEEDS VERIFICATION** | Mixed survey/table/grid versions must fail predictably. |
| Public precision and generalization policy | **NEEDS VERIFICATION** | Grid size, survey precision, field privacy, and aggregate exposure differ. |
| Reason-code and outcome contract | **PROPOSED** | Stable diagnostics require an accepted finite vocabulary. |
| CI and promotion-gate ownership | **NEEDS VERIFICATION** | Current workflows are placeholders. |

This README does not resolve these decisions by assertion.

[Back to top](#top)

---

## Smallest sound implementation sequence

1. Accept the canonical SSURGO/SDA/gSSURGO source and support profiles.
2. Resolve source-registry topology or provide one non-divergent compatibility path.
3. Accept the Soil map-unit/component/horizon contracts and schemas needed by tests.
4. Accept the Agriculture derivative contract/profile for `SoilCropSuitability` or successor.
5. Choose one validator topology and document delegation among Soil, Agriculture, and shared join lanes.
6. Add minimal valid and invalid synthetic fixtures.
7. Implement MUKEY/COKEY/CHKEY and source-vintage tests first.
8. Add weighting, depth, SDA pinning, gSSURGO precision, and resampling tests.
9. Add evidence, policy, public-language, correction-cascade, and rollback cases.
10. Wire fail-closed no-network CI that fails on zero collected tests.
11. Add release-gate adoption only after review and stable outcomes.
12. Update parent READMEs, runbooks, and any contract/schema indexes affected by the implemented behavior.

Each step should be independently reviewable and reversible.

[Back to top](#top)

---

## Migration, correction, and rollback

### Documentation rollback

Revert the commit that introduced v0.2 or restore prior blob:

```text
fb36559ca559de466329aee190fdeb3000365b2a
```

### Future test migration

If executable tests move to a shared Agriculture × Soil test lane:

1. adopt an ADR or migration note;
2. update this README and all validator/test indexes;
3. preserve a compatibility pointer during migration;
4. prove CI collects the new location before deleting the old one;
5. avoid duplicate execution and conflicting results;
6. retain rollback to the prior path until release-gate adoption is verified.

### Correcting this README

When evidence changes:

- update the evidence snapshot and truth labels;
- distinguish newly confirmed behavior from proposals;
- record resolved conflicts and the governing decision;
- update fixture/test/CI inventories from current repository evidence;
- do not rewrite prior implementation history or imply earlier enforcement that did not exist.

[Back to top](#top)

---

## Open verification register

- [ ] Confirm executable inventory under this child test lane.
- [ ] Confirm direct fixture payload inventory under `fixtures/domains/agriculture/ssurgo/`.
- [ ] Confirm accepted SSURGO, SDA, and gSSURGO SourceDescriptors.
- [ ] Resolve gSSURGO source-role/support-type conflict.
- [ ] Confirm canonical Soil source-registry topology.
- [ ] Confirm Soil map-unit/component/horizon schema and contract closure.
- [ ] Confirm accepted `SoilCropSuitability` contract/schema.
- [ ] Confirm MUKEY/COKEY/CHKEY machine rules and crosswalk behavior.
- [ ] Confirm component-weight and horizon-depth method contracts.
- [ ] Confirm source-vintage compatibility rules and stale thresholds.
- [ ] Confirm validator topology and executable names.
- [ ] Confirm policy bundles for field/operator/public precision.
- [ ] Confirm EvidenceRef resolver and correction cascade behavior.
- [ ] Confirm catalog, release, correction, withdrawal, and rollback integration.
- [ ] Confirm public API/UI/map/export/search/graph/AI payload contracts.
- [ ] Confirm CI command, zero-test guard, branch protection, and promotion-gate adoption.
- [ ] Confirm owners and CODEOWNERS.
- [ ] Confirm current publisher rights, terms, and attribution requirements before live use.

[Back to top](#top)

---

## Definition of done

This lane is not implementation-complete until all of the following are verified:

- substantive executable tests exist and collect;
- accepted synthetic valid and invalid fixtures exist;
- canonical SSURGO/SDA/gSSURGO profiles are resolved;
- gSSURGO role/support conflict is resolved by governed authority;
- Soil and Agriculture contract/schema dependencies are accepted;
- MUKEY/COKEY/CHKEY and source-vintage invariants are machine-tested;
- weighting, depth, resampling, and derivative methods are reproducible;
- Soil-owned evidence remains cited rather than copied into Agriculture authority;
- public precision, language, and sensitivity tests fail closed;
- evidence, policy, review, release, correction, and rollback cases are covered;
- correction cascade proves no under- or over-invalidation;
- tests are deterministic and no-network;
- CI fails on zero tests and invokes this lane or an accepted successor;
- workflow success reflects substantive commands rather than TODO echoes;
- required reviewers and owners are recorded;
- documentation and indexes match implemented behavior;
- rollback of both test placement and behavior is mechanical.

Until then, status remains **draft / README-only / NEEDS VERIFICATION**.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-16 |
| Evidence base | `main@1852516d033a6180507c7ad0b4390689a401c988` |
| Review status | Draft v0.2 repository-grounded README; implementation unverified. |
| Last change scope | Documentation only; exactly one README intended. |
| Next review trigger | SSURGO/gSSURGO profile decision, fixture or test addition, validator implementation, registry migration, contract/schema acceptance, source-role ADR, workflow change, policy/release integration, correction event, or rollback implementation. |

[Back to top](#top)
