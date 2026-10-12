<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy/thresholds-readme
title: policy/thresholds — Inactive Threshold Policy Candidate Boundary
type: readme
version: v0.2.0
status: draft; repository-grounded; PROPOSED_INACTIVE; unresolved-only; no-adopted-values; unbound; non-evaluator; non-release; non-publication
owners: NEEDS VERIFICATION — CODEOWNERS routes /policy/ to @bartytime4life; accepted policy and domain stewards were not established
created: 2026-08-10
updated: 2026-08-12
policy_label: public; policy; thresholds; inactive; review-required; no-live-values
owning_root: policy/
responsibility: Bound the inactive cross-domain threshold-policy candidate lane, document its deterministic unresolved-slot profile, and prevent value adoption, consumer binding, or authority overclaim.
related:
  - ../README.md
  - ../../contracts/policy/threshold_policy_registry.md
  - ../../schemas/contracts/v1/policy/threshold_policy_registry.schema.json
  - ./registry.v1.json
  - ../../fixtures/contracts/v1/policy/threshold_policy_registry/
  - ../../tools/validators/policy/validate_threshold_policy_registry.py
  - ../../tests/validators/test_validate_threshold_policy_registry.py
  - ../../.github/workflows/threshold-policy-registry.yml
truth_posture: CONFIRMED singular policy placement, six-slot inactive registry, closed unresolved-only schema, bounded validator, synthetic fixture polarity, and read-only workflow / PROPOSED threshold candidate lane and future adoption discipline / NEEDS VERIFICATION accepted stewards, values, evidence sufficiency, evaluator, consumers, review independence, and required-check enforcement / UNKNOWN production or external reliance
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy/thresholds/`

> **One-line purpose.** `policy/thresholds/` is the versioned policy-source
> boundary for naming cross-domain threshold questions that are not yet
> resolved. It preserves reviewable candidate identity without adopting a
> value, binding a consumer, evaluating policy, activating a source, approving
> release, or publishing.

> [!IMPORTANT]
> **Safe current conclusion:** at
> `main@4f78e13c1aa5192f27c464785befae01357a6df9`, this directory contains this
> README and one `PROPOSED_INACTIVE` registry. The registry names six slots
> across agriculture, atmosphere, hydrology, and soil. Every slot is
> `UNRESOLVED / UNBOUND / HOLD`; every operator, value, unit, effective date,
> and supersession reference is `null`; all seven authority flags are `false`.

> [!CAUTION]
> A registry entry, stable identifier, pressure reference, schema-valid file,
> validator `PASS`, workflow result, commit, or merge is **not** an accepted
> threshold or a `PolicyDecision`. Consumers must not interpret null as zero,
> `HOLD` as permission, or proposal lineage as scientific, operational, or
> release authority.

**Quick navigation:** [Purpose](#purpose) · [Authority](#inherited-authority-owner-and-scope) · [Status](#current-status) · [Child map](#current-direct-child-map) · [Registry](#current-candidate-inventory) · [Invariants](#v1-inactive-profile-invariants) · [Belongs](#what-belongs-here) · [Prohibited](#what-is-prohibited) · [Inputs and outputs](#inputs-and-outputs) · [Exposure](#exposure-mutation-and-retention) · [Trust boundary](#threshold-policy-trust-boundary) · [Adoption](#resolution-versioning-and-adoption-discipline) · [Validation](#validation-coverage-and-limits) · [Related evidence](#related-contracts-schemas-fixtures-tests-and-workflows) · [Correction](#correction-and-rollback) · [Review](#review-triggers-and-evidence-snapshot) · [Open verification](#open-verification-register)

## Purpose

This lane owns one narrow policy-source question:

> Which threshold-policy questions require governed resolution, and what is
> their current non-adopted review posture?

The v1 registry makes those questions stable and inspectable while refusing to
carry live values. It is a coordination surface for future review, not a
configuration file for watchers, detectors, maps, analytics, alerts, or public
decisions.

The lane does not define what a metric means, what JSON shape is valid, whether
source evidence is sufficient, how an evaluator executes, or whether a release
may proceed. Those responsibilities remain with their owning contracts,
schemas, evidence systems, runtime, review, and release surfaces.

[Back to top](#top)

## Inherited authority, owner, and scope

| Field | Current evidence |
|---|---|
| Parent | [`policy/`](../README.md), KFM's canonical source root for allow, deny, hold, restrict, and abstain rules. |
| README profile | `BOUNDARY_COMPACT`: this child lane changes cross-domain threshold-policy ownership and review posture while inheriting the parent root contract. |
| Placement | Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../docs/doctrine/directory-rules.md). Section 9.3 places policy source under singular `policy/`; section 16 defines the compact boundary contract and direct-child map law. |
| Machine projection | [`root_registry.yaml`](../../control_plane/root_registry.yaml) projects `policy/` as canonical, internal, versioned, durable policy-rule authority and prohibits data instances, release decisions, and schemas. The registry projects adopted rules; it does not create authority. |
| Candidate scope ID | `kfm://policy/thresholds/registry/v1`, fixed by the v1 schema. It identifies this candidate object; it does not authorize activation or consumer use. |
| Review route | [CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` to `@bartytime4life`. Routing does not prove review, accepted stewardship, independence, or approval. |
| Local owners | **NEEDS VERIFICATION.** The contract names policy, domain, validation, and release steward roles as candidates; accepted assignments were not established in the reviewed evidence. |
| Release authority | None. [`release/`](../../release/README.md) owns release, correction, withdrawal, rollback, promotion, and signature decisions. |
| Publication authority | None. A threshold slot or policy result cannot publish data, maps, alerts, claims, or notifications. |

[Back to top](#top)

## Current status

| Surface | Confirmed state at the evidence base | Safe interpretation |
|---|---|---|
| Prior README | v0.1.0 boundary document, blob `5339af282ee71e8b53c04be752e5d6a9b15385ef` | This v0.2 revision expands the same inactive boundary in place. |
| Direct-child inventory | `README.md` and `registry.v1.json` only | No local evaluator, bundle, fixture, test, receipt, release, or runtime store exists here. |
| Registry | [`registry.v1.json`](./registry.v1.json), blob `48069cb8d25659e81c386c947df8ac9c1b22beb1` | Six candidate slots; status `PROPOSED_INACTIVE`. |
| Registry identity | `RFC8785-JCS`; declared `spec_hash` `sha256:8b5442cbc3eabaee4ddf87ef06c3c080a4e5df7d3a6edc2d79d88b0e5060cfe1` | The validator recomputes identity over every registry field except `spec_hash`; identity is not policy adoption. |
| Semantic contract | [`ThresholdPolicyRegistry candidate`](../../contracts/policy/threshold_policy_registry.md) | Defines unresolved-slot meaning and non-effects; remains a draft, proposed contract. |
| Machine schema | [`threshold_policy_registry.schema.json`](../../schemas/contracts/v1/policy/threshold_policy_registry.schema.json) | Closed Draft 2020-12 profile; v1 structurally rejects values, active bindings, and authority grants. |
| Fixtures | [One valid and two invalid synthetic cases](../../fixtures/contracts/v1/policy/threshold_policy_registry/README.md) | Proves unresolved-slot acceptance plus numeric-value and active-binding rejection within the bounded profile. |
| Validator and tests | [Deterministic validator](../../tools/validators/policy/validate_threshold_policy_registry.py) and [eight focused test methods](../../tests/validators/test_validate_threshold_policy_registry.py) | Proves bounded shape, identity, ordering, local pressure-reference safety, parser behavior, and negative polarity only. |
| Workflow | [`threshold-policy-registry`](../../.github/workflows/threshold-policy-registry.yml) | Read-only changed-area orchestration; it cannot adopt, bind, activate, promote, release, notify, or publish. |
| Original generated receipt | [`genrec-threshold-policy-registry-20260810.json`](../../data/receipts/generated/genrec-threshold-policy-registry-20260810.json) | Historical provenance for the original candidate packet; it is not review approval or authority for later bytes. |
| Evaluator, bundle selector, consumer, decision receipt, production use | **UNKNOWN / NEEDS VERIFICATION** | No complete active threshold-policy path was established from the inspected evidence. |

All current-state claims above are pinned to
`main@4f78e13c1aa5192f27c464785befae01357a6df9`. Later repository changes require
a fresh inventory and evidence review.

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from the pinned tree, tracked bytes, executable validation, workflow definition, or accepted decision. |
| **PROPOSED** | Candidate design, value, role, behavior, or placement detail not accepted as current operation. |
| **NEEDS VERIFICATION** | A bounded check, assignment, or decision remains before the claim may be relied upon. |
| **UNKNOWN** | The inspected evidence cannot support a stronger statement. |

[Back to top](#top)

## Current direct-child map

This map was verified from the complete, non-truncated tracked tree at the
evidence base. It shows this directory and direct children only.

```text
policy/thresholds/
├── README.md
└── registry.v1.json  # PROPOSED_INACTIVE unresolved-slot policy candidate
```

Neither child is marked as generated, mirrored, localized, or converted in its
tracked bytes. The registry's content identity is deterministic, but that does
not make the file generated or independently authoritative.

[Back to top](#top)

## Current candidate inventory

| Threshold ID | Domain | Class | Question preserved |
|---|---|---|---|
| `kfm.threshold.agriculture.cdl-drift-materiality.v1` | agriculture | `MATERIALITY` | When CDL drift merits steward review without adopting a percentage or area value. |
| `kfm.threshold.atmosphere.aod-materiality.v1` | atmosphere | `SIGNAL_QUALITY` | Whether AOD may support review or tile-health signaling without becoming a scientific or emergency conclusion. |
| `kfm.threshold.atmosphere.frp-materiality.v1` | atmosphere | `SIGNAL_QUALITY` | Whether FRP may support review or tile-health signaling without converting detection into observed-fire truth. |
| `kfm.threshold.atmosphere.ozone-materiality.v1` | atmosphere | `MATERIALITY` | Whether an ozone review threshold is warranted without adopting a health, regulatory, or public-alert interpretation. |
| `kfm.threshold.hydrology.persistence-review.v1` | hydrology | `PERSISTENCE` | How long an anomaly must persist before review without adopting a duration or event classification. |
| `kfm.threshold.soil.moisture-materiality.v1` | soil | `MATERIALITY` | Whether soil-moisture change merits review without adopting an operational cutoff or changing promotion behavior. |

The inventory records questions, not answers. Domain and class labels organize
review; they do not define metric semantics, establish comparability across
domains, or authorize one threshold to govern another domain.

[Back to top](#top)

## v1 inactive-profile invariants

The closed schema and validator preserve the following current invariants:

| Invariant | Required v1 posture | Consequence |
|---|---|---|
| Registry status | `PROPOSED_INACTIVE` | No active registry claim is representable in this profile. |
| Value state | `UNRESOLVED` | Membership does not resolve a threshold. |
| Operator, value, and unit | `null` | Null must not be coerced to zero, false, default, or inherited configuration. |
| Binding state | `UNBOUND` | No watcher, detector, map, evaluator, or other consumer is connected. |
| Review state | `HOLD` | Review remains open; `HOLD` is not a permissive result. |
| Effective date and supersession | `null` | No threshold is in force and no prior policy is claimed to be superseded. |
| Reason codes | `NO_VALUE_ADOPTED`, `STEWARD_REVIEW_REQUIRED` | Each slot states why it cannot operate. |
| Governance flags | Seven exact `false` values | No numeric adoption, evaluation, watcher binding, source activation, promotion, release, or publication authority. |
| Ordering and identity | Unique lexical IDs and canonical arrays; RFC 8785 JCS plus SHA-256 | Reviewable deterministic bytes without implying factual correctness. |

Any edit that weakens one of these invariants is not routine registry
maintenance. It changes the profile's meaning and must be handled as a separate,
dependency-closed governance and compatibility review.

[Back to top](#top)

## What belongs here

Subject to the v1 contract, schema, and review boundary, this directory may
contain:

- the local boundary README;
- versioned, inactive threshold-policy candidate registries;
- stable candidate IDs, domains, metrics, classes, purpose statements, and
  explicit unresolved states;
- sorted steward-role candidates, proposal-lineage references, and repository
  pressure references;
- false-valued non-effect declarations;
- content identity and supersession metadata when an accepted profile defines
  them; and
- reviewed compatibility notes for a later registry version.

A record belongs here because its primary responsibility is **threshold-policy
admissibility and review posture**. A numeric limit used by a test, scientific
method, renderer, cache, performance budget, or local algorithm does not become
cross-domain policy merely because it is called a threshold.

[Back to top](#top)

## What is prohibited

| Prohibited material or claim | Owning surface or required action |
|---|---|
| Live, example, copied, or default values presented as adopted policy | Separate evidence-backed adoption proposal with domain and policy review; v1 cannot carry the value |
| Metric meaning, unit semantics, scientific interpretation, or comparability | [`contracts/`](../../contracts/policy/README.md) and the affected domain's accepted semantic authority |
| JSON Schema, DTO, generated type, or field-shape authority | [`schemas/contracts/v1/policy/`](../../schemas/contracts/v1/policy/README.md) |
| Watcher, detector, evaluator, API, UI, tile, alert, or renderer configuration | Its governed implementation or configuration root after an accepted binding |
| Reusable validator, fixture, or test implementation | [`tools/validators/`](../../tools/validators/policy/README.md), [`fixtures/`](../../fixtures/contracts/v1/policy/threshold_policy_registry/README.md), and [`tests/`](../../tests/validators/README.md) |
| EvidenceBundle, source payload, observation, scientific finding, or claim truth | Evidence, source, and governed lifecycle authorities; a registry consumes references only |
| `PolicyDecision`, review record, receipt, proof, promotion, correction, withdrawal, rollback, or release instance | The owning accountability, process, or [`release/`](../../release/README.md) family |
| Source admission, activation, polling, ingestion, or lifecycle state | Connectors, pipeline specifications, pipelines, policy gates, and lifecycle roots |
| Public alert, notification, map, claim, export, or publication state | Governed APIs and released public-safe artifacts after separate approval |
| Credentials, restricted payloads, exact sensitive locations, or production data | Do not commit; use the applicable secret, quarantine, restriction, redaction, or denial path |

Illustrative source values may be cited as proposal lineage when safe, but they
must not be copied into this v1 registry or fixtures in a way that looks adopted.

[Back to top](#top)

## Inputs and outputs

### Current inputs

Each candidate slot carries two reference families:

- `evidence_refs` preserve proposal lineage. The current validator checks only
  that these arrays are canonical strings; it does **not** retrieve, authenticate,
  or establish the sufficiency of the referenced evidence.
- `pressure_refs` point to tracked repository files where the unresolved
  threshold question is already visible. The validator permits bounded paths
  under `contracts/`, `docs/`, `policy/`, or `tools/`, rejects unsafe or
  symlinked paths, and requires the file to exist. Existence does not make the
  file a consumer or authority.

The registry accepts no runtime observation, source payload, model output,
secret, consumer configuration, review credential, or release state.

### Current outputs

The committed output is the inactive JSON registry itself. The validator emits
a deterministic report with `authority: "NONE"`, a bounded scope, findings, and
an outcome of `PASS`, `FAIL`, or `ERROR`. Neither output is a `PolicyDecision`,
approval, activation signal, receipt, proof, promotion, release, or publication.

### Future resolution inputs

Before even one slot may be proposed as resolved, a separate review unit must
identify at least:

- accepted metric meaning, operator, unit, value type, and temporal scope;
- domain evidence and uncertainty or sensitivity analysis;
- domain owner, policy owner, affected consumers, and independent review route;
- valid, invalid, boundary, missing-evidence, and error fixtures;
- compatibility, versioning, correction, supersession, and rollback behavior;
- rights, sensitivity, notification, and public-exposure consequences where
  material; and
- the exact evaluator, decision, consumer, and release boundaries involved.

These are graduation requirements, not claims that a resolved profile exists.

[Back to top](#top)

## Exposure, mutation, and retention

| Concern | Current boundary |
|---|---|
| Repository visibility | The tracked files are publicly visible. Do not place secrets, restricted source material, precise sensitive locations, or operational credentials here. |
| Operational exposure | The root registry classifies `policy/` as internal policy-rule authority. This lane exposes no accepted public API, client-loadable bundle, or runtime configuration. |
| Permitted mutation | Versioned review through Git. The root registry projects `@bartytime4life` as the current writer/reviewer route; effective controls and independent stewardship remain **NEEDS VERIFICATION**. |
| Runtime writes | None. Evaluations, alerts, decisions, logs, telemetry, receipts, proofs, and reviews must not be written into this source lane. |
| Retention | Durable version history under the parent policy root. Decision and release retention belong to their own object families. |
| Generation | No generator or writable-source relationship is established for the two direct children. Deterministic identity is not generation authority. |
| Sensitive inputs | Not retained. Use safe references and governed classifications rather than copied payloads or harmful precision. |

[Back to top](#top)

## Threshold-policy trust boundary

Threshold policy may decide whether a governed operation is admissible under an
accepted value. It must not manufacture the scientific, evidentiary, review, or
release facts needed to make that decision.

| Concern | Permitted future policy role | Authority it must not assume |
|---|---|---|
| Metric semantics | Consume an accepted metric definition and unit | Define or silently reinterpret the metric |
| Evidence | Require an admissible evidence posture and uncertainty handling | Create an observation, resolve support by assertion, or treat a citation as proof |
| Threshold value | Apply a separately adopted, versioned value to a named operation | Infer a universal value from fixtures, examples, source notes, or current practice |
| Domain boundaries | Use an accepted domain-specific profile | Generalize one domain's threshold to another domain without review |
| Watchers and detectors | Return a bounded result to a governed consumer | Become polling configuration, source activation, or event truth |
| Rights and sensitivity | Apply accepted restrictions and obligations | Clear rights, downgrade sensitivity, or expose protected details in reasons |
| Review | Require authenticated review posture | Assign a steward, approve its own source, or treat CODEOWNERS as completed review |
| Release and publication | Supply one admissibility input to a separate decision | Promote, release, publish, notify, or create public truth |
| Correction | Apply a current version or supersession posture | Create correction, withdrawal, rollback, or lineage facts |

### Fail-closed interpretation

Until a slot is separately accepted and bound, downstream systems must treat it
as unavailable for operational evaluation. Missing or null values, unresolved
evidence, unknown ownership, unbound consumers, held review, evaluator errors,
and absent release state must remain distinguishable and non-permissive. No
caller may substitute a local default or illustrative value to avoid the hold.

[Back to top](#top)

## Resolution, versioning, and adoption discipline

Version 1 is intentionally unable to represent an adopted threshold. Its
schema fixes the inactive states, null fields, and false authority flags. A
resolved value therefore requires a separately reviewed schema/profile change
or successor surface; editing `registry.v1.json` alone cannot legitimately
activate it.

A dependency-closed resolution packet should establish, at minimum:

1. a bounded decision question and affected operation;
2. accepted semantic meaning and machine shape;
3. evidence sufficiency, uncertainty, sensitivity, and domain review;
4. value, operator, unit, effective window, version, and supersession rules;
5. positive, boundary, negative, malformed, missing-context, stale, and error
   fixtures as applicable;
6. deterministic policy rules, native tests, and a versioned bundle;
7. an accepted evaluator and finite outcome, reason, and obligation mapping;
8. authenticated decision, receipt, replay, expiry, correction, and rollback
   handling;
9. governed consumer integration with bypass and default-value resistance; and
10. separate review, promotion, release, notification, and publication gates.

Threshold resolution should be one slot—or one tightly coupled compatible
family—per review unit. Broad cross-domain activation without explicit coupling
evidence is prohibited.

[Back to top](#top)

## Validation coverage and limits

### Current executable coverage

| Check | Confirmed coverage | What it does not prove |
|---|---|---|
| Closed JSON Schema | Required fields, enums, null-only inactive fields, and false governance flags | Correct science, evidence, value, owner, or consumer |
| Canonical identity | RFC 8785 JCS plus SHA-256 over every field except `spec_hash` | Approval, authenticity, signature, or immutability |
| Semantic validator | Sorted unique IDs and arrays, exact unresolved reasons, domain/metric uniqueness, safe existing pressure paths, and all-false governance | Evidence-reference resolution, policy evaluation, or production fitness |
| Parser boundaries | Duplicate keys, non-finite numbers, symlinked inputs, unreadable/oversized inputs, and bounded schema findings fail closed | Repository-wide parser or supply-chain safety |
| Fixture polarity | One valid unresolved slot passes; numeric-value and active-binding cases fail | Adopted values, boundary semantics, or live consumers |
| Focused tests | Eight test methods cover registry replay, schema posture, negative semantics, fixture polarity, parser boundaries, and deterministic no-network behavior | An accepted evaluator, bundle, decision, or release path |
| Hosted workflow | Pull-request and `main` changes under the threshold packet run focused tests, registry validation, fixture replay, and shared schema polarity | Required-check settings, independent approval, policy adoption, release, or publication |

The workflow has `contents: read`, persists no checkout credentials, and records
explicit non-effects. Its dependency installation may use the runner's network;
the repository validator itself resolves only local files and the focused test
denies network use around deterministic serialization.

### Repository-native checks

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_threshold_policy_registry.py' \
  --verbose

python tools/validators/policy/validate_threshold_policy_registry.py \
  --registry

python tools/validators/policy/validate_threshold_policy_registry.py \
  --fixtures

python -m pytest tests/schemas/test_common_contracts.py \
  -q -k threshold_policy_registry
```

### Documentation validation for this README

This documentation revision should preserve:

- one H1, logical heading order, balanced language-tagged fences, and a final
  newline;
- metadata block identity, responsibility, version, dates, and related paths;
- exact direct-child parity with the pinned tree;
- valid repository-relative links and local fragments;
- exact registry counts, IDs, states, null fields, authority flags, blobs, and
  validation claims;
- no runtime, rule, schema, fixture, workflow, release, or publication change;
  and
- remote base/head, changed-path, draft state, and exact-head check read-back.

Passing these checks proves documentation quality and evidence alignment only.
It does not resolve or activate a threshold.

[Back to top](#top)

## Related contracts, schemas, fixtures, tests, and workflows

| Surface | Confirmed role | Authority limit |
|---|---|---|
| [`policy/README.md`](../README.md) | Parent policy-root authority and mixed-maturity inventory | The parent does not activate this registry or supply an accepted value. |
| [`threshold_policy_registry.md`](../../contracts/policy/threshold_policy_registry.md) | Candidate semantics, responsibility split, deterministic rules, adoption burden, and non-effects | Draft semantics are not accepted policy or evidence. |
| [`threshold_policy_registry.schema.json`](../../schemas/contracts/v1/policy/threshold_policy_registry.schema.json) | Closed v1 machine shape that forbids values and authority grants | Schema conformance is not adoption or evaluation. |
| [`registry.v1.json`](./registry.v1.json) | Six stable unresolved candidate slots | Registry membership is not a value, binding, decision, or scientific conclusion. |
| [Synthetic fixture family](../../fixtures/contracts/v1/policy/threshold_policy_registry/README.md) | One valid unresolved case and negative value/binding cases | Synthetic values and failures cannot establish live thresholds. |
| [Validator](../../tools/validators/policy/validate_threshold_policy_registry.py) and [tests](../../tests/validators/test_validate_threshold_policy_registry.py) | Deterministic shape, identity, ordering, path, parser, and polarity checks | Reports carry `authority: "NONE"` and do not execute policy. |
| [`threshold-policy-registry.yml`](../../.github/workflows/threshold-policy-registry.yml) | Read-only changed-area orchestration | Workflow success is QA, not review, adoption, release, or publication. |
| [Source map](../../docs/intake/exploratory/threshold-policy-registry-source-map.md) | Preserves Pass 20 proposal lineage and path-decision reasoning | Exploratory material cannot adopt values or override current repository evidence. |
| [Original generated receipt](../../data/receipts/generated/genrec-threshold-policy-registry-20260810.json) | Provenance for the original candidate packet | A receipt is process memory, not proof, approval, or authority for later bytes. |
| [AI build operating contract](../../docs/doctrine/ai-build-operating-contract.md) and [generated-receipt lane](../../data/receipts/generated/README.md) | Current repository discipline for AI-authored changes | Receipt validity and human review remain separate from merge, release, and publication. |
| [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) | Parent evidence identifies a placeholder general runtime package | It does not establish a threshold evaluator or consumer. |
| [`release/`](../../release/README.md) | Owns release, correction, withdrawal, rollback, promotion, and signatures | Policy source supplies inputs only; it cannot approve or publish. |

These surfaces form a review packet, not an accepted operational chain. Their
vocabularies and authority must remain separate until an accepted binding says
otherwise.

[Back to top](#top)

## Correction and rollback

This README revision changes documentation and its provenance only. It does not
alter the registry, contract, schema, fixtures, validator, tests, workflow,
consumer, runtime, source state, policy result, release, or public artifact.

- **Before merge:** close or abandon the draft pull request. The target on the
  pinned base remains blob `5339af282ee71e8b53c04be752e5d6a9b15385ef`.
- **After an authorized merge:** revert the documentation/provenance commit or
  apply a transparent forward-fix that preserves corrected evidence and
  history.
- **Registry correction:** correct or supersede the registry through its
  versioned contract, schema, identity, fixtures, tests, and review unit; do not
  rewrite this README to conceal a registry defect.
- **Operational reliance discovered:** stop the consumer, preserve evidence,
  and use the owning policy, correction, release, notification, and rollback
  processes. A Git revert alone may not repair an external decision or alert.

[Back to top](#top)

## Review triggers and evidence snapshot

### Evidence snapshot

| Evidence | Reviewed identity |
|---|---|
| Repository base | `main@4f78e13c1aa5192f27c464785befae01357a6df9` |
| Prior target blob | `5339af282ee71e8b53c04be752e5d6a9b15385ef` |
| Registry blob | `48069cb8d25659e81c386c947df8ac9c1b22beb1` |
| Parent policy README blob | `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35` |
| Semantic contract blob | `b1716848cb8887c69cde2e6cfa6ac9d29ad6bdd3` |
| Machine schema blob | `6071b03a44fa4c1d71feb0137c41d63ad4cbd1c1` |
| Validator / tests blobs | `24c9bdd5d7023d2cad4c98149363d9b456a623e4` / `f7f42a132b14dab90b18c431db724e1d1644aa8c` |
| Workflow blob | `659fc5b17b667fba8948179ae42e88a14b8efd1b` |
| Directory Rules / ADR-0029 blobs | `fd49a0b83e55cef52c1124281f093e263526898d` / `b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62` |
| Root registry / CODEOWNERS blobs | `024f668b5f0a9239bafa4f8b09e2afd86300ff8c` / `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` |
| Open-PR overlap | No open pull request changed or named this lane immediately before authoring |
| Review date | 2026-08-12 |

Re-review this boundary when any of the following changes:

- a direct child, registry ID, slot, domain, class, state, reference, identity,
  or generation relationship;
- the contract, schema, fixture polarity, validator, test, workflow, or original
  receipt relationship;
- a value, operator, unit, effective date, supersession, reason, steward, or
  governance flag;
- evidence sufficiency, metric semantics, sensitivity, rights, domain scope, or
  scientific interpretation;
- a watcher, detector, evaluator, bundle, consumer, API, alert, notification,
  promotion, release, or public exposure;
- CODEOWNERS, stewardship, required checks, review independence, or repository
  controls;
- an accepted ADR, migration, correction, withdrawal, rollback, or security
  finding affecting this lane; or
- drift between this README, the tracked tree, and executable validation.

[Back to top](#top)

## Open verification register

| ID | Open item | State | Evidence needed to close |
|---|---|---|---|
| `THRESH-POL-001` | Accepted policy, domain, validation, and release stewards | **NEEDS VERIFICATION** | Approved responsibility assignments and independent review route |
| `THRESH-POL-002` | Evidence-reference resolution and sufficiency for each slot | **UNKNOWN** | Governed resolver results and domain evidence review; string presence is insufficient |
| `THRESH-POL-003` | Accepted metric meaning, operator, unit, value, and temporal scope | **CONFIRMED unresolved at the evidence base** | Separate semantic and policy adoption record with uncertainty analysis |
| `THRESH-POL-004` | Cross-domain compatibility and whether each value belongs here or in a domain profile | **NEEDS VERIFICATION** | Explicit placement and compatibility decision per resolved slot |
| `THRESH-POL-005` | Versioned bundle, selector, evaluator, and native policy outcomes | **UNKNOWN** | Accepted bundle/evaluator contract plus positive, negative, malformed, and error tests |
| `THRESH-POL-006` | Watcher, detector, map, analysis, alert, or other consumer binding | **CONFIRMED unbound in v1; external reliance UNKNOWN** | Accepted consumer contract, binding identity, bypass tests, and external-use review |
| `THRESH-POL-007` | Authenticated `PolicyDecision`, receipt, replay, expiry, and correction path | **UNKNOWN** | Bound decision and accountability artifacts with deterministic replay |
| `THRESH-POL-008` | Promotion, release, notification, and publication integration | **CONFIRMED unauthorized by v1** | Separate governed gates and release evidence; registry membership remains insufficient |
| `THRESH-POL-009` | Effective required-check, code-owner, and separation-of-duties enforcement | **NEEDS VERIFICATION** | Current platform settings and exact-head hosted-check evidence |
| `THRESH-POL-010` | Production or external consumer inventory | **UNKNOWN** | Repository and external dependency inventory with owner confirmation |

Until these items are closed through their owning authorities, this lane remains
inactive, unresolved, unbound, and held.

[Back to top](#top)
