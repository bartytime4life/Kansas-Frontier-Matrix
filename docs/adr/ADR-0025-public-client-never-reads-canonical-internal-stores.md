<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0025-public-client-never-reads-canonical-internal-stores
title: ADR-0025 — Public Client Never Reads Canonical or Internal Stores
type: adr
adr_id: ADR-0025
version: v1.2
status: draft
effective_decision_status: proposed
owners:
  - "NEEDS VERIFICATION — architecture decision owner"
  - "NEEDS VERIFICATION — governed API and public-client steward"
  - "NEEDS VERIFICATION — security, policy, evidence, release, static-delivery, and operations stewards"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Governed API maintainer
  - Explorer Web or affected public-client maintainer
  - Security and infrastructure reviewer
  - Policy and sensitivity steward
  - Evidence and release steward
  - Static-delivery or hosting reviewer when released artifacts are exposed
  - At least one affected domain steward
created: 2026-05-09
updated: 2026-07-24
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2e4049bf511dcc5c4425a297458bf58627b58299
  target_prior_blob: 47762b9f6fc903c4a70b45de7c3030610082f695
  adr_index_blob: cf08fae322ac53426f7394d97897fdb942253049
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  adr_0004_blob: 11b86c462d474385befba0fb2115af9885f592af
  governed_api_readme_blob: 4f21150852f133ba919b11f4f8792185fa870dae
  governed_api_main_blob: bcc8d3a0ddba4b225e962b594d548819df0cbb71
  governed_api_routes_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  governed_api_stub_blob: 5d7c137d2e78ddfca35a1356a96333ac2e84952b
  governed_api_abstain_test_blob: 6474cef4f7378515ab673c288fc9daea19e388a9
  governed_api_boundary_test_blob: d84ccd2a93bdf786e8fca11ee596dcc47e543fc2
  boundary_constants_blob: 6c61f8e9160faa6d91b9c3e0cb6713dad153d9b5
  api_workflow_blob: 5ec0ff53cc874935ed8ef5de791b70a52635ef33
  runtime_response_contract_blob: b81d67dccdd8470e066ab8247eb93c5df67a6679
  runtime_response_schema_blob: 5105d419432a27176a8ee10870d75400cfa2ab8c
  runtime_response_validator_blob: 11ddc64c4299d103b0eef383c2f7bdd3bb12f1f9
  decision_envelope_schema_blob: 349782c8760f77e432ed1e9239d5ddc2ffe1f9b8
  explorer_readme_blob: 755dae3e175b103702caba573a5171d62ed710da
  explorer_src_readme_blob: 770cace029d0b9016ec7bd1c2d879b1bb49c896a
  explorer_package_blob: ce981192e725483c747affb45ca3de36a22ce9ce
  explorer_boundary_test_blob: 97d44069b0a5ab4a82b1e1fc48665e905c08a287
  ui_workflow_blob: a4fec64dc445b060d334c2ae56886cc814cb0e61
  reverse_proxy_readme_blob: fd061eb31ba9c71ca6815d76b46a26864bb0f91c
  published_readme_blob: 8ecb5d2f9737349fb6569efbde36659f398de151
  makefile_blob: 51537af34ee065c2de571134688415042b83b22a
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  apps_api_at_base: absent
inspection_boundary: >
  Current-session GitHub reads and bounded repository search covering the ADR inventory,
  Directory Rules, ADR-0004, this ADR, Governed API and Explorer Web documentation and
  implementation scaffolds, runtime envelope contracts and schemas, API and UI workflows,
  boundary tests, Makefile targets, published-data guidance, reverse-proxy guidance,
  CODEOWNERS, and the exact apps/api path. No complete repository tree clone, browser build,
  deployed client, reverse-proxy configuration, CORS/CSP policy, model-runtime network bind,
  static host, CDN, object store, production database, public origin, runtime log, release,
  correction, rollback, cache invalidation, penetration test, or production publication was
  exercised.
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md
  - docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md
  - docs/adr/ADR-0018-promotion-gate-sequence.md
  - docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md
  - docs/adr/ADR-0024-steward-separation-of-duties-for-release.md
  - docs/doctrine/directory-rules.md
  - apps/governed-api/README.md
  - apps/explorer-web/README.md
  - contracts/runtime/runtime_response_envelope.md
  - schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - apps/governed-api/tests/test_boundary_guards.py
  - tests/policy/test_explorer_web_adapter_boundary.py
  - data/published/README.md
  - infra/reverse_proxy/README.md
  - .github/workflows/api-test.yml
  - .github/workflows/ui-build.yml
  - Makefile
tags: [kfm, adr, public-client, trust-membrane, governed-api, explorer-web, static-delivery, internal-store, deny-by-default, evidence, release, correction, rollback]
notes:
  - "v1.2 is a same-path repository-grounded modernization. It preserves source metadata draft and effective decision status proposed; it does not accept ADR-0025 or prove deployed isolation."
  - "ADR-0004 selects the proposed dynamic trust membrane; ADR-0025 defines the proposed public-client information-flow and anti-bypass constraints around that boundary."
  - "The current Governed API is a three-route WSGI scaffold returning ABSTAIN / NOT_IMPLEMENTED; selected boundary tests exist, but the separate RuntimeResponseEnvelope is not integrated into those routes."
  - "Explorer Web remains implementation-held: package scripts are TODO, no lockfile is established by the UI workflow, and bounded evidence did not verify a non-empty browser implementation inventory."
  - "Static data under data/published is a released-carrier responsibility lane, not a public endpoint by path placement; serving and invalidation remain unverified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0025 — Public Client Never Reads Canonical or Internal Stores

> **Proposed decision.** An ordinary public client must never address, query, mount, fetch, import, proxy, or infer KFM canonical, candidate, evidence-internal, release-internal, model-runtime, administrative, or operational stores directly. Claim-bearing dynamic responses traverse the Governed API trust membrane. Released public-safe bytes may use a separately governed static-delivery edge, but only as immutable release-resolved carriers with enforceable integrity, sensitivity, correction, withdrawal, and rollback posture.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR ID: confirmed](https://img.shields.io/badge/ADR--0025-confirmed-0969da?style=flat-square)](#current-repository-evidence)
[![Governed API: scaffold](https://img.shields.io/badge/governed%20API-3%20ABSTAIN%20routes-f59e0b?style=flat-square)](#current-repository-evidence)
[![Explorer Web: held](https://img.shields.io/badge/explorer%20web-WORKFLOW__HOLD-b42318?style=flat-square)](#current-enforcement-maturity)
[![Static edge: unverified](https://img.shields.io/badge/static%20edge-NEEDS__VERIFICATION-6e7781?style=flat-square)](#current-enforcement-maturity)
[![Publication effect: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **Identity is confirmed; acceptance is not.** [`docs/adr/INDEX.md`](./INDEX.md) uniquely assigns `ADR-0025` to this exact file. Its source metadata is `draft`, which the index normalizes conservatively to effective status `proposed`. A README, test, route, workflow, pull request, merge, or deployed URL cannot accept the decision.

> [!CAUTION]
> **The current boundary is partial scaffolding.** The Governed API has three GET routes that return `ABSTAIN / NOT_IMPLEMENTED`; selected tests reject internal-store path literals and forbidden imports. Explorer Web still has TODO-only build/test scripts, and its workflow fails readiness until real scripts, an exact package-manager pin, and a lockfile exist. No current evidence proves browser, network, static-host, CDN, database, search, graph, or model-runtime isolation.

> [!WARNING]
> **Released placement is not public routing.** `data/published/` owns release-approved public-safe carrier bytes, but the repository path itself is not a public API, filesystem mount, bucket policy, CDN authorization, or release decision. Public exposure requires a governed dynamic projection or an approved static-delivery profile. `data/proofs/`, `data/receipts/`, `data/catalog/`, and `release/` remain internal authority/support stores even when selected public-safe summaries are projected outward.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Context](#context) · [Decision](#proposed-decision) · [Definitions](#definitions-and-store-classes) · [Dynamic](#dynamic-public-path) · [Static](#governed-static-delivery) · [Clients](#client-and-operator-boundaries) · [Authority](#authority-and-publication-boundary) · [Outcomes](#finite-outcomes-and-safe-failure) · [Anti-bypass](#anti-bypass-controls) · [Current evidence](#current-repository-evidence) · [Maturity](#current-enforcement-maturity) · [Validation](#proposed-validation-and-negative-tests) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Risks](#risk-and-open-question-ledger) · [Incident](#incident-correction-and-rollback) · [Rollback](#rollback-and-supersession) · [Checklist](#verification-checklist) · [References](#references) · [History](#revision-history)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0025` — unique and confirmed in [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md` |
| **Source metadata** | `draft` |
| **Effective decision status** | `proposed` |
| **Decision class** | Public-client information flow, trust membrane, static delivery, network exposure, evidence/release projection, and anti-bypass control |
| **Current repository posture** | Governed API fail-closed scaffold; selected structural tests; Explorer Web/UI and public edge held or unverified |
| **Implementation effect of this revision** | Documentation only |
| **Release/publication effect** | None |
| **Supersedes / superseded by** | None / none |
| **Relationship to ADR-0004** | ADR-0004 selects the proposed dynamic membrane; this ADR constrains all public-client paths around it |

### Acceptance versus implementation graduation

Two states remain separate:

1. **ADR acceptance** would approve the public-client store-isolation and static-edge model.
2. **Implementation graduation** would require a non-vacuous public-client inventory, accepted envelope contracts, client and server validation, policy, release resolution, network isolation, static-host controls, negative tests, observability, correction, rollback, and deployed verification.

An accepted ADR without enforcement is doctrine. Conversely, a green path-literal scan or scaffolded `ABSTAIN` route is bounded implementation evidence, not proof of a complete trust membrane.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This revision is grounded in repository bytes at `main@2e4049bf511dcc5c4425a297458bf58627b58299`.

| Evidence surface | CONFIRMED current state | What remains unproved |
|---|---|---|
| ADR inventory | ADR-0025 uniquely maps to this file; source `draft`; effective `proposed` | Acceptance |
| Directory Rules / ADR-0004 | Governed API is the proposed single dynamic trust boundary; no parallel `apps/api/` path at the checked ref | Runtime or deployed enforcement |
| Governed API app | WSGI scaffold; routes `/bootstrap`, `/layers`, `/evidence` | Auth, policy, evidence resolution, release binding, production routing |
| Route behavior | Every registered route returns `ABSTAIN`, `NOT_IMPLEMENTED`, empty evidence refs | Any evidence-backed `ANSWER` or client-facing envelope integration |
| API tests | Route manifest, 404/405, forbidden imports, internal-store path-literal checks | Indirect imports, environment-configured stores, outbound network paths, exfiltration |
| RuntimeResponseEnvelope | Draft contract, closed proposed schema, fixture validator | Governed API integration and accepted state vocabularies |
| Explorer Web | README/source-layout guidance plus TODO package scripts | Implemented browser routes, API client, fetch/import inventory, runtime tests |
| Explorer boundary test | Scans discovered JS/TS files for internal path literals and renderer imports | Non-empty browser source inventory and complete network/data-flow analysis |
| UI workflow | Intentionally fails readiness for placeholder scripts, missing exact package-manager pin, and absent lockfile | Build, tests, bundle contents, browser behavior |
| Reverse proxy | Detailed draft deny-by-default guidance | Concrete config, deployment, route map, TLS/CORS/CSP, public-origin behavior |
| Published data | Canonical released-carrier lane; public readiness deny by default; payloads/consumers/hosting unknown | Any approved static edge, release closure, cache invalidation |
| Public deny suite | Makefile `deny-test` is a TODO marker | Complete public-boundary policy/runtime proof |
| CODEOWNERS | One verified review route | Stewardship, independent review, branch protection, deployment approval |

### Truth labels

- **CONFIRMED** — verified from current repository bytes or governing doctrine.
- **PROPOSED** — candidate decision, interface, policy, path role, migration, or enforcement target.
- **HOLD** — a readiness surface intentionally refuses graduation.
- **NEEDS VERIFICATION** — a concrete check remains open.
- **UNKNOWN** — inspected evidence cannot support a stronger claim.
- **CONFLICTED** — current surfaces assign incompatible meaning, shape, or authority.

[Back to top](#top)

---

<a id="context"></a>

## Context

KFM's lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Trust accumulates through source admission, normalization, validation, evidence, policy, review, release, correction, and rollback. A public client that reaches around those controls can expose:

- unvalidated or stale source captures;
- unresolved rights or sensitivity;
- unpublished canonical records;
- internal identifiers, graph edges, search/vector indexes, or reconstruction clues;
- proof, receipt, review, or release internals stripped of their governing context;
- model prompts, provider endpoints, caches, or unreviewed generated language;
- withdrawn, superseded, or rollback-affected artifacts;
- administrative or debugging state.

The boundary must protect information flow, not merely directory names. A route is unsafe when it allows the public to obtain internal state even if no literal `data/raw` string appears in source. A static file is unsafe when its placement looks “published” but its release, digest, sensitivity, correction, and rollback posture cannot be verified.

### Relationship to ADR-0004

ADR-0004 proposes `apps/governed-api/` as the single dynamic trust membrane. ADR-0025 adds the complementary rule:

- public clients cannot directly address trust-bearing stores;
- public UI code cannot manufacture a second data plane;
- a static edge can serve released bytes without becoming a second policy or truth authority;
- role-gated operator access cannot become the ordinary public path;
- each bypass attempt produces a finite, auditable failure.

This ADR does not independently accept ADR-0004. Both records remain proposed.

[Back to top](#top)

---

<a id="proposed-decision"></a>

## Proposed decision

Upon acceptance and implementation graduation:

1. **Dynamic claim-bearing access** must traverse the accepted Governed API boundary and an accepted client-facing envelope.
2. **Public clients must not directly address** canonical, candidate, proof, receipt, registry, release-internal, model-runtime, admin, secret, database, graph, vector/search, cache, or source-system stores.
3. **Released static bytes may bypass the dynamic API only at the transport layer.** They still require release resolution, immutable identity, accepted integrity metadata, public-safety policy, correction/withdrawal/rollback posture, and a governed edge.
4. **No repository path is a public URL by implication.** Public routing is an independently reviewed deployment state.
5. **The renderer is not an authority.** Map tiles, layer properties, popups, screenshots, graphs, dashboards, search results, and generated summaries remain downstream carriers.
6. **The model runtime is private.** Public origins do not call model providers, local model servers, prompt stores, or adapter harnesses directly.
7. **Negative outcomes are first-class.** Missing evidence, release, policy, freshness, correction, or safe projection produces `ABSTAIN`, `DENY`, or `ERROR`, never silent bypass.
8. **Internal and steward surfaces remain separate.** Role-gated review/admin tools use least-privilege, audited service interfaces; arbitrary direct store access is not normalized as the public architecture.
9. **Corrections and withdrawals propagate through every public path.** Dynamic responses, static aliases, caches, indexes, and client state must converge on the governed release state.
10. **Static and dynamic public paths share one trust contract.** Neither path may strip evidence, policy, release, sensitivity, time, correction, or rollback context required for safe use.

`MUST`, `MUST NOT`, `SHOULD`, and `MAY` below describe the proposed accepted state, not current implementation fact.

[Back to top](#top)

---

<a id="definitions-and-store-classes"></a>

## Definitions and store classes

### Client classes

| Class | Meaning | Boundary |
|---|---|---|
| **Public client** | Browser, mobile app, public CLI, third-party consumer, public Focus/AI surface, or unauthenticated/untrusted origin | Governed dynamic API or governed static edge only |
| **Semi-public client** | Authenticated user surface without stewardship authority | Same membrane; policy may narrow output |
| **Steward/reviewer client** | Authenticated role-gated review surface | Audited governed service interfaces; not normal public path |
| **Operator/admin client** | Narrow operational control surface | Least privilege, private network/auth, immutable audit; no public exposure |
| **Automation/worker** | Pipeline, connector, watcher, CI, or service account | Cannot become a public client or release authority by convenience |
| **Redistributor** | Downstream organization or cache serving KFM-derived bytes | Must preserve release/integrity/correction context or clearly cease claiming governed KFM publication |

Client classification depends on authenticated authority and route posture, not application name alone.

### Store classes

| Store class | Examples | Direct public read |
|---|---|---:|
| Source/capture | `data/raw/`, connector caches, source credentials/endpoints | **DENY** |
| Working/candidate | `data/work/`, `data/quarantine/`, temporary exports, build scratch | **DENY** |
| Canonical pre-release | `data/processed/`, canonical domain records | **DENY** |
| Internal catalog/graph/registry | `data/catalog/`, `data/triplets/`, `data/registry/`, databases, graph/search/vector indexes | **DENY**; project safe projections |
| Evidence/process internals | `data/proofs/`, `data/receipts/`, review and audit stores | **DENY**; project bounded evidence summaries/refs |
| Release internals | decisions, manifests, signatures, correction, withdrawal, rollback records under `release/` | **DENY as store**; expose governed summaries or immutable public sidecars |
| Runtime/model internals | adapters, prompts, caches, provider endpoints, local model servers | **DENY** |
| Secrets/admin/observability | credentials, private logs, metrics with sensitive labels, debug state | **DENY** |
| Released carriers | approved artifacts under `data/published/` or external immutable storage | Conditional through governed static edge or API |
| Public envelope/projection | accepted client-facing response DTO/envelope | Conditional under policy/release/evidence constraints |

### Canonical does not mean public

A canonical record may be valid and still be unreleased, restricted, superseded, operationally sensitive, or too precise for public exposure. Canonicality answers where governed meaning/state lives; it does not answer who may read it.

[Back to top](#top)

---

<a id="dynamic-public-path"></a>

## Dynamic public path

The proposed dynamic path is:

```text
public/semi-public client
  -> public edge
  -> apps/governed-api/
  -> schema + identity + authorization
  -> policy + rights + sensitivity
  -> released or role-allowed projection
  -> evidence/citation resolution
  -> freshness + correction + rollback state
  -> RuntimeResponseEnvelope
  -> client rendering
```

### Dynamic obligations

A mature public route must:

- declare its route family, caller class, input schema, projection contract, and finite outcomes;
- authorize the caller before resolving protected data;
- read internal stores only through reviewed adapters/packages with least-privilege credentials;
- resolve released state or return a negative outcome;
- attach EvidenceRefs and require admissible EvidenceBundle support for claim-bearing `ANSWER`;
- preserve source role, spatial/temporal scope, rights, sensitivity, review, and correction obligations;
- avoid returning internal paths, database keys, prompt text, stack traces, credentials, protected precision, or private reasoning;
- emit an accepted client-facing envelope;
- record an audit-safe request/decision reference;
- make retries, caching, and pagination preserve the same policy and release boundary.

### Current envelope gap

The current routes emit a DecisionEnvelope-shaped scaffold. The separate `RuntimeResponseEnvelope` contract/schema defines the intended client-facing fields, but current route tests do not prove that integration. Acceptance requires one explicit, versioned relationship between policy decisions and client responses rather than two loosely overlapping envelope paths.

[Back to top](#top)

---

<a id="governed-static-delivery"></a>

## Governed static delivery

A static edge is allowed only for immutable released public-safe carriers such as PMTiles, COG, GeoParquet, public JSON projections, reports, stories, styles, sprites, glyphs, or downloadable exports.

### Required static-edge properties

| Control | Required posture |
|---|---|
| Release scope | Artifact resolves to an accountable release decision/manifest |
| Immutable identity | Versioned URI/object identity; no silent overwrite |
| Integrity | Accepted digest/signature/sidecar profile; exact profile depends on ADR-0023 and accepted standards |
| Public safety | Rights, sensitivity, redaction/generalization, field allowlist, and precision reviewed |
| Metadata | Content type, version, source/release refs, time/freshness, caveats |
| Correction | Withdrawal/supersession/rollback refs and client-visible state |
| Cache behavior | Immutable versioned objects; controlled aliases; purge/invalidation plan |
| CORS/range | Explicit origins/methods/headers/range behavior appropriate to the artifact |
| Access | No bucket/container listing or sibling internal-object exposure unless explicitly governed |
| Observability | Safe request/version/error telemetry without protected payload leakage |
| Failure | Missing or invalid release/integrity state fails closed |

A static edge is not a mirror of `data/published/` as a repository directory. It is a reviewed deployment projection of selected immutable objects. `data/published/` itself remains a lifecycle responsibility lane whose recursive payloads, writers, consumers, and hosting state are currently unverified.

### Alias rule

A mutable “current” or “latest” alias is a cache of release state, not authority. Alias updates require the accepted promotion/rollback/correction controls, atomic mutation where supported, cache invalidation, and post-change verification.

[Back to top](#top)

---

<a id="client-and-operator-boundaries"></a>

## Client and operator boundaries

### Explorer Web and other public UIs

Public UI code must not:

- import repository data files into the browser bundle;
- construct filesystem or object-store paths to internal lifecycle roots;
- call internal databases, graph/search/vector services, model providers, or debug endpoints;
- treat tile attributes, screenshots, popup text, renderer state, or cached search results as evidence;
- re-expand redacted/generalized fields;
- convert unknown, missing, malformed, or negative envelopes into an answer;
- hide stale, corrected, withdrawn, restricted, or release-held state.

### Governed AI / Focus clients

The client submits a bounded request to the Governed API. Server-side governed components retrieve evidence, apply policy, and invoke an approved model adapter only after scope and access checks. Raw model output is never a public protocol.

### Review/admin/operator surfaces

These surfaces are not public exceptions. They may perform broader actions only when:

- the user/actor is authenticated and currently authorized;
- the route is private or appropriately restricted;
- access is scoped to the task and subject;
- protected payloads are not cached into public storage;
- actions and reads are auditable;
- exports remain governed;
- the surface cannot be reached from the normal public origin;
- emergency access cannot self-authorize restoration or publication.

Direct database consoles, filesystem mounts, and ad hoc scripts are operational exceptions requiring separate governance, not the normal application contract.

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

The Governed API and static edge are projection and enforcement surfaces. They do not own:

- source truth;
- canonical lifecycle state;
- evidence or proof authorship;
- policy authorship;
- release authority;
- renderer truth;
- model truth;
- correction/rollback authority;
- deployment approval.

A public response can be validly shaped and still lack evidence or release authority. A released artifact can have a valid digest and still be unsafe, withdrawn, stale, or improperly exposed. A boundary check proves only its declared scope.

No route, package, CI pass, static file, CDN object, schema, signature, pull request, merge, or path placement creates `PUBLISHED` state by itself.

[Back to top](#top)

---

<a id="finite-outcomes-and-safe-failure"></a>

## Finite outcomes and safe failure

### Client-facing runtime outcomes

| Outcome | Meaning | Client behavior |
|---|---|---|
| `ANSWER` | Sufficient evidence, policy, release, freshness, correction, and projection support | Render bounded payload with required refs/limitations |
| `ABSTAIN` | Support is insufficient, unresolved, stale, conflicting, or unsafe to narrow | Explain bounded reason; do not infer missing content |
| `DENY` | Access, rights, sensitivity, release, capability, or route policy prohibits delivery | Do not render protected payload |
| `ERROR` | Validation, resolver, adapter, storage, network, or verifier failed | Show safe error; never treat failure as permission |

### Compliance-evaluator outcomes

A boundary validator or inventory report should use:

- `PASS` — all checks required by the selected boundary profile passed;
- `DENY` — a known prohibited public path or exposure exists;
- `HOLD` — inventory, deployment, ownership, release, or review evidence is incomplete;
- `ERROR` — the check could not determine the result safely.

`HOLD` and `ERROR` do not become `PASS` by timeout or administrator convenience.

### Safe error requirements

Public errors must not include:

- repository, filesystem, bucket, object-store, database, index, or model endpoint paths;
- query strings containing secrets or protected identifiers;
- stack traces or dependency versions that materially increase exposure risk;
- prompts, system instructions, hidden context, private reasoning, or raw provider responses;
- exact sensitive geometry or inference-enabling identifiers;
- internal hostnames, service-account names, credentials, or tokens.

[Back to top](#top)

---

<a id="anti-bypass-controls"></a>

## Anti-bypass controls

Defense in depth is required.

| Layer | Proposed control |
|---|---|
| Repository placement | Public deployables under `apps/`; internal lifecycle and release stores remain separate |
| Browser source | Non-vacuous import/fetch/URL/config scans; typed governed client only |
| Governed API | Route manifest, auth, policy, projection, evidence, release, envelope, safe errors |
| Shared packages | No package exports that hand public clients raw store handles or internal path construction |
| Network | Explicit ingress routes; internal/model/admin services private; deny wildcard upstream exposure |
| Static host | Allowlisted immutable released objects; no listing/sibling traversal; reviewed CORS/cache/range |
| CI | Negative fixtures and non-empty inventory assertions; generated bundles inspected |
| Deployment | Environment-specific route, origin, secret, and service-binding review |
| Runtime | Egress allowlists where appropriate; audit-safe logs; no direct public credentials |
| Client | Validate envelope and release metadata before render/use; preserve negative states |
| Operations | Correction, withdrawal, alias rollback, cache purge, and incident verification |

### Why literal scans are insufficient

Current tests reject configured path strings such as `data/raw`, `data/catalog`, `data/published`, and `release/`. That catches obvious drift but not:

- computed paths;
- environment variables and configuration injection;
- package indirection;
- generic filesystem/object-store clients;
- internal hostnames or DSNs;
- reverse-proxy aliases;
- generated browser assets;
- server-side request forgery;
- caches containing prior protected results;
- overly broad static bucket/container access;
- GraphQL/search/vector endpoints that expose equivalent internal state.

Literal scans remain useful as a fast negative guard, not as full information-flow proof.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Current verified state | Safe conclusion |
|---|---|---|
| ADR-0025 | Exact path; source `draft`; effective `proposed` | Decision not accepted |
| ADR-0004 | Repository-grounded proposed dynamic membrane decision | Dependency documented; not accepted |
| `apps/api/` | Exact `apps/api/README.md` path absent at pinned ref; bounded search surfaced no app path | No current parallel app established by inspected evidence |
| Governed API entry | Minimal WSGI dispatcher with registered GET routes, 404, 405 | Bounded executable scaffold |
| Route registry | Exactly `/bootstrap`, `/layers`, `/evidence` | Current route manifest only |
| Route outputs | `ABSTAIN`, `NOT_IMPLEMENTED`, empty evidence refs, zero placeholder hash | Fail-closed scaffold; no claim-bearing answer |
| Route tests | All registered routes structurally checked against DecisionEnvelope subset | Does not prove RuntimeResponseEnvelope integration |
| API boundary tests | 404/405, route set, renderer/model import, internal path-literal checks | Selected source boundaries only |
| Boundary constants | Include RAW, WORK, QUARANTINE, PROCESSED, CATALOG, PUBLISHED, and release path markers | Literal deny vocabulary, not complete flow policy |
| RuntimeResponseEnvelope | Draft contract, proposed closed schema, executable fixture validator | Shape evidence; route integration unproved |
| API workflow | Runs smoke and focused ABSTAIN tests with read-only permissions | Command-bearing CI; not deployment/release evidence |
| Explorer package | Version `0.0.0`; dev/build/test scripts echo `TODO` | No real UI build/test command |
| Explorer source docs | Candidate source map and explicit implementation uncertainty | Source architecture guidance only |
| Explorer boundary test | Scans discovered JS/TS files for renderer imports and store literals | Must assert non-empty inventory to avoid vacuous pass |
| UI workflow | Fails readiness on TODO scripts, missing lockfile, or unpinned package manager | Intentional implementation hold |
| Makefile | API and boundary targets execute; `deny-test` and `ui-build` are TODO markers | Partial tests, incomplete public deny suite |
| Reverse-proxy lane | Draft deny-by-default contract | No concrete edge config/deployment verified |
| Published lane | Canonical released-carrier responsibility; public readiness deny by default | No hosting or public consumer proof |
| CODEOWNERS | Relevant roots route to one account | Review routing only |

### Current violations

No direct Explorer Web or public route violation was confirmed from the inspected implementation because a substantive Explorer Web implementation was not verified. This is **not** proof of compliance. An empty or placeholder client cannot demonstrate safe public behavior.

[Back to top](#top)

---

<a id="current-enforcement-maturity"></a>

## Current enforcement maturity

| Capability | Current state |
|---|---|
| ADR identity/status | `CONFIRMED / proposed` |
| Governed API route scaffold | Implemented, fail-closed |
| Governed API auth/policy/evidence/release | Not established |
| RuntimeResponseEnvelope route integration | Partial / not established |
| API structural boundary tests | Implemented, bounded |
| Complete public deny suite | TODO marker |
| Explorer Web implementation | `WORKFLOW_HOLD` |
| Explorer non-vacuous fetch/import scan | Not established |
| Static edge profile | Proposed / unverified |
| Reverse-proxy configuration | Not verified |
| CORS/CSP/TLS/public-origin policy | Not verified |
| Model-runtime private bind | Not verified |
| Released payload/hosting inventory | Unknown |
| Public alias correction/rollback | Not established |
| Deployment and production traffic | Unknown |
| Observed public-store isolation | Not proved |

**Overall maturity: `SCAFFOLD / HOLD`.** The current repository demonstrates fail-closed route scaffolding and selected static source checks. It does not prove a deployed public trust membrane or static delivery edge.

[Back to top](#top)

---

<a id="proposed-validation-and-negative-tests"></a>

## Proposed validation and negative tests

### Inventory prerequisites

Before a scanner result can be cited as proof:

- the intended client/app source roots must exist;
- the inventory must contain an expected non-zero set of implementation files;
- ignored/generated/bundled artifacts relevant to deployment must be included;
- configuration and environment templates must be inspected;
- the tested revision and inventory digest must be recorded.

### Browser/client checks

At minimum, scan and test:

- static and dynamic imports;
- `fetch`, XHR, WebSocket, EventSource, workers, service workers, GraphQL clients, and SDK initialization;
- URL construction, environment variables, config files, generated manifests, and feature flags;
- internal filesystem/store markers, hostnames, DSNs, bucket/container names, graph/search/vector/model endpoints;
- source maps and bundle content for internal paths or secrets;
- direct model/provider calls;
- malformed/unknown/negative envelope handling;
- stale, corrected, withdrawn, restricted, and rollback-affected state;
- redaction/generalization preservation;
- static artifact release and integrity verification.

### Governed API checks

- route inventory is explicit and versioned;
- unknown routes and unsupported methods fail safely;
- authorization precedes protected resolution;
- no unreviewed store handle is exposed to public handlers;
- every `ANSWER` resolves evidence and release support;
- `ABSTAIN`, `DENY`, and `ERROR` leak no protected detail;
- DecisionEnvelope-to-RuntimeResponseEnvelope mapping is accepted and tested;
- internal dependencies are least privilege and environment scoped;
- outbound network access is allowlisted or reviewed where practical;
- audit records do not contain protected payloads.

### Static edge checks

- only allowlisted immutable released objects are reachable;
- no directory/container listing or sibling-object traversal;
- release manifest/digest/signature profile verifies;
- candidate, withdrawn, superseded, revoked, or restricted artifacts are denied;
- mutable alias points to approved immutable object;
- CORS, range, cache, content type, and security headers are correct;
- cache invalidation and correction propagation are exercised;
- origin/bucket credentials are not present in clients.

### Required negative fixtures

- browser code imports or fetches a lifecycle repository path;
- browser code obtains an internal URL through configuration;
- generic object-store client lists an internal container;
- public GraphQL/search/vector endpoint returns pre-release state;
- UI receives `DENY` but renders cached protected payload;
- UI receives unknown outcome and treats it as success;
- route returns `ANSWER` without evidence or release refs;
- error leaks stack trace, prompt, internal hostname, or exact sensitive geometry;
- static artifact has valid digest but no release approval;
- release-approved artifact has mismatched bytes;
- withdrawn artifact remains at public alias;
- service worker or CDN serves stale pre-correction bytes;
- model runtime is reachable from public origin;
- admin/review route is exposed publicly;
- scanner inventory is empty but test attempts to pass.

### Minimum reason-code families

- `public_path_internal_store`
- `public_path_candidate_or_unreleased`
- `public_path_proof_or_receipt_store`
- `public_path_release_internal`
- `public_path_model_runtime`
- `public_path_admin_or_debug`
- `client_inventory_empty`
- `client_boundary_scan_incomplete`
- `runtime_envelope_invalid`
- `evidence_unresolved`
- `release_unresolved`
- `artifact_integrity_missing_or_invalid`
- `artifact_withdrawn_or_superseded`
- `static_alias_mismatch`
- `cache_invalidation_unverified`
- `network_boundary_unverified`
- `protected_error_detail`
- `redaction_reexpanded`
- `deployment_inventory_missing`

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

Use small, reversible, dependency-ordered changes.

1. **Review/accept or revise ADR-0025** without inferring acceptance from code.
2. **Converge ADR-0004 and ADR-0025 terminology.** One owns dynamic membrane selection; one owns public-client anti-bypass.
3. **Resolve the client envelope integration.** Define the accepted relationship among DecisionEnvelope, PolicyDecision, and RuntimeResponseEnvelope.
4. **Make Explorer Web implementation-bearing.** Real package scripts, pinned package manager, lockfile, source inventory, tests, and governed client.
5. **Make boundary scans non-vacuous.** Assert expected source roots/file counts and include generated/deployment artifacts.
6. **Implement a complete public-boundary deny suite.** Replace the Makefile TODO with deterministic tests and stable reason codes.
7. **Implement governed API policy/evidence/release projection.** Keep routes fail closed until each dependency closes.
8. **Define the static-delivery profile.** Release resolution, integrity, immutable naming, CORS/range/cache, alias, correction, rollback.
9. **Implement and validate edge configuration.** Explicit public routes, private internal/model/admin upstreams, safe headers and origins.
10. **Inventory external stores and deployment bindings.** Databases, graph/search/vector, model runtime, object storage, caches, secrets.
11. **Add end-to-end negative tests.** Browser and external client attempts cannot reach forbidden stores or stale artifacts.
12. **Exercise correction and rollback.** Dynamic response, static alias, CDN, service worker, search/index, and client cache converge.
13. **Record evidence and graduate deliberately.** Replace holds only when current run/deployment evidence supports the claim.

### Documentation obligations

Behavior-changing work must update contracts, schemas, policy, fixtures, validators, app READMEs, infra/hosting docs, release/runbooks, correction/rollback guidance, and the ADR index when status or supersession changes.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

ADR acceptance requires reviewed agreement on the boundary and its dependencies:

- [ ] Architecture, Governed API, Explorer/public client, security/infra, policy/sensitivity, evidence/release, static-hosting, affected domain, and docs reviewers approve.
- [ ] ADR-0004 and ADR-0025 responsibilities are non-duplicative and coherent.
- [ ] Public client, semi-public client, steward, operator, automation, and redistributor classes are defined.
- [ ] Canonical/internal/released store classes and projection rules are accepted.
- [ ] Dynamic and static paths share evidence, policy, release, correction, and rollback obligations.
- [ ] `data/proofs/`, `data/receipts/`, `data/catalog/`, and `release/` are not treated as direct public stores.
- [ ] Static-delivery integrity/signature requirements defer to accepted profiles rather than unverified tooling.
- [ ] Admin/review access is not presented as an ordinary public bypass.
- [ ] Missing deployment or boundary evidence yields `HOLD`, not presumed compliance.
- [ ] No statement implies current production deployment or publication.

Implementation graduation additionally requires:

- [ ] non-placeholder Explorer build/test scripts and non-empty source inventory;
- [ ] accepted client-facing envelope integration;
- [ ] complete browser/API/static/network deny tests;
- [ ] real edge and runtime isolation evidence;
- [ ] released static fixture with correction/rollback behavior;
- [ ] current deployment route and origin inventory;
- [ ] no public model/admin/internal endpoint;
- [ ] observed correction/cache invalidation drill;
- [ ] accountable review and rollback target.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Prevents repository, database, graph, search, model, proof, receipt, and release internals from becoming public truth surfaces.
- Makes the public trust membrane testable across browser, API, edge, static host, and operations.
- Preserves evidence, policy, rights, sensitivity, release, correction, and rollback context.
- Keeps renderer and model outputs downstream of governed evidence.
- Allows efficient static map/data delivery without granting the static host policy or truth authority.
- Makes incomplete inventory and single-layer checks visible as `HOLD`.

### Costs

- Adds latency and implementation effort for envelope construction, evidence resolution, policy, release lookup, and validation.
- Requires explicit route, client, network, static-object, and deployment inventories.
- Requires careful cache and mutable-alias governance.
- Requires tests across application, package, infrastructure, deployment, and client layers.
- Restricts convenient direct access and ad hoc redistribution.
- May block public release while the small team lacks complete implementation or review capacity.

### Preserved invariants

- No canonical root or lifecycle phase changes.
- Promotion remains a governed state transition.
- Public interfaces do not replace evidence or release authority.
- Sensitive, rights-constrained, and living-person material remains fail closed.
- AI and renderers remain interpretive/downstream.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

| Alternative | Disposition |
|---|---|
| Documentation convention only | Rejected: cannot detect indirect or deployment bypass |
| Public read-only access to canonical stores | Rejected: canonical does not mean released or public-safe |
| Treat repository `data/published/` path as automatically public | Rejected: path placement does not supply hosting, release, integrity, or correction |
| Governed API for dynamic queries; ungoverned CDN for bytes | Rejected: static transport still needs the release trust contract |
| Per-domain public APIs | Rejected as default: multiplies trust boundaries; domain segmentation belongs behind one accepted membrane |
| Parallel `apps/api/` public surface | Rejected unless a future accepted ADR defines a non-competing boundary |
| Public model/provider calls with prompt constraints | Rejected: prompts are not policy, evidence, release, or network isolation |
| Browser-side filtering of restricted fields | Rejected: protected data must not reach the browser |
| Path-literal scanning as complete proof | Rejected: useful guard, incomplete information-flow analysis |
| Admin/review app as convenient public fast path | Rejected: privileged surfaces remain private, role-gated, audited |
| Disable boundary checks during incident | Rejected: reduce exposure or disable features; never open an internal bypass |

[Back to top](#top)

---

<a id="risk-and-open-question-ledger"></a>

## Risk and open-question ledger

| Item | Status | Required resolution |
|---|---|---|
| ADR-0004/ADR-0025 overlap | `NEEDS VERIFICATION` | Accepted responsibility split and cross-links |
| RuntimeResponseEnvelope integration | `CONFIRMED GAP` | Versioned mapping and route/client tests |
| Explorer implementation inventory | `HOLD` | Real source, scripts, lockfile, build/test results |
| Boundary scanner vacuity | `HOLD RISK` | Non-zero inventory and expected-file assertions |
| Complete public deny suite | `CONFIRMED GAP` | Replace TODO target with policy/runtime proof |
| `apps/api/` future reappearance | `OPEN` | Explicit internal/deprecated role or successor ADR |
| Internal database/graph/search/vector inventory | `UNKNOWN` | Deployment and service catalogue |
| Model runtime bind/egress | `UNKNOWN` | Network config and runtime tests |
| Reverse-proxy/ingress config | `UNKNOWN` | Concrete config and route verification |
| CORS/CSP/security headers | `UNKNOWN` | Environment-specific tests |
| Static delivery profile | `PROPOSED` | Accepted release/integrity/cache/CORS/range contract |
| Release manifest singular/plural paths | `CONFLICTED` | Separate accepted path decision |
| Published payload/consumer inventory | `UNKNOWN` | Pinned recursive/external object inventory |
| Mutable public aliases | `UNKNOWN` | Atomicity, release source, cache invalidation |
| Service worker/browser cache | `OPEN` | Versioning, correction, withdrawal, purge tests |
| Downstream redistribution | `OPEN` | License, provenance, correction propagation profile |
| Public evidence projection | `OPEN` | Safe EvidenceRef/summary fields without proof-store exposure |
| Performance budgets | `NEEDS VERIFICATION` | Real Kansas workload benchmarks after correctness |
| Observability leakage | `OPEN` | Safe logging/metrics schema and tests |
| Historical public bypasses | `UNKNOWN` | Route, deployment, CDN, and client history audit |
| Ownership and independent review | `NEEDS VERIFICATION` | Steward assignments and branch/deployment controls |

Unknowns narrow public capability. They do not authorize plausible defaults.

[Back to top](#top)

---

<a id="incident-correction-and-rollback"></a>

## Incident, correction, and rollback

### When a bypass is discovered

1. reduce exposure immediately: disable route, alias, object, origin, credential, or feature;
2. preserve relevant logs/config/artifact identities without exposing protected payload;
3. classify affected stores, clients, data classes, time range, and public claims;
4. rotate credentials or signer material where implicated;
5. issue correction, withdrawal, or incident notices as required;
6. invalidate CDN, service-worker, browser, search, vector, and API caches;
7. verify no alternate route or alias remains;
8. restore only through the normal governed release/review path;
9. record post-incident evidence and rollback target.

Emergency containment may be single-operator when delay increases harm, but it may only reduce exposure. The same operator cannot self-authorize restoration or broader release where ADR-0024 requires independent review.

### Rollout failure

When new membrane enforcement breaks a public feature:

- disable or narrow the feature;
- preserve `DENY`/`HOLD` rather than opening a canonical-store bypass;
- use the last verified immutable release where available;
- disclose degraded/stale/correction state;
- restore after policy, tests, release references, and review are valid.

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation-only rollback

Restore prior ADR blob:

```text
47762b9f6fc903c4a70b45de7c3030610082f695
```

A transparent revert restores prior proposed documentation only. It does not change routes, network posture, stores, clients, release state, or publication.

### If this ADR is later accepted

A material relaxation or new public trust boundary requires:

- a successor ADR;
- reciprocal supersession links;
- an updated ADR index;
- migration and compatibility plans for clients, APIs, static edges, stores, schemas, policy, tests, deployment, correction, and rollback;
- an audit of releases and consumers relying on the prior rule.

Do not flip an accepted record back to `proposed`, delete audit history, or create a temporary raw/internal bypass as “rollback.”

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification checklist

### Current revision

- [x] ADR ID, filename, H1, and index row verified.
- [x] Source `draft` and effective `proposed` status preserved.
- [x] Directory Rules and ADR-0004 reviewed.
- [x] Governed API routes, scaffold behavior, tests, workflow, and envelopes inspected.
- [x] Explorer Web docs, package placeholder, boundary test, and UI readiness workflow inspected.
- [x] Published-lane and reverse-proxy guidance inspected.
- [x] Dynamic versus static public paths separated.
- [x] Proof, receipt, catalog, registry, and release stores removed from direct public classification.
- [x] Literal scans bounded as partial, potentially vacuous evidence.
- [x] No deployment, release, isolation, or publication claim introduced.
- [ ] Human review completed.
- [ ] ADR accepted.
- [ ] Implementation graduated.
- [ ] Production public isolation observed.

### Future implementation

- [ ] Governed API uses accepted RuntimeResponseEnvelope for public responses.
- [ ] Explorer Web has a non-empty implementation and typed governed client.
- [ ] Browser scans include source, config, bundles, workers, and generated assets.
- [ ] Complete API deny suite replaces the TODO marker.
- [ ] Policy/evidence/release projection is enforced before `ANSWER`.
- [ ] Reverse proxy/ingress exposes only governed public routes and selected released objects.
- [ ] Model, admin, debug, canonical, and internal stores are private.
- [ ] Static artifacts verify release, integrity, correction, and rollback.
- [ ] Cache/alias correction and withdrawal drill passes.
- [ ] External redistributors receive or preserve the required trust contract.
- [ ] Current deployment and public-origin tests pass.

[Back to top](#top)

---

<a id="references"></a>

## References

| Reference | Relationship and current boundary |
|---|---|
| [`docs/adr/README.md`](./README.md) | ADR operating contract; merge does not accept a decision |
| [`docs/adr/INDEX.md`](./INDEX.md) | Confirms ADR-0025 identity, source `draft`, effective `proposed` |
| [ADR-0004](./ADR-0004-apps-governed-api-is-the-trust-membrane.md) | Proposed single dynamic trust-membrane selection and current scaffold evidence |
| [ADR-0005](./ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md) | Proposed public map-first shell |
| [ADR-0008](./ADR-0008-ollama-subordinate-to-governed-api.md) | Model runtime remains behind governed API |
| [ADR-0010](./ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | Sensitive-domain fail-closed posture |
| [ADR-0011](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | Keeps evidence support, receipts, catalog, release, and publication distinct |
| [ADR-0015](./ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) | Mutable published alias and rollback dependencies |
| [ADR-0018](./ADR-0018-promotion-gate-sequence.md) | Promotion/release gate sequence and current holds |
| [ADR-0019](./ADR-0019-ai-adapter-contract-and-finite-envelopes.md) | Governed AI adapter/envelope boundary |
| [ADR-0020](./ADR-0020-abstain-is-a-first-class-decision.md) | Missing support produces bounded abstention |
| [ADR-0023](./ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md) | Proposed static geo-artifact integrity binding |
| [ADR-0024](./ADR-0024-steward-separation-of-duties-for-release.md) | Independent review for public release and restoration |
| [Directory Rules](../doctrine/directory-rules.md) | Responsibility roots, trust membrane, lifecycle, migration discipline |
| [Governed API README](../../apps/governed-api/README.md) | Draft app boundary and candidate route families |
| [Explorer Web README](../../apps/explorer-web/README.md) | Draft public UI boundary and direct-read prohibition |
| [RuntimeResponseEnvelope contract](../../contracts/runtime/runtime_response_envelope.md) | Draft client-facing semantic contract |
| [RuntimeResponseEnvelope schema](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | Proposed closed machine shape |
| [API boundary tests](../../apps/governed-api/tests/test_boundary_guards.py) | Selected route/import/path-literal checks |
| [Explorer boundary test](../../tests/policy/test_explorer_web_adapter_boundary.py) | Selected renderer/path-literal scan; non-vacuity unresolved |
| [Published lane](../../data/published/README.md) | Released-carrier responsibility; public serving unverified |
| [Reverse proxy guidance](../../infra/reverse_proxy/README.md) | Draft edge contract; no deployment proof |
| [API workflow](../../.github/workflows/api-test.yml) | Command-bearing scaffold checks |
| [UI workflow](../../.github/workflows/ui-build.yml) | Intentional Explorer implementation hold |
| [Makefile](../../Makefile) | Partial boundary targets and TODO public deny/UI markers |

[Back to top](#top)

---

<a id="revision-history"></a>

## Revision history

| Version | Date | Summary |
|---|---|---|
| v1 | 2026-05-09 | Initial proposed ADR codifying the no-direct-public-read trust-membrane invariant. |
| v1.1 | 2026-05-15 | Clarified static delivery, finite outcomes, deny tests, migration, rollback, and attachment-only evidence boundary. |
| v1.2 | 2026-07-24 | Re-grounded the ADR in current repository evidence; confirmed ADR identity, three-route fail-closed Governed API scaffold, selected boundary tests, separate RuntimeResponseEnvelope contract/schema, Explorer/UI implementation hold, published-lane and reverse-proxy uncertainty; separated dynamic API from governed static transport; removed proof/receipt/release stores from direct public classification; bounded path scans as partial and potentially vacuous; added client/store classes, deployment controls, negative tests, convergence, acceptance, incident, cache, correction, rollback, and successor-ADR discipline. |

---

<sub>This ADR is governed by KFM doctrine: public clients use governed projections, released carriers are not sovereign truth, missing support fails closed, and no renderer, model, store path, or transport edge may bypass evidence, policy, release, correction, and rollback.</sub>
