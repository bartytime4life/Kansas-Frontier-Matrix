<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-air-hazards-readme
title: tools/validators/air-hazards/ — Atmosphere/Air × Hazards Validator Seam Boundary
type: readme; directory-readme; cross-domain-validator-lane; atmosphere; hazards; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only-lane; canonical-seam-documentation; compatibility-bridge-confirmed; executable-unimplemented; schemas-mixed-scaffold; policy-scaffold; tests-unestablished; ci-todo-only; not-for-life-safety
owners: OWNER_TBD — Atmosphere steward · Hazards steward · Validator steward · Source-role steward · Freshness steward · Evidence steward · Policy steward · Sensitivity steward · Security steward · Release steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1 proposed Air–Hazards validator guide
policy_label: "repository-facing; tools; validators; cross-domain; atmosphere; hazards; smoke; air-quality; knowledge-character; source-role; freshness; expiry; not-for-life-safety; official-source-redirect; evidence-aware; policy-aware; release-gated; correction-aware; rollback-aware; no-network-by-default; fail-closed; no-truth-authority; no-alert-authority; no-release-authority"
owning_root: tools/
current_path: tools/validators/air-hazards/README.md
responsibility: >
  Repository-grounded contract and routing boundary for deterministic validation across the Atmosphere/Air × Hazards
  seam. This lane coordinates source-role and knowledge-character preservation, smoke/AOD/AQI/PM2.5/model/advisory
  anti-collapse checks, time/freshness/expiry posture, official-source attribution, not-for-life-safety boundaries,
  evidence and citation closure, sensitivity propagation, release/correction/rollback references, and public-surface
  denial while deferring domain meaning, schemas, policy decisions, source registry authority, evidence/proof records,
  receipts, release authority, public serving, and emergency guidance to their owning roots.
truth_posture: >
  CONFIRMED target README v0.1 and prior blob; tools/validators/air-hazards/ contains only this README in bounded search;
  tools/validators/atmosphere_hazards/ is a compatibility bridge pointing here; domain indexes exist at
  tools/validators/domains/atmosphere/ and tools/validators/domains/hazards/; smoke specialization exists as a README-only
  lane at tools/validators/domains/atmosphere/smoke/; broad Hazards routing exists at tools/validators/hazards/; shared
  freshness routing exists at tools/validators/freshness/; no validate_air_hazards executable or AIR_HAZARDS_VALIDATION
  implementation surfaced; SmokeContext semantic contract exists with a permissive PROPOSED schema scaffold; Atmosphere
  schema index is incomplete relative to repository files; Hazards schema index reports no confirmed concrete schema in
  its checked inventory and an unresolved schema-home conflict; Atmosphere and Hazards policy READMEs are greenfield
  scaffolds; Atmosphere and Hazards workflows contain TODO-only echo jobs; Atmosphere test parent is a scaffold with
  executable tests and CI unverified / PROPOSED validation profile, deterministic report, finite findings, reason-code
  families, child delegation, fixtures, no-network tests, CI admission, migration, correction, deprecation, and rollback /
  CONFLICTED canonical seam spelling versus underscore compatibility path; broad seam versus smoke specialty and shared
  freshness responsibilities; Atmosphere contract casing/alias drift; Atmosphere concrete schema inventory versus stale
  index; Hazards domain versus non-domain schema-home notes / UNKNOWN active cross-domain validator implementation,
  production consumers, source-role registry, policy bundle entrypoints, report instances, runtime invocation, operational
  metrics, release-gate use, deployment, and current pass results / NEEDS VERIFICATION owners, CODEOWNERS, canonical
  validator topology, schema and contract pairing, source descriptors and rights, time-field vocabulary, stale thresholds,
  policy outcomes, EvidenceRef/EvidenceBundle resolution, sensitivity reviewers, fixture identity, tests, CI significance,
  correction cascade, deprecation window, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 2ab8e92cfc76f19838de5be5e3d138d33d980bd7
  prior_blob: beae47c4f9af375343a38057c9d054459c9ee0c2
  compatibility_bridge_blob: 5b7ef603ccf1d330c7647a32c63e5e49a23fd672
  atmosphere_validator_index_blob: 0bdf0d021a093b61cdeca0686a936cd91c1af318
  hazards_validator_index_blob: 20b1f0851475cfc14aacdd3248f9ff1133595296
  broad_hazards_index_blob: c3b68e4750978fa3bc08f6617f3699a93f5663ad
  atmosphere_smoke_lane_blob: 5b9ba27e27b9ccad77d495af6b310b4b8c02366a
  freshness_validator_blob: b2ff3fb3341f4f619b3a93fdd3a54922c5d22410
  smoke_context_contract_blob: 3ce536cd9440df2d0c07da4170baf9d32a4cbb1a
  smoke_context_schema_blob: 0069827d36b6ff94a58b333d39de3b7cf5804a97
  atmosphere_schema_index_blob: 1165bd4719fff2c17ce4e7f5253fa8af8315f333
  hazards_schema_index_blob: 2e8fa3c0cd987936d0bdd07024a41c78247d02a0
  atmosphere_policy_readme_blob: d897f4f67458f9d12e0ef2b2e7146eeba935df4b
  hazards_policy_readme_blob: 6118f23a6cd480494f92e8355cbfe61b19a0c25c
  atmosphere_tests_parent_blob: 6474cc33c3bdd668fd8713e06e94f7dacda97b6b
  atmosphere_workflow_blob: a3c6a21db798b02202c87f76bfba5f45c5f08c9b
  hazards_workflow_blob: ada4e42302667488316fd0ca96137c76e1d6d4f5
  validators_root_blob: e35742288404a1eeb214f8269fbacb1429c0f86a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  bounded_path_checks:
    - tools/validators/air-hazards/ surfaced only README.md
    - validate_air_hazards and AIR_HAZARDS_VALIDATION searches surfaced only this README
    - tools/validators/atmosphere_hazards/ is documented as a compatibility bridge and forbids duplicate implementation
    - tools/validators/domains/atmosphere/smoke/ is README-only and executable behavior remains unverified
    - tests/validators/air-hazards/ did not surface as an implemented test lane
    - policy/domains/atmosphere/README.md and policy/domains/hazards/README.md are greenfield scaffolds
    - domain-atmosphere and domain-hazards workflows execute TODO echo commands
related:
  - ../README.md
  - ../_common/README.md
  - ../atmosphere_hazards/README.md
  - ../hazards/README.md
  - ../freshness/README.md
  - ../evidence/README.md
  - ../citation/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../domains/atmosphere/README.md
  - ../domains/atmosphere/smoke/README.md
  - ../domains/hazards/README.md
  - ../../../docs/architecture/smoke-atmosphere-hazards.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/SENSITIVITY.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../contracts/domains/atmosphere/SmokeContext.md
  - ../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../contracts/domains/atmosphere/AdvisoryContext.md
  - ../../../schemas/contracts/v1/domains/atmosphere/SmokeContext.schema.json
  - ../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../schemas/contracts/v1/domains/hazards/
  - ../../../policy/domains/atmosphere/
  - ../../../policy/domains/hazards/
  - ../../../policy/release/hazards/
  - ../../../fixtures/domains/atmosphere/
  - ../../../fixtures/domains/hazards/
  - ../../../tests/domains/atmosphere/
  - ../../../tests/domains/hazards/
  - ../../../data/registry/sources/atmosphere/
  - ../../../data/registry/sources/hazards/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, tools, validators, air-hazards, atmosphere, hazards, smoke, aod, aqi, pm25, advisory, source-role, knowledge-character, freshness, expiry, evidence, sensitivity, not-for-life-safety, official-source, fail-closed, migration, rollback]
notes:
  - "This revision changes only tools/validators/air-hazards/README.md plus the required generated provenance receipt."
  - "No validator code, contract, schema, policy, fixture, test, workflow, source descriptor, receipt instance, proof, release record, API route, alert, model call, or public output is created or modified."
  - "This README preserves air-hazards as the documented cross-domain seam and keeps atmosphere_hazards as a compatibility bridge."
  - "A later implementation, rename, schema-home decision, policy activation, or release-gate adoption must use reviewed migration/ADR discipline."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere/Air × Hazards Validator Seam Boundary

`tools/validators/air-hazards/`

> **One-line purpose.** This lane defines the deterministic validation boundary for claims and products crossing the Atmosphere/Air × Hazards seam—preserving source role, knowledge character, time/freshness, official-source authority, evidence, sensitivity, release, correction, and rollback without becoming domain truth, an emergency alert, a policy decision, or publication authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Lane: cross-domain seam" src="https://img.shields.io/badge/lane-cross--domain__seam-blueviolet">
  <img alt="Implementation: README only" src="https://img.shields.io/badge/implementation-README__only-orange">
  <img alt="Boundary: not life safety" src="https://img.shields.io/badge/boundary-not__life__safety-critical">
  <img alt="Posture: cite or abstain" src="https://img.shields.io/badge/posture-cite__or__abstain-success">
</p>

> [!IMPORTANT]
> **Current enforcement is not established.** Bounded repository search surfaced only this README under `air-hazards/`; no `validate_air_hazards*` executable or implemented `AIR_HAZARDS_VALIDATION_*` result producer was found.

> [!CAUTION]
> **A schema-valid smoke object can still be unsafe or false.** The inspected `SmokeContext` schema is a permissive `PROPOSED` scaffold with empty properties and `additionalProperties: true`. Shape acceptance does not prove source role, freshness, evidence closure, policy permission, release readiness, or life-safety suitability.

> [!WARNING]
> **KFM is never an emergency-alert authority.** Warning, watch, advisory, smoke, AQI, fire-weather, and operational-context material may be represented only as evidence-bound context with visible source, role, validity, expiry, caveat, official-source redirect, release state, correction path, and rollback posture.

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Inventory](#confirmed-repository-inventory) · [Routing](#seam-routing-map) · [Ownership](#domain-ownership-boundary) · [Characters](#knowledge-character-and-source-role-model) · [Packet](#validation-input-packet) · [Invariants](#cross-domain-validation-invariants) · [Report](#validation-report-contract) · [Outcomes](#finite-outcomes-and-reason-codes) · [Maturity](#contract-schema-policy-and-fixture-maturity) · [Security](#security-privacy-and-untrusted-content) · [Lifecycle](#lifecycle-release-correction-and-rollback) · [Tests](#tests-fixtures-and-no-network-posture) · [CI](#ci-admission-contract) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Migration](#migration-compatibility-and-deprecation) · [Open](#open-verification-register) · [Rollback](#rollback-path) · [Ledger](#evidence-ledger) · [Changelog](#changelog)

---

<a id="purpose"></a>

## Purpose

`tools/validators/air-hazards/` is the cross-domain validator seam for Atmosphere/Air context that is consumed by, compared with, or represented beside Hazards context.

The durable validation question is:

> Does the candidate preserve which domain owns each fact, which source role and knowledge character each input carries, when each input is valid, which official source remains authoritative, what evidence and policy support the requested use, and whether the output is safe for the requested surface?

This lane may eventually orchestrate deterministic checks for:

- smoke, plume, aerosol, AOD, PM2.5, AQI, ozone, weather, wind, forecast, and advisory context;
- wildfire or fire-weather context without claiming legal fire status or operational command;
- issue time, valid time, expiry, retrieval time, model-run time, release time, and correction time;
- source role, knowledge character, model/observation separation, and remote-sensing/event separation;
- official-source attribution and not-for-life-safety disclaimers;
- EvidenceRef/EvidenceBundle, citation, policy, review, release, correction, and rollback linkage;
- sensitivity and reconstruction risk across infrastructure, people/land, habitat, rare species, archaeology, and precise assets;
- finite fail-closed outcomes for map, API, tile, export, graph, search, Focus Mode, report, and AI surfaces.

This lane must not:

- define Atmosphere/Air or Hazards meaning;
- issue, confirm, replace, summarize into, or compete with an official emergency alert;
- create a HazardEvent, AirObservation, SmokeContext, EvidenceBundle, PolicyDecision, ReleaseManifest, or public layer;
- call source systems in the default validator suite;
- infer PM2.5 from AOD or smoke masks without an accepted method and evidence profile;
- promote model or remote-sensing products into observations or confirmed events;
- treat a passing validator as truth, policy permission, release approval, or publication.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Evidence verdict

| Surface | Status | Safe conclusion |
|---|---:|---|
| Requested README | **CONFIRMED v0.1 before revision** | The proposed seam contract existed. |
| Direct `air-hazards/` inventory | **CONFIRMED README-only in bounded search** | No executable, configuration, fixture, or test file surfaced under the lane. |
| `validate_air_hazards*` search | **No executable surfaced** | Do not claim a runnable Air–Hazards validator. |
| `atmosphere_hazards/` | **CONFIRMED compatibility bridge** | It points to `air-hazards/` and forbids duplicate implementation. |
| Atmosphere domain validator index | **CONFIRMED README / implementation unverified** | Routes narrow Atmosphere validators and the smoke child lane. |
| Hazards domain validator index | **CONFIRMED README / implementation unverified** | Routes domain-scoped Hazards validation and not-for-life-safety checks. |
| Broad Hazards index | **CONFIRMED README / implementation unverified** | Routes broad Hazards helpers outside the per-domain tree. |
| Atmosphere smoke child | **CONFIRMED README-only lane** | Defines smoke/AOD seam invariants; no executable was verified. |
| Shared freshness lane | **CONFIRMED README / implementation unverified** | Owns reusable stale-state and expiry validation concepts. |
| `SmokeContext` contract | **CONFIRMED semantic contract** | Defines source-dependent smoke context and anti-collapse rules. |
| `SmokeContext` schema | **CONFIRMED permissive PROPOSED scaffold** | Empty properties and open additional properties provide little enforcement. |
| Atmosphere schema index | **CONFIRMED draft / inventory drift** | The index lists one known schema while additional files exist. |
| Hazards schema index | **CONFIRMED draft / path conflict** | No concrete schema was confirmed by its checked inventory; placement remains conflicted. |
| Atmosphere/Hazards policy READMEs | **CONFIRMED greenfield scaffolds** | Policy authority exists as a root, but substantive executable rules are not established. |
| Atmosphere tests parent | **CONFIRMED scaffold** | Test responsibilities are documented; executable coverage remains unverified. |
| Atmosphere/Hazards workflows | **CONFIRMED TODO-only** | Jobs echo TODO; workflow success would not prove validator enforcement. |
| Runtime use, report emission, release-gate adoption | **UNKNOWN** | No operational claim is made. |

### Current maturity statement

The lane is suitable for:

- responsibility routing;
- compatibility and naming control;
- review checklists;
- implementation planning;
- test and fixture design;
- migration and rollback planning.

It is not evidence of:

- runnable validation;
- a stable report schema;
- active policy evaluation;
- complete schema coverage;
- released public products;
- current operational alert handling;
- life-safety suitability;
- production deployment.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

### Placement basis

The existing path remains under `tools/`, the responsibility root for durable validators and checkers. No new path is introduced.

Responsibility remains separated:

```text
tools/validators/air-hazards/                  = cross-domain validation orchestration and findings
tools/validators/atmosphere_hazards/           = compatibility pointer; no duplicate implementation
tools/validators/domains/atmosphere/smoke/     = Atmosphere smoke specialization
tools/validators/freshness/                    = shared stale-state and expiry checks
docs/domains/                                  = domain doctrine and human-readable boundaries
contracts/domains/                             = semantic object meaning
schemas/contracts/v1/                          = machine-checkable shape
policy/                                        = allow / deny / restrict / hold / abstain decisions
data/registry/sources/                         = admitted source records and source descriptors
data/proofs/                                   = EvidenceBundles and proof support
data/receipts/                                 = process-memory and validation receipts
tests/ and fixtures/                           = executable proof and deterministic examples
release/                                       = release, correction, withdrawal, and rollback authority
apps/ and runtime/                             = governed serving and runtime behavior
```

### Authority rules

| Concern | Owning authority | This lane may | This lane must not |
|---|---|---|---|
| Atmosphere/Air meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` | Validate declared semantics. | Redefine observations, models, AOD, smoke, AQI, or advisory meaning. |
| Hazards meaning | `docs/domains/hazards/`, `contracts/domains/hazards/` | Validate declared Hazards boundaries. | Issue alerts, define events, or create emergency instructions. |
| Machine shape | Accepted `schemas/contracts/v1/...` homes | Load and validate schemas. | Invent schema fields locally or select a schema home silently. |
| Policy | `policy/domains/atmosphere/`, `policy/domains/hazards/`, release policy | Check decision refs and obligations. | Make policy decisions or expose hidden thresholds. |
| Sources | `data/registry/sources/...` | Check source refs, roles, rights, cadence, and official-source links. | Admit sources or treat watcher output as authority. |
| Evidence | Evidence contracts and `data/proofs/` | Resolve and evaluate references. | Create proof closure or treat a ref as a bundle. |
| Receipts | `data/receipts/` | Require and reference receipts. | Store emitted receipts here. |
| Release | `release/` | Check readiness and references. | Approve publication or issue withdrawal. |
| Public serving | Governed `apps/` and runtime roots | Validate an envelope or derivative candidate. | Serve data, alerts, maps, or answers directly. |

### Anti-collapse law

This lane must keep distinct:

- checker success and truth;
- evidence closure and policy permission;
- policy permission and release approval;
- source observation and model output;
- AOD/smoke mask and PM2.5 concentration;
- AQI report and pollutant measurement;
- atmospheric context and hazard event truth;
- remote-sensing detection and confirmed ground event;
- warning/advisory context and KFM-issued instruction;
- freshness and current truth;
- public rendering and release authority.

[Back to top](#top)

---

<a id="confirmed-repository-inventory"></a>

## Confirmed repository inventory

### Direct lane

```text
tools/validators/air-hazards/
└── README.md
```

No executable or test file was confirmed beneath this path.

### Related validator surfaces

| Path | Current role | Implementation posture |
|---|---|---|
| `tools/validators/air-hazards/` | Canonical documented Atmosphere/Air × Hazards seam. | README-only. |
| `tools/validators/atmosphere_hazards/` | Naming and compatibility bridge. | README-only; duplicate code denied. |
| `tools/validators/domains/atmosphere/` | Per-domain Atmosphere child-validator index. | README-backed; execution unverified. |
| `tools/validators/domains/atmosphere/smoke/` | Smoke/AOD specialization. | README-only; execution unverified. |
| `tools/validators/domains/hazards/` | Per-domain Hazards validator index. | README-backed; execution unverified. |
| `tools/validators/hazards/` | Broad Hazards routing index. | README-backed; no child executable confirmed. |
| `tools/validators/freshness/` | Shared time/freshness/expiry lane. | README-backed; execution unverified. |
| `tools/validators/evidence/` | Shared EvidenceRef/EvidenceBundle validation routing. | README-backed; implementation varies outside this edit. |
| `tools/validators/cross-domain-joins/` | Generic cross-domain anti-collapse checks. | Separate shared responsibility. |
| `tools/validators/_common/` | Shared JSON Schema runner and registry helpers. | Confirmed implementation, but not Air–Hazards semantics. |

### Documentation and trust surfaces

| Surface | Confirmed posture |
|---|---|
| `SmokeContext` semantic contract | Draft semantic contract with explicit smoke/AOD/PM2.5/model/Hazards boundaries. |
| `SmokeContext` schema | `PROPOSED`, empty properties, `additionalProperties: true`. |
| Atmosphere schema index | Draft and incomplete relative to actual repository files. |
| Hazards schema index | Draft, reports no concrete schema in its checked inventory, and records a schema-home conflict. |
| Atmosphere policy README | Greenfield scaffold with over-broad wording; no substantive rule enforcement proven. |
| Hazards policy README | Greenfield scaffold with over-broad wording; no substantive rule enforcement proven. |
| Atmosphere domain tests | Parent scaffold with planned child lanes and unverified executable coverage. |
| Atmosphere/Hazards domain workflows | TODO-only echo jobs. |

[Back to top](#top)

---

<a id="seam-routing-map"></a>

## Seam routing map

Route each concern to the narrowest responsible lane.

| Validation concern | Preferred lane | Reason |
|---|---|---|
| Cross-domain Atmosphere/Air × Hazards packet | `tools/validators/air-hazards/` | Coordinates the seam without absorbing domain meaning. |
| Legacy underscore path | `tools/validators/atmosphere_hazards/` | Compatibility pointer only. |
| SmokeContext or AODRaster object-specific checks | `tools/validators/domains/atmosphere/smoke/` | Atmosphere owns smoke/AOD atmospheric semantics. |
| Generic observation/model/mask/advisory role checks within Atmosphere | `tools/validators/domains/atmosphere/` or accepted child | Domain-specific validation. |
| HazardEvent, WarningContext, ImpactArea, and not-for-life-safety checks | `tools/validators/domains/hazards/` | Hazards-domain responsibility. |
| Broad Hazards helper that intentionally sits outside domain tree | `tools/validators/hazards/` | Broad routing, with explicit justification. |
| Source cadence, issue/valid/expiry/retrieval/correction timing | `tools/validators/freshness/` | Shared reusable time posture. |
| EvidenceRef and EvidenceBundle closure | `tools/validators/evidence/` and accepted resolver | Shared evidence responsibility. |
| Generic cross-domain join integrity | `tools/validators/cross-domain-joins/` | Shared anti-collapse logic. |
| Schema parsing and `$ref` resolution | `tools/validators/_common/` and schema wrappers | Shared machine-shape plumbing. |
| Public release readiness | `tools/validators/release/` plus `release/` records | Validator checks; release authority remains separate. |

### Delegation rule

A future Air–Hazards parent runner should:

1. validate the seam packet shape;
2. delegate object-specific checks to owning domain validators;
3. delegate freshness checks to the shared freshness lane;
4. delegate evidence resolution to accepted evidence validators;
5. evaluate policy through accepted policy runtime interfaces;
6. aggregate findings without rewriting child reason codes;
7. return one deterministic parent report;
8. never call a model, issue an alert, or publish output.

[Back to top](#top)

---

<a id="domain-ownership-boundary"></a>

## Domain ownership boundary

### Atmosphere/Air owns

- air stations and air observations;
- pollutant measurements such as PM2.5 and ozone;
- source-dependent smoke context;
- AOD rasters and remote-sensing masks/proxies;
- atmospheric model fields and forecasts;
- wind, temperature, humidity, and other weather context;
- AQI/report context when represented as report/advisory context rather than raw concentration;
- Atmosphere-specific uncertainty, units, averaging periods, and model-run lineage.

### Hazards owns

- hazard events and hazard observations;
- warning, watch, and advisory context as evidence-bound operational context;
- disaster declarations and regulatory/historical hazard context;
- wildfire detection/event context subject to source-role limitations;
- exposure, resilience, impact-area, and hazard-timeline derivatives;
- not-for-life-safety disclaimers and official-source redirects for Hazards surfaces;
- Hazards release, correction, withdrawal, and rollback posture.

### The seam owns no truth

The Air–Hazards validator seam may check relationships such as:

```text
SmokeContext --supports/contextualizes--> HazardTimeline
PM25Observation --contextualizes--> ExposureSummary
WindField --contextualizes--> FireWeatherContext
AdvisoryContext --refers-to--> OfficialSource
AODRaster --supports-with-limitations--> SmokeContext
WildfireDetection --may-relate-to--> SmokeContext
```

It must not convert those edges into ownership transfer.

[Back to top](#top)

---

<a id="knowledge-character-and-source-role-model"></a>

## Knowledge-character and source-role model

### Required separations

| Input or output | Required character or role | Forbidden upgrade |
|---|---|---|
| Ground sensor pollutant reading | Observed measurement with units, averaging period, QA, and time | Generic “air quality fact” without measurement posture. |
| AQI value/report | Derived or report/advisory context | Raw pollutant concentration. |
| AOD raster | Remote-sensing mask/proxy | PM2.5, AQI, exposure, or health impact. |
| HMS-style smoke analysis | Remote-sensing analysis/mask context | Confirmed ground smoke event or concentration. |
| HRRR-Smoke-style field | Atmospheric model field | Observation or official warning. |
| Satellite hotspot/thermal detection | Remote-sensing detection/candidate | Legal fire status, confirmed perimeter, evacuation need, or ground event. |
| Official warning/watch/advisory | Operational context from named official source | KFM-authored instruction or open-ended current state. |
| Historical regulatory archive | Regulatory/historical context | Current observed condition. |
| KFM derivative | Derived public-safe context with evidence and release lineage | Source observation, official alert, or release authority. |

### Minimum source-role fields

A mature validation packet should carry, directly or by resolvable reference:

- source identifier and SourceDescriptor reference;
- source role;
- knowledge character;
- object family;
- official-source status;
- rights and attribution posture;
- observed/source/model/issue/valid/retrieval/release/correction times as applicable;
- uncertainty and limitations;
- evidence refs and bundle refs;
- policy, review, release, and rollback refs;
- requested audience and requested surface.

Missing role or character must never default to observed, official, current, safe, or public.

[Back to top](#top)

---

<a id="validation-input-packet"></a>

## Validation input packet

The packet below is **PROPOSED** until an accepted contract and schema exist.

```yaml
validation_request:
  request_id: string
  profile_id: string
  profile_version: string
  checked_at: date-time
  requested_operation: validate
  requested_surface: map | api | tile | export | report | search | graph | focus_mode | ai | release_preflight
  audience: public | steward | restricted | internal
  candidate_ref: string
  candidate_type: string
  owning_domain: atmosphere | hazards | cross_domain
  source_refs: []
  source_roles: []
  knowledge_characters: []
  evidence_refs: []
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_refs: []
  release_refs: []
  receipt_refs: []
  correction_refs: []
  rollback_refs: []
  time_posture:
    observed_at: null
    source_at: null
    model_run_at: null
    issued_at: null
    valid_from: null
    valid_until: null
    retrieved_at: null
    released_at: null
    corrected_at: null
  sensitivity:
    tier: null
    exact_geometry_present: false
    reconstruction_risk: unknown
  official_source:
    is_official_context: false
    source_url_ref: null
    redirect_required: false
  content_digests:
    candidate: sha256:<hex>
    profile: sha256:<hex>
```

### Packet rules

- Inputs should be immutable for one validation run.
- Raw payloads should be referenced, not copied into reports.
- Digests must use accepted canonicalization rules.
- Validation time must not overwrite source or observation time.
- Official-source URLs should be safe references, not scraped instructions.
- Sensitive geometry and private data must not appear in logs or public findings.
- Missing required context must produce a finite negative result.

[Back to top](#top)

---

<a id="cross-domain-validation-invariants"></a>

## Cross-domain validation invariants

| Invariant | Required validation | Fail-closed condition |
|---|---|---|
| Domain ownership preserved | Every object and claim names its owning domain. | Atmosphere truth is republished as Hazards truth or vice versa. |
| Source role preserved | Observed, modeled, remote-sensing, regulatory, advisory, aggregate, candidate, and derived roles remain distinct. | A role is missing, silently upgraded, or relabeled. |
| Knowledge character preserved | Character matches source and object family. | Model, mask, report, or advisory is treated as observation. |
| AQI boundary preserved | AQI remains a derived/report context with method and period. | AQI is treated as raw concentration. |
| AOD boundary preserved | AOD remains proxy/mask context. | AOD is treated as PM2.5, AQI, exposure, or health impact. |
| Smoke boundary preserved | SmokeContext remains source-dependent atmospheric context. | Smoke context becomes PM2.5, confirmed event, impact, or instruction. |
| Model boundary preserved | Model run, version, valid interval, and uncertainty remain visible. | Model field is presented as observed fact or official warning. |
| Detection boundary preserved | Remote-sensing detection remains candidate/context. | Hotspot or plume mask becomes confirmed legal/ground event. |
| Alert authority denied | Official source and validity remain visible; KFM is referral-only. | KFM issues or replaces a warning, watch, advisory, or life-safety direction. |
| Freshness explicit | Required source, issue, valid, expiry, model, retrieval, release, and correction times remain distinct. | Stale, expired, superseded, or unversioned context is shown as current. |
| Evidence closure required | Claim-bearing output resolves required EvidenceRefs to admissible support. | Ref is absent, unresolved, stale, withdrawn, or insufficient. |
| Policy and rights required | Requested use is evaluated under current policy, rights, and sensitivity context. | Policy is missing, ambiguous, stale, or bypassed. |
| Most-restrictive sensitivity wins | Cross-lane joins inherit the strictest applicable posture. | Sensitive geometry, infrastructure, people, habitat, or archaeology detail leaks. |
| Release remains separate | Public-bound derivative has release, correction, and rollback refs. | Validator success is used as publication approval. |
| Correction cascade preserved | Upstream correction or withdrawal reaches dependent derivatives. | Corrected source remains active in public output without review. |
| No lifecycle shortcut | Candidate follows governed lifecycle states. | RAW, WORK, QUARANTINE, or unreleased data reaches a public surface. |
| No generated authority | AI summaries and narrative carriers remain downstream. | Generated text becomes evidence, alert, or domain truth. |

### Terminal decisions

Any violation above should result in one of:

```text
FAIL | ABSTAIN | DENY | HOLD | ERROR
```

`PASS` is allowed only when every configured required check completes successfully for the declared scope.

[Back to top](#top)

---

<a id="validation-report-contract"></a>

## Validation report contract

The report below is **PROPOSED**. No accepted Air–Hazards ValidationReport schema was confirmed.

```yaml
validation_report:
  report_id: string
  report_version: string
  validator_profile_ref: string
  validator_profile_digest: sha256:<hex>
  checked_subject_ref: string
  checked_subject_digest: sha256:<hex>
  started_at: date-time
  completed_at: date-time
  outcome: PASS | FAIL | ABSTAIN | DENY | HOLD | ERROR
  blocking: true
  reason_codes: []
  findings:
    - finding_id: string
      check_id: string
      severity: INFO | WARN | ERROR | BLOCK
      reason_code: string
      message: string
      object_ref: null
      evidence_refs: []
      remediation: null
  delegated_reports: []
  source_refs: []
  evidence_refs: []
  policy_decision_refs: []
  review_refs: []
  release_refs: []
  receipt_refs: []
  correction_refs: []
  rollback_refs: []
  limitations: []
```

### Report rules

- The report must be deterministic for identical canonical inputs and profile versions.
- Findings must use stable reason codes rather than free-form-only prose.
- Reports must not include credentials, raw restricted content, private chain-of-thought, or exact sensitive geometry.
- A report is not an EvidenceBundle, PolicyDecision, ReleaseManifest, official warning, or public answer.
- Report storage belongs in an accepted artifact or receipt lane, not this README directory.
- Delegated child findings should retain their original identifiers and reason codes.
- Unknown or unsupported fields must not silently pass.

[Back to top](#top)

---

<a id="finite-outcomes-and-reason-codes"></a>

## Finite outcomes and reason codes

### Parent outcomes

| Outcome | Meaning |
|---|---|
| `AIR_HAZARDS_PASS` | All configured required seam checks passed for the declared scope. |
| `AIR_HAZARDS_FAIL` | One or more required validation checks failed. |
| `AIR_HAZARDS_ABSTAIN` | Available evidence or context is insufficient to decide safely. |
| `AIR_HAZARDS_DENY` | Policy, sensitivity, rights, alert-authority, or public-boundary rules prohibit the requested use. |
| `AIR_HAZARDS_HOLD` | Steward review, correction, source refresh, policy resolution, or release support is pending. |
| `AIR_HAZARDS_ERROR` | Validator machinery, profile loading, dependency execution, or report construction failed safely. |

These names are proposed compatibility vocabulary. They must not be treated as implemented enum values until a contract/schema and tests are accepted.

### Proposed reason-code families

| Family | Example codes |
|---|---|
| Placement and configuration | `VALIDATOR_PROFILE_MISSING`, `VALIDATOR_PROFILE_CONFLICT`, `DUPLICATE_IMPLEMENTATION_RISK`, `DEPENDENCY_VALIDATOR_MISSING` |
| Domain and object identity | `OWNING_DOMAIN_MISSING`, `DOMAIN_AUTHORITY_COLLAPSE`, `OBJECT_FAMILY_MISSING`, `OBJECT_FAMILY_CONFLICT` |
| Source role and character | `SOURCE_ROLE_MISSING`, `SOURCE_ROLE_COLLAPSE`, `KNOWLEDGE_CHARACTER_MISSING`, `KNOWLEDGE_CHARACTER_COLLAPSE` |
| Air-quality anti-collapse | `AQI_AS_CONCENTRATION_DENIED`, `AOD_AS_PM25_DENIED`, `SMOKE_CONTEXT_AS_PM25_DENIED`, `MODEL_AS_OBSERVATION_DENIED` |
| Hazard/event anti-collapse | `REMOTE_SENSING_AS_EVENT_DENIED`, `ATMOSPHERE_AS_HAZARD_TRUTH_DENIED`, `HAZARD_AS_SENSOR_TRUTH_DENIED` |
| Alert and life safety | `ALERT_AUTHORITY_DENIED`, `NOT_FOR_LIFE_SAFETY_POSTURE_MISSING`, `OFFICIAL_SOURCE_REDIRECT_MISSING`, `OPERATIONAL_INSTRUCTION_DENIED` |
| Time and freshness | `TIME_KIND_MISSING`, `VALIDITY_WINDOW_MISSING`, `EXPIRY_MISSING`, `FRESHNESS_WINDOW_EXPIRED`, `SUPERSESSION_UNRESOLVED` |
| Evidence and citation | `EVIDENCE_REF_MISSING`, `EVIDENCE_REF_UNRESOLVED`, `EVIDENCE_BUNDLE_INCOMPLETE`, `CITATION_VALIDATION_MISSING` |
| Rights, policy, sensitivity | `RIGHTS_UNRESOLVED`, `POLICY_DECISION_MISSING`, `SENSITIVITY_REVIEW_REQUIRED`, `SENSITIVE_JOIN_DENIED` |
| Release and correction | `RELEASE_REFERENCE_MISSING`, `CORRECTION_PATH_MISSING`, `ROLLBACK_TARGET_MISSING`, `UPSTREAM_CORRECTION_UNPROPAGATED` |
| Lifecycle and public boundary | `LIFECYCLE_VIOLATION`, `UNRELEASED_INPUT_DENIED`, `PUBLIC_BOUNDARY_VIOLATION`, `REPORT_DESTINATION_INVALID` |
| Runtime failure | `INPUT_PARSE_ERROR`, `SCHEMA_LOAD_ERROR`, `DEPENDENCY_ERROR`, `VALIDATOR_INTERNAL_ERROR` |

Reason codes should be safe to expose at the intended audience level. They must not reveal hidden policy thresholds, precise protected locations, private identities, credentials, or source payload contents.

[Back to top](#top)

---

<a id="contract-schema-policy-and-fixture-maturity"></a>

## Contract, schema, policy, and fixture maturity

### Atmosphere contracts

Confirmed semantic contract surfaces include:

- `SmokeContext`;
- `AODRaster`;
- `PM25Observation`;
- `AdvisoryContext`;
- `ForecastContext`;
- `WindField`;
- `AirObservation`;
- `AtmosphereAirDecisionEnvelope`.

Their existence does not prove complete schemas, fixtures, validators, policy, or runtime use.

### Atmosphere schemas

Confirmed current issues:

- `SmokeContext.schema.json` is a permissive scaffold;
- the Atmosphere schema index lists only a limited known inventory while additional schema files exist;
- contract casing and alias paths coexist;
- fixture and validator linkage is incomplete or unverified;
- schema validity alone cannot enforce semantic anti-collapse.

### Hazards schemas

The Hazards schema index records:

- a proposed/conflicted canonical posture;
- no concrete `.schema.json` file confirmed by its checked inventory;
- an unresolved `domains/hazards/` versus `v1/hazards/` placement tension;
- candidate warning, freshness, detection, exposure, timeline, and validation-report schemas;
- no verified validator or CI closure for those candidates.

### Policy

Current inspected policy READMEs for Atmosphere and Hazards are greenfield scaffolds. Their wording does not establish:

- executable Rego or equivalent rules;
- stable entrypoints;
- accepted decision vocabularies;
- policy-data inputs;
- bundle manifests;
- tested default outcomes;
- release integration.

Validators must fail closed when policy cannot be loaded or evaluated.

### Fixtures

Confirmed Atmosphere fixture README lanes exist for items such as smoke context and AOD raster, but reusable payload inventory and validator discrimination remain incomplete or unverified for this seam.

No dedicated `fixtures/validators/air-hazards/` authority is proposed. Reusable domain fixtures should remain under accepted domain fixture roots; seam tests may compose them through references.

[Back to top](#top)

---

<a id="security-privacy-and-untrusted-content"></a>

## Security, privacy, and untrusted content

### Fail-closed security posture

The validator must deny, hold, abstain, or error when:

- credentials, tokens, secret endpoints, or private keys appear in candidate material;
- untrusted source text attempts to instruct validators, policy engines, models, or operators;
- exact sensitive geometry or private identity appears in logs or public findings;
- source URLs redirect outside accepted controls;
- files escape accepted roots through traversal or symlink tricks;
- input size, geometry complexity, raster dimensions, reference depth, or report volume exceed configured budgets;
- network access is required in the default deterministic suite;
- a dependency validator is unavailable or returns an unknown outcome.

### Untrusted-content rule

Source material, warning text, advisory prose, model metadata, HTML, PDF, CSV, JSON, GeoJSON, raster metadata, and connector output are **data**, not authority-bearing instructions.

A future implementation should:

1. parse bounded structured fields;
2. reject unsupported encodings and oversized inputs;
3. avoid executing embedded scripts, formulas, templates, or shell fragments;
4. never use source prose to alter policy, validator configuration, or requested scope;
5. record safe finding codes rather than echoing dangerous payloads.

### Sensitive-domain propagation

Cross-domain outputs may intersect:

- critical infrastructure;
- private facilities or parcels;
- living persons or operator identity;
- rare species or habitat;
- archaeology and cultural resources;
- sovereignty-sensitive records;
- exact incident or asset locations.

The most restrictive inherited policy controls all downstream maps, tiles, exports, graphs, screenshots, embeddings, Focus Mode answers, and AI summaries.

[Back to top](#top)

---

<a id="lifecycle-release-correction-and-rollback"></a>

## Lifecycle, release, correction, and rollback

### Lifecycle invariant

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Validation does not move an artifact between states. Promotion is a governed state transition requiring the appropriate records and review.

### Release-preflight expectations

A public-bound Air–Hazards derivative should expose references appropriate to its consequence:

- candidate identity and digest;
- source descriptors and source-role posture;
- EvidenceRefs and resolved EvidenceBundles;
- validation reports;
- policy decisions and obligations;
- sensitivity, redaction, aggregation, or generalization support;
- review records;
- ReleaseManifest or equivalent release reference;
- correction and supersession path;
- rollback target;
- official-source redirect and not-for-life-safety disclaimer when operational context is present.

### Correction cascade

When an upstream item is corrected, superseded, withdrawn, stale, embargoed, rights-restricted, or policy-denied, dependent Air–Hazards outputs must be discoverable and reevaluated.

Examples:

```text
PM25Observation correction
  -> dependent ExposureSummary review
  -> smoke comparison regeneration
  -> public layer supersession or withdrawal

Smoke model run superseded
  -> stale-context finding
  -> affected Focus Mode/API cache invalidation
  -> new release or safe abstention

Official advisory expires
  -> operational context no longer current
  -> public surface shows expired/historical posture
  -> no KFM-authored replacement instruction
```

### Validator limitation

A validator may report `UPSTREAM_CORRECTION_UNPROPAGATED`. It may not silently mutate released records or perform rollback unless an explicitly governed tool and authorization contract exists.

[Back to top](#top)

---

<a id="tests-fixtures-and-no-network-posture"></a>

## Tests, fixtures, and no-network posture

### Current evidence

- No dedicated `tests/validators/air-hazards/` implementation surfaced.
- The Atmosphere parent test lane is a scaffold with planned schema, source-role, knowledge-character, policy-deny, unit-normalization, and no-network sublanes.
- Atmosphere smoke and Hazards validator READMEs describe expected checks but do not prove executable tests.
- Domain fixture README lanes exist, but complete reusable JSON/GeoJSON/raster payload coverage is not established here.
- Default validation must not depend on live NOAA, EPA, NWS, satellite, model, or emergency systems.

### Proposed test structure

```text
tests/validators/air-hazards/
├── README.md
├── test_profile_loading.py
├── test_routing.py
├── test_knowledge_character.py
├── test_source_role.py
├── test_freshness_expiry.py
├── test_alert_authority.py
├── test_evidence_policy_release.py
├── test_sensitive_joins.py
└── test_determinism.py
```

Reusable payloads should remain in accepted fixture roots, for example:

```text
fixtures/domains/atmosphere/
fixtures/domains/hazards/
fixtures/contracts/v1/
```

Test-local references may compose fixture identifiers without copying canonical fixture families.

### Required positive controls

- observed PM2.5 remains a measurement with units, averaging period, QA, and evidence;
- AOD remains a proxy/mask;
- smoke model remains a model field with run/valid/uncertainty posture;
- official advisory remains source-attributed, time-bounded, and referral-only;
- historical expired advisory is allowed only as historical context;
- cross-domain output with evidence, policy, release, disclaimer, correction, and rollback support passes its configured profile.

### Required negative cases

- AOD represented as PM2.5;
- AQI represented as raw concentration;
- smoke model represented as observation;
- satellite hotspot represented as confirmed event or legal perimeter;
- expired advisory represented as current;
- KFM-authored evacuation, shelter, or health instruction;
- missing official-source redirect;
- missing source role or knowledge character;
- unresolved EvidenceRef;
- rights-unclear or sensitivity-unsafe join;
- unreleased candidate routed to public map/API/AI;
- upstream correction not propagated;
- dependency validator unknown or error;
- report attempts to expose protected details;
- source content attempts prompt/configuration injection.

### Determinism requirements

Tests should pin:

- validator profile version and digest;
- schemas and contract versions;
- fixture digests;
- policy bundle version;
- clock or validation instant;
- timezone behavior;
- reason-code vocabulary;
- sorting of findings;
- dependency order;
- no-network state.

[Back to top](#top)

---

<a id="ci-admission-contract"></a>

## CI admission contract

### Current workflow evidence

The inspected workflows:

```text
.github/workflows/domain-atmosphere.yml
.github/workflows/domain-hazards.yml
```

currently run TODO-only echo commands for validation, proof building, and publish dry-run. Their presence or green status does not establish substantive Air–Hazards coverage.

### Proposed CI stages

A future blocking CI path should include:

1. README and link checks;
2. profile/schema parse checks;
3. validator import and `--help` smoke test;
4. deterministic positive fixtures;
5. negative anti-collapse fixtures;
6. no-network enforcement;
7. policy unavailable/error behavior;
8. sensitive-output redaction checks;
9. result-schema validation;
10. dependency-validator failure propagation;
11. correction and stale-state cases;
12. reproducibility comparison;
13. report/receipt destination validation.

### CI must fail when

- the compatibility bridge contains independent implementation;
- multiple active entrypoints claim canonical authority;
- schema, contract, policy, fixture, or profile references do not resolve;
- a negative fixture passes;
- an expected valid fixture fails;
- findings are nondeterministic;
- the default suite uses network access;
- validator output leaks secrets or sensitive detail;
- unknown outcomes are treated as success;
- TODO-only jobs are presented as substantive coverage.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

1. **Accept the lane topology.** Confirm `air-hazards/` as canonical seam and `atmosphere_hazards/` as compatibility-only, or record a reviewed migration.
2. **Define an immutable seam profile.** Specify dependencies, required checks, finite outcomes, safe reason codes, and resource budgets.
3. **Resolve contract and schema references.** Pair Atmosphere and Hazards object families without creating cross-domain canonical copies.
4. **Harden core schemas.** Replace empty-property scaffolds with reviewed fields, valid/invalid fixtures, and registry records.
5. **Define policy entrypoints.** Establish runtime inputs, default fail-closed behavior, obligations, and safe errors.
6. **Implement child validators first.** Smoke/AOD and domain-specific checks should remain with owning lanes.
7. **Implement shared freshness and evidence dependencies.** Avoid duplicate time and evidence logic.
8. **Implement a thin parent orchestrator.** Aggregate child reports; do not redefine child semantics.
9. **Add structured report schema.** Validate all emitted reports.
10. **Add deterministic no-network tests.** Include positive controls and strong negative matrices.
11. **Wire substantive CI.** Replace TODO echo jobs with commands that can block.
12. **Run a documentation-only dry adoption.** Observe findings without gating release.
13. **Adopt as a gate only after review.** Require owners, security/privacy review, receipts, correction behavior, and rollback proof.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

The Air–Hazards validator seam is not implementation-complete until all required items are verified.

### Placement and ownership

- [ ] One canonical seam path and one active implementation are accepted.
- [ ] Compatibility paths contain no independent validator logic.
- [ ] Owners and CODEOWNERS are assigned.
- [ ] Atmosphere, Hazards, smoke specialty, freshness, evidence, and release responsibilities are non-overlapping.

### Contracts and schemas

- [ ] Every validated object family has an accepted semantic contract.
- [ ] Canonical schema homes are resolved.
- [ ] Schemas have stable IDs, meaningful required fields, and bounded extensibility.
- [ ] Contract/schema casing and aliases are dispositioned.
- [ ] ValidationReport and profile schemas are accepted.

### Policy, evidence, and sources

- [ ] SourceDescriptor and source-role requirements are explicit.
- [ ] Rights and attribution are reviewable.
- [ ] Policy preflight entrypoints and defaults are tested.
- [ ] EvidenceRef resolution and EvidenceBundle admission are deterministic.
- [ ] Official-source and not-for-life-safety obligations are enforced.

### Tests and CI

- [ ] Positive and negative fixtures exist.
- [ ] No-network behavior is enforced.
- [ ] Anti-collapse cases fail for expected reason codes.
- [ ] Sensitive-output tests prevent leakage.
- [ ] Correction and expiry cases are covered.
- [ ] CI executes substantive tests and is required where intended.
- [ ] Current pass results are recorded with commit and profile digests.

### Operations and governance

- [ ] Reports and receipts write only to accepted roots.
- [ ] Metrics and incident hooks are defined without sensitive payloads.
- [ ] Release-gate adoption is separately reviewed.
- [ ] Correction, supersession, withdrawal, and rollback have tested paths.
- [ ] Deprecation and compatibility windows are documented.

[Back to top](#top)

---

<a id="migration-compatibility-and-deprecation"></a>

## Migration, compatibility, and deprecation

### Current naming posture

```text
tools/validators/air-hazards/          # documented canonical seam
tools/validators/atmosphere_hazards/   # compatibility bridge
```

This README does not itself make an accepted ADR decision. It preserves the current documented relationship and prevents parallel implementation.

### Migration options

#### Option A — retain current topology

- implement only under `air-hazards/`;
- keep `atmosphere_hazards/` as README/migration pointer;
- add tests proving no duplicate executable files;
- deprecate old references gradually.

#### Option B — rename to underscore spelling

- accept an ADR or migration note;
- move implementation and tests atomically;
- keep a compatibility pointer at the old path;
- update registries, workflows, docs, imports, and receipts;
- provide rollback to the prior path.

#### Option C — move seam under a shared joins tree

- justify responsibility and compatibility impact;
- avoid duplicating domain child validators;
- provide adapters for existing paths;
- update Directory Rules or ADR evidence if needed.

### One-active-implementation rule

At any point:

- one canonical implementation path;
- one stable CLI/package entrypoint;
- one validator profile identity;
- one report schema family;
- compatibility paths may delegate or point, but must not fork behavior.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Status | Required evidence |
|---|---|---|---|
| AH-001 | Is `air-hazards/` formally accepted as canonical, or only documented as such? | NEEDS VERIFICATION | ADR, migration record, Directory Rules decision, or steward approval. |
| AH-002 | Which path should hold the future executable? | NEEDS VERIFICATION | Accepted topology and package/CLI design. |
| AH-003 | Are any consumers already importing an unpublished entrypoint? | UNKNOWN | Complete code/import/workflow search. |
| AH-004 | Which Atmosphere object contracts are canonical amid casing and alias drift? | NEEDS VERIFICATION | Contract registry and migration notes. |
| AH-005 | Which Atmosphere schemas are active versus generated scaffolds? | NEEDS VERIFICATION | Schema registry, fixtures, validators, and review state. |
| AH-006 | What is the accepted Hazards schema home? | NEEDS VERIFICATION | Resolved ADR/schema-home decision. |
| AH-007 | Which policy packages evaluate Atmosphere/Hazards seam use? | UNKNOWN | Policy bundle manifest, entrypoints, inputs, tests, and versioning. |
| AH-008 | What source-role vocabulary is authoritative? | NEEDS VERIFICATION | Accepted contract/schema/registry enum. |
| AH-009 | What knowledge-character vocabulary is authoritative? | NEEDS VERIFICATION | Accepted contract/schema and tests. |
| AH-010 | Which SourceDescriptors are active for smoke, AOD, PM2.5, AQI, weather, advisories, and fire detections? | NEEDS VERIFICATION | Source registry records and rights reviews. |
| AH-011 | What time fields and stale thresholds apply per product? | NEEDS VERIFICATION | Freshness profile contract, policy, fixtures, and domain approval. |
| AH-012 | How are official-source redirects represented and validated? | NEEDS VERIFICATION | Contract/schema/policy and UI/API integration tests. |
| AH-013 | What EvidenceBundle admission result does the seam consume? | UNKNOWN | Resolver contract and deterministic fixtures. |
| AH-014 | What is the stable ValidationReport schema and reason-code registry? | PROPOSED | Contract, schema, fixtures, validator implementation. |
| AH-015 | Which sensitivity reviewers are required for infrastructure, people/land, habitat, rare species, and archaeology joins? | NEEDS VERIFICATION | Policy matrix and CODEOWNERS. |
| AH-016 | Where do generated reports and validation receipts live? | NEEDS VERIFICATION | Accepted artifact/receipt layout and schema. |
| AH-017 | Are domain workflows intended to become blocking? | NEEDS VERIFICATION | Workflow policy and branch-protection evidence. |
| AH-018 | What resource limits apply to geometry, rasters, references, and report findings? | NEEDS VERIFICATION | Security review and profile configuration. |
| AH-019 | How are source and model corrections propagated to released derivatives? | UNKNOWN | Dependency graph, correction workflow, and tests. |
| AH-020 | What deprecation window applies to `atmosphere_hazards/`? | NEEDS VERIFICATION | Migration plan and consumer inventory. |
| AH-021 | Is the validator used in runtime, Focus Mode, map/API release, or AI answer gates? | UNKNOWN | Code, workflow, logs, dashboards, and release records. |
| AH-022 | What are the current pass/fail results? | UNKNOWN | Executable implementation and pinned test run. |

[Back to top](#top)

---

<a id="rollback-path"></a>

## Rollback path

### Documentation-only rollback

For this README revision:

1. revert the README commit;
2. restore prior blob `beae47c4f9af375343a38057c9d054459c9ee0c2`;
3. revert or remove the paired generated provenance receipt;
4. confirm links and parent indexes still resolve.

No runtime, policy, source, evidence, release, or deployment rollback is required because this change does not alter executable behavior.

### Future implementation rollback

A future validator rollout should define:

- previous profile and executable version;
- previous policy bundle version;
- previous schema/contract baseline;
- feature flag or gate-disable mechanism;
- report/receipt compatibility strategy;
- affected release candidates and public surfaces;
- correction/withdrawal steps for invalidated outputs;
- consumer migration and compatibility window;
- incident owner and review record.

Rollback must not restore an unsafe public output merely because the previous validator accepted it.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Blob | What it supports |
|---|---|---|
| Prior requested README | `beae47c4f9af375343a38057c9d054459c9ee0c2` | Prior proposed seam scope and outcome vocabulary. |
| Compatibility bridge | `5b7ef603ccf1d330c7647a32c63e5e49a23fd672` | `atmosphere_hazards/` points to `air-hazards/` and denies duplicate logic. |
| Atmosphere validator index | `0bdf0d021a093b61cdeca0686a936cd91c1af318` | Per-domain routing and smoke child relationship. |
| Hazards validator index | `20b1f0851475cfc14aacdd3248f9ff1133595296` | Hazards object/freshness/not-for-life-safety validation posture. |
| Broad Hazards index | `c3b68e4750978fa3bc08f6617f3699a93f5663ad` | Broad versus per-domain Hazards routing. |
| Atmosphere smoke lane | `5b9ba27e27b9ccad77d495af6b310b4b8c02366a` | Smoke/AOD anti-collapse and seam specialization. |
| Freshness lane | `b2ff3fb3341f4f619b3a93fdd3a54922c5d22410` | Shared time, stale-state, expiry, correction, and rollback checks. |
| SmokeContext contract | `3ce536cd9440df2d0c07da4170baf9d32a4cbb1a` | Smoke semantic meaning and boundaries. |
| SmokeContext schema | `0069827d36b6ff94a58b333d39de3b7cf5804a97` | Permissive scaffold status. |
| Atmosphere schema index | `1165bd4719fff2c17ce4e7f5253fa8af8315f333` | Proposed schema home and incomplete indexed inventory. |
| Hazards schema index | `2e8fa3c0cd987936d0bdd07024a41c78247d02a0` | Schema-home conflict and missing concrete inventory. |
| Atmosphere policy README | `d897f4f67458f9d12e0ef2b2e7146eeba935df4b` | Greenfield policy scaffold. |
| Hazards policy README | `6118f23a6cd480494f92e8355cbfe61b19a0c25c` | Greenfield policy scaffold. |
| Atmosphere test parent | `6474cc33c3bdd668fd8713e06e94f7dacda97b6b` | Planned test responsibilities and unverified execution. |
| Atmosphere workflow | `a3c6a21db798b02202c87f76bfba5f45c5f08c9b` | TODO-only validation/proof/publish jobs. |
| Hazards workflow | `ada4e42302667488316fd0ca96137c76e1d6d4f5` | TODO-only validation/proof/publish jobs. |
| Validator root README | `e35742288404a1eeb214f8269fbacb1429c0f86a` | Validators are fail-closed checkers, not authority. |
| Directory Rules | `2affb080e6f0043867c64c7f06c1ca52030fbd55` | Responsibility-root placement and parallel-home discipline. |

### Evidence limitations

- Repository search is bounded and may miss unindexed, generated, ignored, or future files.
- README content can describe intent without proving execution.
- Workflow presence can exist without substantive commands.
- Schema presence can exist without meaningful constraints.
- No runtime logs, deployment state, dashboards, or current test execution were inspected for this documentation-only change.
- No claim is made that a public Air–Hazards product currently exists.

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

### v0.2 — 2026-07-16

- grounded the lane in current repository evidence;
- classified the direct lane as README-only;
- preserved `air-hazards/` as the documented seam and `atmosphere_hazards/` as compatibility-only;
- mapped Atmosphere, Hazards, smoke specialty, freshness, evidence, policy, release, and public-serving responsibilities;
- documented contract/schema/policy/test/CI maturity;
- added explicit not-for-life-safety and official-source requirements;
- added validation packet, report, finite outcomes, reason-code families, security controls, test matrix, CI contract, implementation sequence, definition of done, migration, open register, correction, and rollback;
- recorded evidence blobs and current verification limits.

### v0.1 — 2026-07-07

- replaced the empty file with a proposed Air–Hazards validator guide.

[Back to top](#top)
