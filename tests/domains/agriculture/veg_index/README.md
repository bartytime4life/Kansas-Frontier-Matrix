<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-agriculture-veg-index-readme
title: tests/domains/agriculture/veg_index/ — Agriculture Vegetation-Index Test Boundary
type: readme; directory-readme; domain-test-sublane; vegetation-index-enforceability-boundary
version: v0.2
status: draft; repository-grounded; README-only; no-executable-test-established; HLS-VI-fixture-README-only; connector-README-only; CI-TODO-only; non-authoritative
owners: OWNER_TBD — Agriculture test steward · Agriculture domain steward · Remote-sensing steward · Source steward · Fixture steward · Validation steward · Contract/schema steward · Policy steward · Rights/sensitivity reviewer · Evidence steward · Release steward · CI steward · Docs steward
created: 2026-07-05
updated: 2026-07-16
supersedes: v0.1 vegetation-index context test-lane README
policy_label: public-review; tests; agriculture; vegetation-index; modeled-context; source-role-preserving; QA-aware; spatial-support-aware; temporal-support-aware; aggregate-public-default; field-level-deny-default; no-network-default; evidence-aware; policy-aware; release-subordinate; correction-aware; rollback-aware; no-publication-authority
current_path: tests/domains/agriculture/veg_index/README.md
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; canonical tests responsibility root;
  Agriculture parent test README; Agriculture bounded-context, sublane, cross-lane,
  policy, and placement documentation; HLS-VI fixture README; NASA HLS connector README;
  Agriculture validator README; TODO-only Agriculture and documentation workflows;
  Makefile test target excluding this lane; generated-receipt schema and PR contract;
  bounded indexed search returning only this README in the direct lane; checked absence
  of representative conftest.py, test_veg_index.py, test_source_role.py, and HLS-VI
  valid_1.json paths / PROPOSED executable vegetation-index test profile, fixture manifest,
  test modules, reason-code vocabulary, schema/contract bindings, deterministic calculations,
  source-role and QA-mask canaries, evidence/policy/release closure tests, correction and
  rollback cases, and CI promotion blocking / CONFLICTED modeled or aggregate context versus
  any future direct-observation or field-truth wording; public aggregate posture versus any
  exact field-resolution exposure; flat versus nested NASA HLS connector topology; detailed
  README expectations versus absent executable proof / UNKNOWN exhaustive unindexed or
  differently named files, fixture payload inventory, canonical vegetation-index object family,
  accepted index formulas and QA profiles, validator executable, source activation, current
  test pass rates, branch-protection significance, production consumers, and release use /
  NEEDS VERIFICATION owners, CODEOWNERS, canonical schemas and contracts, fixture identities,
  source-role vocabulary binding, rights terms, mask and compositing profiles, reason-code
  registry, live-test authorization, CI ownership, promotion-gate adoption, correction cascade,
  and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 0165bbf59e9c7ce85148ff254ba723ef8c116a79
  prior_blob: 9619829359ed8353a96112a7e1999178d57f7ea2
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    schema_home_adr: ab0010a278d766356845c23055f882f328abb418
    drift_register: 97a775522dcd058299f752ac7862d0fc56c13280
    tests_root_readme: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
    agriculture_tests_parent: 35ebf2a578f2a39b4f4766cc4146aafde8124e67
    agriculture_schema_test_readme: 345f667c8d1879853e80087f3609c76cf52bde06
    agriculture_validator_readme: 40d268b425d9939ab6a8cda7bd197ba758572d3f
    hls_vi_fixture_readme: 2dc9bbca4ad57615cb9a6fd46911dd235374c719
    nasa_hls_connector_readme: c6a1726c6e11f164a8b8562f5bb9b7215100a0e1
    agriculture_domain: 6e6b6201b159337e2018e8362bb5848c4518e943
    agriculture_sublanes: c3b403f4944cefea0bd58de5c21985bf146260f2
    agriculture_atmosphere_stress: 8bca9de0133f52fbd8ef11b9830c17119a9e4db5
    agriculture_policy: ba73c387e16f70895f32444e489d6d55dd577b75
    agriculture_workflow: a9f5f212ef61d72fdc209d9f8b173bbf87fb1803
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    pull_request_template: 13c5d4ed045e201188ebb54b518a586b42b481d4
    generated_receipt_schema: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  direct_lane_indexed_files:
    - tests/domains/agriculture/veg_index/README.md
  checked_absent_paths:
    - AGENTS.md
    - tests/AGENTS.md
    - tests/domains/AGENTS.md
    - tests/domains/agriculture/AGENTS.md
    - tests/domains/agriculture/veg_index/AGENTS.md
    - tests/domains/agriculture/veg_index/conftest.py
    - tests/domains/agriculture/veg_index/test_veg_index.py
    - tests/domains/agriculture/veg_index/test_source_role.py
    - fixtures/domains/agriculture/hls_vi/valid/valid_1.json
  open_pull_request_check: no open pull request matched the target path or vegetation-index README query
  bounded_inventory_note: >
    Indexed search and named-path probes establish only the checked snapshot. They do not
    prove permanent absence from history, forks, unindexed paths, generated workspaces,
    Git LFS, external stores, dynamic test generation, or differently named files.
related:
  - ../README.md
  - ../../../README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../../docs/registers/DRIFT_REGISTER.md
  - ../../../../docs/domains/agriculture/DOMAIN.md
  - ../../../../docs/domains/agriculture/sublanes/README.md
  - ../../../../docs/domains/agriculture/atmosphere-stress.md
  - ../../../../docs/domains/agriculture/FILE_SYSTEM_PLAN.md
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../fixtures/domains/agriculture/hls_vi/README.md
  - ../../../../connectors/nasa-hls/README.md
  - ../../../../tools/validators/agriculture/README.md
  - ../../../../.github/workflows/domain-agriculture.yml
  - ../../../../Makefile
  - ../../../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, tests, agriculture, vegetation-index, remote-sensing, hls-vi, modeled, QA-mask, spatial-support, temporal-support, source-role, evidence, policy, release, no-network, fail-closed, correction, rollback]
notes:
  - "This revision replaces the short v0.1 lane summary with a repository-grounded Tests README profile."
  - "The direct lane remains README-only in bounded evidence; no executable test is claimed or created."
  - "Vegetation-index material remains modeled or derived context and cannot be promoted into direct field observation, crop confirmation, damage determination, alert authority, or release approval."
  - "The reusable HLS-VI fixture lane and NASA HLS connector lane remain documentation-only in inspected evidence."
  - "The Agriculture workflow and documentation workflows are TODO echo scaffolds; green completion is not substantive proof."
  - "This change creates no test, fixture payload, schema, contract, policy, validator, connector, source activation, lifecycle object, evidence object, release object, map layer, API route, AI answer, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/domains/agriculture/veg_index/` — Agriculture Vegetation-Index Test Boundary

> **One-line purpose.** Define the enforceability boundary for proving that Agriculture vegetation-index material preserves modeled/derived source role, quality-mask and support metadata, evidence and policy constraints, public-safe aggregation, finite failure outcomes, and release subordination without becoming direct field truth, crop confirmation, alert authority, or publication authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: vegetation index" src="https://img.shields.io/badge/lane-vegetation__index-success">
  <img alt="Maturity: README only" src="https://img.shields.io/badge/maturity-README__only-lightgrey">
  <img alt="Source role: modeled" src="https://img.shields.io/badge/source__role-modeled-purple">
  <img alt="Public exact field detail: deny" src="https://img.shields.io/badge/public__field__detail-DENY-red">
  <img alt="Network: off by default" src="https://img.shields.io/badge/network-off__by__default-critical">
  <img alt="CI: TODO only" src="https://img.shields.io/badge/CI-TODO__only-orange">
</p>

> [!IMPORTANT]
> **Current implementation is not established.** Bounded indexed search surfaced only this README in the direct lane, and representative executable paths were absent. The HLS-VI fixture lane and NASA HLS connector lane are also documentation-only in inspected evidence. This README defines what future tests must prove; it does not claim that those tests, fixtures, schemas, validators, sources, or release gates already exist.

> [!CAUTION]
> **Vegetation indices are modeled or derived context, not direct field observations.** A value, raster cell, composite, anomaly, summary, or rendered color must not be relabeled as crop identity, planting confirmation, yield, damage, operator behavior, field condition, regulatory finding, or alert authority merely because it passed a calculation or schema check.

> [!WARNING]
> **Public exact field-level exposure fails closed.** A test must reject or restrict output that resolves modeled, aggregate, or remotely sensed context to a private field, operator, parcel-adjacent record, or unsupported precision unless a governed transform, evidence chain, policy decision, review state, release record, correction path, and rollback target explicitly support the narrower output.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-directory-rules-basis) · [Status](#current-evidence-and-maturity) · [Scope](#scope-and-non-scope) · [Inputs](#accepted-input-families) · [Fixtures](#fixture-families-and-routing) · [Invariants](#vegetation-index-invariants) · [Cases](#required-case-matrix) · [Layers](#validation-layers) · [Outcomes](#finite-outcomes-and-reason-codes) · [Network](#no-network-and-live-test-separation) · [Commands](#deterministic-setup-and-commands) · [Failures](#failure-interpretation) · [CI](#ci-and-promotion-boundary) · [Sensitivity](#rights-sensitivity-and-public-safe-test-data) · [Maintenance](#maintenance-and-fixture-update-rules) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#changelog-correction-and-rollback)

---

## Purpose

`tests/domains/agriculture/veg_index/` is the Agriculture domain test sublane for vegetation-index and related remotely sensed context.

Its durable question is:

> Can a vegetation-index candidate be processed, interpreted, tested, and potentially prepared for a governed public-safe derivative while preserving source identity, modeled/derived role, index and band semantics, quality-mask state, spatial and temporal support, uncertainty, evidence closure, rights and sensitivity posture, lifecycle state, policy decision, release state, correction lineage, and rollback readiness?

A complete test family should prove at least these boundaries:

1. the source or upstream artifact is explicitly identified;
2. modeled or derived source role is preserved through every transform;
3. the index definition and required input bands are explicit;
4. scale, offset, units or unitless semantics, no-data handling, and valid range are explicit where applicable;
5. quality masks, exclusions, and compositing rules are not silently dropped;
6. observed time, source time, retrieval time, valid time, and release time remain distinguishable where material;
7. spatial support, resolution, footprint, CRS, and generalization limits remain visible;
8. uncertainty and caveats survive calculation, aggregation, cataloging, API projection, and display;
9. evidence references resolve before answer-like or claim-bearing output is accepted;
10. public outputs remain aggregate-safe or generalized unless a stronger governed basis exists;
11. policy and release state are required before public-facing use;
12. correction, supersession, withdrawal, and rollback behavior are testable;
13. the default suite remains deterministic and no-network;
14. failures produce finite, reviewable outcomes rather than silent acceptance.

This lane proves enforceability. It does not create Agriculture truth, remote-sensing truth, source authority, schema authority, policy authority, evidence authority, lifecycle promotion, release approval, or public publication.

[Back to top](#top)

---

## Authority and Directory Rules basis

**Canonical test responsibility / non-authoritative domain sublane.**

Directory Rules place enforceability proof under `tests/`, with the domain expressed as a segment: `tests/domains/agriculture/veg_index/`. The target path already exists, so this revision does not create or move a responsibility boundary.

| Concern | Authority home | This lane's role |
|---|---|---|
| Vegetation-index executable tests | `tests/domains/agriculture/veg_index/` | Owns test modules and assertions when implemented. |
| Agriculture test organization | `tests/domains/agriculture/` | Owns the domain test index and child-lane routing. |
| Vegetation-index semantic meaning | `contracts/domains/agriculture/` or accepted shared/domain contract family | Tests meaning; does not define it. |
| Machine-checkable shape | `schemas/contracts/v1/domains/agriculture/` or accepted shared family per ADR-0001 | Tests shape; does not author schemas. |
| Source identity and activation | `data/registry/sources/` and source-governance surfaces | Consumes references; cannot activate a source. |
| NASA HLS acquisition/admission | Accepted connector path under `connectors/` | Tests bounded outputs; cannot fetch or admit by default. |
| Reusable vegetation-index fixtures | `fixtures/domains/agriculture/hls_vi/` or accepted successor | Consumes synthetic fixtures; does not duplicate reusable fixture authority. |
| Test-local fixture material | `tests/fixtures/` only when the owning test documents the split | May consume narrowly scoped material; current direct fixture binding is unverified. |
| Validator implementation | `tools/validators/` or accepted successor | Tests validator behavior; does not implement durable validation here. |
| Policy, rights, sensitivity, exposure | `policy/` | Tests finite decisions and obligations; cannot grant permission. |
| Evidence, receipts, proofs, catalogs | accepted `data/` trust-object lanes | Tests references and closure; does not emit authoritative records. |
| Lifecycle artifacts | `data/raw`, `work`, `quarantine`, `processed`, `catalog`, `triplet`, `published` | Uses synthetic representations only; stores no lifecycle data here. |
| Release, correction, rollback | `release/` | Tests prerequisites and behavior; cannot approve a transition. |
| Public API, map, UI, export, AI output | governed application and released-artifact surfaces | Tests boundaries only; cannot expose a route or layer. |

### Placement determination

- **CONFIRMED:** `tests/` is the canonical enforceability root.
- **CONFIRMED:** `tests/domains/agriculture/veg_index/README.md` exists at the pinned base.
- **CONFIRMED:** the target remains in the same path and responsibility root.
- **CONFIRMED:** ADR-0001 identifies `schemas/contracts/v1/domains/agriculture/` as the proposed canonical domain schema home for machine shape.
- **CONFIRMED:** no path-scoped `AGENTS.md` file was present at the named root-to-target probes.
- **CONFIRMED:** the drift register contains no vegetation-index-specific placement resolution that changes this target.
- **NOT APPLICABLE:** no new root, schema home, lifecycle stage, release home, proof home, or registry home is created.
- **NOT APPLICABLE:** no ADR is triggered by this README-only revision and its established generated-receipt companion.

### Anti-collapse rules

This lane must not collapse:

- index calculation into source observation;
- surface reflectance into vegetation condition;
- vegetation condition into crop identity;
- crop identity into planting confirmation;
- a grid cell into a field observation;
- an aggregate into a place-specific assertion;
- a modeled anomaly into damage or loss;
- a stress indicator into an alert or operational instruction;
- schema validity into semantic validity;
- semantic validity into evidence closure;
- evidence closure into policy permission;
- policy permission into release approval;
- release approval into permanent correctness;
- a green workflow into substantive test coverage;
- README presence into executable maturity.

[Back to top](#top)

---

## Current evidence and maturity

| Surface | Inspected state | Safe conclusion |
|---|---|---|
| Direct `veg_index/` lane | **CONFIRMED README-only in bounded indexed search** | Documentation exists; executable tests are not established. |
| Representative `conftest.py` | **NOT FOUND at named path** | No direct fixture/plugin setup is established by that conventional path. |
| Representative `test_veg_index.py` | **NOT FOUND at named path** | No monolithic vegetation-index test module is established by that path. |
| Representative `test_source_role.py` | **NOT FOUND at named path** | No direct source-role test module is established by that path. |
| Agriculture parent tests | **CONFIRMED README** | Lists `veg_index/`; implementation remains NEEDS VERIFICATION. |
| HLS-VI fixture lane | **CONFIRMED README-only in inspected evidence** | Fixture intent exists; payloads and consumer bindings are not established. |
| Representative HLS-VI `valid_1.json` | **NOT FOUND at named path** | That conventional fixture instance is absent; differently named material remains UNKNOWN. |
| NASA HLS connector | **CONFIRMED README-only at direct implementation probes** | No supported fetch, QA decoder, admission path, or test handoff is established. |
| Connector topology | **CONFLICTED** | Flat and nested NASA HLS documentation paths coexist; this test README does not choose between them. |
| Agriculture validator lane | **CONFIRMED README-only in bounded direct search** | No Agriculture validator executable is established. |
| Agriculture policy lane | **CONFIRMED draft documentation and scaffolds** | Intended policy posture exists; runtime enforcement remains unproved. |
| Agriculture workflow | **CONFIRMED TODO echo jobs** | Workflow completion cannot prove validation, proof, or release behavior. |
| `make test` | **CONFIRMED excludes this lane** | The repository default test target runs shared schema/contract tests only. |
| Open target PR | **NONE MATCHED by bounded query** | No existing open PR was found for this target at preflight. |
| Current pass rates | **UNKNOWN** | No executable lane and no meaningful lane-specific CI result were established. |
| Production or release use | **UNKNOWN** | No consumer, activated source, release manifest, or public layer was verified. |

### Maturity summary

| Capability | Status |
|---|---:|
| README boundary | **CONFIRMED** |
| Executable tests | **NOT ESTABLISHED** |
| Canonical fixture payloads | **NOT ESTABLISHED** |
| Canonical schema/contract binding | **NEEDS VERIFICATION** |
| Agriculture vegetation-index validator | **NOT ESTABLISHED** |
| No-network test harness | **NOT ESTABLISHED** |
| Live-test lane | **NOT AUTHORIZED / NOT ESTABLISHED** |
| Policy enforcement | **UNKNOWN** |
| Evidence-resolution test coverage | **NOT ESTABLISHED** |
| Release-gate integration | **NOT ESTABLISHED** |
| CI promotion significance | **UNKNOWN** |
| Production readiness | **UNKNOWN** |

[Back to top](#top)

---

## Scope and non-scope

### In scope

This lane may contain tests for:

- vegetation-index source-role preservation;
- index identity and definition metadata;
- band/reference semantics and deterministic computation;
- scale, offset, valid range, no-data, and numeric edge behavior;
- quality-mask preservation and required exclusions;
- spatial support, resolution, CRS, footprint, and generalization;
- temporal support, acquisition window, compositing window, and freshness;
- uncertainty, confidence, caveat, and model-version propagation;
- aggregation and suppression requirements;
- field/operator/parcel-adjacent exposure denial;
- source, rights, sensitivity, evidence, policy, review, release, correction, and rollback references;
- catalog and API/UI/AI projection boundaries;
- valid, invalid, denied, abstained, held, quarantined, and error cases;
- deterministic no-network replay;
- correction and supersession non-regression.

### Out of scope

This lane must not contain or perform:

- production-sized source imagery, rasters, COGs, tiles, or lifecycle datasets;
- real private field geometry, operator identity, parcel-owner joins, or restricted records;
- source credentials, API keys, tokens, cookies, or live endpoint configuration;
- live network calls in the default suite;
- connector implementation or source activation;
- canonical vegetation-index formulas or scientific policy by assertion;
- Agriculture domain contracts or schemas;
- policy rules or release decisions;
- validator implementation that belongs under `tools/validators/`;
- source registry records, EvidenceBundles, receipts, proofs, catalogs, or release objects as authority;
- map layers, API routes, dashboards, reports, exports, alerts, recommendations, or AI answers;
- generated language treated as expected truth;
- publication or promotion.

### Explicit non-authority statement

A test may prove that a candidate meets a declared expectation. It cannot prove that:

- the source is authoritative for a broader claim;
- the index is scientifically suitable for every crop, season, place, or decision;
- a crop is present;
- a field is healthy or damaged;
- a person or operator performed an action;
- an alert should be issued;
- an Agriculture object should be published;
- an AI answer is correct beyond its cited released evidence.

[Back to top](#top)

---

## Accepted input families

Tests should consume only bounded, reviewable, synthetic or public-safe inputs.

| Input family | Minimum test-visible metadata | Authority limit |
|---|---|---|
| Source descriptor projection | stable source ID, provider/source family, source role, rights/sensitivity posture, version or source head | Does not activate source access. |
| Asset/granule projection | collection/product identity, granule or asset identity, acquisition time, checksum/digest where material | Does not establish source authenticity without governed evidence. |
| Band/input projection | band names/roles, scale/offset, no-data, valid range, spatial support | Does not define a canonical formula by itself. |
| Vegetation-index candidate | index identity, formula/profile reference, numeric result or compact array, model/algorithm version | Remains modeled/derived context. |
| QA/mask projection | mask profile/version, cloud/shadow/snow/water/no-data handling, excluded-pixel counts or flags | Does not prove all source-specific QA semantics are covered. |
| Spatial support projection | CRS, pixel/grid support, footprint or generalized geometry, resolution, aggregation unit | Must not imply unsupported field precision. |
| Temporal support projection | source/acquisition time, observed/valid interval, compositing window, retrieval time, release time where relevant | Must not collapse distinct time kinds. |
| Uncertainty/caveat projection | quality flags, confidence class, limitations, stale state | Must survive downstream projections. |
| Evidence projection | `EvidenceRef`, resolution result, citation status, relevant receipt/proof references | Must resolve or produce a finite non-answer outcome. |
| Policy/release projection | sensitivity tier, audience, obligations, review state, release state, rollback target | Does not confer authority merely by presence. |
| Expected-result projection | finite outcome, reason code, allowed fields, denied fields, deterministic values | Fixture expectation only, not source truth. |

### Input rejection rules

The default suite should reject or quarantine inputs that:

- have no source identity or source role;
- label modeled/derived material as observed;
- omit index identity or required calculation profile;
- omit QA/mask state when the profile requires it;
- carry invalid or non-finite numbers where the contract forbids them;
- omit spatial or temporal support needed to interpret the value;
- claim finer precision than the input supports;
- contain real private field/operator/person information;
- depend on a live endpoint, credential, clock, or mutable external state;
- cite unresolved evidence while requesting answer-like output;
- request public use without policy and release context.

[Back to top](#top)

---

## Fixture families and routing

### Reusable fixture home

The current repository documents `fixtures/domains/agriculture/hls_vi/` as the reusable Agriculture vegetation-index fixture lane. In inspected evidence, that lane contains a README but no confirmed payload or consumer binding.

A future fixture family may use small files such as:

```text
fixtures/domains/agriculture/hls_vi/
  README.md
  valid/
    valid_<case>.json
  invalid/
    invalid_<case>.json
    invalid_<case>.expected_error.txt
  denied/
    denied_<case>.json
  abstained/
    abstained_<case>.json
  quarantined/
    quarantined_<case>.json
  error/
    error_<case>.json
```

> [!NOTE]
> This layout is **PROPOSED** and must be reconciled with the fixture-root README, actual consumers, schemas, manifests, and repository conventions before files are added. It does not describe current inventory.

### Fixture families to establish

| Family | Purpose | Required posture |
|---|---|---|
| `source_role` | Prove modeled/derived role is fixed and cannot upgrade to observed. | Include positive and anti-collapse cases. |
| `index_definition` | Prove index/profile identity and input-band requirements. | Formula/profile reference must be explicit. |
| `qa_mask` | Prove required mask metadata and exclusions are preserved. | Missing required mask state fails closed. |
| `numeric_edges` | Zero denominator, no-data, non-finite values, clipping, scale/offset, range. | Deterministic, explicit expected outcome. |
| `spatial_support` | Resolution, CRS, footprint, grid support, aggregation/generalization. | Reject unsupported exact-place claims. |
| `temporal_support` | Acquisition, composite, valid interval, retrieval, freshness/stale state. | Keep time kinds distinct. |
| `uncertainty` | Confidence, quality flags, caveat propagation. | Downstream projections retain limitations. |
| `aggregation` | County/grid/public-safe summaries and suppression thresholds. | Require `AggregationReceipt` or equivalent when accepted. |
| `sensitivity` | Field/operator/parcel-adjacent exposure attempts. | Public exact exposure denied by default. |
| `evidence` | Resolved, missing, stale, conflicted, withdrawn evidence. | Return ANSWER only for supported released scope. |
| `policy_release` | Allowed, restricted, held, denied, unreleased, superseded states. | Most restrictive decision wins. |
| `correction_rollback` | Corrected, withdrawn, superseded, rollback-target cases. | No stale artifact remains silently authoritative. |
| `projection` | Catalog/API/Evidence Drawer/Focus Mode field preservation. | No authority upgrade or caveat loss. |

### Fixture data rules

Fixtures must be:

- synthetic or safely generalized;
- small enough for review in a pull request;
- deterministic and self-contained;
- free of credentials and private endpoints;
- free of real operator/person/parcel-sensitive detail;
- accompanied by source-role and sensitivity intent;
- paired with expected finite outcomes and reason codes;
- versioned or hash-pinned when a calculation profile matters;
- updated with the consuming test in the same change;
- withdrawn or superseded visibly when an expectation changes.

Large raster payloads, real source scenes, or mutable downloads do not belong in this fixture lane.

[Back to top](#top)

---

## Vegetation-index invariants

### 1. Source-role invariant

Vegetation-index material remains `modeled` or `derived` unless an accepted source-role vocabulary defines a narrower term. Promotion, validation, cataloging, rendering, summarization, or review must not upgrade it to `observed`.

Tests must fail when:

- `modeled` becomes `observed`;
- `aggregate` becomes field observation;
- a derived index is described as source-native measurement without support;
- a source-role field disappears across a transform or projection.

### 2. Identity invariant

A testable candidate should preserve enough identity to distinguish:

- provider and source family;
- collection/product and version;
- granule/asset/tile identity where material;
- input bands or band roles;
- index/profile identity;
- algorithm/model version;
- QA/mask profile version;
- spatial and temporal support;
- transform or aggregation identity;
- content/spec hashes where governed contracts require them.

Two different input scenes, profiles, masks, windows, or resolutions must not collapse into one identity merely because their numeric result is equal.

### 3. Calculation invariant

When calculation logic exists, tests should prove:

- required inputs are present;
- input ordering and semantics are explicit;
- scale/offset and no-data handling occur before or after calculation according to the accepted profile;
- denominator and zero/near-zero behavior is deterministic;
- non-finite results are rejected or represented by an accepted no-data outcome;
- clipping or range constraints are explicit rather than silent;
- precision and rounding are stable;
- repeated runs with the same pinned inputs produce the same result.

This README does not select a canonical formula or tolerance. Those remain NEEDS VERIFICATION until contract, schema, implementation, and scientific review converge.

### 4. QA-mask invariant

If the accepted profile requires QA filtering, tests must prove that:

- mask identity and version are present;
- excluded conditions are explicit;
- masked pixels cannot silently re-enter an aggregate;
- no-data is distinct from valid zero;
- cloud, shadow, snow, water, saturation, or other profile-defined exclusions are not silently ignored;
- downstream summaries carry mask/coverage statistics or caveats where required;
- missing mandatory QA state produces a finite failure outcome.

### 5. Spatial-support invariant

Tests must preserve:

- CRS and coordinate/footprint semantics;
- source pixel or grid support;
- output resolution;
- aggregation cell, county, HUC, or other public-safe unit;
- resampling/generalization method where material;
- geometry/area coverage caveats;
- scale-dependent fitness limits.

A rendered field polygon does not convert a grid-derived value into a field observation. A test should reject any projection that implies a finer support than the evidence carries.

### 6. Temporal-support invariant

Tests should distinguish, where applicable:

- acquisition/source time;
- observed or valid interval;
- compositing window;
- retrieval time;
- processing time;
- catalog time;
- release time;
- correction or supersession time.

A composite must not be described as a single-time observation. Stale or temporally unsupported requests should return `ABSTAIN`, `HOLD`, `DENY`, or `ERROR` according to the owning policy and runtime contract.

### 7. Cross-lane ownership invariant

Agriculture owns Agriculture-side interpretation and stress context. It does not re-own:

- Atmosphere/Air observations;
- Soil map-unit, horizon, or soil-property truth;
- Hydrology observations or flood/drought authority;
- People/Land identity, ownership, parcel, or operator truth;
- Flora taxonomy or occurrence truth;
- Hazards alert authority.

Tests should prove that cross-lane references preserve owning-domain identity, source role, sensitivity, evidence support, and release state.

### 8. Evidence invariant

Claim-bearing or answer-like output requires resolvable released support. Tests should prove:

- `EvidenceRef` resolves to the intended `EvidenceBundle` or equivalent accepted object;
- citations identify the correct source/asset/profile scope;
- missing, stale, conflicted, withdrawn, or policy-blocked evidence does not produce `ANSWER`;
- projections retain citation and limitation metadata;
- generated summaries cannot substitute for evidence.

### 9. Public-safety invariant

The public default is aggregate or generalized context. Tests should deny or restrict:

- exact private field/operator/parcel-adjacent exposure;
- unsupported crop or damage claims;
- surveillance-like time series tied to identifiable operators;
- source-rights violations;
- cross-lane joins that increase sensitivity without recorded review;
- release-facing output without rollback and correction support.

### 10. Non-alert invariant

Vegetation-index, drought-stress, pest-stress, weather, smoke, or anomaly context must not become an emergency alert, regulatory determination, crop-management instruction, insurance decision, or operational directive through test wording or expected output.

[Back to top](#top)

---

## Required case matrix

Every implemented test family should include the relevant positive and negative classes below. A category may be marked not applicable only with a reason.

| Class | Representative condition | Expected result |
|---|---|---|
| **Valid** | Modeled role, source/profile identity, QA state, support, evidence, policy, and release context satisfy the declared test contract. | `PASS` or runtime `ANSWER` only within supported scope. |
| **Invalid** | Required field, type, enum, range, band, profile, mask, time, CRS, or digest is malformed. | Test failure / validation `ERROR` with bounded reason. |
| **Denied** | Public exact field/operator/parcel exposure; rights block; source-role upgrade; unreleased sensitive output. | `DENY` or policy `RESTRICT` with obligations; no protected payload. |
| **Abstained** | Evidence missing, stale, conflicted, unresolved, or outside spatial/temporal support. | `ABSTAIN`; no fabricated value or explanation. |
| **Held** | Steward review, transform receipt, policy decision, or release gate is pending. | `HOLD` or accepted equivalent; no promotion. |
| **Quarantined** | Source identity/integrity/rights/QA is insufficient for admission or normalization. | `QUARANTINE`; reason and repair path recorded. |
| **Error** | Calculator, schema resolver, validator, policy engine, evidence resolver, or fixture loader fails. | `ERROR`; fail closed; no fallback allow. |
| **Corrected** | A prior value/profile/evidence reference is corrected. | Supersession/correction lineage visible; old result no longer silently current. |
| **Withdrawn** | Source or evidence is withdrawn or rights change. | Downstream answer/release denied or abstained; withdrawal propagated. |
| **Rollback** | Release or transform is reverted to a known target. | Prior safe state restored and identifiable; no mixed-version output. |

### Minimum negative canaries

An implementation should include explicit canaries for:

1. missing source ID;
2. missing source role;
3. modeled-as-observed upgrade;
4. missing index/profile identity;
5. missing required input band;
6. invalid scale/offset or no-data semantics;
7. zero/invalid denominator or non-finite result;
8. missing mandatory QA/mask metadata;
9. masked pixel included in aggregate;
10. composite presented as single-time observation;
11. field precision finer than source support;
12. unresolved `EvidenceRef`;
13. missing rights or sensitivity posture;
14. missing aggregation/redaction receipt;
15. missing release state or rollback target;
16. live network attempt in default suite;
17. private data in fixture or failure output;
18. correction or withdrawal not propagated;
19. generated summary accepted as authority;
20. TODO workflow interpreted as substantive proof.

[Back to top](#top)

---

## Validation layers

A mature lane should exercise distinct layers rather than relying on one broad test.

| Layer | What it proves | What it does not prove |
|---|---|---|
| File/JSON parsing | Fixture and schema files are readable. | Semantic correctness or authority. |
| Schema conformance | Machine shape meets an accepted schema. | Scientific fitness, evidence, policy, or release. |
| Semantic contract | Terms, required meanings, and invariants align. | Source authenticity or admissibility. |
| Source identity/role | Provider, product, asset, and role are preserved. | Rights clearance or evidence closure by itself. |
| Numeric/calculation | Deterministic math and edge behavior match the pinned profile. | Fitness for every use or place. |
| QA/mask | Required exclusions and coverage metadata are preserved. | Complete scientific validation of all source conditions. |
| Spatial support | Resolution, CRS, footprint, and aggregation claims are bounded. | Public permission or field truth. |
| Temporal support | Time kinds, windows, freshness, and stale behavior are bounded. | Long-term validity beyond evidence. |
| Rights/sensitivity | Requested exposure is allowed, restricted, held, or denied. | Release approval by itself. |
| Evidence/citation | Support resolves and citations match scope. | Policy or release completion. |
| Lifecycle/catalog | State transitions and catalog/proof references are coherent. | Publication merely because a catalog entry exists. |
| Release/correction/rollback | Public-impact prerequisites and reversal paths are present. | Permanent correctness. |
| API/UI/map/AI projection | Downstream surfaces retain role, evidence, caveats, and finite outcomes. | Canonical truth in the presentation layer. |

### Recommended implementation decomposition

The following module names are **PROPOSED**, not current files:

```text
tests/domains/agriculture/veg_index/
  README.md
  test_source_role.py
  test_index_definition.py
  test_numeric_edges.py
  test_qa_mask.py
  test_spatial_support.py
  test_temporal_support.py
  test_aggregation_and_sensitivity.py
  test_evidence_policy_release.py
  test_projection_boundaries.py
  test_correction_and_rollback.py
  test_no_network.py
```

Before creating these files, confirm contract/schema/fixture ownership, actual package imports, reason-code conventions, and repository test collection.

[Back to top](#top)

---

## Finite outcomes and reason codes

### Outcome vocabulary

Tests must distinguish test-run outcomes from runtime/policy outcomes.

| Vocabulary | Values | Use |
|---|---|---|
| Test assertion | pass / fail / skip / xfail only when justified | Pytest or accepted runner result. |
| Runtime envelope | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Governed public/internal response contract. |
| Policy decision | `ALLOW`, `DENY`, `RESTRICT`, `HOLD`, `ABSTAIN`, `ERROR` | Admissibility and obligations. |
| Lifecycle disposition | admit, quarantine, reject, hold, promote candidate | Pipeline/test representation only; publication remains separate. |

A test must not translate `ABSTAIN`, `DENY`, `HOLD`, or `QUARANTINE` into failure when that is the expected safe behavior. Conversely, a safe finite outcome must not make the overall suite pass if required metadata or policy evaluation was never exercised.

### Proposed reason-code seed set

The names below are **PROPOSED** test-design seeds and do not establish a canonical registry:

| Reason code | Intended condition |
|---|---|
| `VEG_INDEX_SOURCE_ID_MISSING` | Source identity absent. |
| `VEG_INDEX_SOURCE_ROLE_MISSING` | Source role absent. |
| `VEG_INDEX_MODELED_AS_OBSERVED` | Derived/model role upgraded to observed. |
| `VEG_INDEX_PROFILE_MISSING` | Index or calculation profile absent. |
| `VEG_INDEX_REQUIRED_BAND_MISSING` | Required input band/role absent. |
| `VEG_INDEX_NUMERIC_INVALID` | Invalid range, non-finite value, denominator, scale, or offset behavior. |
| `VEG_INDEX_QA_MASK_MISSING` | Mandatory QA/mask profile absent. |
| `VEG_INDEX_QA_LEAK` | Masked/excluded values enter result. |
| `VEG_INDEX_SPATIAL_SUPPORT_MISSING` | CRS/resolution/footprint/support absent. |
| `VEG_INDEX_PRECISION_UNSUPPORTED` | Output implies finer precision than evidence. |
| `VEG_INDEX_TEMPORAL_SUPPORT_MISSING` | Acquisition/window/validity support absent. |
| `VEG_INDEX_STALE` | Requested use exceeds freshness or valid interval. |
| `VEG_INDEX_EVIDENCE_UNRESOLVED` | Evidence reference cannot resolve. |
| `VEG_INDEX_RIGHTS_UNRESOLVED` | Rights/terms posture missing or unclear. |
| `VEG_INDEX_FIELD_EXPOSURE_DENIED` | Public exact field/operator/parcel exposure blocked. |
| `VEG_INDEX_AGGREGATION_RECEIPT_MISSING` | Required aggregate transform proof absent. |
| `VEG_INDEX_RELEASE_STATE_MISSING` | Public-facing use lacks release state. |
| `VEG_INDEX_ROLLBACK_TARGET_MISSING` | Release-facing use lacks reversal target. |
| `VEG_INDEX_LIVE_NETWORK_FORBIDDEN` | Default test attempted network access. |
| `VEG_INDEX_PRIVATE_FIXTURE_DATA` | Fixture or error output contains protected detail. |
| `VEG_INDEX_CORRECTION_NOT_PROPAGATED` | Supersession/withdrawal/correction did not cascade. |

Canonical reason codes, namespaces, and mappings remain NEEDS VERIFICATION.

[Back to top](#top)

---

## No-network and live-test separation

### Default suite

The default vegetation-index test suite must be:

- no-network;
- credential-free;
- deterministic;
- based on local synthetic fixtures;
- independent of current external service availability;
- independent of mutable remote files;
- independent of wall-clock time except through injected/fixed clocks;
- safe to run in a public pull request environment;
- unable to publish, promote, or mutate lifecycle stores.

A test that attempts DNS, HTTP, cloud storage, source API, authentication, or remote raster access in the default suite should fail with a bounded reason.

### Separate live tests

Any future live-source test must be explicitly separate and must have:

1. a named purpose that cannot be met by fixtures;
2. explicit authorization;
3. source terms and rights review;
4. secret handling outside logs and fixtures;
5. endpoint allowlisting and bounded scope;
6. timeout, retry, backoff, and rate-limit behavior;
7. no publication side effects;
8. safe redaction of errors and metadata;
9. a scheduled/manual lane distinct from pull-request default tests;
10. result labeling that does not turn source availability into correctness.

No such live test lane is established by inspected evidence.

[Back to top](#top)

---

## Deterministic setup and commands

### Current repository-grounded inventory commands

```bash
find tests/domains/agriculture/veg_index -maxdepth 5 -type f | sort
find fixtures/domains/agriculture/hls_vi -maxdepth 5 -type f 2>/dev/null | sort
```

These commands inspect visible files only. They do not prove test collection, pass status, dynamic fixtures, generated data, external storage, or release use.

### Future lane-specific test command

Once executable tests and dependencies exist, the repository's current Python/pytest convention supports a lane command such as:

```bash
python -m pytest tests/domains/agriculture/veg_index -q
```

This command is **PROPOSED for future use** and was not run for this README-only revision because no executable test module is established at the target lane.

### Current root test target limitation

The current `make test` target runs:

```bash
python -m pytest tests/schemas tests/contracts -q
```

It does not collect `tests/domains/agriculture/veg_index/`. Therefore `make test` success cannot be reported as vegetation-index test success.

### Fail-closed command rule

Do not append `|| true` to a command presented as validation. If a diagnostic command is intentionally non-blocking, label it diagnostic and report its exit status separately.

### Reproducibility requirements

When implementation lands, test setup should pin or record:

- package/environment lock or accepted dependency mechanism;
- Python/runtime version where the repository requires it;
- fixture hashes or immutable IDs;
- schema and contract versions;
- calculation/profile version;
- source and QA profile version;
- injected clock/time zone;
- deterministic seed when randomized testing is used;
- expected reason-code registry version;
- network-disabled configuration.

[Back to top](#top)

---

## Failure interpretation

| Failure | Interpretation | Safe response |
|---|---|---|
| Parse/schema failure | Input or expected output does not meet machine shape. | Reject fixture/candidate; do not infer broader invalidity without semantic evidence. |
| Contract/invariant failure | Meaning or domain rule is violated. | Fail test and identify the violated invariant. |
| Source-role failure | Authority character changed or disappeared. | Build-stop for affected path; no promotion. |
| QA/mask failure | Required exclusions or coverage semantics were lost. | Quarantine or error; no public summary. |
| Numeric mismatch | Calculation/profile or expected fixture disagrees. | Fail deterministically; inspect profile/version and rounding. |
| Spatial/temporal support failure | Output claim exceeds evidence support. | Abstain, deny, restrict, or quarantine according to context. |
| Rights/sensitivity failure | Requested exposure is not permitted or unresolved. | Deny/hold; redact protected detail from logs. |
| Evidence failure | Citation/support cannot resolve or is stale/withdrawn. | Abstain; do not fabricate. |
| Policy engine failure | Admissibility cannot be determined. | Error and fail closed; never default allow. |
| Release/rollback failure | Public-impact prerequisites or reversal path absent. | Block promotion/release. |
| Network attempt | Default suite is non-deterministic or unsafe. | Fail test and identify attempted boundary. |
| CI scaffold success | Workflow executed only TODO steps. | Report non-substantive; do not upgrade maturity. |

### What a passing suite does not prove

Even a complete green lane would not prove:

- the underlying source is error-free;
- the chosen index is fit for every agronomic question;
- a crop, field condition, yield, damage, or operator action is true;
- every Kansas geography, date, sensor, season, or atmospheric condition is covered;
- source rights permit every downstream use;
- an aggregate may be disaggregated safely;
- a policy decision applies to another audience or release;
- a release was approved;
- a map, API, export, or AI answer is authoritative without released evidence;
- future source/product versions remain compatible;
- correction and rollback have been exercised in production.

[Back to top](#top)

---

## CI and promotion boundary

### Current state

The inspected `.github/workflows/domain-agriculture.yml` triggers on pull requests and pushes to `main`, but its jobs only check out the repository and echo TODO messages. The documentation build, link-check, and citation-validation workflows are also TODO echo scaffolds.

Therefore:

- workflow presence is CONFIRMED;
- substantive Agriculture vegetation-index validation is NOT ESTABLISHED;
- a green check does not prove lane execution;
- branch-protection significance is UNKNOWN;
- no current workflow may be cited as release or promotion proof for this lane.

### Future CI requirements

A meaningful lane gate should:

1. collect the target test modules explicitly;
2. run with network disabled;
3. validate fixture manifests and valid/invalid polarity;
4. exercise source-role, QA, support, evidence, policy, release, correction, and rollback cases;
5. emit machine-readable test results;
6. distinguish expected `DENY`/`ABSTAIN`/`HOLD`/`QUARANTINE` from unexpected failures;
7. fail when required categories are skipped without approval;
8. block only after the workflow, ownership, and gate significance are reviewed;
9. never publish or promote merely because tests pass;
10. link the test run to the exact commit, fixture hashes, schemas, profiles, and reason-code version.

### Promotion rule

Tests provide evidence to a gate. They do not perform promotion. Publication still requires the owning validation, policy, review, proof, release, correction, and rollback controls.

[Back to top](#top)

---

## Rights, sensitivity, and public-safe test data

Agriculture vegetation-index testing can become sensitive when combined with exact field boundaries, operator identity, parcel ownership, production/yield records, private inputs, or fine-grained time series.

### Default posture

- Use synthetic or generalized geometry.
- Use fictional identifiers.
- Avoid real operator, owner, resident, address, parcel, or account data.
- Avoid source payloads whose redistribution rights are unclear.
- Do not embed credentials, signed URLs, private endpoints, or access tokens.
- Do not include restricted source metadata in expected errors.
- Prefer county, grid, watershed, or other reviewed aggregate-safe examples.
- Record aggregation/generalization intent in fixture metadata.
- Ensure failure snapshots cannot leak protected values.

### Sensitive-case testing

When testing a denial or redaction path, represent sensitive conditions with synthetic markers rather than real sensitive content. A denial fixture should prove the policy behavior without reproducing the protected material.

### Public-safe output rule

A public-safe expected result should expose only fields justified by the fixture's source role, evidence, sensitivity, rights, audience, release, and transform posture. Omitted or redacted fields should be asserted explicitly so future refactors cannot reintroduce them silently.

[Back to top](#top)

---

## Maintenance and fixture-update rules

Update this README when any of the following changes:

- executable test modules are added, renamed, split, or removed;
- fixture families or manifest conventions change;
- a canonical vegetation-index contract or schema is accepted;
- the NASA HLS connector topology is resolved;
- a source descriptor or activation record becomes authoritative;
- index, band, QA/mask, calculation, or compositing profiles change;
- spatial/temporal support rules change;
- policy outcomes, obligations, or reason codes change;
- public aggregation/generalization rules change;
- EvidenceBundle, receipt, proof, catalog, release, correction, or rollback bindings change;
- the default test command or CI workflow becomes substantive;
- owners or CODEOWNERS become real;
- a live-test lane is authorized or retired;
- a source/product version change invalidates fixtures;
- an incident or correction exposes a missing test.

### Fixture change checklist

Before merging a fixture change:

- [ ] Identify the consuming test.
- [ ] State the test class: valid, invalid, denied, abstained, held, quarantined, error, corrected, withdrawn, or rollback.
- [ ] Confirm the fixture is synthetic/public-safe and rights-cleared.
- [ ] Preserve source role and support metadata.
- [ ] Pin the profile/schema/contract version used by the expectation.
- [ ] Update expected outcome and reason code.
- [ ] Add or update a negative canary when the change fixes a boundary defect.
- [ ] Verify no network or credential dependency was introduced.
- [ ] Run the lane-specific command when implementation exists.
- [ ] Record any skipped category and justification.
- [ ] Update generated receipts or operation records required by repository convention.

### Correction and supersession

When a fixture or expected result was wrong:

1. describe the error;
2. identify affected tests and downstream claims;
3. supersede rather than silently overwrite when review history matters;
4. add a regression case that would have caught the defect;
5. update evidence/profile/version references;
6. verify withdrawn or stale expectations cannot remain current;
7. record rollback or restoration instructions.

[Back to top](#top)

---

## Definition of done

This lane may be described as an implemented vegetation-index test boundary only when all applicable items are verified:

### Placement and authority

- [ ] The target path remains under the canonical `tests/` responsibility root.
- [ ] Contracts, schemas, policy, fixtures, validators, source records, data, evidence, and release authority remain separate.
- [ ] Any connector or schema-home conflict is resolved or visibly tracked.
- [ ] Owners and CODEOWNERS are assigned.

### Executable coverage

- [ ] At least one substantive test module exists.
- [ ] The lane has positive and negative cases.
- [ ] Valid, invalid, denied, abstained, quarantined, and error behaviors are covered where applicable.
- [ ] Correction/supersession/rollback cases are covered for release-facing behavior.
- [ ] The default suite is no-network and deterministic.
- [ ] A separate live-test lane, if any, is explicitly authorized and isolated.

### Contract and fixture closure

- [ ] Canonical semantic contract is identified.
- [ ] Canonical machine schema is identified.
- [ ] Fixture manifest and identity rules are accepted.
- [ ] Reusable fixture payloads exist and are linked to consumers.
- [ ] Calculation, band, QA/mask, spatial, temporal, and uncertainty profiles are versioned.
- [ ] Reason-code vocabulary is accepted.

### Governance closure

- [ ] Source role cannot upgrade during promotion.
- [ ] Public exact field/operator exposure is denied by default.
- [ ] Evidence resolution and citation tests exist.
- [ ] Policy and release prerequisites are tested separately.
- [ ] Passing tests cannot publish or promote.
- [ ] Correction, withdrawal, and rollback references are testable.

### CI and receipts

- [ ] CI explicitly collects this lane.
- [ ] CI does more than echo TODO.
- [ ] Required categories cannot be silently skipped.
- [ ] Results are tied to commit and fixture/profile versions.
- [ ] Generated-receipt or operation-journal requirements are met.
- [ ] Branch-protection significance is verified before claiming promotion blocking.

Until then, the safe status remains **README-only / implementation not established**.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `VI-TEST-OQ-01` | What canonical Agriculture object family represents a vegetation-index candidate or derivative? | NEEDS VERIFICATION | Accepted contract/schema/registry evidence. |
| `VI-TEST-OQ-02` | Which schema path and `$id` govern the candidate and output shapes? | NEEDS VERIFICATION | Accepted ADR/registry plus schema files and tests. |
| `VI-TEST-OQ-03` | Which calculation profiles and tolerances are accepted? | NEEDS VERIFICATION | Scientific/domain review, versioned contract, implementation tests. |
| `VI-TEST-OQ-04` | Which band and QA/mask profiles are canonical for each source/product? | NEEDS VERIFICATION | Source descriptors, connector contracts, fixture profiles. |
| `VI-TEST-OQ-05` | Which spatial and temporal support fields are mandatory? | NEEDS VERIFICATION | Contract/schema and public-use policy. |
| `VI-TEST-OQ-06` | What is the accepted source-role vocabulary binding for vegetation indices? | NEEDS VERIFICATION | Source authority register and policy tests. |
| `VI-TEST-OQ-07` | Is `fixtures/domains/agriculture/hls_vi/` the canonical reusable fixture home or a provisional lane? | NEEDS VERIFICATION | Fixture parent contract, consumers, migration decision. |
| `VI-TEST-OQ-08` | Which connector path is canonical: flat `connectors/nasa-hls/` or nested `connectors/nasa/hls/`? | CONFLICTED / NEEDS VERIFICATION | ADR or migration record. |
| `VI-TEST-OQ-09` | Which executable validator owns vegetation-index checks? | NEEDS VERIFICATION | Tool inventory, registry, tests, command evidence. |
| `VI-TEST-OQ-10` | Which policy rules enforce field/operator/public aggregation posture? | NEEDS VERIFICATION | Executable policy, tests, runtime binding. |
| `VI-TEST-OQ-11` | Which reason-code registry and namespaces should these tests use? | NEEDS VERIFICATION | Accepted contract/schema/registry. |
| `VI-TEST-OQ-12` | Which EvidenceBundle and citation fields are required? | NEEDS VERIFICATION | Evidence contracts, resolver tests, API projection. |
| `VI-TEST-OQ-13` | Which catalog/layer/release objects consume vegetation-index outputs? | UNKNOWN | Current consumers, manifests, release records. |
| `VI-TEST-OQ-14` | Does any live test exist under a different name or external harness? | UNKNOWN | Recursive tree, workflow, external test inventory. |
| `VI-TEST-OQ-15` | What current tests pass, fail, skip, or xfail? | UNKNOWN | Executable lane and CI logs. |
| `VI-TEST-OQ-16` | Does branch protection require Agriculture checks? | UNKNOWN | Repository rules and protection evidence. |
| `VI-TEST-OQ-17` | Who owns scientific, source, sensitivity, and release review? | NEEDS VERIFICATION | CODEOWNERS/steward registry. |
| `VI-TEST-OQ-18` | How do correction and withdrawal cascade to public derivatives and AI summaries? | NEEDS VERIFICATION | Correction contracts, dependency graph, rollback drill. |
| `VI-TEST-OQ-19` | Which source rights permit fixture derivation and redistribution? | NEEDS VERIFICATION | Source terms/rights decision and fixture provenance. |
| `VI-TEST-OQ-20` | When may a public aggregate be sufficiently coarse and non-identifying? | NEEDS VERIFICATION | Policy thresholds, review record, aggregation tests. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Prior target README, blob `9619829…` | CONFIRMED | Existing purpose, authority split, negative cases, no-network and fail-closed intent. | Short summary; no implementation proof. |
| `tests/README.md` | CONFIRMED repository document | Canonical enforceability root, fixture separation, no live sensitive data, trust-spine expectations. | Executable depth and CI remain unverified. |
| `tests/domains/agriculture/README.md` | CONFIRMED repository document | Agriculture parent test boundary and `veg_index/` child listing. | Says child implementation NEEDS VERIFICATION. |
| `docs/doctrine/directory-rules.md` | CONFIRMED doctrine | Responsibility-root placement and domain-as-segment rule. | Does not prove executable content. |
| ADR-0001 schema-home | CONFIRMED repository ADR / status proposed | Proposed canonical machine-shape home and separation from contracts/policy/fixtures. | Does not define vegetation-index fields. |
| Drift register | CONFIRMED repository register | Existing drift process and absence of a surfaced target-specific resolution. | Register may be incomplete or later superseded. |
| Agriculture `DOMAIN.md` | CONFIRMED repository document | Aggregate default, field-level fail-closed, bounded-context and cross-lane humility. | Domain doctrine, not test implementation. |
| Agriculture sublane README | CONFIRMED repository document | Vegetation index as modeled topical context; mask/time metadata; anti-collapse and aggregate safety. | “Sublane” is docs-side proposed vocabulary. |
| Agriculture × Atmosphere stress reference | CONFIRMED repository document | Agriculture owns interpretation; Atmosphere owns observations; KFM is not alert authority. | Cross-lane reference, not executable contract. |
| Agriculture policy README | CONFIRMED draft repository document | Fail-closed field/operator exposure and finite policy outcomes. | Runtime enforcement unknown. |
| HLS-VI fixture README | CONFIRMED repository document | Synthetic, compact, no-network fixture intent and valid/invalid pattern. | No confirmed payload, schema, validator, or consumer. |
| NASA HLS connector README | CONFIRMED repository document | Derived-context boundary, QA preservation, connector/path conflicts, documentation-only maturity. | No active connector or source activation proof. |
| Agriculture validator README | CONFIRMED repository document | Broad validation obligations and no executable established. | Validator topology remains conflicted. |
| Agriculture workflow | CONFIRMED YAML scaffold | PR trigger and job names. | Jobs only echo TODO; no substantive proof. |
| Makefile | CONFIRMED repository file | Current pytest convention and default test scope. | Default target excludes this lane. |
| Named-path probes | CONFIRMED responses | Representative direct test and fixture files were absent at checked paths. | Differently named/unindexed/generated/external files remain UNKNOWN. |
| Open-PR search | CONFIRMED bounded query | No open target PR matched preflight queries. | Search may not capture every semantically related PR. |

### Source conversion and external research

No PDF conversion, OCR, or external web research was required for this README. Version-sensitive NASA product facts are intentionally excluded; this test boundary relies on repository doctrine and current repository evidence only.

[Back to top](#top)

---

## Changelog, correction, and rollback

### v0.2 — 2026-07-16

- Replaced the short lane summary with a repository-grounded Tests README profile.
- Preserved the prior purpose, authority boundary, negative cases, no-network posture, and open verification items.
- Added bounded current-state evidence and explicit README-only maturity.
- Added fixture routing, source-role, identity, calculation, QA-mask, spatial, temporal, evidence, policy, release, correction, and rollback test obligations.
- Added valid, invalid, denied, abstained, held, quarantined, error, corrected, withdrawn, and rollback case classes.
- Added deterministic command guidance grounded in the current pytest/Makefile convention without claiming execution.
- Added failure interpretation, what-green-does-not-prove, CI limits, sensitivity rules, maintenance, definition of done, and evidence ledger.
- Recorded the NASA HLS connector-path conflict and TODO-only workflow status without resolving them by assertion.

### No-loss assessment

The prior README's substantive material is retained and expanded:

| Prior material | v0.2 location |
|---|---|
| Purpose: governed context, not field truth/release approval | Purpose; Scope; Invariants |
| Evidence basis and responsibility-root split | Authority; Current evidence; Evidence ledger |
| Source-role and derivation preservation | Vegetation-index invariants; Required cases |
| Transform, evidence, citation, receipt, policy, release checks | Inputs; Validation layers; CI/promotion |
| Uncertainty, scale, time, product identity | Invariants; Fixture families |
| Negative cases and fail-safe outcomes | Required case matrix; Reason codes |
| Belongs/does not belong | Scope and non-scope |
| No live source calls | No-network/live separation |
| Validation and open questions | Commands; Open verification register |

No strong existing material was intentionally removed.

### Rollback

This change is documentation-only and reversible.

To restore the prior README exactly:

```bash
git checkout 0165bbf59e9c7ce85148ff254ba723ef8c116a79 -- tests/domains/agriculture/veg_index/README.md
```

When reverting the AI-authored change, also remove or supersede the paired generated receipt for this revision according to repository receipt-retention policy. Do not treat rollback as a source, policy, release, or publication decision.

### Correction path

If this README overstates current implementation, misroutes authority, or uses an unaccepted term:

1. file the discrepancy against the affected document or drift register;
2. narrow the claim to CONFIRMED evidence;
3. update the README version and changelog;
4. supersede the generated receipt rather than silently mutating provenance;
5. keep the prior revision reachable through Git history;
6. re-run remote read-back and link/structure validation.

[Back to top](#top)
