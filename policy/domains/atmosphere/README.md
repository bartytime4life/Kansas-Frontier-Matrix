<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/domains/atmosphere
title: Atmosphere Domain Policy Boundary README
type: readme; directory-readme; domain-policy-boundary; policy-source-index; maturity-and-activation-guardrail
version: v0.3
status: draft; repository-grounded; proposed-rule-scaffolds-only; evaluator-unbound; bundle-unaccepted; non-release; non-publication; not-for-life-safety
owners: "@bartytime4life — verified CODEOWNERS review route; Atmosphere, policy, directory-governance, source-rights, sensitivity/privacy, contract/schema, validator/test, runtime, release, security, and public-surface stewardship assignments NEEDS VERIFICATION"
created: 2026-05-08
updated: 2026-08-13
supersedes: unversioned greenfield scaffold
policy_label: restricted-review; policy; atmosphere; proposed; fail-closed-integration; no-active-bundle; no-public-authority; not-emergency-alerting
current_path: policy/domains/atmosphere/README.md
owning_root: policy/
boundary_profile: BOUNDARY_COMPACT
responsibility: >
  Directory boundary and complete direct inventory for Atmosphere-specific policy source. It
  distinguishes thirteen proposed default-only Rego scaffolds from accepted policy, records the
  input, decision, bundle, evaluator, validation, rights, sensitivity, release, correction, and
  public-serving boundaries needed before activation, and prevents rule-source presence from being
  mistaken for evidence, approval, release, publication, regulatory guidance, or life-safety authority.
truth_posture: >
  CONFIRMED accepted ADR-0029 directory-placement authority and canonical singular policy root;
  verified CODEOWNERS review route; complete fourteen-blob direct lane consisting of this README
  and thirteen PROPOSED Rego files; two files expose only `default deny := false`, eleven expose
  only `default allow := false`, and none contains an operative rule body beyond package/default
  declarations and comments; eleven generated-style packages and two `kfm.atmosphere_*` packages;
  duplicate or near-duplicate advisory, AOD/PM2.5, and model/observation concepts; no native
  Atmosphere Rego test, accepted bundle payload, evaluator binding, or implemented policy runtime;
  mixed adjacent validation with ten substantive and ten placeholder validator modules, seven
  substantive and eight placeholder Python test modules, and seven relevant no-network workflows /
  PROPOSED this directory as the preferred Atmosphere policy-source lane; one accepted package,
  entrypoint, input, normalized decision, reason/obligation, immutable bundle, selector, evaluator,
  correction, and rollback chain; policy behavior preserving knowledge character, source role,
  rights, sensitivity, time, and official-authority boundaries /
  CONFLICTED mixed `allow` and `deny` result relations; mixed package namespaces; overlapping rule
  names; human decision-envelope semantics versus a minimal proposed machine schema and placeholder
  validator/test; `air` versus `atmosphere` namespace drift across multiple roots; documentation
  whose maturity claims are not uniformly current /
  UNKNOWN accepted entrypoint, active bundle manifest, bundle digest, selector, evaluator,
  authenticated decision emission, production consumer, required-check significance, deployment,
  promotion integration, monitoring, and public-surface enforcement /
  NEEDS VERIFICATION functional steward assignments, source-specific rights and freshness rules,
  exact-station generalization, low-cost-sensor caveat/correction requirements, complete consumer
  inventory, obligation handlers, correction propagation, cache invalidation, and rollback drills.
responsibility_signature:
  owns: Atmosphere-specific admissibility rule source and this directory boundary
  receives: governed input references and context through an accepted evaluator contract
  produces: proposed rule source today; evaluator-native results only after accepted activation
  must_not_own: domain semantics, schemas, evidence, source payloads, runtime, release, publication, or public presentation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9fa82de35cb665840a071013fb5f1813fcc05a6a
  complete_tree: 61336b5a672cc6f0da8fa37e1450917dc4842e67
  direct_lane_tree: 95edfb6f423bb53e3e620d1832758054b309ec30
  prior_blob: d897f4f67458f9d12e0ef2b2e7146eeba935df4b
  policy_root_blob: 6c5021f9d92778581a4e9331a9dd6ddb7efc5e35
  policy_domains_parent_blob: ed9be975c9da2c7d77d94fab621db39f23953813
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  policy_input_profile_blob: 3af1c2c8d525f60f6e2aac89c5a0455898d77768
  decision_semantics_profile_blob: 2df81c2498735de07f8d05fb0c14ee28be558c12
  decision_vocabulary_blob: 51158caefd7b440851fb37489c511a5c710bed2b
  reviewer_roles_blob: 41c438ff318a6764070bbedf69fd1b45ee41cf75
  atmosphere_decision_envelope_contract_blob: e68e33e08bc9e2ea0373ecd07f471d8f8ea24d69
  atmosphere_decision_envelope_schema_blob: 28b217bb32b4a7d8935dc76715ad2f3a7eee2c47
  atmosphere_tests_readme_blob: 29204b56a1e35ff74ba8a2e33bd8a424175e9dab
  atmosphere_validators_readme_blob: 64680d31a964d4052b4cf444700982a9d3a9e579
  domain_atmosphere_workflow_blob: fccba4b6e2cdae561ec8a4904446ed5dbe6ec8ce
  policy_runtime_core_blob: e7e14cf39ae6919fbbc80f1b471de6b907292edb
  policy_bundles_readme_blob: 0a13a9c9beddfa764d47e5dd6a2ea7ef91bf0d53
  air_policy_readme_blob: 9369c8cb418e6bd656924a644f82a31558c6446e
  air_policy_readme_receipt_blob: 05bec52fa749e7f048909accec7ba1010d7caf61
related:
  - ../README.md
  - ../../README.md
  - ../air/README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/SENSITIVITY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../contracts/domains/atmosphere/README.md
  - ../../../contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json
  - ../../../tests/domains/atmosphere/README.md
  - ../../../tools/validators/domains/atmosphere/README.md
  - ../../../pipeline_specs/atmosphere/README.md
  - ../../../pipelines/domains/atmosphere/README.md
  - ../../../contracts/policy/policy_input_bundle_profile_v1.md
  - ../../../contracts/policy/policy_decision_vocabulary.md
  - ../../../contracts/policy/policy_decision_semantics_profile_v1.md
  - ../../../contracts/policy/policy_reviewer_role_vocabulary.md
  - ../../decision/vocabulary.v1.json
  - ../../decision/reviewer_roles.v1.json
  - ../../bundles/README.md
  - ../../../packages/policy-runtime/README.md
  - ../../../data/registry/sources/atmosphere/README.md
  - ../../../data/proofs/atmosphere/README.md
  - ../../../release/candidates/atmosphere/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/doctrine/ai-build-operating-contract.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../control_plane/root_registry.yaml
  - ../../../control_plane/domain_lane_register.yaml
  - ../../../.github/workflows/policy-test.yml
  - ../../../.github/workflows/domain-atmosphere.yml
tags:
  - kfm
  - policy
  - atmosphere
  - air-quality
  - weather
  - smoke
  - aod
  - climate
  - source-role
  - knowledge-character
  - anti-collapse
  - rights
  - sensitivity
  - freshness
  - exact-station-generalization
  - low-cost-sensor
  - advisory-not-alert
  - no-network
  - finite-outcomes
  - release-gated
  - correction
  - rollback
notes:
  - "This revision changes only policy/domains/atmosphere/README.md."
  - "No Rego or YAML rule, policy value, numeric threshold, bundle, evaluator, schema, contract, fixture, test, validator, workflow, source record, lifecycle object, proof, release artifact, deployment, alias, or public behavior is created or changed."
  - "No separate generated receipt is added because the requested change remains a one-file documentation update; the pull request remains draft for human review."
  - "File presence, a proposed default, a passing fixture workflow, and documentation metadata are not policy activation, approval, proof, release, or publication."
  - "Main advanced during authoring only through merged PR #2716: the separate Air compatibility README and its generated receipt. This target and all other inspected inventories remained unchanged, and the snapshot was re-pinned."
  - "KFM is not an AQI, medical, regulatory, emergency-alerting, or life-safety issuing authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Domain Policy Boundary

> **One-line purpose.** Govern the repository boundary for Atmosphere-specific admissibility rules while making clear that thirteen default-only Rego scaffolds do not yet form an accepted, bundled, evaluated, or publicly authoritative policy system.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.3" src="https://img.shields.io/badge/version-v0.3-informational">
  <img alt="Authority: proposed source" src="https://img.shields.io/badge/authority-proposed__source-orange">
  <img alt="Direct lane: fourteen blobs" src="https://img.shields.io/badge/direct__lane-14__blobs-blue">
  <img alt="Rules: thirteen stubs" src="https://img.shields.io/badge/rules-13__stubs-orange">
  <img alt="Native Rego tests: none" src="https://img.shields.io/badge/native__Rego__tests-none-critical">
  <img alt="Bundle: inactive" src="https://img.shields.io/badge/bundle-inactive-critical">
  <img alt="Runtime: unimplemented" src="https://img.shields.io/badge/runtime-unimplemented-critical">
</p>

> [!IMPORTANT]
> **This is the preferred Atmosphere policy-source lane, not proof of active policy.** The directory owns proposed Atmosphere-specific admissibility source and boundary documentation. It does not own domain semantics, schemas, evidence, source payloads, runtime evaluation, lifecycle state, release, publication, or presentation.

> [!CAUTION]
> **The current files cannot safely be activated as a set.** Eleven packages expose only `allow := false`; two expose only `deny := false`; package namespaces differ; several concepts overlap; and no accepted entrypoint, result adapter, native Rego test suite, immutable bundle, selector, or evaluator was verified.

> [!WARNING]
> **KFM is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority.** An Atmosphere policy result, fixture check, map layer, badge, README, or generated receipt must never be presented as official guidance or an emergency instruction.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Boundary](#repository-fit-and-responsibility-boundary) · [Belongs](#what-belongs-here) · [Inventory](#direct-rule-source-inventory) · [Doctrine](#atmosphere-policy-spine) · [Inputs](#inputs) · [Outputs](#outputs) · [Decisions](#decision-normalization-boundary) · [Bundles](#bundle-evaluator-and-activation-boundary) · [Validation](#validation) · [Review](#review-burden) · [Lifecycle](#release-correction-and-rollback) · [Related](#related-folders) · [Conflicts](#conflict-register) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Purpose

`policy/domains/atmosphere/` is the proposed source boundary for Atmosphere-specific admissibility decisions. Its durable question is:

> Given a governed request and explicit Atmosphere context, which operation may proceed, must be denied, should receive no policy answer, or cannot be evaluated—and which obligations must survive into every downstream consumer?

### In scope

- Atmosphere-specific allow, deny, restrict, hold, and abstention conditions after their contracts are accepted;
- safeguards for source role, knowledge character, rights, sensitivity, freshness, and audience;
- guards against presenting AQI as concentration, AOD as surface PM2.5, or modeled context as observation;
- low-cost-sensor caveat, correction, confidence, and limitation requirements;
- advisory-versus-alert and official-authority boundaries;
- deterministic rule-source inventory, package, entrypoint, bundle, evaluator, correction, and rollback documentation;
- links to governing semantics, machine shapes, evidence, validation, workflow, lifecycle, and public-serving surfaces.

### Out of scope

- scientific or domain-semantic authority;
- source discovery, acquisition, transformation, or payload storage;
- contract or JSON Schema ownership;
- EvidenceBundle, receipt, or proof creation;
- release, deployment, publication, correction, withdrawal, or rollback execution;
- API, UI, MapLibre, export, report, or AI implementation;
- regulatory determination, health advice, emergency alerting, or life-safety direction;
- activation by filename, directory presence, default declaration, or documentation assertion.

### Non-goals

This README does not:

1. accept the thirteen Rego files;
2. choose between the current `allow` and `deny` result relations;
3. resolve duplicate concepts or package namespaces;
4. activate a bundle, evaluator, selector, alias, workflow, or public consumer;
5. certify adjacent tests, validators, fixtures, contracts, schemas, or workflows;
6. establish a numeric threshold or scientific interpretation;
7. assign functional stewards from CODEOWNERS routing;
8. promote, release, deploy, publish, correct, withdraw, or roll back an artifact.

[Back to top](#top)

---

## Authority level

**Draft directory boundary / proposed policy-source index / no runtime, release, publication, or official-issuing authority.**

[ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) accepts Directory Rules v2 as repository placement authority. The [`root_registry`](../../../control_plane/root_registry.yaml) assigns the singular `policy/` root normative allow, deny, hold, restrict, and abstain rules and prohibits data instances, release decisions, and schemas here. Those accepted placement rules do not accept this domain's policy behavior or activate these files.

### Governing order

When artifacts disagree, apply the most recent accepted authority in this order:

1. KFM core invariants and accepted operating law;
2. accepted ADRs and Directory Rules;
3. accepted Atmosphere semantic, source, rights, sensitivity, and public-serving doctrine;
4. accepted contracts, schemas, policy vocabularies, bundles, and evaluator profiles;
5. released artifacts and their correction or rollback records;
6. this README;
7. proposed Rego, examples, fixtures, workflow profiles, and scaffolds.

A lower-ranked artifact cannot weaken a higher-ranked denial, restriction, attribution, sensitivity, evidence, review, release, correction, or rollback requirement.

### Authority map

| Concern | Authority home | This directory's role |
|---|---|---|
| Atmosphere meaning and object families | [`docs/domains/atmosphere/`](../../../docs/domains/atmosphere/README.md) and accepted semantic contracts | Consume references; do not redefine |
| Machine shapes | `schemas/` | Consume accepted version; do not embed schemas |
| Source identity, role, rights, and cadence | Governed source registry | Require explicit context; never invent it |
| Evidence and proof | EvidenceRef, EvidenceBundle, receipt, and proof families | Require and preserve references; never manufacture closure |
| Atmosphere admissibility source | This lane after acceptance | Own rule source, not evaluator state |
| Bundle and evaluator | Accepted bundle/runtime boundaries | Supply accepted source to one immutable binding |
| Tests and validators | `tests/` and `tools/validators/` | Require policy-native and integration evidence |
| Pipelines | `pipeline_specs/` and `pipelines/` | No acquisition or transformation role |
| Release, correction, withdrawal, rollback | `release/` and governed records | Constrain operations; execute none |
| API, UI, map, report, export, AI | Governed application surfaces | Produce no public output directly |
| CI | `.github/workflows/` | Evidence of declared checks, never activation by itself |

### Ownership boundary

[`.github/CODEOWNERS`](../../../.github/CODEOWNERS) routes `/policy/` review to `@bartytime4life`. That is **CONFIRMED review routing**, not proof that the same person holds every Atmosphere, evidence, source-rights, sensitivity, security, runtime, release, or publication role. Functional stewardship and separation of duties remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

## Status

**PROPOSED rule-source lane; direct inventory complete; implementation, activation, and production enforcement unproved.**

All counts below are complete for the untruncated repository tree at `main@9fa82de35cb665840a071013fb5f1813fcc05a6a`. They describe tracked state, not deployed state.

### Direct lane

`policy/domains/atmosphere/` contains exactly fourteen tracked blobs:

~~~text
policy/domains/atmosphere/
├── README.md
├── abstain_on_ambiguous.rego
├── advisory-not-alert.rego
├── advisory_no_life_safety.rego
├── aod-not-pm25.rego
├── aod_is_not_pm25.rego
├── aqi_is_not_concentration.rego
├── deny_unpublished.rego
├── dryrun_no_live_fetch.rego
├── freshness_gate.rego
├── low_cost_sensor_caveats_required.rego
├── model-as-observed-deny.rego
├── model_is_not_observation.rego
└── source_role_required.rego
~~~

### Maturity matrix

| Surface | Pinned inventory | Maturity | Safe claim |
|---|---:|---|---|
| This direct lane | 14 blobs | 1 README + 13 PROPOSED default-only Rego scaffolds | Source intent exists; active policy does not |
| Native Atmosphere Rego tests | 0 | Absent | No rule-level execution proof |
| Atmosphere Python tests | 16 Python files | 7 substantive + 8 placeholder modules + empty `__init__` | Bounded adjacent behavior is partly executable |
| Atmosphere validator modules | 20 | 10 substantive + 10 placeholders | Bounded fixture validation exists; broad validation does not |
| Relevant no-network workflows | 7 | Mixed bounded profiles and explicit holds | Declared fixture execution; no policy activation |
| Atmosphere decision envelope | Human draft + minimal proposed schema + placeholder validator/test | Misaligned | Semantic intent exists; machine enforcement does not |
| `policy/bundles/` | Documentation + one inactive proposed profile | Documentation only | No accepted Atmosphere bundle payload |
| Policy runtime core | Comment-only placeholder | Unimplemented | No evaluator |
| Atmosphere release candidate lane | README only | Non-release | No released candidate |
| `policy/domains/air/` | Compatibility documentation lane | Namespace drift remains | Must not become a second source |

### Evidence boundary

This README establishes tracked path presence, inspected file content, and the stated scope of checked-in workflows. It cannot establish:

- deployed policy selection or production enforcement;
- branch protection or required-check significance;
- complete off-repository consumers;
- scientific, medical, regulatory, or legal correctness;
- live-source rights, authorization, currentness, or availability;
- accepted functional steward assignments;
- EvidenceBundle or ProofPack validity;
- promotion, release, deploy, publication, correction, or rollback completion.

Those claims remain `UNKNOWN` or `NEEDS VERIFICATION` until direct evidence closes them.

[Back to top](#top)

---

## Repository fit and responsibility boundary

The accepted responsibility root is `policy/`. The Atmosphere segment is listed in the proposed machine domain-lane projection and the draft human register. The machine register also records unresolved `air: atmosphere` alias drift. Neither register entry, on its own, creates policy authority.

~~~text
Atmosphere semantics/contracts/schemas
              │ governed references
              ▼
governed input context ──► accepted Atmosphere policy source
                                      │
                                      ▼
                         immutable bundle + evaluator
                                      │ evaluator-native result
                                      ▼
                            normalized PolicyDecision
                                      │ obligations preserved
                                      ▼
                 governed consumer and separate lifecycle gates
~~~

### Boundary invariants

1. A repository path does not activate policy.
2. Rule source does not own its semantic inputs or evidence.
3. A default relation is not a normalized decision.
4. Policy evaluation does not admit, promote, release, deploy, or publish an object.
5. A passing fixture workflow does not prove rule enforcement.
6. Public consumers cannot select a repository slug, package, entrypoint, or bundle.
7. `air` and `atmosphere` cannot both become active sources.
8. Rights, sensitivity, source role, time, evidence, and correction obligations survive every adapter.
9. Missing or unresolved context cannot be converted into permission.
10. KFM does not become an official or life-safety issuer through policy wording or presentation.

[Back to top](#top)

---

## What belongs here

After appropriate acceptance and review, this directory may contain:

- Atmosphere-specific Rego or equivalent normative policy source;
- package and entrypoint documentation;
- rule-local helper modules whose only responsibility is Atmosphere admissibility;
- policy-native unit tests if the accepted repository layout places them beside source;
- non-secret test data that is explicitly allowed by the accepted policy-test layout;
- source-to-bundle inclusion metadata that does not itself activate a bundle;
- deprecation, supersession, correction, and rollback pointers for rule source;
- this README and other narrowly scoped policy-source documentation.

Every future executable file must identify:

- accepted policy and semantic authority;
- package namespace and entrypoint;
- exact input and evaluator contracts;
- output relation and normalization behavior;
- failure and missing-input behavior;
- reason and obligation mapping;
- source-rights, sensitivity, temporal, and evidence dependencies;
- native tests and bundle inclusion;
- owners, reviewers, activation state, correction, and rollback path.

## What does not belong here

| Material | Correct responsibility home |
|---|---|
| Domain doctrine or object semantics | [`docs/domains/atmosphere/`](../../../docs/domains/atmosphere/README.md) and `contracts/` |
| JSON Schemas | `schemas/` |
| Source descriptors, rights records, or payloads | Governed registry and data lifecycle roots |
| Evidence, receipts, proof objects, or attestations | `data/evidence/`, `data/receipts/`, `data/proofs/`, or accepted equivalent |
| Policy input or decision instances | Governed audit/receipt surfaces |
| Active bundle, manifest, selector, or activation record | Accepted [`policy/bundles/`](../../bundles/README.md) and control-plane boundary |
| Evaluator/runtime implementation | Accepted policy-runtime package |
| General fixtures, Python tests, or validators | `fixtures/`, `tests/domains/atmosphere/`, and `tools/validators/domains/atmosphere/` |
| Acquisition, transformation, or orchestration | `pipeline_specs/` and `pipelines/` |
| Release, correction, withdrawal, or rollback objects | `release/` and governed lifecycle records |
| API, UI, MapLibre, export, report, or AI behavior | Governed application/runtime roots |
| Credentials, tokens, raw protected payloads, or sensitive geometry | Never policy source |
| Official health, regulatory, emergency, or life-safety instruction | Applicable official issuing authority |

Cross-domain or generic policy belongs in its accepted shared or domain-specific home. Do not duplicate canonical objects merely to make this directory self-contained.

[Back to top](#top)

---

## Direct rule-source inventory

Each current Rego file is a proposed scaffold. The implementation column is based on executable, non-comment content at the pinned tree.

| File | Package | Only declared result/default | Current implementation |
|---|---|---|---|
| [`abstain_on_ambiguous.rego`](abstain_on_ambiguous.rego) | `kfm.atmosphere_abstain_on_ambiguous` | `deny := false` | Package + default only; filename does not match exposed relation |
| [`advisory-not-alert.rego`](advisory-not-alert.rego) | `kfm.generated.policy.domains.atmosphere.advisory_not_alert` | `allow := false` | Package + default only |
| [`advisory_no_life_safety.rego`](advisory_no_life_safety.rego) | `kfm.generated.policy.domains.atmosphere.advisory_no_life_safety` | `allow := false` | Package + default only; overlaps advisory concept |
| [`aod-not-pm25.rego`](aod-not-pm25.rego) | `kfm.generated.policy.domains.atmosphere.aod_not_pm25` | `allow := false` | Package + default only |
| [`aod_is_not_pm25.rego`](aod_is_not_pm25.rego) | `kfm.generated.policy.domains.atmosphere.aod_is_not_pm25` | `allow := false` | Package + default only; overlaps AOD concept |
| [`aqi_is_not_concentration.rego`](aqi_is_not_concentration.rego) | `kfm.generated.policy.domains.atmosphere.aqi_is_not_concentration` | `allow := false` | Package + default only |
| [`deny_unpublished.rego`](deny_unpublished.rego) | `kfm.atmosphere_deny_unpublished` | `deny := false` | Package + default only; commented example is not operative |
| [`dryrun_no_live_fetch.rego`](dryrun_no_live_fetch.rego) | `kfm.generated.policy.domains.atmosphere.dryrun_no_live_fetch` | `allow := false` | Package + default only |
| [`freshness_gate.rego`](freshness_gate.rego) | `kfm.generated.policy.domains.atmosphere.freshness_gate` | `allow := false` | Package + default only |
| [`low_cost_sensor_caveats_required.rego`](low_cost_sensor_caveats_required.rego) | `kfm.generated.policy.domains.atmosphere.low_cost_sensor_caveats_required` | `allow := false` | Package + default only |
| [`model-as-observed-deny.rego`](model-as-observed-deny.rego) | `kfm.generated.policy.domains.atmosphere.model_as_observed_deny` | `allow := false` | Package + default only |
| [`model_is_not_observation.rego`](model_is_not_observation.rego) | `kfm.generated.policy.domains.atmosphere.model_is_not_observation` | `allow := false` | Package + default only; overlaps model/observation concept |
| [`source_role_required.rego`](source_role_required.rego) | `kfm.generated.policy.domains.atmosphere.source_role_required` | `allow := false` | Package + default only |

### What these defaults mean—and do not mean

- `default allow := false` makes that package relation false absent another rule; it does not define a complete decision, reason, obligation, audience, trace, or lifecycle effect.
- `default deny := false` means the package does not deny absent another rule; it is not equivalent to allow, abstain, answer, or successful evaluation.
- A filename containing `deny`, `abstain`, or a doctrinal phrase has no executable meaning beyond its rule body.
- Comments and example rules are documentation, not active logic.
- Thirteen individually safe-looking defaults do not form a composable policy without an accepted entrypoint and result adapter.

### Confirmed conflict families

| Family | Files | Risk |
|---|---|---|
| Advisory/alert | `advisory-not-alert.rego`, `advisory_no_life_safety.rego` | Overlap without one canonical result or supersession relation |
| AOD/PM2.5 | `aod-not-pm25.rego`, `aod_is_not_pm25.rego` | Duplicate intent can diverge or be evaluated twice |
| Model/observation | `model-as-observed-deny.rego`, `model_is_not_observation.rego` | Duplicate intent with misleading `allow` relation under a deny-oriented name |
| Ambiguity | `abstain_on_ambiguous.rego` | Name promises abstention while package exposes `deny` only |
| Package namespace | Eleven generated packages, two flat `kfm.atmosphere_*` packages | No single import, entrypoint, or bundle contract |

No duplicate should be deleted or silently consolidated until consumer discovery, identity history, semantic review, tests, and rollback mapping are complete.

[Back to top](#top)

---

## Atmosphere policy spine

Future accepted policy must preserve the distinction between what a datum is, how it was produced, who may use it, how current it is, and what operation is being requested.

### Object-family context

The human Atmosphere domain boundary currently describes these candidate families: AirStation, AirObservation, PM25Observation, OzoneObservation, SmokeContext, AODRaster, WeatherStation, WeatherObservation, WindField, PrecipitationObservation, TemperatureObservation, ClimateNormal, ClimateAnomaly, ForecastContext, and AdvisoryContext.

This list is semantic context, not an input schema. A policy evaluator must consume accepted versioned identifiers and shapes rather than parse prose or infer an object family from a path.

### Anti-collapse rules

| Boundary | Required posture |
|---|---|
| AQI vs concentration | Never present an index or reporting category as a pollutant concentration observation |
| AOD/smoke raster vs PM2.5 | Never present remotely sensed or modeled context as a surface PM2.5 measurement |
| Model/forecast vs observation | Preserve source role and knowledge-character labels |
| Calibration vs observation | Calibration metadata supports interpretation; it is not the observation |
| Low-cost sensor vs regulatory monitor | Preserve source role, correction state, caveats, confidence, and limitations |
| Advisory context vs official warning | Do not issue life-safety direction; refer only through an approved official-authority mechanism |
| Stale vs current | Require explicit temporal and freshness state |
| Aggregate/generalized vs exact station | Never re-expand or imply protected siting precision |
| Map layer vs evidence | Tiles, rasters, contours, legends, and styles are carriers, not authority |
| Cross-domain context vs canonical claim | Atmosphere may support another domain without silently owning its claims |

### Rights and sensitivity

Future policy must fail closed when applicable source terms, license, attribution, redistribution, written-permission, confidentiality, audience, join, or re-identification constraints are missing or unresolved.

The most restrictive applicable posture must survive:

- joins across sources and domains;
- aggregation and geometry generalization;
- caching and tile generation;
- export and report generation;
- AI retrieval or summarization;
- correction, withdrawal, and supersession;
- bundle, package, or slug migration.

Exact station siting may require generalization when private land, sensitive infrastructure, or re-identification risk is plausible. Generalization does not grant a less restrictive audience or lifecycle state.

### Time and freshness

Policy context must distinguish, where applicable:

- observed time;
- valid time;
- issue time;
- retrieval time;
- processing time;
- source cadence;
- source-specific stale-after or currentness state;
- historical, current, modeled, and forecast roles.

No policy may infer current operational conditions from stale or time-ambiguous material.

### Official-authority boundary

For emergency action, health protection, official AQI guidance, regulatory status, or other consequential direction, KFM must not fabricate or impersonate the issuer. A governed consumer may provide a bounded non-answer or denial and an approved official reference, subject to rights and audience controls.

[Back to top](#top)

---

## Inputs

No accepted runtime input contract is bound to the current thirteen files. A path string, filename, Rego package, UI toggle, or caller-supplied slug is insufficient policy context.

### Shared candidate profile

The checked-in `PolicyInputBundle` profile is `PROPOSED_INACTIVE`, fixture-only, and non-evaluator. It enumerates candidate operations and audiences, but its authority flags remain false. It is evidence of vocabulary work, not an accepted runtime contract.

### Required input families

| Family | Minimum posture before evaluation |
|---|---|
| Request | Stable request/correlation identity and declared operation |
| Domain | Accepted logical domain identity and any approved compatibility mapping |
| Caller | Governed service/user identity and capabilities where applicable |
| Audience | One accepted audience value |
| Object | Accepted object-family/version reference, not filename inference |
| Source role | Observation, model, forecast, advisory, calibration, or other accepted role |
| Knowledge character | Explicit observed, derived, modeled, forecast, contextual, or equivalent state |
| Rights | License, attribution, redistribution, consent, confidentiality, and review state |
| Evidence | EvidenceRef/EvidenceBundle state and validation references |
| Time | Observed, valid, issue, retrieval, processing, cadence, and freshness as applicable |
| Sensitivity | Precision, exact-station/private-land/infrastructure exposure, join, and re-identification risk |
| Policy | Exact bundle ID/version/digest, evaluator profile, entrypoint, and activation state |
| Lifecycle | Candidate/released/superseded/withdrawn state plus correction and rollback references |
| Trace | Audit-safe trace without credentials, raw protected payloads, or protected geometry |

### Input rules

- References must be resolvable under the evaluator's accepted contract; the rule source must not fetch live network data.
- Missing evidence, rights, sensitivity, audience, source-role, or freshness context cannot be guessed.
- Invalid input is distinct from a valid input that policy intentionally declines to answer.
- Source data and protected geometry must not be copied into decision logs.
- Caller-controlled fields cannot select repository paths, packages, entrypoints, or bundle versions.
- Time-dependent evaluation must receive deterministic time context rather than read ambient wall-clock state unless the evaluator contract explicitly governs it.

[Back to top](#top)

---

## Outputs

### Current output

Today this lane produces only **proposed rule-source files and documentation**. No accepted evaluator-native result, normalized PolicyDecision, signed decision receipt, release decision, or public artifact was verified.

### Future evaluator-native result

An accepted evaluator may produce only the result shape defined by its versioned entrypoint contract. That raw result must not be consumed as a public or lifecycle decision until a governed adapter has:

1. verified bundle identity, version, digest, selector, and evaluator compatibility;
2. distinguished successful evaluation from invalid input or execution failure;
3. normalized exactly one finite policy outcome;
4. attached deterministic reasons and obligations from accepted vocabularies;
5. preserved source, evidence, rights, sensitivity, audience, temporal, and lifecycle references;
6. emitted an authenticated, auditable decision record where required;
7. kept secrets, protected payloads, and sensitive geometry out of diagnostics;
8. handed the result to a separately governed consumer.

### Non-output

A policy result is not:

- an observation or scientific claim;
- a semantic contract or schema instance merely because fields resemble one;
- an EvidenceBundle, ProofPack, validation receipt, or approval;
- source admission, promotion, release, deployment, or publication;
- a correction, withdrawal, or rollback execution;
- medical, regulatory, emergency, or life-safety direction.

[Back to top](#top)

---

## Decision normalization boundary

### Candidate finite outcomes

The checked-in shared decision vocabulary and semantics profile are `PROPOSED_INACTIVE`. Their candidate outward surface is finite:

- `ANSWER`
- `ABSTAIN`
- `DENY`
- `ERROR`

The AtmosphereAirDecisionEnvelope human draft uses related semantics, but its machine schema is a minimal proposed scaffold and its dedicated validator and finite-outcome test are placeholders. No current Rego entrypoint maps the thirteen package relations to that envelope.

### Required distinctions

| Condition | Candidate normalized class | Constraint |
|---|---|---|
| Policy explicitly permits a bounded operation | `ANSWER` | Permission and obligations must be explicit; absence of denial is insufficient |
| Policy intentionally supplies no answer for valid context | `ABSTAIN` | Must not be represented by `deny := false` alone |
| Policy forbids the requested operation | `DENY` | Reason and safe obligations required; no protected-detail leakage |
| Input, bundle, evaluator, or execution is invalid/unavailable | `ERROR` | Must not degrade into allow or authoritative abstention |

`HOLD` and `RESTRICT` may be internal workflow or obligation concepts, but this README does not add them to the inactive outward vocabulary or decide their wire representation.

### Normalization requirements

- one request yields one normalized decision;
- all evaluated package outputs are interpreted through one accepted adapter;
- contradictory outputs fail closed and generate reviewable evidence;
- missing packages, rules, or bundle members are errors, not permissions;
- reasons are deterministic identifiers, not free-text policy logic;
- obligations are machine-actionable and preserved by every consumer;
- unknown reasons or obligations fail safely;
- raw Rego booleans are never rendered to public users as authority.

[Back to top](#top)

---

## Bundle, evaluator, and activation boundary

No accepted Atmosphere bundle payload, manifest instance, selector, evaluator binding, or production consumer was verified. [`policy/bundles/`](../../bundles/README.md) is documentation-only at the direct lane, and the policy runtime core is a comment-only placeholder.

### Required immutable binding

Before activation, one reviewed record must bind:

| Field | Requirement |
|---|---|
| Logical domain | Accepted Atmosphere identifier and compatibility disposition |
| Source set | Exact paths and blob/content digests |
| Package/entrypoint | One accepted namespace and result contract |
| Dependencies | Exact versions and digests; no recursive directory discovery |
| Bundle | Stable ID, version, manifest, content digest, creation evidence |
| Evaluator | Engine/version, capabilities, limits, input/output adapter versions |
| Selector | Governed environment/audience/operation mapping; no caller path choice |
| Activation | Reviewed state, effective time, expiration/supersession, approvals |
| Validation | Native tests, integration profiles, negative tests, reports, receipts |
| Correction/rollback | Exact prior binding, invalidation scope, exercise evidence |

### Forbidden shortcuts

~~~text
directory exists
  → recursively package every .rego file
  → infer entrypoints from filenames
  → treat false as deny or true as allow everywhere
  → call a green fixture workflow policy proof
  → expose the result to UI, map, export, report, AI, or release
~~~

Each arrow crosses an unproved authority boundary.

### Activation sequence

~~~mermaid
flowchart LR
    A[Accepted semantics and schemas] --> B[One package and entrypoint]
    B --> C[Implemented rules and native tests]
    C --> D[Immutable manifest and digest]
    D --> E[Compatible evaluator and adapter]
    E --> F[Independent review]
    F --> G[Explicit activation record]
    G --> H[Governed consumers]
    H --> I[Separate release and publication gates]
    I --> J[Monitoring, correction, rollback]
~~~

Completion of an earlier node never implies a later state transition.

[Back to top](#top)

---

## Validation

### Current policy-native coverage

- **Zero** native Atmosphere Rego tests were verified.
- The general `policy-test` workflow evaluates one separate Pass 12 release-gate test, not these thirteen files.
- No checked-in workflow was verified to load an Atmosphere bundle, invoke its entrypoint, normalize its result, or exercise a governed consumer.

### Adjacent Python tests

The direct Atmosphere test lane has fifteen test modules plus an empty `__init__.py`.

**Seven substantive modules in the accepted workflow profile:**

- `test_atmosphere_smoke.py`
- `test_correctable_environmental_event_assessment.py`
- `test_knowledge_character_registry.py`
- `test_low_cost_sensor_caveat_required.py`
- `test_observed_modeled_separation.py`
- `test_prescribed_burn_quality_flag.py`
- `test_pm25_trigger_candidate_assessment.py`

**Eight placeholder modules:** advisory/no-life-safety, AOD-as-PM2.5 denial, AQI-as-concentration denial, decision-envelope finite outcomes, dry-run/no-live-fetch, model-as-observed denial, temporal-field distinction, and unit normalization.

These tests exercise bounded Python/fixture behavior where substantive. They do not execute the current Rego files.

### Adjacent validators

The direct Atmosphere validator lane has twenty Python modules.

**Ten substantive modules in the accepted workflow profile:** PM sensor trust profile, PM2.5 colocation manifest, correctable environmental-event assessment, knowledge character, low-cost-sensor caveats, public-safe precipitation fixture, observed/modeled separation, prescribed-burn quality flag, PM2.5 trigger-candidate assessment, and AirNow/AQS reconciliation.

**Ten placeholders:** air observation, AOD raster, Atmosphere decision envelope, catalog matrix, EvidenceBundle, forecast context, parameter units, schema, smoke context, and source descriptor.

### Relevant no-network workflows

Seven checked-in workflows are relevant to Atmosphere's bounded profiles:

- `atmosphere-airnow-aqs-reconciliation`
- `atmosphere-aqs-site-delta`
- `correctable-environmental-event-assessment`
- `domain-atmosphere`
- `pm-sensor-trust-profile`
- `pm25-sensor-colocation-manifest`
- `pm25-trigger-candidate-assessment`

The `domain-atmosphere` workflow inventories accepted versus placeholder modules, executes bounded synthetic profiles, and records explicit holds for broader validation, proof, release, and live-source behavior. A workflow pass proves only those declared steps on that exact revision.

### Minimum rule-test matrix before activation

Every accepted policy family needs deterministic no-network tests for:

- explicit allow/answer behavior;
- explicit denial;
- intentional abstention;
- invalid and missing input;
- ambiguous and contradictory package results;
- stale, future, and time-ambiguous context;
- missing or restrictive rights and attribution;
- sensitivity, exact-station, join, and re-identification risk;
- source-role and knowledge-character mismatch;
- low-cost-sensor caveat and correction state;
- model/observation, AOD/PM2.5, and AQI/concentration anti-collapse;
- advisory and official-authority boundaries;
- unknown reason or obligation handling;
- duplicate-rule and bundle-membership detection;
- bundle/evaluator incompatibility;
- consumer obligation preservation;
- correction, supersession, cache invalidation, and exact rollback.

### Validation commands

Repository-native commands and required-check status must be confirmed in a real checkout and hosted CI. This README does not invent a working Atmosphere policy command where none was verified.

Review evidence should record exact command, environment, dependency lock/digests, input fixtures, expected result, actual result, and immutable run reference. Network access is forbidden unless an accepted profile explicitly requires and governs it; policy evaluation itself should use supplied references/context rather than live fetches.

[Back to top](#top)

---

## Threat model and failure behavior

| Threat or failure | Required response |
|---|---|
| Caller selects `air`, `atmosphere`, package, entrypoint, or bundle | Reject or resolve through accepted server-side configuration only |
| Missing rights, sensitivity, evidence, audience, source role, or freshness | Fail closed; do not guess |
| Contradictory rule outputs | Configuration/evaluation error plus reviewable audit evidence |
| Duplicate concept evaluated twice | Reject bundle or fail activation |
| Stale bundle or selector | Refuse evaluation or use only an explicitly accepted prior binding |
| Bundle digest mismatch | Reject before evaluation |
| Evaluator incompatibility | Error; no permissive fallback |
| Live network fetch attempted from policy | Deny execution and record safe diagnostic evidence |
| Protected detail enters logs/reasons | Redact, contain, and trigger security/privacy review |
| Obligation dropped by API/UI/map/export/AI adapter | Block operation; consumer is non-conformant |
| Fixture result treated as approval | Hold lifecycle transition |
| Corrected or withdrawn state remains cached | Invalidate affected decisions/artifacts and open correction review |
| Advisory implies official or life-safety authority | Deny/abstain per accepted semantics and route only to approved official references |

Diagnostics must be useful to authorized reviewers without revealing credentials, raw protected payloads, exact sensitive locations, or inference-enabling details.

[Back to top](#top)

---

## Review burden

Changes here are trust-bearing because a small source or packaging change can alter admissibility across APIs, maps, exports, reports, AI adapters, and release gates.

### Review matrix

| Change | Required review capability |
|---|---|
| README clarification | Policy + Atmosphere + documentation |
| Rego/package change | Policy + Atmosphere + security/privacy + test |
| Source-role or knowledge-character behavior | Atmosphere semantics + source/evidence + policy |
| Rights or sensitivity behavior | Source-rights + privacy/sensitivity + policy |
| Package/entrypoint/result adapter | Policy runtime + architecture + security |
| Bundle/selector/evaluator | Policy runtime + policy + security + operations |
| Input/decision/reason/obligation contract | Contract/schema + policy + consumer owners |
| Air/Atmosphere migration | Directory governance + affected-root owners + runtime |
| Public API/UI/map/export/report/AI effect | Surface owner + policy + security/privacy + release |
| Official-authority behavior | Atmosphere + hazards/life-safety boundary + security |
| Release/correction/rollback binding | Release + policy + independent reviewer |

These are capability requirements, not assertions that named people are assigned.

### Separation of duties

- the author is not the sole approver;
- rule acceptance is separate from bundle construction;
- bundle construction is separate from activation;
- tests and generated receipts are separate from approval;
- policy evaluation is separate from promotion and release;
- release is separate from publication;
- correction and rollback remain independently executable;
- a README merge cannot activate policy.

### Reviewer checklist

- [ ] Evidence is pinned to a current complete tree.
- [ ] Only policy-source responsibility is added here.
- [ ] One package namespace, entrypoint, input, and raw-result contract is explicit.
- [ ] Duplicate concepts have reviewed supersession and identity history.
- [ ] Defaults, missing input, ambiguity, and invalid execution are distinguished.
- [ ] Reasons and obligations are deterministic and versioned.
- [ ] Rights, sensitivity, source role, knowledge character, freshness, evidence, and lifecycle references survive normalization.
- [ ] Native Rego and governed-consumer tests cover positive and negative paths.
- [ ] Bundle content is explicit, immutable, digest-bound, and non-recursive.
- [ ] Selector and public consumers cannot be caller-controlled by path or slug.
- [ ] Official-authority and protected-detail boundaries are tested.
- [ ] Policy, release, deployment, and publication states remain separate.
- [ ] Correction, invalidation, and rollback identify exact targets.
- [ ] Receipts remain provenance, not approval.

[Back to top](#top)

---

## Release, correction, and rollback

### Lifecycle separation

An accepted policy decision may constrain a lifecycle transition, but it does not perform that transition. Separate governed records and approvals remain required for admission, promotion, release, deployment, publication, correction, withdrawal, restoration, and rollback.

### Correction triggers

Open a correction or rollback review if:

- a rule or bundle produces a decision inconsistent with its accepted semantics;
- `air` and `atmosphere` both become active or produce slug-dependent decisions;
- duplicate rule concepts diverge or execute twice;
- a selector loads the wrong, stale, incomplete, or incompatible bundle;
- source, evidence, rights, sensitivity, time, or lifecycle references are lost;
- an obligation is dropped by a consumer;
- stale, corrected, superseded, or withdrawn state remains cached;
- a public surface presents policy as scientific proof, approval, official guidance, or life-safety instruction;
- exact rollback cannot restore the prior known-good binding.

### Runtime rollback record

Any future active binding needs:

- affected domain, operation, audience, environment, and consumer set;
- current and prior bundle IDs, versions, manifests, and digests;
- selector and evaluator versions;
- activation and rollback decisions;
- correction/withdrawal references;
- cache and derived-artifact invalidation scope;
- verification results after restoration;
- independent review evidence.

### README rollback

For this documentation-only revision, the exact prior blob is:

~~~text
d897f4f67458f9d12e0ef2b2e7146eeba935df4b
~~~

Restoring that blob reverts only this README. It does not roll back any policy source, bundle, evaluator, selector, deployment, release, publication, correction, or public behavior.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Parent domain-policy boundary |
| [`../../README.md`](../../README.md) | Canonical policy-root responsibility boundary |
| [`../air/README.md`](../air/README.md) | Separate compatibility lane; must not become parallel authority |
| [`../../../docs/domains/atmosphere/README.md`](../../../docs/domains/atmosphere/README.md) | Human Atmosphere scope and object-family context |
| [`../../../docs/domains/atmosphere/CANONICAL_PATHS.md`](../../../docs/domains/atmosphere/CANONICAL_PATHS.md) | Preferred placement and namespace-drift context |
| [`../../../docs/domains/atmosphere/POLICY.md`](../../../docs/domains/atmosphere/POLICY.md) | Draft human policy doctrine, not runtime enforcement |
| [`../../../docs/domains/atmosphere/SENSITIVITY.md`](../../../docs/domains/atmosphere/SENSITIVITY.md) | Draft sensitivity/generalization posture |
| [`../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md`](../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md) | Draft public-serving and official-authority boundary |
| [`../../../contracts/domains/atmosphere/README.md`](../../../contracts/domains/atmosphere/README.md) | Atmosphere semantic-contract family |
| [`../../../contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md`](../../../contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md) | Draft human decision-envelope semantics |
| [`../../../schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json`](../../../schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json) | Minimal proposed machine-shape scaffold |
| [`../../../tests/domains/atmosphere/README.md`](../../../tests/domains/atmosphere/README.md) | Mixed substantive/placeholder test boundary |
| [`../../../tools/validators/domains/atmosphere/README.md`](../../../tools/validators/domains/atmosphere/README.md) | Mixed substantive/placeholder validator boundary |
| [`../../../pipeline_specs/atmosphere/README.md`](../../../pipeline_specs/atmosphere/README.md) | Proposed declarative pipeline boundary |
| [`../../../pipelines/domains/atmosphere/README.md`](../../../pipelines/domains/atmosphere/README.md) | Atmosphere executable-pipeline scaffold |
| [`../../../contracts/policy/policy_input_bundle_profile_v1.md`](../../../contracts/policy/policy_input_bundle_profile_v1.md) | Inactive candidate input profile |
| [`../../../contracts/policy/policy_decision_vocabulary.md`](../../../contracts/policy/policy_decision_vocabulary.md) | Inactive candidate decision/reason/obligation vocabulary |
| [`../../../contracts/policy/policy_decision_semantics_profile_v1.md`](../../../contracts/policy/policy_decision_semantics_profile_v1.md) | Inactive candidate decision-semantics profile |
| [`../../../contracts/policy/policy_reviewer_role_vocabulary.md`](../../../contracts/policy/policy_reviewer_role_vocabulary.md) | Inactive candidate reviewer-role vocabulary |
| [`../../decision/vocabulary.v1.json`](../../decision/vocabulary.v1.json) | Machine-readable candidate vocabulary |
| [`../../decision/reviewer_roles.v1.json`](../../decision/reviewer_roles.v1.json) | Machine-readable candidate reviewer roles |
| [`../../bundles/README.md`](../../bundles/README.md) | Bundle boundary; no accepted active Atmosphere payload verified |
| [`../../../packages/policy-runtime/README.md`](../../../packages/policy-runtime/README.md) | Proposed runtime boundary; core remains unimplemented |
| [`../../../data/registry/sources/atmosphere/README.md`](../../../data/registry/sources/atmosphere/README.md) | Source identity, role, rights, and cadence context |
| [`../../../data/proofs/atmosphere/README.md`](../../../data/proofs/atmosphere/README.md) | Proof boundary; not policy authority |
| [`../../../release/candidates/atmosphere/README.md`](../../../release/candidates/atmosphere/README.md) | Candidate release boundary; not a release |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | Accepted placement text through ADR-0029 |
| [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) | Draft human domain-lane register |
| [`../../../control_plane/domain_lane_register.yaml`](../../../control_plane/domain_lane_register.yaml) | Proposed machine projection and unresolved `air` alias |
| [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) | Repository drift register |
| [`../../../.github/workflows/policy-test.yml`](../../../.github/workflows/policy-test.yml) | General policy test workflow; not current Atmosphere Rego coverage |
| [`../../../.github/workflows/domain-atmosphere.yml`](../../../.github/workflows/domain-atmosphere.yml) | Bounded Atmosphere fixture profile and explicit holds |

[Back to top](#top)

---

## Air compatibility boundary

`policy/domains/air/` exists separately as a compatibility guardrail. The repository's proposed machine register records `air: atmosphere` as unresolved alias drift, while Atmosphere documentation prefers `atmosphere` for new work.

Until an accepted migration decision exists:

1. at most one segment may supply evaluated Atmosphere rules;
2. aliases cannot create separate package namespaces, entrypoints, bundle IDs, or selectors;
3. a request cannot evaluate both lanes and merge, race, or prefer results;
4. public callers cannot select a repository segment;
5. missing preferred policy cannot fall through to unreviewed compatibility source;
6. source, evidence, rights, sensitivity, lifecycle, correction, and rollback identity must survive migration;
7. the most restrictive applicable posture remains effective;
8. no alias may create official or life-safety authority.

Merged PR #2716 hardened the separate Air README and added its generated receipt. It changed no Atmosphere policy file, rule, test, validator, workflow, bundle, runtime, or public behavior. The Air README is now current repository documentation, but it remains a compatibility boundary rather than a second policy source or activation record.

[Back to top](#top)

---

## Contributor workflow

1. Pin the current default-branch commit and complete tree.
2. Re-read this README, the parent/root boundaries, ADR-0029, directory rules, CODEOWNERS, and relevant Atmosphere doctrine.
3. Search open PRs and recent history for exact-path and semantic overlap.
4. Classify each proposed statement as confirmed, proposed, conflicted, unknown, or needing verification.
5. Keep source changes separate from bundle activation, runtime changes, and lifecycle/public-surface changes unless an accepted plan explicitly joins them.
6. Update or add native policy tests before claiming behavior.
7. Validate package, entrypoint, inputs, result normalization, reasons, obligations, bundle membership, evaluator compatibility, and failure behavior.
8. Run bounded no-network tests and record exact commands and revisions.
9. Review rights, sensitivity, official-authority, logging, correction, and rollback impacts.
10. Create a draft PR with exact scope, evidence, validation, overlap, holds, and rollback target.
11. Observe hosted checks on the exact head; do not rewrite baselines or bypass failures to make documentation appear green.
12. Require human review; do not mark ready, merge, activate, release, deploy, or publish as part of documentation authoring.

[Back to top](#top)

---

## Conflict register

| ID | Conflict | Confirmed evidence | Closure condition |
|---|---|---|---|
| `ATMPOL-001` | Result relation | Two `deny` defaults vs eleven `allow` defaults | One accepted entrypoint and normalized result adapter |
| `ATMPOL-002` | Package namespace | Eleven generated-style packages vs two flat packages | One accepted versioned namespace |
| `ATMPOL-003` | Duplicate concepts | Advisory, AOD/PM2.5, and model/observation overlaps | Supersession/identity map plus native tests |
| `ATMPOL-004` | Abstention semantics | `abstain_on_ambiguous` exposes `deny` only | Accepted finite-outcome mapping and test |
| `ATMPOL-005` | Rule implementation | All thirteen files are default-only scaffolds | Reviewed operative bodies with policy-native tests |
| `ATMPOL-006` | Native test coverage | No Atmosphere Rego tests | Dependency-closed deterministic suite |
| `ATMPOL-007` | Input contract | Shared profile is inactive; files bind no accepted shape | Accepted input version and evaluator binding |
| `ATMPOL-008` | Decision envelope | Human semantics vs minimal schema and placeholder validator/test | Accepted aligned contract/schema/validator/tests |
| `ATMPOL-009` | Bundle/evaluator | No accepted payload, selector, or runtime implementation | Immutable bundle plus compatible evaluator and activation |
| `ATMPOL-010` | Validation interpretation | Bounded fixture checks coexist with placeholders | Clear dependency-closed policy and integration evidence |
| `ATMPOL-011` | Air/Atmosphere namespace | Multiple roots contain both segments | Accepted migration decision and consumer map |
| `ATMPOL-012` | Rights/freshness | Domain posture exists; source-specific rules unverified | Accepted source-specific matrices and tests |
| `ATMPOL-013` | Public obligations | Consumer enforcement not verified | End-to-end API/UI/map/export/report/AI tests |
| `ATMPOL-014` | Official authority | Doctrine disclaims authority; runtime proof absent | Approved redirect behavior and negative tests |
| `ATMPOL-015` | Ownership | CODEOWNERS route verified; functional roles unassigned | Recorded steward assignments and separation |
| `ATMPOL-016` | Correction/rollback | No active binding or completed drill | Exact target, invalidation plan, and exercised restoration |

This README records conflicts; it resolves none by assertion.

[Back to top](#top)

---

## Smallest sound resolution sequence

1. Freeze expansion of the thirteen stubs until one rule architecture is accepted.
2. Record duplicate/package/result conflicts with stable identities.
3. Inventory tracked and deployed consumers of `air`, `atmosphere`, current packages, and any bundle discovery logic.
4. Accept the Atmosphere/Air namespace and migration decision.
5. Align Atmosphere semantics, machine schemas, source roles, rights, sensitivity, time, and official-authority posture.
6. Accept one input contract and one finite decision/reason/obligation vocabulary.
7. Choose one Rego package namespace, entrypoint, result relation, and normalization adapter.
8. Supersede duplicates without losing history or rollback identity.
9. Implement the rules beyond defaults.
10. Add deterministic native tests for every policy family and failure mode.
11. Build an explicit immutable bundle with exact dependencies and digest.
12. Bind a compatible evaluator and server-controlled selector.
13. Prove obligation preservation in governed consumers.
14. Review independently across policy, domain, evidence, rights, privacy, runtime, security, release, and public surfaces.
15. Activate through an explicit record with monitoring, correction, cache invalidation, and exact rollback.
16. Keep promotion, release, deployment, and publication as separate decisions.
17. Close each `ATMPOL-*` conflict only with direct evidence.

Each step is independently reviewable and reversible. No later step is implied by completion of an earlier one.

[Back to top](#top)

---

## Definition of done

This lane is activation-ready only when:

- [ ] functional stewards and independent reviewer roles are recorded;
- [ ] `air` versus `atmosphere` is resolved by an accepted decision;
- [ ] tracked and deployed consumers are inventoried;
- [ ] one package namespace, entrypoint, input shape, and raw-result contract is accepted;
- [ ] duplicate rule concepts are superseded with identity history;
- [ ] all intended rules have operative bodies and deterministic native tests;
- [ ] missing, invalid, ambiguous, contradictory, and stale states fail safely;
- [ ] domain semantics, schema, source role, rights, sensitivity, freshness, and evidence references align;
- [ ] one immutable bundle/manifest/evaluator/selector chain is accepted;
- [ ] reasons and obligations are versioned and enforced by every governed consumer;
- [ ] public callers cannot select paths, packages, entrypoints, bundles, or aliases;
- [ ] API/UI/map/export/report/AI surfaces preserve policy and protected-detail boundaries;
- [ ] official-authority behavior is bounded and tested;
- [ ] promotion, release, deployment, and publication remain separate approvals;
- [ ] monitoring, correction, withdrawal, cache invalidation, and rollback are exercised;
- [ ] exact activation and rollback evidence is auditable;
- [ ] all `ATMPOL-*` conflicts and open verification items close with direct evidence.

Until then, this directory remains draft, proposed-source-only, evaluator-unbound, non-release, non-publication, and not for life-safety use.

[Back to top](#top)

---

## Open verification register

| ID | Verification item | Evidence needed |
|---|---|---|
| `ATMPOL-OPEN-001` | Functional owners | Recorded role assignments; CODEOWNERS alone is insufficient |
| `ATMPOL-OPEN-002` | Accepted Air/Atmosphere decision | Accepted ADR/equivalent with scope, consumers, and status |
| `ATMPOL-OPEN-003` | Deployed consumers | Inventory beyond tracked repository |
| `ATMPOL-OPEN-004` | Package and entrypoint | Accepted Rego/evaluator contract |
| `ATMPOL-OPEN-005` | Input contract | Accepted versioned shape and reference-resolution rules |
| `ATMPOL-OPEN-006` | Decision normalization | Accepted finite outcomes, reasons, obligations, and adapter |
| `ATMPOL-OPEN-007` | Bundle/evaluator/selector | Manifest, digest, compatibility matrix, and activation record |
| `ATMPOL-OPEN-008` | Decision-envelope alignment | Accepted semantics, schema, validator, and tests |
| `ATMPOL-OPEN-009` | Source rights | Source-specific terms, attribution, redistribution, and review |
| `ATMPOL-OPEN-010` | Freshness | Source-specific temporal/currentness rules |
| `ATMPOL-OPEN-011` | Exact-station posture | Generalization and sensitive-infrastructure tests |
| `ATMPOL-OPEN-012` | Low-cost-sensor posture | Caveat, correction, confidence, limitation, and role profile |
| `ATMPOL-OPEN-013` | Obligation handlers | API/UI/map/export/report/AI enforcement evidence |
| `ATMPOL-OPEN-014` | Official redirection | Approved references and end-to-end negative tests |
| `ATMPOL-OPEN-015` | Required checks | Branch-protection and check-significance evidence |
| `ATMPOL-OPEN-016` | Production enforcement | Deployment/runtime evidence |
| `ATMPOL-OPEN-017` | Correction and rollback | Invalidation map and completed exact-target drill |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Supports | Limit |
|---|---|---|
| Complete pinned main tree | Exact tracked counts and path presence | Does not reveal deployed or off-repository consumers |
| Prior Atmosphere README blob | History and documentation rollback target | Generic scaffold; no policy proof |
| ADR-0029 + Directory Rules + root registry | Accepted placement and root responsibility | Do not accept domain behavior or activate policy |
| Domain-lane registers | Current Atmosphere projection and unresolved Air alias | Registers remain draft/proposed and do not create authority |
| CODEOWNERS | `/policy/` review route | Does not assign all functional roles |
| Thirteen Rego files | Exact package/default inventory | Defaults and names are not a complete policy system |
| Shared policy profiles/vocabularies | Candidate inputs, outcomes, reasons, obligations, roles | `PROPOSED_INACTIVE`; authority flags false |
| AtmosphereAirDecisionEnvelope contract + schema | Semantic intent and current alignment gap | Schema is minimal; validator/test placeholders |
| Atmosphere Python tests | Seven substantive bounded modules | Eight placeholders; no native Rego tests |
| Atmosphere validators | Ten substantive bounded modules | Ten placeholders; no broad closure |
| Seven Atmosphere workflows | Declared no-network fixture execution and explicit holds | No live-source, policy, proof, release, or publication authority |
| Policy bundles boundary | Intended packaging and activation separation | No accepted Atmosphere payload or selector |
| Policy runtime core | Implementation state | Comment-only placeholder |
| Atmosphere doctrine | Anti-collapse, rights, sensitivity, time, and official-authority intent | Human drafts do not prove runtime enforcement |
| Merged Air PR #2716 | Adjacent compatibility analysis and exact path disjointness | Documentation/provenance only; does not activate Atmosphere policy |

### Reproducibility note

The evidence snapshot pins the repository commit, complete tree, direct lane tree, prior target blob, and primary governing artifacts. Counts and claims must be recomputed whenever main, this lane, the Air compatibility lane, shared policy contracts, Atmosphere tests/validators/workflows, bundles, runtime, governance, or lifecycle/public consumers change.

### No-loss ledger

| Prior heading | Preserved here |
|---|---|
| Purpose | Expanded into scope, non-goals, and durable question |
| Authority level | Reconciled with accepted Directory Rules and explicit authority map |
| What belongs here | Narrowed to policy-source responsibility |
| What does not belong here | Expanded into responsibility-root routing |
| Inputs | Replaced generic folder pointer with an explicit unbound input boundary |
| Outputs | Replaced generic folder pointer with current/future/non-output distinctions |
| Validation | Replaced generic pointer with exact policy-native and adjacent coverage |
| Review burden | Expanded into capability matrix, separation, and checklist |
| Related folders | Replaced generic parallel-folder note with resolved relationships |
| Status | Replaced greenfield label with pinned maturity evidence |

[Back to top](#top)

---

## Changelog

| Date | Version | Change | Status |
|---|---|---|---|
| 2026-05-08 | Unversioned | Added the generic greenfield directory scaffold. | Proposed documentation only |
| 2026-08-13 | v0.3 | Reconciled the complete fourteen-blob lane, thirteen default-only Rego files, mixed packages/results and duplicate concepts, zero native Rego tests, bounded adjacent validation, inactive bundle/runtime, decision-envelope gap, Air alias drift, review, public-authority, correction, rollback, and evidence boundaries. | Documentation only; no rule or runtime behavior changed |

---

KFM rule: `policy/domains/atmosphere/` may own reviewed Atmosphere admissibility source. It must not become a substitute for semantics, evidence, rights, sensitivity, runtime, release, publication, official guidance, or life-safety authority—and source presence alone must never be mistaken for activation.

<p align="right"><a href="#top">Back to top</a></p>
