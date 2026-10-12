<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-governed-api-deployment-rules
title: Governed API — Deployment Rules
type: standard
version: v0.2
status: draft; repository-grounded; deployment-unverified; non-release; non-publication
owners: "@bartytime4life via CODEOWNERS routing; accountable API, security, infrastructure, and operations stewardship NEEDS VERIFICATION"
created: 2026-05-24
updated: 2026-08-19
policy_label: public
current_path: docs/architecture/governed-api/DEPLOYMENT_RULES.md
owning_root: docs/
responsibility: explain the governed API deployment boundary, current repository evidence, required deployment properties, and the proof needed before deployment claims are allowed
truth_posture: >-
  CONFIRMED current repository paths, the bounded WSGI scaffold, the three registered
  ABSTAIN routes, the loopback-only Compose placeholder, non-root placeholder image,
  static Compose checks, build-only Compose workflow, accepted Directory Rules v2, and
  CODEOWNERS routing / PROPOSED deployment controls and acceptance profiles / UNKNOWN
  live environments, ingress, TLS, CORS, authentication, authorization, rate limiting,
  secret store, network enforcement, observability, health, release binding, deployment,
  external verification, and publication
supersedes: v0.1 at the same path; documentation only
related:
  - README.md
  - README.md
  - ../deployment-topology.md
  - THREAT_MODEL.md
  - AUDIENCE_CLASSES.md
  - ENVELOPES.md
  - ERROR_CODES.md
  - LIFECYCLE_GATES.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../infra/README.md
  - ../../../infra/compose/docker-compose.yml
  - ../../../infra/docker/Dockerfile.governed-api
  - ../../../apps/governed-api/src/governed_api/main.py
  - ../../../apps/governed-api/src/governed_api/routes/registry.py
  - ../../../apps/governed-api/src/governed_api/stub.py
  - ../../../apps/governed-api/tests/test_boundary_guards.py
  - ../../../tests/infra/test_compose_static.py
  - ../../../.github/workflows/infra-compose-smoke.yml
  - ../../../.github/workflows/api-test.yml
tags:
  - kfm
  - architecture
  - governed-api
  - deployment
  - trust-membrane
  - tls
  - cors
  - rate-limit
  - secrets
  - observability
  - network
  - health
  - rollback
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 091c128261d0bec26de36d9df7a549c4f3402777
  target_prior_blob: 977709a9f6cbac8bef8e433e0d4a0b2bf7d034aa
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  governed_api_main_blob: 4eb335f5fe69a492b27edb5dcaad55ec5a62d38a
  route_registry_blob: 341816f22115bd25f30d5d74e23dc26bdbfd0066
  stub_blob: 371e60cefe9d0b909e59267bab46cab6c56e267a
  compose_blob: 8a45891700a501f6e18a921ce8d260956441e4b3
  governed_api_dockerfile_blob: a84d9fb0eff8c8557645203f8ddb5e155398d329
  compose_static_test_blob: 7627d55ec83ec15e848f637522b907c0f55f5e9d
  compose_workflow_blob: a9b51526bbcf9bf80295cc8fd3a9188bcca97da2
  api_test_workflow_blob: 84ba16a3c36a1d58b2f6f1059a31ed6354063357
  audience_classes_blob: 28662c84ac1347cd63f0246fc47d418f76b7ec0b
  inspection_method: exact repository file reads and open-pull-request overlap search; no mounted checkout, container startup, live environment, ingress, host, cluster, secret store, network control, deployment record, dashboard, or runtime log inspected
notes:
  - "This revision keeps the stable document ID, H1, path, and numbered section anchors."
  - "Legacy deployment prescriptions are retained as design concerns but no longer presented as current implementation or accepted numeric profiles."
  - "The document explains requirements; infra/, apps/, configs/, runtime/, policy/, tests/, release/, and data/ retain their own authorities."
  - "No route, contract, schema, policy, configuration, workflow, image, environment, release, deployment, or publication state changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed API — Deployment Rules

> **One-line purpose.** Separate what the repository currently proves about Governed API deployment preparation from the controls a real deployment must implement and the evidence required before KFM may call that deployment ready, released, deployed, verified, or public.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-bounded-conclusion)
[![Runtime: bounded ABSTAIN scaffold](https://img.shields.io/badge/runtime-bounded%20ABSTAIN%20scaffold-1f6feb?style=flat-square)](#current-bounded-conclusion)
[![Compose: render/build only](https://img.shields.io/badge/compose-render%2Fbuild%20only-6e7781?style=flat-square)](#current-bounded-conclusion)
[![Deployment: unknown](https://img.shields.io/badge/deployment-UNKNOWN-b42318?style=flat-square)](#current-bounded-conclusion)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-boundary)

> [!IMPORTANT]
> **Safe current conclusion:** the repository contains a bounded WSGI Governed API scaffold, three registered `GET` routes that return `ABSTAIN / NOT_IMPLEMENTED`, loopback-only placeholder Compose ports, non-root placeholder Dockerfiles, static Compose boundary tests, and a workflow that renders and builds the placeholders without starting services. This is deployment-preparation evidence only. It does **not** establish application packaging, startup, health, ingress, TLS, CORS, authentication, authorization, rate limiting, secret management, enforced network policy, observability, release binding, a live environment, deployment, external verification, or publication.

> [!CAUTION]
> A Dockerfile, Compose file, port mapping, workflow, passing image build, route test, badge, pull request, merge, or this document is not a deployment decision. KFM publication remains a separate governed state transition with evidence, policy, review, release, correction, and rollback support.

> [!NOTE]
> **Document authority:** this file is a human-readable architecture standard under `docs/`. It does not configure infrastructure, define application behavior, create policy, approve an audience, issue a release, or operate an environment. Enforceable mechanics remain in their owning roots and must be validated there.

---

## Table of contents

1. [Scope](#1-scope)
2. [Deployment placement](#2-deployment-placement)
3. [TLS posture](#3-tls-posture)
4. [CORS posture](#4-cors-posture)
5. [Rate limits](#5-rate-limits)
6. [Secret hygiene](#6-secret-hygiene)
7. [Log discipline](#7-log-discipline)
8. [Network policy](#8-network-policy)
9. [Health, readiness, and tracing](#9-health-readiness-and-tracing)
10. [Anti-patterns](#10-anti-patterns)
11. [Open questions and ADR triggers](#11-open-questions-and-adr-triggers)
12. [Related docs](#12-related-docs)
13. [Appendix](#13-appendix)

---

## Current bounded conclusion

The current repository supports a narrow, no-network development and validation story:

```text
apps/governed-api/ WSGI scaffold
  -> /bootstrap, /layers, /evidence
  -> schema-shaped ABSTAIN / NOT_IMPLEMENTED responses

infra/compose/docker-compose.yml
  -> loopback-only placeholder port declarations
  -> placeholder image builds
  -> no service startup or health proof
```

The following maturity states remain distinct:

| State | Meaning | Current status |
|---|---|---|
| **Source present** | Relevant files exist at a pinned commit. | **CONFIRMED** |
| **Statically checked** | Selected path, non-root, loopback, and forbidden-mount rules are tested. | **CONFIRMED, bounded** |
| **Image-buildable** | Placeholder Dockerfiles build in the Compose smoke workflow. | **CONFIRMED, bounded** |
| **Application-packaged** | The image contains the Governed API payload and deterministic startup command. | **UNKNOWN / HOLD** |
| **Startable** | The declared service starts under the intended image and configuration. | **UNKNOWN / HOLD** |
| **Healthy** | Liveness, readiness, dependency, and shutdown behavior are observed. | **UNKNOWN / HOLD** |
| **Integrated** | Evidence, policy, release, correction, and rollback dependencies are wired and tested. | **UNKNOWN / HOLD** |
| **Released** | A governed release record identifies exact deployable bytes and rollback target. | **UNKNOWN / HOLD** |
| **Deployed** | A named environment has applied the released bytes. | **UNKNOWN / HOLD** |
| **Verified** | Independent probes and records confirm the intended environment behavior. | **UNKNOWN / HOLD** |
| **Published** | KFM has authorized a public or semi-public exposure. | **UNKNOWN / HOLD** |

See [`deployment-topology.md`](../deployment-topology.md) for the broader repository-wide readiness map.

[↑ Back to top](#top)

---

## 1. Scope

This document defines the cross-environment properties expected of a Governed API deployment and the evidence needed to claim those properties. It is intentionally provider-neutral and environment-neutral.

### In scope

- placement and authority boundaries for deployment-related work;
- transport security, proxy trust, and browser-origin posture;
- resource and abuse controls;
- secret references, loading, rotation, revocation, and leak response;
- operational logging, audit separation, metrics, and tracing;
- ingress, egress, administrative, and dependency boundaries;
- liveness, readiness, startup, shutdown, and degraded-state behavior;
- release binding, environment identity, validation, correction, and rollback;
- finite `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`, and `HOLD` conclusions.

### Out of scope

- selecting a cloud, cluster, reverse proxy, certificate authority, identity provider, rate-limit product, secret manager, log backend, tracing backend, or monitoring vendor;
- declaring the historical `public`, `partner`, `steward`, `internal`, or `denied` literals to be a canonical audience enum;
- defining exact route paths, quotas, TLS versions, cipher suites, retention periods, health endpoint names, or service-level objectives without an accepted profile and implementation evidence;
- changing route behavior, response contracts, schemas, policy, infrastructure, workflows, release state, deployment state, or publication state;
- documenting confidential environment details or security-sensitive topology.

### When these rules bind

Use this document when a change proposes to:

1. package or start `apps/governed-api/`;
2. expose it through a proxy, load balancer, tunnel, VPN, service mesh, or public edge;
3. add authentication, authorization, CORS, rate limits, health, metrics, or tracing;
4. connect evidence, policy, release, source, model, catalog, tile, or data dependencies;
5. create or change an environment profile;
6. claim readiness, release, deployment, verification, rollback, or public exposure.

### Reading rule

A row marked **Required before exposure** is a target requirement, not proof that the repository currently satisfies it. A row marked **HOLD** blocks the corresponding maturity claim until its acceptance evidence exists.

[↑ Back to top](#top)

---

## 2. Deployment placement

### Authority boundary

Accepted Directory Rules v2, through [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), make placement a responsibility decision. This existing document remains under `docs/architecture/governed-api/` because it explains the deployment boundary to humans. It does not move deployment mechanics into `docs/`.

| Concern | Owning root | This document's relationship |
|---|---|---|
| Human architecture and deployment rules | `docs/` | Explain the boundary and verification burden. |
| Deployable Governed API process | [`apps/governed-api/`](../../../apps/governed-api/) | Own application behavior, package metadata, startup contract, and app-local configuration. |
| Deployment, host, network, ingress, hardening, and provisioning | [`infra/`](../../../infra/) | Own executable or declarative deployment mechanics. |
| Shared non-secret defaults and templates | [`configs/`](../../../configs/) | Own genuinely shared configuration; app-only settings stay with the app. |
| Runtime provider adapters and deterministic local composition | [`runtime/`](../../../runtime/) | Remain private and subordinate to the Governed API. |
| Semantic interface meaning | [`contracts/`](../../../contracts/) | Define meaning; do not place semantic authority in infrastructure files. |
| Machine-checkable shape | [`schemas/`](../../../schemas/) | Validate manifests and envelopes where a canonical schema exists. |
| Admissibility, access, rights, sensitivity, and fail-safe decisions | [`policy/`](../../../policy/) | Decide allowance; infrastructure only enforces reviewed consequences. |
| Executable proof and fixtures | [`tests/`](../../../tests/) and [`fixtures/`](../../../fixtures/) | Prove positive and negative behavior without becoming policy or release authority. |
| Process receipts and proof support | [`data/receipts/`](../../../data/receipts/) and [`data/proofs/`](../../../data/proofs/) | Record bounded process/proof objects; neither self-authorizes release. |
| Release, correction, withdrawal, and rollback decisions | [`release/`](../../../release/) | Bind exact deployable bytes and environment transitions. |
| Operational procedures | [`docs/runbooks/`](../../runbooks/) | Describe reviewed actions after mechanics and ownership exist. |

### Current repository evidence

| Surface | What is confirmed | What is not established |
|---|---|---|
| [`main.py`](../../../apps/governed-api/src/governed_api/main.py) | Standard-library WSGI app and a local `serve()` helper bound by default to `127.0.0.1:8000`. | Production server, process manager, concurrency, timeouts, proxy handling, graceful shutdown, or container command. |
| [`routes/registry.py`](../../../apps/governed-api/src/governed_api/routes/registry.py) | Exactly `/bootstrap`, `/layers`, and `/evidence` are registered. | Health, metrics, admin, auth, or deployment-control routes. |
| [`stub.py`](../../../apps/governed-api/src/governed_api/stub.py) | Registered routes produce bounded `ABSTAIN / NOT_IMPLEMENTED` payloads. | Evidence resolution, policy execution, release checks, or live serving. |
| [`Dockerfile.governed-api`](../../../infra/docker/Dockerfile.governed-api) | Pinned base, bounded package install, non-root user, and `/app` workdir. | Application payload, startup command, health check, exposed port contract, or deployability. |
| [`docker-compose.yml`](../../../infra/compose/docker-compose.yml) | Loopback host mapping `127.0.0.1:8080:8080`. | An app command listening on container port `8080`, startup, health, dependency wiring, or public ingress. |
| [`test_compose_static.py`](../../../tests/infra/test_compose_static.py) | Context/Dockerfile resolution, final non-root user, loopback ports, and selected forbidden mounts/escape settings. | Service startup, network enforcement, application behavior, image content, vulnerabilities, or environment state. |
| [`infra-compose-smoke.yml`](../../../.github/workflows/infra-compose-smoke.yml) | Static checks plus Compose render and placeholder image build; services are deliberately not started. | Runtime, health, release, deployment, or publication. |
| [`api-test.yml`](../../../.github/workflows/api-test.yml) | Governed API smoke and ABSTAIN envelope tests. | Deployment, ingress, auth, rate, CORS, TLS, secret, observability, or environment proof. |

### Current integration HOLDs

1. The placeholder image does not copy or install the application and has no `CMD` or `ENTRYPOINT`.
2. Compose declares container port `8080`, while the current standalone helper defaults to `8000`; no packaging or environment profile reconciles that difference.
3. No health check, startup dependency, ingress, secret, configuration, or release identity is bound to the service.
4. No current repository evidence identifies a deployed environment or externally reachable route.
5. No current repository evidence proves the old `dev / staging / prod` channel assumption or any per-region replica model.

These are deployment-readiness gaps, not authorization to implement them inside this documentation change.

[↑ Back to top](#top)

---

## 3. TLS posture

### Current state

No TLS listener, reverse-proxy configuration, certificate reference, trusted-proxy profile, forwarded-header policy, or observed HTTPS endpoint was verified in the inspected Governed API, Compose, Dockerfile, tests, or workflows. **Public or semi-public exposure therefore remains HOLD.**

### Required before exposure

| Rule | Required property | Acceptance evidence |
|---|---|---|
| Encrypt untrusted hops | Consequential request and response traffic is encrypted across every hop outside an explicitly reviewed trusted boundary. | Reviewed ingress topology, configuration, and an observed probe against the named environment. |
| Bind an environment identity | Certificates and hostnames identify the intended environment and release channel. | Certificate/hostname inventory, expiry/renewal evidence, and environment record. |
| Refuse unsafe plaintext | Plaintext must not serve protected content. Redirect, refusal, or absence of a plaintext listener is selected deliberately for the environment. | Negative probe showing no protected response over plaintext. |
| Trust proxy metadata narrowly | Forwarded scheme, host, client address, and trace headers are accepted only from named trusted proxies. | Proxy allowlist/configuration plus spoofed-header negative tests. |
| Manage keys outside Git | Private keys, signing material, and credentials are never committed or baked into images. | Secret reference review and image/repository scan. |
| Renew and revoke | Certificate renewal and emergency revocation have an owner, observable signal, and tested procedure. | Runbook, dry run, or provider record plus alert path. |
| Apply browser transport policy safely | HSTS, subdomain scope, and any preload decision are enabled only after domain ownership, all affected subdomains, rollback cost, and certificate continuity are reviewed. | Header probe and documented scope decision. |
| Protect internal hops proportionately | Internal encryption or mutual authentication follows the actual topology and threat model; it is not inferred from a legacy audience label. | Accepted environment profile and mutual-auth negative tests where required. |

### Non-prescriptive items

This document does not hard-code TLS `1.3`, permit or forbid a specific `1.2` cipher suite, require OCSP stapling, force `includeSubDomains`, opt into browser preload, or mandate mutual TLS for a historical `internal` class. Those choices are version-sensitive and topology-specific. The deployed ingress profile must state its supported protocol set and be checked against current security guidance at implementation time.

### Failure behavior

- A certificate, identity, proxy-trust, or transport-policy failure must not silently downgrade to an unsafe listener.
- Public clients receive a bounded safe failure; operator detail stays out of public envelopes.
- A failed transport check blocks the **verified** and **published** states even when an image or service is otherwise healthy.

[↑ Back to top](#top)

---

## 4. CORS posture

### Current state

The inspected WSGI scaffold emits JSON responses but contains no verified CORS middleware or origin policy. The route registry contains only `GET` handlers and the boundary tests reject other methods on registered routes. There is no verified browser-client transport integration. **Any CORS posture remains PROPOSED / HOLD.**

### Rules

| Rule | Requirement |
|---|---|
| CORS is not authorization | Authentication, capability, field, evidence, policy, release, and sensitivity checks remain server-side. |
| Origin policy is route- and environment-bound | Allowed origins, methods, headers, credentials, exposed headers, and cache behavior belong to a reviewed profile tied to exact routes and clients. |
| Default is no browser delegation | A route without an admitted CORS profile emits no cross-origin permission. |
| Credentials narrow the profile | Credentialed browser requests require exact origins; origin reflection without validation and `*` with credentials are forbidden. |
| Public wildcard requires proof | A wildcard may be considered only for an explicitly public, non-credentialed, release-safe route with no restricted fields and an accepted exposure profile. No such profile is verified today. |
| Preflight is behavior, not decoration | `OPTIONS`, allowed methods, headers, status, cache headers, and `Vary` behavior are tested against the actual edge and application composition. |
| Error paths match the profile | CORS behavior on `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `404`, `405`, and rate-limit responses is deliberate and does not leak protected metadata. |
| Origins are environment-specific | Development loopback origins do not automatically become staging or production origins. |
| Browser controls do not weaken non-browser controls | A command-line client or server-to-server caller receives the same policy and release checks even though CORS does not apply. |

### Acceptance evidence

A CORS claim requires:

1. a canonical route/client exposure profile;
2. configuration in the owning app or infrastructure lane;
3. positive and negative tests for admitted and rejected origins;
4. credentials and cookie/token posture where applicable;
5. observed headers at the final ingress, including cache behavior;
6. evidence that the Explorer uses the governed endpoint rather than internal stores;
7. a rollback that removes the exposure without leaving cached permissive headers.

The historical audience-class table is not an origin allowlist. See [`AUDIENCE_CLASSES.md`](AUDIENCE_CLASSES.md) for the current vocabulary HOLD.

[↑ Back to top](#top)

---

## 5. Rate limits

### Current state and vocabulary correction

No rate limiter, quota store, distributed counter, route cost profile, retry contract, load test, or abuse-control configuration was verified. The historical `T-PUB`, `T-PART`, `T-STEW`, and `T-INT` tiers depended on audience literals that are not established as the canonical runtime model. They are retained as lineage only and must not be implemented as current authority.

### Required control dimensions

A future rate-control profile should make these dimensions explicit rather than deriving them from one broad class:

| Dimension | Examples of required decisions |
|---|---|
| Route and operation | Read-only bootstrap, layer discovery, evidence resolution, export, admin, or future mutation. |
| Caller or workload identity | Anonymous network source, authenticated principal, capability grant, service identity, or trusted scheduled workload. |
| Cost | CPU, memory, resolver calls, policy evaluation, external adapter work, response size, or export duration. |
| Scope | Per connection, source address, principal, grant, tenant, route, service, environment, and global aggregate. |
| Burst and sustained budget | Bounded burst, refill behavior, concurrency, queueing, and timeout. |
| Failure mapping | HTTP status, finite KFM outcome, reason code, retry advice, and cache behavior. |
| Dependency failure | Fail-safe behavior when the limiter or counter store is unavailable. |
| Exemption | Named operational exception, approver, scope, expiry, audit, and revocation. |
| Privacy | Avoid high-cardinality or sensitive identifiers in metrics and logs. |

### Rules

- A limit must protect both availability and trust-bearing dependencies; an inexpensive route and an evidence-resolution route need not share the same budget.
- Exhaustion must return a bounded response consistent with the accepted envelope and error-code contracts. This document does not invent a current `error/rate/*` code.
- Retry advice is emitted only when the system can support it accurately.
- Distributed deployments must define counter consistency and failure behavior.
- Expensive work should have concurrency, payload-size, and execution-time bounds in addition to request counts.
- Repeated abuse must not trigger a deliberately slow “tar-pit” response that consumes more service capacity.
- Emergency overrides are time-bounded and auditable; they do not bypass evidence, policy, release, or sensitive-field controls.
- A limiter failure must not silently grant broader access. The exact fail-open or fail-closed behavior for a genuinely public-safe route requires an accepted availability profile.

### Acceptance evidence

Rate-limit readiness requires deterministic unit/contract tests, integration tests at the actual ingress, load and abuse tests, bounded-cardinality metrics, failure-injection for the counter backend, retry-behavior tests, and an environment-specific rollback or disable plan. Numeric limits remain **NEEDS VERIFICATION** until measured.

[↑ Back to top](#top)

---

## 6. Secret hygiene

### Current state

The placeholder Governed API Dockerfile contains no application payload or secret references, and the current Compose placeholder contains no `secrets:` block or sensitive mounts. That is a useful negative boundary, not proof of a secret-management system. No secret store, workload identity, key rotation process, or live credential was inspected.

### Rules

| Rule | Requirement |
|---|---|
| Keep values out of Git | Secret values, private keys, tokens, passwords, and restricted connection strings are never committed, placed in generated receipts, or embedded in images. |
| Separate reference from value | Repository configuration may name a required secret reference and shape; the value is supplied by the environment's approved secret mechanism. |
| Minimize privilege | Each workload receives only the secrets and operations it needs, for the shortest practical lifetime. |
| Fail safely at bootstrap | Missing, malformed, expired, or unauthorized secret material prevents the affected capability from starting or becoming ready; it does not fall back to a default credential. |
| Redact before output | Logs, traces, metrics labels, errors, envelopes, crash reports, and test snapshots never contain secret values. |
| Rotate and revoke | Normal rotation and emergency revocation are testable, observable, attributable, and recoverable. |
| Avoid secret sprawl | Do not duplicate the same secret into Compose, app config, workflow variables, images, and runbooks. |
| Treat workload identity separately | Service identity, caller identity, and user authorization are distinct from secret storage. |
| Keep tests synthetic | Tests use synthetic values or isolated test credentials and prove that accidental echo is rejected. |
| Record incidents privately | Suspected exposure follows [`SECURITY.md`](../../../SECURITY.md); public issues and pull requests contain no usable secret detail. |

### Required deployment evidence

- secret inventory by reference name and consumer, without values;
- source and rotation owner;
- least-privilege policy or role binding;
- bootstrap and revocation negative tests;
- repository, image, log, and artifact scan results;
- incident and rollback procedure;
- proof that the old value stops working after rotation where the provider permits such testing.

No specific secret manager, cloud workload identity, SPIFFE deployment, or rotation cadence is selected here.

[↑ Back to top](#top)

---

## 7. Log discipline

### Current state

The inspected scaffold does not establish a structured logging, audit, metrics, or tracing subsystem. GitHub workflow logs are CI execution output only. They are not Governed API operational logs, KFM receipts, EvidenceBundles, review records, release records, or publication proof.

### Object-family separation

| Record | Purpose | Must not be collapsed into |
|---|---|---|
| Operational log | Diagnose service events and capacity. | Evidence, policy decision, review, receipt, or release. |
| Security/audit event | Record a security-relevant or authority-relevant action with protected access. | General debug output or public response. |
| Metric | Aggregate bounded operational signals. | Per-person activity history or release approval. |
| Trace | Correlate a request across reviewed components. | Raw evidence store, prompt archive, or unrestricted payload capture. |
| KFM receipt | Record what governed process ran with which pinned inputs and outputs. | Ordinary application log or automatic approval. |
| Proof/review/release object | Support validation, human decision, and release state. | Logging backend entry. |

### Rules

- Prefer structured, allowlisted event fields over payload echo and arbitrary object serialization.
- Use a request or operation correlation identifier that is safe to expose at the relevant boundary; do not assume it is identical to every envelope or trace identifier until the contract says so.
- Never log raw evidence bodies, prompts, model context, secret values, authorization tokens, private headers, restricted geometry, living-person data, DNA/genomics, confidential source locators, or internal-store credentials.
- Route, outcome, reason, release, policy, and evidence identifiers are recorded only at the precision permitted by policy and the environment's audit profile.
- Public-facing errors remain bounded; operator detail is correlated internally rather than returned.
- Retention, deletion, legal hold, access, export, and regional storage are explicit. They are not inferred from a legacy audience class.
- Sampling is selected by event type and risk, not by a broad caller label. Security and release-relevant audit events require their own completeness rule.
- High-cardinality fields are bounded before they reach metrics or indexing systems.
- Redaction is tested on normal responses, errors, exceptions, malformed requests, adapter failures, and startup failures.
- Logging or tracing backend failure must not cause secret/payload fallback or silently disable required security audit behavior.

### Acceptance evidence

A deployment must identify the logging and audit schemas, allowed/forbidden fields, retention and access profiles, redaction tests, sink-failure behavior, correlation model, dashboard/alert ownership, and rollback. No current deployment satisfies this merely because CI emits logs.

[↑ Back to top](#top)

---

## 8. Network policy

### Current state

Compose publishes both placeholder services only on host loopback, and the static test rejects selected privileged and sensitive-mount patterns. No proxy route, firewall rule, VPN, cluster network policy, egress allowlist, DNS policy, service identity, or applied host state was verified. Loopback binding is a bounded local-development safeguard, not a complete deployment topology.

### Required boundaries

```text
public or approved client
  -> reviewed ingress / edge
  -> Governed API
  -> reviewed internal services and released artifacts only

never as a normal path:
public client
  -> RAW / WORK / QUARANTINE / canonical store
  -> direct model runtime
  -> source credential or unrestricted provider
  -> review/admin/debug surface
```

| Boundary | Required posture |
|---|---|
| Public ingress | Only named, reviewed routes and methods are reachable through the intended edge. |
| Direct service access | Pod, container, VM, development port, debug server, and admin interfaces are not independently public. |
| Internal dependencies | Each connection is named, authenticated where required, least-privilege, time-bounded, and observable. |
| Canonical/internal stores | Not exposed as public endpoints; the Governed API reaches only reviewed interfaces needed for its bounded role. |
| Model runtimes | Private and subordinate; no browser or public client sends direct model traffic. |
| External providers | Egress occurs through the owning connector/adapter boundary and accepted source/rights profile, not arbitrary route-handler URLs. |
| Egress | Deny or constrain by destination, protocol, operation, redirect behavior, and resolved address according to threat model. |
| DNS and redirects | Defend against rebinding, private-address pivoting, open redirects, and allowlist bypass. |
| Admin and review | Separate route, identity, authorization, and network posture; absence of public advertisement is not sufficient. |
| Static artifacts | Only released, public-safe carriers are served; a reachable object-store path is not release authorization. |
| Telemetry | Destinations and exported fields are reviewed; telemetry cannot become an exfiltration path. |

### Acceptance evidence

A network claim requires the intended topology, exact exposed route/port inventory, firewall/proxy/mesh or equivalent configuration, negative reachability tests, egress and SSRF tests, dependency identity tests, observed environment probes, and a rollback that removes exposure. Configuration source and applied state must be distinguishable.

[↑ Back to top](#top)

---

## 9. Health, readiness, and tracing

### Current state

No `/healthz`, `/readyz`, `/metrics`, or other operator endpoint appears in the current route registry. No container health check, Compose health check, startup probe, readiness dependency, metrics exporter, tracing SDK, or observed health signal was verified. Those historical endpoint names are not current API facts.

### Health semantics before endpoint names

| Signal | Required meaning | Must not do |
|---|---|---|
| **Liveness** | The process can make progress and is not irrecoverably wedged. | Depend on every external provider or expose sensitive state. |
| **Startup** | Required local initialization for the selected capability profile completed. | Mark a process ready merely because the socket opened. |
| **Readiness** | The instance can safely serve the routes enabled for that environment and release. | Claim global readiness when evidence, policy, release, or required dependency state is unavailable. |
| **Dependency status** | Named internal dependency status is available to authorized operators at bounded detail. | Publish provider names, internal addresses, credentials, or restricted failure detail. |
| **Degraded state** | The service narrows capabilities or returns finite safe outcomes according to contract. | Guess, bypass policy, or serve stale/unreleased material silently. |
| **Shutdown** | New work stops, in-flight work is bounded, and termination is observable. | Drop trust-bearing actions without a receipt/audit consequence when one is required. |

Endpoint paths and exposure classes are selected only after the app, ingress, operator surface, and authorization model exist. Operator health endpoints should not be added to the public route registry by default.

### Metrics

Metrics must have bounded cardinality and avoid secret, personal, sensitive, source-private, exact-location, prompt, and evidence-body data. A minimum useful set may include request counts, finite outcomes, latency, saturation, dependency status, policy/evidence resolution failures, readiness transitions, and build/release identity—but only after field and retention review.

### Tracing

- A standard trace-context format is **PROPOSED**, not implemented.
- Incoming trace headers are validated at trust boundaries and are not blindly trusted as local identity.
- Trace identifiers may correlate to a response identifier, but equality is not assumed until the envelope contract requires it.
- Span names and attributes are allowlisted; raw evidence, prompts, tokens, restricted coordinates, and private provider URLs are excluded.
- Sampling, export, retention, tenant separation, and operator access are explicit.
- The trace backend is not evidence authority, release authority, or a substitute for a KFM receipt.

### Acceptance evidence

Health/observability readiness requires application tests, container/orchestrator checks, dependency-failure injection, startup/shutdown tests, unauthorized-access negatives, cardinality/redaction tests, observed environment signals, alert ownership, and rollback. A green image build cannot satisfy these checks.

[↑ Back to top](#top)

---

## 10. Anti-patterns

| Anti-pattern | Why it fails | Required correction |
|---|---|---|
| Calling a placeholder image “deployed” | Buildability is not startup, health, environment, or release proof. | Use the maturity vocabulary and provide environment evidence. |
| Copying the app into the image without a startup contract | The image may contain bytes but remain non-startable or ambiguous. | Pin package, command, port, user, config, and shutdown behavior. |
| Exposing the development WSGI helper publicly | It is not established as a production server or hardened ingress. | Add a reviewed production serving profile and tests. |
| Treating a loopback Compose port as a public topology | Loopback is local binding only. | Document and test the actual ingress and negative reachability. |
| Hard-coding TLS versions forever in prose | Security guidance and platform support change. | Pin an environment profile and reverify current guidance. |
| Trusting all forwarded headers | Clients can spoof scheme, host, or address. | Accept them only from reviewed trusted proxies. |
| Wildcard or reflected CORS without an exposure profile | Browser delegation can exceed intended public surface. | Use exact tested profiles or retain no CORS permission. |
| Using legacy audience labels as auth or rate-limit policy | The vocabulary is not established as a canonical runtime enum. | Resolve caller, capability, field, route, and exposure dimensions separately. |
| Tar-pitting abusive clients | It consumes service capacity and complicates failure semantics. | Return bounded responses and enforce upstream controls. |
| Secrets in `.env`, Compose, images, logs, traces, receipts, or PRs | Values persist and spread beyond intended controls. | Externalize, rotate, revoke, scan, and use references only. |
| Logging full request/response or evidence payloads | It can duplicate restricted truth into an uncontrolled store. | Allowlist structured fields and test redaction. |
| Public health, metrics, debug, or admin endpoints by accident | Operational detail and control surfaces cross the membrane. | Separate ingress, identity, authorization, and network policy. |
| Route-handler arbitrary egress | It bypasses source, rights, adapter, SSRF, and audit boundaries. | Use governed connector/adapter paths and explicit egress policy. |
| Treating CI logs or telemetry as receipts/proofs | Object-family authority collapses. | Emit governed objects through their canonical process only. |
| Claiming readiness because all upstreams answer | Safe serving also depends on policy, evidence, release, configuration, and route profile. | Define readiness by enabled capability and fail-safe behavior. |
| Deploying a commit rather than a released artifact identity | Commit existence does not establish approved deployable bytes. | Bind image/package digest to a release/candidate record and rollback target. |
| Editing docs to “complete” a control | Prose cannot enforce infrastructure or runtime behavior. | Implement and test the control in its owning root. |

[↑ Back to top](#top)

---

## 11. Open questions and ADR triggers

### Current HOLD register

| Item | What must be decided or proven | Decision home | Current state |
|---|---|---|---|
| Application packaging | Build context, install/copy method, immutable dependency set, startup command, port, worker/concurrency model, timeouts, and shutdown. | `apps/governed-api/` + `infra/docker/` | **HOLD** |
| Compose port contract | Reconcile declared container port `8080` with the app's current local default `8000`. | `infra/compose/` + app config | **HOLD** |
| Environment profiles | Names, purpose, isolation, configuration ownership, data class, release channel, and rollback. | `infra/`, `configs/`, `release/` | **HOLD** |
| Ingress and TLS | Edge topology, trusted proxies, certificate identity, plaintext behavior, headers, and current protocol profile. | `infra/` + security review | **HOLD** |
| Caller and capability model | Authentication, principal/workload identity, capability grants, field-level authorization, revocation, and audit. | contracts/schemas/policy/apps | **HOLD** |
| CORS | Exact clients, origins, routes, methods, headers, credentials, caches, and negative tests. | app/infra config + tests | **HOLD** |
| Rate and abuse controls | Cost model, scopes, numerical budgets, backend, failure behavior, and load evidence. | app/package/infra + tests | **HOLD** |
| Secret management | Provider, references, workload identity, least privilege, rotation, revocation, and scans. | infra/config/security | **HOLD** |
| Network and egress | Exposed routes/ports, dependency edges, provider egress, SSRF controls, admin separation, and applied-state proof. | `infra/` | **HOLD** |
| Health and observability | Signal semantics, endpoint/control plane, metrics, traces, retention, alerts, and redaction. | app/infra/runbooks | **HOLD** |
| Release binding | Image/package digest, SBOM/attestation posture where required, release decision, correction, and rollback target. | `release/` and governed support lanes | **HOLD** |
| Environment verification | Independent probes, drift detection, incident route, and rollback rehearsal. | tests/tools/runbooks/release | **HOLD** |
| Public exposure | Rights, sensitivity, evidence, policy, review, release, route, field, and rollback closure. | governed release process | **HOLD** |

### ADR triggers

An accepted ADR or equivalent governed decision is required when a change:

- changes a root or authority boundary;
- establishes a new canonical public path, caller/identity model, envelope meaning, release gate, or cross-service trust boundary;
- selects a long-lived architecture that materially constrains multiple applications or environments;
- creates a compatibility break or retires an existing interface;
- changes the relationship among evidence, policy, release, correction, rollback, and public exposure.

A routine provider/configuration selection does not automatically need an ADR when it stays inside an accepted architecture, has a clear owner, is reversible, and does not change authority. It still needs review, tests, and rollback.

### Questions that implementation must answer

1. Which exact artifact is deployed: source commit, wheel, container digest, manifest list, or another immutable package?
2. Which release or candidate record authorizes that artifact for the named environment?
3. Which routes and fields are enabled, and what evidence/policy/release dependencies do they require?
4. What happens when each dependency is missing, stale, denied, unavailable, or inconsistent?
5. Which external and internal edges are reachable, and which negative probes prove the exclusions?
6. How are credentials, keys, grants, and emergency revocations handled?
7. What evidence distinguishes configured state from applied state and observed state?
8. Who may deploy, verify, approve, roll back, and declare public exposure?
9. What correction or withdrawal propagates when a release or dependency is revoked?
10. What exact rollback restores the prior known-good artifact and configuration?

[↑ Back to top](#top)

---

## 12. Related docs

### Governing and adjacent documents

| Reference | Role | Current bounded status |
|---|---|---|
| [`README.md`](README.md) | Governed API architecture index and current scaffold boundary. | Repository-grounded; no live deployment claimed. |
| [`README.md`](README.md) | Governed API architecture landing page. | Human architecture; implementation claims require current evidence. |
| [`../deployment-topology.md`](../deployment-topology.md) | Repository-wide deployment readiness and topology distinctions. | Repository-grounded draft; current deployment unknown. |
| [`THREAT_MODEL.md`](THREAT_MODEL.md) | Threats and boundary risks for the Governed API. | Architecture input; enforcement requires implementation evidence. |
| [`AUDIENCE_CLASSES.md`](AUDIENCE_CLASSES.md) | Audience/caller vocabulary reconciliation. | Legacy audience enum and numeric tiers are not canonical or enforced. |
| [`ENVELOPES.md`](ENVELOPES.md) | Response-envelope architecture. | Does not itself prove current route integration. |
| [`ERROR_CODES.md`](ERROR_CODES.md) | Finite error/reason vocabulary planning. | Deployment failures must bind to accepted contracts before use. |
| [`LIFECYCLE_GATES.md`](LIFECYCLE_GATES.md) | Lifecycle and route exposure constraints. | Does not turn deployment into publication. |
| [`directory-rules.md`](../../doctrine/directory-rules.md) | Accepted placement law through ADR-0029. | Canonical writable Directory Rules authority. |
| [`infra/README.md`](../../../infra/README.md) | Deployment, host, network, exposure, and hardening root contract. | Bounded Compose checks/builds confirmed; live infra unestablished. |
| [`SECURITY.md`](../../../SECURITY.md) | Private-first security reporting and repository security posture. | Controls disclosure; not deployment proof. |
| [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) | Contribution, validation, generated-receipt, review, and rollback requirements. | Applies to this documentation change. |

### Direct implementation evidence

| Reference | What it can support |
|---|---|
| [`main.py`](../../../apps/governed-api/src/governed_api/main.py) | Current WSGI dispatcher and local serve defaults. |
| [`routes/registry.py`](../../../apps/governed-api/src/governed_api/routes/registry.py) | Exact current route registry. |
| [`stub.py`](../../../apps/governed-api/src/governed_api/stub.py) | Current finite negative scaffold behavior. |
| [`test_boundary_guards.py`](../../../apps/governed-api/tests/test_boundary_guards.py) | Route set, method rejection, safe errors, no internal-store path literals, and forbidden runtime imports. |
| [`Dockerfile.governed-api`](../../../infra/docker/Dockerfile.governed-api) | Current placeholder image contents and non-root boundary. |
| [`docker-compose.yml`](../../../infra/compose/docker-compose.yml) | Current placeholder service names, build contexts, and loopback ports. |
| [`test_compose_static.py`](../../../tests/infra/test_compose_static.py) | Exact static Compose assertions. |
| [`infra-compose-smoke.yml`](../../../.github/workflows/infra-compose-smoke.yml) | Hosted render/build orchestration that does not start services. |
| [`api-test.yml`](../../../.github/workflows/api-test.yml) | Governed API smoke and ABSTAIN route orchestration. |

[↑ Back to top](#top)

---

## 13. Appendix

<details>
<summary><strong>13.1 Current-state matrix</strong></summary>

| Control area | Repository evidence | Current conclusion |
|---|---|---|
| Application routes | Three registered `GET` routes. | **CONFIRMED, bounded** |
| Finite responses | Registered routes return `ABSTAIN / NOT_IMPLEMENTED`; safe `404`/`405` errors tested. | **CONFIRMED, bounded** |
| Internal-store literal guard | App source is checked for selected forbidden internal-store paths. | **CONFIRMED, bounded** |
| App packaging | No payload copy/install or startup command in placeholder image. | **UNKNOWN / HOLD** |
| Service port | Compose declares `8080`; local helper defaults to `8000`; no reconciliation profile. | **CONFLICTED / HOLD** |
| Container user | Final placeholder image user is non-root and statically tested. | **CONFIRMED, bounded** |
| Container start/health | Services are not started by the Compose workflow; no health check verified. | **UNKNOWN / HOLD** |
| Host exposure | Compose host mappings are loopback-only. | **CONFIRMED local placeholder only** |
| Public ingress | No observed or configured public edge verified. | **UNKNOWN / HOLD** |
| TLS | No current implementation evidence. | **UNKNOWN / HOLD** |
| CORS | No current implementation evidence. | **UNKNOWN / HOLD** |
| Authentication/authorization | No current implementation evidence in inspected app surfaces. | **UNKNOWN / HOLD** |
| Rate limits | No limiter or canonical numeric tier profile verified. | **UNKNOWN / HOLD** |
| Secrets | No secret values or secret-management system verified. | **UNKNOWN / HOLD** |
| Logs/metrics/traces | No governed operational subsystem verified. | **UNKNOWN / HOLD** |
| Egress/network policy | No applied rule set verified. | **UNKNOWN / HOLD** |
| Release binding | No deployable digest/release/environment record verified. | **UNKNOWN / HOLD** |
| Deployment/publication | No environment or release evidence inspected. | **UNKNOWN / HOLD** |

</details>

<details>
<summary><strong>13.2 Deployment-readiness checks</strong></summary>

These checks are not the KFM publication promotion gates and must not reuse their authority. They are deployment-readiness evidence labels for this document.

| Check | Question | Minimum closure |
|---|---|---|
| `D0 — identity` | Are exact source, package/image digest, config version, schema/policy versions, and environment named? | Immutable deployment record. |
| `D1 — package` | Does the image/package contain only intended payloads and a deterministic startup contract? | Build manifest, dependency lock, non-root check, content inspection. |
| `D2 — start` | Does it start, bind the intended interface/port, handle signals, and stop cleanly? | Startup/shutdown integration test. |
| `D3 — health` | Do liveness/readiness/degraded signals reflect the enabled capability safely? | Positive and failure-injection tests. |
| `D4 — edge` | Are ingress, TLS, proxy trust, CORS, auth, rate, and payload bounds enforced? | Config review plus final-edge positive/negative probes. |
| `D5 — membrane` | Are evidence, policy, release, correction, and internal-store boundaries preserved? | End-to-end governed response tests and denied-path tests. |
| `D6 — secrets/network` | Are secrets external, least-privilege, rotatable, and are ingress/egress edges bounded? | Scans, revocation test, reachability/SSRF negatives. |
| `D7 — observability` | Are logs, audit, metrics, traces, alerts, retention, and redaction safe? | Schema/redaction/cardinality/sink-failure tests. |
| `D8 — release/rollback` | Is the deployment bound to an approved candidate/release and tested rollback? | Release reference, correction path, rollback rehearsal. |
| `D9 — environment verification` | Does observed state match declared state after application? | Independent probes, drift record, reviewer checkpoint. |

A public exposure remains HOLD until the separate KFM release and publication controls appropriate to consequence are satisfied.

</details>

<details>
<summary><strong>13.3 Minimum deployment record</strong></summary>

A future machine-readable deployment record or equivalent should identify, without containing secrets:

- deployment/environment ID and purpose;
- source commit and immutable package/image digest;
- architecture/platform and build manifest;
- app, contract, schema, policy, configuration, and release versions;
- enabled route/capability/field profile;
- ingress hostname and transport profile reference;
- dependency and egress profile references;
- secret reference names and workload identity reference;
- deployed-at time and deployer identity;
- validation/probe references and finite conclusions;
- correction, withdrawal, and rollback target;
- prior known-good deployment identity;
- reviewer and verification state;
- public-exposure state as a separate field or linked decision.

The repository does not currently establish this object family at this path. Placement and schema decisions require current authority review before implementation.

</details>

<details>
<summary><strong>13.4 Repository-owned validation entrypoints</strong></summary>

Current repository files establish these bounded commands:

```bash
# Governed API scaffold and envelope behavior
make governed-api-smoke

python -m pytest \
  apps/governed-api/tests/test_abstain_routes.py \
  -q \
  --strict-config \
  --strict-markers

# Static Compose boundary
python -m unittest discover \
  --start-directory tests/infra \
  --pattern 'test_compose_static.py' \
  --verbose

# Placeholder render and image build; does not start services
docker compose -f infra/compose/docker-compose.yml config --quiet
docker compose -f infra/compose/docker-compose.yml build

# Documentation diff hygiene
git diff --check
```

These commands do not prove startup, health, ingress, external reachability, live secrets, applied network policy, environment state, release, deployment, or publication. A future runtime/deployment suite must add those checks without weakening the current negative boundaries.

</details>

<details>
<summary><strong>13.5 Truth-label legend</strong></summary>

- **CONFIRMED** — verified from pinned repository files, tests, workflows, accepted decisions, or other admissible evidence in the current work.
- **PROPOSED** — a design or requirement not verified as current implementation.
- **UNKNOWN** — not established strongly enough to act as fact.
- **NEEDS VERIFICATION** — checkable, but not yet checked strongly enough to act as fact.
- **HOLD** — operational posture used here when the evidence needed for a maturity or exposure claim is incomplete. It does not replace a core truth label.
- **CONFLICTED** — two current surfaces do not yet reconcile; the conflict is stated rather than silently normalized.

</details>

<details>
<summary><strong>13.6 Change history and rollback</strong></summary>

| Version | Date | Change |
|---|---|---|
| `v0.1` | 2026-05-24 | Proposal-era rules for TLS, CORS, legacy audience-based rate tiers, secrets, logs, network, health, and tracing. |
| `v0.2` | 2026-08-19 | Grounds the document in the current WSGI/Compose/Dockerfile/test/workflow evidence; removes unsupported implementation claims and numeric audience-tier authority; separates target requirements from current state; adds readiness, validation, release-binding, correction, and rollback HOLDs. |

**Rollback:** revert the documentation commit, restore target blob `977709a9f6cbac8bef8e433e0d4a0b2bf7d034aa`, remove or supersede the paired generated receipt according to repository receipt policy, and re-run the same documentation and receipt checks. No runtime, release, deployment, or publication rollback is created because this revision changes none of those states.

</details>

---

**Related (mini)** · [`README.md`](README.md) · [`../deployment-topology.md`](../deployment-topology.md) · [`THREAT_MODEL.md`](THREAT_MODEL.md) · [`AUDIENCE_CLASSES.md`](AUDIENCE_CLASSES.md) · [`ENVELOPES.md`](ENVELOPES.md) · [`ERROR_CODES.md`](ERROR_CODES.md) · [`LIFECYCLE_GATES.md`](LIFECYCLE_GATES.md) · [`infra/README.md`](../../../infra/README.md)

**Last updated:** 2026-08-19 · **Doc version:** v0.2 · **Doc status:** repository-grounded draft · **Current deployment:** UNKNOWN / HOLD

[↑ Back to top](#top)
