<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-service-configs-readme
title: runtime/service_configs/ — Governed Runtime Service-Configuration Handoff
type: readme
version: v0.2
status: draft; repository-grounded; canonical-runtime-sublane; README-only; implementation-unconfirmed; ci-unproved; non-authoritative
owners: OWNER_TBD — Runtime steward · Configuration steward · Security steward · Infrastructure steward · Governed-API steward · Validation steward · Docs steward
created: 2026-07-05
updated: 2026-07-15
supersedes: v0.1 runtime service-configuration guardrail
policy_label: public; runtime; service-configs; no-secrets; no-public-runtime; no-policy-authority; no-release-authority
current_path: runtime/service_configs/README.md
truth_posture: CONFIRMED target README, Directory Rules v1.4 placement, runtime and configs root boundaries, configs/local ignore posture, mock-first loopback .env.example, placeholder Ollama adapter, proposed runtime envelope contracts, security doctrine, and bounded absence of tracked files under this lane beyond the README / PROPOSED runtime service-profile and activation contract / UNKNOWN owners, profile format, consumers, loaders, precedence, validation, service health, secret-store integration, deployment, receipts, and CI enforcement / NEEDS VERIFICATION accepted ADRs, schema home, consumer inventory, network controls, rollback automation, and CODEOWNERS coverage
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: faefb1f451cd0e5185b975ba8e78e69970680cb9
  prior_blob: d4fd83c12e3f573a8a3d2e60bf48b698113fd884
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  runtime_root_blob: c8a0854af5c6ac4854ad5dcc880eb81251a211c3
  configs_root_blob: 129c20163580bef696cf90fec79e063d9c9a5f08
  configs_local_blob: 16f0c64baa482db3b146aa2a8d62a9b7baf3fede
  env_example_blob: 50e972a4c5c009ed89097753932fc328039c1aec
  gitignore_blob: 50e0e0e2485e6dbd6b7e1c2767350b459335b22b
  ollama_readme_blob: b0708364fa002760383882f18843e31c6c4209c7
  ollama_adapter_blob: 1769a719d6a6df53e001abbc4c67ad486ab5c944
  adr_0008_blob: 9dcaef6cffafb4b44a9740cab5ba3811305b1983
  runtime_response_contract_blob: b81d67dccdd8470e066ab8247eb93c5df67a6679
  secrets_doc_blob: 562b654e101ca3c52e32b85f7acdaea9f589ab5c
  incident_response_blob: ee0b4ceb6d20858297dfd8308afbfb0cc50d2ea6
related:
  - ../README.md
  - ../local/README.md
  - ../model_adapters/README.md
  - ../model_adapters/AdapterContract.md
  - ../model_adapters/OllamaAdapter.py
  - ../mock/README.md
  - ../ollama/README.md
  - ../envelopes/README.md
  - ../../configs/README.md
  - ../../configs/local/README.md
  - ../../.env.example
  - ../../.gitignore
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md
  - ../../docs/security/SECRETS.md
  - ../../docs/security/INCIDENT_RESPONSE.md
  - ../../contracts/runtime/runtime_response_envelope.md
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../policy/runtime/README.md
  - ../../tests/
  - ../../tools/validators/
notes:
  - "This revision changes only runtime/service_configs/README.md."
  - "The lane remains README-only; no profile, loader, schema, validator, test, workflow, daemon, secret, deployment, or release artifact is created."
  - "Shared safe defaults and reusable templates remain canonical under configs/."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Runtime Service-Configuration Handoff

`runtime/service_configs/`

> **One-line purpose.** Document the runtime-side service-profile, binding, activation, health, and rollback boundary for KFM runtime services while shared defaults remain under `configs/`, deployment controls remain under `infra/`, and real secrets remain outside the repository.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![shared defaults](https://img.shields.io/badge/shared__defaults-configs%2F-blue)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![public runtime](https://img.shields.io/badge/public__runtime-denied-critical)

> [!IMPORTANT]
> **This README is not runtime or deployment proof.** The repository confirms this README, adjacent configuration boundaries, a mock-first loopback example, draft/proposed runtime contracts, and a placeholder Ollama adapter. It does not confirm an accepted profile format, loader, active daemon, approved model, health probe, secret store, validator, dedicated tests, substantive CI, deployment, or receipt stream.

> [!CAUTION]
> **This lane is not a second general configuration root.** Shared safe defaults and reusable templates belong under [`configs/`](../../configs/README.md). This lane documents how a named runtime service consumes reviewed configuration and how that binding is admitted, observed, disabled, or rolled back.

> [!WARNING]
> Real credentials, tokens, private URLs, signing material, passwords, protected data, secret-bearing `.env` files, and private model paths must never be committed here. A tracked secret is a security incident.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status-and-evidence-boundary) · [Placement](#repository-fit) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Profile](#proposed-runtime-service-profile) · [Security](#security-and-exposure) · [Outcomes](#finite-outcomes) · [Validation](#validation) · [Review](#review-burden) · [Rollback](#rollback-correction-and-migration) · [Open](#open-verification-register)

---

## Purpose

`runtime/service_configs/` is the runtime-facing handoff lane for **named internal services**. It documents:

- which runtime service or adapter consumes a configuration profile;
- which shared default or template the profile references;
- which non-secret binding, timeout, resource, and health classes apply;
- which evidence, policy, rights, sensitivity, and release gates remain outside the service;
- which finite outcome is returned when configuration is absent, invalid, held, disabled, or unhealthy;
- how operators deactivate, supersede, or roll back the binding.

The audience is runtime, configuration, security, infrastructure, governed-API, validation, operations, and documentation maintainers.

This README does not install or start a service, select a model, approve a provider, create policy, define schema authority, expose an endpoint, or publish KFM material.

[Back to top](#top)

---

## Authority level

**Canonical runtime sublane / non-authoritative configuration handoff.**

Directory Rules place `service_configs/` under `runtime/`. The same doctrine places reusable non-secret defaults and templates under `configs/`, deployment and exposure controls under `infra/`, semantic meaning under `contracts/`, machine shape under `schemas/`, and admissibility under `policy/`.

| Concern | Owning surface | This lane's role |
|---|---|---|
| Shared safe defaults and reusable templates | `configs/` | References them; does not duplicate them. |
| Workstation-local overrides | ignored `configs/local/` files | Documents expected override relationship only. |
| Runtime service binding and activation notes | `runtime/service_configs/` | Owns the handoff documentation. |
| Provider-neutral adapter behavior | `runtime/model_adapters/` | References the adapter boundary. |
| Provider-specific runtime behavior | accepted runtime lane, such as `runtime/ollama/` | References provider-specific constraints. |
| Deployment, service manager, firewall, proxy, network policy | `infra/` | Records required posture; does not define deployment. |
| Secret values | approved external secret system | Stores references-by-name only. |
| Contract meaning and schema shape | `contracts/`, `schemas/` | References canonical definitions. |
| Allow, deny, restrict, abstain | `policy/` | Obeys decisions; never replaces policy with config. |
| Tests and validators | `tests/`, `fixtures/`, `tools/validators/` | Names required proof. |
| Receipts, proofs, lifecycle data | `data/` | Uses governed pointers only. |
| Release, correction, withdrawal, rollback | `release/` | Cannot authorize any of them. |

No path move or new authority root is introduced by this README. A future design that makes this lane a parallel home for general configuration, policy, schemas, secrets, or deployment requires drift review and an ADR.

[Back to top](#top)

---

## Status and evidence boundary

### Confirmed at the pinned base

| Surface | Evidence | Safe conclusion |
|---|---|---|
| `runtime/service_configs/README.md` | Target blob recorded above | The directory README exists. |
| Other tracked files in this lane | Bounded repository search returned none | README-only within the inspected search boundary. |
| Directory Rules v1.4 | `runtime/service_configs/` appears in the runtime tree | Placement is doctrine-confirmed. |
| `runtime/README.md` | Parent root names this lane | Runtime service configuration is subordinate to evidence, policy, and release. |
| `configs/README.md` | Canonical configuration root | Shared defaults and templates belong there. |
| `configs/local/README.md` plus `.gitignore` | Local children are ignored except the README | Workstation overrides are untracked and non-authoritative. |
| `.env.example` | `KFM_MODEL_RUNTIME=mock`; loopback API and Ollama examples | Public example is mock-first and loopback-oriented; it is not activation proof. |
| `runtime/model_adapters/OllamaAdapter.py` | One-line placeholder | Executable adapter behavior is not implemented by file presence. |
| Runtime envelope contract/schema families | Present with draft/PROPOSED posture | Finite shapes exist as proposals; emission is unproved. |
| `policy/runtime/README.md` | Greenfield stub | Runtime policy enforcement is unproved. |
| Docs workflows | TODO echo stubs | Workflow presence is not substantive validation. |

### Unknown or needs verification

Accepted owners, profile format, loader, consumer inventory, merge precedence, service manager, model admission, secret-store integration, health checks, resource budgets, validators, fixtures, dedicated tests, policy wiring, evidence resolution, citation validation, receipts, logs, CI enforcement, deployment, public exposure, and rollback automation.

### Material correction from v0.1

The prior README allowed non-secret service templates here without clearly separating them from `configs/`. This revision narrows the boundary:

- **shared default or reusable template** → `configs/`;
- **untracked machine-local override** → `configs/local/`;
- **runtime-specific binding and activation handoff** → `runtime/service_configs/`;
- **deployment/exposure definition** → `infra/`;
- **real secret** → external secret system;
- **contract/schema/policy** → its canonical authority root.

[Back to top](#top)

---

## Repository fit

```text
runtime/
├── README.md
├── service_configs/
│   └── README.md                 # this file; runtime-side configuration handoff
├── local/                        # local runtime wiring
├── model_adapters/               # provider-neutral adapter boundary
├── mock/                         # deterministic mock runtime
├── ollama/                       # provider-specific local runtime
└── envelopes/                    # finite-outcome helpers

configs/                          # shared safe defaults and templates
configs/local/                    # ignored workstation overrides
infra/                            # deployment, service manager, network and exposure
contracts/                        # semantic meaning
schemas/                          # machine-checkable shape
policy/                           # admissibility and obligations
fixtures/  tests/  tools/        # deterministic proof and validators
data/                             # lifecycle records, receipts and proofs
release/                          # release, correction and rollback authority
```

The primary responsibility is **runtime binding**, so the path remains under `runtime/`. Domain, provider, and deployment concerns must stay in their own responsibility lanes.

[Back to top](#top)

---

## What belongs here

- This README.
- Runtime-specific profile documentation for a named service or adapter.
- References to shared defaults under `configs/`.
- Non-secret bind posture such as `loopback-only`, `private-allowlist`, or `disabled`.
- Placeholder variable names and secret references-by-name.
- Timeout, retry, cancellation, circuit-breaker, queue, concurrency, and resource classes.
- Health, readiness, governance-admission, and release-readiness semantics.
- Adapter, contract, schema, policy, fixture, test, validator, receipt, and rollback pointers.
- Activation, deactivation, supersession, and migration notes.
- Safe diagnostic field lists and redaction requirements.

A future tracked profile must identify at minimum:

| Field family | Required intent |
|---|---|
| Identity | Stable `profile_id`, version, digest/spec hash, status, owner. |
| Consumer | Named service, adapter, and caller boundary. |
| Shared configuration | Canonical default/template reference and optional local override class. |
| Binding | Host posture and port/socket class without secret-bearing private details. |
| Provider/model | Profile references only; no weights or credentials. |
| Reliability | Timeouts, retries, cancellation, idempotency, circuit breaking. |
| Resources | Context, output, memory, CPU/GPU, concurrency, queue limits. |
| Governance | Evidence, policy, rights, sensitivity, citation, release, correction obligations. |
| Observability | Safe health fields, logs, metrics, and receipt pointers. |
| Recovery | Kill switch, fallback profile, supersession, rollback target. |

[Back to top](#top)

---

## What does not belong here

| Forbidden here | Correct home or response |
|---|---|
| Shared reusable defaults or generic templates | `configs/` |
| Workstation-local secret-bearing or machine-specific files | ignored local state; not tracked |
| Real credentials, API keys, tokens, passwords, signing keys, private URLs | approved external secret system; rotate and investigate if committed |
| Provider-neutral adapter implementation | accepted adapter/implementation lane |
| Model weights, caches, binaries, private model paths | external/runtime-managed storage |
| Service manager, container, firewall, reverse proxy, VPN, Kubernetes, Terraform | `infra/` |
| Semantic object contracts | `contracts/` |
| JSON Schema | `schemas/` |
| Policy rules or decisions | `policy/` |
| Fixtures, tests, validator code | `fixtures/`, `tests/`, `tools/validators/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED data | `data/` lifecycle roots |
| EvidenceBundles, receipts, proofs, release manifests | governed `data/` and `release/` roots |
| Public API routes or UI clients | accepted app/API/UI roots |
| Direct browser-to-model or browser-to-internal-service configuration | nowhere; deny |
| Generated language treated as evidence, policy, approval, or publication | nowhere |

[Back to top](#top)

---

## Outputs

This lane may support these downstream artifacts without owning them:

- a reviewed runtime service-profile pointer;
- a configuration digest/spec hash supplied to a runtime receipt;
- a named adapter/provider binding;
- safe health/readiness metadata;
- finite failure mapping;
- activation/deactivation instructions;
- validation and negative-test requirements;
- rollback and supersession pointers.

A parsed profile, successful connection, healthy process, or model response does **not** establish evidence closure, policy allow, citation validity, review approval, release readiness, or publication authority.

[Back to top](#top)

---

## Keystone invariants

1. Evidence outranks configuration and generated output.
2. Policy, rights, sensitivity, consent, review, release, correction, and withdrawal state cannot be bypassed by flags or environment variables.
3. Public clients use governed APIs and released artifacts, never direct runtime endpoints.
4. Mock-first and no-network behavior is the deterministic default until a provider binding is explicitly admitted.
5. Real secrets are never committed.
6. Unknown fields, conflicting sources, invalid values, and unresolved secret references fail closed.
7. Health is not admission; admission is not release readiness.
8. `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` remain first-class outcomes.
9. Configuration changes that alter behavior require versioning, validation, and rollback.
10. Runtime configuration cannot move material through `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`.

[Back to top](#top)

---

## Proposed runtime service profile

The following is a **documentation contract**, not an accepted schema:

```yaml
profile_id: runtime-service:ollama-local-dev:v1
version: v1
status: held
active: false
consumer:
  service: governed-api
  adapter: ollama
configuration:
  shared_default_ref: configs/dev/<reviewed-file>
  local_override_class: configs/local/<ignored-file>
binding:
  posture: loopback-only
  endpoint_ref: env:OLLAMA_HOST
runtime:
  mode: local-ollama
  model_profile_ref: NEEDS_VERIFICATION
limits:
  connect_timeout_class: bounded
  read_timeout_class: bounded
  retries: 0
  concurrency_class: single_or_bounded
security:
  direct_public_access: deny
  outbound_network: deny_by_default
  secrets: references_only
governance:
  evidence_resolution: required_when_claim_depends_on_evidence
  policy_precheck: required
  citation_validation: required_for_answer
  finite_outcomes: [ANSWER, ABSTAIN, DENY, ERROR]
observability:
  prompt_logging: deny
  protected_context_logging: deny
  receipt_family_ref: NEEDS_VERIFICATION
rollback:
  fallback_profile_ref: runtime-service:mock:v1
  kill_switch: required
```

Required behavior:

- `active: false` or `status: held` must prevent provider activation.
- Unknown fields and duplicate keys must not be silently accepted.
- `endpoint_ref` is a reference, not permission to expose the endpoint.
- Missing policy/evidence/citation prerequisites cannot be converted to `ANSWER`.
- Fallback to mock or disabled state must preserve the public contract.

[Back to top](#top)

---

## Configuration sources and precedence

Confirmed repository surfaces are `.env.example`, `configs/`, ignored `configs/local/`, and this runtime handoff lane. No loader or merge order is verified.

A future implementation should define and test a single precedence order. A safe proposal is:

```text
canonical shared default
  < reviewed environment template
  < explicitly named local override
  < runtime-injected secret reference resolution
  < request-scoped non-secret override allowed by contract
```

This is `PROPOSED`. Before adoption, tests must prove:

- unknown and duplicate fields fail closed;
- conflicting sources produce a safe error or hold;
- request fields cannot override policy, exposure, evidence, citation, receipt, or release gates;
- logs and receipts identify which non-secret sources contributed without exposing secrets;
- defaults remain deterministic when overrides are absent.

[Back to top](#top)

---

## Security and exposure

The repository example binds the governed API and Ollama example to loopback and selects `mock` as the model runtime. Treat that as a safe public example, not runtime admission.

A future runtime binding must:

- default to disabled, mock, loopback-only, or private allowlist;
- prohibit public DNS, browser-visible model endpoints, and direct client credentials;
- keep CORS, reverse proxy, firewall, VPN, systemd, containers, and host access in `infra/`;
- prevent direct reads from RAW, WORK, QUARANTINE, canonical, or unreleased stores;
- disable outbound tools and network by default;
- resolve secret references outside the repository;
- redact endpoints and infrastructure details from public diagnostics when needed;
- expose only governed finite envelopes to clients.

A direct public model path, public runtime port, or browser-side internal service URL is a `DENY` condition.

### Secret incident response

When a real secret is committed or exposed:

1. stop using the value and take the affected surface fail-closed;
2. rotate or revoke it;
3. preserve audit evidence without redistributing the secret;
4. inspect logs, history, caches, artifacts, and downstream exposure;
5. follow security incident and correction procedures;
6. add preventive validation before reactivation.

Deleting the line is not sufficient containment.

[Back to top](#top)

---

## Finite outcomes

| Outcome | Configuration/runtime use |
|---|---|
| `ANSWER` | Profile is admitted, service is healthy enough, evidence/policy/citation gates pass, and the governed caller may answer. |
| `ABSTAIN` | Evidence, citation, freshness, model fitness, or bounded context is insufficient. |
| `DENY` | Policy, rights, sensitivity, access, release, or security posture forbids the operation. |
| `ERROR` | Configuration, loader, secret resolution, adapter, timeout, health, schema, receipt, or dependency failure prevents safe completion. |

Suggested internal operator states such as `HELD`, `DISABLED`, `NOT_CONFIGURED`, `DEGRADED`, or `CIRCUIT_OPEN` must map to one of the four governed client outcomes; they must not leak as accidental success.

### Health is not authority

Keep these states distinct:

| State | Question answered |
|---|---|
| Process health | Is the process responding? |
| Readiness | Can it accept bounded work? |
| Governance admission | Is this profile/service allowed for this task? |
| Evidence/policy/citation readiness | Can this request proceed safely? |
| Release readiness | May a downstream artifact be promoted? |

A process can be healthy while governance admission is denied.

[Back to top](#top)

---

## Reliability and observability

A future profile should define bounded timeouts, no or tightly bounded retries, cancellation propagation, idempotent request identity, circuit breaking, queue and concurrency limits, and a safe fallback.

Retries must not:

- multiply side effects or receipts without deterministic identity;
- retry `DENY` or evidence insufficiency;
- hide permanent configuration defects;
- bypass cancellation or resource budgets;
- switch providers silently.

Safe telemetry may include profile ID/version/digest, adapter/provider class, health class, latency, timeout/retry counts, finite outcome, reason code, and receipt pointer.

Telemetry must exclude credentials, secret values, prompt text by default, protected context, raw evidence, exact sensitive geometry, private model paths, private chain-of-thought, and unrestricted provider responses.

[Back to top](#top)

---

## Validation

### Documentation checks for this change

```bash
# Target and tracked-lane inventory
find runtime/service_configs -maxdepth 4 -type f | sort

# Markdown structure and relative links
python <repo-approved-markdown-checker> runtime/service_configs/README.md

# High-signal credential patterns; replace with accepted scanner
rg -n --hidden --glob '!README.md' \
  '(BEGIN .*PRIVATE KEY|github_pat_|ghp_|AKIA[0-9A-Z]{16}|Bearer[[:space:]]+[A-Za-z0-9._~+/=-]{20,})' \
  runtime/service_configs

# Relevant tests once they exist
pytest -q tests/runtime tests/configs tests/security
```

The placeholder commands are guidance, not claims of current tooling. Current documentation workflows are stubs and must not be reported as substantive enforcement.

### Future profile validation matrix

| Check | Expected failure posture |
|---|---|
| Schema and unknown fields | Reject / `ERROR` |
| Duplicate keys or conflicting sources | Reject / hold |
| Secret-like literal | Security hold and incident review when real |
| Missing consumer or adapter | `NOT_CONFIGURED` → `ERROR` |
| Public bind or direct client endpoint | `DENY` |
| Missing evidence/policy/citation requirement | `ABSTAIN` or `DENY` |
| Invalid model/profile rights | Hold or `DENY` |
| Timeout/resource limit absent | Hold |
| Health failure | `ERROR` or degraded fallback |
| Missing receipt/rollback pointer when required | Hold; no release claim |

Required negative fixtures should cover missing fields, unknown fields, duplicate keys, literal secrets, public binds, unresolved secret references, policy-bypass flags, direct raw-store paths, invalid outcomes, excessive resources, missing fallback, and stale/superseded profiles.

[Back to top](#top)

---

## Safe change and activation pattern

### Documentation-only change

1. Pin the base ref and target blob.
2. Verify Directory Rules, ADRs, drift register, parent/sibling READMEs, and nearby contracts.
3. Preserve useful existing guardrails.
4. Change only this README.
5. Validate Markdown structure, relative links, secret-safety patterns, and one-file diff scope.
6. Create a draft pull request.
7. Re-read the remote file and report workflow state accurately.

### Future profile addition

1. Confirm the named consumer and responsibility split.
2. Add or update semantic contract and schema in their canonical roots.
3. Add valid and invalid fixtures.
4. Implement fail-closed validation.
5. Prove deterministic mock behavior first.
6. Add security, evidence, policy, citation, health, resource, and rollback tests.
7. Keep provider activation disabled until every required gate passes.
8. Activate through a reviewed, reversible change.

A successful parse, connection, health probe, or model response is not enough to activate a provider for governed use.

[Back to top](#top)

---

## Review burden

Ordinary README wording changes require maintainer/docs review.

Material changes require the owning runtime/configuration maintainers plus the affected security, infrastructure, API, policy/evidence, validation, and operations reviewers. Examples include:

- new service or provider binding;
- changes to public/private bind posture;
- secret reference or injection changes;
- model/profile changes;
- evidence, policy, citation, or finite-outcome changes;
- timeout, retry, resource, logging, receipt, activation, or rollback changes.

Current CODEOWNERS is a broad greenfield placeholder and does not prove runtime-specific separation of duties.

[Back to top](#top)

---

## Related folders

- [`runtime/README.md`](../README.md)
- [`runtime/local/README.md`](../local/README.md)
- [`runtime/model_adapters/README.md`](../model_adapters/README.md)
- [`runtime/model_adapters/AdapterContract.md`](../model_adapters/AdapterContract.md)
- [`runtime/ollama/README.md`](../ollama/README.md)
- [`runtime/mock/README.md`](../mock/README.md)
- [`runtime/envelopes/README.md`](../envelopes/README.md)
- [`configs/README.md`](../../configs/README.md)
- [`configs/local/README.md`](../../configs/local/README.md)
- [`.env.example`](../../.env.example)
- [`.gitignore`](../../.gitignore)
- [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md)
- [`ADR-0008`](../../docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md)
- [`docs/security/SECRETS.md`](../../docs/security/SECRETS.md)
- [`docs/security/INCIDENT_RESPONSE.md`](../../docs/security/INCIDENT_RESPONSE.md)
- [`contracts/runtime/runtime_response_envelope.md`](../../contracts/runtime/runtime_response_envelope.md)
- [`schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json)
- [`policy/runtime/README.md`](../../policy/runtime/README.md)
- `fixtures/`, `tests/`, `tools/validators/`, `data/`, `release/`, and `infra/` counterparts as implemented and verified.

## ADRs

| Decision surface | Status | Relevance |
|---|---|---|
| Directory Rules §10.1 and §10.3 | Governing doctrine | Places this lane and separates runtime/config/infra/secrets responsibilities. |
| ADR-0008 | Proposed/draft | Keeps Ollama and local runtimes behind the governed API. |
| ADR-0001 schema-home convention | Referenced by doctrine; verify current status before schema work | Machine shape belongs under canonical `schemas/`, not here. |

This README-only clarification needs no new ADR because it creates no root, authority home, schema, policy, service, or deployment behavior.

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Purpose, authority, status, belongs/does-not-belong, inputs/outputs, validation, review burden, related folders, ADRs, and last-reviewed state are present.
- [x] The split among runtime handoff, shared configs, local overrides, infra, and secrets is explicit.
- [x] Current repository claims are pinned and bounded.
- [x] Prior no-secrets, no-public-runtime, no-policy, no-evidence, no-release, and no-lifecycle-authority guardrails are preserved.
- [x] Mock-first and loopback examples are not overstated as implementation.
- [x] No service profile, code, schema, policy, fixture, test, workflow, secret, deployment, receipt, or release artifact is created.
- [x] Rollback and verification gaps are explicit.

### Future runtime service profile

- [ ] Owners and reviewers are accepted.
- [ ] Profile contract/schema and canonical path are accepted.
- [ ] Consumer, loader, precedence, and unknown-field behavior are tested.
- [ ] Secrets remain reference-only and leak response is exercised.
- [ ] Mock-first, no-network, public-path denial, and finite outcomes are proven.
- [ ] Evidence, policy, rights, sensitivity, citation, correction, and release gates are enforced outside the service.
- [ ] Health, readiness, admission, and release readiness remain distinct.
- [ ] Reliability, resource, observability, receipt, kill-switch, migration, and rollback behavior are tested.
- [ ] Substantive CI or another enforced validation path exists.

[Back to top](#top)

---

## Rollback, correction, and migration

This README can be rolled back by reverting its single-file commit; the prior blob is recorded in the metadata block. No runtime or deployment state changes because this revision changes documentation only.

A future profile must define a safe rollback: restore the prior profile, fall back to deterministic mock, disable the optional service, drain bounded work, or forward-fix with documented containment.

Move material to `configs/` when it becomes a reusable shared default/template. Move material here only when its primary responsibility becomes a named runtime binding. Either migration must preserve history, update consumers atomically when in scope, record old/new IDs and digests, avoid parallel authority, and prove rollback.

If undocumented consumers block cleanup, record the conflict in the drift register instead of silently maintaining two authoritative homes.

[Back to top](#top)

---

## Open verification register

| Item | Status |
|---|---|
| Accepted owner and CODEOWNERS coverage | NEEDS VERIFICATION |
| Whether future profiles live here or only pointers live here | NEEDS VERIFICATION |
| Accepted profile format and schema path | UNKNOWN / NEEDS VERIFICATION |
| Named loader, consumers, and precedence | UNKNOWN |
| Unknown-field, conflict, and secret-reference behavior | UNKNOWN |
| Runtime policy and evidence/citation integration | UNKNOWN |
| Ollama daemon, adapter, model profiles, versions, rights | UNKNOWN |
| Health/readiness/admission probes | UNKNOWN |
| Reliability and resource budgets | UNKNOWN |
| Safe logs and receipt persistence | UNKNOWN |
| Dedicated validator, fixtures, tests, and substantive CI | UNKNOWN |
| Deployment, secret store, and public exposure controls | UNKNOWN / default deny |
| Kill switch and rollback automation | UNKNOWN |
| Correction and supersession registry | NEEDS VERIFICATION |

[Back to top](#top)

---

## Evidence basis

This revision is grounded in the pinned repository target and surrounding runtime/configuration/security evidence, plus the uploaded KFM repository-documentation operating prompt. It did not execute code, inspect untracked workstation files, contact a runtime, query a secret store, run a model, validate a deployment, inspect runtime logs, or prove any consumer.

Implementation, enforcement, availability, deployment, health, receipt, and CI claims therefore remain `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION` unless explicitly confirmed above.

## Last reviewed

`2026-07-15`

Review again after changes to Directory Rules, relevant ADRs, `configs/`, `.env.example`, `.gitignore`, runtime adapters/providers, profile contracts/schemas, secret/deployment posture, validation/CI, public exposure, ownership, or rollback behavior.

<p align="right"><a href="#top">Back to top</a></p>
