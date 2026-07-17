<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/no-network/readme
title: tests/domains/atmosphere/no-network/ — Atmosphere Offline Execution and Egress-Denial Test Boundary
type: readme; directory-readme; domain-test-lane; atmosphere; no-network; hermetic-tests; egress-denial; non-authoritative
version: v0.2
status: draft; repository-grounded; direct-lane-readme-only; executable-tests-not-established; no-root-conftest-confirmed; blocker-not-established; pytest-markers-not-registered; no-network-fixtures-v0-2-confirmed; reusable-fixture-root-confirmed; runbook-draft; workflow-todo-only; make-test-excludes-lane; deterministic; credential-free; fail-closed; not-emergency-authority
owners: OWNER_TBD — Atmosphere steward · Test/QA steward · Security steward · Network/runtime steward · Connector steward · Pipeline steward · Fixture steward · Source steward · Policy steward · Evidence steward · Validator steward · API/UI/Map steward · Release steward · CI steward · Docs steward
created: 2026-07-05
updated: 2026-07-16
supersedes: v0.1 Atmosphere No-Network Test Lane README
policy_label: "public-review; tests; atmosphere; no-network; hermetic; egress-denied; credential-free; deterministic; source-role-aware; knowledge-character-aware; evidence-aware; deny-by-default; correction-aware; rollback-aware; no-source-authority; no-policy-authority; no-release-authority; not-emergency-authority"
current_path: tests/domains/atmosphere/no-network/README.md
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; Directory Rules tests responsibility-root placement;
  canonical tests root; Atmosphere test parent; no-network-fixtures sibling v0.2 on main after PR #1331;
  reusable Atmosphere fixture parent; Atmosphere no-network runbook; root pyproject with pytest but no
  marker registry or blocker plugin; no root tests/conftest.py; TODO-only domain-atmosphere workflow;
  Makefile test target excluding this lane; named-path probes finding no direct conftest.py,
  test_no_network.py, test_network_denial.py, or parent-level test_no_network.py; bounded search
  surfacing no executable blocker pattern / PROPOSED this lane own broad default-suite egress denial,
  blocker self-tests, transport coverage, credential and hidden-state denial, integration-tier
  separation, safe diagnostics, nonempty collection, CI artifacts, correction, rollback, and
  promotion expectations while fixture routing, provenance, digests, consumer backlinks, and public
  safety remain with no-network-fixtures / CONFLICTED or drift-prone detailed runbook prerequisites
  versus absent executable suite; broad no-network versus fixture-specific overlap; proposed marker,
  blocker, report, and CI names; Atmosphere/Air compatibility paths; runbook statements about
  egress-disabled CI without current workflow implementation / UNKNOWN exhaustive recursive inventory,
  package-local blockers, OS/container firewall controls, collected case count, integration jobs,
  retained reports, branch-protection significance, pass rates, coverage, mutation score, flake rate,
  release dependency, and production parity / NEEDS VERIFICATION accepted owners, CODEOWNERS,
  canonical blocker implementation, marker registry, loopback policy, integration/live-source tier,
  safe artifacts, required-check status, correction cascade, and rollback rehearsal
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: d0151870581168ab8cdd0ae0d852d902469ee3b4
  prior_blob: fd6e756370cee5eb6ec0a91773990e46d6c0083a
  direct_lane_files_confirmed:
    - tests/domains/atmosphere/no-network/README.md
  checked_absent_paths:
    - tests/domains/atmosphere/no-network/conftest.py
    - tests/domains/atmosphere/no-network/test_no_network.py
    - tests/domains/atmosphere/no-network/test_network_denial.py
    - tests/domains/atmosphere/test_no_network.py
    - tests/conftest.py
  related_repository_blobs:
    tests_root: 2c03b844ab8007453e091c3b24160a209e5214ff
    atmosphere_test_parent: 6474cc33c3bdd668fd8713e06e94f7dacda97b6b
    no_network_fixtures: aecabb196f0c88ff4d0fab2ada30f2ca4f79a703
    atmosphere_fixture_parent: 3046c1246e4f6999a1c1eae0040a47b49012d52f
    no_network_runbook: b4ee495b8f99a6e6c760c272d91d5d976c04d892
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    atmosphere_workflow: a3c6a21db798b02202c87f76bfba5f45c5f08c9b
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    pyproject: e3bd40e8e6ce14dfcde78ff5c09608095c3eca76
  merged_related_pr:
    number: 1331
    title: docs(tests): ground Atmosphere no-network fixture boundary
    state: closed-and-present-on-main
  bounded_inventory_note: >
    Direct reads, named-path probes, and indexed search establish only the checked snapshot. They do
    not prove permanent absence from history, forks, ignored files, generated workspaces, dynamic
    tests, package-local hooks, external CI controls, or later commits.
related:
  - ../README.md
  - ../no-network-fixtures/README.md
  - ../schema/README.md
  - ../source-role/README.md
  - ../knowledge-character/README.md
  - ../policy-deny/README.md
  - ../../../README.md
  - ../../../../fixtures/domains/atmosphere/README.md
  - ../../../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../connectors/
  - ../../../../pipelines/domains/atmosphere/
  - ../../../../pipeline_specs/atmosphere/
  - ../../../../tools/validators/domains/atmosphere/README.md
  - ../../../../policy/domains/atmosphere/README.md
  - ../../../../apps/governed-api/
  - ../../../../apps/explorer-web/
  - ../../../../.github/workflows/domain-atmosphere.yml
  - ../../../../Makefile
  - ../../../../pyproject.toml
  - ../../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, tests, atmosphere, no-network, offline, hermetic, egress, sockets, DNS, HTTP, cloud, tiles, geocoding, model-runtime, credentials, determinism, fixtures, CI, correction, rollback]
notes:
  - "This revision changes only this README; a generated provenance receipt is paired separately."
  - "The lane owns broad egress denial; fixture-specific governance remains with no-network-fixtures."
  - "The direct lane is README-only in bounded evidence; no executable blocker, marker registry, direct test, or root conftest was established."
  - "No test code, network hook, fixture payload, source record, schema, contract, policy, validator, connector, pipeline, workflow, lifecycle object, release object, alert, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Offline Execution and Egress-Denial Test Boundary

`tests/domains/atmosphere/no-network/`

> **Purpose.** Prove that the default Atmosphere test tier is hermetic, credential-free, deterministic, and unable to reach live HTTP, DNS, sockets, SDKs, databases, queues, maps, model runtimes, source systems, or mutable external state.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Inventory: README only" src="https://img.shields.io/badge/inventory-README__only-lightgrey">
  <img alt="Blocker: not established" src="https://img.shields.io/badge/blocker-not__established-orange">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Credentials: denied" src="https://img.shields.io/badge/credentials-denied-critical">
  <img alt="Authority: tests only" src="https://img.shields.io/badge/authority-tests__only-purple">
</p>

> [!IMPORTANT]
> **No-network means active denial, not merely avoiding calls in current examples.** A mature suite must install and self-test controls that make attempted outbound access visible and deterministic across synchronous, asynchronous, subprocess, browser, SDK, map, model, database, queue, telemetry, and background-task paths.

> [!CAUTION]
> **Current enforcement is not established.** The checked lane contains this README only. No direct test module, lane or root `conftest.py`, registered no-network marker, or executable blocker surfaced. A README, mock-only happy path, absent credential, TODO workflow, or zero-case collection is not proof of hermetic execution.

> [!WARNING]
> **KFM is not the official emergency, alerting, health, exposure, or life-safety authority.** Offline tests may verify advisory redirects and finite denial/abstention behavior. They must not make a fixture, cached response, model, or generated answer appear to be an official warning or medical instruction.

**Quick links:** [Purpose](#purpose-and-scope) · [Status](#current-evidence-and-maturity) · [Authority](#authority-and-directory-rules-basis) · [Sibling](#relationship-to-no-network-fixtures) · [Inventory](#confirmed-and-checked-inventory) · [Threats](#threat-model) · [Tiers](#test-tiers) · [Blocker](#network-blocker-contract) · [Matrix](#required-test-matrix) · [Hidden state](#credentials-proxies-caches-and-hidden-state) · [Processes](#subprocess-browser-worker-and-runtime-boundaries) · [Fixtures](#fixture-and-local-dependency-contract) · [Outcomes](#finite-outcomes-and-reason-codes) · [Diagnostics](#safe-diagnostics-artifacts-and-canaries) · [Lifecycle](#lifecycle-evidence-policy-and-release-boundary) · [Commands](#inventory-collection-and-execution) · [Failures](#failure-interpretation) · [CI](#ci-and-promotion-boundary) · [Maintenance](#maintenance-and-change-discipline) · [Plan](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#correction-and-rollback)

---

## Purpose and scope

The durable question for this lane is:

> Can the default Atmosphere test tier execute with every external transport denied, every credential absent, and every mutable upstream unavailable—without silently falling back, weakening policy, inventing evidence, or crossing lifecycle and publication boundaries?

A mature suite should prove that:

1. outbound HTTP, HTTPS, DNS, sockets, FTP/SFTP, WebSocket, cloud SDK, database, message-bus, map-resource, model-runtime, and source-client access is denied;
2. the blocker activates before network-capable code or import side effects execute;
3. forbidden attempts fail immediately with stable, safe diagnostics;
4. async clients, threads, subprocesses, workers, browsers, native libraries, and shutdown hooks cannot bypass denial;
5. proxies, profiles, keychains, metadata services, developer caches, and credentials are ignored or actively denied;
6. retries, mirrors, redirects, DNS fallback, alternate IP families, stale caches, and silent offline modes do not hide an attempt;
7. live-source checks are opt-in, separately marked, separately governed, and excluded from default CI;
8. schemas, policies, registries, fixtures, map assets, API payloads, and mock model responses resolve locally;
9. missing live data cannot become guessed data, stale truth, permissive policy, or an uncited answer;
10. denied dependencies produce test failure or finite `ABSTAIN`, `DENY`, or `ERROR` outcomes;
11. results do not vary with current weather, air quality, provider availability, VPN, locale, clock, or user profile;
12. reports contain safe reason codes and synthetic identifiers, not secrets, payloads, private hosts, or protected details;
13. failure paths cannot write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release authority;
14. a green result remains bounded test evidence, not source admission, evidence closure, policy approval, release approval, or production parity.

This lane does not own fixture payloads, source descriptors, connectors, pipelines, schemas, contracts, policy, evidence, release decisions, or public runtime code.

[Back to top](#top)

---

## Current evidence and maturity

### Safe conclusion

The repository documents a strong no-network posture, but executable Atmosphere egress denial is not established.

| Surface | Inspected status | Safe conclusion |
|---|---|---|
| This lane | **README-only** | Broad no-network intent exists; direct coverage is not established. |
| Lane `conftest.py` | **Not found** | No lane-local hook was established. |
| Root `tests/conftest.py` | **Not found** | No repository-wide pytest blocker was established by this probe. |
| Direct test modules | **Not found at named paths** | No direct blocker self-test was established. |
| Root pytest configuration | **Minimal and confirmed** | pytest is configured; markers and a blocker plugin are not registered. |
| [`no-network-fixtures/`](../no-network-fixtures/README.md) | **Repository-grounded v0.2 on `main`** | Owns fixture routing, provenance, digests, consumers, safety, and remote-reference rules. |
| [`fixtures/domains/atmosphere/`](../../../../fixtures/domains/atmosphere/README.md) | **README parent confirmed** | Payload validity and active consumers remain unverified. |
| No-network runbook | **Detailed draft** | Describes egress-disabled CI; most implementation prerequisites remain proposed. |
| `domain-atmosphere` workflow | **TODO-only** | Green execution cannot prove no-network behavior. |
| Root `make test` | **Excludes this lane** | Runs schema and contract tests only. |
| Blocker-pattern search | **No executable match surfaced** | Bounded search did not establish `pytest-socket`, raw-socket patching, or equivalent controls. |

### Truth labels

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current files, named-path probes, merged PR evidence, or bounded search. |
| `PROPOSED` | Recommended test, blocker, marker, artifact, reason code, or CI rule not implemented here. |
| `UNKNOWN` | Not resolved by inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not verified strongly enough for reliance or promotion. |
| `CONFLICTED` | Docs, lanes, or maturity claims overlap or disagree. |

### Maturity ladder

| Level | Requirement | Current posture |
|---|---|---|
| L0 | Lane contract exists. | **CONFIRMED** |
| L1 | Direct test object collects. | **NEEDS VERIFICATION** |
| L2 | Blocker intercepts a transport. | **NOT ESTABLISHED** |
| L3 | Blocker self-test rejects a known canary. | **NEEDS VERIFICATION** |
| L4 | HTTP, DNS, sockets, async, SDK, process, and browser paths are covered. | **NEEDS VERIFICATION** |
| L5 | Credentials, proxies, caches, profiles, and metadata services are denied. | **NEEDS VERIFICATION** |
| L6 | Live/integration tier is isolated. | **NEEDS VERIFICATION** |
| L7 | Safe report is retained. | **NEEDS VERIFICATION** |
| L8 | Failure blocks relevant promotion. | **UNKNOWN** |
| L9 | Current pass, coverage, flake, mutation, and rollback evidence exists. | **UNKNOWN** |

[Back to top](#top)

---

## Authority and Directory Rules basis

Directory Rules place enforceability proof under `tests/` and Atmosphere as a domain segment.

| Responsibility | Owning home | Relationship here |
|---|---|---|
| Broad Atmosphere egress denial | `tests/domains/atmosphere/no-network/` | This lane. |
| Fixture routing and provenance | `tests/domains/atmosphere/no-network-fixtures/` | Companion proof lane. |
| Reusable synthetic payloads | `fixtures/domains/atmosphere/` | Consumed locally; never copied here as a warehouse. |
| Connector implementation | `connectors/` | Blocked, stubbed, or excluded by tests. |
| Pipeline code/specs | `pipelines/domains/atmosphere/`, `pipeline_specs/atmosphere/` | Exercised offline; not implemented here. |
| Validator code | `tools/validators/` | Called locally; tests do not become validators. |
| Meaning and shape | `contracts/`, `schemas/` | Tested, never redefined here. |
| Policy | `policy/domains/atmosphere/` | Expected decisions tested; rules remain external. |
| Source admission | Source registry/admission roots | Synthetic references only; no activation. |
| Evidence/proofs | Governed evidence/proof roots | Synthetic references only. |
| Lifecycle data | Canonical `data/` phase roots | Writes denied; temporary simulation only. |
| Release/correction/rollback | `release/` and accepted contracts | Simulated only; no real decision or signature. |
| Public API/UI/map/AI | Governed application/runtime roots | Tested with local payloads; not implemented here. |
| CI | `.github/workflows/` | Invokes this lane when substantive; workflow code stays outside tests. |

[Back to top](#top)

---

## Relationship to `no-network-fixtures`

The two lanes are complementary:

| Lane | Owns | Does not own |
|---|---|---|
| `no-network/` | Active egress denial, transport coverage, credential denial, integration-tier separation, blocker self-tests, process/browser/runtime coverage, and hermetic CI. | Fixture corpus authority, manifest semantics, digests, consumer backlinks, or fixture provenance. |
| `no-network-fixtures/` | Locality, routing, provenance, digests, deterministic generation, public safety, remote-reference rejection, consumers, orphans, duplicates, and expected outcomes. | Broad socket/HTTP/SDK blocker implementation. |

A bounded proof requires both:

```text
safe local fixture
    + active multi-transport blocker
    + finite outcomes
    + safe retained evidence
    = bounded no-network proof
```

PR #1331 supplied the sibling v0.2 now present on `main`. This lane remains independently collectible and reviewable.

[Back to top](#top)

---

## Confirmed and checked inventory

```text
tests/domains/atmosphere/no-network/
└── README.md
```

Named probes did not find:

```text
tests/domains/atmosphere/no-network/conftest.py
tests/domains/atmosphere/no-network/test_no_network.py
tests/domains/atmosphere/no-network/test_network_denial.py
tests/domains/atmosphere/test_no_network.py
tests/conftest.py
```

Configuration evidence:

| File | Confirmed fact | Limit |
|---|---|---|
| `pyproject.toml` | pytest dependency and root `pythonpath`. | No markers or blocker plugin. |
| `Makefile` | `make test` runs `tests/schemas` and `tests/contracts`. | This lane is excluded. |
| `domain-atmosphere.yml` | Three named jobs. | Every job is a TODO echo. |
| No-network runbook | Defines desired egress-disabled behavior. | Implementation remains proposed. |
| Fixture parent | Documents reusable lanes. | Payload and consumer depth remain unverified. |

This inventory is bounded; it does not prove absence from history, ignored/generated workspaces, packages, or external CI.

[Back to top](#top)

---

## Threat model

Default tests must prevent:

- direct or transitive HTTP/HTTPS calls;
- DNS resolution and raw TCP/UDP sockets;
- FTP/SFTP, WebSocket, EventSource, and streaming clients;
- retries, redirects, mirrors, alternate hosts, proxy routing, and IP-family fallback;
- cloud metadata, token refresh, profile discovery, object storage, secret managers, and SDK calls;
- remote databases, caches, message buses, telemetry, and exception reporters;
- map styles, tiles, sprites, glyphs, imagery, terrain, geocoding, and analytics;
- remote model, embedding, vector, reranking, citation, and AI services;
- subprocess, shell, CLI, native library, browser, service-worker, thread, and background-task escape;
- remote schemas, JSON references, policies, registries, packages, fonts, or documentation;
- developer-local caches or services masking a forbidden call;
- silent fallback to stale, guessed, partial, or uncited data;
- writes to lifecycle, evidence, proof, receipt, release, or public paths after a failed dependency.

### Loopback and local sockets

`localhost`, Unix sockets, named pipes, and developer-local services are not automatically safe. Any allowed local service must be test-created, non-forwarding, explicitly tiered, and torn down by the owning test.

[Back to top](#top)

---

## Test tiers

| Tier | Network posture | Use |
|---|---|---|
| Tier 0 — pure/static | No network-capable initialization. | Contracts, schemas, pure functions, static guards. |
| Tier 1 — default hermetic | Active blocker; local fixtures only. | Local and pull-request CI. |
| Tier 2 — local service simulation | Explicit loopback/in-process service; no external forwarding. | Adapter and route tests. |
| Tier 3 — live integration | Explicit opt-in; separate workflow, rights, credentials, cost, and retention. | Upstream compatibility checks only. |
| Tier 4 — production monitoring | Outside this lane. | Operational watchers and health checks. |

No canonical marker names were found. Candidate markers such as `offline`, `no_network`, `local_service`, `integration`, and `live_source` are **PROPOSED** until registered.

[Back to top](#top)

---

## Network blocker contract

A future blocker should:

1. activate before network-capable test code runs;
2. be enabled by default;
3. fail if initialization or coverage checks fail;
4. require an explicit reviewed opt-out;
5. cover collection/import side effects where practical;
6. expose a version/configuration hash in safe reports;
7. use defense in depth: CI/container egress control, socket interception, runtime-client interception, and domain-client assertions;
8. reject unsupported transports rather than implicitly allowing them.

### Required self-tests

Use reserved synthetic destinations and prove denial for:

- raw socket and DNS;
- synchronous and asynchronous HTTP;
- WebSocket/streaming;
- cloud metadata and object-store SDK;
- database and message bus;
- map tile/style/geocoder;
- remote model/embedding/vector/citation service;
- subprocess CLI;
- browser/service worker;
- background thread/task;
- telemetry/error reporting.

No self-test should contact a real source or organization.

### Allowlist posture

Default: no external allowlist. Any allowed local endpoint must be necessary, test-created, loopback/in-process, non-forwarding, short-lived, manifested, and unable to grant source or publication authority.

[Back to top](#top)

---

## Required test matrix

| Concern | Required proof | Failure posture |
|---|---|---|
| Blocker activation | Known canary fails before domain use. | Suite error if absent or late. |
| Sync HTTP | Common clients denied. | Immediate failure. |
| Async HTTP | Async clients and pending tasks denied/drained. | Failure; no delayed escape. |
| DNS and sockets | IPv4/IPv6 and resolver paths covered. | Failure with redacted destination class. |
| Streaming | WebSocket/SSE/reconnect denied. | Failure. |
| SDK/cloud | Metadata, credentials, object stores, token refresh denied. | Failure or explicit error. |
| Database/queue | Remote DB, cache, and message bus denied. | Failure. |
| Map/browser | Tiles, styles, sprites, glyphs, geocoding, workers denied or local. | Failure. |
| Model/AI | Remote inference, embeddings, vector, citation, telemetry denied. | `ABSTAIN`, `DENY`, or `ERROR`; no invented answer. |
| Subprocess/native | Child processes and native clients cannot escape. | Failure. |
| Credentials | Tests run without real secrets or profiles. | Failure on access. |
| Proxies | Proxy variables cannot route traffic. | Failure. |
| Cache | Empty and populated cache results are governed. | Failure on undeclared dependency. |
| Retry/fallback | Redirects, mirrors, retries, stale cache, alternate IP remain denied. | Failure. |
| Integration isolation | Live checks excluded from default collection. | Failure if unmarked. |
| Nonempty collection | Required blocker self-tests collect. | Zero-case run fails. |
| Finite outcome | Denied dependency cannot become guessed truth. | Explicit framework/domain outcome. |
| No authority writes | No lifecycle, proof, receipt, release, or public writes. | Failure. |
| Safe diagnostics | No secrets, payloads, protected details, or current alerts. | Security failure. |

[Back to top](#top)

---

## Credentials, proxies, caches, and hidden state

Deny or isolate:

- API keys, tokens, cookies, connection strings, signed URLs, `.env`, and service accounts;
- AWS/GCP/Azure/Kubernetes/database/vendor profiles;
- OS keychains, credential helpers, SSH agents, netrc, browser profiles, and metadata services;
- proxy variables and proxy auto-discovery;
- developer caches, browser caches, downloaded responses, local databases, and running daemons;
- VPN state, DNS search domains, host aliases, machine names, account IDs, and user-home paths.

Required cases:

| Case | Expected result |
|---|---|
| No credentials | Default suite still runs. |
| Synthetic secret canary | Detected and never used. |
| Proxy variables set | External request still denied. |
| Cache empty | Local fixture remains sufficient. |
| Cache populated | Outcome unchanged unless cache is explicitly declared. |
| Metadata route available | Access denied. |
| Developer service on localhost | Unapproved connection denied. |
| Signed URL in fixture | Treated as inert text; never refreshed. |
| Private host in exception | Redacted. |

A test that passes only because a developer is authenticated, cached, or running a local service is not hermetic.

[Back to top](#top)

---

## Subprocess, browser, worker, and runtime boundaries

Python-level patches do not automatically cover:

- `subprocess`, shell, task runners, CLIs, and native executables;
- browser `fetch`, XHR, WebSocket, EventSource, workers, service workers, and resource loading;
- Node scripts and package tasks;
- asyncio tasks, thread pools, process pools, callbacks, retry timers, and shutdown telemetry;
- native libraries or other language runtimes.

A mature suite should scrub inherited environment, control working directories, enforce timeouts, drain/cancel background work, redact output, and assert no attempt occurs after the main test assertion.

[Back to top](#top)

---

## Fixture and local-dependency contract

This lane consumes local fixtures; it does not govern the fixture corpus.

| Dependency | Allowed when |
|---|---|
| Reusable Atmosphere fixture | Declared under `fixtures/domains/atmosphere/`, public-safe, and tied to a consumer. |
| Tiny inline value | Non-reusable, inspectable, synthetic, and documented. |
| Temporary directory | Test-scoped, cleaned, and outside canonical lifecycle roots. |
| Local schema/contract/policy | Read from repository paths; never fetched remotely. |
| In-process adapter | Deterministic and unable to forward externally. |
| Loopback server | Explicit tier, owned lifecycle, no forwarding, and not required for pure cases. |
| Local map asset | Declared, compact, public-safe, and free of remote references. |
| Mock model/runtime envelope | Deterministic and not evidence or release truth. |

Every URL, endpoint, `$ref`, style source, tile URL, model name, callback, citation, and attachment in a local fixture is untrusted input. Presence does not authorize retrieval.

[Back to top](#top)

---

## Finite outcomes and reason codes

| Layer | Outcomes | Meaning |
|---|---|---|
| Pytest | pass, fail, skip, error | Framework result only. |
| Blocker | `BLOCKED`, `BYPASS_DETECTED`, `UNSUPPORTED_TRANSPORT`, `ERROR` | Hermetic-control result. |
| Runtime | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Governed public envelope where applicable. |
| Integration | `AVAILABLE`, `UNAVAILABLE`, `DENIED`, `ERROR` | Upstream check only; never release approval. |

Proposed reason codes:

```text
ATMO_NET_BLOCKER_MISSING
ATMO_NET_BLOCKER_INIT_FAILED
ATMO_NET_BLOCKER_BYPASSED
ATMO_NET_UNSUPPORTED_TRANSPORT
ATMO_NET_HTTP_ATTEMPT
ATMO_NET_DNS_ATTEMPT
ATMO_NET_SOCKET_ATTEMPT
ATMO_NET_WEBSOCKET_ATTEMPT
ATMO_NET_CLOUD_SDK_ATTEMPT
ATMO_NET_DATABASE_ATTEMPT
ATMO_NET_MESSAGE_BUS_ATTEMPT
ATMO_NET_TILE_ATTEMPT
ATMO_NET_GEOCODE_ATTEMPT
ATMO_NET_MODEL_RUNTIME_ATTEMPT
ATMO_NET_SUBPROCESS_ATTEMPT
ATMO_NET_BROWSER_ATTEMPT
ATMO_NET_TELEMETRY_ATTEMPT
ATMO_NET_CREDENTIAL_ACCESS
ATMO_NET_PROXY_BYPASS
ATMO_NET_CACHE_DEPENDENCY
ATMO_NET_RETRY_BYPASS
ATMO_NET_BACKGROUND_ATTEMPT
ATMO_NET_LIVE_TEST_UNMARKED
ATMO_NET_ZERO_CASES
ATMO_NET_UNSAFE_DIAGNOSTIC
ATMO_NET_AUTHORITY_WRITE
ATMO_NET_NONDETERMINISTIC
```

These names are proposed. Codes and messages must not contain real hosts, tokens, account IDs, payloads, exact locations, living-person data, or alert text.

[Back to top](#top)

---

## Safe diagnostics, artifacts, and canaries

Proposed safe finding:

```json
{
  "case_id": "ATMO-NET-CASE-0001",
  "outcome": "BLOCKED",
  "reason_code": "ATMO_NET_HTTP_ATTEMPT",
  "transport": "https",
  "client_family": "synthetic-http-client",
  "test_tier": "default-hermetic",
  "redacted_destination": "<external-host>",
  "network_bytes_sent": 0
}
```

Reports may include synthetic IDs, test names, blocker version/config hash, transport/client family, finite outcomes, redacted destination class, attempt count, collection count, and duration.

Reports must exclude full URLs, query strings, auth headers, cookies, tokens, signed URLs, source payloads, private hosts, account IDs, user-home paths, exact protected locations, living-person data, current alert text, and unrestricted stack traces.

Use synthetic canaries for secret-like values, private hosts, remote references, tiles, model endpoints, metadata paths, and alert-shaped text. Assert they are absent from JUnit, logs, summaries, snapshots, screenshots, PR annotations, and retained artifacts.

[Back to top](#top)

---

## Lifecycle, evidence, policy, and release boundary

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Boundary | Required assertion |
|---|---|
| RAW | Default tests do not fetch or write raw payloads. |
| WORK/QUARANTINE | Failures use temporary sandboxes, not canonical phase paths. |
| PROCESSED | Fixtures do not become processed products. |
| CATALOG/TRIPLET | No-network success cannot create catalog or graph truth. |
| PUBLISHED | Tests never publish, sign, upload, tile, or serve release artifacts. |
| Evidence | Missing network cannot be replaced by generated evidence; resolve locally or abstain/deny. |
| Policy | Blocker success does not imply policy permission. |
| Release | Dry-run shape may be tested locally; no approval, signature, or promotion occurs. |
| Correction/Rollback | Blocker and expected-outcome changes preserve history and rollback targets. |

[Back to top](#top)

---

## Inventory, collection, and execution

### Inventory

```bash
find tests/domains/atmosphere/no-network -maxdepth 5 -type f | sort
find tests/domains/atmosphere -maxdepth 2 -name 'test_*.py' -type f | sort
find tests -maxdepth 2 -name 'conftest.py' -type f | sort
```

### Candidate blocker search

```bash
git grep -nE \
  'pytest[_-]?socket|disable[_-]?network|socket\.socket|create_connection|requests|httpx|aiohttp|urllib|WebSocket|telemetry' \
  -- tests .github pyproject.toml tools apps packages connectors pipelines
```

Text matches require review; they are not implementation proof.

### Collection and focused run

```bash
python -m pytest --collect-only -q tests/domains/atmosphere/no-network
python -m pytest -q tests/domains/atmosphere/no-network
```

A mature lane should fail when required self-tests collect zero cases.

### Proposed default-tier selection

```bash
python -m pytest -q tests/domains/atmosphere -m "not integration and not live_source"
```

Marker names are proposed until registered.

### Proposed safe report

```bash
mkdir -p artifacts/qa
python -m pytest -q tests/domains/atmosphere/no-network \
  --junitxml=artifacts/qa/atmosphere-no-network.xml
```

Artifact location and retention remain proposed.

### Repository context

```bash
make test
make validate
```

Current evidence says these commands do not collect this lane. Their success must not be reported as Atmosphere no-network coverage.

[Back to top](#top)

---

## Failure interpretation

| Signal | Safe interpretation | Do not claim |
|---|---|---|
| README exists | Lane contract exists. | Network is blocked. |
| No call observed | Current cases did not visibly call network. | Every transport is denied. |
| Credentials absent | Secrets were not supplied. | Credential lookup is blocked. |
| Mock passes | Named path used a mock. | Transitive/fallback egress is impossible. |
| HTTP patch passes | Covered HTTP path was denied. | DNS, sockets, subprocesses, browsers, SDKs, or native clients are covered. |
| Socket canary fails | One socket path was blocked. | Every runtime/process is hermetic. |
| Zero tests collect | Coverage gap. | Green suite. |
| TODO workflow passes | Scaffold executed. | No-network enforcement succeeded. |
| `make test` passes | Schema/contract targets passed. | This lane passed. |
| Cache returns data | Cache path worked. | A live attempt never occurred. |
| `ABSTAIN` returned | Unsupported answer was declined. | Evidence is complete. |
| Unsupported transport | Coverage gap/error. | Implicit allow. |
| Report includes host/token | Security failure. | Helpful detail. |

### What passing does not prove

A green no-network suite does not prove source admission, current upstream content, rights, freshness, live connector compatibility, production egress controls, complete native-runtime coverage, evidence sufficiency, policy permission, official advisory accuracy, model correctness, deployment safety, release approval, publication, cache invalidation, or operational rollback.

[Back to top](#top)

---

## CI and promotion boundary

Current evidence:

- `domain-atmosphere.yml` is TODO-only;
- `make test` excludes this lane;
- pytest markers and a blocker plugin are not registered;
- no retained no-network report or required-check status was established.

A substantive job should:

1. install pinned dependencies in a clearly separate build/bootstrap stage;
2. scrub credentials, proxies, profiles, caches, and developer state;
3. disable egress for the test phase;
4. assert blocker initialization and configuration;
5. assert nonzero collection and required self-tests;
6. run actual transport canaries based on repository dependencies;
7. run representative Atmosphere tests with local fixtures;
8. fail on unsupported transports and unmarked live checks;
9. scan reports for canaries, secrets, private hosts, alerts, and protected details;
10. retain a safe summary under an accepted policy;
11. block relevant promotion when hermetic validation is required.

A green result remains one prerequisite among identity, rights, sensitivity, evidence, validation, policy, review, release, correction, and rollback.

[Back to top](#top)

---

## Maintenance and change discipline

### Adding a network-capable dependency

- inventory every transport, initialization path, credential chain, retry, proxy, cache, and shutdown behavior;
- add blocker coverage and self-tests;
- add safe diagnostic redaction;
- confirm default collection remains no-network;
- record rollback.

### Adding a live-source check

- explain why local fixtures are insufficient;
- place it in a separate integration surface;
- define markers, workflow, credentials, rights, cost, cadence, retention, and owner;
- exclude it from default local/PR CI;
- prevent outputs from entering canonical lifecycle or release paths;
- distinguish upstream unavailability from product defect.

### Changing the blocker

Require old/new configuration hashes, coverage comparison, self-test comparison, consumer inventory, migration notes, artifact comparison, and rollback target.

### Moving tests

Move only with one primary responsibility, no duplicated active cases, updated collection/CI commands, corrected fixture/helper imports, backlink updates, compatibility notes, and rollback.

[Back to top](#top)

---

## Smallest sound implementation sequence

1. Inventory direct and parent-level Atmosphere tests.
2. Select the canonical blocker owner and path under Directory Rules.
3. Register default/integration markers.
4. Add raw-socket and synchronous-HTTP self-tests.
5. Add DNS and async coverage.
6. Add credential, proxy, cache, retry, and background-task cases.
7. Bind representative Atmosphere fixture consumers.
8. Add process/browser/map/SDK/database/queue/telemetry/model coverage based on actual dependencies.
9. Add safe reason codes and redacted reports.
10. Add a nonzero collection manifest.
11. Wire an egress-disabled CI test phase.
12. Make material failures block relevant promotion.
13. Align the runbook with actual commands and artifacts.
14. Rehearse correction and rollback.

A first proof slice should stay small: raw socket, sync HTTP, async HTTP, local fixture success, nonzero collection, safe diagnostics, and fail-closed CI.

[Back to top](#top)

---

## Definition of done

- [ ] Direct tests collect.
- [ ] Expected case count is nonzero and governed.
- [ ] Blocker owner/path is accepted.
- [ ] Initialization is fail-closed.
- [ ] Raw socket, DNS, sync HTTP, and async HTTP self-tests pass.
- [ ] Actual repository transports have explicit coverage.
- [ ] Process/browser/native/background paths are addressed.
- [ ] Credentials, proxies, profiles, caches, and metadata services are denied.
- [ ] Live checks are separately marked and excluded by default.
- [ ] Representative Atmosphere tests use local fixtures only.
- [ ] Retry/fallback/cache paths cannot bypass denial.
- [ ] Unsupported transports fail explicitly.
- [ ] Lifecycle, proof, receipt, release, and public writes are denied.
- [ ] Safe diagnostics and canary scans pass.
- [ ] Substantive CI runs with egress denied during the test phase.
- [ ] Safe artifacts are retained.
- [ ] Failures block relevant promotion.
- [ ] Owners/CODEOWNERS are accepted.
- [ ] Current pass, coverage, mutation, and flake evidence exists.
- [ ] Correction and rollback are rehearsed.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| ATMO-NET-01 | Which file/package owns the canonical blocker? | NEEDS VERIFICATION | Directory Rules decision and executable code. |
| ATMO-NET-02 | Repository-wide or selected-lane blocker? | OPEN | Test architecture decision and migration plan. |
| ATMO-NET-03 | What markers define default, local-service, integration, and live-source tiers? | NEEDS VERIFICATION | Registered pytest config and CI selection. |
| ATMO-NET-04 | Are loopback, Unix sockets, and named pipes denied by default? | OPEN | Threat model and blocker contract. |
| ATMO-NET-05 | Which transports are used by current dependencies? | NEEDS VERIFICATION | Dependency/import inventory. |
| ATMO-NET-06 | How are subprocesses and native libraries sandboxed? | NEEDS VERIFICATION | Tests and CI controls. |
| ATMO-NET-07 | How are browser, MapLibre, tile, geocoder, and worker requests intercepted? | NEEDS VERIFICATION | Browser/map harness. |
| ATMO-NET-08 | How are model, embedding, vector, and citation services denied? | NEEDS VERIFICATION | Runtime adapter inventory/tests. |
| ATMO-NET-09 | Are metadata services, profiles, proxies, and keychains denied? | NEEDS VERIFICATION | Environment-scrubbed tests. |
| ATMO-NET-10 | What cache contract is accepted? | OPEN | Cache policy and deterministic cases. |
| ATMO-NET-11 | What reason-code registry is accepted? | NEEDS VERIFICATION | Contract/schema/registry decision. |
| ATMO-NET-12 | What report shape and retention policy are accepted? | NEEDS VERIFICATION | QA artifact contract/workflow. |
| ATMO-NET-13 | How is nonzero collection enforced? | NEEDS VERIFICATION | Manifest or CI threshold. |
| ATMO-NET-14 | Which failures block promotion? | UNKNOWN | Promotion gate and branch protection. |
| ATMO-NET-15 | Do sibling READMEs retain reciprocal links and non-overlapping responsibilities? | NEEDS VERIFICATION | Backlink/responsibility audit. |
| ATMO-NET-16 | Does the runbook match actual commands and paths? | CONFLICTED / NEEDS VERIFICATION | Implementation and runbook revision. |
| ATMO-NET-17 | Who owns security review and live-test exceptions? | NEEDS VERIFICATION | CODEOWNERS/stewardship register. |
| ATMO-NET-18 | What are current metrics? | UNKNOWN | Reports and dashboards. |
| ATMO-NET-19 | Has rollback been rehearsed? | NEEDS VERIFICATION | Drill artifacts/logs. |
| ATMO-NET-20 | Are production egress controls aligned? | UNKNOWN | Deployment/network policy evidence. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Supports | Limits |
|---|---|---|
| Prior blob `fd6e756370cee5eb6ec0a91773990e46d6c0083a` | Existing scope and planning intent. | Does not prove enforcement. |
| `tests/README.md` blob `2c03b844...` | Canonical test root and mixed maturity. | Does not establish this lane's cases. |
| Atmosphere parent blob `6474cc33...` | Domain test placement and child map. | Parent remains scaffold-oriented. |
| Fixture sibling blob `aecabb19...` | Fixture-specific responsibility on current `main`. | Does not implement broad egress denial. |
| Fixture parent blob `3046c124...` | Reusable fixture responsibility. | Payload validity/consumers unverified. |
| Runbook blob `b4ee495b...` | Desired egress-disabled proof slice. | Many prerequisites proposed. |
| `pyproject.toml` blob `e3bd40e8...` | pytest config. | No markers/blocker plugin. |
| `Makefile` blob `4dc8cf63...` | Current test/validate commands. | Excludes this lane. |
| Workflow blob `a3c6a21d...` | Atmosphere job names. | TODO echoes only. |
| Named-path probes/search | No direct blocker/test at checked paths. | Bounded, not exhaustive. |
| Directory Rules blob `2affb080...` | Tests root and domain-segment placement. | Does not select a blocker library. |

Do not upgrade a runbook, marker name, mock, or TODO workflow into current enforcement truth.

[Back to top](#top)

---

## Correction and rollback

### v0.2 — 2026-07-16

- replaces the scaffold-oriented v0.1 README;
- records README-only maturity and absent named blocker/test/config paths;
- aligns with the merged fixture-governance sibling v0.2;
- separates broad egress denial from fixture-specific governance;
- adds threat, tier, blocker, transport, credential, cache, process, browser, model, diagnostic, CI, correction, and rollback contracts;
- changes no executable behavior.

### Correction path

Capture the exact claim and current file/test/config/workflow/artifact evidence; correct the truth label; preserve history; update parent/sibling indexes; update the generated receipt; and request materiality-appropriate QA, security, domain, CI, and release review.

### Rollback

Restore prior README blob `fd6e756370cee5eb6ec0a91773990e46d6c0083a`, remove the paired generated receipt, verify no test, blocker, marker, fixture, connector, pipeline, workflow, lifecycle, release, or public path changed, rerun Markdown/link/secret checks, and preserve the rollback commit.

Future executable rollback must also restore blocker configuration, markers, transport coverage, self-test manifest, environment scrub, fixture/local-service expectations, report contract, CI/required-check configuration, and consumer expectations.

---

## Maintainer summary

`tests/domains/atmosphere/no-network/` is the broad hermetic-execution proof boundary for Atmosphere tests. Current documentation is strong, but the direct lane is README-only, pytest has no registered no-network markers or blocker plugin, named conftest/test paths are absent, `make test` excludes the lane, and the Atmosphere workflow is TODO-only. The next sound change is a small active blocker proof slice—not a broad rewrite.

[Back to top](#top)
