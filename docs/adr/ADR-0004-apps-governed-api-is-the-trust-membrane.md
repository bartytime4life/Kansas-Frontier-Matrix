<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0004-apps-governed-api-trust-membrane
title: "ADR-0004 — `apps/governed-api/` is the Trust Membrane"
type: adr
adr_id: ADR-0004
version: v1.4
status: draft
owners:
  - "NEEDS VERIFICATION — architecture decision owner"
  - "NEEDS VERIFICATION — governed API owner"
  - "NEEDS VERIFICATION — security and policy owner"
reviewers_required:
  - Docs steward
  - Architecture steward
  - Governed API maintainer
  - Security / policy reviewer
  - Evidence / release reviewer
  - "at least one affected client or subsystem owner"
created: 2026-05-10
updated: 2026-09-12
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility: record the proposed governed API trust-membrane decision, its verified implementation boundary, acceptance holds, and rollback posture without granting runtime, release, or publication authority
responsibility_root: docs/
current_path: docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 49deb7558cf36f0f14b51643efff30ea631c681e
  base_tree: c2cc9e260ce837a591803184e37d0e55a04309db
  target_prior_blob: afe430ac64a60007f29589324dec60f1f9b34c4f
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  adr_index_blob: 0c143676dfd3c1bda16cb44398c5ad5d4a49cf67
  apps_readme_blob: 95b3b021cad9bcafbd53fd1ddd18f6b51df22d80
  apps_root_lane_count: 8
  governed_api_tree_entries: 42
  governed_api_blob_count: 30
  governed_api_directory_count: 12
  governed_api_readme_blob: 5154fccf675f421c03a2245d58e31febd600de8b
  governed_api_main_blob: 4eb335c7c0b27f62c7419c478542e8fe40e1ff38
  governed_api_routes_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  governed_api_stub_blob: 1870c401a49fb4c7b53ab123e6a80770690bce51
  governed_api_route_test_blob: 2be20f5d93c03da7677c34b11a31875a00b2ed28
  governed_api_failure_test_blob: 8ca054fc89abed1ee13af6b21958d9896dec85ee
  governed_api_failure_fixture_blob: 294725cd2e345888daccece519b4c2be645079ef
  governed_api_boundary_test_blob: 4035e537e6c52194928df5ab8ceb41a35f5f30ca
  api_workflow_blob: 84ba16a3c36a1d58b2f6f1059a31ed6354063357
  policy_boundary_workflow_blob: 1d7ba1df0f8ed291a15b1d9a44e404ba95d9e35c
  makefile_blob: 670471891242e97d9e40415f94f5980c42645c7d
  runtime_response_schema_blob: 8b86e7db8b18b65a56a4e639dfc54e1b2db93155
  decision_envelope_schema_blob: 349782c8760f77e432ed1e9239d5ddc2ffe1f9b8
  runtime_response_contract_blob: 9dfc286984b5b52b383753fe6215a2b31df8c876
  precision_actually_used_contract_blob: 0a8e43ce3c3a08f253ac720572c866c21b54dd7f
  decision_envelope_contract_blob: b7e33c1351c9c28c5cfb3fc107d87204b3fdf455
  runtime_response_validator_blob: 44ce7d51038a9adf9fcbdb18108cc27da8381e33
  runtime_response_contract_alignment_test_blob: 746486ddc4e356d9dc28c7c46481c067f43ad23d
  schema_validation_workflow_blob: fb6dea20bc03bb2ddac134b9dbebbcf044d4e246
  explorer_package_blob: e3ef41da15915d23fb8872a7ba881d66cf892093
  explorer_governed_client_blob: dce12a2bc152c059a60168f89a43d82483a9cf14
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  apps_api_at_base: absent
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - docs/adr/ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md
  - docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md
  - docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/trust-membrane.md
  - docs/architecture/governed-api/README.md
  - apps/README.md
  - apps/governed-api/README.md
  - apps/explorer-web/src/adapters/GovernedClient.ts
  - control_plane/root_registry.yaml
  - contracts/runtime/decision_envelope.md
  - contracts/runtime/runtime_response_envelope.md
  - contracts/runtime/precision_actually_used.md
  - schemas/contracts/v1/runtime/decision_envelope.schema.json
  - schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - .github/workflows/api-test.yml
  - .github/workflows/policy-boundary-guards.yml
  - .github/workflows/schema-validation.yml
tags: [kfm, adr, governance, governed-api, trust-membrane, runtime-envelope, finite-outcomes, evidence, policy, release, no-parallel-api]
notes:
  - "v1.4 is a same-path current-state reconciliation; it does not accept the decision or change executable behavior."
  - "ADR-0004 identity and tracked path are confirmed by docs/adr/INDEX.md; source metadata remains draft and effective decision status remains proposed."
  - "The three registered routes are a bounded WSGI scaffold: GET returns RuntimeResponseEnvelope-shaped ABSTAIN / NOT_IMPLEMENTED; unknown routes and unsupported methods return safe RuntimeResponseEnvelope-shaped ERROR."
  - "The route test asserts the exact required RuntimeResponseEnvelope field set and schema subset. That resolves the older decision-envelope-shaped-scaffold claim without establishing evidence, policy, release, or substantive ANSWER behavior."
  - "Fixture-only failure builders deterministically exercise ABSTAIN, DENY, and ERROR cases, including safe correlation handling. They are not live endpoints, policy evaluation, or production failure handling."
  - "RuntimeResponseEnvelope v0.4 documents the conditional precision rule, and a repository-owned contract/schema alignment test verifies field coverage. This is shape/meaning alignment, not runtime authority."
  - "Explorer Web is buildable and test-bearing, but its GovernedClient is fixture-only and performs no network or lifecycle-store access; no live governed-api integration is inferred."
  - "Workflow definitions are inspected as wiring only. Current CI conclusions belong to exact-head run records and are not asserted here."
  - "A governed static-delivery edge for already released public-safe artifacts may complement the dynamic API, but it cannot become a second trust authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0004 — `apps/governed-api/` is the Trust Membrane

> **Proposed decision.** KFM will use **`apps/governed-api/`** as the single dynamic public trust boundary for claim-bearing and trust-bearing responses. Ordinary clients will not read lifecycle, canonical, candidate, evidence-internal, model-runtime, graph, search, or release-internal stores directly. A separately governed static-delivery edge may serve already released public-safe artifacts, but it is not a second API, policy engine, or truth authority.

| At a glance | Current posture |
|---|---|
| Decision | **DRAFT source / effectively PROPOSED** |
| Configured app | `apps/governed-api/` present |
| Executable dynamic routes | Three deterministic `ABSTAIN / NOT_IMPLEMENTED` RuntimeResponseEnvelope scaffolds; safe `ERROR` routing responses |
| Public response integration | **CONFIRMED for the registered scaffold** — full RuntimeResponseEnvelope required field set; **HOLD** for substantive evidence/policy/release mapping |
| Current client | Buildable/test-bearing fixture-first Explorer; no live API transport proved |
| Publisher | **No** |
| Evidence snapshot | `main@49deb7558cf36f0f14b51643efff30ea631c681e` |

> [!IMPORTANT]
> **Repository configuration is not reviewed decision authority.** The repository already contains `apps/governed-api/`, three bounded routes, schemas, contracts, fixtures, validators, tests, and CI wiring. The canonical ADR index still records ADR-0004 as effectively `proposed`. This revision documents the current boundary without changing the ADR to `accepted`.

> [!CAUTION]
> **Fail-closed scaffolding is not a complete trust membrane.** The registered routes emit schema-tested `RuntimeResponseEnvelope`-shaped `ABSTAIN / NOT_IMPLEMENTED` holds, and routing failures emit safe `ERROR` envelopes. They do not resolve evidence, evaluate an accepted policy bundle, authorize a caller, bind a release, or prove deployed isolation. No route may graduate to substantive `ANSWER` merely because the WSGI app, schema validator, fixture, or smoke test is green.

<a id="quick-navigation"></a>

**Quick navigation:** [Status](#1-status) · [Context](#2-context) · [Decision](#3-decision) · [Diagram](#4-trust-membrane--diagram) · [Invariants](#5-operational-invariants) · [Envelope contract](#6-runtimeresponseenvelope-contract) · [Negative outcomes](#7-required-deny-cases) · [Surfaces](#8-affected-paths) · [`apps/api/`](#9-resolution-of-the-appsapi-question) · [Consequences](#10-consequences) · [Alternatives](#11-alternatives-considered) · [Migration](#12-migration--backward-compatibility) · [Validation](#13-validation--compliance) · [Related](#14-related-adrs-and-docs) · [Open work](#15-open-questions--needs-verification) · [Reason codes](#appendix-a--reason-code-vocabulary) · [Anti-patterns](#appendix-b--anti-patterns-this-adr-forbids)

---

## 1. Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0004` — unique and confirmed in the canonical [`INDEX.md`](./INDEX.md) |
| **Source metadata** | `draft` |
| **Effective decision status** | `proposed` — not binding as an accepted ADR until the record and index carry matching reviewed `accepted` status |
| **Decision class** | Public trust-boundary selection, no-parallel-public-API rule, dynamic response-envelope requirement, and public-client store isolation |
| **Tracked path** | `docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md` |
| **Current configured app** | [`apps/governed-api/`](../../apps/governed-api/) |
| **Current plural/parallel app state** | Exact `apps/api/` path absent at the pinned snapshot |
| **Current implementation posture** | Bounded executable WSGI scaffold: three GET routes return RuntimeResponseEnvelope-shaped `ABSTAIN / NOT_IMPLEMENTED`; unknown routes and unsupported methods return safe `ERROR` envelopes; fixture-only negative cases cover additional finite outcomes |
| **Current client posture** | Explorer Web builds and tests fixture-first projections; its `GovernedClient` is no-network and does not prove live Governed API integration |
| **Decision dependencies** | Evidence, policy, release/correction, finite-outcome contracts, client integration, static-delivery governance, security, observability, and rollback |
| **Publication effect** | None. This ADR, a route, schema, test, workflow, commit, pull request, or merge is not a release or publication decision. |

### 1.1 Current repository evidence snapshot

The following findings are **CONFIRMED at `main@49deb7558cf36f0f14b51643efff30ea631c681e`** unless marked otherwise. Workflow definitions are evidence of wiring only; a workflow conclusion must be tied to its exact run and tested commit.

| Surface | Verified state | What it proves—and does not prove |
|---|---|---|
| [`docs/adr/INDEX.md`](./INDEX.md) | ADR-0004 is the unique tracked record for this decision; effective status is `proposed`; source metadata is `draft`. | Proves identity and conservative status normalization; does not accept the decision. |
| [Directory Rules](../doctrine/directory-rules.md) and [ADR-0029](./ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted ADR-0029 adopts the exact Directory Rules bytes. They place deployables under `apps/`, name `apps/governed-api/` as the main public trust path, and prohibit `apps/api/` from becoming parallel authority. | Proves accepted placement authority and intended app roles; does not accept ADR-0004 or prove runtime enforcement. |
| [`root.apps`](../../control_plane/root_registry.yaml) | Active canonical machine projection classifies `apps/` as the mixed-exposure deployable-application root and prohibits data instances, release decisions, and schemas. | Confirms the projection of adopted placement; the registry is not independent decision authority. |
| [`apps/README.md`](../../apps/README.md) and current tree | Eight direct app lanes are present. `apps/governed-api/` has 42 recursively listed entries: 30 blobs and 12 directories including the app root. Direct reads confirm the WSGI entry point, route registry, envelope builder, three executable test modules, and test support modules. | Proves bounded repository structure; not deployment, auth, policy, or release maturity. |
| [`apps/governed-api/README.md`](../../apps/governed-api/README.md) | The v0.3 draft describes the bounded WSGI scaffold, three `ABSTAIN` routes, safe routing errors, fixture-only negative outcomes, and no live source/policy/release service. | Orientation consistent with direct source evidence; neither the README nor code proves production behavior. |
| [`main.py`](../../apps/governed-api/src/governed_api/main.py) | Small WSGI app dispatches registered GET routes, returns `405` for unsupported methods on registered paths, and `404` for unknown paths using safe `ERROR` envelopes. | Proves bounded dispatch behavior; not authentication, authorization, evidence resolution, policy evaluation, or network isolation. |
| [`routes/registry.py`](../../apps/governed-api/src/governed_api/routes/registry.py) | Exactly three routes are registered: `/bootstrap`, `/layers`, and `/evidence`. | Proves current surface manifest; not full endpoint catalogue or versioned public API. |
| [`stub.py`](../../apps/governed-api/src/governed_api/stub.py) | Live `ABSTAIN` and routing `ERROR` builders emit the ten RuntimeResponseEnvelope required fields. The fixture-only builder also expresses deterministic `ABSTAIN`, `DENY`, and `ERROR` cases without registering routes. | Proves fail-closed shape construction and fixture behavior; not evidence-backed answers, policy evaluation, accepted digests, or release-bound responses. |
| [`test_abstain_routes.py`](../../apps/governed-api/tests/test_abstain_routes.py) | Iterates every registered route, fixes time, expects `200 OK` / `ABSTAIN` / `NOT_IMPLEMENTED`, requires exactly the RuntimeResponseEnvelope required keys, forbids decision and precision fields, and validates the schema subset. | Proves the current live scaffold's bounded negative RuntimeResponseEnvelope posture; not substantive route semantics. |
| [`test_api_failure_fixtures.py`](../../apps/governed-api/tests/test_api_failure_fixtures.py) and [fixture cases](../../apps/governed-api/tests/fixtures/api_failure_cases.json) | Nine deterministic fixture cases cover malformed input, unsupported scope, missing evidence, policy denial, stale/unavailable dependencies, timeout, cancellation, and internal defect. Tests preserve distinct `ABSTAIN`/`DENY`/`ERROR` outcomes and reject unsafe correlation reflection. | Proves fixture-only negative-shape behavior; no live endpoint, policy evaluator, dependency, or audit system is implied. |
| [`test_boundary_guards.py`](../../apps/governed-api/tests/test_boundary_guards.py) | Checks schema-shaped `404`/`405` errors, forbidden renderer/model imports, exact three-route manifest, and absence of hard-coded internal-store literals in app source. | Proves selected structural boundaries; not complete information-flow, auth, policy, deployment, or exfiltration proof. |
| [`Makefile`](../../Makefile) | Provides `governed-api-dev`, `governed-api-smoke`, `governed-api-verify`, `boundary-guards`, `boundary-guards-ci`, and `deny-test`. The last target runs only the app-local boundary module; it is not a complete public-denial matrix. | Proves command-bearing bounded checks and a deliberately narrow deny surface, not full trust-membrane enforcement. |
| [`api-test.yml`](../../.github/workflows/api-test.yml) | Hash-locked dependency installation, immutable action pins, read-only checkout, an all-app-test smoke job, a focused route-test job, and non-authoritative summaries are wired. | Proves CI definition, not the state of a current run, release approval, deployment, auth, policy, evidence closure, or public behavior. |
| [`RuntimeResponseEnvelope` schema](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | Proposed client-facing shape requires the ten base fields and conditionally requires `precision_actually_used` plus nonempty evidence for `ANSWER`; non-`ANSWER` outcomes must omit the precision object. | Proves current machine shape and precision-disclosure constraints; not accepted meaning or evidence/policy/release integration. |
| [`DecisionEnvelope` schema](../../schemas/contracts/v1/runtime/decision_envelope.schema.json) | Separate proposed decision schema requires decision identity, outcome, policy family, reasons, obligations, and evaluation time. | Proves a distinct machine-shape proposal; it is not the live scaffold's public response object. |
| [`RuntimeResponseEnvelope` contract](../../contracts/runtime/runtime_response_envelope.md) and [alignment test](../../tests/contracts/test_runtime_response_contract_alignment.py) | v0.4 documents the `ANSWER` precision/evidence condition and the non-`ANSWER` prohibition. The repository-owned test requires the contract and precision profile to cover schema fields and both conditional rules. | Confirms current contract/schema field alignment; not a runtime answer, policy decision, release decision, or publication authority. |
| [runtime validator](../../tools/validators/validate_runtime_response_envelope.py) and [`schema-validation.yml`](../../.github/workflows/schema-validation.yml) | The dedicated validator loads the response schema and applies bounded precision semantics. The workflow configures both runtime families among nine aggregate validator fixture lanes plus schema/contract tests. | Proves local validation and CI wiring boundaries only; a green result would still not prove runtime mapping, policy, evidence, release, or publication. |
| [`apps/explorer-web/package.json`](../../apps/explorer-web/package.json) and [`GovernedClient.ts`](../../apps/explorer-web/src/adapters/GovernedClient.ts) | Vite build plus test scripts are present. `GovernedClient` validates a fixture-only Evidence Drawer projection and explicitly performs no network or lifecycle-store access. | Proves a buildable/test-bearing fixture client boundary; no live Governed API transport or RuntimeResponseEnvelope consumption. |
| Exact `apps/api/` path | Recursive exact-head tree contains zero matching entries. | Proves no parallel app exists at this snapshot; not a permanent guarantee. |
| [`CODEOWNERS`](../../.github/CODEOWNERS) | Routes `/docs/adr/`, `/apps/governed-api/`, schemas, policy, release, tests, and validators to `@bartytime4life`. | Proves GitHub review routing; not stewardship assignment, independent approval, or acceptance. |
| Production exposure, auth, audit sink, dashboards, service health, rate limits, and network isolation | **UNKNOWN / NEEDS VERIFICATION** | No admissible operational evidence was inspected. |

### 1.2 Safe current conclusion

The repository has a **real but intentionally narrow fail-closed API scaffold**. It is stronger than documentation-only intent and weaker than an accepted, production-capable trust membrane.

The safe claim is:

> `apps/governed-api/` currently demonstrates route registration, RuntimeResponseEnvelope-shaped `ABSTAIN` and routing `ERROR` behavior, fixture-only finite negative outcomes, and selected import/path boundaries. Explorer demonstrates a buildable fixture-first consumer boundary, not live transport. Evidence resolution, accepted policy evaluation, release binding, authentication, authorization, observability, deployed isolation, and substantive `ANSWER` behavior remain unproved. The former contract/schema precision-prose drift is resolved at the current contract and alignment-test boundary; it does not close the remaining implementation gates.

[Back to top](#top)

---

## 2. Context

KFM's governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move. Public trust must therefore be enforced at the point where released state becomes a response, map payload, export, story, review projection, or AI-assisted explanation.

### 2.1 Why a dedicated dynamic membrane is required

Without one accountable dynamic boundary:

- public clients can accidentally become readers of canonical or lifecycle stores;
- evidence resolution, source role, policy, rights, sensitivity, freshness, release, correction, and rollback checks fragment by client or route;
- generated language can be rendered before evidence and citation closure;
- `ABSTAIN`, `DENY`, and `ERROR` can be hidden as empty or partial success;
- review, CLI, admin, and worker conveniences can harden into unreviewed public paths;
- two public API deployables can evolve different denial vocabularies and audit trails;
- a renderer, graph, search index, object store, or model runtime can become a de facto source of truth.

### 2.2 Dynamic API and governed static delivery are different concerns

This ADR governs the **dynamic trust boundary**. It does not require every immutable public-safe byte to be proxied through the WSGI process.

| Surface | Allowed posture | Trust requirement |
|---|---|---|
| Dynamic claim-bearing or trust-bearing request | `apps/governed-api/` | Finite response envelope, policy/evidence/release checks, safe errors, auditability |
| Static PMTiles, COG, GeoParquet, report, story, JSON sidecar, or other released artifact | Governed static-delivery edge MAY serve it | Release manifest, digest/integrity metadata, public-safe classification, correction/rollback references, no hidden internal path |
| Canonical, candidate, internal, model-runtime, graph, search, source, or lifecycle store | Direct public read is forbidden | Governed projection or explicit denial |
| Review/admin/operator request | Governed and role-gated route | Authentication, authorization, audit, no self-approval, no direct browser file mutation |

A static edge is a delivery mechanism, not a second policy substrate or public API authority. The membrane is operational: the artifact must already be released and verifiable.

### 2.3 Relationship to adjacent decisions

This ADR answers **where dynamic public trust is enforced**. Adjacent proposed ADRs answer narrower questions:

- ADR-0005 identifies Explorer Web as the map-first client.
- ADR-0008 and ADR-0019 place model runtimes and adapters behind the API.
- ADR-0010 establishes deny-by-default sensitive-domain posture.
- ADR-0020 makes abstention first-class.
- ADR-0025 forbids public clients from reading canonical/internal stores and permits a governed static edge for released artifacts.

All remain proposed; this ADR does not grant them accepted status.

[Back to top](#top)

---

## 3. Decision

**If accepted, KFM adopts the following rules.**

### 3.1 Dynamic trust-boundary rule

1. **Single dynamic public membrane.** `apps/governed-api/` is the sole normal dynamic boundary for public and semi-public trust-bearing responses.
2. **Ordinary clients use governed interfaces.** Explorer Web, external API consumers, Evidence Drawer, Focus Mode, Story/Compare/Export surfaces, and role-gated review retrieval do not read internal stores or model providers directly.
3. **Finite client-facing envelope.** Every dynamic trust-bearing public response is represented by a `RuntimeResponseEnvelope` with exactly one outcome: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
4. **Decision objects stay distinct.** A `DecisionEnvelope` or `PolicyDecision` may feed the public response, but neither silently substitutes for the client-facing `RuntimeResponseEnvelope`.
5. **Evidence before answer.** Claim-bearing `ANSWER` responses require resolvable evidence support and citations appropriate to the claim. Missing or inadequate support yields `ABSTAIN`, `DENY`, or `ERROR`.
6. **Policy before exposure.** Rights, sensitivity, source terms, caller role, release state, freshness, correction, withdrawal, and rollback posture are evaluated before the response is exposed.
7. **Released state only.** Dynamic public reads project released public-safe state and governed proof/release metadata. They do not expose RAW, WORK, QUARANTINE, PROCESSED, candidate, registry-internal, receipt-internal, graph-internal, search-internal, or direct source-system records.
8. **No direct model client.** Browsers and ordinary clients do not call Ollama, OpenAI-compatible services, local model runtimes, embedding/vector services, or model caches directly.
9. **No direct renderer authority.** MapLibre, tiles, scenes, screenshots, popups, and client feature state are downstream carriers. They do not authorize release or substitute for evidence.
10. **Review/admin/operator boundaries remain governed.** Role-gated clients may have broader projections or submit actions, but they remain audited, policy-bound, separation-of-duties aware, and outside the normal public path.
11. **Workers remain non-publishers.** Workers, connectors, and pipelines produce candidates, receipts, validation outputs, and release inputs; they do not speak directly to ordinary public clients or approve publication.
12. **App boundary is non-sovereign.** `apps/governed-api/` applies contracts, schemas, policy, evidence, and release state from their owning roots; it does not redefine or own those authorities.

### 3.2 Governed static-delivery rule

A static edge MAY serve a released public-safe artifact without proxying all bytes through `apps/governed-api/` when all of the following are true:

- a governed release record identifies the artifact;
- integrity metadata identifies the exact bytes or representation;
- public-safe rights and sensitivity posture are resolved;
- release, correction, withdrawal, supersession, and rollback state are available;
- client or edge behavior does not infer trust from location alone;
- no canonical, candidate, internal, protected, or direct model/source path is exposed;
- the edge cannot mint dynamic decisions or bypass policy.

### 3.3 Authority and publication boundary

`apps/governed-api/`:

- **does own** app-local route dispatch, request handling, response construction, app-local guards, app-local tests, and deployable composition;
- **does not own** object meaning, machine shape, policy source, evidence, canonical lifecycle state, release approval, correction approval, rollback authority, source admission, shared reusable libraries, deployment secrets, or publication state.

A successful response, test, deployment, or uptime check does not promote data or authorize release.

### 3.4 Current scaffold rule

Until the acceptance gates in §13.2 are closed:

- the three registered routes SHOULD remain fail-closed;
- a route MAY return a schema-valid `ABSTAIN`/`NOT_IMPLEMENTED` hold;
- no route may return a substantive `ANSWER` merely because a fixture, subset assertion, or smoke test passes;
- replacing the scaffold with a real handler requires contract/schema mapping, negative tests, and rollback in the same bounded change.

> [!IMPORTANT]
> The safest current implementation is the one the repository already uses: explicit `ABSTAIN` rather than invented or weakly supported success. This ADR treats that behavior as a valid hold state, not as feature completion.

[Back to top](#top)

---

## 4. Trust Membrane — Diagram

```mermaid
flowchart LR
    subgraph Current["CONFIRMED current scaffold"]
        REG["3 registered GET routes<br/>/bootstrap · /layers · /evidence"]
        STUB["RuntimeResponseEnvelope-shaped scaffold<br/>ABSTAIN · NOT_IMPLEMENTED"]
        ERRORS["RuntimeResponseEnvelope-shaped routing errors<br/>404 / 405 · ERROR"]
        TESTS["route + fixture + boundary tests"]
        REG --> STUB --> TESTS
        REG --> ERRORS --> TESTS
    end

    subgraph Target["PROPOSED accepted dynamic trust path"]
        CLIENTS["Explorer Web · external clients<br/>Evidence Drawer · Focus · review"]
        API["apps/governed-api<br/>request + policy + evidence + release"]
        DECISION["DecisionEnvelope / PolicyDecision<br/>internal decision posture"]
        RESPONSE["RuntimeResponseEnvelope<br/>ANSWER · ABSTAIN · DENY · ERROR"]
        CLIENTS --> API
        API --> DECISION
        DECISION --> RESPONSE
        RESPONSE --> CLIENTS
    end

    subgraph Governed["Governed supporting authorities"]
        POLICY["policy/"]
        EVIDENCE["EvidenceRef -> EvidenceBundle"]
        RELEASE["ReleaseManifest · correction · rollback"]
        PUBLISHED["released public-safe artifacts"]
        RUNTIME["runtime adapters"]
    end

    subgraph Denied["Not a direct public path"]
        INTERNAL["RAW · WORK · QUARANTINE · PROCESSED<br/>registries · receipts · graph/search internals<br/>source systems · model providers"]
    end

    POLICY --> API
    EVIDENCE --> API
    RELEASE --> API
    PUBLISHED --> API
    RUNTIME --> API
    CLIENTS -. "DENY direct access" .-> INTERNAL

    STATIC["Governed static-delivery edge<br/>released + digest-bound only"]
    PUBLISHED --> STATIC --> CLIENTS
```

> [!NOTE]
> The current and target lanes are intentionally separate. Existing route, fixture, and boundary tests prove a schema-shaped fail-closed hold and limited negative handling. They do not prove the complete target flow. The static edge carries released bytes; it does not emit dynamic policy or evidence decisions.

[Back to top](#top)

---

## 5. Operational Invariants

| ID | Invariant | Current evidence posture |
|---|---|---|
| **I-1** | `apps/governed-api/` is the only normal dynamic public trust-bearing API. | Directory Rules + repository path CONFIRMED; ADR acceptance proposed |
| **I-2** | Dynamic client-facing trust responses use `RuntimeResponseEnvelope` with exactly `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. | Contract/schema present and proposed; the current three live scaffolds and routing errors use the required field shape, while substantive route semantics remain held |
| **I-3** | `DecisionEnvelope` remains a distinct internal/runtime decision object and is not treated as the public response object without an explicit accepted mapping. | Two contracts/schemas CONFIRMED distinct; no registered route currently substitutes a DecisionEnvelope for its public response |
| **I-4** | Public clients do not read lifecycle, candidate, canonical, receipt-internal, proof-internal, registry-internal, graph, search, source, or model-runtime stores directly. | Doctrine + selected static tests CONFIRMED; complete flow proof absent |
| **I-5** | Claim-bearing `ANSWER` requires resolvable evidence support and validated citations appropriate to the claim. | Doctrine/contract present; no current `ANSWER` route |
| **I-6** | Rights, sensitivity, caller role, source terms, release, freshness, correction, withdrawal, and rollback posture are enforced before exposure. | Intended contract present; accepted evaluator/integration unproved |
| **I-7** | `ABSTAIN`, `DENY`, and `ERROR` are first-class governed outcomes, not hidden exceptions or empty success. | Live route `ABSTAIN` and routing `ERROR` behavior plus fixture-only `ABSTAIN`/`DENY`/`ERROR` cases CONFIRMED; no policy execution inferred |
| **I-8** | `ERROR` responses do not expose prompts, credentials, private endpoints, stack traces, internal file paths, restricted detail, or hidden reasoning. | Safe routing shape and unsafe-correlation fixture assertion CONFIRMED; representative public error-path coverage remains incomplete |
| **I-9** | Model adapters and providers remain behind the membrane; browser/provider direct traffic is forbidden. | Import guard exists; network/deployment isolation unproved |
| **I-10** | Static delivery is allowed only for already released public-safe, integrity-bound artifacts with correction/rollback visibility. | Adjacent ADR/doctrine proposal; static edge implementation unproved |
| **I-11** | Review, admin, and operator paths are role-gated, audited, and cannot approve their own policy-significant release effects. | Doctrine; current review/admin surfaces are scaffolded or unproved |
| **I-12** | Workers, connectors, and pipelines are non-publishers and cannot become alternate public APIs. | Repository static tests CONFIRMED; complete runtime proof absent |
| **I-13** | The app consumes contracts, schemas, policy, evidence, and release state; it does not redefine their authority. | Responsibility-root documentation and current structure CONFIRMED |
| **I-14** | Every substantive route change has deterministic negative cases and a reversible rollback or forward-fix path. | Required acceptance posture; current routes remain scaffolds |
| **I-15** | A green workflow, commit, PR, route, static edge, or deployed process does not make content KFM-published. | KFM core invariant |

[Back to top](#top)

---

## 6. `RuntimeResponseEnvelope` Contract

The public response and internal decision surfaces are related but not interchangeable.

### 6.1 Current scaffold shape

The current live scaffold emits a `RuntimeResponseEnvelope`-shaped hold object. For `/layers`, the effective shape is:

```json
{
  "id": "stub:layers",
  "spec_hash": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "version": "v1-stub",
  "issued_at": "<time>",
  "outcome": "ABSTAIN",
  "reason_code": "NOT_IMPLEMENTED",
  "evidence_refs": [],
  "policy_state": "baseline",
  "freshness": "current",
  "correction_state": "none"
}
```

The current route test checks the exact top-level required-field set and validates this object against `runtime_response_envelope.schema.json` through `assert_jsonschema_subset`. Because the outcome is not `ANSWER`, it correctly omits `precision_actually_used`. Unknown-route and unsupported-method responses use the same runtime-envelope field family with safe `ERROR` state.

This is a bounded hold object. It is not evidence closure, policy evaluation, release binding, or a substantive client claim.

### 6.2 `DecisionEnvelope` vs `RuntimeResponseEnvelope`

| Concern | `DecisionEnvelope` | `RuntimeResponseEnvelope` |
|---|---|---|
| Primary role | Records finite runtime decision posture, policy family, reasons, obligations, and evaluation time | Carries client-facing finite response posture, evidence refs, policy state, freshness, and correction state |
| Required identity | `decision_id` | `id` |
| Required finite field | `outcome` | `outcome` |
| Required policy context | `policy_family` | `policy_state` |
| Required explanation | `reasons`, `obligations` | `reason_code`; state fields |
| Required time | `evaluated_at` | `issued_at` |
| Evidence shape | Optional array of strings | Required array of EvidenceRef objects |
| Freshness/correction | Not required | `freshness` and `correction_state` required |
| Precision disclosure | Not defined | `precision_actually_used` required for `ANSWER` and forbidden otherwise by current schema |
| Current app use | No registered route emits it as the public response | Every registered hold route and routing error uses this required field family |
| Authority status | Contract/schema present; proposed | Contract/schema present; proposed |

### 6.3 Confirmed scaffold integration and remaining gap

The prior snapshot described a material response-shape gap. At the pinned revision, that statement is no longer correct:

- `make_abstain_envelope()` and `make_error_envelope()` construct the runtime response's ten required fields;
- `test_abstain_routes.py` asserts the exact schema-required key set, no decision-only fields, no non-`ANSWER` precision object, and the response-schema subset for every registered route;
- `test_boundary_guards.py` applies the same runtime-envelope checks to safe `404` and `405` responses;
- `test_api_failure_fixtures.py` validates deterministic fixture-only `ABSTAIN`, `DENY`, and `ERROR` shapes, including a non-reflection assertion for unsafe correlation input; and
- the v0.4 RuntimeResponseEnvelope contract and `test_runtime_response_contract_alignment.py` now cover the schema's precision condition.

The remaining gap is semantic and operational, not a current scaffold field mismatch. There is no implemented evidence resolver, accepted policy evaluator, release/correction join, caller authorization, or substantive `ANSWER` path from which an internal `DecisionEnvelope` or `PolicyDecision` must be mapped. The fixture `policy_denial` case is only a deterministic translation profile; it is not a policy decision.

This is not a reason to weaken either schema or collapse object families. It is an acceptance blocker for a substantive route, while the current fail-closed runtime-envelope scaffold is an accurate bounded implementation claim.

### 6.4 Required mapping before substantive `ANSWER`

Before any route graduates from scaffolded `ABSTAIN` to substantive `ANSWER`, the implementation MUST establish and test this relationship:

```text
request context
  -> authorization + policy + evidence + release/freshness/correction evaluation
  -> DecisionEnvelope and/or PolicyDecision
  -> endpoint payload projection
  -> RuntimeResponseEnvelope
  -> client
```

The accepted mapping must answer:

- which decision fields are preserved, transformed, or referenced;
- how obligations reach the client without leaking protected policy detail;
- how EvidenceRef objects are resolved and represented;
- how supported spatial, temporal, and attribute precision is computed, bound to top-level evidence, and linked to transform receipts;
- how release, freshness, correction, withdrawal, and rollback state are encoded;
- how endpoint-specific payloads are represented without reopening `additionalProperties`;
- how `ANSWER` differs from non-claim bootstrap/config responses;
- how schema versions and compatibility are negotiated; and
- how invalid or unmapped internal decisions fail closed.

### 6.5 Minimum client-facing semantics

The current RuntimeResponseEnvelope schema confirms these required fields:

| Field | Current machine-shape role |
|---|---|
| `id` | Response identity |
| `spec_hash` | SHA-256 contract/spec lineage hook |
| `version` | Envelope version |
| `issued_at` | Emission time |
| `outcome` | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` |
| `reason_code` | Safe primary reason |
| `evidence_refs` | EvidenceRef objects |
| `policy_state` | Policy-state summary |
| `freshness` | Freshness/staleness posture |
| `correction_state` | Correction/withdrawal/supersession posture |
| `precision_actually_used` | Conditionally required `ANSWER` disclosure for supported spatial, temporal, and attribute precision, evidence refs, and transform-receipt refs; forbidden for non-`ANSWER` outcomes |

The schema closes additional properties. For `ANSWER`, top-level `evidence_refs` must be nonempty and the precision object's evidence refs must be a subset of them; the validator also applies bounded temporal and transform-disclosure semantics. Endpoint payload representation therefore needs an explicit contract decision; it must not be smuggled in through undocumented fields.

> [!WARNING]
> A route that returns only a `DecisionEnvelope` or adds arbitrary payload fields would violate the public response boundary. The current holds avoid that error by emitting the schema-tested RuntimeResponseEnvelope field family; future substantive routes must retain it.

[Back to top](#top)

---

## 7. Required Deny Cases

This heading retains the original anchor, but the table distinguishes `DENY`, `ABSTAIN`, `ERROR`, and transport responses accurately.

### 7.1 Minimum negative behavior

| Trigger | Required outcome | Current coverage |
|---|---|---|
| Unknown route | `404 Not Found` with a safe RuntimeResponseEnvelope-shaped `ERROR` body | **CONFIRMED** |
| Unsupported method on a registered route | `405 Method Not Allowed` with a safe RuntimeResponseEnvelope-shaped `ERROR` body | **CONFIRMED** |
| Registered route not implemented | Schema-bounded `ABSTAIN / NOT_IMPLEMENTED` RuntimeResponseEnvelope hold | **CONFIRMED for all three registered routes** |
| Fixture malformed input, unavailable dependency, timeout, or internal defect | Deterministic safe `ERROR` shape and reason code | **CONFIRMED fixture-only** |
| Fixture unsupported scope, missing evidence, stale dependency, or cancellation | Deterministic `ABSTAIN` shape and reason code | **CONFIRMED fixture-only** |
| Fixture policy denial | Deterministic `DENY / POLICY_DENIED` shape | **CONFIRMED fixture-only; not an evaluated policy decision** |
| Governed API imports renderer or direct model client | Test/build failure | **CONFIRMED bounded import guard** |
| API or Explorer source hard-codes internal lifecycle/store paths | Test/build failure | **CONFIRMED bounded literal scan** |
| Public request targets RAW, WORK, QUARANTINE, PROCESSED, candidate, registry-internal, receipt-internal, graph/search internal, direct source, or model provider | `DENY` with safe reason; never accidental filesystem error | **PROPOSED / not fully implemented** |
| Evidence cannot resolve or citations cannot validate | `ABSTAIN` | **PROPOSED beyond fixture translation** |
| Rights, sensitivity, source terms, caller role, release state, or embargo blocks exposure | `DENY` or reviewed restricted projection | **PROPOSED / policy integration unproved** |
| Source is stale beyond endpoint policy | `ABSTAIN` or stale-safe bounded response according to accepted contract | **PROPOSED beyond fixture translation** |
| Adapter, resolver, schema, policy, or dependency fails | `ERROR` with safe audit reference and no internal leakage | **PROPOSED beyond fixture translation** |
| Exact protected archaeology, rare-species, living-person, DNA/genomic, cultural, or critical-infrastructure detail requested | `DENY` or approved transformed/restricted projection | **PROPOSED / domain policy required** |
| Unreleased layer or artifact requested | `DENY` | **PROPOSED / release integration unproved** |
| Model candidate or generated text is presented as observation/evidence | `DENY` or `ABSTAIN` | **PROPOSED** |
| Browser attempts direct model/provider call | Build/test/network denial | **Static import posture partly confirmed; deployed network denial unproved** |
| Review/admin/CLI request attempts direct file mutation or self-approval | `DENY` plus audit-safe record | **PROPOSED** |
| Static edge serves missing-digest, withdrawn, corrected-without-lineage, or non-public-safe artifact | Edge/client verification failure; do not render as trusted | **PROPOSED** |
| Empty or unsupported payload is labeled `ANSWER` | Schema/semantic test failure | **PROPOSED** |

### 7.2 Current bounded tests are necessary but insufficient

The current checks establish schema-shaped route/method errors, route holds, fixture-negative shape behavior, import, route-manifest, and path-literal boundaries. They do not prove:

- identity or authentication;
- role/capability authorization;
- accepted policy bundle execution;
- evidence resolution or citation validation;
- release/correction/rollback integration;
- response confidentiality or timing behavior;
- dependency egress or provider isolation;
- logging/redaction;
- static-edge integrity verification;
- deployment, ingress, CORS, CSP, rate-limit, or cache policy; or
- complete deny/abstain/error coverage.

`make deny-test` remains intentionally narrower than the all-app-test smoke suite: it runs the app-local boundary module, not the fixture-negative module and not a complete public policy, evidence, rights, sensitivity, release, or exfiltration matrix.

[Back to top](#top)

---

## 8. Affected Paths

This documentation change modifies only this ADR. The surfaces below are the verified implementation and authority neighborhood affected by eventual acceptance.

### 8.1 Current verified surfaces

| Surface | Current role | Current status | Decision impact |
|---|---|---|---|
| [`apps/governed-api/`](../../apps/governed-api/) | Dynamic trust-membrane deployable | Minimal executable RuntimeResponseEnvelope scaffold | Canonical dynamic app if ADR is accepted |
| [`apps/governed-api/src/governed_api/main.py`](../../apps/governed-api/src/governed_api/main.py) | WSGI dispatch | Executable bounded behavior | Preserve safe `404`/`405` runtime envelopes and add accepted middleware/route composition incrementally |
| [`routes/registry.py`](../../apps/governed-api/src/governed_api/routes/registry.py) | Route manifest | Three routes | Route additions require contract/policy/evidence/negative-test closure |
| [`stub.py`](../../apps/governed-api/src/governed_api/stub.py) | Fail-closed envelope builders | Live `ABSTAIN/NOT_IMPLEMENTED` and routing `ERROR` plus fixture-only negative translations | Safe rollback baseline; not a production evidence/policy/release implementation |
| [`apps/governed-api/tests/`](../../apps/governed-api/tests/) | App-local route, failure-fixture, and boundary proof | Three executable test modules plus support modules | Expand without replacing cross-root tests |
| [`apps/explorer-web/`](../../apps/explorer-web/) | Normal public-client candidate | Buildable/test-bearing fixture-first shell; `GovernedClient` performs no network access | Live governed transport and RuntimeResponseEnvelope consumption remain unproved |
| [`apps/review-console/`](../../apps/review-console/) | Role-gated review client | Documentation/scaffold maturity | Must not read or mutate receipt/report/diff files directly |
| [`contracts/runtime/`](../../contracts/runtime/) | Decision and response meaning | Separate proposed contracts; runtime response v0.4 has current precision-condition prose | Preserve distinct object meanings and define substantive-route mapping |
| [`schemas/contracts/v1/runtime/`](../../schemas/contracts/v1/runtime/) | Machine shape | Both schemas present, proposed | Preserve closed shapes; version deliberate changes |
| [`fixtures/contracts/v1/runtime/`](../../fixtures/contracts/v1/runtime/) | Positive/negative schema examples | Aggregate runtime fixture lanes configured | Expand outcome, evidence, additional-property, and state cases as routes gain semantics |
| [`tools/validators/validate_runtime_response_envelope.py`](../../tools/validators/validate_runtime_response_envelope.py) | Dedicated RuntimeResponseEnvelope validator | Schema plus bounded precision semantics | Shape validation only; never substitute for policy/evidence/runtime proof |
| [`policy/runtime/`](../../policy/runtime/) | Runtime admissibility | Policy root exists; accepted evaluator/bundle unproved | Required before substantive trust decisions |
| [`packages/evidence-resolver/`](../../packages/evidence-resolver/) | Shared evidence resolution boundary | Maturity NEEDS VERIFICATION | Required for claim-bearing `ANSWER` |
| [`runtime/`](../../runtime/) | Adapters behind API | Maturity NEEDS VERIFICATION | Provider/model details must not cross public boundary |
| [`release/`](../../release/) | Release, correction, withdrawal, rollback authority | Separate root present | API consumes state; does not approve it |
| [`api-test.yml`](../../.github/workflows/api-test.yml) | Bounded CI orchestration | Command-bearing; all-app smoke plus focused route job | Keep read-only; expand representative checks deliberately |
| [`schema-validation.yml`](../../.github/workflows/schema-validation.yml) | Shape/fixture CI | Both runtime families configured among nine aggregate validators | Does not prove mapping or runtime behavior |
| [`docs/architecture/governed-api/README.md`](../architecture/governed-api/README.md) | Current architecture landing page | Repository-grounded explanatory boundary; implementation claims still require current evidence | Navigation correction only; this ADR's decision status is unchanged |
| `apps/api/` | Potential parallel API | Absent at snapshot | No migration required now; future creation is governed by Section 9 |

### 8.2 Required implementation packet for the first substantive route

The smallest sound implementation packet SHOULD include:

- one route family and one bounded public-safe use case;
- explicit request and response contracts;
- an internal-decision-to-RuntimeResponseEnvelope mapping where the route uses a `DecisionEnvelope` or `PolicyDecision`;
- valid and invalid fixtures for both internal decision and public response;
- no-network evidence/resolver fixture or mock;
- policy allow/deny/abstain/error cases;
- release/freshness/correction fixture state;
- app-local and cross-root negative tests;
- safe logging and audit reference behavior;
- client or static-edge integration test as applicable;
- rollback to the `ABSTAIN/NOT_IMPLEMENTED` handler; and
- docs updated to match verified behavior.

Do not implement all route families in one broad PR.

[Back to top](#top)

---

## 9. Resolution of the `apps/api/` Question

The exact `apps/api/` path is absent at the pinned snapshot. No current migration or deprecation record is required solely for a path that is not present.

If `apps/api/` is introduced or discovered later:

| Condition | Required disposition |
|---|---|
| It serves dynamic public trust traffic | **DENY architecture change** unless a new accepted ADR replaces this decision |
| It is a frozen legacy path | Declare `legacy`, identify canonical replacement, forbid new public routes, and track retirement |
| It is a generated mirror or external export | Declare class and deterministic source; it cannot execute independent policy or decisions |
| It is internal-only | Document exact caller, network boundary, auth, data access, and why it is not a parallel public membrane |
| It is a narrowly scoped service | Prove that it does not mint public trust outcomes, bypass the Governed API, or become a second denial/audit surface |
| It is only a static artifact host | Treat it as governed static delivery, not an API authority; use a name and contract that do not imply parallel dynamic policy |
| Hyphen/underscore naming differs | Do not create both `governed-api` and `governed_api`; use a reviewed migration if renaming is necessary |

> [!WARNING]
> Route-prefix separation is not architectural separation. Two public deployables that each decide evidence, policy, release, or denial posture create two membranes, even when they use different URL prefixes.

[Back to top](#top)

---

## 10. Consequences

### 10.1 Positive

- **One accountable dynamic boundary.** Evidence, policy, release, freshness, correction, and safe-error behavior converge in one deployable.
- **Current fail-closed work is preserved.** The existing `ABSTAIN/NOT_IMPLEMENTED` scaffold remains a valid hold and rollback baseline.
- **Object-family boundaries become visible.** Internal decisions and client-facing responses remain distinct rather than being renamed into one another.
- **Cite-or-abstain becomes operational.** Missing support is a typed outcome, not an empty success.
- **Client and model paths remain subordinate.** Explorer Web, review surfaces, static delivery, and model adapters cannot silently become truth or policy authority.
- **Static delivery stays efficient without weakening governance.** Already released public-safe bytes may use a verified edge without creating a parallel dynamic API.
- **Review and rollback become testable.** A substantive route can be introduced as a small packet with a known fail-closed fallback.

### 10.2 Costs and tradeoffs

- **More explicit contracts.** A substantive route that uses an internal decision must define the DecisionEnvelope/RuntimeResponseEnvelope mapping rather than rely on one permissive JSON object. The existing scaffold already preserves the public response field family.
- **Additional response metadata and validation.** Evidence, state, and audit fields add latency, payload, and implementation cost.
- **More negative testing.** Success-path coverage is insufficient; each route needs abstain, deny, error, stale, correction, and leak-safe cases.
- **Cross-root review burden.** Material changes touch app, contract, schema, policy, evidence, release, tests, security, and clients.
- **Static-edge verification work.** Efficient direct artifact delivery still needs digest, release, correction, and rollback support.
- **No convenience bypass.** Direct file/database/model reads and app-local policy shortcuts remain unavailable even during early development.
- **Acceptance cannot be inferred from implementation.** The repository may continue to use the scaffold while the ADR remains proposed.

### 10.3 Risks if the decision is not accepted or enforced

- the scaffold may evolve into ad-hoc route JSON without a client-facing contract;
- public clients may bypass the app or read released/internal stores without release/correction context;
- static artifact hosting may be mistaken for publication authority;
- DecisionEnvelope and RuntimeResponseEnvelope may drift or collapse;
- different clients may interpret `ABSTAIN`, `DENY`, and `ERROR` differently;
- model, graph, search, or renderer shortcuts may become public truth paths;
- review/admin routes may become self-approving mutation surfaces;
- a green smoke test may be cited as production or release readiness.

[Back to top](#top)

---

## 11. Alternatives Considered

<details>
<summary>Expand alternatives and disposition</summary>

| Alternative | Benefit | Why rejected |
|---|---|---|
| Keep the current scaffold indefinitely without accepting a target architecture | Lowest immediate implementation cost | A safe hold is valuable, but it does not define how substantive routes, evidence, policy, release, clients, and static edges converge |
| Let every app enforce its own trust rules | Local autonomy | The weakest app becomes the public boundary; denial vocabulary, evidence, and audit semantics drift |
| Use a shared `packages/` helper as the membrane | Reuse across apps | A library can be bypassed or imported inconsistently; it supports the membrane but is not the deployable boundary |
| Put the membrane in Explorer Web | Convenient for the map client | External clients bypass it; UI/rendering is not policy or release authority |
| Keep `apps/api/` and `apps/governed-api/` as public siblings | Route specialization | Creates parallel policy, evidence, denial, and audit surfaces |
| Use a reverse proxy, API gateway, or WAF as the entire membrane | Strong transport/exposure controls | Infrastructure cannot resolve EvidenceBundles, apply KFM semantic outcomes, or bind correction/release state by itself |
| Serve all static bytes through the WSGI app | Simple conceptual rule | Unnecessary bottleneck; a governed static edge is safe when release/integrity/correction requirements are met |
| Use static artifacts only and remove dynamic API | Efficient delivery | Cannot support governed evidence resolution, role-aware review, bounded AI, corrections, or dynamic finite outcomes |
| Expose model runtime directly | Fast AI integration | Bypasses evidence, policy, citation, release, provider-neutrality, and safe-error boundaries |
| Treat a DecisionEnvelope or the current hold scaffold as the permanent public response contract | Avoid mapping work | Collapses the distinct RuntimeResponseEnvelope boundary or mistakes a fail-closed hold for evidence, policy, release, and client-response semantics |
| Make RuntimeResponseEnvelope permissive enough to accept the current stub and arbitrary payloads | Easy migration | Weakens closed-schema governance and hides object-family drift |
| Per-domain public APIs | Domain ownership | Multiplies public membranes and makes cross-domain policy/evidence consistency harder |
| Defer all decisions until production | Avoid premature architecture | By then routes, clients, and data paths may already have hardened into competing authorities |

</details>

[Back to top](#top)

---

## 12. Migration & Backward Compatibility

Migration is incremental. This ADR does not authorize a broad rewrite or require changing the current safe scaffold in the documentation PR.

### 12.1 Phase 0 — preserve the fail-closed baseline

- Keep `/bootstrap`, `/layers`, and `/evidence` returning bounded RuntimeResponseEnvelope `ABSTAIN/NOT_IMPLEMENTED` holds.
- Preserve safe RuntimeResponseEnvelope `404`/`405` errors, route-manifest, import-boundary, path-literal, and fixture-negative tests.
- Preserve the current route registry as the rollback surface.
- Do not introduce live sources, model calls, public credentials, or deployment secrets.

### 12.2 Phase 1 — define the internal/public decision relationship for substantive routes

- Preserve the current v0.4 RuntimeResponseEnvelope contract/schema alignment and scaffold route tests.
- Review `DecisionEnvelope` and `RuntimeResponseEnvelope` contracts and schemas together when a route uses an internal decision.
- Decide whether the public envelope references or embeds a decision, and how obligations/reasons are represented.
- Define endpoint payload representation under the closed RuntimeResponseEnvelope schema.
- Add reciprocal contract notes, fixtures, validators, and mapping tests.
- Keep both object families distinct unless a successor ADR explicitly changes their meaning.

### 12.3 Phase 2 — add no-network governed dependencies

- Introduce accepted interfaces or mocks for policy, evidence, release/correction, and audit.
- Use deterministic public-safe fixtures.
- Prove `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` without external services.
- Replace fixture translation claims with tested evaluator/resolver behavior only when those components exist.
- Add safe reason/obligation vocabularies or registry references.

### 12.4 Phase 3 — graduate one route

Choose one bounded route, preferably a public-safe released layer descriptor or bootstrap posture that does not require AI or sensitive geometry.

The route PR must include:

- request and response shape;
- internal-to-public envelope mapping where applicable;
- evidence/release/policy fixtures;
- negative tests;
- no-leak behavior;
- client or consumer contract;
- metrics/audit posture; and
- rollback to the stub.

### 12.5 Phase 4 — integrate the normal client

- Replace Explorer Web placeholder scripts with a pinned, reproducible build only when a real slice exists.
- Centralize dynamic trust calls through a governed client.
- Verify released static artifacts before rendering.
- Render all four finite outcomes as distinct UI states.
- Do not treat popup text or tile properties as evidence.

### 12.6 Phase 5 — add review, export, and AI surfaces

- Add review retrieval with role, audit, and no-direct-file-mutation tests.
- Add exports with citation/release/correction metadata.
- Add model adapters only behind the API and only after evidence/citation/policy/receipt gates.
- Keep providers replaceable and client-invisible.

### 12.7 Phase 6 — deployment and operational hardening

- Verify ingress, auth, CORS, CSP, rate limits, egress, secret handling, cache policy, and static-edge integrity.
- Add redacted logs, metrics, tracing, alerting, and audit joins.
- Perform rollback and correction drills.
- Record required checks, review controls, and separation-of-duties enforcement.

### 12.8 Backward compatibility

- Existing route paths MAY be retained while handler semantics become versioned.
- The current `ABSTAIN/NOT_IMPLEMENTED` object is a RuntimeResponseEnvelope-shaped scaffold compatibility surface, not an accepted public v1 response or a substantive claim.
- A substantive envelope change requires an explicit version transition and client compatibility test.
- Static artifact URLs MAY remain stable when the release/integrity metadata remains verifiable and correction/rollback state is propagated.
- No compatibility alias may bypass the membrane or become a second dynamic authority.

### 12.9 Rollback

**Documentation rollback:** restore prior ADR blob `afe430ac64a60007f29589324dec60f1f9b34c4f`.

**Runtime rollback target:** the current route registry and `make_abstain_envelope()` RuntimeResponseEnvelope scaffold.

For each substantive route migration:

1. retain or be able to restore the prior stub handler;
2. disable the new handler by a reviewed reversible selection mechanism;
3. invalidate any unsafe cache or static pointer;
4. preserve audit and correction history;
5. record a rollback or forward-fix artifact in the accepted migration/release home; and
6. do not restore direct-store or direct-model access as a workaround.

[Back to top](#top)

---

## 13. Validation & Compliance

### 13.1 Current repository-native checks

| Check | Current command/surface | Current proof boundary |
|---|---|---|
| Governed API smoke | `make governed-api-smoke` | Runs all app-local tests, including route holds, fixture-only failure cases, and boundary guards; no production-flow proof |
| Live route envelope hold | [`test_abstain_routes.py`](../../apps/governed-api/tests/test_abstain_routes.py) | Requires the full RuntimeResponseEnvelope required field set and valid `ABSTAIN/NOT_IMPLEMENTED` shape for every registered route |
| Routing-error envelope hold | [`test_boundary_guards.py`](../../apps/governed-api/tests/test_boundary_guards.py) | Requires schema-shaped safe `ERROR` responses for `404` and `405` plus selected import, manifest, and internal-path guards |
| Fixture-only finite failures | [`test_api_failure_fixtures.py`](../../apps/governed-api/tests/test_api_failure_fixtures.py) | Checks deterministic `ABSTAIN`/`DENY`/`ERROR` fixture translations and unsafe-correlation non-reflection; not live policy/dependency behavior |
| Governed API import boundary | `make governed-api-verify` | Runs app tests and rejects direct MapLibre/Cesium/Ollama imports in the app |
| Cross-root boundary guards | `make boundary-guards`; `make boundary-guards-ci` | Runs selected control-plane, Explorer adapter, connector non-publisher, and app-boundary tests; not complete end-to-end flow proof |
| Runtime schema/fixture validation | `make schemas`; [runtime validator](../../tools/validators/validate_runtime_response_envelope.py) | Nine aggregate validator fixture families include runtime response and decision envelopes; shape and bounded precision semantics only |
| Contract/schema alignment | [`test_runtime_response_contract_alignment.py`](../../tests/contracts/test_runtime_response_contract_alignment.py) | Requires RuntimeResponseEnvelope prose and its precision profile to cover current schema fields and both `ANSWER` conditions |
| API CI | [`api-test.yml`](../../.github/workflows/api-test.yml) | Wires all-app smoke and focused route-check jobs. Exact result must be verified against the PR or commit run before being cited. |
| ADR coherence | `python tools/validators/validate_adr_index.py` | Checks ADR identity/index coherence; does not accept this ADR |
| ADR negative tests | `python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers` | Exercises validator rejection paths |
| Bounded API deny suite | `make deny-test` | Runs only the app-local boundary module; not a full policy, evidence, rights, sensitivity, release, or exfiltration matrix |
| Explorer build/test | package scripts | Build/test surface exists; governed transport and live API consumption remain held |

### 13.2 Acceptance gates for ADR-0004

ADR acceptance and implementation acceptance are related but separate. Acceptance SHOULD require reviewed evidence for each applicable gate.

| Gate | Requirement | Current status at snapshot |
|---|---|---|
| **A — identity and placement** | ADR ID/path unique; `apps/governed-api/` present; no parallel public API | **PARTIAL PASS** — identity/path/app confirmed; ADR still proposed |
| **B — contract separation** | DecisionEnvelope and RuntimeResponseEnvelope meanings, schemas, mapping, precision disclosure, and versioning are explicit | **PARTIAL** — distinct contracts exist; v0.4 contract/schema precision alignment is tested; a substantive-route internal decision mapping is not implemented |
| **C — finite runtime behavior** | Every substantive dynamic route emits validated `RuntimeResponseEnvelope` with one of four outcomes | **PARTIAL** — current three routes and routing errors emit the required runtime field family, but there is no substantive dynamic route |
| **D — evidence and citation** | Claim-bearing `ANSWER` resolves admissible evidence and validated citations | **HOLD** — no substantive `ANSWER` route |
| **E — policy, rights, sensitivity, and role** | Accepted evaluator/bundle, representative allow/deny/restrict/abstain cases, caller role enforcement | **HOLD** — fixture translations are not policy execution |
| **F — release, freshness, correction, withdrawal, rollback** | Response/static edge binds current release and disposition state | **HOLD** |
| **G — negative/security coverage** | Internal-path, sensitive, unreleased, stale, invalid, leaky error, direct model, review mutation, and empty-answer cases | **PARTIAL** — app tests cover routing, imports, internal literals, and fixture-negative shapes; material policy/evidence/release/security cases remain unimplemented |
| **H — client/static-edge conformance** | Explorer/external clients use governed dynamic/static contracts and verify integrity | **HOLD** — Explorer is buildable and fixture-first, but its GovernedClient has no network transport and no live API/static-edge conformance proof |
| **I — operational controls** | Auth, ingress, egress, secrets, logs, metrics, rate limits, CORS/CSP, deployment isolation verified | **UNKNOWN / HOLD** |
| **J — rollback and correction drill** | One route and one static artifact can be reverted/withdrawn without losing lineage | **HOLD** |
| **K — reviewed status transition** | ADR and index move together to `accepted` with named review evidence | **HOLD** |

### 13.3 Documentation validation for this revision

The documentation implementation must pass:

- complete baseline/no-loss review;
- KFM metadata parsing;
- one H1 and matching ADR ID;
- preserved major numbered section anchors;
- balanced fenced blocks, HTML, and `<details>`;
- resolved internal fragments;
- repository-relative link safety;
- no unsupported owner, route, status, CI, deployment, release, or publication claim;
- remote read-back and blob verification;
- branch comparison showing only the intended ADR path; and
- repository-native documentation and ADR checks when GitHub Actions completes.

> [!CAUTION]
> `200 OK` with an empty or unsupported success payload is not a trust-membrane pass. Neither is schema validity alone. Tests must assert the correct finite outcome, safe reason/state, evidence/release obligations, and absence of protected leakage.

[Back to top](#top)

---

## 14. Related ADRs and Docs

Unless a row says otherwise, the numbered ADRs below are currently effectively `proposed`.

| Reference | Relationship |
|---|---|
| [`ADR-0001`](./ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Default machine-schema home |
| [`ADR-0002`](./ADR-0002-contracts-vs-schemas-split.md) | Meaning/shape/policy/fixture/test/validator responsibility split |
| [`ADR-0003`](<./ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md>) | Singular policy authority root |
| [`ADR-0005`](./ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md) | Normal map-first client of the trust membrane |
| [`ADR-0008`](./ADR-0008-ollama-subordinate-to-governed-api.md) | Local model runtime subordination |
| [`ADR-0010`](./ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | Sensitive-domain fail-closed posture |
| [`ADR-0012`](./ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) | Source-edge non-publication boundary |
| [`ADR-0019`](./ADR-0019-ai-adapter-contract-and-finite-envelopes.md) | Provider-neutral AI adapter and finite envelope intent |
| [`ADR-0020`](./ADR-0020-abstain-is-a-first-class-decision.md) | First-class abstention semantics |
| [`ADR-0025`](./ADR-0025-public-client-never-reads-canonical-internal-stores.md) | No-direct-store rule and governed static-delivery edge |
| [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) | **Accepted** adoption record for the exact Directory Rules bytes; placement authority, not acceptance of ADR-0004 |
| [Directory Rules](../doctrine/directory-rules.md) | Responsibility-root placement and app-role doctrine |
| [Trust Membrane doctrine](../doctrine/trust-membrane.md) | Trust-warranty vocabulary; current document status remains draft |
| [Governed API architecture](../architecture/governed-api/README.md) | Human architecture landing page; current-state claims remain subordinate to repository evidence |
| [`apps/README.md`](../../apps/README.md) | Repository-grounded app-root inventory and maturity map |
| [`apps/governed-api/README.md`](../../apps/governed-api/README.md) | App-local responsibility boundary |
| [`GovernedClient.ts`](../../apps/explorer-web/src/adapters/GovernedClient.ts) | Fixture-only public-safe projection adapter; explicitly not a live network client |
| [`root.apps`](../../control_plane/root_registry.yaml) | Active machine projection of the adopted `apps/` responsibility-root placement |
| [`DecisionEnvelope` contract](../../contracts/runtime/decision_envelope.md) | Internal/runtime decision meaning |
| [`RuntimeResponseEnvelope` contract](../../contracts/runtime/runtime_response_envelope.md) | Client-facing runtime response meaning |
| [`precision_actually_used` contract](../../contracts/runtime/precision_actually_used.md) | Proposed schema-bound precision disclosure; v0.4 RuntimeResponseEnvelope prose and the alignment test cover the current conditional rule |
| [`DecisionEnvelope` schema](../../schemas/contracts/v1/runtime/decision_envelope.schema.json) | Current decision machine shape |
| [`RuntimeResponseEnvelope` schema](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | Intended client-facing machine shape |
| [`api-test` workflow](../../.github/workflows/api-test.yml) | Bounded API CI |
| [`policy-boundary-guards` workflow](../../.github/workflows/policy-boundary-guards.yml) | Path-scoped structural boundary checks; not exact-head runtime proof for this snapshot |
| [`schema-validation` workflow](../../.github/workflows/schema-validation.yml) | Shape/fixture CI for both runtime families |
| [`CODEOWNERS`](../../.github/CODEOWNERS) | GitHub review routing only |

[Back to top](#top)

---

## 15. Open Questions / NEEDS VERIFICATION

| ID | Question or gap | Required evidence / decision |
|---|---|---|
| **OQ-04-01** | Who owns and accepts this architectural decision? | Verified stewardship/decision record; CODEOWNERS alone is insufficient |
| **OQ-04-02** | How exactly does DecisionEnvelope become or feed RuntimeResponseEnvelope? | Reviewed contract/schema mapping and representative tests |
| **OQ-04-03** | How are endpoint-specific payloads represented under the closed RuntimeResponseEnvelope schema? | Contract and schema version decision |
| **OQ-04-04** | Which outcomes/fields are required for non-claim bootstrap/config responses? | Contract semantics and client tests |
| **OQ-04-05** | Which accepted policy evaluator, bundle, input contract, reason codes, and obligations govern runtime routes? | Policy source, tests, workflow, and decision artifacts |
| **OQ-04-06** | Which EvidenceRef resolver and EvidenceBundle store/interface support claim-bearing answers? | Implementation, fixtures, tests, and no-network proof |
| **OQ-04-07** | How are ReleaseManifest, correction, withdrawal, freshness, and rollback state joined to responses? | Accepted identifiers, adapters, schemas, and tests |
| **OQ-04-08** | What identity, authentication, authorization, and capability model applies to public, registered, steward, admin, and system callers? | Security/identity architecture and negative tests |
| **OQ-04-09** | What is the governed static-edge contract and integrity verification mechanism? | Release/static delivery profile, digest/signature policy, client/edge tests |
| **OQ-04-10** | Which Explorer Web client wrapper consumes dynamic envelopes and static release metadata? | Working client slice with pinned dependencies and tests |
| **OQ-04-11** | What ingress, egress, CORS, CSP, rate-limit, cache, secret, and network-isolation controls apply? | Infrastructure/config/deployment evidence |
| **OQ-04-12** | What redacted logs, metrics, traces, audit joins, and retention limits are allowed? | Observability/privacy contract and deployed evidence |
| **OQ-04-13** | What latency and response-size budgets apply to envelopes, evidence resolution, and mobile clients? | Performance budget and measured proof |
| **OQ-04-14** | What is the canonical public reason-code and obligation registry? | Accepted policy/control-plane location, schema, and tests |
| **OQ-04-15** | What is the audit/retention relationship among request, response, decision, policy, evidence, release, receipt, and correction IDs? | Identity/retention design and privacy review |
| **OQ-04-16** | Which branch-protection and independent-review controls are actually enforced? | Repository ruleset evidence; not inferred from CODEOWNERS |
| **OQ-04-17** | When may one route graduate from scaffolded `ABSTAIN` to `ANSWER`? | Closed §13.2 gates for that route packet |
| **OQ-04-18** | How should the Governed API architecture landing page and app README remain synchronized as implementation advances? | Separate scoped documentation task with current evidence |
| **OQ-04-19** | What future condition, if any, would justify an internal `apps/api/` service? | Concrete consumer and reviewed no-parallel-authority proof |
| **OQ-04-20** | Which rollback/forward-fix record home governs route-contract migrations? | Current migrations/release contracts and Directory Rules review |
| **OQ-04-21** | How will the aligned RuntimeResponseEnvelope and `precision_actually_used` contracts evolve with endpoint payloads and future versioning? | One reviewed meaning/shape decision, synchronized contract/schema/fixtures, compatibility evidence, and mapping tests before substantive `ANSWER` |

[Back to top](#top)

---

## Appendix A — Reason-code vocabulary

This is an illustrative grouping for design and tests. It is not a canonical registry and does not create policy authority.

<details>
<summary>Expand illustrative reason-code groups</summary>

### Routing and capability

- `route.not_found`
- `method.not_allowed`
- `capability.not_implemented`
- `capability.unavailable`
- `request.invalid`

### Lifecycle and release

- `public.internal_reference_denied`
- `release.unpublished`
- `release.stale`
- `release.withdrawn`
- `release.superseded`
- `catalog.not_closed`
- `proof.incomplete`
- `manifest.digest_missing`
- `rollback.target_missing`

### Evidence and citation

- `evidence.unresolved`
- `evidence.insufficient`
- `evidence.conflicted`
- `evidence.source_role_mismatch`
- `citation.unvalidated`
- `citation.missing_for_claim`

### Rights and sensitivity

- `rights.unknown`
- `rights.no_public_redistribution`
- `rights.attribution_missing`
- `sensitivity.archaeology_exact_denied`
- `sensitivity.rare_species_exact_denied`
- `sensitivity.living_person_denied`
- `sensitivity.dna_inference_denied`
- `sensitivity.critical_infrastructure_denied`
- `sensitivity.cultural_or_sacred_denied`
- `sensitivity.geometry_requires_transform`

### AI and runtime

- `ai.direct_client_forbidden`
- `ai.missing_evidence_or_citations`
- `ai.generated_as_observation_denied`
- `ai.out_of_scope`
- `adapter.fault`
- `resolver.fault`
- `schema.validation_failed`
- `runtime.envelope_invalid`

### Review and operations

- `review.direct_file_read_denied`
- `review.direct_file_mutation_denied`
- `review.role_required`
- `review.self_approval_denied`
- `freshness.stale`
- `audit.reference_missing`
- `not_for_life_safety`

</details>

Reason codes must be safe to expose at their intended surface. They must not encode protected facts, precise restricted locations, secrets, private prompts, raw evidence, internal file paths, or hidden reasoning.

[Back to top](#top)

---

## Appendix B — Anti-patterns this ADR forbids

<details>
<summary>Expand anti-pattern register</summary>

| Anti-pattern | Symptom | Required response |
|---|---|---|
| **Decision envelope relabeled as public response** | Current stub or internal policy object is documented as RuntimeResponseEnvelope without mapping | Hold route graduation; resolve contract/schema relationship |
| **Arbitrary payload in a closed envelope** | Handler adds undocumented fields to RuntimeResponseEnvelope | Version and update contract/schema/fixtures deliberately |
| **Empty `ANSWER`** | Route avoids `ABSTAIN` by returning success with empty/placeholder payload | Fail test; use status-appropriate outcome |
| **Public route reads canonical/internal store** | Client/API reads RAW, WORK, QUARANTINE, PROCESSED, registry, receipt, graph, search, source, or model store directly | Route through governed projection or deny |
| **Static path treated as publication** | Artifact is trusted because it is under a public URL or `data/published/` | Require release/integrity/correction/rollback verification |
| **Parallel public API** | `apps/api/` or another app serves independent trust-bearing routes | Deprecate/internalize or replace ADR through review |
| **Direct model client** | Browser calls provider/model/vector endpoint | Move adapter behind API; deny network path |
| **UI or renderer as policy** | Style filter, popup, tile attribute, or component state decides exposure | Apply policy and transforms before delivery |
| **Generated text as evidence** | Focus/AI answer lacks resolved evidence and citations | `ABSTAIN` or `DENY` |
| **Sensitive detail hidden only in presentation** | Exact protected data ships but is visually filtered | Redact/generalize/restrict before artifact generation |
| **Leaky `DENY` or `ERROR`** | Reason body reveals protected detail, prompt, secret, stack trace, or internal path | Return safe reason/audit reference |
| **Review console reads or writes files directly** | Browser retrieves/mutates receipts, reports, diffs, decisions, or release files | Governed role-gated API and separation of duties |
| **Worker publishes** | Worker/connector/pipeline writes public/release state as authority | Emit candidate/receipt; require governed promotion |
| **Smoke test used as release proof** | Green `api-test` badge cited as policy/security/release completion | Narrow claim to the exact tested scaffold |
| **App defines policy/schema/contract authority** | App-local copy diverges from owning root | Consume canonical interfaces; remove parallel definition |
| **Migration without rollback** | Handler/schema/client cutover has no stub fallback, cache invalidation, or lineage | Hold migration until rollback/forward-fix exists |
| **Transport security treated as semantic governance** | WAF/proxy/auth is claimed to resolve evidence or release state | Keep transport and KFM semantic gates distinct |
| **Permanent scaffold ambiguity** | Multiple docs call the scaffold both complete and unimplemented | Use repository-grounded status and explicit acceptance gates |

</details>

[Back to top](#top)

---

## Related docs

- [Canonical ADR index](./INDEX.md)
- [ADR authoring contract](./README.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [Trust Membrane doctrine](../doctrine/trust-membrane.md)
- [Governed API architecture](../architecture/governed-api/README.md)
- [Apps root README](../../apps/README.md)
- [Governed API app README](../../apps/governed-api/README.md)
- [Explorer fixture client](../../apps/explorer-web/src/adapters/GovernedClient.ts)
- [Root registry projection](../../control_plane/root_registry.yaml)
- [DecisionEnvelope contract](../../contracts/runtime/decision_envelope.md)
- [RuntimeResponseEnvelope contract](../../contracts/runtime/runtime_response_envelope.md)
- [`precision_actually_used` contract](../../contracts/runtime/precision_actually_used.md)
- [API test workflow](../../.github/workflows/api-test.yml)
- [Policy boundary workflow](../../.github/workflows/policy-boundary-guards.yml)
- [Schema-validation workflow](../../.github/workflows/schema-validation.yml)
- [Drift register](../registers/DRIFT_REGISTER.md)
- [Verification backlog](../registers/VERIFICATION_BACKLOG.md)

---

## Change Log

| Version | Date | Change |
|---|---|---|
| `v1.4` | 2026-09-12 | Reconciled the proposal with exact `main@49deb755`: refreshed the eight-lane/42-entry app inventory; confirmed the live scaffold's full RuntimeResponseEnvelope field set and safe routing errors; added fixture-only finite failure evidence; recorded v0.4 runtime-contract/precision alignment and its repository-owned test; removed stale exact-run claims; and preserved source `draft`, effective `proposed`, all substantive implementation holds, and the no-publication posture. |
| `v1.3` | 2026-08-13 | Reconciled the proposal with exact `main@52a6c7b`: adopted directory-placement evidence, the 38-entry Governed API scaffold, corrected `deny-test` scope, exact-head API/UI workflow results, the failed aggregate schema run with both runtime validators passing, RuntimeResponseEnvelope precision contract/schema drift, and Explorer's buildable but fixture-only client boundary. Preserved source `draft`, effective `proposed`, all implementation holds, and the no-publication posture. |
| `v1.2` | 2026-07-23 | Same-path repository-grounded modernization. Confirmed ADR identity/path and current Governed API scaffold; recorded three fail-closed routes and bounded tests; distinguished DecisionEnvelope from RuntimeResponseEnvelope; added governed static-delivery nuance, acceptance gates, current surface map, migration phases, rollback, verification backlog, and exact related ADRs; preserved decision status as proposed. |
| `v1.1` | 2026-05-15 | Tightened evidence boundary, schema-home posture, validation gates, migration discipline, finite outcomes, deny cases, and apps/api convergence guidance. |
| `v1` | 2026-05-10 | Initial proposal selecting `apps/governed-api/` as the trust membrane. |

---

**Last updated:** 2026-09-12 · **Decision status:** `proposed` · **Source metadata:** `draft` · **Path:** `docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md` · [Back to top](#top)
