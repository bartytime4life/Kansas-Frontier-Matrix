<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-mock-readme
title: runtime/mock/ — Deterministic Mock Runtime and Proof Boundary
type: readme; directory-readme; canonical-runtime-sublane; deterministic-mock-boundary; test-support-index
version: v1.1
status: draft; repository-grounded; canonical-lane-confirmed; README-only; implementation-unconfirmed; mock-first; no-network-default; ci-unproved; non-authoritative
owners: OWNER_TBD — Runtime steward · Governed-AI steward · Test steward · Fixture steward · Contract steward · Schema steward · Policy steward · Evidence steward · Receipt steward · Security steward · Migration steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub replaced by v1 on 2026-07-03
updated: 2026-07-15
supersedes: v1 mock runtime lane guide
policy_label: "public-doctrine; runtime; mock; deterministic-tests; mock-first; no-network; finite-outcomes; evidence-subordinate; policy-subordinate; release-subordinate; no-public-runtime; no-lifecycle-authority; no-truth-authority; rollback-aware"
current_path: runtime/mock/README.md
truth_posture: >
  CONFIRMED target v1 README, Directory Rules canonical runtime/mock sublane, latest runtime root,
  tracked root environment example selecting mock runtime and loopback governed API, provider-neutral
  model-adapter lane, mock-adapter child README, schema-paired draft/PROPOSED runtime envelopes,
  focus-mock-test TODO-only workflow, and bounded absence of selected runtime/mock implementation
  and dedicated test paths / PROPOSED deterministic mock profile, fixture manifest, replay identity,
  finite outcomes, failure injection, resource bounds, receipt-ready facts, validation matrix,
  migration, correction, and rollback / CONFLICTED broad runtime/mock responsibility versus
  runtime/model_adapters/mock child-lane responsibility and prior note-oriented status vocabulary
  versus schema-paired runtime outcomes / UNKNOWN executable mock adapter, public API consumer,
  accepted mock request profile, fixture family, test collection, policy execution, EvidenceRef
  resolution, citation validation, receipt persistence, deployment, and operational health /
  NEEDS VERIFICATION owners, CODEOWNERS, lane split, contract/schema acceptance, fixture registry,
  substantive CI, first governed consumer, migration policy, correction propagation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  prior_blob: b48aa917319fd4b3fc458c7b5575eaaafcdc800d
  runtime_root_blob: 894d15bb2e2d0185f433e35c690e0a6b42327fb9
  model_adapters_mock_blob: 18fdd7034f1e8768f813acc38209eef8688b78d3
  env_example_blob: 50e972a4c5c009ed89097753932fc328039c1aec
  focus_mock_workflow_blob: 9dcd509f87df4ab213bbac7f5ff6cebb02937a78
  bounded_path_checks:
    - runtime/mock/README.md exists
    - runtime/mock/__init__.py was not found
    - runtime/mock/adapter.py was not found
    - runtime/mock/runtime.py was not found
    - tests/runtime/mock/README.md was not found
    - bounded search surfaced runtime/mock documentation but no executable mock adapter
    - .env.example selects KFM_MODEL_RUNTIME=mock and loopback API/runtime examples
    - focus-mock-test workflow runs TODO echo commands only
related:
  - ../README.md
  - ../model_adapters/README.md
  - ../model_adapters/mock/README.md
  - ../envelopes/README.md
  - ../service_configs/README.md
  - ../local/README.md
  - ../ollama/README.md
  - ../../apps/governed-api/README.md
  - ../../contracts/runtime/decision_envelope.md
  - ../../contracts/runtime/runtime_response_envelope.md
  - ../../contracts/runtime/ai_receipt.md
  - ../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../fixtures/contracts/v1/runtime/README.md
  - ../../tests/schemas/test_common_contracts.py
  - ../../policy/runtime/README.md
  - ../../data/receipts/README.md
  - ../../release/README.md
  - ../../.env.example
  - ../../.github/workflows/focus-mock-test.yml
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, runtime, mock, deterministic, no-network, fixtures, replay, finite-outcomes, governed-ai, envelopes, receipts, failure-injection, migration, rollback]
notes:
  - "This revision changes only runtime/mock/README.md."
  - "The lane remains documentation-only at the checked implementation paths."
  - "Selecting mock in .env.example is a safe default, not proof that an executable mock runtime exists."
  - "This README creates no adapter, fixture, test, validator, policy, receipt, workflow, deployment, release, or public route."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `runtime/mock/` — Deterministic Mock Runtime and Proof Boundary

> **One-line purpose.** Define the canonical runtime lane for deterministic, no-network, fixture-backed mock behavior that exercises governed runtime contracts before live providers are admitted, while remaining subordinate to evidence, policy, validation, receipts, release, correction, rollback, and the governed public trust membrane.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lane: canonical mock" src="https://img.shields.io/badge/lane-canonical__mock-success">
  <img alt="Maturity: README only" src="https://img.shields.io/badge/maturity-README__only-lightgrey">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-blueviolet">
  <img alt="Public runtime: denied" src="https://img.shields.io/badge/public__runtime-denied-red">
</p>

> [!IMPORTANT]
> `runtime/mock/` is a canonical runtime sublane, but canonical placement is not implementation proof. Current evidence establishes this README, a mock-first environment example, and surrounding contracts and documentation—not an executable mock adapter, fixture registry, dedicated test suite, substantive CI gate, governed API integration, emitted receipt stream, or deployment.

> [!CAUTION]
> A mock result is synthetic test material. It cannot establish evidence, settle policy, satisfy release, promote lifecycle state, authorize publication, or become public truth.

> [!WARNING]
> Mock infrastructure must not silently reach live networks, real providers, canonical stores, secret systems, private files, restricted EvidenceBundles, or sensitive location material. Any such access is a test failure unless a separately governed integration profile explicitly permits it.

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-bounded-scope) · [Placement](#repository-fit-and-placement) · [Split](#runtime-mock-versus-mock-adapter-child-lane) · [Authority](#authority-and-anti-collapse-rules) · [Model](#proposed-mock-runtime-model) · [Determinism](#determinism-replay-and-identity) · [Inputs](#inputs-and-context-minimization) · [Outcomes](#finite-outcomes-and-failure-injection) · [Fixtures](#fixtures-golden-cases-and-synthetic-data) · [Receipts](#envelopes-receipts-and-observability) · [Security](#security-network-and-resource-controls) · [Testing](#testing-validation-and-current-proof-boundary) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Maintenance](#maintenance-correction-migration-and-rollback)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

| Surface | Status | Safe conclusion |
|---|---|---|
| `runtime/mock/README.md` | **CONFIRMED** | Canonical lane documentation exists. |
| Directory Rules | **CONFIRMED** | Assign deterministic mock runtime support under `runtime/mock/`. |
| Latest runtime root | **CONFIRMED** | Treats mock-first execution as subordinate to governed evidence, policy, envelopes, and release. |
| Root `.env.example` | **CONFIRMED** | Selects `KFM_MODEL_RUNTIME=mock` and loopback bindings; this is a safe example, not activation proof. |
| `runtime/model_adapters/mock/README.md` | **CONFIRMED documentation** | A mock-adapter child lane exists, creating an unresolved responsibility split with this lane. |
| Runtime contracts and schemas | **CONFIRMED draft/PROPOSED families** | Finite envelope shapes exist; runtime emission and adoption remain unproved. |
| Selected `runtime/mock` implementation files | **Not found at checked paths** | No executable adapter or runtime module is established by current checks. |
| Dedicated mock test README | **Not found at checked path** | No dedicated test-root contract was established there. |
| `focus-mock-test` workflow | **CONFIRMED TODO-only** | Green status cannot prove deterministic flow, envelope shape, or no-network behavior. |
| Executable consumer, fixtures, policy integration, receipts, deployment, health | **UNKNOWN** | Documentation and examples are not operational proof. |

**Authority:** this README governs placement, boundaries, and implementation admission for this lane. Canonical contracts, schemas, executable policy, fixtures, tests, validator output, EvidenceBundles, receipts, release records, correction records, and steward decisions outrank it.

[Back to top](#top)

---

<a id="purpose-and-bounded-scope"></a>

## Purpose and bounded scope

This lane exists to support safe runtime development before live providers are admitted. It should make these properties inspectable:

1. fixed inputs and expected outputs;
2. deterministic finite outcomes;
3. no-network execution;
4. bounded context and resource use;
5. explicit contract and schema profile;
6. fixture and test identity;
7. policy, evidence, citation, freshness, and correction simulations;
8. receipt-ready runtime facts;
9. failure injection and negative-path coverage;
10. migration and rollback when a live adapter replaces a mock.

This lane does **not** define provider-neutral adapter APIs, semantic contracts, JSON Schemas, policy rules, evidence truth, source authority, fixture payload authority, lifecycle storage, receipt persistence, release state, public API routes, UI behavior, or deployment topology.

[Back to top](#top)

---

<a id="repository-fit-and-placement"></a>

## Repository fit and placement

```text
runtime/
├── mock/                         # broad deterministic mock runtime behavior; this lane
├── model_adapters/
│   └── mock/                     # adapter-specific mock compatibility/index lane
├── envelopes/                    # runtime envelope wiring and handoff
├── service_configs/              # runtime service binding guidance
├── local/                        # local runtime wiring
└── ollama/                       # provider-specific local runtime

contracts/runtime/                # semantic meaning
schemas/contracts/v1/runtime/     # machine-checkable shape
fixtures/                         # deterministic examples
tests/                            # executable proof
tools/validators/                 # validators
policy/runtime/                   # admissibility and obligations
data/receipts/                    # persisted process memory
release/                          # release, correction, rollback authority
apps/governed-api/                # accepted public trust membrane
```

The path is valid under the runtime responsibility root. No new root or domain-specific authority is introduced by this README.

[Back to top](#top)

---

<a id="runtime-mock-versus-mock-adapter-child-lane"></a>

## `runtime/mock/` versus mock-adapter child lane

The repository currently documents both:

- `runtime/mock/` for broad deterministic runtime behavior; and
- `runtime/model_adapters/mock/` for adapter-specific mock notes.

Until maintainers accept a sharper split:

| Concern | Default home |
|---|---|
| End-to-end deterministic runtime scenarios | `runtime/mock/` |
| Mock mode, replay identity, failure injection, no-network rules | `runtime/mock/` |
| Provider-neutral mock adapter card or adapter compatibility note | `runtime/model_adapters/mock/` |
| Reusable adapter implementation | accepted package/runtime implementation lane |
| Fixture payload | `fixtures/` |
| Executable test | `tests/` |
| Contract or schema | `contracts/`, `schemas/` |
| Runtime envelope wiring | `runtime/envelopes/` |
| Persisted receipt | `data/receipts/` |

Do not implement the same mock client, fixture resolver, outcome mapper, or receipt builder independently in both lanes. If consolidation is chosen, preserve inbound links and add a migration note.

[Back to top](#top)

---

<a id="authority-and-anti-collapse-rules"></a>

## Authority and anti-collapse rules

Disallowed collapses:

```text
mock output != evidence
mock fixture != source record
mock ANSWER != supported public claim
mock DENY != policy authority
schema-valid mock != implemented runtime
green TODO workflow != behavioral proof
selected mock default != active service
deterministic text != botanical, historical, legal, or spatial truth
receipt-shaped fixture != emitted receipt
successful mock run != release approval
```

Required separations:

- `EvidenceBundle` outranks mock language;
- executable policy owns allow, deny, restrict, and obligations;
- runtime envelopes carry finite results but do not create evidence;
- fixtures remain synthetic or explicitly sanitized;
- tests prove behavior, not real-world truth;
- persisted receipts remain outside this lane;
- release and publication remain governed state transitions;
- public clients use the governed API and never call mock internals directly.

[Back to top](#top)

---

<a id="proposed-mock-runtime-model"></a>

## Proposed mock runtime model

No accepted mock profile contract or schema was verified. A future profile should identify:

- stable mock profile ID and version;
- status and owner;
- adapter profile and envelope profile;
- fixture-set ID and immutable digest;
- deterministic seed and clock profile;
- request profile and context limits;
- expected outcome and reason code;
- simulated evidence, policy, citation, freshness, correction, and release posture;
- failure-injection mode;
- latency and resource profile;
- receipt-fixture profile;
- supersession and rollback references.

A minimal conceptual flow is:

```text
governed caller
  -> bounded mock request
  -> explicit fixture + seed + clock
  -> deterministic outcome selection
  -> contract/schema validation
  -> policy/evidence/citation simulation as configured
  -> RuntimeResponseEnvelope / DecisionEnvelope candidate
  -> receipt-ready facts
  -> caller renders ANSWER, ABSTAIN, DENY, or ERROR
```

Every arrow remains **PROPOSED** until implementation and tests prove it.

[Back to top](#top)

---

<a id="determinism-replay-and-identity"></a>

## Determinism, replay, and identity

A deterministic mock must pin all material inputs:

- profile version;
- fixture digest;
- request canonicalization;
- seed;
- clock;
- locale and timezone;
- ordering rules;
- retry count;
- latency simulation;
- outcome mapping;
- reason-code mapping;
- envelope profile;
- policy/evidence simulation state;
- software revision when implementation exists.

The same canonical inputs should produce byte-stable or semantically stable outputs according to an accepted comparison profile.

Replay identity must remain distinct:

```text
mock_profile_id
fixture_set_id
request_id
run_id
response_id
envelope_id
receipt_id
```

Do not reuse IDs across fixture, run, response, envelope, and receipt families.

[Back to top](#top)

---

<a id="inputs-and-context-minimization"></a>

## Inputs and context minimization

Allowed inputs should be explicit, bounded, and synthetic or public-safe:

- deterministic request fixtures;
- contract-valid envelope fixtures;
- synthetic EvidenceRef and policy-result fixtures;
- public-safe citation fixtures;
- fixed clock and seed settings;
- bounded simulated provider metadata;
- expected-output and expected-failure manifests.

Denied by default:

- live network access;
- real provider calls;
- raw or restricted lifecycle stores;
- secret systems;
- private filesystem traversal;
- exact sensitive locations;
- unrestricted prompts or tool calls;
- production credentials or private endpoints;
- unreviewed real source payloads.

A mock should receive the minimum context needed to exercise the target behavior. Tests for sensitive workflows should use synthetic coordinates and synthetic identities.

[Back to top](#top)

---

<a id="finite-outcomes-and-failure-injection"></a>

## Finite outcomes and failure injection

Schema-paired runtime outcomes are:

| Outcome | Mock meaning |
|---|---|
| `ANSWER` | Produce a deterministic contract-shaped candidate supported by the configured synthetic context. |
| `ABSTAIN` | Simulate insufficient evidence, citation, freshness, correction, or scope support. |
| `DENY` | Simulate a policy or access decision that forbids disclosure or execution. |
| `ERROR` | Simulate validation, configuration, adapter, resource, timeout, or internal failure. |

Caller-owned workflow states such as `HOLD`, `NEEDS_REVIEW`, `QUARANTINE`, `SUPERSEDED`, or `RETIRED` must not be silently encoded as additional envelope outcomes.

Failure injection should cover:

- missing fixture;
- malformed request;
- unknown profile;
- schema mismatch;
- denied policy;
- unresolved EvidenceRef;
- stale or corrected support;
- invalid citation;
- timeout and cancellation;
- retry exhaustion;
- resource overflow;
- corrupted digest;
- non-deterministic output;
- attempted network access;
- attempted secret or filesystem access;
- receipt persistence failure;
- unsupported envelope version.

No failure may silently downgrade to `ANSWER`.

[Back to top](#top)

---

<a id="fixtures-golden-cases-and-synthetic-data"></a>

## Fixtures, golden cases, and synthetic data

Fixture payloads belong under the accepted fixture root, not in this runtime documentation lane.

A governed fixture set should include:

- manifest with stable ID and version;
- content digests;
- source and generation provenance;
- synthetic/public-safe classification;
- sensitivity review;
- valid and invalid cases;
- expected outcome and reason;
- expected envelope or receipt shape;
- fixed seed and clock;
- correction and supersession lineage.

Golden cases should be small, inspectable, immutable within a version, and no-network. Invalid fixtures should fail for one primary reason where practical.

Never include real credentials, private prompts, unpublished steward notes, restricted EvidenceBundle content, or exact rare-species, archaeological, infrastructure, or living-person locations.

[Back to top](#top)

---

<a id="envelopes-receipts-and-observability"></a>

## Envelopes, receipts, and observability

Mock behavior may create contract-shaped candidates for validation, but:

- an envelope fixture is not an emitted production envelope;
- a receipt fixture is not persisted process memory;
- a mock policy result is not an executable policy decision;
- a synthetic EvidenceRef is not evidence closure.

Receipt-ready facts may include:

- run and profile identity;
- fixture digest;
- request and response identity;
- selected outcome and reason;
- contract/schema versions;
- seed and clock profile;
- validation results;
- policy/evidence/citation simulation state;
- timing and bounded resource metrics;
- correction and supersession references.

Logs and metrics must avoid prompts, protected context, fixture payload dumps, private reasoning, secrets, and sensitive coordinates.

[Back to top](#top)

---

<a id="security-network-and-resource-controls"></a>

## Security, network, and resource controls

Default controls:

| Concern | Default |
|---|---|
| Network | denied |
| Provider call | denied |
| Public endpoint | denied |
| Filesystem | temporary sandbox or explicit read-only fixture roots |
| Secrets | absent |
| Tool execution | denied unless explicitly simulated |
| Clock | fixed |
| Randomness | seeded |
| Retries | bounded |
| Concurrency | bounded |
| Context/output size | bounded |
| Temporary files | isolated and deleted |
| Logs | minimized and redacted |

A mock test should fail when code attempts unexpected network, DNS, subprocess, secret, home-directory, canonical-store, or unrestricted filesystem access.

Resource exhaustion and retry storms must be tested as finite failures, not allowed to hang CI.

[Back to top](#top)

---

<a id="testing-validation-and-current-proof-boundary"></a>

## Testing, validation, and current proof boundary

Current proof is insufficient:

- no selected executable file was found under `runtime/mock/`;
- no selected dedicated mock test README was found;
- the dedicated workflow runs only TODO echo commands;
- no fixture registry, deterministic replay report, or emitted receipt was verified.

A substantive test matrix should cover:

| Area | Minimum proof |
|---|---|
| Import/initialization | no network, file, secret, or provider side effects |
| Determinism | repeated identical requests match accepted comparison rules |
| Finite outcomes | all four outcomes and stable reason mappings |
| Negative paths | no fluent fallback from missing evidence or denied policy |
| Envelopes | paired schema-valid and invalid cases |
| Receipts | receipt-ready facts and no private reasoning |
| Network | unexpected socket/DNS/provider access fails |
| Filesystem | only approved temporary/fixture roots |
| Time/randomness | fixed clock and seed are honored |
| Resources | limits, timeout, cancellation, retries, concurrency |
| Security | injection-like fixture text remains data, not instruction |
| Sensitivity | synthetic protected-location cases fail closed |
| Migration | mock/live adapter parity at the provider-neutral boundary |
| Rollback | defective mock profile can be superseded or reverted |

A substantive CI sequence is **PROPOSED**:

```text
inventory -> install/build -> collect tests -> no-network guard
          -> fixture integrity -> deterministic replay -> finite outcomes
          -> schema/contract validation -> policy/evidence negative paths
          -> resource/security tests -> receipt checks -> rollback drill
```

The current `focus-mock-test` workflow does not execute this sequence.

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What belongs here

- this README;
- broad mock runtime profile and behavior documentation;
- deterministic replay and failure-injection guidance;
- indexes pointing to accepted fixtures, tests, adapters, envelopes, and receipts;
- migration notes from mock to live runtime;
- deprecation, correction, and rollback notes;
- documentation that explains mock-first governance without storing authority objects.

[Back to top](#top)

---

<a id="what-does-not-belong-here"></a>

## What does not belong here

| Material | Correct home |
|---|---|
| Provider-neutral adapter implementation | accepted adapter/package lane |
| Adapter-specific mock card | `runtime/model_adapters/mock/` until the split is resolved |
| Live provider implementation | accepted provider-specific lane |
| Contracts and schemas | `contracts/`, `schemas/` |
| Policy | `policy/` |
| Fixture payloads and golden outputs | `fixtures/` |
| Executable tests | `tests/` |
| Validators | `tools/validators/` |
| Lifecycle data | `data/<phase>/` |
| EvidenceBundles and proofs | governed proof roots |
| Persisted receipts | `data/receipts/` |
| Release/correction/rollback decisions | `release/` |
| Public routes and serializers | governed application roots |
| Credentials, private endpoints, protected context | never committed here |

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

1. Confirm ownership and the split with `runtime/model_adapters/mock/`.
2. Select one narrow governed caller and request profile.
3. Accept or pin the relevant runtime contract/schema profiles.
4. Define a closed mock-profile contract and schema in authority roots.
5. Create synthetic valid/invalid fixtures with manifests and digests.
6. Implement a side-effect-free deterministic mock behind the provider-neutral adapter boundary.
7. Add fixed clock, seed, latency, failure injection, cancellation, and resource bounds.
8. Add no-network, no-secret, filesystem, and injection tests.
9. Validate finite envelopes and receipt-ready facts.
10. Make CI collect and fail nonzero on the dedicated tests.
11. Document activation, supersession, correction, and rollback.
12. Keep the mock default until a live runtime closes an equal or stronger gate set.

Each step should be separately reviewable and reversible.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This lane becomes implementation-backed only when:

- an accepted owner and CODEOWNERS rule exist;
- the mock/adaptor-lane split is resolved;
- an executable mock implementation exists at an accepted path;
- package/import/build behavior is reproducible;
- closed mock profile and runtime envelope contracts/schemas are accepted;
- fixture manifests and immutable digests exist;
- tests collect nonzero cases;
- no-network and no-secret guards are enforced;
- all finite outcomes and negative paths are covered;
- deterministic replay is demonstrated;
- resource, cancellation, and failure-injection tests pass;
- receipt-ready facts are validated without private reasoning;
- a governed caller consumes the mock through the provider-neutral boundary;
- substantive CI runs the suite;
- migration, correction, supersession, and rollback are exercised;
- documentation matches actual behavior.

Until then, maturity remains **README-only / implementation unconfirmed**.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Verification item | Status |
|---|---|---|
| MOCK-01 | Owners and CODEOWNERS. | NEEDS VERIFICATION |
| MOCK-02 | Permanent split with `runtime/model_adapters/mock/`. | NEEDS VERIFICATION |
| MOCK-03 | Executable mock implementation path. | UNKNOWN |
| MOCK-04 | Build/package/import contract. | UNKNOWN |
| MOCK-05 | Accepted request and response profiles. | NEEDS VERIFICATION |
| MOCK-06 | Mock profile contract and closed schema. | NEEDS VERIFICATION |
| MOCK-07 | Fixture root, manifest, IDs, and digest rules. | NEEDS VERIFICATION |
| MOCK-08 | Fixed clock, seed, locale, ordering, and comparison profile. | NEEDS VERIFICATION |
| MOCK-09 | Finite reason-code registry. | NEEDS VERIFICATION |
| MOCK-10 | Failure-injection vocabulary. | NEEDS VERIFICATION |
| MOCK-11 | No-network, DNS, subprocess, secret, and filesystem enforcement. | NEEDS VERIFICATION |
| MOCK-12 | Resource, timeout, cancellation, retry, and concurrency limits. | NEEDS VERIFICATION |
| MOCK-13 | Contract/schema fixture coverage. | NEEDS VERIFICATION |
| MOCK-14 | Policy/evidence/citation/freshness/correction negative cases. | NEEDS VERIFICATION |
| MOCK-15 | Receipt-ready facts and persistence boundary. | NEEDS VERIFICATION |
| MOCK-16 | First governed API or runtime consumer. | UNKNOWN |
| MOCK-17 | Substantive dedicated test collection. | UNKNOWN |
| MOCK-18 | Substantive CI replacing TODO echoes. | NEEDS VERIFICATION |
| MOCK-19 | Mock-to-live parity and migration policy. | NEEDS VERIFICATION |
| MOCK-20 | Correction, supersession, deactivation, and rollback drill. | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="maintenance-correction-migration-and-rollback"></a>

## Maintenance, correction, migration, and rollback

### README rollback

Before merge, close the review branch. After merge, revert the documentation commit or restore the prior blob recorded in metadata. No runtime or data rollback is required for this README-only change.

### Mock profile correction

Do not overwrite a profile silently. Preserve the prior bytes and digest, issue a new version, record the defect and affected tests/runs, supersede the defective profile, rerun deterministic and negative suites, and retain a rollback target.

### Migration to live runtime

A live adapter must not inherit authority from the mock. Revalidate contracts, schemas, provider identity, model identity, network and tool permissions, resource limits, policy/evidence/citation behavior, observability, receipts, deployment, security, and rollback. Preserve provider-neutral caller behavior and compare live results against governed mock expectations without requiring identical generated wording.

### Incident posture

Disable or quarantine the mock profile when it leaks protected data, reaches forbidden resources, becomes non-deterministic, produces unsupported `ANSWER`, omits required negative outcomes, or invalidates receipt/replay integrity. Preserve evidence needed for review without exposing protected content.

[Back to top](#top)
