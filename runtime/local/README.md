<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-local-readme
title: runtime/local/ — Governed Local Runtime Wiring and Coordination Lane
type: readme; directory-readme; canonical-runtime-lane; local-runtime-coordination-boundary
version: v1.1
status: draft; repository-grounded; canonical-lane-confirmed; README-only; implementation-unconfirmed; deployment-unverified; non-authoritative
owners: OWNER_TBD — Runtime steward · Operations steward · Governed-API steward · Configuration steward · Security steward · Policy steward · Evidence steward · Citation steward · Adapter steward · Envelope steward · Test steward · Release steward · Migration steward · Docs steward
created: NEEDS VERIFICATION — greenfield stub was replaced by v1 on 2026-07-03
updated: 2026-07-15
supersedes: v1 local runtime wiring guide
policy_label: "public-doctrine; runtime; local-runtime; internal-only; mock-first; loopback-first; evidence-subordinate; policy-subordinate; release-subordinate; finite-outcomes; cite-or-abstain; no-direct-public-runtime; no-secrets; no-lifecycle-authority; rollback-aware"
current_path: runtime/local/README.md
truth_posture: >
  CONFIRMED target v1 README, canonical runtime root v0.3, Directory Rules v1.4 placement,
  path-scoped repository search returning this README as the only runtime/local result,
  shared and local-only configuration boundaries, canonical provider-neutral model-adapter lane,
  canonical deterministic mock lane, canonical Ollama provider-specific lane, canonical runtime
  envelope handoff lane, canonical runtime service-configuration handoff lane, mock-first loopback
  .env.example, schema-paired draft/PROPOSED DecisionEnvelope, RuntimeResponseEnvelope, and
  AIReceipt families, one-line OllamaAdapter placeholder, and runtime-policy greenfield stub /
  PROPOSED local runtime profile, activation record, dependency and health declaration, finite
  failure mapping, validation matrix, receipt/replay posture, and migration checklist /
  UNKNOWN executable local harness, runtime loader, local service manager, accepted request
  contract, approved adapters/providers/models, runtime policy execution, EvidenceRef resolution,
  citation validation, receipt persistence, configuration precedence, secret-store integration,
  health probes, resource limits, network/tool permissions, public-client enforcement, dedicated
  runtime/local tests, substantive CI, deployment topology, operational logs, dashboards, and
  release state /
  NEEDS VERIFICATION accepted owners, CODEOWNERS coverage, canonical local-runtime note identity,
  profile/schema home, first governed consumer, activation authority, correction propagation,
  migration receipts, kill-switch ownership, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 6c71c48e88b34d76d00b43ab39d0a3a1b99328c7
  prior_blob: 39772916a3fc25e7899570344d5c70a1cb2939c9
  runtime_root_blob: 894d15bb2e2d0185f433e35c690e0a6b42327fb9
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  configs_local_blob: 16f0c64baa482db3b146aa2a8d62a9b7baf3fede
  service_configs_blob: 90ffda75759b5b62db86aef190f2be19a8853915
  model_adapters_blob: 16456452e03884dabb24c670c41c9e359f679769
  mock_blob: b48aa917319fd4b3fc458c7b5575eaaafcdc800d
  ollama_blob: b0708364fa002760383882f18843e31c6c4209c7
  envelopes_blob: ec0d621cdfd342176fe20f7237ff113ace49e2a7
  env_example_blob: 50e972a4c5c009ed89097753932fc328039c1aec
  runtime_policy_blob: b9bfee731553c504b514f07a6862ef3e68328f02
  bounded_path_search:
    - "runtime/local returned runtime/local/README.md and no additional path result"
  bounded_commit_search:
    - "runtime/local returned the prior README expansion commit ef3915fcbc071550b69ade19121c3f41df03b5be"
related:
  - ../README.md
  - ../model_adapters/README.md
  - ../model_adapters/AdapterContract.md
  - ../model_adapters/OllamaAdapter.py
  - ../model_adapters/mock/README.md
  - ../mock/README.md
  - ../ollama/README.md
  - ../envelopes/README.md
  - ../service_configs/README.md
  - ../AI/README.md
  - ../../apps/governed-api/README.md
  - ../../configs/README.md
  - ../../configs/local/README.md
  - ../../infra/README.md
  - ../../contracts/runtime/README.md
  - ../../contracts/runtime/decision_envelope.md
  - ../../contracts/runtime/runtime_response_envelope.md
  - ../../contracts/runtime/ai_receipt.md
  - ../../schemas/contracts/v1/runtime/README.md
  - ../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../fixtures/contracts/v1/runtime/README.md
  - ../../tests/schemas/test_common_contracts.py
  - ../../tools/validators/validate_decision_envelope.py
  - ../../tools/validators/validate_runtime_response_envelope.py
  - ../../policy/runtime/README.md
  - ../../data/receipts/README.md
  - ../../release/README.md
  - ../../.env.example
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md
  - ../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - ../../docs/security/SECRETS.md
  - ../../docs/security/INCIDENT_RESPONSE.md
  - ../../docs/registers/DRIFT_REGISTER.md
tags: [kfm, runtime, local-runtime, canonical-lane, internal-wiring, governed-api, model-adapters, mock-first, loopback-first, service-configs, finite-outcomes, evidence, policy, citations, receipts, no-secrets, no-direct-public-runtime, rollback]
notes:
  - "This revision changes only runtime/local/README.md."
  - "The lane remains README-only at the bounded repository search; no harness, loader, service, adapter, config, schema, policy, fixture, test, workflow, receipt, deployment, release record, or public route is created."
  - "Local runtime wiring is distinct from ignored workstation overrides in configs/local/, reusable configuration in configs/, runtime service bindings in runtime/service_configs/, provider-neutral adapters in runtime/model_adapters/, and provider-specific Ollama details in runtime/ollama/."
  - "The prior README is preserved as lineage through the recorded prior blob and the v1 to v1.1 change summary."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `runtime/local/` — Governed Local Runtime Wiring and Coordination Lane

> **One-line purpose.** Document how an internal KFM runtime is assembled, selected, bounded, validated, observed, disabled, and rolled back on a local machine without turning workstation state, provider output, generated language, configuration, or a successful process into evidence, policy, release authority, or a direct public path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v1.1" src="https://img.shields.io/badge/version-v1.1-informational">
  <img alt="Lane: canonical local runtime" src="https://img.shields.io/badge/lane-canonical__local__runtime-success">
  <img alt="Maturity: README only" src="https://img.shields.io/badge/maturity-README__only-lightgrey">
  <img alt="Default runtime: mock" src="https://img.shields.io/badge/default__runtime-mock-blueviolet">
  <img alt="Public runtime access: denied" src="https://img.shields.io/badge/public__runtime__access-denied-red">
  <img alt="Truth posture: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-green">
</p>

> [!IMPORTANT]
> **`runtime/local/` coordinates internal local wiring; it is not a sovereign runtime authority.** A running process, successful model call, schema-valid object, green test, local override, generated answer, or healthy port does not establish source authority, evidence closure, policy approval, disclosure permission, lifecycle promotion, release approval, or public truth.

> [!CAUTION]
> **Public and semi-public clients must not call a local runtime, model provider, local port, or secret-bearing service directly.** They must use an accepted governed application boundary, receive finite response envelopes, and render only outcomes and obligations permitted by evidence, policy, rights, sensitivity, release, freshness, and correction state.

> [!WARNING]
> **Do not commit real secrets or protected context.** Tokens, passwords, private endpoints, signing material, secret-bearing `.env` files, private model paths, raw prompts, protected coordinates, restricted EvidenceBundle contents, and private chain-of-thought do not belong in this lane, examples, logs, screenshots, fixtures, diagnostics, or pull-request bodies.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Operating law](#local-runtime-operating-law) · [Flow](#governed-local-runtime-flow) · [Modes](#runtime-modes-and-activation-posture) · [Configuration](#configuration-secrets-and-local-state) · [Evidence](#evidence-policy-citation-and-release-posture) · [Receipts](#receipts-replay-and-observability) · [Security](#security-network-tools-and-exposure) · [Failures](#finite-outcomes-and-failure-semantics) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Profile](#minimal-local-runtime-profile) · [Done](#definition-of-done) · [Migration](#migration-correction-and-rollback) · [Open](#open-verification-register) · [Last reviewed](#last-reviewed)

---

## Purpose

`runtime/local/` is the canonical KFM lane for **general local runtime wiring and coordination notes**.

It exists to answer:

1. Which governed caller may request local runtime work?
2. Which runtime mode is selected: disabled, deterministic mock, provider-specific local runtime, or another reviewed binding?
3. Which provider-neutral adapter boundary is used?
4. Which tracked defaults, untracked workstation overrides, runtime service bindings, and external secret references affect the local run?
5. Which evidence, policy, rights, sensitivity, citation, release, freshness, and correction conditions must already be satisfied?
6. Which finite result may leave the runtime boundary?
7. Which receipt, envelope, version, digest, health, and rollback references make the run inspectable?
8. How can the local runtime be disabled or replaced without changing the public contract?

This lane is for coordination that crosses several runtime sublanes. Narrower concerns stay in their owning lanes:

| Concern | Owning lane |
|---|---|
| Provider-neutral adapter cards and handoffs | [`runtime/model_adapters/`](../model_adapters/) |
| Deterministic mock runtime behavior | [`runtime/mock/`](../mock/) |
| Mock adapter child notes | [`runtime/model_adapters/mock/`](../model_adapters/mock/) |
| Ollama-specific local runtime details | [`runtime/ollama/`](../ollama/) |
| Finite envelope helper and handoff notes | [`runtime/envelopes/`](../envelopes/) |
| Runtime service profile and activation handoff | [`runtime/service_configs/`](../service_configs/) |
| Shared safe defaults and reusable templates | [`configs/`](../../configs/) |
| Ignored workstation overrides | [`configs/local/`](../../configs/local/) |
| Deployment, firewall, proxy, service manager, and exposure | [`infra/`](../../infra/) |
| Public trust-membrane behavior | [`apps/governed-api/`](../../apps/governed-api/) |

This README does not start a daemon, select a model, approve a provider, define a request contract, activate policy, resolve evidence, validate citations, persist receipts, expose a route, deploy a service, or publish KFM material.

[Back to top](#top)

---

## Authority level

**Canonical runtime sublane / non-authoritative local coordination boundary.**

Directory Rules place `local/` under the canonical `runtime/` responsibility root. This lane refines the parent root; it cannot override contracts, schemas, policy, evidence, rights, sensitivity, validation, release, correction, rollback, security, or accepted ADRs.

| Concern | Authority home | `runtime/local/` role |
|---|---|---|
| Local runtime coordination | `runtime/local/` | Owns bounded coordination notes and indexes. |
| Provider-neutral adapter behavior | `runtime/model_adapters/` | References the adapter boundary and selected mode. |
| Provider-specific behavior | Accepted provider-specific runtime lane | References provider version, model profile, constraints, and kill switch. |
| Shared configuration | `configs/` | References reviewed defaults or templates. |
| Workstation-local overrides | ignored `configs/local/` files | May name an expected override relationship; cannot inventory or authorize local files. |
| Runtime service bindings | `runtime/service_configs/` | References the binding, activation, health, and rollback handoff. |
| Deployment and exposure | `infra/` | Records required posture; cannot define deployment here. |
| Semantic meaning | `contracts/` | References canonical object meaning. |
| Machine-checkable shape | `schemas/` | References canonical schemas. |
| Allow, deny, restrict, abstain, obligations | `policy/` | Obeys decisions; does not infer policy from configuration or model output. |
| Evidence and citations | Governed evidence and citation roots | Uses resolvable references; does not create evidence. |
| Tests, fixtures, validators | `tests/`, `fixtures/`, `tools/validators/` | Names required proof; does not store executable proof here. |
| Receipts and proofs | Accepted `data/` receipt/proof lanes | Uses pointers; does not invent persistence or retention behavior. |
| Release, correction, withdrawal, rollback | `release/` | Cannot authorize any governed transition. |
| Public API and client behavior | Accepted app/API/UI roots | Must remain behind the trust membrane. |

### Anti-collapse rules

This lane must not collapse:

- local runtime notes into implementation proof;
- provider output into evidence;
- configuration into policy;
- a schema-valid object into admissibility;
- a healthy process into release readiness;
- a local port into a public interface;
- generated language into a citation;
- a receipt pointer into a receipt instance;
- a release reference into release approval;
- a copied file into lifecycle promotion;
- operator convenience into durable authority.

A proposal that changes these boundaries requires explicit architecture review and normally an ADR.

[Back to top](#top)

---

## Status

### Confirmed repository state

At `main@6c71c48e88b34d76d00b43ab39d0a3a1b99328c7`:

| Surface | Status | Safe conclusion |
|---|---|---|
| `runtime/local/README.md` | **CONFIRMED** | The target v1 README exists; its prior blob is recorded above. |
| `runtime/README.md` | **CONFIRMED v0.3 canonical root** | The parent defines runtime as internal execution support subordinate to governed controls. |
| Directory Rules v1.4 | **CONFIRMED doctrine** | Names `runtime/local/` as a canonical runtime sublane. |
| Path-scoped repository search | **CONFIRMED bounded result** | Returned this README and no additional `runtime/local/` path result. |
| Path-scoped commit search | **CONFIRMED bounded result** | Returned the prior README expansion commit; no implementation lineage was established. |
| `runtime/model_adapters/` | **CONFIRMED canonical documentation lane** | Provider-neutral adapter behavior belongs there. |
| `runtime/mock/` | **CONFIRMED canonical documentation lane** | Deterministic mock runtime notes belong there. |
| `runtime/ollama/` | **CONFIRMED canonical documentation lane** | Ollama-specific local runtime guidance exists; implementation remains scaffolded. |
| `runtime/envelopes/` | **CONFIRMED canonical handoff lane** | Runtime envelope documentation and contract/schema drift are visible. |
| `runtime/service_configs/` | **CONFIRMED canonical handoff lane; README-only** | Runtime binding/configuration handoff is documented; a loader or active service is not proven. |
| `.env.example` | **CONFIRMED public example** | Uses `KFM_MODEL_RUNTIME=mock`, loopback governed API binding, and loopback Ollama host. |
| `runtime/model_adapters/OllamaAdapter.py` | **CONFIRMED placeholder through adjacent evidence** | One-line presence does not prove executable adapter behavior. |
| Runtime envelope contracts and schemas | **CONFIRMED present; draft/PROPOSED** | Finite object families exist; acceptance and runtime emission are not established. |
| Runtime validators and fixture/schema harness | **CONFIRMED adjacent surfaces** | Presence does not prove local-runtime integration or current test success. |
| `policy/runtime/README.md` | **CONFIRMED greenfield stub** | Runtime policy implementation is not established. |

### Current maturity

| Capability | Status | Safe conclusion |
|---|---:|---|
| Lane placement | **CONFIRMED** | `runtime/local/` is a canonical runtime sublane. |
| README boundary | **CONFIRMED** | Local coordination rules are documented. |
| Local harness implementation | **UNKNOWN / not found in bounded path search** | Do not claim a runnable harness. |
| Runtime loader or mode selector | **UNKNOWN** | No accepted loader or precedence behavior is established here. |
| Mock implementation | **UNKNOWN** | Mock documentation exists; executable local mock integration is not proved by this lane. |
| Provider implementation | **UNKNOWN / scaffolded adjacent evidence** | Ollama documentation and placeholder adapter exist; live binding is unproved. |
| Request contract | **NEEDS VERIFICATION** | Do not treat descriptive `FocusRequest` notes as accepted canonical meaning or shape. |
| Finite envelopes | **PROPOSED contract/schema families** | Shape and vocabulary exist, but profile conflicts and runtime use remain unresolved. |
| Policy execution | **UNKNOWN** | The runtime policy README is a stub. |
| Evidence resolution and citation validation | **UNKNOWN** | No local integration is established. |
| Receipts and persistence | **UNKNOWN** | Do not infer AIReceipt or runtime receipt emission. |
| Configuration consumer and precedence | **UNKNOWN** | Shared and local lanes are documented; consumer behavior is not established. |
| Health, logs, metrics, SLOs | **UNKNOWN** | No operational runtime proof was inspected. |
| Dedicated tests and substantive CI | **UNKNOWN** | Adjacent schema validation is not a local-runtime integration suite. |
| Deployment and public boundary enforcement | **UNKNOWN / denied by default** | No local success authorizes public exposure. |
| Ownership | **OWNER_TBD** | Accepted owners and CODEOWNERS remain unverified. |

### Material corrections from v1

The prior v1 README provided useful placement and note templates, but v1.1 narrows several boundaries:

- `runtime/local/` is **general local runtime coordination**, not a catch-all for every local file.
- `configs/local/` is the ignored workstation-override boundary; its files are unknown by design.
- Shared safe defaults and reusable templates remain under `configs/`.
- Runtime-specific service binding and activation handoffs belong under `runtime/service_configs/`.
- Provider-neutral adapter behavior belongs under `runtime/model_adapters/`.
- Ollama-specific behavior belongs under `runtime/ollama/`.
- Deterministic mock runtime notes belong under `runtime/mock/`.
- Runtime outcome objects belong to their canonical contract/schema families, not this README.
- A note status such as `ACTIVE_LOCAL` does not prove a running, approved, healthy, or release-ready service.
- The lane is README-only in the bounded repository evidence; implementation remains `UNKNOWN`.

### Current visible lane

```text
runtime/local/
└── README.md          # confirmed tracked surface in the bounded repository search
```

Do not infer ignored workstation files, unindexed branches, generated artifacts, running processes, or local machine state from this visible tree.

[Back to top](#top)

---

## What belongs here

The lane may contain, after placement and review:

- this README and a bounded local-runtime index;
- local runtime coordination notes that span multiple canonical runtime sublanes;
- local harness architecture notes that do not pretend to be executable code;
- mode-selection and dependency-wiring notes;
- loopback-only exposure and no-network-default notes;
- pointers to provider-neutral adapters and provider-specific bindings;
- references to reviewed shared defaults and runtime service profiles;
- references-by-name to external secrets;
- local health, readiness, degraded, held, disabled, and kill-switch semantics;
- finite result mapping to `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
- receipt, envelope, evidence, policy, citation, fixture, test, validator, and rollback pointers;
- deterministic replay requirements and safe diagnostic field lists;
- activation, deactivation, supersession, migration, and rollback notes;
- review records that explain why a local runtime is allowed for a named internal use case.

A new tracked artifact should answer **why its primary responsibility is general local coordination** rather than adapter, mock, Ollama, envelope, service configuration, infrastructure, test, or release work.

### Candidate local-runtime artifact classes

| Artifact class | Placement posture |
|---|---|
| Lane README or bounded index | Allowed here. |
| Cross-lane local runtime profile | **PROPOSED** here pending identity/schema/ADR review. |
| Local harness source code | **NEEDS VERIFICATION**; choose the owning app/package/runtime implementation boundary before creating it. |
| Provider-neutral adapter card | Route to `runtime/model_adapters/`. |
| Ollama-specific profile | Route to `runtime/ollama/` and referenced configuration/deployment homes. |
| Shared config template | Route to `configs/`. |
| Untracked machine override | Route to ignored `configs/local/`. |
| Service binding/activation profile | Route to `runtime/service_configs/`. |
| Deployment unit, firewall, proxy, container, service manager | Route to `infra/`. |
| Runtime fixture or test | Route to `fixtures/` or `tests/`. |
| Runtime receipt instance | Route to the accepted receipt data lane. |

Do not create a child hierarchy under `runtime/local/` merely because an artifact is used on a local machine. Placement follows responsibility, not execution location.

[Back to top](#top)

---

## What does not belong here

| Do not put this in `runtime/local/` | Correct posture |
|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | Use governed lifecycle roots under `data/`. |
| EvidenceBundle contents or source records | Use accepted evidence/source homes and resolvable references. |
| Canonical contracts | Use `contracts/`. |
| JSON Schemas | Use `schemas/`. |
| Policy rules or policy decisions | Use `policy/` and governed decision records. |
| Shared safe defaults or reusable templates | Use `configs/`. |
| Workstation-local overrides | Use ignored `configs/local/` files. |
| Runtime service binding profiles | Use `runtime/service_configs/` unless a reviewed profile explicitly spans several lanes. |
| Provider-neutral adapter implementation or cards | Use `runtime/model_adapters/` or the accepted implementation package. |
| Ollama-specific runtime files | Use `runtime/ollama/` and referenced config/infra roots. |
| Model weights, caches, manifests, or private model paths | Keep outside the repository under approved operational controls. |
| Fixture payloads or golden outputs | Use `fixtures/`. |
| Executable tests | Use `tests/`. |
| Validator implementation | Use `tools/validators/`. |
| Service units, containers, proxies, firewall rules, deployment manifests | Use `infra/`. |
| Receipts, proofs, logs, traces, or metrics as durable instances | Use accepted operational/data roots with retention and redaction controls. |
| Release manifests, promotion decisions, correction notices, withdrawal notices, rollback cards | Use `release/`. |
| Public API routes, UI components, or browser-side provider access | Use accepted app/API/UI roots behind the trust membrane. |
| Real credentials, tokens, passwords, signing material, or secret-bearing `.env` files | Never commit; use approved secret injection. |
| Raw prompts, private chain-of-thought, or unrestricted protected context | Do not store or expose. |
| Generated text presented as evidence, policy, review, release, legal/title conclusion, or public truth | Nowhere. |

### Explicit denials

This lane must not:

- expose `127.0.0.1`, a LAN address, container port, or model daemon as a public contract;
- grant network or tool access because a provider supports it;
- substitute a local environment variable for an accepted policy decision;
- treat missing evidence as permission to improvise;
- store restricted context in logs for debugging convenience;
- silently fall back from `DENY` or `ABSTAIN` to an answer;
- promote lifecycle state;
- approve release or rollback;
- claim implementation based only on README, placeholder, schema, or workflow presence.

[Back to top](#top)

---

## Inputs

A local runtime may consume only bounded, minimized, policy-safe inputs from an allowed caller.

### Governed input classes

| Input class | Minimum expectation |
|---|---|
| Caller identity | Named internal caller or governed application boundary. |
| Request identity | Stable request/correlation identifier; canonical request contract remains `NEEDS VERIFICATION`. |
| Scope | Explicit task, domain, spatial/temporal bounds, and allowed operation. |
| Runtime mode | `disabled`, `mock`, provider-specific local binding, or another reviewed mode. |
| Adapter identity | Provider-neutral adapter/profile reference and version. |
| Evidence support | Resolvable `EvidenceRef` or other allowed support pointer; do not pass canonical stores directly. |
| Policy context | Policy decision/reference, rights, sensitivity, consent, access, release, freshness, and correction posture. |
| Configuration references | Tracked default/template, optional ignored local override relationship, and runtime service-profile reference. |
| Secret references | Reference-by-name only; no secret values in a tracked profile or log. |
| Resource limits | Timeout, retry, concurrency, queue, memory/CPU/GPU class, cancellation, and circuit-breaker posture. |
| Network/tool permissions | Explicit allowlist or denial; never inherited from provider defaults. |
| Envelope profile | Accepted or explicitly proposed response profile and schema pointer. |
| Receipt posture | Required receipt class, persistence target, redaction, and retention reference when applicable. |
| Correction posture | Current correction, withdrawal, supersession, or stale-state constraints. |
| Rollback target | Previous safe mode/profile or `disabled` fallback. |

### Input rejection

Return or propagate a negative outcome when an input is:

- missing, malformed, ambiguous, stale, or unsupported;
- outside the caller's allowed scope;
- not backed by admissible evidence where evidence is required;
- denied or restricted by policy, rights, sensitivity, consent, access, or release state;
- dependent on an unapproved provider, model, adapter, profile, tool, or network destination;
- secret-bearing or overbroad;
- incompatible with the selected envelope profile;
- unable to produce the required receipt or trace boundary;
- unable to preserve correction or rollback obligations.

### Data minimization

Pass the smallest sufficient context. Prefer:

- identifiers over full records;
- generalized or redacted geometry over precise sensitive locations;
- excerpts over entire documents;
- release-safe facts over canonical/internal objects;
- references over duplicated evidence;
- bounded structured fields over raw prompt dumps;
- reason codes over private reasoning.

[Back to top](#top)

---

## Outputs

Outputs from this lane are **candidate runtime results and coordination records**, not sovereign truth.

### Permitted output classes

| Output | Required posture |
|---|---|
| Finite runtime result | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| Candidate answer payload | Must remain bounded by evidence, citations, policy, release, freshness, and correction state. |
| `DecisionEnvelope` candidate | Use the accepted profile; current contract/schema family remains draft/PROPOSED. |
| `RuntimeResponseEnvelope` candidate | Use the accepted profile; do not invent compatibility silently. |
| Receipt pointer | Must resolve to a governed receipt if the workflow requires one. |
| Evidence references | Must be resolvable and policy-safe; references do not become evidence by repetition. |
| Obligations and reason codes | Use controlled vocabularies when accepted; unresolved registries remain `NEEDS VERIFICATION`. |
| Health/readiness result | Distinguish process health from governance admission and release readiness. |
| Safe diagnostics | Structured, minimized, redacted, non-secret, and free of private reasoning. |
| Rollback/deactivation result | Records requested state and pointer; does not itself authorize release rollback. |

### Output prohibitions

A local runtime output must not:

- claim source authority it does not have;
- cite a non-resolving or unauthorized reference;
- expose restricted support;
- return private reasoning;
- return secrets or private endpoint details;
- invent an `ANSWER` after evidence, policy, citation, or validation failure;
- present `ACTIVE_LOCAL` as production or release state;
- directly mutate lifecycle or release records;
- bypass the governed application boundary.

### Finite outcome mapping

| Outcome | Use when |
|---|---|
| `ANSWER` | The caller is allowed, support is sufficient and resolvable, policy permits, citations validate, the output profile validates, and required obligations are preserved. |
| `ABSTAIN` | Evidence, authority, freshness, citation support, scope, confidence, or required context is insufficient. |
| `DENY` | Policy, rights, sensitivity, consent, access, release, correction, network, tool, model, or caller posture forbids the operation. |
| `ERROR` | Adapter, configuration, dependency, validation, timeout, resource, envelope, receipt, health, or service failure prevents a governed result. |

A local helper may use internal operational states, but public or governed caller-facing results must map deterministically to the accepted finite vocabulary.

[Back to top](#top)

---

## Local runtime operating law

Every local runtime integration should preserve these invariants:

1. **Governed caller first.** No direct browser-to-provider or browser-to-runtime path.
2. **Mock first.** Deterministic contract-valid mocks precede live-provider reliance.
3. **Provider neutrality.** Caller contracts do not depend on Ollama- or provider-specific response shapes.
4. **Evidence before interpretation.** Runtime generation cannot substitute for EvidenceBundle support.
5. **Policy outside the model.** Allow, deny, restrict, obligations, consent, and sensitivity remain governed.
6. **Cite or abstain.** Unsupported answer-like output does not pass.
7. **Finite outcomes.** Negative states are explicit and testable.
8. **Bounded context.** Inputs are minimized, scoped, and policy-safe.
9. **No implicit network or tools.** Access is explicitly admitted and least-privileged.
10. **No secrets in repo or diagnostics.** Secret references are external and redacted.
11. **Receipts without private reasoning.** Capture identities, versions, hashes, decisions, timings, and outcomes—not chain-of-thought.
12. **Deterministic identity where practical.** Profiles, adapters, models, configs, schemas, policies, and fixtures are versioned or hashed.
13. **Correction-aware.** Stale, corrected, withdrawn, or superseded support changes downstream eligibility.
14. **No lifecycle authority.** Runtime cannot promote data.
15. **No release authority.** Runtime cannot approve publication, correction, withdrawal, or rollback.
16. **Reversible activation.** Every non-mock binding has a disable path and safe fallback.
17. **Health is not governance.** A responding process may still be denied, held, stale, or unapproved.
18. **Documentation is not proof.** Code, fixtures, tests, workflow results, receipts, and runtime evidence are required for behavior claims.

[Back to top](#top)

---

## Governed local runtime flow

The intended flow is:

```text
internal caller or governed API
  -> authenticate / authorize caller
  -> scope and minimize request
  -> resolve policy-safe evidence support
  -> evaluate rights / sensitivity / consent / access / release / freshness / correction
  -> choose runtime mode
       -> disabled
       -> deterministic mock
       -> admitted provider-specific local runtime
  -> load reviewed non-secret defaults and approved binding references
  -> apply resource / network / tool / timeout / cancellation limits
  -> invoke provider-neutral adapter
  -> receive candidate result
  -> validate envelope / citations / obligations / redaction
  -> emit required receipt pointer
  -> return ANSWER / ABSTAIN / DENY / ERROR
```

This is a **PROPOSED operating flow**. Current repository evidence does not prove every stage is implemented.

### Gate order

A safe implementation should fail closed in this order:

1. caller and scope;
2. rights, sensitivity, consent, access, and release;
3. evidence resolution and freshness;
4. runtime mode and provider/model admission;
5. configuration and secret-reference resolution;
6. network, tool, and resource admission;
7. adapter execution;
8. output schema, policy, citation, and redaction checks;
9. receipt and observability obligations;
10. governed caller response.

Do not invoke a provider merely to discover that the request should have been denied earlier.

[Back to top](#top)

---

## Runtime modes and activation posture

### Proposed mode vocabulary

| Mode | Meaning | Default exposure |
|---|---|---|
| `disabled` | No local runtime invocation is allowed. | Denied. |
| `mock` | Deterministic fixture-backed behavior only. | Internal tests or reviewed local development. |
| `local_provider` | A reviewed provider-specific local binding behind the provider-neutral adapter boundary. | Loopback/private only; public denied. |
| `held` | Configuration or implementation exists but governance admission is incomplete. | Denied. |
| `degraded` | Runtime is partially available but must return bounded negative outcomes for unsupported work. | Internal only. |
| `retired` | Binding is no longer selectable. | Denied. |

These mode names are **PROPOSED**, not an accepted contract.

### Activation prerequisites

A non-mock local runtime should not become selectable until all applicable items are evidenced:

- accepted caller and use case;
- accepted adapter/request/envelope profile;
- provider and model identity, version, digest, rights, and risk review;
- approved configuration references and secret injection;
- loopback/private exposure and network/tool allowlists;
- deterministic mock and negative fixtures;
- adapter unit tests and local integration tests;
- evidence, policy, citation, and correction integration tests;
- four-outcome coverage;
- timeout, cancellation, retry, circuit-breaker, and resource tests;
- required receipt emission and redaction tests;
- public-boundary denial tests;
- health, readiness, governance-admission, and kill-switch behavior;
- steward review and rollback target.

### Health versus admission

Keep these distinct:

| State | Question |
|---|---|
| Process health | Is the process responding? |
| Dependency readiness | Are required local dependencies available? |
| Contract readiness | Do request and response profiles validate? |
| Governance admission | Is this provider/model/config allowed for this use case now? |
| Evidence readiness | Is required support resolvable and current? |
| Release readiness | May any resulting material enter a governed release process? |
| Public eligibility | May a governed client render the result? |

A healthy process can still be unapproved, held, denied, stale, or release-ineligible.

[Back to top](#top)

---

## Configuration, secrets, and local state

### Boundary map

| Configuration concern | Correct home |
|---|---|
| Shared safe defaults | `configs/` |
| Reusable templates and examples | Reviewed tracked lanes under `configs/` |
| Workstation-specific overrides | Ignored `configs/local/` files |
| Runtime binding and activation handoff | `runtime/service_configs/` |
| General cross-lane local coordination | `runtime/local/` |
| Provider-specific settings and constraints | Provider-specific runtime lane, such as `runtime/ollama/` |
| Deployment/service manager/network exposure | `infra/` |
| Secret values | Approved external secret system |
| Secret reference names | May appear in reviewed docs/configs when non-sensitive |
| Contract, schema, policy | Their canonical authority roots |

### Confirmed public example posture

The root `.env.example` currently documents:

```text
KFM_ENV=dev
KFM_LOG_LEVEL=info
KFM_API_BIND=127.0.0.1
KFM_API_PORT=8080
KFM_MODEL_RUNTIME=mock
OLLAMA_HOST=http://127.0.0.1:11434
```

This confirms a **mock-first, loopback-oriented example**, not a loader, precedence rule, active daemon, approved model, secret integration, or deployment.

### Precedence

Do not document or implement a generic precedence chain without a verified consumer. A candidate consumer-specific order might be:

```text
accepted built-in safe default
  -> tracked reviewed environment/profile
  -> optional ignored workstation override
  -> external secret injection
  -> command-line or operator override, only if explicitly allowed
```

This order is **PROPOSED** and must be bound to an actual loader, schema, tests, unknown-field behavior, and security review before it becomes a fact.

### Secret posture

- Store references-by-name, never values.
- Redact values from exceptions, traces, health output, screenshots, and support bundles.
- Do not expose private URLs when a symbolic endpoint identity is sufficient.
- Do not print full environment dictionaries.
- Do not copy `.env` contents into PRs or issue reports.
- Treat accidental tracked secret exposure as an incident and rotate/revoke according to security doctrine.
- Ignored files are not automatically safe; they can leak through backups, shell history, editor sync, logs, screenshots, and archives.

[Back to top](#top)

---

## Evidence, policy, citation, and release posture

### Evidence

A local runtime may interpret governed support. It cannot create source authority.

When an answer depends on evidence:

- resolve the `EvidenceRef` or equivalent allowed pointer;
- verify source authority, rights, sensitivity, freshness, correction, and release state;
- provide only the minimum permitted support;
- validate citations against the actual support;
- abstain when support is missing, stale, non-resolving, unauthorized, or insufficient.

### Policy

Policy evaluation must remain outside provider discretion.

The runtime must not infer permission from:

- model confidence;
- prompt wording;
- local configuration;
- network reachability;
- a successful provider response;
- the absence of an explicit deny string;
- a schema-valid payload.

Current repository evidence confirms only a greenfield `policy/runtime/README.md` stub. Executable runtime policy remains `UNKNOWN`.

### Citations

An answer-like result should not pass merely because it contains citation-shaped text. Citation validation should confirm:

- the reference resolves;
- the cited support is admissible for the caller;
- the claim is actually supported;
- location and time scope are correct;
- correction/withdrawal state is current;
- no restricted detail is leaked;
- the response profile preserves required evidence references.

### Release and lifecycle

Local runtime output cannot:

- promote data from one lifecycle state to another;
- approve a ReleaseManifest or PromotionDecision;
- create publication authority;
- override a correction or withdrawal;
- authorize rollback;
- make an unreleased object public.

A local result may support a governed review packet only through explicit pointers and validation records.

[Back to top](#top)

---

## Receipts, replay, and observability

### Receipt posture

When required, a local run should produce or reference a governed receipt that captures enough to inspect and replay the decision boundary without storing private reasoning.

Candidate fields include:

- run/request/correlation identity;
- caller and use-case identity;
- runtime mode;
- adapter/profile version and digest;
- provider/model identity and digest, when applicable;
- configuration/profile digest and non-secret reference set;
- contract/schema/policy versions;
- EvidenceRef identifiers or bounded support digests;
- start/end time and duration;
- resource and timeout class;
- network/tool permission profile;
- finite outcome and controlled reason codes;
- obligation and citation-validation result;
- correction/release state references;
- redaction status;
- prior safe profile and rollback target.

These fields are **PROPOSED** until aligned with accepted receipt contracts and data placement.

### Private reasoning

Do not store:

- hidden chain-of-thought;
- unrestricted raw prompts;
- complete restricted evidence;
- secrets;
- unnecessary personal or precise sensitive location data;
- model internals that are not required for audit.

Store structured reasons, obligations, references, versions, hashes, and outcomes instead.

### Replay

A reproducible local run should pin or record:

- request/profile version;
- adapter/provider/model identity;
- configuration and policy digests;
- evidence/citation support identity;
- fixture identity for mocks;
- deterministic seed where meaningful;
- time source and evaluation timestamp;
- known nondeterminism;
- expected outcome class;
- correction and supersession state.

Replay success does not prove source truth or current admissibility; support and policy may have changed.

### Observability

Safe local diagnostics should distinguish:

- process health;
- dependency readiness;
- adapter invocation;
- policy/evidence/citation gate state;
- finite outcome counts;
- latency/resource classes;
- receipt persistence status;
- correction/rollback events.

Diagnostics must be minimized, redacted, retention-bounded, and access-controlled.

[Back to top](#top)

---

## Security, network, tools, and exposure

### Default security posture

- loopback-only unless explicitly reviewed;
- no public provider or runtime port;
- no browser-direct provider calls;
- no unrestricted egress;
- no tools by provider default;
- no shell, filesystem, database, or canonical-store access without explicit least-privilege admission;
- no secret values in tracked files;
- no restricted context in routine logs;
- no silent fallback to a less governed mode;
- fail closed when policy, evidence, citation, configuration, or receipt gates are unavailable.

### Network admission

A networked local runtime profile should state:

- allowed destination identity;
- protocol and port class;
- DNS and redirect posture;
- timeout and retry limits;
- proxy and certificate posture;
- request/response size limits;
- logging and redaction behavior;
- offline/no-network test mode;
- kill switch;
- owner and review record.

### Tool admission

A tool-capable adapter should require:

- named tool identity and version;
- explicit caller/use-case allowlist;
- least-privilege input/output contract;
- sandbox boundary;
- denied operations;
- timeout/resource limits;
- deterministic or mock substitute;
- receipt and audit fields;
- negative tests;
- revocation and rollback path.

Provider capability does not equal KFM permission.

### Public boundary

The governed API or another accepted trust-membrane caller owns public-facing enforcement. `runtime/local/` must not define a public contract, URL, browser SDK, CORS policy, tile/API route, or UI integration.

[Back to top](#top)

---

## Finite outcomes and failure semantics

Negative states are first-class behavior.

| Condition | Expected finite posture |
|---|---|
| Caller not allowed | `DENY` |
| Sensitive/rights/consent/access policy forbids | `DENY` |
| Required evidence missing or insufficient | `ABSTAIN` |
| Evidence reference does not resolve | `ABSTAIN` or `ERROR` according to accepted contract |
| Citation support does not validate | `ABSTAIN` |
| Runtime mode disabled | `DENY` or `ERROR` according to caller contract |
| Adapter/profile not admitted | `DENY` |
| Config missing or invalid | `ERROR` |
| Secret reference unavailable | `ERROR` |
| Dependency unhealthy | `ERROR` |
| Provider/model unavailable | `ERROR` |
| Timeout or cancellation | `ERROR` |
| Resource limit exceeded | `ERROR` |
| Envelope validation fails | `ERROR` |
| Receipt required but cannot persist | Fail closed; usually `ERROR` |
| Correction or withdrawal invalidates support | `ABSTAIN` or `DENY` |
| All gates pass and support is sufficient | `ANSWER` |

Do not hide a negative result behind generic success text.

### Operational states

Internal coordination may also use states such as:

- `DRAFT`;
- `READY_FOR_REVIEW`;
- `MOCK_ONLY`;
- `HELD`;
- `ACTIVE_LOCAL`;
- `DEGRADED`;
- `DISABLED`;
- `SUPERSEDED`;
- `RETIRED`.

These are **PROPOSED coordination states**. They are not the canonical caller-facing finite outcome vocabulary and do not prove implementation or release status.

[Back to top](#top)

---

## Validation

Validation must match the claim being made. README presence validates documentation only.

### Documentation checks

```bash
test -f runtime/local/README.md

python - <<'PY'
from pathlib import Path

path = Path("runtime/local/README.md")
text = path.read_text(encoding="utf-8")
required = [
    "## Purpose",
    "## Authority level",
    "## Status",
    "## What belongs here",
    "## What does not belong here",
    "## Inputs",
    "## Outputs",
    "## Validation",
    "## Review burden",
    "## Related folders",
    "## ADRs",
    "## Last reviewed",
]
positions = [text.index(heading) for heading in required]
assert positions == sorted(positions)
assert text.count("```") % 2 == 0
assert not any(line.endswith((" ", "\t")) for line in text.splitlines())
print("runtime/local README structure: PASS")
PY
```

### Repository inventory checks

```bash
find runtime/local -maxdepth 4 -type f -print | sort
git log --oneline -- runtime/local
git grep -n "runtime/local" -- . ':!runtime/local/README.md'
```

Review results; do not infer implementation absence from one search alone.

### Link and secret checks

```bash
python -m pip install --disable-pip-version-check --quiet linkchecker
linkchecker runtime/local/README.md

git grep -nE \
  '(BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|github_pat_|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|Bearer[[:space:]]+[A-Za-z0-9._~+/-]+=*)' \
  -- runtime/local/README.md
```

A secret scanner should supplement, not replace, review.

### Contract and schema checks

Use the repository's accepted validators and fixtures for the chosen envelope profile. Current adjacent entry points include:

```bash
python tools/validators/validate_decision_envelope.py
python tools/validators/validate_runtime_response_envelope.py
pytest tests/schemas/test_common_contracts.py
```

These checks do not prove a local runtime integration unless local adapter, policy, evidence, citation, receipt, and public-boundary behavior are also exercised.

### Required test families before implementation claims

| Test family | Minimum negative and positive coverage |
|---|---|
| Mode selection | disabled, mock default, admitted local provider, unknown mode |
| Configuration | missing, malformed, unknown fields, stale version, override precedence |
| Secrets | missing reference, denied plaintext value, redacted error/log |
| Adapter | success, unsupported request, malformed output, exception |
| Evidence | resolving support, missing support, stale/corrected/withdrawn support |
| Policy | allow, deny, restrict/obligation, evaluator unavailable |
| Citation | valid support, non-resolving reference, unsupported claim, restricted citation |
| Outcomes | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Envelope | valid profile, unknown profile, schema failure, obligation mismatch |
| Receipts | required success, persistence failure, redaction, join/replay |
| Time/resources | timeout, cancellation, retry cap, concurrency/resource limit |
| Network/tools | denied by default, allowlisted destination/tool, revocation |
| Health | process healthy but governance held; dependency unavailable; degraded mode |
| Public boundary | direct browser/runtime/provider path denied |
| Correction | stale cache invalidated; superseded support changes outcome |
| Rollback | provider disabled; mock/disabled fallback; prior profile restored |

### CI posture

A green generic docs or schema workflow is not sufficient to claim local-runtime readiness. A substantive gate should:

- collect real tests;
- fail closed;
- avoid `|| true` for mandatory controls;
- run offline/mock tests by default;
- make provider integration opt-in and non-secret;
- validate negative outcomes;
- publish inspectable test/receipt artifacts without protected data;
- block public-boundary regressions.

[Back to top](#top)

---

## Review burden

### Routine documentation review

Required for:

- wording, navigation, metadata, evidence snapshot, and link corrections;
- status clarifications that do not change authority;
- adding verified references to existing canonical lanes.

Reviewers:

- runtime steward or subsystem maintainer;
- docs steward.

### Elevated steward review

Required when a change touches:

- runtime modes or activation;
- provider/model admission;
- adapters or envelope profiles;
- evidence or citation behavior;
- policy, rights, sensitivity, consent, access, or release;
- secret handling;
- network, tools, filesystem, database, or canonical-store access;
- receipts, logs, retention, or private context;
- public API/client behavior;
- correction, withdrawal, supersession, or rollback;
- path placement, migration, or compatibility commitment.

Include relevant runtime, governed-API, security, policy, evidence, release, configuration, test, and migration stewards.

### ADR or migration record required

Normally required for:

- a new child authority lane under `runtime/local/`;
- moving implementation into or out of this lane;
- defining a canonical local-runtime profile/schema home;
- changing the public trust membrane;
- accepting direct provider access;
- changing finite outcome vocabulary;
- creating a new receipt family;
- changing secret, network, tool, or logging posture;
- retaining a compatibility path as durable authority;
- changing the split among `runtime/local/`, `runtime/service_configs/`, `configs/`, `infra/`, and provider-specific lanes.

### Review evidence

A behavior-changing PR should state:

- exact scope and base commit;
- confirmed versus proposed behavior;
- affected contracts, schemas, policy, configs, tests, fixtures, validators, receipts, apps, infra, and release records;
- negative tests;
- security and privacy review;
- migration and rollback;
- current workflow results;
- unresolved risks.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`runtime/`](../) | Canonical parent runtime responsibility root. |
| [`runtime/model_adapters/`](../model_adapters/) | Canonical provider-neutral adapter lane. |
| [`runtime/model_adapters/mock/`](../model_adapters/mock/) | Mock-only adapter child lane. |
| [`runtime/mock/`](../mock/) | Deterministic mock runtime lane. |
| [`runtime/ollama/`](../ollama/) | Provider-specific local Ollama lane. |
| [`runtime/envelopes/`](../envelopes/) | Finite-outcome envelope helper and handoff lane. |
| [`runtime/service_configs/`](../service_configs/) | Runtime service-binding and activation handoff. |
| [`runtime/AI/`](../AI/) | Governed-AI compatibility and index lane; not canonical implementation authority. |
| [`apps/governed-api/`](../../apps/governed-api/) | Intended public/semi-public trust membrane. |
| [`configs/`](../../configs/) | Shared safe defaults and templates. |
| [`configs/local/`](../../configs/local/) | Ignored workstation-local overrides. |
| [`infra/`](../../infra/) | Deployment, service manager, firewall, proxy, and exposure controls. |
| [`contracts/runtime/`](../../contracts/runtime/) | Canonical runtime object meaning. |
| [`schemas/contracts/v1/runtime/`](../../schemas/contracts/v1/runtime/) | Machine-checkable runtime shapes. |
| [`policy/runtime/`](../../policy/runtime/) | Runtime policy lane; currently a greenfield stub. |
| [`fixtures/contracts/v1/runtime/`](../../fixtures/contracts/v1/runtime/) | Contract-valid and invalid runtime fixtures. |
| [`tests/`](../../tests/) | Executable proof. |
| [`tools/validators/`](../../tools/validators/) | Validator implementation. |
| [`data/receipts/`](../../data/receipts/) | Receipt documentation and instances under accepted layout. |
| [`release/`](../../release/) | Release, correction, withdrawal, and rollback authority. |
| [`docs/security/`](../../docs/security/) | Secret and incident-response doctrine. |
| [`docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | Placement and architecture drift register. |

### Dependency direction

Preferred direction:

```text
governed caller
  -> provider-neutral runtime boundary
  -> local mode binding
  -> provider-specific adapter/service

local runtime
  -> references contracts / schemas / policy / evidence / configs
  -> emits validated finite candidates and receipt pointers

public clients
  -> governed API
  -X-> local runtime internals
  -X-> provider ports
  -X-> secret stores
  -X-> canonical/internal data stores
```

[Back to top](#top)

---

## ADRs

### Existing related ADRs

| ADR | Current posture | Relevance |
|---|---|---|
| [`ADR-0008 — Ollama subordinate to governed API`](../../docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md) | Draft/proposed in current evidence | Keeps local model runtime behind the governed API. |
| [`ADR-0019 — AI adapter contract and finite envelopes`](../../docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md) | Draft/proposed in current evidence | Proposes provider-neutral adapters and four finite outcomes. |

Neither ADR is implementation proof.

### ADR backlog

| Decision | Status |
|---|---|
| Canonical local-runtime request contract and schema | NEEDS VERIFICATION |
| Canonical local-runtime profile identity and storage home | NEEDS VERIFICATION |
| Runtime mode and activation vocabulary | PROPOSED |
| Configuration loader and precedence contract | NEEDS VERIFICATION |
| Envelope profile reconciliation | NEEDS VERIFICATION |
| Receipt family, persistence, redaction, and retention | NEEDS VERIFICATION |
| Provider/model admission and rights review | NEEDS VERIFICATION |
| Network/tool permission model | NEEDS VERIFICATION |
| Health versus governance-admission contract | PROPOSED |
| Public-boundary enforcement and local integration topology | NEEDS VERIFICATION |
| `runtime/local/` implementation ownership versus app/package/infra homes | NEEDS VERIFICATION |
| Correction propagation and rollback automation | NEEDS VERIFICATION |

Do not create parallel schema, contract, policy, receipt, configuration, or implementation homes while these decisions remain open.

[Back to top](#top)

---

## Minimal local runtime profile

The following is a **documentation template**, not an accepted schema or active configuration:

```markdown
# <local-runtime-profile-id>

## Status
DRAFT / READY_FOR_REVIEW / MOCK_ONLY / HELD / ACTIVE_LOCAL / DEGRADED / DISABLED / SUPERSEDED / RETIRED

## Scope
- Caller:
- Allowed use case:
- Spatial/temporal/domain bounds:
- Public exposure: DENIED

## Runtime selection
- Mode:
- Provider-neutral adapter:
- Provider-specific binding:
- Provider/model identity and digest:
- Prior safe mode:

## Governed dependencies
- Request contract/schema:
- Decision/envelope contract/schema:
- Policy reference:
- Evidence/citation reference:
- Receipt profile:
- Correction/release reference:

## Configuration
- Shared default/template:
- Optional local override relationship:
- Runtime service profile:
- External secret references:
- Precedence contract:

## Security and resources
- Bind/exposure:
- Network allowlist:
- Tool allowlist:
- Timeout/retry/cancellation:
- CPU/memory/GPU/concurrency:
- Redaction/retention:

## Validation
- Mock fixtures:
- Adapter tests:
- Evidence/policy/citation tests:
- Four-outcome tests:
- Receipt tests:
- Public-boundary denial tests:
- Workflow/run evidence:

## Operations
- Health/readiness:
- Governance admission:
- Observability:
- Kill switch:
- Rollback target:
- Owner/reviewer:
- Review date:

## Open blockers
- <item or none>
```

Do not commit a profile containing secret values, private endpoints, raw prompts, protected evidence, precise sensitive locations, or private reasoning.

### Proposed identity posture

Until an accepted registry exists, use a stable, human-readable identifier and record:

- profile ID;
- version;
- status;
- owner;
- content/spec digest;
- supersedes/superseded-by;
- created/reviewed timestamps;
- canonical references.

The identifier format remains `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Definition of done

### Documentation-only revision

- [ ] Target and parent root evidence are pinned.
- [ ] Directory Rules placement is cited.
- [ ] Canonical and adjacent lane boundaries are explicit.
- [ ] Confirmed, proposed, conflicted, unknown, and needs-verification claims are separated.
- [ ] No secrets or protected context are present.
- [ ] Relative links resolve.
- [ ] Required README headings are present and ordered.
- [ ] Markdown fences and whitespace pass.
- [ ] Rollback is mechanical.

### First executable local-runtime slice

Not done until:

- [ ] owning implementation path is verified against Directory Rules;
- [ ] accepted request, adapter, and envelope profiles exist;
- [ ] deterministic mock path exists and passes;
- [ ] evidence, policy, citation, correction, and release gates are integrated;
- [ ] configuration loader and precedence are explicit and tested;
- [ ] secret injection and redaction are tested;
- [ ] four finite outcomes are covered;
- [ ] network/tool access is denied by default and tested;
- [ ] receipts are emitted or failure is fail-closed;
- [ ] health and governance admission are distinct;
- [ ] direct public/provider access is denied by tests;
- [ ] dedicated local-runtime tests run in substantive CI;
- [ ] deployment and operational state are evidenced;
- [ ] owners and reviewers accept the slice;
- [ ] kill switch and rollback are tested;
- [ ] docs and changelog are updated.

A working local demo is not sufficient.

[Back to top](#top)

---

## Migration, correction, and rollback

### Placement migration

Before moving or creating local-runtime artifacts:

1. inventory current files, inbound links, consumers, configs, tests, workflows, receipts, and deployments;
2. classify each artifact by primary responsibility;
3. consult Directory Rules and accepted ADRs;
4. record conflicts in the drift register;
5. choose one canonical home;
6. add compatibility pointers only when needed;
7. update contracts, schemas, policy, configs, tests, docs, and ownership together;
8. validate old and new paths;
9. record migration and rollback;
10. remove compatibility surfaces only after consumers and links are verified.

Do not perform a file move and call it promotion.

### Runtime correction

When a local runtime document or profile is wrong:

- preserve the prior version or blob;
- state the correction and affected claims;
- update references and compatibility notes;
- invalidate stale examples or cached guidance;
- identify affected tests, receipts, consumers, and deployments;
- re-run relevant validation;
- record reviewer and date.

### Runtime rollback

A safe rollback may require:

- disable the affected mode/profile;
- restore `mock` or `disabled`;
- revoke provider/model/tool/network admission;
- restore the prior reviewed configuration/profile;
- stop or isolate the local service through the owning operational surface;
- invalidate stale outputs and caches;
- preserve receipts and incident evidence;
- notify governed callers;
- record the rollback target and reason;
- update docs and correction records.

For this README revision, rollback is mechanical: revert the update commit or restore prior blob `39772916a3fc25e7899570344d5c70a1cb2939c9`.

[Back to top](#top)

---

## Open verification register

| Item | Evidence needed |
|---|---|
| Exact recursive `runtime/local/` inventory | Commit-pinned tree listing and file classification. |
| Accepted owners and CODEOWNERS | Current ownership rules plus steward confirmation. |
| First governed consumer | Verified app/package/runtime call path and tests. |
| Canonical request contract | Accepted semantic contract, paired schema, fixtures, validator, and ADR. |
| Local runtime profile home and identity | Directory Rules review, schema/contract decision, registry and migration plan. |
| Runtime mode vocabulary | Accepted contract or ADR plus tests. |
| Executable mock path | Code, deterministic fixtures, four-outcome tests, current CI results. |
| Provider-specific activation | Adapter implementation, provider/model profile, rights/security review, integration tests, receipts, kill switch. |
| Configuration loading and precedence | Consumer code, parser/schema, unknown-field behavior, override and secret tests. |
| Secret-store integration | Approved mechanism, least privilege, rotation, redaction, incident hooks. |
| Runtime policy execution | Executable policy bundle, evaluator wiring, negative tests, audit records. |
| Evidence and citation integration | Resolver/citation code, failure tests, receipts, governed caller integration. |
| Envelope profile conflict | Accepted profile/compatibility decision and parity tests. |
| Receipt persistence | Accepted contract/profile, data home, join behavior, retention, redaction, replay. |
| Health and observability | Health/readiness/admission contracts, logs, metrics, dashboards, SLOs, alerts. |
| Network and tool admission | Allowlist model, sandbox, denied operations, tests, revocation. |
| Dedicated tests and CI | Collected local-runtime tests and fail-closed workflow evidence. |
| Deployment and public boundary | Infra config, route inventory, network tests, direct-access denial tests. |
| Correction propagation | Invalidation, cache, supersession, caller notification, receipt linkage. |
| Rollback automation | Tested disable/fallback/restore path and rollback records. |
| Operational health | Current runtime logs, receipts, metrics, incidents, and service status. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-15 |
| Evidence base | `main@6c71c48e88b34d76d00b43ab39d0a3a1b99328c7` |
| Target prior blob | `39772916a3fc25e7899570344d5c70a1cb2939c9` |
| Review mode | Repository-grounded documentation revision; one-file scope |
| Implementation effect | None — documentation only |
| Rollback | Revert the update commit or restore the prior blob; no runtime, config, secret, adapter, model, service, test, data, receipt, deployment, release, or public route is changed |

### Maintenance triggers

Re-review when:

- the lane receives its first tracked file beyond this README;
- a local harness or loader is implemented;
- a governed caller invokes a local runtime;
- runtime mode or activation vocabulary changes;
- an adapter/provider/model becomes executable or admitted;
- a local-runtime profile or schema is accepted;
- configuration loading, precedence, or secret integration changes;
- runtime policy, evidence resolution, or citation validation becomes executable;
- envelope profiles are reconciled;
- receipt persistence is implemented;
- network or tool access changes;
- dedicated tests or workflows are introduced;
- deployment or public-boundary behavior changes;
- correction or rollback automation changes;
- Directory Rules or an accepted ADR changes placement.

### v1 → v1.1 change summary

- Grounds the lane against the merged runtime-root v0.3 evidence.
- Records the bounded README-only inventory and avoids implementation overclaiming.
- Separates general local coordination from `configs/local/`, `runtime/service_configs/`, `runtime/model_adapters/`, `runtime/mock/`, `runtime/ollama/`, `runtime/envelopes/`, and `infra/`.
- Corrects `ACTIVE_LOCAL` so it is visibly a proposed coordination state, not implementation or release proof.
- Adds governed inputs, candidate outputs, finite outcomes, fail-closed semantics, and public-boundary denials.
- Adds configuration, secret, evidence, policy, citation, receipt, replay, observability, network, tool, and resource posture.
- Adds implementation admission gates, negative test families, ADR backlog, definition of done, correction, migration, and rollback.
- Preserves the prior README's central purpose and lineage while making current uncertainty explicit.

<p align="right"><a href="#top">Back to top</a></p>
