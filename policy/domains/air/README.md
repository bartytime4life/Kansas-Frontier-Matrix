<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/domains/air
title: Air Policy Compatibility Boundary README
type: readme; directory-readme; domain-policy-compatibility-boundary; alias-guardrail; policy-index
version: v0.3
status: draft; repository-grounded; compatibility-only; direct-lane-marker-and-readme; preferred-atmosphere-policy-scaffolds; adjacent-fixture-profiles; evaluator-unbound; fail-closed; non-release; non-publication; not-for-life-safety
owners: "@bartytime4life — verified CODEOWNERS review route; Atmosphere/Air, policy, directory-governance, rights, sensitivity, source, contract/schema, validator/test, runtime, release, security, and docs stewardship assignments NEEDS VERIFICATION"
created: 2026-06-15
updated: 2026-08-13
supersedes: v0.2 Air policy compatibility guardrail
policy_label: restricted-review; policy; air; atmosphere; compatibility-only; slug-drift; redirect-to-atmosphere; no-active-policy-here; no-public-authority; not-emergency-alerting
current_path: policy/domains/air/README.md
owning_root: policy/
responsibility: >
  Compatibility and migration boundary for the unresolved `air` policy segment. It records the
  complete direct inventory, redirects new Atmosphere policy work toward
  `policy/domains/atmosphere/`, distinguishes proposed policy scaffolds from bounded fixture
  validation, prevents parallel policy and bundle authority, and preserves evidence, rights,
  sensitivity, review, release, correction, and rollback boundaries without activating this path.
truth_posture: >
  CONFIRMED accepted ADR-0029 directory-placement authority and canonical singular policy root;
  verified CODEOWNERS review route; complete two-blob Air inventory consisting of this README and
  an empty marker; complete fourteen-blob preferred Atmosphere policy inventory consisting of one
  short README and thirteen PROPOSED default-only Rego scaffolds; two scaffolds default
  `deny := false` and eleven default `allow := false`; no operative rule body, native Rego test,
  accepted bundle payload, evaluator binding, or runtime implementation; mixed adjacent
  Atmosphere fixture validation with ten substantive and ten placeholder validator modules, seven
  substantive and eight placeholder Python test modules, and seven relevant no-network workflows;
  shared PROPOSED_INACTIVE input, decision, reason, obligation, semantics, and reviewer-role
  profiles whose authority flags remain false; an AtmosphereAirDecisionEnvelope semantic draft
  whose lower-case schema, validator, and finite-outcome test remain scaffolds or placeholders /
  PROPOSED keep this lane documentation-only; route new policy source to the Atmosphere lane after
  accepted namespace and activation review; preserve one active policy source, one bundle
  identity, one normalized decision, and one rollback path; use repository-local Air reason and
  obligation terms only as non-normative documentation shorthand /
  CONFLICTED `air` and `atmosphere` segments across policy, contracts, schemas, tests, pipeline
  specifications, and pipeline documentation; duplicate or near-duplicate Atmosphere Rego names;
  inconsistent package/default semantics; semantic decision-envelope prose versus a minimal
  proposed machine schema; local compatibility dispositions versus the inactive shared
  ANSWER/ABSTAIN/DENY/ERROR vocabulary /
  UNKNOWN accepted Air-to-Atmosphere migration ADR, package namespace, entrypoint, bundle manifest,
  selector, evaluator, authenticated decision emission, production consumer, public alias,
  deployment binding, required-check significance, promotion integration, monitoring, and
  release-gate adoption /
  NEEDS VERIFICATION functional steward assignments, alias lifetime, complete consumer inventory,
  source-specific rights rules, stale-state thresholds, exact-station generalization, low-cost
  sensor caveat/correction requirements, decision-envelope alignment, public API/UI/map/AI
  obligation enforcement, correction propagation, cache invalidation, and rollback drills.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: f61d9df6409917610fa45d739fab55cab86f5eb2
  complete_tree: abff80bd000194c69a95d461fa28a4137925d9d2
  prior_blob: d722464dcce4effeb5f70861bbfb629b8d3aed9d
  policy_root_blob: 6c5021f9d92778581a4e9331a9dd6ddb7efc5e35
  policy_domains_parent_blob: ed9be975c9da2c7d77d94fab621db39f23953813
  atmosphere_policy_readme_blob: d897f4f67458f9d12e0ef2b2e7146eeba935df4b
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  policy_input_profile_blob: 3af1c2b83a6d4a724b2442bf7ee7944c344f63d0
  decision_semantics_profile_blob: 2df81cf319e45a2e3aa4148c0d1b54a84d0122b5
  decision_vocabulary_blob: ae68a9f3cf80308f18bd04207ef2c85057750f12
  reviewer_roles_blob: 01559907b2622606f35bb9a8ae5d0347e9b7e263
  atmosphere_decision_envelope_contract_blob: e68e33f1750ad944cb1b7e1c5ac72f761c03d80e
  atmosphere_decision_envelope_schema_blob: 28b217f010ca5be9aa249bfa41f477f03853dd9a
  atmosphere_tests_readme_blob: 29204b8ecddaa8dd6ce068bf7ff4fe1d1a1cfbe9
  atmosphere_validators_readme_blob: 64680d859fcb48a521259aeeaab33acbd304e496
  domain_atmosphere_workflow_blob: fccba4b60f9967c9bf83dcfa35af9c650a6fc9bc
  policy_runtime_core_blob: e7e14cf39ae6919fbbc80f1b471de6b907292edb
  policy_bundles_readme_blob: 0a13a9c9beddfa764d47e5dd6a2ea7ef91bf0d53
related:
  - ../README.md
  - ../../README.md
  - ../atmosphere/README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/SENSITIVITY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../contracts/air/README.md
  - ../../../contracts/domains/atmosphere/README.md
  - ../../../contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json
  - ../../../tests/domains/air/README.md
  - ../../../tests/domains/atmosphere/README.md
  - ../../../tools/validators/domains/atmosphere/README.md
  - ../../../pipeline_specs/air/README.md
  - ../../../pipeline_specs/atmosphere/README.md
  - ../../../pipelines/domains/air/README.md
  - ../../../pipelines/domains/atmosphere/README.md
  - ../../../contracts/policy/policy_input_bundle_profile_v1.md
  - ../../../contracts/policy/policy_decision_vocabulary.md
  - ../../../contracts/policy/policy_decision_semantics_profile_v1.md
  - ../../../contracts/policy/policy_reviewer_role_vocabulary.md
  - ../../decision/vocabulary.v1.json
  - ../../decision/reviewer_roles.v1.json
  - ../../../packages/policy-runtime/README.md
  - ../../../policy/bundles/README.md
  - ../../../data/registry/sources/atmosphere/README.md
  - ../../../data/proofs/atmosphere/README.md
  - ../../../release/candidates/atmosphere/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/doctrine/ai-build-operating-contract.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../.github/workflows/policy-test.yml
  - ../../../.github/workflows/domain-atmosphere.yml
tags:
  - kfm
  - policy
  - air
  - atmosphere
  - compatibility
  - slug-drift
  - alias
  - redirect
  - migration
  - anti-collapse
  - source-role
  - knowledge-character
  - rights
  - sensitivity
  - stale-state
  - low-cost-sensor
  - exact-station-generalization
  - official-authority-redirect
  - finite-outcomes
  - no-network
  - release-gated
  - correction
  - rollback
notes:
  - "This revision changes only policy/domains/air/README.md plus the required AI-generated provenance receipt."
  - "No Rego or YAML rule, policy value, numeric threshold, bundle, evaluator, schema, contract, fixture, test, validator, workflow, source record, lifecycle object, proof, release artifact, deployment, alias, or public behavior is created or changed."
  - "File presence, a proposed default, a passing fixture workflow, and a generated receipt are not policy activation, approval, proof, release, or publication."
  - "Main advanced during authoring only through policy/bundles/README.md; the Air target and all Air/Atmosphere inventories remained unchanged, and this snapshot incorporates the updated documentation-only bundle boundary."
  - "KFM is not an AQI, medical, regulatory, emergency-alerting, or life-safety issuing authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Air Policy Compatibility Boundary

> **One-line purpose.** Keep `policy/domains/air/` non-authoritative, direct new Atmosphere policy work to [`policy/domains/atmosphere/`](../atmosphere/README.md), and prevent an unresolved alias from becoming a second rule source, bundle selector, public route, or truth path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.3" src="https://img.shields.io/badge/version-v0.3-informational">
  <img alt="Authority: compatibility only" src="https://img.shields.io/badge/authority-compatibility__only-orange">
  <img alt="Direct lane: two blobs" src="https://img.shields.io/badge/direct__lane-2__blobs-blue">
  <img alt="Atmosphere policy: proposed stubs" src="https://img.shields.io/badge/atmosphere__policy-proposed__stubs-orange">
  <img alt="Validation: fixture bounded" src="https://img.shields.io/badge/validation-fixture__bounded-8250df">
  <img alt="Runtime: unimplemented" src="https://img.shields.io/badge/runtime-unimplemented-critical">
  <img alt="Default: fail closed" src="https://img.shields.io/badge/default-fail__closed-critical">
</p>

> [!IMPORTANT]
> **This lane is a compatibility boundary, not an active policy source.** Its tracked marker and README do not select a rule set, emit a decision, authorize an operation, or create a public alias.

> [!CAUTION]
> **The preferred Atmosphere lane is not ready to activate.** Its thirteen Rego files are explicitly proposed, default-only scaffolds with inconsistent result relations and duplicate concepts. No native Rego tests, accepted bundle payload, evaluator binding, or runtime implementation was verified.

> [!WARNING]
> **A successful Atmosphere fixture workflow proves only its declared bounded profile.** It does not prove policy enforcement, scientific or regulatory validity, source admission, an EvidenceBundle or ProofPack, promotion, release, deployment, publication, medical guidance, emergency alerting, or life-safety authority.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status-and-repository-evidence) · [Alias contract](#air-to-atmosphere-compatibility-contract) · [Belongs](#what-belongs-here) · [Inventory](#preferred-atmosphere-policy-inventory) · [Doctrine](#atmosphereair-policy-spine) · [Inputs](#minimum-policy-input-contract) · [Decisions](#decision-vocabulary-and-normalization) · [Codes](#reason-codes-and-obligations) · [Public surfaces](#public-surface-contract) · [Validation](#validation-tests-and-ci) · [Review](#review-burden-and-separation-of-duties) · [Migration](#migration-correction-and-rollback) · [Related](#related-folders) · [Conflicts](#conflict-register) · [Sequence](#smallest-sound-resolution-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Purpose

`policy/domains/air/` exists to make unresolved namespace drift visible and safe. It does not own Atmosphere domain meaning, machine shapes, source records, evidence, runtime logic, release state, or public presentation.

Its durable question is:

> When a caller encounters the historical `air` segment, how does KFM preserve one governed Atmosphere policy path without inventing authority, evaluating two rule sets, losing provenance, or weakening a denial, restriction, review, correction, or rollback obligation?

### In scope

- documenting the current `air`/`atmosphere` conflict;
- pointing contributors and internal tooling to the preferred Atmosphere lane;
- preventing duplicate discovery, bundle creation, evaluation, and public exposure;
- defining non-authoritative alias and migration invariants;
- preserving source, evidence, rights, sensitivity, time, review, release, correction, and rollback references;
- truth-labeling the maturity of adjacent Atmosphere contracts, schemas, tests, validators, workflows, and pipelines;
- recording the review and proof needed before any alias or migration can activate.

### Out of scope

- executable Atmosphere policy;
- policy values, thresholds, scoring, or regulatory interpretation;
- semantic-contract or JSON Schema authority;
- live-source acquisition, transformation, or validation;
- an active bundle, selector, evaluator, or runtime;
- release, deploy, publication, correction, or withdrawal execution;
- AQI, medical, regulatory, emergency, or life-safety instructions;
- resolving the namespace by documentation alone.

### Non-goals

This README does not:

1. rename or delete a lane;
2. declare a public redirect;
3. normalize repository paths at runtime;
4. accept the current Rego defaults;
5. certify the adjacent fixture profiles;
6. authorize an AtmosphereAirDecisionEnvelope;
7. assign functional stewards;
8. change any policy, workflow, release, or publication state.

[Back to top](#top)

---

## Authority level

**Compatibility documentation only / no policy authority / no release authority / no publication authority.**

[ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) accepts the exact Directory Rules v2 text as repository placement authority. Under those rules, the singular `policy/` root owns normative allow, deny, restrict, abstain, redaction, sensitivity, promotion-adjacent, and release-adjacent decisions. The unresolved issue here is the domain segment and its migration—not the responsibility root.

| Concern | Authority home | Role of this lane |
|---|---|---|
| Domain meaning | Accepted Atmosphere doctrine and semantic contracts | Link only |
| Machine shape | `schemas/` | Link only |
| Source identity, role, rights, and cadence | Governed source registry | Require context; never invent it |
| Evidence and proof | EvidenceRef, EvidenceBundle, receipt, and proof families | Preserve references; never manufacture closure |
| Policy source | Accepted lane under `policy/` | Redirect contributors; contain no executable source |
| Policy bundle and evaluator | Accepted bundle/runtime boundaries | Record prerequisites; select nothing |
| Tests and validators | `tests/` and `tools/validators/` | Report observed maturity |
| Pipeline behavior | `pipeline_specs/` and `pipelines/` | No execution role |
| Release, correction, withdrawal, rollback | `release/` and governed records | Preserve identity; approve nothing |
| API, UI, map, export, report, AI | Governed application surfaces | Must not expose repository-path choice as authority |
| CI | `.github/workflows/` | Evidence of declared checks, never activation by itself |

### Governing order

When sources conflict, apply the most recent accepted authority in this order:

1. KFM core invariants and accepted operating law;
2. accepted ADRs;
3. accepted Directory Rules and root registry;
4. an accepted Air-to-Atmosphere namespace/migration decision;
5. accepted Atmosphere policy, sensitivity, source, rights, and public-serving doctrine;
6. accepted contracts, schemas, vocabularies, policy bundles, and evaluator profiles;
7. released artifacts and their correction/rollback records;
8. this compatibility README;
9. proposed scaffolds, examples, fixtures, and workflow holds.

A lower-ranked artifact cannot weaken a higher-ranked denial, restriction, attribution, evidence, review, release, correction, or rollback requirement.

### Ownership boundary

[`.github/CODEOWNERS`](../../../.github/CODEOWNERS) routes `/policy/` review to `@bartytime4life`. That is **CONFIRMED review routing**, not proof that one person holds every Atmosphere, rights, sensitivity, security, runtime, release, or publication role. Functional stewardship and separation of duties remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

## Status and repository evidence

All counts below are complete for the untruncated tree at `main@f61d9df6409917610fa45d739fab55cab86f5eb2`. They describe tracked repository state, not deployed state.

### Direct Air lane

`policy/domains/air/` contains exactly two tracked blobs:

~~~text
policy/domains/air/
├── .gitkeep        # empty marker
└── README.md       # this compatibility boundary
~~~

**Safe conclusion:** no direct Rego, data, manifest, selector, bundle, test, validator, workflow, or runtime file exists in this lane.

### Maturity matrix

| Surface | Pinned inventory | Maturity | What may safely be claimed |
|---|---:|---|---|
| `policy/domains/air/` | 2 blobs | Compatibility only | Marker + README; no executable policy |
| `policy/domains/atmosphere/` | 14 blobs | 1 README + 13 PROPOSED default-only Rego scaffolds | Preferred source lane exists; enforcement does not |
| `policy/sensitivity/atmosphere/` | 1 empty marker | Placeholder | No domain sensitivity rule |
| `contracts/air/` | README + marker | Compatibility only | Contract alias remains visible |
| `contracts/domains/atmosphere/` | 44 blobs | Mixed draft/proposed | Substantial semantics exist; acceptance and alignment vary |
| `schemas/contracts/v1/domains/atmosphere/` | 76 blobs | Mixed, duplicated naming | Machine-shape candidates exist; one namespace is not established here |
| `tests/domains/air/` | README + marker | Compatibility only | No executable Air tests |
| `tests/domains/atmosphere/` | 39 blobs; 16 Python files | 7 substantive + 8 placeholder test modules + empty `__init__`; remaining blobs are documentation/markers | Bounded behaviors are partly executable |
| `tools/validators/domains/atmosphere/` | 24 blobs, including 20 validator modules | 10 substantive + 10 placeholders | Bounded fixture checks exist; broad validation does not |
| `pipeline_specs/air/` | README + marker | Compatibility only | No active Air spec |
| `pipeline_specs/atmosphere/` | README + 5 small YAML stubs | Proposed | Declarative pipeline surface is not implemented |
| `pipelines/domains/air/` | README + marker | Compatibility only | No executable Air pipeline |
| `pipelines/domains/atmosphere/` | 16 blobs; Python entry files are tiny placeholders | Scaffold | No production pipeline may be inferred |
| `policy/bundles/` | 2 documentation files; one PROPOSED_INACTIVE packaging profile | Documentation-only direct lane | No accepted Atmosphere bundle payload or active selector |
| policy runtime core | One comment-only source file | Unimplemented | No evaluator |
| Atmosphere release candidate lane | README only | Non-release | No released candidate |

### Evidence boundary

This README may establish tracked presence, exact inspected content, and the stated behavior of checked-in workflows. It cannot establish:

- production deployment or runtime selection;
- branch-protection or required-check significance;
- complete off-repository consumers;
- scientific, medical, regulatory, or legal correctness;
- source authorization or live-source currentness;
- accepted steward assignments;
- policy or contract acceptance;
- EvidenceBundle or ProofPack validity;
- promotion, release, publication, or life-safety authority.

Those claims remain `UNKNOWN` or `NEEDS VERIFICATION` until direct evidence closes them.

[Back to top](#top)

---

## Air-to-Atmosphere compatibility contract

The placement preference is `atmosphere` for new work. A separately accepted namespace/migration decision was not verified, so the `air` lane remains visible as a guardrail rather than silently disappearing.

### Compatibility invariants

Until that decision exists:

1. **One active source.** At most one segment may supply evaluated Atmosphere rules.
2. **One package contract.** Alias handling cannot produce independent package namespaces or entrypoints.
3. **One bundle identity.** Equivalent content cannot produce separate bundle IDs or digests by slug.
4. **One evaluation.** A request cannot execute both lanes and merge, race, or prefer whichever returns first.
5. **One normalized decision.** Repository-path choice cannot change decision meaning.
6. **No path activation.** A directory, README, Rego filename, or proposed default does not activate policy.
7. **No silent fallback.** Missing preferred policy cannot fall through to an unreviewed compatibility source.
8. **No public path selection.** Public callers cannot choose `air` to bypass Atmosphere policy.
9. **No lifecycle bypass.** Alias resolution cannot admit, promote, release, restore, or publish an object.
10. **No provenance rewrite.** SourceDescriptor, EvidenceRef, receipt, proof, release, correction, and rollback identities survive migration.
11. **Most restrictive rule wins.** Rights, sensitivity, audience, join, freshness, lifecycle, and release restrictions are preserved.
12. **No semantic collapse.** AQI, concentration, AOD, PM2.5, model, observation, calibration, advisory, and official warning remain distinct.
13. **No authority impersonation.** KFM does not become a medical, regulatory, emergency, or life-safety issuer through an alias.

### Required resolution flow

~~~mermaid
flowchart LR
    A[Caller requests air or atmosphere] --> B{Accepted namespace map?}
    B -- No --> C[ABSTAIN or bounded configuration ERROR]
    B -- Yes --> D[Resolve one canonical logical domain]
    D --> E{Accepted bundle + evaluator + input profile?}
    E -- No --> F[Fail closed]
    E -- Yes --> G[Evaluate exactly once]
    G --> H[Normalize to accepted PolicyDecision]
    H --> I[Apply obligations in governed consumer]
    I --> J{Separate release/publication approval?}
    J -- No --> K[No state transition]
    J -- Yes --> L[Governed release path]
~~~

The exact `ABSTAIN` versus `ERROR` branch is not settled by this README; it depends on the accepted decision-semantics profile and whether the condition is an intentional policy non-answer or an execution/configuration failure.

### Forbidden shortcut

~~~text
repository path exists
  → path is treated as active policy
  → public caller chooses a slug
  → unbound Rego default is evaluated
  → green fixture check is treated as approval
  → result is rendered or released
~~~

Every arrow in that shortcut crosses an unproved authority boundary.

[Back to top](#top)

---

## What belongs here

Accepted content is deliberately narrow:

- this README;
- an empty compatibility marker;
- an ADR pointer;
- non-executable alias, deprecation, migration, or tombstone metadata **after** its schema and activation semantics are accepted;
- byte-complete migration inventories and identity maps;
- checksums and rollback targets;
- reviewer instructions;
- links to drift, correction, and supersession records.

Any future non-marker file must state:

- its object kind and non-authoritative status;
- the preferred target path;
- whether it can be discovered by runtime code—the default is no;
- its owner and review state;
- activation and expiry conditions;
- correction and rollback behavior;
- whether public clients can read it—the default is no.

## What does not belong here

| Material | Correct responsibility home |
|---|---|
| Atmosphere Rego or equivalent source | [`policy/domains/atmosphere/`](../atmosphere/README.md), after accepted design/review |
| Active bundle or manifest | Accepted `policy/bundles/` lane |
| Evaluator/runtime implementation | Accepted package/runtime boundary |
| Policy input or decision instances | Governed audit/receipt surfaces |
| Semantic contracts | `contracts/` |
| JSON Schemas | `schemas/` |
| Sources, rights records, or payloads | Governed registry and data lifecycle roots |
| Fixtures and executable tests | `fixtures/` and `tests/domains/atmosphere/` |
| Validators | `tools/validators/domains/atmosphere/` |
| Pipeline specs or transforms | `pipeline_specs/atmosphere/` and `pipelines/domains/atmosphere/` |
| Receipts and proofs | `data/receipts/` and `data/proofs/` |
| Release/correction/withdrawal objects | `release/` |
| API, UI, MapLibre, report, export, or AI behavior | Governed application/runtime roots |
| Official AQI, medical, regulatory, emergency, or life-safety direction | The applicable official issuing authority |

Adding executable policy here before a separately accepted namespace decision would create parallel authority and must fail review.

[Back to top](#top)

---

## Preferred Atmosphere policy inventory

The preferred lane contains exactly one README and thirteen Rego files at the pinned tree.

| File | Declared relation/default | Inspected implementation status |
|---|---|---|
| [`abstain_on_ambiguous.rego`](../atmosphere/abstain_on_ambiguous.rego) | `deny := false` | PROPOSED default-only scaffold; name/result mismatch |
| [`deny_unpublished.rego`](../atmosphere/deny_unpublished.rego) | `deny := false` | PROPOSED default-only scaffold |
| [`advisory-not-alert.rego`](../atmosphere/advisory-not-alert.rego) | `allow := false` | PROPOSED default-only scaffold |
| [`advisory_no_life_safety.rego`](../atmosphere/advisory_no_life_safety.rego) | `allow := false` | PROPOSED default-only scaffold; overlaps preceding concept |
| [`aod-not-pm25.rego`](../atmosphere/aod-not-pm25.rego) | `allow := false` | PROPOSED default-only scaffold |
| [`aod_is_not_pm25.rego`](../atmosphere/aod_is_not_pm25.rego) | `allow := false` | PROPOSED default-only scaffold; overlaps preceding concept |
| [`aqi_is_not_concentration.rego`](../atmosphere/aqi_is_not_concentration.rego) | `allow := false` | PROPOSED default-only scaffold |
| [`dryrun_no_live_fetch.rego`](../atmosphere/dryrun_no_live_fetch.rego) | `allow := false` | PROPOSED default-only scaffold |
| [`freshness_gate.rego`](../atmosphere/freshness_gate.rego) | `allow := false` | PROPOSED default-only scaffold |
| [`low_cost_sensor_caveats_required.rego`](../atmosphere/low_cost_sensor_caveats_required.rego) | `allow := false` | PROPOSED default-only scaffold |
| [`model-as-observed-deny.rego`](../atmosphere/model-as-observed-deny.rego) | `allow := false` | PROPOSED default-only scaffold |
| [`model_is_not_observation.rego`](../atmosphere/model_is_not_observation.rego) | `allow := false` | PROPOSED default-only scaffold; overlaps preceding concept |
| [`source_role_required.rego`](../atmosphere/source_role_required.rego) | `allow := false` | PROPOSED default-only scaffold |

### Confirmed limitations

- no file contains an operative rule body beyond its default and comments;
- result relations are inconsistent: two expose `deny` while eleven expose `allow`;
- package naming is not unified;
- three concept families have duplicate or near-duplicate filenames;
- `abstain_on_ambiguous.rego` does not expose an abstain relation;
- no native Atmosphere Rego test was verified;
- no accepted entrypoint, input shape, result adapter, bundle manifest, bundle digest, selector, or evaluator binding was verified;
- the sibling README remains a short proposed scaffold and overstates what material may live under `policy/`;
- the policy runtime is not implemented and `policy/bundles/` has no accepted active payload.

### Hardening required before activation

1. accept one package namespace and one entrypoint/result contract;
2. remove or supersede duplicate concepts with explicit migration history;
3. bind exact shared or domain-specific input and decision contracts;
4. implement rules beyond defaults;
5. define deterministic reason and obligation mapping;
6. add native positive, negative, ambiguous, missing-input, and invalid-input Rego tests;
7. add bundle manifest, content digest, evaluator compatibility, and selector rules;
8. prove no-network execution and deterministic time handling;
9. integrate governed consumers without repository-path selection;
10. separate policy acceptance from promotion, release, deploy, and publication;
11. exercise correction and rollback against an exact prior bundle;
12. preserve the official-authority boundary.

[Back to top](#top)

---

## Atmosphere/Air policy spine

Any future accepted policy, regardless of its final slug, must preserve knowledge character and trust boundaries.

### Anti-collapse rules

| Boundary | Required posture |
|---|---|
| AQI vs pollutant concentration | Never present an index/report object as a concentration observation |
| AOD/smoke raster vs PM2.5 | Never present modeled or remotely sensed context as a PM2.5 measurement |
| Model/forecast vs observation | Keep role and knowledge-character labels explicit |
| Calibration vs observation | Calibration metadata supports interpretation; it is not the observation |
| Low-cost sensor vs regulatory monitor | Preserve source role, caveats, correction state, confidence, and limitations |
| Advisory context vs official warning | Do not issue life-safety direction; point to an approved official source when allowed |
| Stale vs current | Require explicit temporal and freshness state |
| Aggregate vs exact station | Never re-expand generalized output into sensitive station/property/infrastructure detail |
| Map layer vs evidence | Tiles, rasters, contours, legends, and styles are carriers, not authority |
| Cross-domain context vs canonical claim | Atmosphere may support another domain without silently owning its claims |

### Rights and sensitivity

Future policy must fail closed when source terms, license, attribution, redistribution, written-permission, confidentiality, or audience rights are missing or unresolved.

The most restrictive applicable posture must survive:

- joins across sources and domains;
- geometry generalization;
- aggregation;
- caching;
- export and report generation;
- correction and withdrawal;
- bundle or slug migration.

Exact station siting may require generalization when private land, sensitive infrastructure, or re-identification risk is plausible. Generalization does not grant a less restrictive audience or release state.

### Time and freshness

A policy input must distinguish, where applicable:

- observed time;
- valid time;
- issue time;
- retrieval time;
- processing time;
- source cadence;
- source-specific stale-after or currentness state;
- historical, current, modeled, and forecast context.

No policy may infer current operational conditions from stale or time-ambiguous material.

### Official-authority boundary

When asked for emergency action, health protection, official AQI guidance, regulatory status, or other consequential direction, KFM must not fabricate or impersonate the issuing authority. A governed consumer may provide a bounded non-answer or denial and an approved official reference without exposing restricted details.

[Back to top](#top)

---

## Minimum policy input contract

A decision cannot be made from a path string or filename.

### Shared candidate profile

The checked-in `PolicyInputBundle` profile is `PROPOSED_INACTIVE`, fixture-only, and non-evaluator. It currently enumerates five operations—`ANSWER`, `RENDER`, `EXPORT`, `PROMOTE`, and `RELEASE`—and seven audiences—`PUBLIC`, `RESTRICTED_REVIEW`, `STEWARD`, `INTERNAL`, `AI_ADAPTER`, `MAP_RUNTIME`, and `RELEASE_GATE`. Every authority flag remains false.

That profile is useful evidence of candidate vocabulary. It is not an accepted runtime contract.

### Required input families

| Family | Minimum posture |
|---|---|
| Request | Stable request/correlation identity and declared operation |
| Domain | Logical domain plus accepted canonical/compatibility mapping |
| Caller | Governed service/user identity and capabilities where applicable |
| Audience | One accepted audience value |
| Object and source role | Object family, role, knowledge character, and provenance |
| Rights | License, attribution, redistribution, consent, confidentiality, and review state |
| Evidence | EvidenceRef/EvidenceBundle state and validation references |
| Time | Observed, valid, issue, retrieval, processing, cadence, and freshness fields as applicable |
| Sensitivity | Precision, station/private-land/infrastructure exposure, join and re-identification risk |
| Policy | Exact bundle ID/version/digest, evaluator profile, entrypoint, and activation state |
| Lifecycle/release | Candidate/released/superseded/withdrawn state, manifest, correction, and rollback refs |
| Migration | Decision ref, alias map, effective state, and exact rollback target |
| Trace | Audit-safe trace without credentials, raw payloads, or protected geometry |

### Missing-input posture

- missing evidence, rights, sensitivity, audience, or freshness context fails closed;
- an unresolved alias is not guessed;
- a missing bundle/evaluator is an execution/configuration condition, not permission;
- absence of a denial rule is not an allow;
- unsupported official-authority requests do not become advice;
- diagnostics disclose only what the caller is authorized to see.

[Back to top](#top)

---

## Decision vocabulary and normalization

### Shared candidate outcome surface

The checked-in shared decision vocabulary and semantics profile are `PROPOSED_INACTIVE`. Their outward result surface is finite:

- `ANSWER`
- `ABSTAIN`
- `DENY`
- `ERROR`

The vocabulary explicitly does **not** claim policy evaluation, decision emission, promotion authorization, release authorization, or publication authorization.

### Compatibility dispositions are not new outcomes

Terms such as `REDIRECT`, `HOLD`, `RESTRICT`, `ALLOW`, and `REVIEW` are useful internal documentation or workflow dispositions. They must not leak as extra public outcomes unless an accepted contract adds them.

| Internal condition | Safe normalization requirement |
|---|---|
| Accepted alias map rewrites `air` to the canonical logical domain | Resolve before evaluation; do not emit `REDIRECT` as policy |
| Namespace map absent or intentionally unsupported | `ABSTAIN` or `ERROR` according to accepted semantics; never guess |
| Required context unresolved | Fail closed; commonly `ABSTAIN` or `DENY` depending on accepted rule |
| Answer allowed only with enforceable duties | `ANSWER` plus registered obligations; otherwise fail closed |
| Policy bundle/evaluator unavailable | `ERROR` or accepted fail-closed equivalent; never `ANSWER` |
| Explicit prohibition | `DENY` with safe registered reasons |
| Promotion/release/publication requested | A policy result may be necessary but is never sufficient for the state transition |

Normalization must be deterministic, authenticated, replayable against exact input/bundle identities, and safe for the caller's audience.

[Back to top](#top)

---

## Reason codes and obligations

### Shared reason-code candidates

The current inactive registry contains exactly nine reason codes:

- `CONSENT_REQUIRED`
- `EVIDENCE_STALE`
- `EVIDENCE_UNRESOLVED`
- `OPERATION_ALLOWED_WITH_OBLIGATIONS`
- `POLICY_BUNDLE_UNAVAILABLE`
- `POLICY_INPUT_INCOMPLETE`
- `PUBLIC_PRECISION_UNSAFE`
- `RIGHTS_UNKNOWN`
- `SENSITIVITY_UNRESOLVED`

### Shared obligation candidates

The inactive registry contains exactly eight obligations, all currently associated with `ANSWER`:

- `ATTACH_CITATIONS`
- `ATTACH_RIGHTS_NOTICE`
- `DELAY_PUBLICATION`
- `GENERALIZE_GEOMETRY`
- `REDACT_EXACT_LOCATION`
- `REQUIRE_STEWARD_REVIEW`
- `VERIFY_ROLLBACK_TARGET`
- `WITHHOLD_EXPORT`

These codes are candidate shared vocabulary, not proof of an active registry or handler.

### Air-local documentation terms

Phrases such as `alias_unresolved`, `redirect_required`, `source_role_missing`, `official_authority_required`, `preserve_caveat`, or `attach_freshness_label` may clarify this README, tests, or migration design. They are **not registered reason codes or obligations** unless separately accepted into the canonical vocabulary with schemas, handlers, tests, and versioning.

Downstream code must never branch on README-only prose.

[Back to top](#top)

---

## Public-surface contract

Public clients consume governed logical services and released artifacts—not repository paths, Rego packages, workflow holds, or raw evaluator output.

| Surface | Required behavior |
|---|---|
| API | Accept governed domain/operation inputs; never expose a caller-selectable policy path |
| Explorer UI | Show knowledge character, source role, time/freshness, caveats, and citations that policy requires |
| MapLibre | Treat map layers as presentations; preserve source/rights/sensitivity and precision obligations |
| Export/report | Enforce withholding, redaction, generalization, attribution, and release state |
| Governed AI | Cite or abstain; preserve uncertainty and policy obligations; do not invent official advice |
| Cache | Key by policy/bundle/version and invalidate on correction, withdrawal, rights, or policy changes |
| Error handling | Reveal no credentials, restricted payloads, protected geometry, or policy-sensitive internals |

### Non-bypass rule

A public or downstream caller must not be able to obtain a different result by:

- submitting `air` instead of `atmosphere`;
- addressing a Rego package directly;
- omitting audience, evidence, rights, sensitivity, or freshness context;
- calling a fixture workflow;
- reading a proposed schema or README as released truth;
- replaying a stale bundle after correction or withdrawal.

### State-transition rule

An allowed or answered policy result is never, by itself, approval to promote, release, deploy, or publish. Those are separately governed, reviewable, reversible transitions.

[Back to top](#top)

---

## Validation, tests, and CI

Current Atmosphere validation is mixed. The bounded executable slices are useful; their limits must remain visible.

### Native policy validation

| Check | Current state |
|---|---|
| Atmosphere Rego sources | 13 proposed default-only scaffolds |
| Native Rego tests | 0 verified |
| Accepted package/entrypoint | Not verified |
| Bundle build/digest | Not verified |
| Evaluator compatibility | Not verified |
| PolicyDecision adapter | Not verified |
| Obligation handlers | Not verified |
| Runtime core | Comment-only placeholder |
| Broad policy workflow | Readiness/drift guard; no Rego evaluation or decision emission |

### Atmosphere Python tests

Seven modules contain substantive deterministic tests:

- `test_atmosphere_smoke.py` — synthetic precipitation-profile behavior despite the broad filename;
- `test_correctable_environmental_event_assessment.py`;
- `test_knowledge_character_registry.py`;
- `test_low_cost_sensor_caveat_required.py`;
- `test_observed_modeled_separation.py`;
- `test_pm25_trigger_candidate_assessment.py`;
- `test_prescribed_burn_quality_flag.py`.

Eight modules are explicit placeholders or docstring-only surfaces:

- `test_advisory_no_life_safety.py`;
- `test_aod_as_pm25_denied.py`;
- `test_aqi_as_concentration_denied.py`;
- `test_decision_envelope_finite_outcomes.py`;
- `test_dryrun_no_live_fetch.py`;
- `test_model_as_observed_denied.py`;
- `test_temporal_fields_distinct.py`;
- `test_unit_normalization.py`.

The zero-byte `__init__.py` is packaging only.

### Atmosphere validators

Ten modules contain substantive bounded logic:

- `airnow_aqs_reconciliation/validate_reconciliation.py`;
- `validate_correctable_environmental_event_assessment.py`;
- `validate_knowledge_character.py`;
- `validate_low_cost_sensor_caveats.py`;
- `validate_observed_modeled_separation.py`;
- `validate_pm25_sensor_colocation_manifest.py`;
- `validate_pm25_trigger_candidate_assessment.py`;
- `validate_pm_sensor_trust_profile.py`;
- `validate_prescribed_burn_quality_flag.py`;
- `validate_public_safe_precipitation_fixture.py`.

Ten remain placeholders:

- `validate_air_observation.py`;
- `validate_aod_raster.py`;
- `validate_atmosphere_decision_envelope.py`;
- `validate_catalog_matrix.py`;
- `validate_evidence_bundle.py`;
- `validate_forecast_context.py`;
- `validate_parameter_units.py`;
- `validate_schema.py`;
- `validate_smoke_context.py`;
- `validate_source_descriptor.py`.

### Relevant no-network workflows

| Workflow | Bounded executable claim | Explicitly withheld |
|---|---|---|
| [`domain-atmosphere.yml`](../../../.github/workflows/domain-atmosphere.yml) | Orchestrates declared fixture profiles and maturity checks | Live fetch, policy decision, proof, release, deploy, publication |
| [`atmosphere-airnow-aqs-reconciliation.yml`](../../../.github/workflows/atmosphere-airnow-aqs-reconciliation.yml) | Fixture reconciliation | Live EPA/KDHE use, admission, certification, alerting, publication |
| [`atmosphere-aqs-site-delta.yml`](../../../.github/workflows/atmosphere-aqs-site-delta.yml) | Fixture site-delta profile | Live source, lifecycle write, policy, guidance, release |
| [`correctable-environmental-event-assessment.yml`](../../../.github/workflows/correctable-environmental-event-assessment.yml) | Synthetic event-assessment profile | Real event, threshold, correction authority, deploy |
| [`pm-sensor-trust-profile.yml`](../../../.github/workflows/pm-sensor-trust-profile.yml) | Fixture trust-profile checks | Live sensor, scientific validity, reference equivalence, health authority |
| [`pm25-sensor-colocation-manifest.yml`](../../../.github/workflows/pm25-sensor-colocation-manifest.yml) | Fixture manifest checks | Source admission, policy, promotion, publication |
| [`pm25-trigger-candidate-assessment.yml`](../../../.github/workflows/pm25-trigger-candidate-assessment.yml) | Synthetic candidate assessment | Numeric threshold, AQI/health advice, regulatory decision, deploy |

### What green means

A green run supports only the exact checked-in fixture, validator, assertion, and workflow boundary. It does not upgrade `PROPOSED` to `ACCEPTED`, bind an evaluator, validate live currentness, approve source use, create proof, or authorize a state transition.

### Minimum future policy test matrix

An activatable policy lane needs deterministic positive and negative coverage for:

- canonical and compatibility slugs;
- duplicate discovery and double evaluation;
- missing/invalid/ambiguous inputs;
- AQI/concentration, AOD/PM2.5, model/observation, and calibration/observation collapse;
- low-cost-sensor caveats and correction state;
- rights, attribution, consent, confidentiality, and audience restrictions;
- exact-station generalization and sensitive joins;
- all temporal fields and stale-state boundaries;
- official-authority requests;
- every accepted reason code and obligation;
- bundle/evaluator version mismatch;
- correction, withdrawal, cache invalidation, and rollback;
- network denial and safe diagnostic output.

[Back to top](#top)

---

## Decision-envelope alignment gap

[`AtmosphereAirDecisionEnvelope.md`](../../../contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md) is a semantic draft. It explicitly does not establish a PolicyDecision, EvidenceBundle, release decision, or runtime proof.

Its lower-case machine-shape counterpart, [`atmosphere_air_decision_envelope.schema.json`](../../../schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json), exists but is a minimal `PROPOSED` scaffold whose fields remain to be defined. The dedicated validator and finite-outcome test are placeholders.

Therefore:

- contract prose is not validated by the current schema;
- schema presence is not acceptance;
- finite outcome claims are not executable proof;
- no public or release consumer should accept this envelope until semantic, schema, validator, test, policy, and runtime layers align.

[Back to top](#top)

---

## Review burden and separation of duties

Alias and namespace changes are governance-significant because they can alter policy discovery even when the diff looks like path cleanup.

### Candidate reviewer roles

The shared reviewer-role vocabulary is `PROPOSED_INACTIVE` and currently names:

- `DOMAIN_STEWARD`
- `EVIDENCE_STEWARD`
- `POLICY_STEWARD`
- `RELEASE_STEWARD`
- `SECURITY_PRIVACY_REVIEWER`

Its role-assignment, approval-recording, policy, promotion, release, and publication authority flags are all false.

### Review matrix

| Change | Required review capability |
|---|---|
| README clarification | Policy + Atmosphere/Air + docs |
| Alias/migration metadata | Policy + directory governance + runtime |
| Canonical namespace decision | Architecture + policy + domain + affected-root owners |
| Rego/package change | Policy + domain + security/privacy + test |
| Bundle/selector/evaluator change | Policy runtime + policy + security |
| Rights/sensitivity behavior | Source/rights + sensitivity/privacy |
| Public route/export behavior | Surface owner + policy + release |
| Official-authority behavior | Domain + hazards/life-safety boundary + security |
| Release/correction/rollback mapping | Release + independent reviewer |

These are capability requirements, not assertions that named people are assigned.

### Separation rules

- the author is not the sole approver;
- path migration is separate from bundle activation;
- bundle activation is separate from policy acceptance;
- tests are separate from approval;
- policy acceptance is separate from promotion and release;
- release is separate from publication;
- correction and rollback remain independently executable;
- a README merge or generated receipt cannot activate an alias.

### Reviewer checklist

- [ ] Evidence is pinned to a current complete tree.
- [ ] The Air lane remains non-executable.
- [ ] No duplicate or newly active Atmosphere rule source is introduced.
- [ ] Package namespace, entrypoint, input, and result contracts are explicit.
- [ ] Bundle/evaluator/selector identities are deterministic.
- [ ] Alias handling evaluates once and fails closed.
- [ ] Rights, sensitivity, freshness, evidence, review, release, correction, and rollback survive migration.
- [ ] Public consumers cannot select repository paths.
- [ ] Official-authority boundaries are tested.
- [ ] Logs and errors expose no protected detail.
- [ ] Rollback identifies an exact prior known-good state.
- [ ] Receipts remain provenance, not approval.

[Back to top](#top)

---

## Migration, correction, and rollback

### Decision required

ADR-0029 settles directory-rule authority; it does **not**, by itself, prove an accepted Air-to-Atmosphere migration plan. A separately accepted decision should specify:

- canonical segment and affected roots;
- package, object, schema, fixture, and route namespaces;
- whether an alias is permitted and for how long;
- bundle and selector behavior;
- consumer migration;
- public compatibility posture;
- deprecation milestones;
- review and activation duties;
- correction and rollback behavior.

### Migration record

| Field | Requirement |
|---|---|
| `migration_id` | Stable identity |
| `decision_ref` | Accepted governing decision |
| `source_paths` | Exact `air` paths and blob/digest identities |
| `target_paths` | Exact `atmosphere` paths and expected identities |
| `identity_map` | Package, schema, object, fixture, route, bundle, and release mappings |
| `consumers` | Complete known internal and public consumer inventory |
| `bundle_before` / `bundle_after` | ID, version, digest, selector, evaluator |
| `review_state` | Recorded independent reviews/approvals |
| `effective_at` / `expires_at` | Activation and compatibility lifetime |
| `validation_refs` | Tests, reports, runs, and receipts |
| `rollback_target` | Exact prior selector, bundle, and repository state |
| `public_impact` | API/UI/map/export/report/AI effects |
| `correction_refs` | Corrections, supersessions, or withdrawals |

### Correction triggers

Open a correction or rollback review if:

- both segments become active;
- decisions differ only because of slug;
- a selector loads the wrong or stale bundle;
- identity, evidence, source, rights, or release references drift;
- a public route exposes `air` as authority;
- an obligation is dropped during alias handling;
- stale, corrected, superseded, or withdrawn policy remains cached;
- advisory behavior implies medical, regulatory, emergency, or life-safety authority;
- migration makes exact rollback impossible.

### README rollback

For this documentation-only revision, the exact prior blob is:

~~~text
d722464dcce4effeb5f70861bbfb629b8d3aed9d
~~~

Restoring that blob reverts only this README. It does not roll back any future policy, bundle, evaluator, migration, release, deploy, or public behavior.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Parent domain-policy boundary |
| [`../atmosphere/README.md`](../atmosphere/README.md) | Preferred Atmosphere policy lane; currently proposed scaffolds |
| [`../../../docs/domains/atmosphere/CANONICAL_PATHS.md`](../../../docs/domains/atmosphere/CANONICAL_PATHS.md) | Placement preference and drift context |
| [`../../../docs/domains/atmosphere/POLICY.md`](../../../docs/domains/atmosphere/POLICY.md) | Human-facing policy doctrine |
| [`../../../docs/domains/atmosphere/SENSITIVITY.md`](../../../docs/domains/atmosphere/SENSITIVITY.md) | Sensitivity/generalization posture |
| [`../../../contracts/air/README.md`](../../../contracts/air/README.md) | Air contract compatibility lane |
| [`../../../contracts/domains/atmosphere/README.md`](../../../contracts/domains/atmosphere/README.md) | Preferred semantic-contract family |
| [`../../../contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md`](../../../contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md) | Draft semantic envelope |
| [`../../../schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json`](../../../schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json) | Proposed minimal machine-shape scaffold |
| [`../../../tests/domains/air/README.md`](../../../tests/domains/air/README.md) | Air test compatibility lane |
| [`../../../tests/domains/atmosphere/README.md`](../../../tests/domains/atmosphere/README.md) | Mixed executable/placeholder Atmosphere tests |
| [`../../../tools/validators/domains/atmosphere/README.md`](../../../tools/validators/domains/atmosphere/README.md) | Mixed executable/placeholder validators |
| [`../../../pipeline_specs/air/README.md`](../../../pipeline_specs/air/README.md) | Air pipeline-spec compatibility lane |
| [`../../../pipeline_specs/atmosphere/README.md`](../../../pipeline_specs/atmosphere/README.md) | Proposed Atmosphere pipeline-spec lane |
| [`../../../pipelines/domains/air/README.md`](../../../pipelines/domains/air/README.md) | Air executable-pipeline compatibility lane |
| [`../../../pipelines/domains/atmosphere/README.md`](../../../pipelines/domains/atmosphere/README.md) | Atmosphere pipeline scaffold |
| [`../../../contracts/policy/policy_input_bundle_profile_v1.md`](../../../contracts/policy/policy_input_bundle_profile_v1.md) | Inactive shared input profile |
| [`../../../contracts/policy/policy_decision_vocabulary.md`](../../../contracts/policy/policy_decision_vocabulary.md) | Inactive shared decision/reason/obligation vocabulary |
| [`../../../contracts/policy/policy_decision_semantics_profile_v1.md`](../../../contracts/policy/policy_decision_semantics_profile_v1.md) | Inactive shared semantics profile |
| [`../../../contracts/policy/policy_reviewer_role_vocabulary.md`](../../../contracts/policy/policy_reviewer_role_vocabulary.md) | Inactive reviewer-role vocabulary |
| [`../../decision/vocabulary.v1.json`](../../decision/vocabulary.v1.json) | Machine-readable candidate vocabulary |
| [`../../decision/reviewer_roles.v1.json`](../../decision/reviewer_roles.v1.json) | Machine-readable candidate reviewer roles |
| [`../../../packages/policy-runtime/README.md`](../../../packages/policy-runtime/README.md) | Proposed runtime boundary |
| [`../../../policy/bundles/README.md`](../../../policy/bundles/README.md) | Bundle boundary; no accepted payload verified |
| [`../../../data/registry/sources/atmosphere/README.md`](../../../data/registry/sources/atmosphere/README.md) | Source identity/role/rights context |
| [`../../../data/proofs/atmosphere/README.md`](../../../data/proofs/atmosphere/README.md) | Proof boundary; not policy authority |
| [`../../../release/candidates/atmosphere/README.md`](../../../release/candidates/atmosphere/README.md) | Candidate release boundary |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | Accepted placement text via ADR-0029 |
| [`../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Directory Rules adoption decision |
| [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) | Repository drift register |

[Back to top](#top)

---

## Conflict register

| ID | Conflict | Confirmed evidence | Closure condition |
|---|---|---|---|
| `AIRPOL-001` | `air` vs `atmosphere` | Both segments exist across responsibility roots; placement doctrine prefers Atmosphere | Accepted namespace/migration decision |
| `AIRPOL-002` | Compatibility vs source authority | Air has only marker + README; Atmosphere has proposed scaffolds | Keep Air non-executable; accept one source lane |
| `AIRPOL-003` | Rego result contract | 2 `deny` defaults vs 11 `allow` defaults; packages differ | One package/entrypoint/result adapter |
| `AIRPOL-004` | Duplicate concepts | Three near-duplicate filename pairs | Supersession/identity map + tests |
| `AIRPOL-005` | Contract/schema alignment | Rich semantic draft vs minimal proposed schema | Aligned accepted contract/schema |
| `AIRPOL-006` | Envelope execution proof | Validator and finite-outcome test are placeholders | Substantive validator/test + policy/runtime binding |
| `AIRPOL-007` | Shared vocabulary authority | Profiles are `PROPOSED_INACTIVE`; authority flags false | Accepted versioned vocabulary and handlers |
| `AIRPOL-008` | Validation maturity | Bounded fixture profiles coexist with placeholders | Dependency-closed policy test/validator suite |
| `AIRPOL-009` | Bundle/evaluator | No active payload; runtime core placeholder | Immutable bundle + compatible evaluator + selector |
| `AIRPOL-010` | Public alias behavior | No accepted route/consumer binding verified | Contracted, tested, reviewed non-bypass behavior |
| `AIRPOL-011` | Rights/freshness profiles | Domain requirements exist; source-specific rules unverified | Accepted source-specific matrices/tests |
| `AIRPOL-012` | Official-authority boundary | Doctrine/workflows disclaim authority; runtime proof absent | End-to-end governed consumer tests |
| `AIRPOL-013` | Ownership | CODEOWNERS route verified; functional roles unassigned | Recorded steward assignments and separation |
| `AIRPOL-014` | Release/rollback | No accepted slug-aware release mapping or drill | Reviewed mapping + exercised rollback |

This README records conflicts; it resolves none by assertion.

[Back to top](#top)

---

## Smallest sound resolution sequence

1. **Freeze Air expansion.** Keep `policy/domains/air/` marker-and-documentation only.
2. **Record drift.** Bind current paths and identities in the drift register.
3. **Inventory consumers.** Find every repository and deployed reference to both segments.
4. **Accept the namespace decision.** Define canonical segment, affected roots, alias lifetime, and rollback.
5. **Harden the Atmosphere README.** Make its inventory and policy-only boundary exact.
6. **Choose one Rego contract.** One package namespace, entrypoint, result relation, and fail-closed semantics.
7. **Resolve duplicate scaffolds.** Supersede with explicit identity history.
8. **Align contracts and schemas.** Close the decision-envelope gap.
9. **Accept input/decision vocabularies.** Version operations, audiences, reasons, obligations, and reviewer roles.
10. **Implement rules and native tests.** Cover every policy family and failure mode without network access.
11. **Build immutable bundle/evaluator binding.** Pin source, dependencies, version, digest, selector, and compatibility.
12. **Integrate governed consumers.** Preserve obligations; forbid repository-path selection.
13. **Run migration dry-run.** Compare exact decisions and identity continuity under old/new references.
14. **Review independently.** Separate authorship, policy acceptance, activation, release, and publication.
15. **Activate with exact rollback.** Only after accepted evidence; keep correction executable.
16. **Deprecate or tombstone Air.** Preserve only the approved audit/compatibility surface.
17. **Close conflicts with evidence.** Update `AIRPOL-*` items and drift records.

Each step is independently reviewable and reversible. No later step is implied by completion of an earlier one.

[Back to top](#top)

---

## Definition of done

This compatibility boundary is complete only when:

- [ ] functional stewards and reviewer separation are recorded;
- [ ] an accepted namespace/migration decision resolves `air` versus `atmosphere`;
- [ ] tracked and deployed consumers are inventoried;
- [ ] the Air lane contains no executable policy;
- [ ] the Atmosphere lane has one accepted package, entrypoint, input, and result contract;
- [ ] duplicate rule concepts are superseded with identity history;
- [ ] semantic contracts, schemas, validators, and tests align;
- [ ] one immutable bundle/manifest/evaluator/selector chain is accepted;
- [ ] shared reasons, obligations, and reviewer roles are versioned and active;
- [ ] deterministic native policy tests cover positive, negative, missing, ambiguous, invalid, correction, and rollback cases;
- [ ] public API/UI/map/export/report/AI consumers cannot bypass policy by slug;
- [ ] rights, sensitivity, source role, knowledge character, freshness, and obligations survive every consumer;
- [ ] official-authority behavior is bounded and tested;
- [ ] promotion, release, deploy, and publication remain separate approvals;
- [ ] cache invalidation, correction, withdrawal, and rollback are exercised;
- [ ] drift and conflict records close with exact evidence;
- [ ] no sensitive, restricted, medical, regulatory, emergency, or life-safety claim is introduced.

Until then, this lane remains draft, compatibility-only, non-authoritative, and fail-closed.

[Back to top](#top)

---

## Open verification register

| ID | Verification item | Evidence needed |
|---|---|---|
| `AIRPOL-OPEN-001` | Accepted Air-to-Atmosphere decision | Accepted ADR/equivalent with scope and status |
| `AIRPOL-OPEN-002` | Functional owners | Recorded steward assignments; CODEOWNERS alone is insufficient |
| `AIRPOL-OPEN-003` | Deployed consumers | Search/inventory beyond tracked repository |
| `AIRPOL-OPEN-004` | Package and entrypoint | Accepted Rego/runtime contract |
| `AIRPOL-OPEN-005` | Bundle/evaluator/selector | Manifest, digest, compatibility matrix, activation record |
| `AIRPOL-OPEN-006` | Decision-envelope alignment | Accepted semantics + schema + validator + tests |
| `AIRPOL-OPEN-007` | Source rights | Source-specific terms, attribution, redistribution, review |
| `AIRPOL-OPEN-008` | Freshness | Source-specific temporal/currentness rules |
| `AIRPOL-OPEN-009` | Exact-station posture | Generalization and sensitive-infrastructure tests |
| `AIRPOL-OPEN-010` | Low-cost-sensor posture | Caveat, correction, confidence, and source-role profile |
| `AIRPOL-OPEN-011` | Obligation handlers | API/UI/map/export/AI enforcement evidence |
| `AIRPOL-OPEN-012` | Official redirection | Approved references and end-to-end negative tests |
| `AIRPOL-OPEN-013` | Required checks | Branch protection/check significance |
| `AIRPOL-OPEN-014` | Production enforcement | Deployment/runtime evidence |
| `AIRPOL-OPEN-015` | Release and rollback | Slug-aware release map and completed drill |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Supports | Limit |
|---|---|---|
| Complete main tree | Exact tracked counts and path presence | Does not reveal deployed/off-repo consumers |
| Prior Air README blob | Compatibility history and rollback target | Documentation only |
| ADR-0029 + Directory Rules | Accepted placement/root authority | Does not select a domain slug or activate policy |
| CODEOWNERS | `/policy/` review route | Does not assign all functional roles |
| Atmosphere policy files | Exact default-only scaffold inventory | Filenames/defaults are not operative policy |
| Shared policy profiles/vocabularies | Candidate inputs, outcomes, reasons, obligations, roles | `PROPOSED_INACTIVE`; all authority flags false |
| AtmosphereAirDecisionEnvelope contract + schema | Semantic intent and current alignment gap | Both remain non-runtime; schema is minimal |
| Atmosphere tests | Seven substantive bounded profiles | Eight test modules remain placeholders; no native Rego tests |
| Atmosphere validators | Ten substantive bounded validators | Ten validator modules remain placeholders |
| Seven Atmosphere workflows | Deterministic fixture execution and explicit holds | No live-source, policy, proof, release, or publication authority |
| Policy runtime core | Implementation state | Comment-only placeholder |
| Policy bundles README/inventory | Intended bundle boundary | No accepted active payload verified |
| Air/Atmosphere contracts, schemas, specs, and pipelines | Namespace drift and mixed maturity | Presence does not settle authority |
| Atmosphere doctrine | Anti-collapse, rights, sensitivity, time, and official-authority intent | Runtime enforcement still needs proof |

### Reproducibility note

The evidence snapshot pins the repository commit, complete tree, target prior blob, and primary governing artifacts. Counts should be recomputed whenever main, either policy lane, shared policy contracts, Atmosphere tests/validators/workflows, runtime, bundles, or governance changes.

[Back to top](#top)

---

## Changelog

| Date | Version | Change | Status |
|---|---|---|---|
| 2026-06-15 | v0.1 | Expanded an empty placeholder into an Air/Atmosphere slug-conflict guardrail. | Documentation only |
| 2026-07-19 | v0.2 | Added pinned repository evidence, alias invariants, decision normalization, review, migration, rollback, and evidence sections. | Documentation + provenance receipt only |
| 2026-08-13 | v0.3 | Reconciled current main: exact two-blob Air lane; thirteen default-only Atmosphere Rego scaffolds; mixed tests/validators; seven bounded workflows; inactive shared policy vocabularies; decision-envelope alignment gap; accepted directory authority and verified review routing. Added stable conflict/open IDs, explicit normalization limits, public non-bypass rules, and an evidence-closed resolution sequence. | Documentation + provenance receipt only; no policy or public behavior changed |

---

KFM rule: `policy/domains/air/` is a compatibility boundary only. It must not become an active rule source, bundle selector, public alias, release shortcut, or parallel truth path.

<p align="right"><a href="#top">Back to top</a></p>
