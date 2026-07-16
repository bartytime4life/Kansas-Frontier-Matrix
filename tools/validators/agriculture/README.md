<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-agriculture-readme
title: tools/validators/agriculture/ — Agriculture Validation Profile and Compatibility Boundary
type: readme; directory-readme; agriculture-validator-profile; compatibility-boundary; non-authoritative-checker-lane
version: v0.2
status: draft; repository-grounded; README-only; no-agriculture-executable-established; validator-placement-conflicted; schema-scaffolds; policy-scaffolds; test-contracts-mostly-readme-only; ci-todo-only; sensitive-domain; non-authoritative
owners: OWNER_TBD — Agriculture steward · Validation steward · Schema steward · Contract steward · Policy steward · Source steward · Rights steward · Sensitivity/privacy reviewer · Soil steward · Hydrology steward · Atmosphere steward · Hazards steward · People/Land steward · Evidence steward · Release steward · Security steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1 proposed Agriculture validator lane guide
policy_label: "public-review; tools; validators; agriculture; broad-validation-profile; compatibility-routing; README-only; fail-closed; aggregate-public-default; field-level-deny-default; operator-privacy; rights-aware; source-role-preserving; evidence-aware; lifecycle-aware; release-gated; no-network-default; no-publication-authority; correction-aware; rollback-aware"
current_path: tools/validators/agriculture/README.md
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; tools/validators parent boundary; merged
  tools/validators/_common v0.3 runtime boundary; bounded direct-lane search returning this README only;
  parallel tools/validators/domains/agriculture parent and soil-join child READMEs; shared
  tools/validators/joins/agriculture-soil README; tools/validators/soil-suitability README;
  Agriculture domain doctrine and twelve object families; Agriculture test parent and README-backed
  schema, policy-deny, aggregate-only, catalog-closure, rollback-drill, soil-moisture, SSURGO-lineage,
  and vegetation-index lanes; Agriculture schema index drift and permissive PROPOSED schema scaffolds;
  draft Agriculture policy lane and PROPOSED Rego stubs; TODO-only domain-agriculture workflow; and
  absence of a surfaced validate_agriculture executable or AG_VALIDATION implementation / PROPOSED
  retain this directory as the broad Agriculture validation profile and compatibility boundary until
  one implementation topology is accepted; define profile identity, bounded inputs, finite outcomes,
  schema/policy/evidence/lifecycle/release checks, cross-lane delegation, no-network tests, structured
  reports, correction, migration, deprecation, and rollback / CONFLICTED broad Agriculture lane versus
  tools/validators/domains/agriculture edge-parent convention; three Agriculture-Soil routing lanes;
  Agriculture schema index versus repository inventory; permissive schema scaffolds versus conformance
  language; deny/abstain policy names versus inconsistent scaffold defaults; README-backed test
  expectations versus absent executable tests; and green/TODO workflows versus unproved enforcement /
  UNKNOWN accepted validator executable home, active profile schema, current SourceDescriptors,
  source activation records, canonical Agriculture schema set, policy query interface, fixture payloads,
  validator registry, report schema, receipt emission, CI coverage, release-gate integration,
  production consumers, operational monitoring, and runtime use / NEEDS VERIFICATION owners,
  CODEOWNERS, path/namespace ADR, exact object/schema/contract closure, source rights, sensitivity rules,
  reason-code contract, no-network fixtures, executable tests, policy enforcement, correction cascade,
  deprecation plan, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b902a5c34165ac55d2bb46b470f21e4002cf505f
  prior_blob: ba9009bdecb6e007423122c32c53fffc3559976d
  validators_parent_blob: e35742288404a1eeb214f8269fbacb1429c0f86a
  common_runtime_readme_blob: 12df3198498356b32bf309a314eb255604b37415
  domains_agriculture_readme_blob: 1c414b4d0d14ba4c433bd04654e06128387c9beb
  domains_agriculture_soil_join_blob: 6374ad7010737bed5c95156348267e04272edfaf
  joins_agriculture_soil_blob: d6f3cf61e0e5ac1fc15ae508e9168b4f25c2a3a2
  soil_suitability_blob: 802e239f6d4b1053a3bd4877a75fba90a69ed91b
  agriculture_domain_readme_blob: a2cac517ad26ea9105d46b5a7472de25cb35da2b
  agriculture_tests_parent_blob: 35ebf2a578f2a39b4f4766cc4146aafde8124e67
  agriculture_schema_test_blob: 345f667c8d1879853e80087f3609c76cf52bde06
  agriculture_policy_deny_test_blob: 07f3dcb643e49ce54bae06a17399ee3829d72d1c
  agriculture_schema_index_blob: 35d28a2c767a2e932572656c0f93727ceb18a541
  crop_observation_schema_blob: 18417141a0e2d84a52d74dc6ef680300264e3e19
  agriculture_policy_readme_blob: ba73c387e16f70895f32444e489d6d55dd577b75
  deny_unpublished_policy_blob: 35c813606f37d3578230092fc526430e256b134d
  domain_agriculture_workflow_blob: a9f5f212ef61d72fdc209d9f8b173bbf87fb1803
  direct_lane_inventory:
    - tools/validators/agriculture/README.md
related:
  - ../README.md
  - ../_common/README.md
  - ../domains/README.md
  - ../domains/agriculture/README.md
  - ../domains/agriculture/soil-join/README.md
  - ../joins/README.md
  - ../joins/agriculture-soil/README.md
  - ../soil-suitability/README.md
  - ../policy/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../evidence/README.md
  - ../lifecycle/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../docs/domains/agriculture/OBJECTS.md
  - ../../../docs/domains/agriculture/OBJECT_FAMILIES.md
  - ../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../docs/domains/agriculture/POLICY.md
  - ../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../contracts/domains/agriculture/
  - ../../../schemas/contracts/v1/domains/agriculture/README.md
  - ../../../schemas/contracts/v1/agriculture/README.md
  - ../../../policy/domains/agriculture/README.md
  - ../../../policy/sensitivity/agriculture/README.md
  - ../../../data/registry/sources/agriculture/
  - ../../../fixtures/domains/agriculture/
  - ../../../tests/domains/agriculture/README.md
  - ../../../release/candidates/agriculture/
  - ../../../.github/workflows/domain-agriculture.yml
tags: [kfm, tools, validators, agriculture, validation-profile, compatibility, aggregation, privacy, source-rights, schemas, policy, evidence, lifecycle, release, cross-lane, soil, hydrology, atmosphere, hazards, no-network, correction, rollback]
notes:
  - "This revision changes only tools/validators/agriculture/README.md; a generated provenance receipt is paired separately."
  - "No Agriculture validator executable, schema, contract, policy, fixture, test, workflow, source record, data object, receipt instance, proof, release record, runtime behavior, or public artifact is created or modified."
  - "The README records current repository conflicts and maturity without selecting a canonical validator implementation path by assertion."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/agriculture/` — Agriculture Validation Profile and Compatibility Boundary

> **One-line purpose.** Define the broad Agriculture validation contract, route specialized checks to their owning validator lanes, and prevent schema checks, policy checks, evidence checks, or validator success from becoming Agriculture truth, source authority, release approval, or public publication.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Inventory: README only" src="https://img.shields.io/badge/inventory-README__only-lightgrey">
  <img alt="Placement: conflicted" src="https://img.shields.io/badge/placement-CONFLICTED-orange">
  <img alt="Implementation: not established" src="https://img.shields.io/badge/implementation-not__established-critical">
  <img alt="Public field detail: deny" src="https://img.shields.io/badge/public__field__detail-DENY-red">
  <img alt="Default network: off" src="https://img.shields.io/badge/default__network-off-critical">
</p>

> [!IMPORTANT]
> **This direct directory is README-only in bounded repository evidence.** No `validate_agriculture*` executable, Agriculture validator registry entry, Agriculture validation profile, emitted `ValidationReport`, fixture-backed command, or substantive Agriculture validator CI is established here.

> [!CAUTION]
> **Placement is unresolved.** Broad Agriculture scope is documented here, edge-specific scope is documented under `tools/validators/domains/agriculture/`, and Agriculture × Soil concerns appear in at least three additional validator routing lanes. Do not create duplicate executable implementations while this topology remains unresolved.

> [!WARNING]
> Agriculture can expose private or rights-limited detail through fields, parcels, operators, ownership, production, yield, irrigation, pesticide/application records, or cross-lane joins. A validator must minimize error output, preserve the most restrictive posture, and deny public exact exposure unless governed aggregation, redaction, review, evidence, policy, and release controls support a narrower public-safe derivative.

**Quick links:** [Purpose](#purpose) · [Status](#current-evidence-and-maturity) · [Authority](#authority-and-placement) · [Topology](#validator-topology-and-overlap) · [Domain](#agriculture-domain-scope) · [Profile](#minimum-agriculture-validation-profile) · [Checks](#validation-families) · [Cross-lane](#cross-lane-delegation-matrix) · [Schemas](#schema-conformance-boundary) · [Policy](#policy-rights-and-sensitivity-boundary) · [Evidence](#evidence-lifecycle-and-release-boundary) · [Inputs](#minimum-input-contract) · [Outputs](#bounded-output-contract) · [Outcomes](#finite-outcomes-and-reason-codes) · [Security](#privacy-security-and-log-minimization) · [Testing](#tests-fixtures-and-ci) · [Belongs](#what-belongs-here) · [Sequence](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#maintenance-migration-correction-and-rollback) · [Ledger](#evidence-ledger)

---

## Purpose

`tools/validators/agriculture/` is the broad Agriculture validator **profile and compatibility boundary** under the `tools/validators/` responsibility root.

Its durable question is:

> Does an Agriculture candidate satisfy the declared object contract, machine shape, source identity and role, rights, privacy and sensitivity posture, evidence support, lifecycle state, cross-lane authority boundaries, policy decision, release prerequisites, correction lineage, and rollback requirements for the requested use?

The answer may be a deterministic validation result or a bounded request for review. It must not become:

- Agriculture domain truth;
- source admission or source-role authority;
- schema or semantic-contract authority;
- a policy decision by itself;
- an EvidenceBundle;
- a lifecycle promotion;
- release approval;
- field-management or agronomic advice;
- a public map, API, export, report, search result, or AI answer.

This README defines broad validation obligations and routes specialized validation. It does not establish an executable merely because the path exists.

[Back to top](#top)

---

## Current evidence and maturity

| Surface | Inspected status | Safe conclusion |
|---|---|---|
| `tools/validators/agriculture/` | **CONFIRMED README-only in bounded search** | Broad profile documentation exists; no direct executable surfaced. |
| `tools/validators/README.md` | **CONFIRMED parent contract** | Validators are fail-closed checkers, not truth or release authority. |
| `tools/validators/_common/` | **CONFIRMED working shared JSON Schema helper lane** | Shared plumbing exists; it does not establish Agriculture-specific coverage. |
| `tools/validators/domains/agriculture/` | **CONFIRMED README-only parent** | Documents edge-specific Agriculture validator routing. |
| `tools/validators/domains/agriculture/soil-join/` | **CONFIRMED README-only child** | Documents Agriculture-facing Soil join invariants; no executable established. |
| `tools/validators/joins/agriculture-soil/` | **CONFIRMED README-only shared join lane** | Shared Agriculture × Soil routing overlaps the domain child. |
| `tools/validators/soil-suitability/` | **CONFIRMED README-only derivative lane** | Suitability-specific routing overlaps Agriculture × Soil concerns. |
| Agriculture domain doctrine | **CONFIRMED repository document / draft implementation posture** | Defines twelve Agriculture object families and deny-by-default field/operator exposure. |
| Agriculture schema test lane | **CONFIRMED README-only v0.2** | Documents inventory drift and missing Agriculture-specific validator closure. |
| Agriculture policy-deny test lane | **CONFIRMED README-only v0.2** | Documents policy scaffold conflicts and TODO-only enforcement. |
| Agriculture test parent | **CONFIRMED README** | Lists eight README-backed child test lanes; executable depth remains unverified. |
| Agriculture schema index | **CONFIRMED stale/incomplete relative to repository inventory** | Index names one scaffold while bounded test research surfaced many schema files. |
| Representative `CropObservation` schema | **CONFIRMED permissive `PROPOSED` scaffold** | Empty `properties` and `additionalProperties: true`; not meaningful conformance proof. |
| Agriculture policy parent | **CONFIRMED draft** | Defines intended policy boundary; runtime enforcement remains unproved. |
| `deny_unpublished.rego` | **CONFIRMED `PROPOSED` stub** | No active deny rule; default `deny := false`. |
| `domain-agriculture` workflow | **CONFIRMED TODO-only jobs** | Green workflow status cannot prove validation, proof, or release-dry-run behavior. |
| Agriculture validator executable | **NOT SURFACED** | Do not claim a runnable Agriculture validator. |
| Agriculture validation report schema | **UNKNOWN** | No accepted structured report contract was established. |
| Production/runtime use | **UNKNOWN** | No operational consumer, monitoring, or release-gate use established. |

**Current determination:** this lane is a broad documentation contract and compatibility surface. It is not an active Agriculture validator implementation.

[Back to top](#top)

---

## Authority and placement

KFM places files by primary responsibility:

```text
docs/           Agriculture doctrine, scope, policy intent, runbooks
contracts/      Agriculture object meaning
schemas/        machine-checkable shape
policy/         allow / deny / restrict / hold / abstain decisions
tools/          reusable validator implementation
fixtures/       deterministic test data
tests/          enforceability proof
connectors/     source-specific access and admission
pipelines/      executable lifecycle orchestration
data/           lifecycle records, registry, receipts, proofs, catalogs, published artifacts
release/        promotion, correction, withdrawal, supersession, rollback
apps/           governed serving surfaces
```

### Placement test

| Question answered by a file | Owning home |
|---|---|
| What does `CropObservation` mean? | `contracts/domains/agriculture/` |
| What fields must it contain? | accepted Agriculture schema home under `schemas/` |
| Is exact field/operator exposure allowed? | `policy/` |
| How is a source fetched? | `connectors/` |
| How does a candidate move through lifecycle stages? | `pipelines/` |
| Does a candidate conform to declared requirements? | `tools/validators/` |
| Does the validator fail closed? | `tests/` with `fixtures/` |
| Where is the resulting report or receipt stored? | accepted `data/` trust-artifact lane |
| May the candidate be published? | `release/` and governed serving surfaces |

### Validator authority limit

```text
validator pass != semantic truth
validator pass != source admission
validator pass != policy allow
validator pass != evidence closure
validator pass != promotion
validator pass != publication
```

[Back to top](#top)

---

## Validator topology and overlap

### Current broad and edge lanes

```text
tools/validators/
├── agriculture/                         # this broad profile; README-only
├── domains/agriculture/                 # edge-specific parent; README-only
│   └── soil-join/                       # Agriculture-facing Soil join; README-only
├── joins/agriculture-soil/              # shared Agriculture × Soil route; README-only
└── soil-suitability/                    # derivative-specific route; README-only
```

### Current documented split

| Concern | Documented candidate lane | Status |
|---|---|---|
| Broad Agriculture validation | `tools/validators/agriculture/` | **PROPOSED profile boundary** |
| Agriculture edge-specific checks | `tools/validators/domains/agriculture/<edge>/` | **PROPOSED** |
| Shared Agriculture × Soil join checks | `tools/validators/joins/agriculture-soil/` | **PROPOSED** |
| Agriculture-facing Soil join checks | `tools/validators/domains/agriculture/soil-join/` | **PROPOSED** |
| `SoilCropSuitability` derivative checks | `tools/validators/soil-suitability/` | **PROPOSED** |

This split is described by READMEs but is not yet established by executable ownership, registry identity, imports, tests, CI, ADR, or migration record.

### One-active-implementation rule

For each validator concern there must be one active implementation owner. Other paths may:

- index;
- delegate;
- wrap without redefining behavior;
- provide a temporary compatibility shim;
- document migration.

They must not contain independent evolving rule sets, outcome vocabularies, policy assumptions, or report shapes.

### Freeze posture

Until the topology is accepted:

- do not add an executable directly here merely to satisfy the README;
- do not duplicate Soil-join logic across three lanes;
- do not create a second Agriculture validator registry id;
- do not inline policy or schema definitions into validator code;
- do not claim a lane is canonical from naming alone.

[Back to top](#top)

---

## Agriculture domain scope

Agriculture doctrine identifies twelve object families:

| Object family | Broad validator concerns |
|---|---|
| `CropObservation` | identity, source role, crop vocabulary, time, geometry/aggregation, evidence |
| `FieldCandidate` | candidate status, field precision, privacy, rights, no-public-exact posture |
| `CropRotation` | temporal ordering, field/aggregate scope, source continuity, uncertainty |
| `YieldObservation` | units, vintage, geography, confidentiality, source rights, aggregation |
| `IrrigationLink` | cross-lane Hydrology references, identity, rights, sensitivity, evidence |
| `ConservationPractice` | program/source context, time, geometry precision, rights, claims scope |
| `SoilCropSuitability` | Soil ownership, MUKEY continuity, method/version, modeled posture |
| `AgriculturalEconomyObservation` | aggregation, confidentiality, units, source terms, temporal scope |
| `SupplyChainNode` | public/private facility distinction, source role, infrastructure sensitivity |
| `DroughtStressIndicator` | modeled/derived status, Hazards/Atmosphere ownership, time, uncertainty |
| `PestStressIndicator` | indicator-not-advice, source role, uncertainty, Flora/Fauna boundaries |
| `AggregationReceipt` | transform inputs, method, public-safe output, reviewer, lineage |

The current repository does not establish full contract/schema/fixture/validator closure for these families. A validator must not infer missing rules from object names or domain prose.

[Back to top](#top)

---

## Minimum Agriculture validation profile

A future active profile should be immutable, reviewable, and consumer-bound.

```yaml
profile_id: kfm.validator.agriculture.candidate
profile_version: 1.0.0
status: draft
owner_ref: <governed owner ref>
implementation_ref: <one verified executable>
object_families:
  - CropObservation
schema_refs:
  - <accepted immutable schema ref>
contract_refs:
  - <accepted semantic contract ref>
policy_entrypoints:
  - <accepted Agriculture policy decision path>
source_descriptor_refs:
  - <admitted source descriptor ref>
fixture_set_ref: <immutable no-network fixture set>
report_schema_ref: <accepted ValidationReport profile>
allowed_operations:
  - validate_candidate
public_exact_geometry_allowed: false
promotion_authority: false
publication_authority: false
```

### Required profile fields

1. stable id and semantic version;
2. one implementation owner;
3. explicit object-family scope;
4. immutable contracts and schemas;
5. source descriptor and source-role requirements;
6. policy query entrypoints and expected outcome vocabulary;
7. evidence, lifecycle, release, correction, and rollback requirements;
8. fixture set and expected results;
9. side-effect and network posture;
10. structured report contract;
11. deprecation and supersession behavior.

A README, filename, directory, schema `$id`, or workflow name is not a profile.

[Back to top](#top)

---

## Validation families

### 1. Identity and contract pairing

Check:

- stable object id and object-family discriminator;
- Agriculture ownership or explicit external-owner reference;
- semantic contract ref;
- schema ref and version;
- source descriptor refs;
- source role and authority;
- transaction/valid/observed/retrieval times where material;
- supersession and correction lineage.

### 2. Machine shape

Check:

- JSON parsing and dialect;
- unique/stable `$id`;
- `$ref` closure;
- required fields and enums;
- format behavior;
- closed/open world posture;
- schema/contract/fixture/validator path closure;
- no duplicate canonical schema authority.

A permissive scaffold with empty `properties` cannot prove substantive Agriculture conformance.

### 3. Source and rights

Check:

- admitted `SourceDescriptor` and activation state;
- source role preserved;
- license, attribution, redistribution, confidentiality, and access terms;
- source vintage and cadence;
- source-specific caveats;
- public-use and derivative-use restrictions.

### 4. Privacy, sensitivity, and aggregation

Check:

- exact field, parcel, operator, ownership, private-party, and restricted-source exposure;
- aggregation/redaction/generalization method;
- minimum-cell and reconstruction-risk posture where governed;
- `AggregationReceipt` or `RedactionReceipt` linkage;
- requested audience and public surface;
- joined sensitivity under the most restrictive rule.

### 5. Evidence and claim support

Check:

- `EvidenceRef` resolution;
- EvidenceBundle completeness and authority;
- citation and rights linkage;
- contradiction and stale-state posture;
- claim scope versus source support;
- generated or modeled text does not substitute for evidence.

### 6. Lifecycle and release

Check:

- current lifecycle state;
- no RAW/WORK/QUARANTINE-to-public shortcut;
- validation and policy decisions match the requested transition;
- release candidate and manifest refs;
- correction, withdrawal, supersession, and rollback targets;
- public clients consume only released public-safe derivatives.

### 7. Cross-lane authority

Check that Agriculture cites rather than redefines Soil, Hydrology, Atmosphere, Hazards, People/Land, Flora, Fauna, Habitat, and Infrastructure truth.

[Back to top](#top)

---

## Cross-lane delegation matrix

| Agriculture concern | Owning lane retained | Broad Agriculture check | Specialized route |
|---|---|---|---|
| Soil map units and MUKEY | Soil | reference, role, evidence, correction linkage | Agriculture × Soil join / soil-suitability lane |
| Streamflow, water levels, flood context | Hydrology | reference, time, source role, scope | domain/cross-lane validator if accepted |
| Weather, climate, smoke, AOD | Atmosphere | reference, time, uncertainty, role | Atmosphere × Agriculture validator if accepted |
| Drought event/status | Hazards | distinguish hazard event from derived crop stress | Hazards/Agriculture cross-lane route |
| Parcel, ownership, operator, living person | People/DNA/Land | deny public exact/person-linked exposure | sensitivity/privacy policy and validator lanes |
| Plant taxonomy/rare plant context | Flora | reference only; preserve sensitivity and taxonomy authority | Flora/Agriculture cross-lane route if accepted |
| Pest organism identity | Fauna/Flora as appropriate | indicator scope, evidence, non-advice posture | domain owner validator plus Agriculture derivative check |
| Critical facilities/supply nodes | Settlements/Infrastructure | public-safe representation and source role | infrastructure-sensitive validator route |

The broad Agriculture validator should orchestrate or delegate these checks through declared profiles. It should not copy specialized rules into one monolith.

[Back to top](#top)

---

## Schema conformance boundary

Current evidence shows:

- the Agriculture schema index lists one `aggregation_receipt` scaffold;
- bounded schema research found a substantially larger Agriculture schema inventory;
- the shorter `schemas/contracts/v1/agriculture/` compatibility lane coexists with the domain lane;
- representative schemas are `PROPOSED` scaffolds;
- `crop_observation.schema.json` has empty `properties` and `additionalProperties: true`;
- the schema-specific Agriculture test lane is README-only;
- shared schema workflows do not establish Agriculture-specific coverage.

### Required validator behavior

An Agriculture validator must distinguish:

```text
schema file exists
schema parses
schema is metaschema-valid
schema resolves refs
schema discriminates valid from invalid fixtures
schema is paired with meaning
schema is accepted for the profile
candidate conforms to schema
candidate satisfies evidence/policy/release requirements
```

These are separate findings.

### Schema fail conditions

- schema ref missing or mutable;
- schema status is scaffold/stub for a consequential use;
- duplicate or conflicting `$id`;
- schema path and metadata disagree;
- paired contract missing;
- required fixture set missing;
- no invalid fixture is rejected;
- public-bound candidate validates only because the schema is permissive;
- domain schema duplicates shared release/evidence/runtime authority without accepted specialization.

[Back to top](#top)

---

## Policy, rights, and sensitivity boundary

Current Agriculture policy material is not established as production enforcement:

- the parent policy README is draft;
- inspected Rego files are marked `PROPOSED` stubs/scaffolds;
- `deny_unpublished.rego` contains no active deny rule and defaults `deny` to false;
- policy-deny tests are README-only;
- policy and Agriculture workflows use TODO commands;
- decision-envelope and outcome contracts remain unresolved.

### Validator responsibility

A validator may verify that:

- the expected policy bundle and entrypoint exist;
- policy input validates;
- policy returns an allowed finite outcome;
- reason codes and obligations validate;
- required rights/sensitivity reviews are present;
- deny/restrict/hold/abstain results block downstream paths;
- policy output does not leak protected details;
- the policy version and digest are recorded.

A validator must not invent a policy decision when policy is absent or broken.

### Default public posture

```text
aggregate public-safe Agriculture derivative = candidate for review
exact field/operator/private join             = deny by default
rights unclear                                = hold or abstain
sensitivity unclear                           = hold or abstain
policy unavailable                            = error and fail closed
unpublished candidate                         = deny public use
```

[Back to top](#top)

---

## Evidence, lifecycle, and release boundary

### Evidence

A claim-bearing Agriculture candidate requires resolvable evidence support appropriate to significance. The validator should check references and closure state, but it does not create or approve the EvidenceBundle.

### Lifecycle

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Validation is one gate in this sequence. It is not a lifecycle writer and must not move data by itself.

### Release

For public-bound output, validate:

- public-safe representation;
- evidence closure;
- policy outcome and obligations;
- validation report identity;
- artifact and manifest integrity;
- review state;
- release decision ref;
- correction path;
- rollback target;
- upstream invalidation/correction cascade.

A catalog record, valid schema, map layer, or passing validator does not imply release.

[Back to top](#top)

---

## Minimum input contract

Illustrative only; exact shape requires an accepted contract and schema.

```yaml
validation_request_id: <stable id>
profile_ref: <immutable Agriculture validator profile>
implementation_ref: <one executable version>
operation: validate_candidate
requested_surface: internal_review
candidate_ref: <immutable candidate>
object_family: CropObservation
contract_ref: <semantic contract>
schema_ref: <machine schema>
source_descriptor_refs: []
evidence_refs: []
policy_input_ref: <bounded policy input>
lifecycle_state: WORK
release_ref: null
correction_refs: []
rollback_ref: null
network_allowed: false
```

### Input rules

- resolve repository-relative paths from an explicit root;
- do not scan arbitrary directories for “likely” schemas or policies;
- do not infer source role from provider name or filename;
- do not accept hidden ambient activation or release state;
- reject unsupported object families and operations;
- cap file count, byte size, nesting, references, and error volume;
- use opaque refs for sensitive inputs where practical.

[Back to top](#top)

---

## Bounded output contract

A future machine result should separate mechanics from governance.

```yaml
validation_report_id: <stable id>
profile_ref: <immutable profile>
implementation_ref: <version/digest>
request_ref: <validation request>
outcome: NEEDS_REVIEW
reason_codes:
  - AG_SCHEMA_PROFILE_UNRESOLVED
findings: []
validated_refs: []
missing_refs: []
policy_decision_ref: null
evidence_status: unresolved
lifecycle_effect: none
promotion_authorized: false
publication_authorized: false
review_required: true
correction_refs: []
rollback_ref: null
```

### Output rules

- deterministic ordering;
- bounded and redacted findings;
- JSON Pointer or safe object path where useful;
- no raw sensitive values in messages;
- no policy or release authority claims;
- explicit `lifecycle_effect: none` unless a separate governed writer acts;
- input/profile/implementation hashes;
- machine-readable finite outcome plus safe human summary.

[Back to top](#top)

---

## Finite outcomes and reason codes

### Outcome vocabulary

| Outcome | Meaning |
|---|---|
| `PASS` | All checks in the accepted profile passed for the declared scope. |
| `FAIL` | One or more deterministic conformance checks failed. |
| `DENY` | A governed policy or public-boundary condition prohibits the requested use. |
| `RESTRICT` | Use may proceed only under explicit obligations. |
| `HOLD` | A required review, evidence, rights, policy, release, or correction dependency is pending. |
| `QUARANTINE` | Candidate must be isolated pending resolution. |
| `ABSTAIN` | Available support is insufficient to decide safely. |
| `NEEDS_REVIEW` | Human/steward interpretation is required. |
| `ERROR` | Validation machinery failed; no unsafe fallback is allowed. |

### Reason-code families

```text
AG_PROFILE_MISSING
AG_IMPLEMENTATION_UNRESOLVED
AG_OBJECT_FAMILY_UNSUPPORTED
AG_CONTRACT_MISSING
AG_SCHEMA_MISSING
AG_SCHEMA_SCAFFOLD_INSUFFICIENT
AG_SCHEMA_ID_CONFLICT
AG_SCHEMA_REF_UNRESOLVED
AG_FIXTURE_COVERAGE_MISSING
AG_SOURCE_DESCRIPTOR_MISSING
AG_SOURCE_ACTIVATION_MISSING
AG_SOURCE_ROLE_MISSING
AG_SOURCE_ROLE_COLLAPSE
AG_RIGHTS_UNRESOLVED
AG_SENSITIVITY_UNRESOLVED
AG_FIELD_LEVEL_PUBLIC_DENIED
AG_OPERATOR_JOIN_PUBLIC_DENIED
AG_AGGREGATION_RECEIPT_MISSING
AG_REDACTION_RECEIPT_MISSING
AG_CROSS_LANE_AUTHORITY_COLLAPSE
AG_MUKEY_MISSING
AG_MUKEY_UNRESOLVED
AG_EVIDENCE_REF_MISSING
AG_EVIDENCE_UNRESOLVED
AG_POLICY_BUNDLE_MISSING
AG_POLICY_DECISION_UNRESOLVED
AG_LIFECYCLE_VIOLATION
AG_RELEASE_REFERENCE_MISSING
AG_ROLLBACK_TARGET_MISSING
AG_UPSTREAM_CORRECTION_PENDING
AG_PUBLIC_SURFACE_DENIED
AG_SYSTEM_ERROR
```

Shared reason codes should be reused where accepted. Agriculture-specific codes must not redefine shared meanings.

[Back to top](#top)

---

## Privacy, security, and log minimization

Validators may process sensitive Agriculture candidates even when they never publish them.

### Do not expose in default output

- exact private field or parcel geometry;
- operator or living-person identity;
- ownership/person joins;
- proprietary yield or production values;
- pesticide/application detail;
- restricted source excerpts;
- credentials, signed URLs, tokens, or private endpoints;
- hidden redaction/generalization thresholds;
- reconstruction hints from differencing or small cells.

### Safe logging posture

Prefer:

- validation request id;
- object family;
- profile and implementation refs;
- bounded reason codes;
- JSON Pointer without raw value;
- counts with suppression where required;
- opaque evidence/policy/release refs;
- reviewer route.

### Resource safety

An implementation should define limits for:

- input bytes and file count;
- JSON depth and array length;
- schema and `$ref` count;
- regex/format behavior;
- error count and message length;
- processing time and memory;
- path traversal and symlink handling;
- network access, which defaults to off.

[Back to top](#top)

---

## Tests, fixtures, and CI

### Current test surface

The Agriculture test parent indexes:

```text
aggregate_only/
catalog_closure/
policy_deny/
rollback_drill/
schema/
soil_moisture/
ssurgo_lineage/
veg_index/
```

These are README-backed lanes. Current evidence does not establish executable Agriculture test modules in those paths.

### Required test families

| Test family | Required proof |
|---|---|
| Profile loading | Missing, malformed, superseded, and unknown profiles fail closed. |
| Schema | Valid fixtures pass; invalid fixtures fail for expected reasons; permissive scaffolds cannot masquerade as active coverage. |
| Contracts | Object family and semantic contract pairing remain explicit. |
| Sources | Missing descriptors, roles, activation, rights, vintage, or citation fail safely. |
| Aggregation/privacy | Exact field/operator/private joins cannot reach public-bound outputs. |
| Cross-lane | Neighboring-domain identity, source role, and evidence remain intact. |
| Evidence | Missing, stale, contradicted, withdrawn, or insufficient support blocks claim-bearing use. |
| Policy | Allow/deny/restrict/hold/abstain/error semantics and obligations are enforced. |
| Lifecycle | RAW/WORK/QUARANTINE cannot bypass required states. |
| Release | Missing manifest, review, correction, or rollback blocks public use. |
| Output | Findings are deterministic, structured, bounded, and redacted. |
| No-network | Default unit and CI runs cannot reach live sources. |
| Correction | Upstream changes invalidate or re-review dependent outputs. |
| Rollback | Previous validator/profile version can be restored without dual authority. |

### Fixture posture

Fixtures must be synthetic or appropriately minimized, deterministic, no-network, and paired with explicit expected outcomes. Do not use real operator identities, private polygons, confidential statistics, credentials, or restricted source material.

### CI status

The current `domain-agriculture` workflow contains TODO echo jobs. It does not prove validator execution, policy enforcement, proof building, or publish-dry-run behavior.

Substantive CI should:

1. install pinned dependencies;
2. run profile/schema/contract integrity checks;
3. execute valid and invalid Agriculture fixtures;
4. run policy deny/restrict/abstain tests;
5. prove public-boundary denial;
6. emit structured reports/artifacts;
7. fail on missing coverage or ambiguous outcomes;
8. preserve no-network defaults.

[Back to top](#top)

---

## What belongs here

Allowed now:

- this README;
- compatibility and migration notes;
- broad Agriculture validation profile documentation;
- public-safe outcome/reason-code documentation;
- pointers to specialized validators, tests, fixtures, contracts, schemas, policy, evidence, and release gates.

Allowed after topology and implementation approval:

- one broad Agriculture validator entrypoint that delegates to accepted specialized checks;
- profile loader and Agriculture-specific orchestration that uses `_common` without copying it;
- Agriculture-specific report assembly;
- bounded validators that truly span broad Agriculture concerns and do not belong in a child edge lane;
- compatibility shims that forward to one canonical implementation.

Every code-bearing file requires direct tests, explicit side effects, stable profile identity, structured output, and rollback.

[Back to top](#top)

---

## What does not belong here

| Item | Correct home |
|---|---|
| Shared JSON Schema resolver/runner | `tools/validators/_common/` or accepted shared package after migration |
| Edge-specific Agriculture validators | accepted `tools/validators/domains/agriculture/<edge>/` convention |
| Shared Agriculture × Soil join validator | accepted join-validator lane |
| Suitability-specific validator | accepted suitability-validator lane |
| Agriculture doctrine | `docs/domains/agriculture/` |
| Semantic contracts | `contracts/domains/agriculture/` |
| JSON Schemas | accepted Agriculture schema home under `schemas/` |
| Policy rules and decisions | `policy/` and accepted decision-record homes |
| Source descriptors and activation records | accepted registry/control-plane homes |
| Fixtures | `fixtures/` |
| Tests | `tests/` |
| Lifecycle payloads | governed `data/` lifecycle roots |
| ValidationReport instances, receipts, proofs | accepted `data/` trust-artifact homes |
| Release, correction, withdrawal, rollback records | `release/` |
| Connector or pipeline implementation | `connectors/`, `pipelines/` |
| Public map/API/UI/export/search/AI code | governed application/runtime roots |
| Secrets, private Agriculture records, exact protected geometry | denied from this directory |

[Back to top](#top)

---

## Smallest sound implementation sequence

1. **Keep this direct lane documentation-only.**
2. **Inventory all Agriculture validator-shaped paths, scripts, imports, schemas, policies, fixtures, tests, and workflows.**
3. **Accept one validator topology** for broad, edge, join, and derivative checks.
4. **Define one Agriculture validation-profile contract and stable id grammar.**
5. **Select one credible thin slice**, preferably aggregate/public-safe and no-network.
6. **Reconcile one object family's contract and schema.**
7. **Create valid and invalid synthetic fixtures.**
8. **Implement one validator using shared `_common` plumbing.**
9. **Add rights, sensitivity, evidence, lifecycle, and policy negative cases.**
10. **Emit a structured bounded report.**
11. **Wire substantive CI and reviewer ownership.**
12. **Exercise correction and rollback.**
13. **Migrate or retire duplicate validator lanes with compatibility pointers.**

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Direct lane is classified as README-only.
- [x] Broad versus edge/join/derivative placement conflict is visible.
- [x] Current schema, policy, tests, and CI maturity is bounded.
- [x] Authority, privacy, lifecycle, evidence, release, correction, and rollback boundaries are explicit.

### Topology and ownership

- [ ] Canonical broad Agriculture validator home is accepted.
- [ ] Edge, join, and derivative delegation rules are accepted.
- [ ] One active implementation exists per concern.
- [ ] Owners and CODEOWNERS are enforced.
- [ ] Duplicate lanes have migration/deprecation plans.

### Contract closure

- [ ] Agriculture validation-profile schema is accepted.
- [ ] Structured result/report contract is accepted.
- [ ] Reason-code vocabulary is versioned.
- [ ] One Agriculture object family has contract/schema/fixture/validator closure.
- [ ] Source, rights, sensitivity, evidence, policy, lifecycle, release, correction, and rollback refs are explicit.

### Enforceability

- [ ] Valid and invalid fixtures exist.
- [ ] No-network tests pass.
- [ ] Field/operator public-deny tests pass.
- [ ] Cross-lane authority tests pass.
- [ ] Structured output and redaction tests pass.
- [ ] Substantive CI runs and blocks unsafe changes.
- [ ] Correction and rollback drills pass.

Until these close: **broad Agriculture validation documentation boundary; no active validator established**.

[Back to top](#top)

---

## Open verification register

| ID | Item | Status |
|---|---|---|
| AG-VAL-01 | Assign Agriculture validator, schema, policy, privacy, evidence, and release owners. | NEEDS VERIFICATION |
| AG-VAL-02 | Resolve `agriculture/` versus `domains/agriculture/` ownership. | NEEDS VERIFICATION |
| AG-VAL-03 | Resolve the three Agriculture × Soil validator routes. | NEEDS VERIFICATION |
| AG-VAL-04 | Inventory all Agriculture validator executables and consumers. | NEEDS VERIFICATION |
| AG-VAL-05 | Establish validation-profile identity and schema. | NEEDS VERIFICATION |
| AG-VAL-06 | Reconcile canonical Agriculture schema inventory and alias lanes. | NEEDS VERIFICATION |
| AG-VAL-07 | Complete contract/schema pairing for the twelve object families. | NEEDS VERIFICATION |
| AG-VAL-08 | Define active SourceDescriptors and source-role requirements. | NEEDS VERIFICATION |
| AG-VAL-09 | Verify source rights, licensing, attribution, and confidentiality. | NEEDS VERIFICATION |
| AG-VAL-10 | Harmonize Agriculture policy entrypoints, defaults, outcomes, and reason codes. | NEEDS VERIFICATION |
| AG-VAL-11 | Define field/operator/privacy and aggregation/redaction controls. | NEEDS VERIFICATION |
| AG-VAL-12 | Establish EvidenceRef/EvidenceBundle validation contract. | NEEDS VERIFICATION |
| AG-VAL-13 | Define lifecycle, catalog, release, correction, and rollback checks. | NEEDS VERIFICATION |
| AG-VAL-14 | Create synthetic valid/invalid fixture matrix. | NEEDS VERIFICATION |
| AG-VAL-15 | Implement direct executable tests and no-network enforcement. | NEEDS VERIFICATION |
| AG-VAL-16 | Define structured validation report and receipt destinations. | NEEDS VERIFICATION |
| AG-VAL-17 | Wire substantive CI and branch-protection significance. | NEEDS VERIFICATION |
| AG-VAL-18 | Define log minimization and security/resource limits. | NEEDS VERIFICATION |
| AG-VAL-19 | Add monitoring, correction propagation, and rollback drills. | NEEDS VERIFICATION |
| AG-VAL-20 | Deprecate duplicate lanes without losing history or consumers. | NEEDS VERIFICATION |

[Back to top](#top)

---

## Maintenance, migration, correction, and rollback

### Maintenance triggers

Update this README when:

- an Agriculture validator executable is added, removed, renamed, or moved;
- a profile, object family, schema, contract, policy entrypoint, fixture, test, report, or reason code changes;
- source rights or sensitivity posture changes;
- a cross-lane validator is accepted or retired;
- CI, release-gate, correction, or rollback behavior changes;
- duplicate Agriculture validator lanes are reconciled.

### Migration discipline

A topology migration must:

1. inventory histories, imports, commands, workflows, docs, profiles, and consumers;
2. classify every file by primary responsibility;
3. select one active implementation per concern;
4. preserve history and stable ids where practical;
5. add an ADR or migration note when compatibility/authority changes;
6. provide time-bounded forwarding shims only where needed;
7. prevent dual execution and dual report emission;
8. update tests, fixtures, CI, CODEOWNERS, reports, and runbooks;
9. declare deprecation/removal dates;
10. prove rollback.

### Correction

When validator behavior or documentation is wrong:

- preserve prior version and affected report ids;
- identify impacted candidates/releases;
- correct profile/code/schema/policy/fixture through review;
- replay deterministically;
- issue correction/withdrawal records where downstream artifacts were affected;
- update this README and the verification register.

### Documentation rollback for this revision

Before merge, close the review branch. After merge, revert the documentation/receipt commits or restore prior README blob `ba9009bdecb6e007423122c32c53fffc3559976d` through a reviewed branch. No validator runtime, policy, schema, lifecycle, release, or public rollback is required because this revision changes documentation only.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Supports | Does not prove |
|---|---|---|
| Target README v0.1 | Prior broad Agriculture validator intent. | Executable Agriculture validation. |
| Bounded direct-path search | Direct lane surfaced as README-only. | Exhaustive Git tree absence. |
| Validator parent README | Fail-closed validator authority boundary. | Agriculture-specific coverage. |
| `_common` v0.3 | Working shared JSON Schema resolver/runner infrastructure. | Agriculture profile or schema coverage. |
| `domains/agriculture` README | Proposed edge-specific split. | Accepted topology or executable parent. |
| Soil-join and suitability READMEs | Overlapping proposed specialized concerns. | One canonical implementation. |
| Agriculture domain README | Twelve object families and deny-by-default sensitive posture. | Current implementation closure. |
| Agriculture tests parent | Eight README-backed intended test lanes. | Executable tests or current pass state. |
| Agriculture schema test README | Schema inventory drift and missing coverage. | Accepted canonical schema inventory. |
| Agriculture policy-deny test README | Policy/default/outcome conflicts and TODO enforcement. | Active policy runtime. |
| Agriculture schema index | Draft schema-lane intent and one indexed scaffold. | Complete repository inventory. |
| `crop_observation.schema.json` | Representative permissive scaffold. | Meaningful object conformance. |
| Agriculture policy README | Intended Agriculture policy boundary. | Production policy enforcement. |
| `deny_unpublished.rego` | Confirmed proposed stub and current default. | Deny behavior. |
| `domain-agriculture` workflow | Pull-request workflow names and TODO jobs. | Validation, proof, or release enforcement. |

[Back to top](#top)

---

## Changelog

| Version | Date | Change | Status |
|---|---|---|---|
| v0.1 | 2026-07-07 | Replaced an empty file with a proposed broad Agriculture validator guide. | Superseded |
| v0.2 | 2026-07-16 | Grounded the lane as README-only; surfaced broad/edge/join/suitability overlap; incorporated current schema, policy, test, and workflow maturity; added profile, validation-family, cross-lane, privacy, structured-output, CI, migration, correction, and rollback contracts. | Draft / repository-grounded |

---

> **Final rule:** Agriculture validation may report whether declared checks passed for a bounded request. It cannot turn a permissive schema, scaffold policy, README, map, model, or generated summary into evidence-backed, rights-cleared, policy-approved, released public truth.

[Back to top](#top)
