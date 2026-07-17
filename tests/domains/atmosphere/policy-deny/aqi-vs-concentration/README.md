<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/policy-deny/aqi-vs-concentration/readme
title: tests/domains/atmosphere/policy-deny/aqi-vs-concentration/ — AQI-as-Concentration Denial Test Boundary
type: readme; directory-readme; domain-test-lane; atmosphere; policy-deny; AQI; concentration; anti-collapse; non-authoritative
version: v0.2
status: draft; repository-grounded; direct-lane-readme-only; adjacent-parent-placeholder-test-confirmed; executable-policy-test-not-established; single-rego-scaffold-confirmed; hyphenated-planning-path-not-found; policy-input-contract-unknown; canonical-observation-contracts-confirmed; lowercase-compatibility-pointers-confirmed; paired-schemas-permissive-scaffolds; invalid-fixture-metadata-only; airnow-source-profile-draft; validator-not-established; workflow-todo-only; make-test-excludes-lane; fail-closed; cite-or-abstain; not-health-or-alert-authority
owners: OWNER_TBD — Atmosphere steward · Air-quality steward · AQI/report steward · PM2.5 steward · Ozone steward · Policy steward · Test/QA steward · Contract steward · Schema steward · Fixture steward · Source steward · Evidence steward · Validator steward · API/UI/AI steward · Release steward · Security reviewer · CI steward · Docs steward
created: 2026-07-05
updated: 2026-07-16
supersedes: v0.1 Atmosphere Policy-Deny Test Lane — AQI vs Concentration README
policy_label: "public-review; tests; atmosphere; policy-deny; AQI-not-concentration; anti-collapse; public-aqi-report-aware; pollutant-aware; units-aware; averaging-aware; source-role-aware; knowledge-character-aware; evidence-aware; no-network; deny-by-default; correction-aware; rollback-aware; no-policy-authority; no-evidence-authority; no-release-authority; not-health-authority; not-alert-authority"
current_path: tests/domains/atmosphere/policy-deny/aqi-vs-concentration/README.md
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; Directory Rules tests responsibility-root placement;
  tests root and Atmosphere policy-deny parent; Atmosphere policy doctrine stating AQI is not
  concentration; one default-deny Rego scaffold at aqi_is_not_concentration.rego; planned hyphenated
  aqi-not-concentration.rego path not found at the checked location; canonical AirObservation,
  PM25Observation, and OzoneObservation semantic contracts; lowercase PM25/Ozone compatibility
  pointers routing to canonical CamelCase contracts; paired AirObservation, PM25Observation, and
  OzoneObservation schemas with empty properties and additionalProperties true; metadata-only invalid
  AirObservation fixture placeholder; parent-level test_aqi_as_concentration_denied.py containing only
  a one-line PROPOSED placeholder docstring; named-path probes finding no direct conftest.py or child
  test module; EPA AirNow source profile draft separating PUBLIC_AQI_REPORT from provisional raw
  pollutant readings and regulatory AQS posture; TODO-only domain-atmosphere workflow; root Makefile
  test target excluding this lane / PROPOSED focused negative-path tests, policy input adapter, stable
  decision envelope, reason-code vocabulary, real synthetic fixtures, case manifest, pollutant and
  units assertions, averaging/standard/version preservation, AirNow/AQS anti-collapse tests,
  UI/API/map/search/AI carrier assertions, nonempty collection, CI artifacts, correction, rollback,
  and promotion significance / CONFLICTED or drift-prone underscored live Rego path versus hyphenated
  planning path, docs-proposed test location versus current parent-level placeholder, lowercase
  compatibility paths versus canonical CamelCase contracts, and whether a dedicated AQI report object
  family exists or AQI remains role-dependent within pollutant-specific observation contracts /
  UNKNOWN exhaustive recursive inventory, generated or ignored tests, active policy engine binding,
  actual validator, accepted policy input shape, accepted AQI standard/version registry, collected
  case count, pass rate, coverage, mutation score, flake rate, release dependency, production
  consumers, and operational correction behavior / NEEDS VERIFICATION accepted owners, CODEOWNERS,
  canonical Rego file/package, policy adapter, schema closure, fixture payloads and digests,
  reason-code registry, substantive tests, CI retention, required-check status, AQI object-family
  decision, correction cascade, and rollback rehearsal
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b22a43297c76248c174e15bfd6d5b2c75c563e92
  prior_blob: 75f2cd07f4ac833f005d9741e3b5aebd58b1fde5
  direct_lane_files_confirmed:
    - tests/domains/atmosphere/policy-deny/aqi-vs-concentration/README.md
  adjacent_test:
    path: tests/domains/atmosphere/test_aqi_as_concentration_denied.py
    blob: 325a693178e4a02f5cd8f5d52ba84f6343b451d8
    status: one-line PROPOSED placeholder docstring
  checked_absent_paths:
    - tests/domains/atmosphere/policy-deny/aqi-vs-concentration/conftest.py
    - tests/domains/atmosphere/policy-deny/aqi-vs-concentration/test_aqi_vs_concentration.py
    - tests/domains/atmosphere/policy-deny/aqi-vs-concentration/test_aqi_as_concentration_denied.py
    - tests/domains/atmosphere/policy-deny/test_aqi_vs_concentration.py
    - tests/domains/atmosphere/test_aqi_not_concentration.py
    - policy/domains/atmosphere/aqi-not-concentration.rego
  related_repository_blobs:
    tests_root: 2c03b844ab8007453e091c3b24160a209e5214ff
    policy_deny_parent: 4ed619ce5d9d68c24b8bf515adf1aee68869caf1
    atmosphere_policy_doctrine: 53480f8a9e7db4d863ed15cc96c708f0e8d40ef4
    knowledge_character_contract: d38eb867122f5c36d1d8e004b99d856f3ef1f200
    rego_underscored: 4b93dcdde70bca334f5c541d4d847a32869b31bf
    adjacent_test_placeholder: 325a693178e4a02f5cd8f5d52ba84f6343b451d8
    air_observation_contract: d2c1c36cb9c68584ded1bbe9a827d352b3e42311
    pm25_contract: dabc318f6dcf4267858cb4953c3379ac2a60879d
    ozone_contract: d1d6acd09aa9859359539e0715df84f881180913
    pm25_compat_pointer: f4fdad90db504010210bf428590caedc8451f207
    ozone_compat_pointer: 0921d58e5d023eca5e3c36fb648cc0f7da52edb8
    air_observation_schema: 31e70d688dcc536f250eb17f37c2330e5f42f252
    pm25_schema: 4b04e1fc128f56345f4ab180c84c10f98a78e921
    ozone_schema: a630dad554d3fba4d5252983633e81850579d8b7
    invalid_fixture_placeholder: ad05872267df38f4e666565bec353e580b40b683
    airnow_source_profile: 9462a6c5896b1cedd1af2620a1b877153c031c38
    atmosphere_workflow: a3c6a21db798b02202c87f76bfba5f45c5f08c9b
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  related_change_state:
    no_network_rollback_pr: "1338 merged before this snapshot"
    aod_vs_pm25_sibling_pr: "1341 merged before this snapshot"
  bounded_inventory_note: >
    Direct reads, named-path probes, indexed search, and PR metadata establish only the checked
    snapshot. They do not prove permanent absence from history, forks, ignored files, generated
    workspaces, dynamic test generation, Git LFS, external policy stores, differently named paths,
    package-local policy adapters, or later commits.
related:
  - ../README.md
  - ../../README.md
  - ../../test_aqi_as_concentration_denied.py
  - ../../../README.md
  - ../../../../README.md
  - ../../aod-vs-pm25/README.md
  - ../../../../../docs/doctrine/directory-rules.md
  - ../../../../../docs/domains/atmosphere/POLICY.md
  - ../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../../../contracts/domains/atmosphere/knowledge_character.md
  - ../../../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../../../contracts/domains/atmosphere/OzoneObservation.md
  - ../../../../../contracts/domains/atmosphere/pm25-observation.md
  - ../../../../../contracts/domains/atmosphere/ozone-observation.md
  - ../../../../../schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json
  - ../../../../../schemas/contracts/v1/domains/atmosphere/PM25Observation.schema.json
  - ../../../../../schemas/contracts/v1/domains/atmosphere/OzoneObservation.schema.json
  - ../../../../../policy/domains/atmosphere/aqi_is_not_concentration.rego
  - ../../../../../fixtures/domains/atmosphere/objects/AirObservation.invalid.aqi_as_concentration.json
  - ../../../../../docs/sources/catalog/epa/airnow-api.md
  - ../../../../../tools/validators/domains/atmosphere/README.md
  - ../../../../../data/proofs/
  - ../../../../../release/
  - ../../../../../.github/workflows/domain-atmosphere.yml
  - ../../../../../Makefile
  - ../../../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, tests, atmosphere, policy-deny, AQI, concentration, public-aqi-report, observed-sensor, PM2.5, ozone, AirNow, AQS, anti-collapse, evidence, units, averaging, no-network, correction, rollback]
notes:
  - "This revision changes only this README; a generated provenance receipt is paired separately."
  - "AQI/report context and pollutant concentration are role- and meaning-distinct even when one source payload carries both."
  - "The default-deny Rego scaffold does not prove executable AQI-versus-concentration policy behavior."
  - "No test code, policy bundle, fixture payload, schema, contract, validator, workflow, lifecycle object, release object, health guidance, alert, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AQI-as-Concentration Denial Test Boundary

`tests/domains/atmosphere/policy-deny/aqi-vs-concentration/`

> **Purpose.** Define the focused negative-test boundary that proves an AQI value, category, color, public report, NowCast, layer, summary, or generated statement cannot be presented as a governed pollutant concentration merely by renaming fields, adding units, changing labels, or dropping source-role and evidence context.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Inventory: README only" src="https://img.shields.io/badge/inventory-README__only-lightgrey">
  <img alt="Adjacent test: placeholder" src="https://img.shields.io/badge/adjacent__test-placeholder-orange">
  <img alt="Policy: scaffold" src="https://img.shields.io/badge/policy-default--deny__scaffold-orange">
  <img alt="Rule: AQI is not concentration" src="https://img.shields.io/badge/rule-AQI%20%E2%89%A0%20concentration-critical">
  <img alt="Authority: tests only" src="https://img.shields.io/badge/authority-tests__only-purple">
</p>

> [!IMPORTANT]
> **The denial concerns meaning, source role, pollutant identity, units, averaging, standard version, and evidence—not only numeric range.** AQI is an index/report posture. A pollutant concentration is an observation, archive value, model value, or governed derivative with explicit pollutant, units, method, time, and provenance. A number alone cannot establish which one it is.

> [!CAUTION]
> **Current executable enforcement is not established.** The checked child lane contains this README only. The adjacent parent-level test is a one-line `PROPOSED` placeholder. The Rego file contains only a package declaration and `default allow := false`; the observation schemas accept arbitrary properties; and the named invalid fixture contains metadata rather than an AQI or concentration object.

> [!WARNING]
> **KFM is not the official AQI, health, medical, emergency, or protective-action authority.** This lane can prove that unsupported AQI-to-concentration claims are denied or abstained. It cannot establish exposure, health effects, regulatory exceedance, protective action, or official warnings.

**Quick links:** [Purpose](#purpose-and-scope) · [Status](#current-evidence-and-maturity) · [Authority](#authority-and-directory-rules-basis) · [Rule](#governing-rule) · [Objects](#object-source-role-and-knowledge-character-boundaries) · [Source posture](#airnow-aqs-and-source-reporting-posture) · [Policy](#policy-file-and-naming-drift) · [Concentration](#governed-concentration-boundary) · [Matrix](#required-test-matrix) · [Fixtures](#fixture-and-case-contract) · [Surfaces](#public-and-derived-surface-tests) · [Outcomes](#finite-outcomes-and-reason-code-posture) · [Evidence](#evidence-policy-release-and-correction-boundary) · [Security](#no-network-sensitivity-and-safe-diagnostics) · [Commands](#inventory-collection-and-execution) · [Failures](#failure-interpretation) · [CI](#ci-and-promotion-boundary) · [Plan](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Ledger](#evidence-ledger) · [Rollback](#changelog-correction-and-rollback)

---

## Purpose and scope

This lane exists to prove one Atmosphere anti-collapse invariant:

```text
PUBLIC_AQI_REPORT / AQI index or category
    is not
OBSERVED_SENSOR / pollutant concentration
```

The durable question is:

> Can every ingest, transform, catalog, graph, map, API, export, search, AI, and release path preserve the distinction between AQI reporting context and pollutant concentration—and fail closed when that distinction is missing, contradicted, or overstated?

A mature suite should prove that:

1. an AQI value cannot acquire concentration meaning by field, slug, title, legend, route, unit, or tooltip changes;
2. a category, color, descriptor, or overall AQI cannot be emitted as a PM2.5, ozone, or generic concentration;
3. `PUBLIC_AQI_REPORT` cannot be silently re-characterized as `OBSERVED_SENSOR`, `REGULATORY_ARCHIVE`, or uncaveated concentration;
4. concentration objects retain pollutant identity, units, method, averaging or temporal basis, station or spatial context, QA, source role, and evidence;
5. a source payload carrying both AQI and raw pollutant values preserves those as distinct fields or governed objects;
6. AirNow AQI/report posture does not become AQS regulatory posture merely because both are EPA-related;
7. an attempted inverse AQI-to-concentration derivation fails closed unless a separately governed method, standard/version, pollutant, rounding rule, applicability boundary, uncertainty, and review record make the claim admissible;
8. UI, map, API, export, search, graph, vector-index, and AI carriers preserve whether a value is AQI, category, concentration, or other context;
9. missing policy, ambiguous policy path, missing fixture payload, unresolved evidence, unknown units, or unknown pollutant fails visibly;
10. default tests are deterministic, local, public-safe, and no-network;
11. a green result remains bounded enforcement evidence, not source admission, scientific validation, regulatory determination, health guidance, policy approval, or release approval.

This lane does not define AQI science, pollutant science, breakpoint tables, concentration standards, object contracts, schemas, policy bundles, conversion algorithms, source authority, EvidenceBundles, release decisions, or public products.

[Back to top](#top)

---

## Current evidence and maturity

### Safe conclusion

KFM has strong semantic documentation for the AQI-versus-concentration distinction, but focused executable enforcement is not established in the checked lane.

| Surface | Inspected status | Safe conclusion |
|---|---|---|
| This child lane | **README-only** | Focused intent exists; direct executable coverage is not established. |
| Adjacent parent-level test | **One-line `PROPOSED` placeholder** | A filename exists, not a substantive test. |
| `aqi_is_not_concentration.rego` | **Default-deny scaffold** | Package/default posture exists; no AQI-specific rule was established. |
| Hyphenated planning path | **Not found at checked path** | Planning/live naming drift remains visible. |
| `AirObservation.md` | **Expanded draft semantic contract** | General observed-sensor meaning exists; it is not an AQI report. |
| `PM25Observation.md` | **Expanded draft semantic contract** | PM2.5 may carry observed or public-report posture according to source role. |
| `OzoneObservation.md` | **Expanded draft semantic contract** | Ozone may carry observed or public-report posture according to source role. |
| Lowercase PM2.5/Ozone files | **Compatibility pointers** | They must not become parallel semantic authority. |
| Observation schemas | **Permissive scaffolds** | Shape validation does not enforce AQI/concentration meaning. |
| Invalid fixture | **Metadata-only placeholder** | No executable invalid object or expected decision is established. |
| AirNow source profile | **Draft documentation** | It distinguishes AQI aggregate/report from provisional raw pollutant values and AQS. |
| Atmosphere workflow | **TODO-only** | Green execution cannot prove the denial. |
| Root `make test` | **Excludes this lane** | It runs schema and contract test directories only. |

### Truth labels

| Label | Meaning here |
|---|---|
| `CONFIRMED` | Verified from current repository files, commit-pinned readback, or PR metadata. |
| `PROPOSED` | Recommended policy, fixture, test, reason code, command, or CI control not established as implementation. |
| `UNKNOWN` | Not resolved by the inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not verified strongly enough to rely on. |
| `CONFLICTED` | Current files, plans, or authority surfaces disagree or overlap materially. |

### Maturity ladder

| Level | Meaning | Current status |
|---:|---|---|
| L0 | No documentation or test lane | Passed. |
| L1 | README states the intended distinction | **CONFIRMED.** |
| L2 | Canonical semantic contracts distinguish report and concentration roles | **CONFIRMED, draft.** |
| L3 | One canonical policy path/package and accepted policy input contract | **PROPOSED / NEEDS VERIFICATION.** |
| L4 | Real synthetic fixtures with expected outcomes and digests | **Not established.** |
| L5 | Substantive negative and positive-control tests | **Not established.** |
| L6 | Public carriers preserve AQI/concentration trust state | **Not established.** |
| L7 | Nonzero collection and retained safe QA artifact | **Not established.** |
| L8 | Required CI check and promotion dependency | **Not established.** |
| L9 | Correction, withdrawal, supersession, and rollback cascade tested | **Not established.** |
| L10 | Operational metrics, ownership, and periodic adversarial review | **Not established.** |

The safe current statement is **L2 documentation maturity with L1 test-lane implementation**.

[Back to top](#top)

---

## Authority and Directory Rules basis

Directory Rules place enforceability proof under `tests/` and preserve separate authority roots for meaning, shape, policy, evidence, lifecycle, and release.

```text
tests/
└── domains/
    └── atmosphere/
        └── policy-deny/
            └── aqi-vs-concentration/
                └── README.md
```

### Responsibility split

| Concern | Owning surface | This lane's role |
|---|---|---|
| Human policy doctrine | `docs/domains/atmosphere/POLICY.md` | Test the documented anti-collapse intent once executable bindings exist. |
| Knowledge-character meaning | `contracts/domains/atmosphere/knowledge_character.md` and canonical docs | Assert that report and observation characters are preserved. |
| Observation meaning | Canonical CamelCase contracts | Consume object meaning; never redefine it locally. |
| Machine shape | `schemas/contracts/v1/domains/atmosphere/` | Exercise schema behavior; never become schema authority. |
| Enforceable policy | `policy/domains/atmosphere/` | Invoke the accepted policy package; never copy rules into test code as policy authority. |
| Reusable fixtures | `fixtures/domains/atmosphere/` | Consume governed synthetic fixtures. |
| Validator implementation | `tools/validators/` or accepted package home | Call validators and assert decisions. |
| Source identity/role | Source registry and source descriptors | Verify required role and authority references. |
| Evidence | `EvidenceRef → EvidenceBundle` and proof roots | Require resolution or abstention. |
| Lifecycle data | `data/raw` through `data/published` | Assert no invalid promotion or write. |
| Release/correction/rollback | `release/` and correction object families | Verify gates and references; never approve release. |
| Public carriers | Governed API/UI/map/export/search/AI roots | Verify semantic preservation downstream. |

> [!CAUTION]
> This README is not a policy bundle, scientific standard, schema, validator, fixture payload, EvidenceBundle, source admission, regulatory determination, health message, or release record.

### No parallel authority

Tests may consume canonical contracts, schemas, policy, fixtures, source records, evidence, and release objects, but must not duplicate or replace them. Lowercase compatibility pointers, source documentation, fixture samples, and green checks remain non-authoritative.

[Back to top](#top)

---

## Governing rule

### Core invariant

```text
AQI/report/index/category/color
    MUST NOT be presented as
pollutant concentration
```

unless a separate governed concentration object exists and independently satisfies its semantic, shape, source-role, units, evidence, policy, review, correction, and release requirements.

### Deny conditions

Deny, abstain, or fail validation when:

- an AQI value is labeled as PM2.5, ozone, or generic concentration;
- a category or color band is assigned concentration units;
- an overall AQI is treated as a pollutant-specific concentration;
- a pollutant-specific AQI is treated as raw concentration without a separately admitted concentration field/object;
- a `PUBLIC_AQI_REPORT` is relabeled `OBSERVED_SENSOR`;
- an AirNow AQI record is presented as AQS regulatory archive evidence;
- an API field, map property, legend, tooltip, export column, graph edge, search field, embedding label, or AI sentence silently substitutes AQI for concentration;
- pollutant identity is missing;
- concentration units are missing, incompatible, or copied from a display label;
- averaging or temporal basis is missing where material;
- the applicable AQI standard, table, version, jurisdiction, or source method is unknown where a derivation is attempted;
- rounding, truncation, category-only input, or overall-index aggregation makes inversion ambiguous;
- source role, evidence, rights, freshness, review state, or release state is unresolved;
- the policy package, fixture, validator, or reason-code contract is missing or ambiguous.

### Allowed contextual use

AQI may be surfaced as:

- an agency/public report;
- an index value;
- a category or color band;
- a near-real-time situational-awareness layer;
- a pollutant-specific sub-index when clearly labeled;
- an overall AQI summary when clearly labeled;
- a contextual citation to an official source;
- a historical report or archived reporting product when its time and authority are explicit.

It remains AQI/report context. It does not become concentration by presentation.

[Back to top](#top)

---

## Object, source-role, and knowledge-character boundaries

### Knowledge characters

| Knowledge character | Meaning in this boundary | Prohibited collapse |
|---|---|---|
| `PUBLIC_AQI_REPORT` | Agency-published AQI/index/report posture | Must not become raw concentration or observed sensor value. |
| `OBSERVED_SENSOR` | Direct instrument-derived observation posture | Must not be inferred from AQI alone. |
| `REGULATORY_ARCHIVE` | Reviewed/archive posture | Must not be inferred from near-real-time AQI/report context. |
| `LOW_COST_SENSOR` | Caveated sensor posture | Must not become reference-grade concentration without required correction and limitations. |
| `ATMOSPHERIC_MODEL_FIELD` | Modeled field | Must not be represented as measured concentration or AQI report without separate derivation. |
| `DERIVED_FUSION` | Governed multi-source derivative | Must not impersonate a source observation or report. |

### Canonical concentration-bearing contracts

| Contract | Canonical meaning | AQI boundary |
|---|---|---|
| `AirObservation.md` | General governed air-quality observation | Explicitly not an AQI report. |
| `PM25Observation.md` | PM2.5-specific record; role-dependent observed/report/low-cost/archive posture | AQI/report values must remain report/index values, not raw concentration. |
| `OzoneObservation.md` | Ozone-specific record; role-dependent observed/report/archive posture | Ozone AQI is not ozone concentration. |

### Compatibility pointers

The lowercase files:

```text
contracts/domains/atmosphere/pm25-observation.md
contracts/domains/atmosphere/ozone-observation.md
```

are compatibility pointers to the CamelCase canonical contracts. Tests and validators should resolve authoritative object meaning through:

```text
contracts/domains/atmosphere/PM25Observation.md
contracts/domains/atmosphere/OzoneObservation.md
```

unless an accepted ADR migrates the canonical paths.

### Object identity rule

A record must not change identity class merely because a transform changes:

- field name;
- JSON key;
- display title;
- layer slug;
- route name;
- legend;
- tooltip;
- export header;
- graph predicate;
- search alias;
- vector metadata;
- generated sentence;
- unit text.

Where meaning changes materially, use a new governed object or correction/re-identity path.

[Back to top](#top)

---

## AirNow, AQS, and source-reporting posture

The current AirNow documentation distinguishes multiple values and roles that may coexist in one source family.

| Source/value posture | Documented role | Required preservation |
|---|---|---|
| AirNow AQI/index/category | Aggregate/context and `PUBLIC_AQI_REPORT` | Label as AQI/report, preserve issuer, time, freshness, and preliminary posture. |
| AirNow raw pollutant value | Provisional observed value | Preserve pollutant, units, station/context, observed time, provisional QA, and evidence separately from AQI. |
| AQS/AirData archive | Regulatory/archive posture | Do not infer from AirNow; preserve later review/revision and supersession relationships. |
| Advisory/context carrier | Referral/context only | Do not convert to KFM life-safety instruction. |

### Required source tests

A mature suite should prove that:

- one source payload may carry distinct AQI and concentration fields without collapse;
- preliminary AirNow values do not become AQS regulatory/archive evidence;
- issuer, pollutant, units, report/observed time, freshness, and source role remain explicit;
- later corrections or AQS revisions preserve supersession rather than rewriting provenance;
- overall AQI, pollutant-specific AQI, category, color, and concentration remain distinguishable.

An overall AQI cannot identify a unique pollutant concentration without additional governed context.

[Back to top](#top)

---

## Policy file and naming drift

### Confirmed current policy file

```text
policy/domains/atmosphere/aqi_is_not_concentration.rego
package kfm.generated.policy.domains.atmosphere.aqi_is_not_concentration
default allow := false
```

This proves only:

- the path exists;
- a package name exists;
- the scaffold defaults to deny.

It does not prove:

- accepted input shape;
- AQI detection;
- concentration detection;
- pollutant or units validation;
- source-role checks;
- reason codes;
- positive controls;
- policy adapter wiring;
- OPA invocation in CI;
- public-carrier enforcement.

### Planning-name drift

The prior README and planning documents refer to:

```text
policy/domains/atmosphere/aqi-not-concentration.rego
```

That path was not found at the checked location. The live underscored path and planning hyphenated path must not be treated as equivalent implicitly.

### Required canonicalization decision

Before executable tests bind to policy:

1. select one canonical file path;
2. select one canonical Rego package;
3. define an accepted input contract;
4. define an accepted result envelope;
5. define stable reason codes;
6. define compatibility/migration handling for stale path references;
7. update docs, tests, workflows, adapters, fixture manifests, and registries together;
8. add a test proving only the canonical package is loaded;
9. add a test proving missing or duplicate policy selection fails setup;
10. record the decision in an ADR or drift/migration record when required.

### Positive-control requirement

A default-deny policy can appear safe while denying every input. The substantive suite must include:

- negative AQI-as-concentration cases;
- valid AQI/report cases;
- valid concentration cases;
- valid source payloads carrying both distinct fields;
- setup failure when policy is missing;
- setup failure when multiple packages match;
- a positive control that proves an admissible concentration can pass;
- a positive control that proves admissible AQI/report context can pass as AQI/report.

[Back to top](#top)

---

## Governed concentration boundary

### Concentration object requirements

A governed concentration record must retain a separate stable identity plus the pollutant, value, units, method, spatial/station context, material time and averaging basis, source role, knowledge character, QA/freshness, evidence, rights/sensitivity state, review/policy state, and correction/release lineage required by its canonical contract.

### Attempted AQI-to-concentration inversion

AQI may be calculated outside KFM from concentration plus pollutant-specific reporting rules. That does not make a reverse calculation automatically admissible.

A reverse or reconstructed concentration claim should fail closed when any material input is missing, including:

- pollutant;
- AQI standard or jurisdiction;
- table/version;
- averaging basis;
- breakpoint range;
- rounding/truncation behavior;
- report vintage;
- source method;
- quality state;
- applicability domain;
- uncertainty;
- evidence;
- review state.

A category or color alone cannot support a concentration claim. An integer AQI may correspond to a range or rounded result rather than a unique source concentration.

### Separate-object rule

When a governed derivation is allowed, the output must:

- receive a separate identity;
- retain the AQI/report input as an input, not mutate it;
- record method and version;
- record assumptions and applicability;
- record uncertainty or range;
- retain the original AQI/report value;
- avoid claiming observed-sensor or regulatory-archive posture unless separately supported;
- carry evidence and review;
- remain correctable and withdrawable;
- pass release gates independently.

This README does not decide whether such inverse derivation should be implemented.

[Back to top](#top)

---

## Required test matrix

### Policy setup and positive controls

| Test | Expected result |
|---|---|
| Canonical package loads once | PASS setup. |
| Policy missing, duplicated, or mismatched | `ERROR`; do not skip. |
| Decision or reason code missing | Fail closed. |
| Default-deny policy rejects valid AQI and valid concentration controls | Test failure; deny-all is not substantive. |
| Valid AQI report remains `PUBLIC_AQI_REPORT` | Conditional allow as report context. |
| Valid PM2.5 or ozone concentration retains pollutant, units, time, source role, QA, and evidence | Conditional allow as concentration. |
| One source payload contains distinct AQI and concentration fields | Allow only when semantics remain separate. |

### Direct collapse cases

| Scenario | Expected result |
|---|---|
| AQI value/category/color placed in concentration field | `DENY`. |
| Overall AQI labeled pollutant-specific concentration | `DENY`. |
| AQI assigned concentration units | `DENY`. |
| `PUBLIC_AQI_REPORT` relabeled `OBSERVED_SENSOR` or `REGULATORY_ARCHIVE` | `DENY`. |
| AQI report changed to PM25/Ozone observation by name or slug | `DENY`. |
| AirNow AQI labeled AQS regulatory measurement | `DENY`. |
| Historical/preliminary report labeled current/final | `RESTRICT`, `HOLD`, or `DENY`. |
| Pollutant, units, method, or required time basis missing | `DENY` or `ABSTAIN`. |

### AQI inversion and derived-output cases

| Scenario | Expected result |
|---|---|
| Category/color converted to exact concentration | `DENY`. |
| Overall AQI converted without pollutant | `DENY`. |
| Standard/version, averaging basis, or rounding behavior missing | `DENY` or `ABSTAIN`. |
| Derived output mutates the source AQI object | `DENY`. |
| Derived output claims observed/archive posture without separate evidence | `DENY`. |
| Method, applicability, uncertainty/range, evidence, or review missing | `DENY` or `ABSTAIN`. |
| Separately identified derivative has accepted method, bounded result, evidence, review, and caveats | Conditional allow as derived output only. |

### Carrier and mutation controls

A passing suite must fail when:

- API/UI/map/export/search/graph/vector/AI surfaces rename AQI as concentration;
- no negative or positive cases are collected;
- every fixture is a placeholder;
- policy is not invoked;
- the test remains only a docstring;
- swapping AQI and concentration labels does not fail;
- policy always allows or always denies without detection.

[Back to top](#top)

---

## Fixture and case contract

The named fixture:

```text
fixtures/domains/atmosphere/objects/AirObservation.invalid.aqi_as_concentration.json
```

contains scaffold metadata only. It is not an invalid AQI or concentration payload and cannot prove policy behavior.

### Required fixture families

- AQI value, category, color, or overall AQI mislabeled as concentration;
- `PUBLIC_AQI_REPORT` mislabeled as observation or archive;
- AirNow AQI mislabeled as AQS;
- concentration missing pollutant, units, method, or time basis;
- inverse derivation missing standard/version, applicability, or uncertainty;
- valid AQI report;
- valid PM2.5 concentration;
- valid ozone concentration;
- valid dual-field payload carrying separate AQI and raw concentration;
- historical/superseded report.

### Proposed case manifest

```yaml
case_id: atmo-aqi-conc-0001
fixture_path: fixtures/domains/atmosphere/policy-deny/aqi-vs-concentration/invalid-aqi-as-pm25.json
fixture_sha256: "<digest>"
policy_package: kfm.generated.policy.domains.atmosphere.aqi_is_not_concentration
expected_outcome: DENY
expected_reason_code: ATMO_AQI_CONC_CHARACTER_COLLAPSE
consumer_test: tests/domains/atmosphere/policy-deny/aqi-vs-concentration/test_aqi_vs_concentration.py
public_safe: true
network_required: false
```

The manifest shape is `PROPOSED`. Fixtures must be synthetic/public-safe, deterministic, local, hashed, consumer-linked, no-network, and never treated as source evidence.

[Back to top](#top)

---

## Public and derived surface tests

| Surface | Required assertion |
|---|---|
| API/envelope | AQI and concentration use distinct fields; concentration retains pollutant/units; unsupported derivation returns `ABSTAIN` or `DENY`; evidence and reason codes remain visible. |
| UI/map | AQI color/category/legend remains AQI; concentration units never appear on AQI-only data; preliminary report is not regulatory determination. |
| Export/search | Column names and aliases preserve meaning; AQI and concentration are not averaged or merged. |
| Graph/vector | Predicates and metadata preserve object family and knowledge character. |
| AI | Generated language cannot infer concentration, exposure, health effect, or regulatory status from AQI alone. |
| Correction | Supersession and withdrawal propagate to every carrier. |

Examples that must fail include “AQI 100 means concentration 100,” AirNow AQI presented as AQS, and any exact concentration answer when only AQI/category evidence is available.

[Back to top](#top)

---

## Finite outcomes and reason-code posture

### Runtime envelope outcomes

```text
ANSWER | ABSTAIN | DENY | ERROR
```

### Policy/review outcomes

```text
ALLOW | RESTRICT | DENY | HOLD | ERROR
```

### Proposed reason codes

| Reason code | Intended meaning |
|---|---|
| `ATMO_AQI_CONC_OBJECT_COLLAPSE` | AQI/report presented as concentration object. |
| `ATMO_AQI_CONC_CHARACTER_COLLAPSE` | Report presented as observation/archive. |
| `ATMO_AQI_CONC_CATEGORY_AS_VALUE` | Category/color used as concentration. |
| `ATMO_AQI_CONC_OVERALL_AS_POLLUTANT` | Overall AQI presented as pollutant concentration. |
| `ATMO_AQI_CONC_POLLUTANT_OR_UNITS_MISSING` | Pollutant or units absent/invalid. |
| `ATMO_AQI_CONC_TIME_BASIS_MISSING` | Required report/observation/averaging basis absent. |
| `ATMO_AQI_CONC_STANDARD_UNKNOWN` | Required standard/version/jurisdiction unknown. |
| `ATMO_AQI_CONC_INVERSION_AMBIGUOUS` | Reverse derivation is unsupported or non-unique. |
| `ATMO_AQI_CONC_AIRNOW_AQS_COLLAPSE` | Preliminary/report posture presented as archive. |
| `ATMO_AQI_CONC_EVIDENCE_MISSING` | Claim lacks resolvable supporting evidence. |
| `ATMO_AQI_CONC_POLICY_SETUP` | Policy missing, ambiguous, or invalid. |
| `ATMO_AQI_CONC_FIXTURE_OR_COLLECTION_INVALID` | Placeholder fixture or zero substantive cases. |
| `ATMO_AQI_CONC_CARRIER_OVERCLAIM` | Downstream carrier changed meaning. |
| `ATMO_AQI_CONC_RELEASE_OR_CORRECTION_BLOCKED` | Release/correction action required. |

These codes are `PROPOSED` until accepted in the canonical reason-code registry.

### Outcome selection

| Condition | Preferred outcome |
|---|---|
| AQI mislabeled concentration | `DENY`. |
| User asks for concentration but evidence contains AQI only | `ABSTAIN`. |
| Required policy missing | `ERROR` / setup failure. |
| Rights or review unresolved | `HOLD` or `DENY`. |
| Public-safe transform needed | `RESTRICT`. |
| Valid AQI report | `ALLOW` as AQI/report only. |
| Valid concentration object | `ALLOW` as concentration only. |
| Valid bounded derivative | Conditional `ALLOW` as derived output only. |

[Back to top](#top)

---

## Evidence, policy, release, and correction boundary

### Required order

```text
define claim scope
    → resolve source and object identity
    → preserve AQI/report versus concentration meaning
    → validate pollutant, units, time, method, and source role
    → resolve EvidenceRef to EvidenceBundle
    → apply rights, sensitivity, freshness, and policy
    → review
    → release candidate
    → publish
```

Skipping a step must not silently convert the claim to `ALLOW`.

### Lifecycle

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Lifecycle phase | AQI/concentration rule |
|---|---|
| RAW | Preserve source fields and source semantics; do not normalize AQI into concentration. |
| WORK | Parse AQI and concentration separately; unresolved mappings stay work. |
| QUARANTINE | Place collapsed, ambiguous, rights-unclear, or policy-unclear records here. |
| PROCESSED | Emit governed report and concentration objects/fields with separate meaning. |
| CATALOG/TRIPLET | Preserve object family, character, units, source role, and evidence links. |
| PUBLISHED | Require release, correction, and rollback controls; never publish unsupported conversion. |

### Evidence closure

A test may assert that evidence resolves. It does not create an EvidenceBundle.

Required negative states include:

- missing EvidenceRef;
- unresolved EvidenceRef;
- EvidenceBundle supporting AQI only while claim asserts concentration;
- evidence supporting concentration but carrier displays AQI incorrectly;
- source report cited as scientific conversion method;
- stale or superseded source evidence;
- conflicting AQI and concentration values;
- rights or review gaps.

### Correction and supersession

When an invalid AQI-as-concentration representation is found:

1. stop promotion or public serving where governed controls allow;
2. preserve the prior artifact and audit trail;
3. emit a correction/withdrawal/supersession object through the accepted root;
4. identify affected API, UI, map, export, search, graph, vector, AI, catalog, and release consumers;
5. regenerate derived artifacts;
6. retain the original AQI/report evidence;
7. do not rewrite source history to resemble concentration evidence;
8. validate the corrected representation;
9. record rollback target.

[Back to top](#top)

---

## No-network, sensitivity, and safe diagnostics

### No-network default

Focused tests should not depend on:

- live AirNow endpoints;
- live AQS/AirData endpoints;
- geocoding;
- map tiles/styles/sprites/glyphs;
- cloud storage;
- remote databases;
- message buses;
- external model or AI services;
- package downloads;
- remote schemas;
- developer caches;
- credentials.

The sibling `no-network/` lane owns broad egress-denial enforcement. This lane should consume that enforcement and prove AQI/concentration tests remain hermetic.

### Sensitivity and rights

Although AQI reports are usually public-oriented, tests should still fail closed for:

- private or unpublished sensor feeds;
- exact sensitive station/site details;
- living-person or household associations;
- unresolved source rights;
- sensitive cross-lane joins;
- current official alert text presented as KFM authority;
- health records or exposure inference;
- credentials, tokens, cookies, signed URLs, or private endpoints.

### Safe diagnostics

Failure reports may include:

- case ID;
- synthetic object ID;
- expected/actual outcome;
- reason code;
- fixture path and digest;
- policy package/version;
- contract/schema identifiers;
- safe field names;
- bounded mismatch summary.

Failure reports should not include:

- secrets;
- raw headers;
- private URLs;
- full source payloads;
- sensitive coordinates;
- living-person data;
- current official warning text as KFM instruction;
- internal infrastructure detail not needed for review.

### Canary controls

Use conspicuous synthetic canaries to prove:

- AQI category cannot become concentration;
- AQI integer cannot acquire concentration units;
- AirNow cannot become AQS;
- evidence mismatch is detected;
- secret-like values are rejected;
- public carriers preserve reason codes and trust state.

[Back to top](#top)

---

## Inventory, collection, and execution

### Deterministic inventory

```bash
find tests/domains/atmosphere/policy-deny/aqi-vs-concentration \
  -type f -print | LC_ALL=C sort

find fixtures/domains/atmosphere \
  -type f \( -iname '*aqi*' -o -iname '*concentration*' -o -iname '*pm25*' -o -iname '*ozone*' \) \
  -print | LC_ALL=C sort

git grep -n -E \
  'aqi_is_not_concentration|aqi-not-concentration|test_aqi_as_concentration_denied|AQI.*concentration|PUBLIC_AQI_REPORT'
```

### Placeholder detection

```bash
git grep -n -E \
  'PROPOSED placeholder|Status: PROPOSED scaffold|default allow := false|properties.: \{\}|additionalProperties.: true' \
  -- \
  tests/domains/atmosphere \
  policy/domains/atmosphere \
  fixtures/domains/atmosphere \
  schemas/contracts/v1/domains/atmosphere
```

### Collection

```bash
python -m pytest \
  --collect-only -q \
  tests/domains/atmosphere/policy-deny/aqi-vs-concentration \
  tests/domains/atmosphere/test_aqi_as_concentration_denied.py
```

Collection must fail or alert when the substantive case count is zero.

### Focused execution

```bash
python -m pytest -q \
  tests/domains/atmosphere/policy-deny/aqi-vs-concentration \
  tests/domains/atmosphere/test_aqi_as_concentration_denied.py
```

The current repository evidence does not establish that these paths contain runnable tests.

### Proposed policy execution

```bash
opa test \
  policy/domains/atmosphere \
  tests/domains/atmosphere/policy-deny/aqi-vs-concentration
```

This command is `PROPOSED` until OPA tooling, test layout, package selection, and input contracts are verified.

### Root targets

The current Makefile:

- leaves `make policy` as a TODO echo;
- leaves `make fixtures` as a TODO echo;
- runs `make test` only against `tests/schemas` and `tests/contracts`;
- leaves `make deny-test` as a TODO echo.

Therefore none of those targets currently proves this lane.

[Back to top](#top)

---

## Failure interpretation

| Failure | Correct response |
|---|---|
| Policy missing or ambiguous | `ERROR`; resolve setup rather than skip. |
| Negative case allowed | Block promotion and fix policy/adapter. |
| Valid AQI or concentration positive control denied | Detect deny-all or adapter defect. |
| Placeholder fixture used as coverage | Replace with governed synthetic payload. |
| Pollutant, units, time, or role missing | `DENY` or `ABSTAIN`. |
| AirNow labeled AQS | `DENY`. |
| Unsupported AQI inversion | `ABSTAIN` or `DENY`. |
| Evidence supports AQI only | Do not answer concentration. |
| Carrier changes label/meaning | Fail carrier contract. |
| Zero cases, missing reason code, or unsafe diagnostics | Fail CI and correct the report. |
| Correction cannot identify consumers | Hold release. |

### Passing limits

A passing focused suite would not prove:

- AQI standard correctness;
- scientific validity of any inverse calculation;
- completeness of source coverage;
- AirNow admission;
- AQS regulatory authority;
- exposure or health effect;
- current official AQI;
- policy approval;
- rights approval;
- EvidenceBundle truth;
- release readiness;
- production parity;
- public safety;
- operational rollback success.

[Back to top](#top)

---

## CI and promotion boundary

### Substantive CI requirements

A mature required job should:

1. install pinned test and policy dependencies;
2. run without live network access;
3. verify the canonical policy package;
4. reject duplicate/stale policy packages;
5. validate fixture manifests and digests;
6. fail on placeholder-only fixtures;
7. collect a nonzero minimum of negative and positive cases;
8. run policy setup and adapter tests;
9. run object/character/source-role/units/time tests;
10. run AirNow/AQS anti-collapse tests;
11. run carrier tests;
12. emit a safe structured report;
13. retain the report for review;
14. fail on unexpected allow, deny-all behavior, missing reason codes, or zero cases;
15. expose correction and rollback targets where release significance requires them.

### Current CI boundary

`domain-atmosphere.yml` currently runs TODO echo commands. A successful run is not substantive evidence for this lane.

The root `make test` excludes this path. The root policy and deny targets are TODOs.

### Promotion significance

Policy-deny tests may become a prerequisite for release review, but:

- tests do not approve promotion;
- a green check is not a PolicyDecision;
- a green check is not a ReviewRecord;
- a green check is not a ReleaseManifest;
- a green check is not scientific or regulatory validation;
- missing required artifacts must fail closed rather than be bypassed.

[Back to top](#top)

---

## Maintenance and change discipline

Update this README when:

- the canonical policy path/package is accepted;
- a policy input/result contract is accepted;
- a dedicated AQI report object family is accepted or rejected;
- observation contracts or schemas change;
- AQI standard/version registries are introduced;
- fixtures or manifests are added;
- reason codes are accepted;
- tests move between child and parent lanes;
- public carrier contracts change;
- CI becomes substantive;
- correction or rollback procedures change.

### Breaking changes

A change is breaking when it alters:

- policy package/path;
- accepted input profile;
- reason-code meaning;
- object-family mapping;
- knowledge-character mapping;
- pollutant or units requirements;
- time/averaging requirements;
- AQI standard/version handling;
- fixture IDs/digests;
- expected outcome;
- public carrier fields;
- correction/supersession behavior.

Breaking changes should include migration notes, updated fixtures/tests, compatibility handling, review, and rollback.

## Smallest sound implementation sequence

Prefer this implementation order:

1. freeze one canonical policy path/package;
2. define a minimal policy input/result contract;
3. replace metadata-only fixture with one invalid synthetic AQI-as-concentration case;
4. add one valid AQI positive control;
5. add one valid concentration positive control;
6. implement the focused adapter/test;
7. add stable reason codes;
8. add pollutant/units/time/source-role negative cases;
9. add AirNow/AQS cases;
10. add carrier cases;
11. add nonzero collection and safe report;
12. add substantive CI;
13. add correction/rollback tests.

Each step should be independently reviewable and reversible.

[Back to top](#top)

---

## Definition of done

- [ ] Owners, reviewers, canonical Rego path/package, policy input/result contracts, and reason codes are accepted.
- [ ] AQI object-family/role treatment is documented without creating parallel contract authority.
- [ ] Metadata-only placeholders are replaced by hashed synthetic fixtures with consumers and expected outcomes.
- [ ] Negative cases and positive AQI/concentration controls are substantive and nonzero.
- [ ] Pollutant, units, time, source-role, AirNow/AQS, inversion, carrier, and evidence failures are covered.
- [ ] Tests invoke canonical policy/validator code and run no-network.
- [ ] Safe QA artifacts expose case count, outcomes, and reason codes.
- [ ] CI is substantive and its promotion significance is accepted.
- [ ] Correction, supersession, withdrawal, and rollback paths are tested.
- [ ] A green suite remains necessary but not sufficient for policy, scientific, regulatory, health, or release approval.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| AQI-CONC-001 | Which Rego file/package is canonical? | NEEDS VERIFICATION |
| AQI-CONC-002 | Is a dedicated AQI report object family accepted? | OPEN |
| AQI-CONC-003 | What are the accepted policy input/result and reason-code contracts? | NEEDS VERIFICATION |
| AQI-CONC-004 | Which AQI standards/versions and breakpoint registries are admitted? | OPEN |
| AQI-CONC-005 | Which pollutant units and averaging/time fields are mandatory? | NEEDS VERIFICATION |
| AQI-CONC-006 | Should executable tests live in the child or parent lane? | OPEN |
| AQI-CONC-007 | What validator/policy adapter and fixtures are canonical? | UNKNOWN |
| AQI-CONC-008 | Is AirNow admitted, under what roles, and how are AQS corrections represented? | NEEDS VERIFICATION |
| AQI-CONC-009 | Which public carriers consume these fields? | UNKNOWN |
| AQI-CONC-010 | Is this a required promotion check and who owns rollback rehearsal? | UNKNOWN |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Target README + Directory Rules | CONFIRMED | Existing lane and correct test-root placement. | Not executable proof. |
| Policy doctrine + KnowledgeCharacter contract | CONFIRMED draft | AQI/report is distinct from concentration/observation. | Machine enforcement unverified. |
| `aqi_is_not_concentration.rego` | CONFIRMED scaffold | Path/package/default deny. | No AQI-specific logic. |
| Hyphenated path probe | NOT FOUND at checked path | Naming drift. | Not permanent absence. |
| Parent-level test | CONFIRMED placeholder | Planned test location. | No assertions. |
| Canonical Air/PM2.5/Ozone contracts | CONFIRMED draft | Observation/concentration meaning and role boundaries. | Runtime enforcement unverified. |
| Lowercase pointers | CONFIRMED | Compatibility routing. | Not semantic authority. |
| Three schemas | CONFIRMED permissive scaffolds | Files/pointers exist. | Do not enforce meaning. |
| Invalid fixture | CONFIRMED metadata-only | Planned fixture path. | No payload behavior. |
| AirNow source profile | CONFIRMED draft docs | AQI/report, provisional raw value, and AQS distinction. | No source admission. |
| Workflow + Makefile | CONFIRMED scaffolds | Current execution limits. | No focused suite. |
| PRs #1338 and #1341 | CONFIRMED merged | Related current-main documentation state. | No AQI implementation. |

[Back to top](#top)

---

## Changelog, correction, and rollback

### Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Atmosphere AQI-versus-concentration policy-deny lane. |
| 2026-07-16 | v0.2 | Repository-grounded evidence snapshot; explicit README-only maturity; policy-path drift; canonical-contract versus compatibility-pointer split; permissive schema and metadata-only fixture posture; source-role/AirNow-AQS boundary; focused test, fixture, carrier, CI, correction, and rollback contracts. |

### Correction triggers

Correct or supersede this README when:

- a claimed absent path is found;
- the canonical policy path/package is accepted;
- a substantive test or fixture lands;
- AQI object-family treatment changes;
- observation contracts or schemas close;
- AirNow/AQS source-role policy changes;
- a reason code is accepted with different meaning;
- CI becomes substantive;
- a path or authority statement conflicts with an accepted ADR.

### Rollback

Rollback this revision if it:

- is mistaken for executable policy;
- is used to authorize AQI-to-concentration conversion;
- becomes a parallel contract/schema/policy authority;
- overstates AirNow or AQS admission;
- is treated as health, regulatory, or release authority;
- weakens cite-or-abstain or correction controls.

Mechanical rollback target:

```text
README blob: 75f2cd07f4ac833f005d9741e3b5aebd58b1fde5
paired generated receipt: remove through reviewed Git history
```

No executable test, policy bundle, fixture payload, schema, contract, validator, workflow, lifecycle object, release object, health guidance, alert, or public artifact requires rollback for this documentation-only change.

[Back to top](#top)
